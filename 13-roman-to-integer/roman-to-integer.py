class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_to_int = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        count = 0
        length = len(s)

        for i in range(length):
            current_value = roman_to_int[s[i]]
            #subtract if roman digit is less than the next digit ( going left to right approach)
            if i < length - 1 and current_value < roman_to_int[s[i + 1]]:
                count -= current_value
            else:
                count += current_value

        return count