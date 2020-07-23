# Image Classifier using Python on Various Images
In this project I used an _already created_ image classifier to identify dog breeds.

# Project Overview
A city is hosting a dog show and I have volunteered to help the organizing committee with contestant registration. Every participant that registers must submit an image of their dog along with biographical information about their dog. The registration system tags the images based upon the biographical information.

Some people are planning on registering pets that __aren’t actual dogs.__

I needed to use an already developed `Python` classifier to make sure the participants are dogs.

## How To Run The Program:
Ensure you have Python 3.7 or above installed. Then run the following:

`python check_images.py`

The default argument for the image folder is `pet_images/` and the default argument for the CNN Model Architecture is `VGG`.

To change the folder and/or CNN Model Architecture (to resnet or alexnet), run the following:

`python check_images.py --dir your_folder --arch resnet`, OR

`python check_images.py --dir your_folder --arch alexnet`

If you're on a Mac, instead of typing `python`, type `python 3`.

## Dependencies:

There is a `requirements.txt` file describing the minimal dependencies required to run the script.

To install these dependencies with pip, you can issue `pip3 install -r requirements.txt`.

# Built With
* [Python 3.7.7](python.org) - The Programming Language used.
* [humanfriendly](https://pypi.org/project/humanfriendly/) - A Python Library that was used, specifically, the `format_timespan` module.
* [time](https://docs.python.org/3/library/time.html) - A Python Library that was used.
* [PyTorch](https://pytorch.org/) - A Python Library that was used.

# Credits
* [Udacity AI Programming with Python](udacity.com) - Course material and notes/hints.
* [Python Documentation](https://docs.python.org/3/) - Official Python Documentation.
* [Humanfriendly Documentation](https://humanfriendly.readthedocs.io/en/latest/#api-documentation) - Official humanfriendly Documentation.
