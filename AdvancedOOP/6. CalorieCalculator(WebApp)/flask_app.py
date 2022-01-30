from flask.views import MethodView, request
from wtforms import Form, StringField, SubmitField, validators
from flask import Flask, render_template

from calorie import Calorie
from temperature import Temperature

app = Flask(__name__) # Instancing app for run(), link extension


class HomePage(MethodView): # For get() & post()

    def get(self): # for reading
        return render_template('home_page.html') # Looks in templates/


class CalorieCalculatorPage(MethodView):

    def get(self):
        calorie_form = CalorieForm()
        return render_template('calorie_form_page.html',
                               calorie_form= calorie_form) # Make sure to send it to html

    def post(self): # For showing results in same page
        calorie_form = CalorieForm(formdata= request.form) # Gets exiting data in form

        temp = Temperature(city= calorie_form.city.data,
                           country= calorie_form.country.data).get_temperature()

                                            # StringField down same as input()
        calorie_calculator = Calorie(weight= float(calorie_form.weight.data),
                                     height= float(calorie_form.height.data),
                                     age= int(calorie_form.age.data),
                                     temperature= temp).calculate()

        return render_template('calorie_form_page.html',
                               calorie_form= calorie_form,
                               calorie= calorie_calculator,
                               result= True) # For html id else logic


class CalorieForm(Form):
    # for Calorie class
    weight = StringField(label= 'Weight', # Html takes this
                                     # Make sure to give it list
                         validators= [validators.input_required()], # Necessary field
                         render_kw= {"placeholder": 0}) # Hint-text
    height = StringField(label= "Height",
                         validators= [validators.input_required()],
                         render_kw= {"placeholder": 0})
    age = StringField(label="Age",
                      validators= [validators.input_required()],
                      render_kw= {"placeholder": 0})

    # For Temperature class
    city = StringField(label= "City",
                       validators= [validators.input_required()],
                       render_kw={"placeholder": 'X'})
    country = StringField(label="Country",
                       validators= [validators.input_required()],
                       render_kw={"placeholder": 'Y'})

    # Button for submission
    button = SubmitField(label= 'Calculate')


# Instances the classes in given rule page
app.add_url_rule(rule= '/',
                 view_func= HomePage.as_view(name= 'home_page'))
app.add_url_rule(rule= '/calories-form',
                 view_func= CalorieCalculatorPage.as_view(name= 'calorie_calculator_page'))

app.run(debug= True, port= 5000)