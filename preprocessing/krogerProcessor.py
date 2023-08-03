import configparser
import pandas as pd
from preprocessing.processorTemplate import Executor


class KrogerPreprocessor(Executor):

    def __init__(self):
        super().__init__()
        self.config = configparser.RawConfigParser()
        self.config.read('./preprocessing/mappings/kroger.properties')
        self.input_data = pd.read_csv("./preprocessing/input_files/kroger/kroger_stores.csv")

    def execute(self):

        super().execute()



