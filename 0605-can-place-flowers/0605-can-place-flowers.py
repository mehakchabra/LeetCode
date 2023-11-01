class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # Number of valid positions in the list
        count = 0

        # Copy of given list to edit
        fb = flowerbed

        # Length of the given list
        length = len(fb)

        # If only 1 position
        if length == 1 and fb[0] == 0:
            return True

        # Check the beginning
        if fb[0] == 0 and fb[1] == 0:
            fb[0] = 1
            count += 1

        # Check the end
        if fb[length - 1] == 0 and fb[length - 2] == 0:
            fb[length - 1] = 1
            count += 1

        # Current index in the list
        index = 1

        # Check the middle
        while index < length - 1:

            if fb[index - 1] == 0 and fb[index + 1] == 0 and fb[index] != 1:
                fb[index] = 1
                count += 1
                
            index += 1

        # If there is a valid number of open positions in the list
        if count >= n:
            return True
        else:
            return False