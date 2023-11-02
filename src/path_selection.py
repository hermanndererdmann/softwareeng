import os

class path_selection:
    def __init__(self):
        # Prompt user for path input
        self.path = input("Please enter the log file path (or press enter to use the current directory): ").strip()
        # Check if the path is empty (use current directory with default filename)
        if not self.path:
            self.path = os.path.join(os.getcwd(), 'logs.csv')
        # If a directory is given without a file, append the default filename
        elif os.path.isdir(self.path):
            self.path = os.path.join(self.path, 'logs.csv')
        # If a path is given but it does not contain an extension, append '.csv'
        elif not os.path.splitext(self.path)[1]:
            self.path += '.csv'

    def get_path(self):
        # Method to return the selected path
        return self.path
