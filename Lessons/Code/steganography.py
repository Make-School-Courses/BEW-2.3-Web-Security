"""
[Day 7] Assignment: Steganography
  Turn in on Gradescope (https://make.sc/bew2.3-gradescope)

Lesson Plan:
  https://make-school-courses.github.io/BEW-2.3-Web-Security/#/Lessons/Steganography

Deliverables:
  1. All TODOs in this file.
  2. Decoded sample image with secret text revealed.
  3. Your own image encoded with secret text!
"""

from PIL import Image


def decode_image(path_to_png):
    """
    TODO: Add docstring and complete implementation.
    """
    encoded_image = Image.open(path_to_png)
    red_channel = encoded_image.split()[0]

    # Create a new PIL image with the same size as the encoded image:
    decoded_image = Image.new("RGB", encoded_image.size)
    pixels = decoded_image.load()

    # TODO: Complete the implementation:
    # The variables below, x_size and y_size, are provided to assist you.
    x_size = encoded_image.size[0]
    y_size = encoded_image.size[1]

    print(red_channel)  # Start coding here!

    # DO NOT MODIFY. Save the decoded image to disk:
    decoded_image.save("decoded_image.png")


def encode_image(path_to_png):
    """
    TODO: Add docstring and complete implementation.
    """
    pass
