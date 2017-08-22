from FileManagement.IFileHandler import *

#Brendan
import pickle
import os
import sys
import re



class FileHandler(IFileHandler):

    def load_file(self, file):
        # put error handling here
        print("Loading file...")
        contents = []
        the_file = open(file, 'r')
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
    #Kate
    #
    #
    #Validate data
    
    #validate input for date type
    def valid_date(self, birthday):
        minyear = 1918
        maxyear = date.today().year
        
        mydate = birthday.split('-')
        birthdate = mydate[0]
        birthmonth = mydate[1]
        birthyear = mydate[2]
        
        if (int(birthyear) > maxyear or int(birthyear) < minyear):
            birthdayobj = date(int(birthdate), int(birthmonth), int(birthyear))
            return True
        else:
            print('Year is out of range')
            
     #Validate date match year       
    def valid_age(self, birthday):
        today = date.today()
        mydate = birthday.split('-')
        birthdate = int(mydate[0])
        birthmonth = int(mydate[1])
        birthyear = int(mydate[2])
        age = today.year - born.year\
            - ((today.month, today.day) < (birthmonth, birthdate))
        return age

    #Validate file data
    def validate(self,data):
        """ TestCase for validate
        >>> aFileHandler = FileHandler()
        >>> aFileHandler.validate([("e01","m","20","20","Normal","200","12-06-1998")])
        invalidate data: e01
        invalidate data: m
        invalidate data: 20
        invalidate data: 20
        invalidate data: Normal
        invalidate data: 200
        invalidate data: 12-06-1998
        
        """
        for person in data:
            #check the format is a letter and 3 digit e.g A002 or a002
            
            if (re.match(r'[A-Z][0-9]{3}', (person[0]).lower())):
                print (person[0])
            else:
                print(person[0] + " " + 'is incorrect ID, '
                              ' must contains a letter and 3 digits e.g a002')
            
            #check the format is either M/F/Male/Female
            
            if (person[1] == "M" or (person[1]).upper() == "F" or
                person[1] == "Male" or person[1] == "Female"):
                print (person[1])
            else:
                print(person[1] + " " + 'is incorrect Gender, '
                      ' must either be M and Male or F and Female')
            
            #check age is valid entry and match with date
            
            if (re.match(r'[0-9]{2}', person[2]) and person[2] == self.valid_age(person[6])):
                print (person[2])
            elif (person[2] != self.valid_age(person[2])):
                print("Does not match with your birthday, invalid age")
            else:
                print(person[2] + " " + 'age must be an integer')
    
            #check sales is 3 interger value
            if (re.match(r'[0-9]{3}', person[3])):
                return (person[3])
            else:
                print(person[3] + " " + 'is incorrect sales number, '
                    'must be a 2 interger number')
            
            #check BMI is either Normal / Overweight / Obesity or Underweight
            if (re.match(r'\b(NORMAL|OVERWEIGHT|OBESITY|UNDERWEIGHT)\b',(person[4]).upper())):
                print (person[4])
            else:
                print(person[4] + " " ' is incorrect BMI value, '
                      'must select from Normal, Overweight, Obesity or Underweight')
            
            #check Income is float

            if (re.match(r'[0-9]{2,3}', person[5])):
                print (person[5])
            else:
                print(person[5] + " " + 'is incorrect income, '
                    'must be a interger number')            
            
            #check birthday
            
            if (self.valid_date(person[6]) and person[2] == self.valid_age(person[6]) ):
                print (person[6])
            else:
                print(person[2] + " " + 'is incorrect date format, '
                      'must contain DD-MM-YYYY or DD-MM-YY and seperated by -')
                
        return readFile
    
    # Brendan
    #FILE NAME AND PATH TO BE USER DEFINED IN LATER ITERATION
    def pack_pickle(self, graphs):
        try:
            realFilePath = os.path.dirname(os.path.realpath(sys.argv[0])) + "\\files\\pickle.dat"
            if os.path.exists(realFilePath) == False:
                raise IOError

        except IOError:
            while True:
                answer = input('The file path does not exist, do you wish to create it or abort saving graphs: Y or N')
                if answer == 'y' or answer == 'n': break
                else: print('Please enter a valid option')
            if answer == 'y':
                os.makedirs(os.path.dirname(realFilePath))
                pass
            else: return

        pickleOut = open(realFilePath, "wb")
        pickle.dump(graphs, pickleOut)
        pickleOut.close()

    # Brendan
    #
    #
    #CURRENTLY GRAPHS LOADED BY REFERENCE PROBABLY CHANGE LATER, I AM NOT ENTIRELY HAPPY DOING THAT
    def unpack_pickle(self, filepath):
        try:
            if os.path.exists(filepath) == False:
                raise IOError

        except IOError:
            print('File does not exits')
            return

        pickleIn = open(filepath, "rb")
        graphs = pickle.load(pickleIn)
        pickleIn.close()

        return graphs