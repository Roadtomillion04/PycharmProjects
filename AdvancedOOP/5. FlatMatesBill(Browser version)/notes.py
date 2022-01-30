'''
the process of putting the web app to the internet is called deployment

Basic website convention
Every website has port & ip address that is converted to domain name for user friendly
We use MethodView() from flask.view for displaying content in webpage

app.run(debug = True, port= 5000)
enables to change the script in runtime and see the results by refresh

we assign a url extension of a domain name by
Like www.abc.com/news

a = Flask().add_url_rule('/extension',
                        view_func= Inherited class from Method view.as_view('class_name'))


Displaying Info in WebPage
class HomePage(MethodView):
    def get(self): # method from MethodView
        return 'Hi'

When the page is viewed by get request 'Hi' is displayed


Using flask you must follow these to work properly
HTML file should be located in templates directory
CSS file should be located in static directory
We connect html to flask by render_template(html file) inside get() of
Inherited MethodView Class

Make sure to return in get() or post()
return is the web page display

In StringField() we can use
render_kw= {"placeholder": 0} for hint text
validators = [validators.input_required()] that sets input must be required before submission


In HTML
Don't use <a href="/bill"> Go to Bill Page</a> when we change add_url_rule() in flask later
we have to change here everytime
Use : href={{url_for(name declared in as_view() in add_url_rule)}}

We can connect the wtforms from python to HTML by form tag
make sure to pass the billform class instance in render_template() of get()

bill_form = BillForm()
return render_template('bill_form_page.html',
                               bill_form= bill_form) # used in HTML form tag

Use this in form tag to display in web
{{bill_form.variable.label}} {{bill_form.variable}}
variable is StringField(label= 'name')

<hr> tag draws underline
<br> tag for new line

for button action to take in form tag use
<form action= "/extension"> declared in add_to_rule()

While extracting data that user enters use
<form action= "/extension" method= 'post>
or we'll get Method not allowed error

in that same extension class use def post()

conditions in HTML, make sure to pass results in render_template()
of get() or post() where u need
{% if results %}
HTML CODE
{% endif results %}


In CSS
we can modify only the HTML not the backend script

we can connect to CSS in HTML file by
<link rel="stylesheet" href="static/main.css">
in head tag

To see the live changes of CSS press ctrl + shift + R


we can upload the flaskapp to internet by
login to pythonanywhere.com
upload the files
reload the webpage
see errors in log error page
'''
