Planning:
    -create integer stack and letter stack
    -create a final string variable
    -iterate over the string
    -if value of string is equal to a Number
        -append it to the integer stack
    -else if value is eqaul to [ or ]
        -pop to bracket stack
    -else append it to the letter stack
'''

class Solution:
    def decodeString(self, s: str) -> str:
        #Initialize data structure
        stack, res, num = [], '', 0
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c.isalpha():
                res += c
            elif c == '[':
                #Tuple form stacking
                stack.append((res, num))
                #Refresh strings and number of repetitions
                res, num = '', 0
            else:
                #If c==']', pop-up strings and number of repetitions
                last_str, this_num = stack.pop()
                res = last_str + this_num * res
        return res
