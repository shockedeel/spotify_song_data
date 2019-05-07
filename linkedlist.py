import node



class linkedlist(object):

    head: node

    def __init__(self,head=None):
        self.head=head

    def add(self,data):
        #adds to front of list
        #why? faster in the long run with more recent things added first
        n = node.node(data=data)
        if self.head is None:
            head = n
            return
        temp = self.head
        self.head = n
        self.head.set_next(temp)

    def get_head(self):
        return self.head

    def print(self):

        iter=self.head
        print(type(iter))
        while iter is not None:
            print(iter.data.get_id())









#implement