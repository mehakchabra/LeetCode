class Solution:
    def dayOfYear(self, date: str) -> int:
        cal = {
            1 : 31,
            2 : 28,
            3 : 31,
            4 : 30,
            5 : 31, 
            6 : 30, 
            7 : 31,
            8 : 31, 
            9 : 30,
            10 : 31,
            11 : 30,
            12 : 31
        }

        def isLeap(year):
            leap = False
            if (year % 400 == 0) and (year % 100 == 0):
                    leap = True 

            if (year % 4 == 0) and (year % 100 != 0):
                    leap = True
            return leap

        year = int(date[:4])
        month = int(date[5:7])
        day = int(date[8:])
        leap = 0

        ans = 0
        if month > 2 and isLeap(year):
            leap = 1

        for i in range(1, month):
            ans += cal[i]
        return ans+leap+day