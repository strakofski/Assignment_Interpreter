import re
from datetime import date
from FileManagement.FileHandler import *


class Validation(object):
    ''' Check if the data is valid data type or format '''
    def __init__(self,readFile=None):
        self.readFile = load_file()
        for person in self.ReadFile:
            self.length = int(len(person))
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
            
    def valid_age(self, birthday):
        today = date.today()
        mydate = birthday.split('-')
        birthdate = int(mydate[0])
        birthmonth = int(mydate[1])
        birthyear = int(mydate[2])
        age = today.year - born.year\
            - ((today.month, today.day) < (birthmonth, birthdate))
        return age

        
    def validate(self):
        for person in range(0, self.length):
            #check the format is a letter and 3 digit e.g A002 or a002
            if (re.match(r'[A-Z][0-9]{3}', (self.readFile[person][0]).lower())):
                print (self.readFile[person][0])
            else:
                print(self.readFile[person][0] + " " + 'is incorrect ID, '
                              ' must contains a letter and 3 digits e.g a002')
            
            #check the format is either M/F/Male/Female
            
            if (self.readFile[person][1] == "M" or (self.readFile[person][1]).upper() == "F" or
                self.readFile[person][1] == "Male" or self.readFile[person][1] == "Female"):
                print (self.readFile[person][1])
            else:
                print(self.readFile[person][1] + " " + 'is incorrect Gender, '
                      ' must either be M and Male or F and Female')
            
            #check age is valid entry and match with date
            
            if (re.match(r'[0-9]{2}', self.readFile[person][2]) and self.readFile[person][2] == self.valid_age(self.readFile[person][6])):
                print (self.readFile[person][2])
            elif (self.readFile[person][2] != self.valid_age(self.readFile[person][2])):
                print("Does not match with your birthday, invalid age")
            else:
                print(self.readFile[person][2] + " " + 'age must be an integer')
    
            #check sales is 3 interger value
            if (re.match(r'[0-9]{3}', self.readFile[person][3])):
                return (self.readFile[person][3])
            else:
                print(self.readFile[person][3] + " " + 'is incorrect sales number, '
                    'must be a 2 interger number')
            
            #check BMI is either Normal / Overweight / Obesity or Underweight
            if (re.match(r'\b(NORMAL|OVERWEIGHT|OBESITY|UNDERWEIGHT)\b',(self.readFile[person][4]).upper())):
                print (self.readFile[person][4])
            else:
                print(self.readFile[person][4] + " " ' is incorrect BMI value, '
                      'must select from Normal, Overweight, Obesity or Underweight')
            
            #check Income is float

            if (re.match(r'[0-9]{2,3}', self.readFile[person][5])):
                print (self.readFile[person][5])
            else:
                print(self.readFile[person][5] + " " + 'is incorrect income, '
                    'must be a interger number')            
            
            #check birthday
            
            if (self.valid_date(self.readFile[person][6]) and self.readFile[person][2] == self.valid_age(self.readFile[person][6]) ):
                print (self.readFile[person][6])
            else:
                print(self.readFile[person][2] + " " + 'is incorrect date format, '
                      'must contain DD-MM-YYYY or DD-MM-YY and seperated by -')
                
        return readFile
               
             
           