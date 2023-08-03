from preprocessing.processorTemplate import Executor


class ErrorPreprocessor(Executor):

    def execute(self):
        print("Incorrect vendor name, please try again !!!")

