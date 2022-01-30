'''
Things Learnt

This is a boiler plate/backbone backend code for any kivi app

Builder.load_file('frontend.kv)
class DisplayScreen(Screen):
    code
class RootWidget(ScreenManager):
    pass
class MainApp(App): # inheriting app class
    def build(self):
        return RootWidget()
MainApp().run()


Wikipedia API used to get the page instance of our Search

we used kivi language in frontend
The <tag>: should be in name of python class we created

But still the app has bug
when wiki page not found it throws error
'''