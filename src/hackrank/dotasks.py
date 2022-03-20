

class Process:
    def __init__(self, commands):
        self.list = []
        self.commands = commands

    def insert(self, i, e):
        self.list.insert(int(i), int(e))

    def append(self, e):
        self.list.append(int(e))

    def remove(self, e):
        e = int(e)
        tmp = []
        x = True
        for i in self.list:
            if i == e and x == True:
                x = False
            else:
                tmp.append(i)

        self.list = tmp


    def process(self):
        for com in commands:
            com = com.split()
            if com[0] == "insert":
                self.insert(com[1], com[2])
            if com[0] == "append":
                self.append(com[1])
            if com[0] == "remove":
                self.remove(com[1])
            if com[0] == "print":
                print(self.list)
            if com[0] == "sort":
                self.list.sort()
            if com[0] == "pop":
                self.list.pop()
            if com[0] == "reverse":
                self.list.reverse()

if __name__ == '__main__':
    N = int(input())
    commands = []
    lst = []
    for _ in range(N):
        commands.append(input())
    process = Process(commands)
    process.process()