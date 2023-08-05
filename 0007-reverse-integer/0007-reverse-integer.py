class Solution:
    def reverse(self, x: int) -> int:
        x = (str(x))
        if x[0] == "-":
            y = x[1:]
            y = "-" + y[::-1]
            y = int(y)
        else: y =  int(x[::-1])
        if y < -2**31 or y > 2**31 - 1:
            return 0
        return y
