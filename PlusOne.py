class Solution(object):
    def plusOne(self, digits):
        nine_found = False
        multi_nine = False
        k = 0
        for i in range(len(digits) - 1, -1, -1):
            print
            digits[i]
            if digits[i] != 9 and nine_found == False:
                digits[i] += 1
                return digits
            elif digits[i] != 9 and nine_found == True:
                digits[i] += 1
                digits[i + 1] = 0
                return digits
            else:
                if nine_found == True and digits[i] == 9:
                    digits[i + 1] = 0
                    digits[i] = 1
                    multi_nine = True
                    k += 1
                elif nine_found == False and digits[i] == 9:
                    digits[i] = 1
                    nine_found = True
                    k += 1
        if multi_nine != True or k == len(digits):
            digits.append(0)
            return digits
        return digits
        """
        :type digits: List[int]
        :rtype: List[int]
        """
