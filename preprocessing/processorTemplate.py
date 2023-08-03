from abc import abstractmethod


class Executor:

    def __init__(self):
        self.config = None
        self.input_data = None

    @abstractmethod
    def execute(self):

        column_mapping = dict(self.config.items('stores'))
        try:
            self.input_data = self.input_data[column_mapping.keys()]
            self.input_data = self.input_data.rename(columns=column_mapping)
            self.input_data.to_csv("./preprocessing/output/converted.csv", index=False)
            print("converted file successfully saved in 'preprocessing/output' folder as converted.csv")
        except KeyError as e:
            print(e)
