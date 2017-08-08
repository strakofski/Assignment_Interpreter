from cmd import *
from Database.SQLDatabase import *
from FileManagement.FileHandler import *


class Interpreter(Cmd):
    file_handler = FileHandler()
    active_data = None
    database = SQLDatabase()

    def do_write_data(self, args):
        convert = tuple(args.split(','))
        data = [convert]
        self.database.write_to_database(data)

    def do_display_data(self, args):
        self.database.display_data()

    def do_save_file_to_database(self, args):
        print("Saving to database!")
        data = []
        filepath = args
        file_contents = self.file_handler.load_file(filepath)
        print(file_contents)

        #self.database.write_to_database(data)

    def do_backup_database(self, args):
        data = self.database.backup_database()
        self.file_handler.write_file(args, data)

    def do_get_data(self, sql):
        self.database.execute_sql(sql)
        print(self.database.cursor.fetchall())

    def help_write_data(self):
        print("write_file <data>")
        print("Writes data to a file")

    def help_backup_database(self):
        print("backup_database <filepath>")
        print("Saves the Data to a text file")

    def help_save_to_database(self):
        print("save_to_database <filepath>")
        print("Loads a file and saves data to the database.")

    def help_get_data(self):
        print("get_data <sql>")
        print("Executes and SQL script.")

    def emptyline(self):
        pass
