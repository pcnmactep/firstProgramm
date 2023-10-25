#stack its a massiv when have adress next element

#int lenght=1
#stack = []

from asyncio.windows_events import NULL

class stack:
    def __init__(self):
        self.stack=[]
        pass
    def push(self,item):
        self.stack.append(item)
        pass
    def pop(self):
        if (len(self.stack)==0): return None

        removed=self.stack.pop()
        return removed

    def get(self):
        return self[len(self)]
        

