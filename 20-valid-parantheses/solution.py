class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"{" : "}",
                 "(" : ")",
                 "[" : "]"}


        need = []

        for ch in s:
            if ch in pairs:
                need.append(pairs[ch])

            else:
                if not need:
                    return False

                val = need.pop()
                if val != ch:
                    return False

        if need:
            return False
        return True




'''
this one is pretty simple
basically use a stack to track the order that the brackets need to be closed
use a dict to store the pairs
when u see an open one, append its closing one to the stack
then when a clsing one is found, verify that it matches and pop

if at any point it doesnt match or if there is still some unclosed ones at end = return false

Time: O(n)
Space: O(n + 3) = O(n) worst case if all open


'''