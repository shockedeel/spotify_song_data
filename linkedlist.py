import node
class linkedlist(object):
    def __init__(self,head=None):
        self.head=head
    def add(self,data):
        #adds to front of list
        #why? faster in the long run with more recent things added first
        n = node(data)
        if self.head is None:
            head=n
            return

        temp=self.head
        self.head=n
        self.head.set_next(temp)
    def get_head(self):
        return self.head
    








#implement