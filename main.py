# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from pymongo import MongoClient

def client():
    cloud_URI = "mongodb+srv://evan:evan@cassavaleaf.elaid.mongodb.net/<dbname>?retryWrites=true&w=majority"
    client = MongoClient(cloud_URI)
    return client

def getDatabase(client):
    for db in client.list_databases():
        print(db)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    client = client()
    getDatabase(client)
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
