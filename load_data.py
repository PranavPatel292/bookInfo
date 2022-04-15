import os
from flask import *

# function which will load the data into the memory and then return them to  main.py file.

def load_file():
    fileName = os.path.join("./", 'data.json')

    with open(fileName) as test_file:
        data = json.load(test_file)
    print("data loaded!")
    return data