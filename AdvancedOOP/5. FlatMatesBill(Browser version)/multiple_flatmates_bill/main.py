from Reports import PdfGenerator, FileSharer
from flat import Bill, Flatmate

#Bill details
amount = float(input("Enter the Bill amount: "))
period = input("Enter the period(mm/yyyy): ")
bill = Bill(amount= amount, period= period)

#Flatmates info
no_of_flatmates = int(input("How many flatmates are staying: "))
flatmates: list = []
for i in range(no_of_flatmates):
    name = input(f'Enter name{i+1}: ') # As index starts from 0
    days_stayed = int(input(f'Enter {name}\'s days stayed during bill period: '))

    # Creating instance variables with their name
    name = Flatmate(name= name, day_in_house= days_stayed)

    flatmates.append(name)

# Calculating due amount of given flatmates
for flatmate in flatmates:
    print(flatmate.pays(bill, flatmates))

pdf = PdfGenerator(filepath= "Report.pdf",)
print(pdf.generate(bill= bill, flatmates= flatmates))

file_sharer = FileSharer(filepath= pdf.filepath)
print(file_sharer.share())

# Repl CLI link
print(f'Repl link : https://replit.com/@NIRMAL-KUMARKU1/FlatmatesBill?embed=1%20--Repl.it%20-%20FlatmatesBill')
