from PIL import Image
import numpy as np

class Canvas(object):
    """
    Canvas layer for drawing
    """

    def __init__(self, width: int, height: int, color: list):
        self.width = width
        self.height = height
        self.color = color

        # Let's create an empty 3d array                   # make sure to change this
        self.data = np.zeros(shape= (self.width, self.height, 3), dtype= np.uint8)
        self.data[:] = self.color # fills all the data with given color

    def create(self, image_path: str):
        """
        stores the data in given image path
        """
        img = Image.fromarray(obj= self.data, mode= 'RGB')
        img.save(fp= image_path)