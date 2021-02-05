# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from pymongo import MongoClient

# from _db._pymongo import DataBase
# from pprint import pprint

def _mongo():

    cloud_URI = "mongodb+srv://evan:<password>@cassavaleaf.elaid.mongodb.net/<dbname>?retryWrites=true&w=majority"
    client = MongoClient(cloud_URI)

    print(client)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    _mongo()
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
