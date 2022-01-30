# We are going to build a simple calculator and explore to understand just py
import justpy as jp

@jp.SetRoute(route= '/')
def home(): # Request handler function
    wp = jp.WebPage() # create an instance

    # to add a bg, as div is like container class
    ui = jp.Div(a= wp, classes='bg-pink-500 min-h-screen p-4 border-8 border-blue-500 rounded')
    # h-screen takes up entire screen height

    # h1-container
    h1 = jp.Div(a= ui, classes= 'grid grid-cols-3 gap-4')

    input1 = jp.Input(a= h1, placeholder='Enter the first val: ',
             classes= 'form-input m2 font-mono')
    input2 = jp.Input(a= h1, placeholder='Enter the 2nd val: ',
             classes= 'form-input m2 font-mono')
    output = jp.Div(a= h1, text='The results go here..',
           classes= 'm-2 font-underline font-mono')
    jp.Div(a=h1, text='Normal Div...',
           classes='m-2 font-underline font-mono')
    jp.Div(a=h1, text='Yeah me too..',
           classes='m-2 font-underline font-mono')

    # h2-container
    h2 = jp.Div(a= ui, classes= 'grid grid-cols-2 gap-5 p-4 border-4 border-black-900')

    jp.Button(a= h2, text='calculate', click= sum_up,
              # we can access this using widget
              input1= input1, input2= input2, output= output,
              classes= 'border-4 border-white-200 rounded bg-pink-300 '
              'font-bold font-mono px-4 py-0 m-2 hover:bg-blue-300 hover:styling')
    jp.Div(a= h2, text= 'I\'m a cool interactive Div 😁',
           mouseenter= mouse_entered, mouseleave= mouse_exited,
           classes= 'font-mono hover:bg-gray-700')

    return wp


def sum_up(widget, msg): # Event function, All tags passes 2 arguments,
    # use debugger to find non-working or errors
    # widget contains called tag
    # msg is a dict contains event_type info
    from string import digits
    value1 = widget.input1.value # in1 & in2 are input tag instance
    value2 = widget.input2.value # value is an Input tag attribute
    sum = value1 + value2 # value will be considered as string by default

    for letter in sum:
        if letter not in digits: # filters all symbols & chars
            widget.output.text = 'Sorry, You\'ve entered a non-integer value 🙁'

    # if not string in sum
    widget.output.text = f"And the sum is {float(value1) + float(value2)} 😉"


def mouse_entered(widget, msg):
    widget.text = 'Hi, You are Hovering me 😜'

def mouse_exited(widget, msg):
    widget.text= 'See yaa 😎'

jp.justpy() # starts a server
