import urllib.request


def main(url):
    print("Checking connectivity ")

    response = urllib.request.urlopen(url)
    print("Connected to", url, "succesfully")
    print("The response code was:", response.getcode())


print("This is a site connectivity checkout program. ")
input_url = input("Input the url you want to check: ")


main(input_url)
