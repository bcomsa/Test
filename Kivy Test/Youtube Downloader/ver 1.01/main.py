# -*- coding: utf8 -*-
# Author : Tam Vu Quang
# Description:
#  a GUI wrapper of Youtube download
#  using pafy module, which can get metadata and download youtube
#  from video url or playlist url
#  This code uses thread and callback technique (which is new to me)

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import AsyncImage
from kivy.uix.progressbar import ProgressBar
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.graphics import Rectangle, Color
import pafy, threading, os, sys, subprocess, requests, bs4, gc

#from pympler.tracker import SummaryTracker
#tracker = SummaryTracker()

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
<TitleLabel@Label>:
	canvas.before:
		Color:
			rgba: .5, .5, 0, .5
		Rectangle:
			pos: self.x + 1, self.y + 1
			size: self.width - 1, self.height - 1

<Root>:
	BoxLayout:
		size_hint: 3, 1
		orientation: 'vertical'
		Label:
			id: _status_lbl
		BoxLayout:
			size_hint: 1, .8
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
				id: _all_videos_box
				orientation: 'vertical'
				size_hint: 1, None
				height: len(self.children) * HEIGHT_VIDEO_INFO
		ChangeNameBar:
			id: _change_video_name_input
			size_hint: 1, .8

	BoxLayout:
		orientation: 'vertical'
		BoxLayout:
			orientation: 'vertical'
			size_hint: 1, .5
			TitleLabel:
				size_hint: 1, .5
				text: 'Tải Tất Cả'
			GridLayout:
				cols: 2
				Button:
					text: 'Video 720p'
					font_size: 12
					on_release: root.downloadAll('video', '1280x720')
				Button:
					text: 'Video 360p'
					font_size: 12
					on_release: root.downloadAll('video', '640x360')
				Button:
					text: 'Video 240p'
					font_size: 12
					on_release: root.downloadAll('video', '320x240')
				Button:
					text: 'Audio 128kbs'
					font_size: 12
					on_release: root.downloadAll('audio', '128k')
		BoxLayout:
			orientation: 'vertical'
			TitleLabel:
				size_hint: 1, .2
				text: 'Tải Từng Mục'
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
				TitleLabel:
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

MPC_PATH = r'C:\Program Files\K-Lite Codec Pack\MPC-HC\mpc-hc.exe'
print MPC_PATH

