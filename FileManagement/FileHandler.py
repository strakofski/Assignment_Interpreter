from FileManagement.IFileHandler import *


class FileHandler(IFileHandler):
    def __init__(self):
        print("created")

    def load_file(self, file):
        #put error handling here
        print("Loading file...")
        contents = []
        the_file = open(file, 'r')
        for line in the_file:
            line = line.replace('\n',"")
            line = line.split(',')
            line = tuple(line)
            print(line)
            contents.append(line)
        return contents

    def write_file(self, file, data):
        the_file = open(file, 'w')
        string = ""
        for l in data:
            new_data = [l[0], l[1], l[2], l[3], l[4], l[5], l[6]]
            for d in new_data:
                string += str(d)

            string += "\n"
        the_file.write(string)

    def validate_data(self, data):
        print("put code validation here")

    def clean_data(self, data):
        print("data cleaned")