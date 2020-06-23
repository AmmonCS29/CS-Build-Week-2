'''
Understand: 
    -Two linked list that nodes in them
    -values are postive intergers
    -digits are stored in reverse order/ aka right to left
    -each node contains a single digit
    -Add the two numbers and return it as a linked list
    Each list is going to be a total value when put together going left to right. 
    Objective: Add each list together and input the value into nodes in the same order and input
    
Planning:
    - We need to get the values out of the linked lists 
    - put them in the correct order
    - add them together
    - reverse the order of numbers
    - input the values into a linked list
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        list1 = []
        list2 = []
        curr1 = l1
        curr2 = l2
        while curr1 is not None:
            value = curr1.val
            list1.append(value)
            curr1 = curr1.next
        while curr2 is not None:
            value = curr2.val
            list2.append(value)
            curr2 = curr2.next
        
        list1.reverse()
        list2.reverse()
        
        str1 = ''
        for i in list1: 
            str1 += str(i)
        str2 = ''
        for i in list2: 
            str2 += str(i)
        
        new_str1 = int(str1)
        new_str2 =int(str2)
        
        sumof = new_str1 + new_str2
        strsumof = str(sumof)
        
        final_str =[]
        for i in strsumof:
            final_str.append(i)
        
        final_str.reverse()
        ll = ListNode(final_str[0], ListNode(final_str[1], ListNode(final_str[2])))
        
        return ll
        
        
        #ONLY WORKS IF THE SUM IS A 3 DIGIT NUMBER
