# We gonna create blueprints for each page
# So that we can instance the page when requested
import justpy as jp

class About:
    path = '/about'

    def serve_webpage(self):
        # we use Quasar for advanced components, tailwind for styling
        wp = jp.QuasarPage(tailwind=True)
        ui = jp.Div(a= wp, classes= 'bg-pin-500 h-screen')

