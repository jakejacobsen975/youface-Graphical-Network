import unittest
from unittest.mock import patch, MagicMock
import base64
import requests
import openai
from handlers.posts import ImageGenerator



class TestImageGenerator(unittest.TestCase):

    def setUp(self):
        self.imageGen = ImageGenerator()

    @patch("openai.Image.create")
    def test_generateImage(self, mock_create):

        # test case when there are enough tokens
        mock_response = {
            "data": [
                {"url": "https://example.com/image1.jpg"},
                {"url": "https://example.com/image2.jpg"},
            ]
        }
        mock_create.return_value = mock_response

        self.imageGen.generateImage(Prompt="test prompt", ImageCount=2, ImageSize="512x512")

        mock_create.assert_called_once_with(prompt="test prompt", n=2, size="512x512")
        self.assertEqual(self.imageGen.image_url, ["https://example.com/image1.jpg", "https://example.com/image2.jpg"])

        # mock response with unexpected format
        mock_create.reset_mock()
        mock_response = {"invalid": "response format"}
        mock_create.return_value = mock_response

        with self.assertRaises(KeyError):
            self.imageGen.generateImage(Prompt="test prompt", ImageCount=2, ImageSize="512x512")

        mock_create.assert_called_once_with(prompt="test prompt", n=2, size="512x512")

        # test case when there are not enough tokens
        mock_create.side_effect = openai.error.APIError(
            message="Not enough tokens to complete the request."
        )

        with self.assertRaises(openai.error.APIError):
            self.imageGen.generateImage(Prompt="test prompt", ImageCount=2, ImageSize="512x512")

    def test_downloadImage(self):
        # test case when image URL is valid and image is downloaded successfully
        imageGen = ImageGenerator()
        imageGen.image_url = ['https://imgs.search.brave.com/APHgc8UDMrBSann09Uu72ACW8xNavgwDRIei4liH2GY/rs:fit:1200:600:1/g:ce/aHR0cHM6Ly93d3cu/aG93dG9nZWVrLmNv/bS90aHVtYmNhY2hl/LzIvMjAwLzQwZTI4/NzkyNDJhMGY2NDNl/NTUyMDk0ZWM3MGFk/OGU5L3dwLWNvbnRl/bnQvdXBsb2Fkcy8y/MDE4LzA2L3NodXR0/ZXJzdG9ja18xMDA2/OTg4NzcwLnBuZw']
        image = imageGen.downloadImage()
        self.assertEqual(image[:40], 'iVBORw0KGgoAAAANSUhEUgAABLAAAAIqCAIAAAC7')

        # test case when image URL is not valid
        self.imageGen.image_url = "https://example.com/image1.jpg"
        image = self.imageGen.downloadImage()
        self.assertEqual(image, ValueError)
        
        # test case when there is an error while downloading the image
        
        self.imageGen.image_url = "https://example.com/error.jpg"
        image = self.imageGen.downloadImage()
        self.assertEqual(image, ValueError)
            

    @patch("openai.Image.create")
    def test_generateImage_invalid_input(self, mock_create):
        # test case when prompt is empty
        with self.assertRaises(ValueError):
            self.imageGen.generateImage(Prompt="", ImageCount=2, ImageSize="512x512")
        # test case when image size input is invalid
        with self.assertRaises(ValueError):
            self.imageGen.generateImage(Prompt="test prompt", ImageCount=2, ImageSize="invalid_size")
        # test case when prompt contains a word that OpenAI does not accept
        mock_create.side_effect = openai.error.InvalidRequestError(
            message='The following words are not permitted: ["badword"].',
            param='prompt'
        )

        with self.assertRaises(openai.error.InvalidRequestError):
            self.imageGen.generateImage(Prompt="Prompt contains a word that OpenAI does not accept", ImageCount=2, ImageSize="512x512")
        




            '''Explanations for each unit test '''

# The tests can be run using 
# python3 -m unittest tests/images_test.py


# The setUp method creates an instance of the ImageGenerator class for each test case.

# The test_generateImage method tests the generateImage method of the ImageGenerator class. It has three test cases:
# The first test case checks if the generateImage method calls the openai.Image.create function with the correct arguments, and sets the image_url attribute of the ImageGenerator object correctly when there are enough tokens.
# The second test case checks if the generateImage method raises a KeyError when the openai.Image.create function returns an unexpected format.
# The third test case checks if the generateImage method raises an openai.error.APIError when there are not enough tokens to complete the request.

# The test_downloadImage method tests the downloadImage method of the ImageGenerator class. It has three test cases:
# The first test case checks if the downloadImage method downloads the image successfully when the URL is valid.
# The second test case checks if the downloadImage method raises a ValueError when the URL is not valid.
# The third test case checks if the downloadImage method raises a ValueError when there is an error while downloading the image.

# The test_generateImage_invalid_input method tests the generateImage method of the ImageGenerator class for invalid inputs. It has three test cases:
# The first test case checks if the generateImage method raises a ValueError when the prompt is empty.
# The second test case checks if the generateImage method raises a ValueError when the image size input is invalid.
# The third test case checks if the generateImage method raises an openai.error.InvalidRequestError when the prompt contains a word that OpenAI does not accept.