# Chapter 11: Responsive Interfaces, Using Threads and Timers
# Recipe 4: Using Timers
#
import wx

#---- Recipe Code ----#

class TimerTaskBase(object):
    """Defines interface for long running task
    state machine.
    """
    TASK_STATE_PENDING, \
    TASK_STATE_RUNNING, \
    TASK_STATE_COMPLETE = range(3)
    def __init__(self):
        super(TimerTaskBase, self).__init__()

        # Attributes
        self._state = TimerTaskBase.TASK_STATE_PENDING

    #---- Interface ----#

    def ProcessNext(self):
        """Do next iteration of task
        @note: must be implemented by subclass
        """
        raise NotImplementedError

    def InitTask(self):
        """Optional override called before task 
        processing begins
        """
        self.SetState(TimerTaskBase.TASK_STATE_RUNNING)

    #---- Implementation ----#

    def GetState(self):
        return self._state

    def SetState(self, state):
        self._state = state

class TimerTaskMixin(object):
    """Mixin class for a wxWindow object to use timers
    for running long task. Must be used as a mixin with
    a wxWindow derived class!
    """
    def __init__(self):
        super(TimerTaskMixin, self).__init__()

        # Attributes
        self._task = None
        self._timer = wx.Timer(self)

        # Event Handlers
        self.Bind(wx.EVT_TIMER, self.OnTimer, self._timer)
        
    def __del__(self):
        # Make sure timer is stopped
        self.StopProcessing()

    def OnTimer(self, event):
        if self._task is not None:
            self._task.ProcessNext()
            state = self._task.GetState()
            if state == self._task.TASK_STATE_COMPLETE:
                self._timer.Stop()

    def StartTask(self, taskobj):
        assert not self._timer.IsRunning(), \
               "Task already busy!"
        assert isinstance(taskobj, TimerTaskBase)
        self._task = taskobj
        self._task.InitTask()
        self._timer.Start(100)

    def StopProcessing(self):
        if self._timer.IsRunning():
            self._timer.Stop()

#---- End Recipe Code ----#

#---- Sample Application ----#

SAMPLEDNA = """
atggctaaactgaccaagcgcatgcgtgttatccgcgagaaagttgatgcaaccaaacag 
tacgacatcaacgaagctatcgcactgctgaaagagctggcgactgctaaattcgtagaa 
agcgtggacgtagctgttaacctcggcatcgacgctcgtaaatctgaccagaacgtacgt 
ggtgcaactgtactgccgcacggtactggccgttccgttcgcgtagccgtatttacccaa
"""

class DNATranscriberTask(TimerTaskBase):
    """Simple sample task that transcribes dna to rna.
    This is just an example usage of our recipes framework
    this task could easily be done very quickly with using
    the str.replace method. It was done this way just because
    it makes a good simple example for understanding how to break a
    bigger task into several smaller steps.
    """
    def __init__(self, input, outfunct):
        """
        @param input: string of DNA data
        @param outfunct: callable(string) for out put
        """
        super(DNATranscriberTask, self).__init__()

        # Attributes
        input = ''.join(input.split()) # remove whitespace
        self.inputs = list(input)
        self.outfunct = outfunct

    def ProcessNext(self):
        if len(self.inputs) > 0:
            seq = self.inputs.pop(0)
            trans = dict(t='u', T='U')
            outval = trans.get(seq, seq)
            self.outfunct(outval) # return incremental data
        if not len(self.inputs):
            self.SetState(DNATranscriberTask.TASK_STATE_COMPLETE)

class TimerApp(wx.App):
    def OnInit(self):
        self.frame = TimerTaskFrame(None,
                                    title="Slow DNA Transcriber")
        self.frame.Show()
        return True

class TimerTaskFrame(wx.Frame):
    """Main application window"""
    def __init__(self, *args, **kwargs):
        super(TimerTaskFrame, self).__init__(*args,
                                             **kwargs)

        # Attributes
        self.panel = TimerTaskPanel(self)

        # Layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.panel, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.SetInitialSize((400, 300))

class TimerTaskPanel(wx.Panel, TimerTaskMixin):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        TimerTaskMixin.__init__(self)

        # Attributes
        self.input = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.input.SetValue(SAMPLEDNA)
        self.output = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.start = wx.Button(self, label="Transcribe to RNA")

        # Setup
        self.__DoLayout()

        # Event Handlers
        self.Bind(wx.EVT_BUTTON, self.OnButton)

    def __DoLayout(self):
        vsizer = wx.BoxSizer(wx.VERTICAL)
        hsizer = wx.BoxSizer(wx.HORIZONTAL)

        vsizer.Add(self.input, 1, wx.EXPAND)
        hsizer.AddStretchSpacer()
        hsizer.Add(self.start, 0, wx.ALIGN_CENTER)
        hsizer.AddStretchSpacer()
        vsizer.Add(hsizer, 0, wx.EXPAND)
        vsizer.Add(self.output, 1, wx.EXPAND)

        self.SetSizer(vsizer)

    def UpdateOutput(self, value):
        self.output.AppendText(value)

    def OnButton(self, event):
        input = self.input.GetValue()
        task = DNATranscriberTask(input, self.UpdateOutput)
        self.StartTask(task)

if __name__ == '__main__':
    app = TimerApp(False)
    app.MainLoop()
