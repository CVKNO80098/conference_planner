import pandas as pd

class FileReader:

    def __init__(self, file_path):
        self.data = None
        self.file_path = file_path
        self.read_file()


    def read_file(self):
        try:
            self.data = pd.read_excel(self.file_path, keep_default_na=False)
        except FileNotFoundError:
            print("File not found!")

    def dataframe_to_list(self):
        return self.data.values.tolist()


