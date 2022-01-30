import xlsxwriter
import webbrowser

# In xlsx the row are specified in numbers (1 - inf)
# and columns are specified in alphabets (A - ZZ)

# creates xlsx file
workbook = xlsxwriter.Workbook(filename= 'sample.xlsx')

# Adds a new worksheet (table page) to write
worksheet = workbook.add_worksheet()

# writing the content
worksheet.write('A1', 'Item') # A is col, 1 is row
worksheet.write('B1', 'Object')

workbook.close()



webbrowser.open(r'C:\Users\Admin\PycharmProjects\AdvancedOOP\7. AutomatedEmails\sample.xlsx')