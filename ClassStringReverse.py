class rev:
    def __init__(self, str):
        self.str = str
    def returnrevfunc(self):
        temp = ""
        for i in range(len(self.str)):
            temp += self.str[-i - 1]
        return temp

reverse = rev("reverse")
print(reverse.returnrevfunc())