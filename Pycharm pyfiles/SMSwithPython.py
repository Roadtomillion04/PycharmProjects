# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
import os
from twilio.rest import Client # this is copy pasted but make sure to pip install twilio

# Find these values at https://twilio.com/user/account
# To set up environmental variables, see http://twil.io/secure
account_sid = 'AC349fc1413ec4b778baa48e87ba1e8421'
auth_token = 'b8a5392217470bc38ea610fa623e3dbb'

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="+918610846845",
    from_="+12034634142",
    body="Hello there Nirmal How are you, I CANT BELIEVE THIS WORKS !")
