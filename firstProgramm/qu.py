

class queue:


    def add(self,item):
        self.queue.append(item)
        pass
    
    def delete(self,item):
       newqueue=[]
       for i in self.queue:
           if(i!=int(item)):
               newqueue.append(i)
       self.queue=newqueue 

    def get(self):
        if(len(self.queue)==0):return None
        newqueue=[]
        first = self.queue[0]
        for i in self.queue:
            if(i!=first):newqueue.append(i)
            
        self.queue=newqueue
        return first
            
    
    
    def __init__(self):
        self.queue=[]
        pass