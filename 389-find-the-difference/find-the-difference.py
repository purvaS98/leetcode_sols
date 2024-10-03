class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result = 0
        for char in s:
            result ^= ord(char)  # XOR all characters in string s
        for char in t:
            result ^= ord(char)  # XOR all characters in string t
            
        return chr(result)

        '''j = 0
        result = ''  # To store the extra character from 't'
        
        # Loop through each character in 't'
        for i in range(len(t)):
            # If 'j' is within bounds and characters at 'j' and 'i' don't match
            if j < len(s) and s[j] != t[i]:
                result = t[i]  # Capture the different character from 't'
            else:
                # Increment 'j' only if characters match
                if j < len(s):
                    j += 1
        
        # If no mismatch was found, the last character in 't' is the extra one
        if result == '':
            result = t[-1]
            
        return result'''


  
