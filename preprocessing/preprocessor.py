import configparser
import preprocessing
from preprocessing.walmartProcessor import WalmartPreprocessor
from preprocessing.krogerProcessor import KrogerPreprocessor
from preprocessing.errorHandler import ErrorPreprocessor


class Preprocessor:

    def __init__(self, vendor):
        self.vendor = vendor
        self.config = configparser.RawConfigParser()
        self.config.read('./preprocessing/mappings/mapping.properties')

    def execute(self):
        details_dict = dict(self.config.items('VENDOR_OBJECT_MAPPING'))
        try:
            obj = eval(details_dict[self.vendor])()
        except KeyError as e:
            obj = eval(details_dict['error'])()

        obj.execute()




