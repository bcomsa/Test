# -*- coding: utf8 -*-
from kivy.garden.filebrowser import FileBrowser
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.videoplayer import VideoPlayer
from kivy.properties import ListProperty, StringProperty
from kivy.app import App
from kivy.lang import Builder
import os

Builder.load_string('''
<VideoPlayerBox>:
	orientation: 'vertical'
	ActionBar:
		pos_hint: {'top':1}
		ActionView:
			use_separator: True
			ActionPrevious:
				title: 'Action Bar'
				with_previous: False
			ActionOverflow:
			ActionButton:
				text: 'Btn0'
				icon: 'atlas://data/images/defaulttheme/audio-volume-high'
			ActionButton:
				text: 'Btn1'
			ActionButton:
				text: 'Btn2'
			ActionButton:
				text: 'Btn3'
			ActionButton:
				text: 'Btn4'
			ActionGroup:
				text: 'Group1'
				ActionButton:
					text: 'Btn5'
				ActionButton:
					text: 'Btn6'
				ActionButton:
					text: 'Btn7'
	FileBrowser:
		id: fileChooser
		rootpath: root.ROOTPATH
		filters: root.EXTENTION
		on_selection: root.play_video(self.selection)
''')
class VideoPlayerBox(BoxLayout):
	EXTENTION = ListProperty(['*.asf', '*.avi', '*.3gp', '*.mp4', '*.mov', '*.flv', '*.mkv', '*.webm', '*.mxf', '*.ogg'])
	ROOTPATH = StringProperty('C:\Users\pc') if 'nt' in os.name\
								else StringProperty('/home/vuquangtam')

	def play_video(self, selection):
		try:
			filename = selection[0]
			self.videoPlayer = VideoPlayer(source=filename, state='play', thumbnail='data/images/image-loading.gif')
			self.popup = Popup(content=self.videoPlayer, size_hint=(.9, .9), title=filename)
			self.popup.bind(on_dismiss=self.stop_video)
			self.popup.open()
		except:
			pass

	def stop_video(self, obj):
		self.videoPlayer.state = 'stop'
		del self.ids['fileChooser'].selection[:]

class VideoPlayerApp(App):
	def build(self):
		return VideoPlayerBox()

if __name__ == '__main__':
	VideoPlayerApp().run()
