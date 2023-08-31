class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        my_dict ={}
        for i in range(len(heights)):
            my_dict[heights[i]] = names[i]
        my_keys = list(my_dict.keys())
        my_keys.sort()
        sorted_dict = {key:my_dict[key] for key in my_keys}
        my_values = list(sorted_dict.values())
        return my_values[::-1]
        
        