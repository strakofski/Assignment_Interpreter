from FileManagement.IFileHandler import *


class FileHandler(IFileHandler):
    def __init__(self):
        print("created")

    def load_file(self, file):
        # put error handling here
        print("Loading file...")
        contents = []
        the_file = open(file, 'r')
        for line in the_file:
            line = line.replace('\n',"")
            line = line.split(',')
            line = tuple(line)
            contents.append(line)
        print(contents)
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

    # Kate
    #
    #
    #
    def validate_data(self, data):
        print("put code validation here")
        return data
