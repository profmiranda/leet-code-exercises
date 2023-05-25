import math


class Solution:
    roman_dict = [
        ["I", 1],
        ["IV", 4],
        ["V", 5],
        ["IX", 9],
        ["X", 10],
        ["XL", 40],
        ["L", 50],
        ["XC", 90],
        ["C", 100],
        ["CD", 400],
        ["D", 500],
        ["CM", 900],
        ["M", 1000]]
    
    def intToRoman(self, num: int ) -> str:
        roman_string = ''    
        number_of_chars = 0
        for i, r in reversed(list(enumerate(self.roman_dict))):
            # print(f' i={i}, r={r}')
            number_of_chars = math.floor(num/r[1])
            # print(f' number_of_chars={number_of_chars}')
            num = num % r[1]
            # print(f' next num={num}')
            if num == 0 and number_of_chars == 0:
                break
            else:
                roman_string += self.roman_dict[i][0] * number_of_chars
                # print(f' roman_string={roman_string}')
        return roman_string



if __name__ == "__main__":
    c = Solution()
    print(c.intToRoman(134))
    print(c.intToRoman(1349))
    print(c.intToRoman(1994))