class YoutubeDisplayLayout(BoxLayout):
	''' layout display the infomation of video'''
	def __init__(self, title='', duration='', author='', view_count='',
				 thumbnail='', source_videos=None, source_audios=None, **kwargs):
		super(YoutubeDisplayLayout, self).__init__(**kwargs)
		self.source_videos = source_videos  # contain all source pafy video
		self.source_audios = source_audios  # contain all source pafy audio
		self.title = Label(text=title)
		self.duration = Label(text=u'Độ Dài : ' + str(duration))
		self.author = Label(text=u'Người Đăng : ' + author)
		self.view_count = Label(text=u'Lượt Xem : ' + str(view_count))

		other_info_box = BoxLayout()
		other_info_box.add_widget(self.duration)
		other_info_box.add_widget(self.author)
		other_info_box.add_widget(self.view_count)

		info_box = BoxLayout(orientation='vertical')
		info_box.add_widget(self.title)
		info_box.add_widget(other_info_box)

		self.open_box = BoxLayout(orientation='vertical', size_hint=(.2, 1))
		open360p_btn = Button(text='360p')
		open360p_btn.bind(on_release=self.open360pCallback)
		open240p_btn = Button(text='240p')
		open240p_btn.bind(on_release=self.open240pCallback)
		self.open_box.add_widget(open360p_btn)
		self.open_box.add_widget(open240p_btn)

		self.thumbnail = AsyncImage(source=thumbnail, size_hint=(.2, 1))
		self.add_widget(self.thumbnail)
		self.add_widget(info_box)
		self.add_widget(self.open_box)

		self.register_event_type('on_click')  # register an event for the layout
		with self.canvas.before:  # define the selection animation
			self.color = Color(rgba=(0, 0, 0, 0))
			self.rect = Rectangle(size=self.size, pos=self.pos)
		self.bind(pos=self.updateRect, size=self.updateRect)

	def open360pCallback(self, *args):
		url = ''
		for s in self.source_videos:
			if s.resolution == '640x360':
				url = '"' + s.url + '"'
				break
		threading.Thread(target=subprocess.call, args=([MPC_PATH, url], )).start()

	def open240pCallback(self, *args):
		url = ''
		for s in self.source_videos:
			if s.resolution == '320x240':
				url = '"' + s.url + '"'
				break
		threading.Thread(target=subprocess.call, args=([MPC_PATH, url], )).start()

	def select(self):
		self.unselectAll
		self.color.rgba = (1, 0, 0, .2)

	def unselect(self):
		self.color.rgba = (0, 0, 0, 0)

	def unselectAll(self):  # unselect all the layout in video box
		for child in self.parent.children:
			child.unselect()

	def updateRect(self, *args):  # bind rect to self
		self.rect.pos = self.pos
		self.rect.size = self.size

	def on_click(self):  # an event is registered
		pass

	def on_touch_down(self, touch):  # define for the on_click event
		if self.collide_point(*touch.pos) and not self.open_box.collide_point(*touch.pos):
			self.dispatch('on_click')
			return True
		return super(YoutubeDisplayLayout, self).on_touch_down(touch)

	def getTitle(self):  # implicit method
		return self.title.text

	def setTitle(self, value):  # implicit method
		self.title.text = value

class YoutubeInfoDownload(BoxLayout):
	'''layout display all infomation about download progression'''
	def __init__(self, **kwargs):
		super(YoutubeInfoDownload, self).__init__(**kwargs)
		self.padding = 5
		self.name = Label()
		self.progress_status_lbl = Label()
		self.progress_bar = ProgressBar(max=100)
		self.delete_button = Button(text='Xóa')
		download_box = BoxLayout(orientation='vertical')
		download_box.add_widget(self.name)
		download_box.add_widget(self.progress_status_lbl)
		download_box.add_widget(self.progress_bar)
		self.add_widget(download_box)
		self.add_widget(self.delete_button)

	def setFontSize(self, size):  # implicit method
		self.name.font_size = size
		self.progress_status_lbl.font_size = size

	def setName(self, name=''):  # implicit method
		self.name.text = name

	def setProgressStatus(self, progress_status=''):  # implicit method
		self.progress_status_lbl.text = progress_status

	def setProgressPercent(self, progress_percent=''):  # implicit method
		self.progress_bar.value = progress_percent

	def setDeleteButtonCallback(self, func):  # implicit method
		self.delete_button.bind(on_release=func)

class PathInputPopup(Popup):
	'''a popup with the ok button'''
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

