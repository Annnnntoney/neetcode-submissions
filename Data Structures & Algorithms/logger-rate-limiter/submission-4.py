class Logger:

    def __init__(self):
        self.lookup = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.lookup:
            self.lookup[message] = timestamp
            return True
        else:
            interval = timestamp - self.lookup[message]
            if interval >= 10:
                self.lookup[message] = timestamp
                return True
            else:
                return False
