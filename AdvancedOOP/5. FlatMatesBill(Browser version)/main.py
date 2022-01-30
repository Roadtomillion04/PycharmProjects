# we don't want to reinvent the wheel, Let's inherit and build the system easier
from flask.views import MethodView
from wtforms import Form, StringField, SubmitField, validators
from flask import Flask, render_template, request

from flatmates_bill import flat, reports

app = Flask(__name__)

class HomePage(MethodView):

    def get(self): # method from MethodView
        return render_template('index.html') # flask knows if it's inside templates directory

class BillFormPage(MethodView):

    def get(self): # instance here and pass it in render template to use it in form tag
        bill_form = BillForm()
        return render_template('bill_form_page.html',
                               bill_form= bill_form) # used in HTML form tag


class ResultsPage(MethodView):
    # post() as we getting data from form tag give method= 'post'
    def post(self): # This time we extract data what user enters
        bill_form = BillForm(request.form)

        # processing data - Make sure to change the str to int in amount and days stayed
        bill = flat.Bill(amount= float(bill_form.amount.data),
                         period= bill_form.period.data)

        flatmate1 = flat.Flatmate(name= bill_form.name1.data,
                                  days_in_house= int(bill_form.days_stayed1.data))
        flatmate2 = flat.Flatmate(name= bill_form.name2.data,
                          days_in_house= int(bill_form.days_stayed2.data))

        # Creating pdf report
        pdf_report = reports.PdfReport(filename= 'reports.pdf')
        pdf_report.generate(flatmate1, flatmate2, bill)

        # uploading it to file-stack
        file_sharer = reports.FileSharer(pdf_report.filename)
        url = file_sharer.share()

        return render_template('results.html',
                               name1= flatmate1.name.upper(),
                               name2= flatmate2.name.upper(),
                               amount1 = round(flatmate1.pays(bill, flatmate2), 2),
                               amount2 = round(flatmate2.pays(bill, flatmate1), 2),
                               url= url)

class BillForm(Form):
    # like input type text in HTML
    amount = StringField(label= 'Bill Amount: ',
                         render_kw= {"placeholder": 0},
                         validators = [validators.input_required()])
    period = StringField(label= 'Bill Period: ',
                         render_kw= {"placeholder":'MONTH YYYY'},
                         validators = [validators.input_required()])

    # flatmate 1
    name1 = StringField(label= 'Name: ',
                        render_kw= {"placeholder":'X'},
                        validators = [validators.input_required()])
    days_stayed1 = StringField(label= 'How many Days Stayed: ',
                               render_kw= {"placeholder":0},
                               validators = [validators.input_required()])
    # flatmate 2
    name2 = StringField(label= 'Name: ',
                        render_kw= {"placeholder":'Y'},
                        validators = [validators.input_required()])
    days_stayed2 = StringField(label= 'How many Days Stayed: ',
                               render_kw= {"placeholder":0},
                               validators = [validators.input_required()])

    # button
    button = SubmitField(label= 'Calculate')

# adding extensions after domain name                   # good to have same class name
app.add_url_rule(rule= '/', view_func= HomePage.as_view(name= 'home_page'))
app.add_url_rule(rule= '/bill', view_func= BillFormPage.as_view(name= 'bill_form_page'))
app.add_url_rule(rule= '/results', view_func= ResultsPage.as_view(name= 'results_view'))
# as_view() instantiate the class by given name and performs get() or post()

app.run(debug= True, port= 5000) # runs the server