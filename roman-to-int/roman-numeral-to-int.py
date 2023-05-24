import re


class Solution:
    _roman_set_re = '[IVXLCDM]+$'
    total = 0

    def romanToInt(self, s: str) -> str:
        self.total = 0
        if not (len(s) > 0 and len(s) < 16):
            return -1
        result = re.match(self._roman_set_re, s)

        if result is not None:
            i = 0
            last = False
            while i <= len(s)-1:
                # print(i)
                # print(ord(s[i]))
                # print(len(s))
                if (i == (len(s)-1)):  # last digit
                    last = True
                if (s[i] == 'I'):
                    # can only be IV, IX, or I, II, III, IIII
                    if (last == False and s[i+1] != 'I'):
                        if s[i+1] == 'V':
                            self.total = self.total + 4  # IX - 9 or IV - 4
                            i += 2
                            continue
                        if s[i+1] == 'X':
                            self.total = self.total + 9
                            i += 2
                            continue
                    self.total = self.total + 1
                elif (s[i] == 'X'):  # L and C
                    if (last == False and s[i+1] != 'X'):
                        if s[i+1] == 'L':
                            self.total = self.total + 40  # XL - 40 or XC - 90
                            i += 2
                            continue
                        if s[i+1] == 'C':
                            self.total = self.total + 90
                            i += 2
                            continue
                    self.total = self.total + 10
                elif (s[i] == 'C'):  # D and M
                    if (last == False and s[i+1] != 'C'):
                        if s[i+1] == 'D':  # CD - 400
                            self.total = self.total + 400
                            i += 2
                            continue
                        if s[i+1] == 'M':  # CM - 900
                            self.total = self.total + 900
                            i += 2
                            continue
                    self.total = self.total + 100
                elif (s[i] == 'V'):
                    self.total = self.total + 5
                elif (s[i] == 'L'):
                    self.total = self.total + 50
                elif (s[i] == 'D'):
                    self.total = self.total + 500
                elif (s[i] == 'M'):
                    self.total = self.total + 1000
                i += 1
            return self.total


if __name__ == '__main__':
    c = Solution()
    print(c.romanToInt('IX'))
    print(c.romanToInt('XI'))
    print(c.romanToInt('XII'))
    print(c.romanToInt('LVIII'))
    print(c.romanToInt('MCMXCIV'))
