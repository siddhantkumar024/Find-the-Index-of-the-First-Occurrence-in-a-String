Method 1 built in approach:

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if needle in haystack:
            index=haystack.find(needle)
            return index
        else:
            return -1

            


Method 2:
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        x=len(haystack)
        y=len(needle)
        /* Set Up the Loop: We iterate through each valid starting position in haystack: The loop runs from i = 0 to i = x - y (inclusive) This gives us exactly x - y + 1 positions to checkWe use range(x - y + 1) to generate these indices 
        if x= 9 and y =3  valid place are x-y = 6   so we range it from 0 to 7   loop run 0 - 6 */
        for i in range (x-y+1):
            if haystack[i:i+y]== needle:
                return i
        return -1
