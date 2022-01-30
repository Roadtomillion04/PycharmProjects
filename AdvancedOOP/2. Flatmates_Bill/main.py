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
for idx, flatmate in enumerate(flatmates):
                                    # for i = 0, for i = 2
    prev = flatmates[:idx]          # [:0] = [], [:2] = [0, 1]
    end = flatmates[idx+1:]         # [0+1:] = [1], [2+1:] = []
                                    # []+[1] = [1], [0, 1]+[] = [0, 1]
    print(flatmate.pays(bill, prev + end))

pdf = PdfGenerator(filepath= "Report.pdf",)
print(pdf.generate(bill= bill, flatmates= flatmates))

file_sharer = FileSharer(filepath= pdf.filepath)
print(file_sharer.share())

# Repl CLI link
print(f'Repl link : https://replit.com/@NIRMAL-KUMARKU1/FlatmatesBill?embed=1%20--Repl.it%20-%20FlatmatesBill')
