'''
Image Processing:

Load an image into a NumPy array using a library like OpenCV or PIL. (don't have to use OpenCV or PIL)
Implement simple image processing operations such as grayscale conversion, 
resizing, rotation, and flipping using NumPy array manipulation techniques.
'''

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

class ImageProcessor:
    def __init__(self, image_path):
        """
        Initialize the ImageProcessor class with the path to an image.

        Parameters:
            image_path (str): Path to the input image file.

        Returns:
            None
        """

        self.image_path = image_path
        self.img = Image.open(self.image_path)
        self.img_rgbFormat = self.img.convert('RGB')
        self.image_array = np.array(self.img_rgbFormat)
				

    def to_grayscale(self):
        """
        Convert the loaded image to grayscale.

        Parameters:
            None

        Returns:
            numpy.ndarray: Grayscale version of the image.
        """
        gray_array = np.dot(self.image_array[..., :3], [0.2989, 0.5870, 0.1140])
        return gray_array.astype(np.uint8)

    def resize(self, scale_factor):
        """
        Resize the image by a given scale factor.

        Parameters:
            scale_factor (float): Factor by which to scale the image.

        Returns:
            numpy.ndarray: Resized image.
        """
        height, width = self.image.shape[:2]
        new_height, new_width = int(height * scale_factor), int(width * scale_factor)
        resized_image = np.array(Image.fromarray(self.image).resize((new_width, new_height)))

        return resized_image

    def rotate(self, angle):
        """
        Rotate the image by a given angle.

        Parameters:
            angle (float): Angle (in degrees) by which to rotate the image.

        Returns:
            numpy.ndarray: Rotated image.
        """
        rotated_image = np.array(Image.fromarray(self.image).rotate(angle))

        return rotated_image

    def flip_horizontal(self):
        """
        Flip the image horizontally.

        Parameters:
            None

        Returns:
            numpy.ndarray: Horizontally flipped image.
        """
        flipped_image = np.flip(self.image, axis=1)

        return flipped_image

    def flip_vertical(self):
        """
        Flip the image vertically.

        Parameters:
            None

        Returns:
            numpy.ndarray: Vertically flipped image.
        """
        flipped_image = np.flip(self.image, axis=0)

        return flipped_image
        

    def display_image(self, anotherImage=None):
        """
        Display the processed image using Matplotlib.

        Parameters:
					self

        Returns:
            None
        """
        if anotherImage is None:
             plt.imshow(self.image_array, cmap='gray')
             plt.axis('off')
             plt.show()
        else:
             plt.imshow(anotherImage, cmap='gray')
             plt.axis('off')
             plt.show()

def main():
    # Create an instance of the ImageProcessor class
		image = ImageProcessor('imageTest.jpeg')
    # Call each method to perform image manipulation operations

		#first things first, show the original image
		image.display_image()
		#second things second, show the grayscale image
		new_image = image.to_grayscale()
		image.display_image(new_image)
		#thirdly, show the scaled up image
		new_image = image.resize(2)
		#more test cases can be put here

if __name__ == "__main__":
    main()

#marked by ChatGPT as 3.8/5