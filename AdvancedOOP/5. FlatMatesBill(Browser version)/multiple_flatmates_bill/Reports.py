import webbrowser
from fpdf import FPDF
from flat import Bill
import os
from filestack import Client


class PdfGenerator(object):
    """
    Generates a pdf report of Bill need to payed by flatmates
    """

    def __init__(self, filepath: str):
        self.filepath = filepath

    def generate(self, bill: Bill, flatmates: list):

        flatmate_info: dict = {}
        for flatmate in flatmates:
            flatmate_info[flatmate.name] = flatmate.pays(bill= bill, flatmates= flatmates)

        pdf = FPDF(orientation= 'P', unit= 'pt', format= 'A4')

        pdf.add_page()

        # Add icon
        pdf.image(name= 'Resources/house.png', w= 45, h= 45) # resizes image with given points

        # Add title
        pdf.set_font(family= 'Times', style= 'B', size= 24)
        pdf.cell(w= 0, h= 80, txt= 'Flatmates Bill', align= 'C', border= 0, ln= 1)

        # Add Period and value
        pdf.set_font(family= 'Times', style= 'B', size= 16)
        pdf.cell(w= 100, h= 40, txt= 'Period', border= 0, ln= 0)
        pdf.cell(w= 200, h= 40, txt= bill.period, border= 0, ln= 1)

        # Insert name and due amount of flatmates
        pdf.set_font(family= 'arial', style= '', size= 16) # '' - normal style
        for name, pay_amount in flatmate_info.items():
            pdf.cell(w= 100, h= 40, txt= name, border= 0, ln= 0)
            pdf.cell(w= 100, h= 40, txt= f'{round(pay_amount, 2)}', border= 0, ln= 1)
                                    # As godot label expects in string

        # save pdf
        os.chdir('Resources/') # change directory, we have to change the save path
        pdf.output(name= self.filepath)
        webbrowser.open(self.filepath)
        # If you are on mac create manually absolute path string

        return flatmate_info

class FileSharer():
    """
    A class that uploads the given filepath to file_stack server and returns it's url
    """

    def __init__(self, filepath: str, api_key= 'AdG9aDa0nS0mZnP8S3sFwz'):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = Client(apikey= self.api_key)

        file_link = client.upload(filepath= self.filepath)
        return file_link.url
