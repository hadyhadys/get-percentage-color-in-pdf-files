# import module
from pdf2image import convert_from_path

# Store Pdf with convert_from_path function
images = convert_from_path('file.pdf')

list_white_percent = []
list_black_percent = []
list_greyscale_percent = []
list_non_greyscale_percent = []

for i in range(len(images)):

	# Save pages as images in the pdf
	# images[i].save('page'+ str(i) +'.jpg', 'JPEG')

    # Get the image data in the form of a 2D array
    pixels = images[i].load()

    # Get the image dimensions
    width, height = images[i].size

    # Initialize variables to store the number of black, white, greyscale and non-greyscale pixels
    black_pixels = 0
    white_pixels = 0
    greyscale_pixels = 0
    non_greyscale_pixels = 0

    # Iterate over all the pixels in the image
    for x in range(width):
        for y in range(height):
            # Get the pixel value at (x, y)
            r, g, b = pixels[x, y]

            # Check if the pixel is black (0, 0, 0)
            if r == g == b == 0:
                black_pixels += 1
            elif r == g == b == 255:
                white_pixels += 1
            # Check if the pixel is greyscale (r == g == b)
            elif r == g == b:
                greyscale_pixels += 1
            else:
                non_greyscale_pixels += 1

    # Calculate the percentage of black, white, greyscale and non-greyscale pixels
    total_pixels = width * height
    black_percent = (black_pixels / total_pixels) * 100
    white_percent = (white_pixels / total_pixels) * 100
    greyscale_percent = (greyscale_pixels / total_pixels) * 100
    non_greyscale_percent = (non_greyscale_pixels / total_pixels) * 100

    list_black_percent.append(black_percent)
    list_white_percent.append(white_percent)
    list_greyscale_percent.append(greyscale_percent)
    list_non_greyscale_percent.append(non_greyscale_percent)

print("\n")
print("White: {:.2f}%".format(sum(list_white_percent)))
print("Greyscale: {:.2f}%".format(sum(list_black_percent)+sum(list_greyscale_percent)))
print("Other Color: {:.2f}%".format(sum(list_non_greyscale_percent)))