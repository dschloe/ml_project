# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from pymongo import MongoClient
from PIL import Image
import io
from bson.binary import Binary
import matplotlib.pyplot as plt


def client():
    cloud_URI = "mongodb+srv://evan:evan@cassavaleaf.elaid.mongodb.net/<dbname>?retryWrites=true&w=majority"
    client = MongoClient(cloud_URI)
    return client

def getDatabase(client):
    return client.list_database_names()

def inputImages(client):
    images = client.casava_images.train
    im = Image.open("img/image01.png")
    image_bytes = io.BytesIO()
    im.save(image_bytes, format='png')
    image = {
        'data': image_bytes.getvalue()
    }

    image_id = images.insert_one(image).inserted_id
    print("Done")
    return image_id

def read_image(client):
    images = client.casava_images.train
    image = images.find_one()

    pil_img = Image.open(io.BytesIO(image['data']))
    plt.imshow(pil_img)
    plt.show()

def image_upload():
    return None

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    client = client()
    print(getDatabase(client))
    print(inputImages(client))
    read_image(client)
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
