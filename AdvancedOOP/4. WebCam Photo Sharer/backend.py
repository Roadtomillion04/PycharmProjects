from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.clipboard import Clipboard
from kivy.core.window import Window # for bg

from filesharer import FileSharer
import time
import webbrowser

# load_file() is a class method not instance one
Builder.load_file(filename= 'frontend.kv') # connects frontend to backend

class CameraScreen(Screen): # first screen
    def start_webcam(self):
        self.ids.camera.play = True
        # or we can call directly
        self.ids.camera_button.text = 'stop camera'

        # to revert texture == None
        self.ids.camera.texture = self.ids.camera._camera.texture

    def stop_webcam(self):
        self.ids.camera.play = False
        self.ids.camera_button.text = 'start camera'

        # stop currently displays last_frame, to remove that
        self.ids.camera.texture = None

    def capture(self):  # str from time
        """
        Captures a photo of last frame when button clicked, and save it as
        current time image in files
        """
        current_time = time.strftime('%Y-%m-%d-%H-%M-%S')
        self.file_path = f"files/{current_time}.png"
        self.ids.camera.export_to_png(filename= self.file_path)

        # Change screen to ImageScreen
        self.manager.current = 'image_screen' # name we declared in kivy
        # manager calls ScreenManager
        self.manager.current_screen.ids.image_display.source = self.file_path


class ImageScreen(Screen): # second screen
    warning_message = 'please create a link first' # class attribute

    def create_link(self):
        """
        Accesses the captured photo filepath, and uploads it to
        web and inserts the link to label widget
        """
        # To get access to the image filepath of CameraScreen class
        image_file = App.get_running_app().root.ids.camera_screen.file_path

        # uploading image to cloud
        file_sharer = FileSharer(filepath= image_file)
        self.url = file_sharer.upload()
        self.ids.link.text = self.url

    def copy_link(self):
        # copy is class method not instance one
        try:
            Clipboard.copy(self.url) # copy's given str to computer's clipboard
        except: # when the user tries to copy link without create_link()
            self.ids.link.text = self.warning_message

    def open_link(self):
        try:
            webbrowser.open(url= self.url)
        except: # when create link not created
            self.ids.link.text = self.warning_message


# Common convention to run kivy app window
class RootWidget(ScreenManager):
    pass # we can add any method in future when needed

class MainApp(App):
    def build(self):        #r  g  b  a
        Window.clearcolor = (0.5, 0.3, 0.5, 1)
        return RootWidget()

MainApp().run()
