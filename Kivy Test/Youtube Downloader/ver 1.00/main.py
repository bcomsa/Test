# -*- coding: utf8 -*-
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import AsyncImage
from kivy.uix.progressbar import ProgressBar
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.graphics import Rectangle, Color
import pafy, threading, os, sys

Builder.load_string('''
#:set HEIGHT_VIDEO_INFO 80
#:set HEIGHT_BUTTON 50

<YoutubeDisplayLayout>:
	size_hint: 1, None
	height: HEIGHT_VIDEO_INFO
<ScrollViewInfo@ScrollView>:
	canvas.before:
		Color:
			rgba: .5, .5, .5, .5
		Rectangle:
			pos: self.x + 1, self.y + 1
			size: self.width - 1, self.height - 1
<Root>:
	BoxLayout:
		size_hint: 3, 1
		orientation: 'vertical'
		Label:
			id: _info_lbl
			text: 'Nhập Link Youtube Vào Ô Bên Dưới'
		BoxLayout:
			TextInput:
				id: _text_input
			Button:
				size_hint: .15, 1
				text: 'Lấy Link'
				on_release: root.getLink()
			Button:
				id: _get_link_btn
				size_hint: .15, 1
				text: 'Dán'
				on_release: root.pasteClipboard()
			Button:
				size_hint: .15, 1
				text: 'Xóa Sạch'
				on_release: root.clearTextInput()
			Button:
				id: _get_link_btn
				size_hint: .15, 1
				text: 'Nơi Lưu'
				on_release: root.openPathChooser()
		ScrollView:
			size_hint: 1, 5
			do_scroll_x: False
			BoxLayout:
				id: _all_video_box
				orientation: 'vertical'
				size_hint: 1, None
				height: len(self.children) * HEIGHT_VIDEO_INFO
	BoxLayout:
		orientation: 'vertical'
		BoxLayout:
			BoxLayout:
				orientation: 'vertical'
				Label:
					size_hint: 1, .2
					text: 'Video'
				ScrollViewInfo:
					do_scroll_x: False
					BoxLayout:
						id: _video_download_box
						orientation: 'vertical'
						size_hint: 1, None
						height: len(self.children) * HEIGHT_BUTTON
			BoxLayout:
				orientation: 'vertical'
				Label:
					size_hint: 1, .2
					text: 'Audio'
				ScrollViewInfo:
					do_scroll_x: False
					BoxLayout:
						id: _audio_download_box
						orientation: 'vertical'
						size_hint: 1, None
						height: len(self.children) * HEIGHT_BUTTON
		BoxLayout:
			BoxLayout:
				orientation: 'vertical'
				Label:
					size_hint: 1, .2
					text: 'Danh Sách Download'
				ScrollViewInfo:
					do_scroll_x: False
					BoxLayout:
						id: _queue_download_box
						orientation: 'vertical'
						size_hint: 1, None
						height: len(self.children) * HEIGHT_BUTTON
''')

class YoutubeDisplayLayout(BoxLayout):
	def __init__(self, title='', duration='', thumbnail='', source_videos=None, source_audios=None, **kwargs):
		super(YoutubeDisplayLayout, self).__init__(**kwargs)
		info_box = BoxLayout(orientation='vertical')
		self.source_videos = source_videos
		self.source_audios = source_audios
		self.title = TextInput(text=title)  # text input canvas clear when its removed, make an error
		self.duration = Label(text=str(duration))
		info_box.add_widget(self.title)
		info_box.add_widget(self.duration)
		self.thumbnail = AsyncImage(source=thumbnail, size_hint=(.2, 1))
		self.add_widget(self.thumbnail)
		self.add_widget(info_box)
		self.register_event_type('on_click')
		with self.canvas.before:
			self.color = Color(rgba=(0, 0, 0, 0))
			self.rect = Rectangle(size=self.size, pos=self.pos)
		self.bind(pos=self.updateRect, size=self.updateRect)

	def select(self):
		self.unselectAll
		self.color.rgba = (1, 0, 0, .2)

	def unselect(self):
		self.color.rgba = (0, 0, 0, 0)

	def unselectAll(self):
		for child in self.parent.children:
			print child
			child.unselect()

	def updateRect(self, *args):
		self.rect.pos = self.pos
		self.rect.size = self.size

	def on_click(self):
		pass

	def on_touch_down(self, touch):
		if self.thumbnail.collide_point(*touch.pos):
			self.dispatch('on_click')
			return True
		return super(YoutubeDisplayLayout, self).on_touch_down(touch)

	def getTitle(self):
		return self.title.text

	def changeInfo(self, title, duration, thumbnail):
		self.title.text = u'Tên Video : ' + title
		self.duration.text = u'Độ Dài Video : ' + duration
		self.thumbnail.source = thumbnail

