class Solution:
    def defangIPaddr(self, address: str) -> str:
        new_address = ""
        for i in address:
            if i == '.':
               new_address = address.replace(".","[.]")
        return new_address