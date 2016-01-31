# Chapter 11: Responsive Interfaces, Using Threads and Timers
# Recipe 5: Capturing Output
#
import wx
import wx.stc as stc
import threading
import subprocess

class ProcessThread(threading.Thread):
    """Helper Class for OutputWindow to run a subprocess in
    a separate thread and report its output back 
    to the window.
    """
    def __init__(self, parent, command, readblock=4096):
        """
        @param parent: OutputWindow instance
        @param command: Command line command
        @param readblock: amount to read from stdout each read
        """
        assert hasattr(parent, 'AppendUpdate')
        assert readblock > 0
        super(ProcessThread, self).__init__()

        # Attributes
        self._proc = None
        self._parent = parent
        self._command = command
        self._readblock = readblock

        # Setup
        self.setDaemon(True)

    def run(self):
        # Suppress popping up a console window
        # when running on windows
        if subprocess.mswindows:            
            suinfo = subprocess.STARTUPINFO()
            try:
                from win32process import STARTF_USESHOWWINDOW
                suinfo.dwFlags |= STARTF_USESHOWWINDOW
            except ImportError:
                # Give up and try hard coded value 
                # from Windows.h
                suinfo.dwFlags |= 0x00000001
        else:
            suinfo = None
        
        try:
            # Start the subprocess
            outmode = subprocess.PIPE
            errmode = subprocess.STDOUT
            self._proc = subprocess.Popen(self._command,
                                          stdout=outmode,
                                          stderr=errmode,
                                          shell=True,
                                          startupinfo=suinfo)
        except OSError, msg:
            self._parent.AppendUpdate(unicode(msg))
            return

        # Read from stdout while there is output from process
        while True:
            self._proc.poll()
            if self._proc.returncode is None:
                # Still running so check stdout
                txt = self._proc.stdout.read(self._readblock)
                if txt:
                    # Add to UI's update queue
                    self._parent.AppendUpdate(txt)
            else:
                break

class OutputWindow(stc.StyledTextCtrl):
    def __init__(self, parent):
        super(OutputWindow, self).__init__(parent)

        # Attributes
        self._mutex = threading.Lock()
        self._updating = threading.Condition(self._mutex)
        self._updates = list()
        self._timer = wx.Timer(self)
        self._threads = list()

        # Setup
        self.SetReadOnly(True)

        # Event Handlers
        self.Bind(wx.EVT_TIMER, self.OnTimer)

    def __del__(self):
        if self._timer.IsRunning():
            self._timer.Stop()

    def AppendUpdate(self, value):
        """Thread safe method to add updates to UI"""
        self._updating.acquire()
        self._updates.append(value)
        self._updating.release()

    def OnTimer(self, event):
        """Check updates queue and apply to UI"""
        # Check Thread(s)
        tlist = list(self._threads)
        for idx, thread in enumerate(tlist):
            if not thread.isAlive():
                del self._threads[idx]

        # Apply pending updates to control
        ind = len(self._updates)
        if ind:
            # Flush update buffer
            self._updating.acquire()
            self.SetReadOnly(False)
            txt = ''.join(self._updates[:])
            self.AppendText(txt)
            self.GotoPos(self.GetLength())
            self._updates = list()
            self.SetReadOnly(True)
            self._updating.release()

        if not len(self._threads):
            self._timer.Stop()

    def StartProcess(self, command, blocksize=4096):
        """Start command. Blocksize can be used to control
        how much text must be read from stdout before window
        will update.
        """
        procthread = ProcessThread(self, command, blocksize)
        procthread.start()
        self._threads.append(procthread)
        if not self._timer.IsRunning():
            self._timer.Start(250)

