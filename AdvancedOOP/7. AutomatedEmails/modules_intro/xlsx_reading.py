import pandas as pd

# Supports xls, xlsx, xlsm, xlsb, odf, ods and odt file extensions
xlsx_file = pd.read_excel(io= '../files/people.xlsx')

print(xlsx_file) # make sure to install openpyxl to see results in console

# for multiple email sending
for idx, row in xlsx_file.iterrows(): # Iterate over DataFrame rows as (index, Series) pairs.
    print(row['email'])