class ChangeNameBar(BoxLayout):
	def __init__(self, **kwargs):
		super(ChangeNameBar, self).__init__(**kwargs)
		self.input = TextInput()
		to_ascii_btn = Button(text='Không Dấu', font_size=14)
		to_ascii_btn.bind(on_release=self.toAscii)
		to_upper_btn = Button(text='Chữ Hoa', font_size=14)
		to_upper_btn.bind(on_release=self.toUpper)
		to_lower_btn = Button(text='Chữ Thường', font_size=14)
		to_lower_btn.bind(on_release=self.toLower)
		to_title_form_btn = Button(text='Chữ Đầu In Hoa', font_size=14)
		to_title_form_btn.bind(on_release=self.toTitleForm)
		button_box = GridLayout(cols=2, size_hint=(.4, 1))
		button_box.add_widget(to_ascii_btn)
		button_box.add_widget(to_title_form_btn)
		button_box.add_widget(to_upper_btn)
		button_box.add_widget(to_lower_btn)
		self.add_widget(self.input)
		self.add_widget(button_box)

	def setText(self, value):
		self.input.text = value

	def getText(self):
		return self.input.text

	def setInputTextCallback(self, func):
		self.input.bind(text=func)

	def toAscii(self, *args):
		translateDict = {'ă ắ ằ ẳ ẵ ặ â ấ ầ ẳ ẵ ặ á à ả ã ạ': 'a',
						 'é è ẻ ẽ ẹ ê ế ề ể ễ ệ': 'e',
						 'í ì ỉ ĩ ị': 'i',
						 'ó ò ỏ õ ọ ô ố ồ ổ ỗ ộ ơ ớ ờ ở ỡ ợ': 'o',
						 'ú ù ủ ũ ụ ư ứ ừ ử ữ ự': 'u',
						 'ý ỳ ỷ ỹ ỵ': 'y'}
		for set_of_char in translateDict:
			for char in set_of_char.split(' '):
				if char in self.input.text:
					self.input.text = self.input.text.replace(char, translateDict[set_of_char])

	def toUpper(self, *args):
		self.input.text = self.input.text.upper()

	def toLower(self, *args):
		self.input.text = self.input.text.lower()

	def toTitleForm(self, *args):
		self.input.text = self.input.text.title()


