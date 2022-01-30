from filestack import Client

class FileSharer(object):
    """
    uploads the given image to file stack cloud and returns it's url
    """

    def __init__(self, image_path: str, api_key= 'AdG9aDa0nS0mZnP8S3sFwz'):
        self.image_path = image_path
        self.api_key = api_key

    def upload(self):
        client = Client(apikey= self.api_key)

        file_link = client.upload(filepath= self.image_path)
        return file_link.url
