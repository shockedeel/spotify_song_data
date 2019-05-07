class node(object):
    def __init__(self, data=None, next = None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, n):
        self.next = n

    def set_data(self, n):
        self.data = n


