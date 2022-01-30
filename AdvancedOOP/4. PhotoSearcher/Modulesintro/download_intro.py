import wikipedia # using wikipedia API to get user input page

page = wikipedia.page(title= 'Beach') # returns Game page instance

img = page.images # Gives list of all images link found in Game page
summary = page.summary

print(dir(page))
print(img[0], '\n')

# Using requests to download the image link
import requests
from random import choice

                        # so that everytime we get different image from list
res = requests.get(url= choice(img)) # img is a list of links

while res.status_code != 200: # most of the images are not giving response 200
    res = requests.get(url= choice(img))


print(type(res.content))
with open(file= 'image.jpg', mode= 'wb') as file:
    file.write(res.content) # res.content returns in binary so wb

