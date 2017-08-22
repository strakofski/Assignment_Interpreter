import unittest
import Validator
import FileHandler

class ValidatorTest(unittest.TestCase):
    def setUp(self):
        self.readFile = reader.FileHandler()
        self.validateFile = Validator.Validation()
        
    def tearDown(self):
        print("exit")
        
    def test_isValidFormat_IsEqual(self):
        print("Check Valid input format")
        test = [("e01","m","20","20","Normal","200","12-06-1998")]
        self.read.read("testFile.txt")
        self.assertEqual(r, testData, 'Not a valid file')
        
    def test_isNoteValidFormat_IsFalse(self):
        print("Check Valid input format")
        test = [("e01","m","20","20","Normal","200","12-06-1998")]
        self.read.read("testFile2.txt")
        self.assertFalse(r, testData, 'is a valid file')
        
    def test_isValidAge_IsEqual(self):
        print("Check Valid input age match the date")
        age = self.validateFile.valid_age('12-06-1999')
        self.assertFalse(age, 20, 'Age does not match')
    
    
    def test_isNotValidAge_IsNotEqual(self):
        print("Check Valid input age match the date")
        age = self.validateFile.valid_age('12-06-1999')
        self.assertNotEqual(age, 26, 'Age does not match')
    
    def test_isValidDate_IsTrue(self):
        print("Check Valid input date")
        date = self.validateFile.valid_date('12-06-1999')
        self.assertTrue(date == True, 'Date is wrong')
    
    def test_isValidDate_IsFalse(self):
        print("Check Valid input date")
        date = self.validateFile.valid_date('12-06-1999')
        self.assertFalse(date == False, 'Date is wrong')

    def test_isValidDateAgainstAge_IsEqual(self):
        print("check if age match date")
        testData = ("e01","m","20","20","Normal","200","12-06-1998")
        age = self.validateFile.valid_age('12-06-1998')
        self.assertEqual(age, int(testData[3]), 'Age doesn"t match')

    def test_isValidDateAgainstAge_IsNotEqual(self):
        print("check if age match date")
        testData = ("e01","m","25","20","Normal","200","12-06-1998")
        age = self.validateFile.valid_age('12-06-1998')
        self.assertNotEqual(age, int(testData[3]), 'Age doesn"t match')
        
        if __name__ == "__main__":
            unittest.main()
            