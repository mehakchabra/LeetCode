class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        result = []
        Kelvin = celsius + 273.15
        result.append(Kelvin)
        Fahrenheit = celsius * 1.80 + 32.00
        result.append(Fahrenheit)
        return result
        