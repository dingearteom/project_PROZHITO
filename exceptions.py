class Error(Exception):
    """
    custom base class for exceptions
    """
    pass

class Mix(Error):

    def __init__(self, message='Documents are not the same in mixing'):
        self.message = message