class Root(BoxLayout):
	'''main layout'''
	def __init__(self, **kwargs):
		super(Root, self).__init__(**kwargs)
		self.path = os.getcwd()  # path to store downloaded files
		self.cur_youtube_obj = None  # to store the current download object for display download and blabla
		self.text_input = self.ids['_text_input']  # input url
		self.text_input.bind(text=self.onChangeLink)
		self.change_video_name_input = self.ids['_change_video_name_input']  # the change name bar
		self.change_video_name_input.setInputTextCallback(self.onChangeName)
		self.status_lbl = self.ids['_status_lbl']  # the status label
		self.all_videos_box = self.ids['_all_videos_box']  # box contain all YoutubeDisplayLayout obj
		self.audio_download_box = self.ids['_audio_download_box']  # the box contain all audio download button
		self.video_download_box = self.ids['_video_download_box']  # the box contain all video download button
		self.queue_download_box = self.ids['_queue_download_box']  # the box contain all download process
		self.all_thread_download = {}  # list to detect which data belongs to which thread... blabla
		self.lock = threading.Lock()  # mutex thread
		self.pathChooser = PathInputPopup(size_hint=(.5, .5), title='Chọn Nơi Lưu')  # change the self.path popup
		self.pathChooser.setText(self.path)
		self.pathChooser.bind(on_dismiss=self.changePath)

	def onChangeLink(self, obj, val):
		'''display the number of link in the url to the status label'''
		count = 0
		for link in val.split('\n'):
			if link:
				count += 1
		if count:
			self.status_lbl.text = 'Số Link Video : %s' % count
		else:
			self.status_lbl.text = 'Nhập Link Youtube Vào Ô Bên Dưới'

	def onChangeName(self, obj, val):
		'''bind the text in current select download object(YoutubeDisplayLayout) to the text in the change name bar '''
		if self.cur_youtube_obj:
			self.cur_youtube_obj.setTitle(val)

	def pasteClipboard(self):
		self.text_input.paste()
		self.text_input.text += '\n'

	def clearTextInput(self):
		self.text_input.text = ''

	def openPathChooser(self):
		self.pathChooser.open()

	def changePath(self, *args):
		'''implement change path action'''
		path = self.pathChooser.getText()
		if os.path.isdir(path):
			self.path = path
		else:
			self.status_lbl.text = u'Đường Dẫn Không Hợp Lệ'

	def getLink(self):
		'''get link bind to the button'''
		gc.collect()
		self.all_videos_box.clear_widgets()
		threading.Thread(target=self.getYoutubeObjectThread,
							args=(self.text_input.text, self.getLinkCallback)
						).start()  # call thread to prevent block when getting data

	def getYoutubeObjectThread(self, url, callback):
		'''Main function to get data'''
		#url = "https://www.youtube.com/watch?v=JOX-krmWf8Q"
		self.status_lbl.text = u'Đang Lấy Dữ Liệu...'
		all_videos = []
		if 'watch' in url:  # if url is videos
			all_videos = self.getYoutubeVideo(url)
		elif 'playlist' in url:  # if url is playlist
			all_videos = self.getYoutubePlaylist(url)
		else:
			all_videos = self.getYoutubeVideoBySearchQuery(url, 5)
		try:  # call callback
			if callback:
				callback(all_videos)
		except:
			self.status_lbl.text = u'Lỗi...'

	def getYoutubeVideoBySearchQuery(self, url, max_videos):
		if r'youtube.com/results?' not in url:
			url = u'https://www.youtube.com/results?search_query=' + url
		print url
		data = requests.get(url)
		data.raise_for_status()
		soup = bs4.BeautifulSoup(data.text, "html.parser")
		link_elements = soup.select('.yt-lockup-title a')
		all_links = ''
		count = 0
		for link in link_elements:
			if 'watch' in link.get('href'):
				all_links += link.get('href') + '\n'
				count += 1
			if count == max_videos:
				break
		gc.collect()
		return self.getYoutubeVideo(all_links)

	def getYoutubeVideo(self, url):
		'''get data from video urls'''
		all_videos = []
		try:
			for link in url.split('\n'):
				video = pafy.new(link)
				all_videos.append(video)
		except:
			pass
		gc.collect()
		return all_videos

	def getYoutubePlaylist(self, plurl):
		'''get data from playlist url'''
		all_videos = []
		try:
			playlist = pafy.get_playlist(plurl)
			for video in playlist['items']:
				all_videos.append(video['pafy'])
		except:
			pass
		gc.collect()
		return all_videos

	def getLinkCallback(self, all_videos):
		'''Adding YoutubeDisplayLayouts to the all_videos_box'''
		for video in all_videos:  # assign the source_videos, sources audio to use later
			obj = YoutubeDisplayLayout(title=video.title, duration=video.duration,
										thumbnail=video.thumb, view_count=video.viewcount, author=video.username,
										source_videos=video.streams, source_audios=video.audiostreams)
			obj.bind(on_click=self.showDownload)  # when click, show all available video and audio download button
			self.all_videos_box.add_widget(obj)
		#tracker.print_diff()
		i = 0
		for obj in gc.get_objects():
			if isinstance(obj, YoutubeDisplayLayout):
				print obj
		print i
		self.status_lbl.text = u'Xong'

	def showDownload(self, obj):
		'''show all available download button of video object'''
		gc.collect()
		self.cur_youtube_obj = obj  # store in self to use later
		self.cur_youtube_obj.unselectAll()  # select animation
		self.cur_youtube_obj.select()
		self.status_lbl.text = obj.getTitle()  # set the status label
		self.video_download_box.clear_widgets()
		self.audio_download_box.clear_widgets()
		for s in obj.source_videos:  # add download button to video download box
			b = Button(text=s.resolution + '\n' + s.extension)
			b.halign = 'center'
			b.valign = 'middle'
			b.font_size = 12
			b.stream = s  # stream to use later
			b.video_pafy_obj = obj  # video obj to use later
			b.bind(on_release=self.download)  # when click, implement download process
			self.video_download_box.add_widget(b)
		for s in obj.source_audios:  # add download button to audio download box
			b = Button(text=s.quality + '\n' + s.extension)
			b.halign = 'center'
			b.valign = 'middle'
			b.font_size = 12
			b.stream = s   # stream to use later
			b.video_pafy_obj = obj  # video obj to use later
			b.bind(on_release=self.download)  # when click, implement download process
			self.audio_download_box.add_widget(b)
		self.change_video_name_input.setText(obj.getTitle())  # set the change name bar (user friendly)

	def downloadAll(self, kind, quality):
		'''download all video or audio have defined kind and quality'''
		for video_obj in self.all_videos_box.children[::-1]:  # iterate all YoutubeDisplayLayout object to download
			stream = None
			if kind == 'video':
				streams = video_obj.source_videos
			elif kind == 'audio':
				streams = video_obj.source_audios
			else:
				return
			for s in streams:
				if s.quality == quality:  # in pafy, the quality of audio is always 0x0
					stream = s
				elif s.bitrate == quality:  # in pafy, the bitrate of video is always None
					stream = s
			title = video_obj.getTitle()  # getTitle for naming the path to store, and display the name of download widget
			threading.Thread(target=self.downloadThread, args=(stream, title)).start()  # start thread to prevent blocking

	def download(self, obj):
		'''download one video'''
		stream = obj.stream
		filename = obj.video_pafy_obj.getTitle().decode('utf-8')  # decode to prevent unicode error (try it and fix it)
		threading.Thread(target=self.downloadThread, args=(stream, filename)).start()

	def stripStringToWindowsFormat(self, string):
		for char in ': / \ : * ? " < > | '.split(' '):
			if char in string:
				string = string.replace(char, '')
		return string

	def downloadThread(self, stream, filename):
		'''function define the download (which is called in thread by download and downloadAll)'''
		with self.lock:  # because downloadAll call continously in loop, so need to be mutex
			filepath = self.path + os.sep + self.stripStringToWindowsFormat(filename) + '.' + stream.extension
			id = threading.current_thread().ident  # id for identity the thread for store in self to use later (in downloadCallback)
			download_info_btn = YoutubeInfoDownload()
			download_info_btn.setName(filename[:6] + '...' + filename[-6:])
			download_info_btn.setFontSize(12)
			self.all_thread_download[id] = [False, download_info_btn]
			# the first is END thread boolean, 2nd is button to downloadCallback change the info
			# you can't call the sys.exit in the callback of download_info_btn
			# because download_info_btn belongs to the another thread, it fire the callback
			# in the another control widget thread, if you call, it will crash the GUI and don't
			# close the current download thread

			def callback(*arg):
				self.all_thread_download[id][0] = True
				self.queue_download_box.remove_widget(download_info_btn)
			download_info_btn.setDeleteButtonCallback(callback)  # the implicit method to set the callback to the delete button
			self.queue_download_box.add_widget(download_info_btn)  # display it in the box
		try:
			stream.download(filepath=filepath,
								quiet=True, callback=self.downloadCallback)
			self.queue_download_box.remove_widget(download_info_btn)  # when finish, clean it
		except:
			download_info_btn.setProgressStatus('Lỗi')  # display error and dont remove (user friendly)

	def downloadCallback(self, *args):
		download_info_btn = self.all_thread_download[threading.current_thread().ident][1]
		# dont mutex because this item is only accessed by this thread (by thread id)
		# (in the same list, but it is seperate item, and it is immutable, dont need to mutex at all)
		if self.all_thread_download[threading.current_thread().ident][0]:
			sys.exit()
		percent = int(args[2] * 100)
		total_size = args[0]/(1024.0*1024)
		cur_size = args[1]/(1024.0*1024)
		progress_mbyte = '%.2fMB/%.2fMB' % (cur_size, total_size)
		download_info_btn.setProgressStatus(progress_mbyte)  # that why you must store the button in self
		download_info_btn.setProgressPercent(percent)

class YoutubeDownloadApp(App):
	def build(self):
		Window.size = (1024, 500)
		self.title = 'Youtube Downloader'
		return Root()

if __name__ == '__main__':
	YoutubeDownloadApp().run()
