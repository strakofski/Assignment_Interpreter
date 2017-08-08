from cmd import *

from Database.SQLDatabase import *
from FileManagement.FileHandler import *


class Interpreter(Cmd):
    file_handler = FileHandler()
    active_data = None
    database = SQLDatabase()

    def do_hello(self, args):
        """this is a test. help hello"""
        print("working")

    def do_write_file(self, args):
        """test"""
        #self.file_reader_writer.write_file("cmd.txt", ['test','test2'])
        args = args.split(' ')
        print(args)
        self.file_handler.write_file(str(args[0]),str(args[1].split(',')))

    def do_load_file(self, args):
        """Loads a file"""
        data = self.file_handler.load_file(args)
        #filter data...

        print(data)

    def do_save_to_database(self, args):
        print("Saving to database!")

    def do_backup_database(self, args):
        data = self.database.backup_database()
        self.file_handler.write_file(args, data)
