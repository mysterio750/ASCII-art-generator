# What is this?
This is an ASCII art generator.
It converts any image into ASCII art using brightness-based pixel mapping.

# How to use it?
We are using a library called Pillow. To install it, open your command prompt and enter this command:

```bash
pip install pillow
```

Then, paste your desired image path into the second line of code:

```python
img = Image.open(r"#Your image path goes here#")
```

Hit Run, and that's it.

# How it actually works...
A pixel is the smallest unit in digital imagery and is what our screens consist of. Technically speaking, a pixel is just a group of three LEDs—RGB (Red, Green, and Blue).

By adjusting the brightness of these three colors, we can trick our brain into perceiving millions of shades of color.

We can even trick our brain into perceiving a color that does not exist as a single wavelength in nature: **Magenta**. To make our brain see this color, we would need to stimulate both the S-cones and L-cones in our eyes simultaneously. This can be done using two photons, one in the range of 420–440 nanometers (nm) and another in the range of 560–565 nm. This combination cannot be represented by a single wavelength of light.

An image is simply a collection of millions of tiny pixels arranged in a way that makes sense to us.

Here is a color image:

![color image](https://cdn.analyticsvidhya.com/wp-content/uploads/2021/03/Screenshot-from-2021-03-16-11-00-53.png)

And here is how it can be represented by adjusting the brightness of RGB values:

![](https://cdn.analyticsvidhya.com/wp-content/uploads/2021/03/Screenshot-from-2021-03-16-11-01-53.png)

For this project, we do not need the brightness values of each individual color because we are working with a grayscale image. We only need the average brightness of each pixel, which can be calculated as:

```text
average brightness = (red + green + blue) / 3
```

The brightness value ranges from 0 to 255.

We then replace each brightness value with a suitable ASCII character. For example, a very bright pixel might be represented by "@", while a very dark pixel might be represented by " " or ".".

Before doing that, we must resize the image because there is no practical way to fit millions of characters in a row on a typical display while keeping the output readable.

# The library we are using
We are using Pillow (PIL):

https://pypi.org/project/pillow/

This library handles most of the work, such as resizing, converting images to grayscale, and extracting pixel values.

# Code

```python
from PIL import Image

img = Image.open(r"")  # Your image path goes here
new_width = 150
new_height = 50
```

* The first line imports the Pillow library.
* The second line uses the `Image.open()` function to load the image into the program.
* The third and fourth lines assign the desired image dimensions to variables.

```python
tiny_img = img.resize((new_width, new_height))
grayscale_img = tiny_img.convert("L")
pixel_data = list(grayscale_img.getdata())
idk = []
```

* The fifth line resizes the image to the desired resolution using the `resize()` function.
* The sixth line converts the image to grayscale using the `convert()` function.
* The seventh line extracts the pixel data using the `getdata()` function and stores it in the `pixel_data` list.
* The eighth line creates an empty list for convenience.

* From lines 10 to 41, the brightness values are replaced with the desired ASCII characters.

*In line 42, all elements of the `idk` list are joined together using the `join()` function.

* And from line 43rd to 46th, a `While` loop is used to print the ASCII characters according to the specified dimensions.
