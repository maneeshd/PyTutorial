from random import randint
from urllib import request


def download_img(url):
    num = randint(1, 1000)
    file_name = "ManUtd_" + str(num) + ".png"
    request.urlretrieve(url, file_name)


def main():
    url = "https://lh3.googleusercontent.com/-iDzlv7IG4rY/AAAAAAAAAAI/AAAAAAACsik/FnDXDKxLt5I/s0-c-k-no-ns/photo.jpg"
    download_img(url)

if __name__ == '__main__':
    main()
