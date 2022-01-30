from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

Builder.load_file(filename= 'frontend.kv') # connects frontend to backend

import wikipedia
import requests
from random import choice

class FirstScreen(Screen): # inheriting screen class

    def image_links(self):
        print('working...')

        # Get the user input text
        try:
            query = self.manager.current_screen.ids.user_query.text
            # Get the wikipedia page and image link
            page = wikipedia.page(title= query)
            links = page.images
            return links

        except wikipedia.exceptions.PageError:
            print('Not found anything')
            query = ''

    @property # func becomes attributes
    def download_image(self):
        links = self.image_links()

        # Download the random image from links using response
        res = requests.get(url= choice(links))

        while res.status_code != 200:
            res = requests.get(url= choice(links))

        # Save the content in file
        fp = 'image.jpg'
        with open(file= fp, mode= 'wb') as file:
            file.write(res.content)
        return fp

    def set_image(self):
        self.manager.current_screen.ids.img.source = self.download_image
        print('Finished!')


# common convention to run the kivi app window
class RootWidget(ScreenManager):
    pass

class MainApp(App): # inheriting app class
    def build(self):
        return RootWidget()

MainApp().run()