class YoutubeInfoDownload(BoxLayout):
	def __init__(self, **kwargs):
		super(YoutubeInfoDownload, self).__init__(**kwargs)
		self.orientation = 'vertical'
		self.name = Label()
		self.progress_status_lbl = Label()
		self.progress_bar = ProgressBar(max=100)
		self.register_event_type('on_click')
		self.add_widget(self.name)
		self.add_widget(self.progress_status_lbl)
		self.add_widget(self.progress_bar)

	def setFontSize(self, size):
		self.name.font_size = size
		self.progress_status_lbl.font_size = size

	def setName(self, name=''):
		self.name.text = name

	def setProgressStatus(self, progress_status=''):
		self.progress_status_lbl.text = progress_status

	def setProgressPercent(self, progress_percent=''):
		self.progress_bar.value = progress_percent

	def on_click(self):
		pass

	def on_touch_down(self, touch):
		if self.collide_point(*touch.pos):
			self.dispatch('on_click')
			return True
		return super(YoutubeInfoDownload, self).on_touch_down(touch)

class PathInputPopup(Popup):
	def __init__(self, **kwargs):
		super(PathInputPopup, self).__init__(**kwargs)
		box = BoxLayout(orientation='vertical')
		self.text_input = TextInput()
		self.submit_btn = Button(text='OK')
		self.submit_btn.bind(on_release=self.dismiss)
		box.add_widget(self.text_input)
		box.add_widget(self.submit_btn)
		self.content = box

	def getText(self):
		return self.text_input.text

	def setText(self, text):
		self.text_input.text = text

