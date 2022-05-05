class MyStack:
    my_stack=[]
    def __init__(self):
        self.my_stack=[]

    def push(self, x: int) -> None:
        q1=self.my_stack.copy()
        q2=[]
#        q2.append(x)
        # could have written q2=[x]+q1[::-1] but wanted to show how queue works
        #first emptying the queue 
        for i in range (len(q1)-1, -1, -1):
            q2.append(q1.pop(i))          
        # now adding the new element to q1
        q1.append(x)
        # now adding all the elements back to q1
        for i in range(len(q2)-1, -1, -1):
            q1.append(q2.pop(i))          
        self.my_stack=q1        
    def pop(self) -> int:    
        return self.my_stack.pop(0)
    def top(self) -> int:
        return self.my_stack[0]

    def empty(self) -> bool:
        if len(self.my_stack)==0:
            return True
        return False 


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()