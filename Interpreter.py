from cmd import *
from Database.SQLDatabase import *
from FileManagement.FileHandler import *
from Graph import *


class Interpreter(Cmd):

    def __init__(self):
        Cmd.__init__(self)
        self.file_handler = FileHandler()
        self.active_data = None
        self.graph = Graph()
        self.database = SQLDatabase()

    def do_write_data(self, args):
        convert = tuple(args.split(','))
        data = [convert]
        self.database.write_to_database(data)

    def do_display_data(self, args):
        self.database.display_data()

    # Kris Little
    # - This function loads and saves data to the database
    def do_save_file_to_database(self, args):
        print("Saving to database!")
        file_path = args
        data = self.file_handler.load_file(file_path)
        self.database.write_to_database(data)

    # Kris Little
    # backup the database. This could be changed to use the pickle
    # function brendan makes soon
    def do_backup_database(self, args):
        data = self.database.backup_database()
        self.file_handler.write_file(args, data)

    # Kris
    # This gets all data from the database
    def do_get_data(self, sql):
        self.database.execute_sql(sql)
        print(self.database.cursor.fetchall())
        return self.database.cursor.fetchall()

    # Brendan Holt
    # get data by calling the command execute_sql
    # data should be returned as an array holding tuples, keep this in mind
    # feel free to add other graph commands e.g. def do_display_piechart(self, args)
    # (args being data)
    def do_display_graph(self, args):
        print("This will display a graph once Brendan has implemented it!")
        self.database.execute_sql("""select * from employee""")
        data = self.database.cursor.fetchall()
        self.graph.do_something()

    # Brendan Holt
    # write actual unpack code in the FileHandler class
    #
    def do_pickle_pack(self, args):
        print("save")
        self.file_handler.pack_pickle(args)

    # Brendan Holt
    # write actual unpack code in the FileHandler class
    #
    def do_pickle_unpack(self, args):
        self.file_handler.unpack_pickle(args)

    # Help Commands - Kate
    # For each of the do_ commands above, print help info about them
    # Following this format: help_function
    # e.g. help_write_data(self):
    # for info on what each function does, check out the help.doc file
    def help_write_data(self):
        # Example for Kate
        print("help on write data")

    def emptyline(self):
        pass
