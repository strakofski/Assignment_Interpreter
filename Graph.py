class Graph:

    def __init__(self):
        self.data = None
        #NEW Brendan
        self.title = None
        self.type =None
        self.colours = None
        self.labels = None
        self.angle = None

    #CURRENTLY THIS IS DEAD CODE
    def set_data(self, new_graph):
        self.data = new_graph.data
        #NEW Brendan
        self.title = new_graph.title
        self.type = new_graph.type
        self.colours = new_graph.colours
        self.labels = new_graph.labels
        self.angle = new_graph.angle

    # temp function
    def do_something(self):
        print("doing something")
