import time

class Stack:

    class _Node:
        __slots__ = ['data','next']
        def __init__(self, data = None, next=None): 
            self.data = data
            self.next = next

    def __init__(self) -> None:
       self.head = None
    
    def push(self, data):
        self.head = self._Node(data,self.head)
    
    def pop(self):
        if(self.head != None):
            self.head = self.head.next
        return

    def is_empty(self) -> bool:
        if(self.head == None):
            return True
        return
    
    def top(self):
        if(self.head != None):
            return self.head.data

def findPositionandDistance(P):
    stack = Stack()
    stack.push(1)
    x,y,z,d,sign,i = 0,0,0,0,1,2
    while(i<len(P)):
        ascii = ord(P[i])
        if(ascii == 39):
            i+=1 
            break
        if(ascii == 40):
            i+=1 
            continue
        if(ascii == 41):
            stack.pop()
            i+=1
            continue
        if(ascii == 43): 
            sign=1
            i+=1
            continue
        if(ascii == 45): 
            sign=-1
            i+=1
            continue
        if(ascii >= 48 and ascii <= 57):
            numstr = ""
            while(ord(P[i])>=48 and ord(P[i])<=57):
                numstr += P[i]
                i+=1
            stack.push(stack.top()*int(numstr))
            continue
        if(ascii == 88):
            x += sign*stack.top()
            d += stack.top()
            i+=1
            continue
        if(ascii == 89):
            y += sign*stack.top()
            d += stack.top()
            i+=1
            continue
        if(ascii == 90):
            z += sign*stack.top()
            d += stack.top()
            i+=1
            continue
        else: i+=1
    return [x,y,z,d]

start_time = time.time()
print(findPositionandDistance(input()))
print("--- %s seconds ---" % (time.time()-start_time))