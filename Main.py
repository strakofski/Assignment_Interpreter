from Interpreter import *

if __name__ == "__main__":

    the_interpreter = Interpreter()
    the_interpreter.prompt = '> '
    the_interpreter.database.setup()
    the_interpreter.cmdloop('Starting')
