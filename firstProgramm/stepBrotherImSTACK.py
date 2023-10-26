#stack its a massiv when have adress next element

#int lenght=1
#stack = []

from ast import Delete
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
    def delete(self,item):
       newstack=[]
       for i in self.stack:
           if(i!=int(item)):
               newstack.append(i)
       self.stack=newstack 
       Delete(newstack)
          

    
        