class Root(BoxLayout):
	def __init__(self, **kwargs):
		super(Root, self).__init__(**kwargs)
		self.path = os.getcwd()
		self.cur_youtube_obj = None
		self.text_input = self.ids['_text_input']
		self.info_lbl = self.ids['_info_lbl']
		self.all_video_box = self.ids['_all_video_box']
		self.audio_download_box = self.ids['_audio_download_box']
		self.video_download_box = self.ids['_video_download_box']
		self.queue_download_box = self.ids['_queue_download_box']
		self.all_thread_download = {}
		self.lock = threading.Lock()
		self.pathChooser = PathInputPopup(size_hint=(.5, .5), title='Chọn Nơi Lưu')
		self.pathChooser.setText(self.path)
		self.pathChooser.bind(on_dismiss=self.changePath)

	def pasteClipboard(self):
		self.text_input.paste()
		self.text_input.text += '\n'

	def clearTextInput(self):
		self.text_input.text = ''

	def openPathChooser(self):
		self.pathChooser.open()

	def changePath(self, *args):
		path = self.pathChooser.getText()
		if os.path.isdir(path):
			self.path = path
		else:
			self.info_lbl.text = u'Đường Dẫn Không Hợp Lệ'

	def getLink(self):
		#self.all_video_box.clear_widgets()
		with self.lock:
			threading.Thread(target=self.getYoutubeObjectThread,
								args=(self.text_input.text, self.getLinkCallback)
							).start()

	def getYoutubeObjectThread(self, url, callback):
		#url = "https://www.youtube.com/watch?v=JOX-krmWf8Q"
		self.info_lbl.text = u'Đang Lấy Dữ Liệu...'
		all_videos = []
		if 'watch' in url:
			all_videos = self.getYoutubeVideo(url)
		elif 'playlist' in url:
			all_videos = self.getYoutubePlaylist(url)
		else:
			self.info_lbl.text = u'Đường Dẫn Không Hợp Lệ'
			return

		try:
			if callback:
				callback(all_videos)
		except:
			self.info_lbl.text = u'Lỗi...'

	def getYoutubeVideo(self, url):
		all_videos = []
		try:
			for link in url.split('\n'):
				video = pafy.new(link)
				all_videos.append(video)
		except:
			pass
		return all_videos

	def getYoutubePlaylist(self, plurl):
		all_videos = []
		try:
			playlist = pafy.get_playlist(plurl)
			for video in playlist['items']:
				all_videos.append(video['pafy'])
		except:
			pass
		return all_videos

	def getLinkCallback(self, all_videos):
		for video in all_videos:
			obj = YoutubeDisplayLayout(title=video.title, duration=video.duration,
										thumbnail=video.thumb, source_videos=video.streams, source_audios=video.audiostreams)
			obj.bind(on_click=self.showDownload)
			self.all_video_box.add_widget(obj)
		self.info_lbl.text = u'Xong'

	def showDownload(self, obj):
		self.cur_youtube_obj = obj
		self.cur_youtube_obj.unselectAll()
		self.cur_youtube_obj.select()
		self.info_lbl.text = obj.getTitle().decode('utf-8')
		self.video_download_box.clear_widgets()
		self.audio_download_box.clear_widgets()
		for s in obj.source_videos:
			b = Button(text=s.resolution + '\n' + s.extension)
			b.halign = 'center'
			b.valign = 'middle'
			b.font_size = 12
			b.stream = s
			b.bind(on_release=self.download)
			self.video_download_box.add_widget(b)
		for s in obj.source_audios:
			b = Button(text=s.quality + '\n' + s.extension)
			b.halign = 'center'
			b.valign = 'middle'
			b.font_size = 12
			b.stream = s
			b.bind(on_release=self.download)
			self.audio_download_box.add_widget(b)

	def download(self, obj):
		threading.Thread(target=self.downloadThread, args=(obj, )).start()

	def downloadThread(self, obj):
		id = threading.current_thread().ident
		download_info_btn = YoutubeInfoDownload()
		download_info_btn.setName(self.cur_youtube_obj.getTitle().decode('utf-8')[:15])
		download_info_btn.setFontSize(12)
		self.all_thread_download[id] = [False, download_info_btn]

		def callback(*arg):
			with self.lock:
				self.all_thread_download[id][0] = True
				self.queue_download_box.remove_widget(download_info_btn)
		download_info_btn.bind(on_click=callback)

		self.queue_download_box.add_widget(download_info_btn)
		try:
			obj.stream.download(filepath=self.path + os.sep + self.cur_youtube_obj.getTitle().decode('utf-8') + '.' + obj.stream.extension,
								quiet=True, callback=self.downloadCallback)
			download_info_btn.setProgressStatus('Xong')
			#self.queue_download_box.remove_widget(download_info_btn)
		except:
			download_info_btn.setProgressStatus('Lỗi')

	def downloadCallback(self, *args):
		download_info_btn = self.all_thread_download[threading.current_thread().ident][1]
		with self.lock:
			if self.all_thread_download[threading.current_thread().ident][0]:
				sys.exit()
		percent = int(args[2] * 100)
		total_size = args[0]/(1024.0*1024)
		cur_size = args[1]/(1024.0*1024)
		progress_mbyte = '%.2fMB/%.2fMB' % (cur_size, total_size)
		download_info_btn.setProgressStatus(progress_mbyte)
		download_info_btn.setProgressPercent(percent)

class YoutubeDownloadApp(App):
	def build(self):
		Window.size = (1024, 400)
		return Root()

if __name__ == '__main__':
	YoutubeDownloadApp().run()
