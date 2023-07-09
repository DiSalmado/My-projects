from PIL import Image


def resize_image(size1, size2):
    image = Image.open('tipos-de-cara.jpg')

    print(f"Current size : {image.size}")

    resized_image = image.resize((size1, size2))

    resized_image.save('tipos-de-cara-' + str(size1) + '.jpeg')


size1 = int(input("Input the Width: "))
size2 = int(input("Input the Lenght: "))
resize_image(size1, size2)
