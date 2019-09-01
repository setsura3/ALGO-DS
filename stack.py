
class Stack():
    def __init__(self):
        self.ele = []

    def push(self, ele):
        self.ele.append(ele)

    def pop(self):
        return self.ele.pop()

    def get_stack(self):
        return self.ele
    def is_empty(self):
        return self.ele == []

    def peek(self):
        if len(self.ele) > 0:
            return self.ele[-1]
        else:
            print('stack doesnt exist')
    def appendString(self,str):
        for i in range(len(str)):
            self.ele.append(str[i])



#valid parentheses有效的括号
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        #use mapping 
        judge = {'()', '[]', '{}'}
        for i in s:
            #if stack is empty, add the char to stack
            if not stack:
                stack.append(i)
            else:
              #if the last element of stack and the current stack can pair up, delete it
                if stack[-1] + i in judge:
                    stack.pop()
                else:
                    stack.append(i)

        return stack == []


a = Solution()
a.isValid('({[]})')
