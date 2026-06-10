class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for i in asteroids:
            while(stack and i<0 and stack[-1]>0):
                if(abs(i)>stack[-1]):
                    stack.pop()
                elif(abs(i)<stack[-1]):
                    i=0
                else:
                    stack.pop()
                    i=0
            if i:
                stack.append(i)
        return stack
                