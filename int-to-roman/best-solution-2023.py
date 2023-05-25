# FROM: https://leetcode.com/problems/integer-to-roman/submissions/957135613/

class Solution:
    def intToRoman(self, num: int) -> str:
        def choose_int(int_list, x):
            res = int_list[0]
            for k in int_list:
                if k <= x:
                    res = k
                else:
                    break
            return res
            
        roman = ""
        int2rom = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M',}
        int_cand = list(int2rom.keys())
        int_cand.sort()
        while num > 0:
            cur = choose_int(int_cand, num)
            roman += int2rom[cur]
            num -= cur

        return roman