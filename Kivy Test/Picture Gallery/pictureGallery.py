import os
from shutil import copy2
from kivy.garden.filebrowser import FileBrowser
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.app import App
from kivy.lang import Builder

Builder.load_string('''
#:set HEIGHT_MENU_BUTTON 180

<MenuButton>:
	size_hint: 1, None
	height: HEIGHT_MENU_BUTTON

<PictureGallery>:
	BoxLayout:
		orientation: 'vertical'
		ScatterLayout:
			id: _image_scatter
			auto_bring_to_front: False
			do_rotation: False
			Image:
				id: _image_frame
		Button:
			id: _image_name
			size_hint: 1, .1
			on_release: root.setDefaultImageState()
	BoxLayout:
		size_hint: .3, 1
		orientation: 'vertical'
		Button:
			size_hint: 1, .1
			text: 'Add Image'
			on_release: root.showFileBrowser()
		ScrollView:
			do_scroll_x: False
			BoxLayout:
				id: _menu
				orientation: 'vertical'
				size_hint: 1, None
				height: len(self.children) * HEIGHT_MENU_BUTTON
''')

PICTURE_DIR = os.getcwd() + os.sep + 'Pictures'
PICTURE_EXT = 'png jpeg jpg bmp gif'.split()

class MenuButton(Button):
	pass

class PictureGallery(BoxLayout):
	def __init__(self, **kwargs):
		super(PictureGallery, self).__init__(**kwargs)
		self.menu = self.ids['_menu']
		self.image_frame = self.ids['_image_frame']
		self.image_name = self.ids['_image_name']
		self.image_scatter = self.ids['_image_scatter']
		self.file_browser = FileBrowser()
		self.file_browser.bind(on_success=self.addImageEvent, on_canceled=self.cancelFileBrowser)
		self.file_browser_popup = Popup(content=self.file_browser, size_hint=(.8, .8))
		self.loadPictureMenu()

	def loadPictureMenu(self):
		'''Load Dir and Add Button to Menu'''
		last_dir = ''
		self.menu.clear_widgets()
		for dir in os.listdir(PICTURE_DIR):
			splitname = os.path.splitext(dir)
			if splitname[1].strip('.') not in PICTURE_EXT:
				continue
			button_temp = MenuButton(text=splitname[0])
			button_temp.ext = splitname[1]
			button_temp.bind(on_release=self.loadPicture)
			self.menu.add_widget(button_temp)
			last_dir = dir
		self.image_name.text = os.path.splitext(last_dir)[0]
		self.image_frame.source = PICTURE_DIR + os.sep + last_dir

	def loadPicture(self, obj):
		dir = PICTURE_DIR + os.sep + obj.text + obj.ext
		self.image_name.text = obj.text
		self.image_frame.source = dir

	def showFileBrowser(self):
		self.file_browser_popup.open()

	def addImageEvent(self, obj):
		try:
			selection = obj.selection[0]
		except:
			return
		if os.path.splitext(selection)[1].strip('.') in PICTURE_EXT:
			print selection, PICTURE_DIR
			copy2(selection, PICTURE_DIR)
			self.file_browser_popup.dismiss()
			self.loadPictureMenu()

	def cancelFileBrowser(self, obj):
		self.file_browser_popup.dismiss()

	def setDefaultImageState(self):
		self.image_scatter.scale = 1.0
		self.image_scatter.pos = (self.image_name.x, self.image_name.y + self.image_name.height)

class PictureGalleryApp(App):
	def build(self):
		return PictureGallery()

if __name__ == '__main__':
	PictureGalleryApp().run()
