from TheView.IVIew import *

class ConsoleView(IView):
    def say(self, message):
        print("CONSOLE: " + message)
