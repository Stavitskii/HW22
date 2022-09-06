class Request:
    def __init__(self, info):
        self.info = info.split(" ")
        self.from_ = self.info[4]
        self.to = self.info[6]
        self.amount = int(self.info[1])
        self.product = self.info[2]

    def __repr__(self):
        return f"Доставить {self.amount} {self.product} из {self.from_} в {self.to}."
