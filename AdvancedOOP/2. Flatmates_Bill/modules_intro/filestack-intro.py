# To upload a file to file stack cloud

from filestack import Client

# Found in FileStack website after signing in
client = Client(apikey='AdG9aDa0nS0mZnP8S3sFwz')

file_link = client.upload(filepath='sample.txt')
print(file_link.url)

