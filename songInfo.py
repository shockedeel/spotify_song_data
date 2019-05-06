class songInfo:
    def __init__(self,date=None,id=None,timestamp=None,name=None):
        self.date=date
        self.id=id
        self.timestamp=timestamp
        self.name=name
    def getDate(self):
        return self.date
    def getId(self):
        return self.id
    def getTimestamp(self):
        return self.timestamp
    def getName(self):
        return self.name

