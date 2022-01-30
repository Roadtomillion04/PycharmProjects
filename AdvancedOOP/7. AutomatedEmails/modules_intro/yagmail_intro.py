import yagmail

# ya gmail works only for gmail accounts
email = yagmail.SMTP(user= 'karurnirmal04@gmail.com',
                     password= '13032004')

email.send(to= 'mlkochnvc@emlpro.com',
           subject= 'Hi there...',
           contents= 'This is a body of the text',
           attachments= './madeline.png')


# Multiple sending
import pandas as pd
df = pd.read_excel(io= '../files/people.xlsx')

for idx, row in df.iterrows(): # Iterate over DataFrame rows as (index, Series) pairs.
    print(row['email'])

for idx, row in df.iterrows():
    email = yagmail.SMTP(user='karurnirmal04@gmail.com',
                         password='13032004')

    email.send(to= row['email'],
               subject= f'Hi there... {row.name}',
               contents=f'You are interested in {row.interest}',
               attachments='./madeline.png')
