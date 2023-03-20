# Install pillow if you haven't
# Import pillow
# Open up the image we want to resize using Python
# Print the current size os that image
# Specify the size we wanna change it to
# Save the new resized image

from PIL import Image


def resize_image(image, size1, size2):
    resized_image = image.resize((size1, size2))
    resized_image.save("img_resized-" + str(size1) + "x" + str(size2) + ".png")


def main():
    image = Image.open("qrimg.png")
    print(f"Current size: {image.size}")
    size1 = int(input("Enter Width: "))
    size2 = int(input("Enter Height: "))
    resize_image(image, size1, size2)


if __name__ == "__main__":
    main()
