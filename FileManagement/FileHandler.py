from FileManagement.IFileHandler import *
from pickle import *


class FileHandler(IFileHandler):

    def load_file(self, file):
        # put error handling here
        print("Loading file...")
        contents = []
        try:
            the_file = open(file, 'r')
        except FileNotFoundError as e:
            print(e)
            return False
        else:
            for line in the_file:
                line = tuple(line.replace('\n', "").split(','))
                contents.append(line)
            print(contents)
            the_file.close()
            return contents

    def write_file(self, file, data):
        the_file = open(file, 'w')
        string = ""
        for l in data:
            new_data = [l[0], l[1], l[2], l[3], l[4], l[5], l[6]]
            for i in range(len(new_data)):
                string += str(new_data[i])
                # prevent a space at the end of a line
                if i != len(new_data) - 1:
                    string += ','

            string += "\n"
        the_file.write(string)
        the_file.close()

    # Kate
    #
    #
    #
    def validate_data(self, data):
        print("put code validation here")
        return data

    # Brendan
    #
    #
    #
    def pack_pickle(self, obj, file):
        print("code here brendan")

    # Brendan
    #
    #
    #
    def unpack_pickle(self, file):
        print("code here brendan")

        return False