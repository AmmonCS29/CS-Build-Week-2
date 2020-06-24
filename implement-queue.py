'''
Understanding:
implement the following operations of a queue using stacks
    -push will push an element to the back of the queue
    -pop will remove the element from the front of the queue
    - peek getst the front element of the queue
    -empty returns true or false if it is empty

Planning:
-Instantiation is the Queue’s storage object that will be used.
-push(val) is the way to add data to the Queue.
-pop() is the way to remove and return the front element in the Queue.
-peek() is the way to return the front element without removing it.
-empty() is the way to tell if a Queue is empty and contains any values.
'''

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.stack) > 0:
            
            return self.stack.pop(0)
        else:
            return None

    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.stack):
            return self.stack[0]
        else:
            return None
    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if len(self.stack) > 0:
            return False
        else:
            return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
