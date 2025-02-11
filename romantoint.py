class Solution(object):
    def romanToInt(self, s):
            """
            :type s: str
            :rtype: int
            """
            total = 0
            roman = list(s)

            for roman in s:
                if roman == "I":
                    total += 1
                elif roman == "V":
                    total += 5
                elif roman == "X":
                    total += 10
                elif roman == "L":
                    total += 50
                elif roman == "C":
                    total += 100
                elif roman == "D":
                    total += 500
                elif roman == "M":
                    total += 1000
                else:
                    total += 0

            return total      
        
def main():
    result = Solution()
    print(result.romanToInt("MCMXCIV"))
    

if __name__=="__main__":
    main()