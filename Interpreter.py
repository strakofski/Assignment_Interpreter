from cmd import *
from Database.SQLDatabase import *
from FileManagement.FileHandler import *
from Graph import *


class Interpreter(Cmd):

    def __init__(self):
        Cmd.__init__(self)
        self.file_handler = FileHandler()
        self.active_data = None
        self.graph = []
        self.database = SQLDatabase()

    def do_write_data(self, args):
        convert = tuple(args.split(','))
        data = [convert]
        self.database.write_to_database(data)

    # Kris
    # Pull data from database
    def do_display_data(self, args):
        self.database.display_data()

    # Kris Little
    # - This function loads and saves data to the database
    def do_load_from_file(self, args):
        args = args.split(' ')
        file_path = ""
        optn = ""
        if len(args) == 1:
            file_path = args[0]
            data = self.file_handler.load_file(file_path)
            self.database.write_to_database(data)
        elif len(args) == 2:
            file_path = args[1]
            optn = args[0]
            if "-d" in optn:
                data = self.file_handler.load_file(file_path)
                self.database.write_to_database(data)
            elif "-g" in optn:
                print("creating graph")
            else:
                print("Invalid option. Refer to help file")

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
        return self.database.cursor.fetchall()

    # Brendan Holt
    # get data by calling the command execute_sql
    # data should be returned as an array holding tuples, keep this in mind
    # feel free to add other graph commands e.g. def do_display_piechart(self, args)
    # (args being data)
    def do_create_graph(self, args):
        print("This will display a graph once Brendan has implemented it!")
        self.database.execute_sql("""select * from employee""")
        data = self.database.cursor.fetchall()
        filename = args
        new_graph = Graph(data, filename)
        self.graph.append(new_graph)

        # display graph ? maybe an option in here to not display the graph right away?

    def do_list_graphs(self, args):
        for g in range(len(self.graph)):
            print(g, self.graph[0].file)

    # Brendan Holt
    # write actual unpack code in the FileHandler class
    # args being file name e.g. pickle_pack file.pickle
    # save all graphs
    def do_save_graphs(self, args):
        for g in self.graph:
            self.file_handler.pack_pickle(g, g.file)

    # Brendan Holt
    # write actual unpack code in the FileHandler class
    # args being filename e.g. pickle_unpack
    def do_load_graphs(self, args):
        filepath = args
        graph = self.file_handler.unpack_pickle(filepath)
        self.graph.append(graph)

    # Help Commands - Kate
    # For each of the do_ commands above, print help info about them
    # Following this format: help_function
    # e.g. help_write_data(self):
    # for info on what each function does, check out the help.doc file
    def help_write_data(self):
        # Example for Kate
        print("help on write data")

    #
    def emptyline(self):
        pass
