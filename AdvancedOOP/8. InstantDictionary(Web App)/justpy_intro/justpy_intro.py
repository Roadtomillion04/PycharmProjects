# just py is a framework we can build frontend using python
import justpy as jp

def home(): # we need to add url to display this func
    webpage_instance = jp.WebPage()
    # adding tag component to webpage
    jp.Div(a= webpage_instance, text='Hello')
    jp.Div(a= webpage_instance, text='Hello again')
    return webpage_instance

@jp.SetRoute(route= '/about')
def about(): # we need to add url to display this func
    webpage_instance = jp.WebPage()
    jp.Div(a= webpage_instance, text='Hi Hello World just learning',
           # styling in just py, classes is css
           classes= "text-yellow-500 text-lg font-mono bg-indigo-300")
    jp.Div(a= webpage_instance, text='I\'m the star!')
    return webpage_instance


# to add url and instantiate a function
jp.Route(path= '/', func_to_run= home)

# to start a server
jp.justpy()