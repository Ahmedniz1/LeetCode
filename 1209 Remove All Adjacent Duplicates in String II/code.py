from tracemalloc import start


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack=[['$',0]]
        for c in s:
            if stack[-1][0]==c:
                stack[-1][1]+=1
                if stack[-1][1]==k:
                    stack.pop()
            else:
                stack.append([c,1])
        output=''
        for i in range(len(stack)):
            output+=stack[i][0]*stack[i][1]
        return output

temp=Solution()
print("deeedbbcccbdaa")
print(temp.removeDuplicates("deeedbbcccbdaa",3))
print(temp.removeDuplicates("pbbcggttciiippooaais",2))
