class songInfo(object):
    def __init__(self, date=None, id=None, timestamp=None, name=None):
        self.date = date
        self.id = id
        self.timestamp = timestamp
        self.name = name

    def get_date(self):
        return self.date

    def get_id(self):
        return self.id

    def get_timestamp(self):
        return self.timestamp

    def get_name(self):
        return self.name


