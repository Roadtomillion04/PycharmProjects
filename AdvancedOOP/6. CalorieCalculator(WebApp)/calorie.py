from temperature import Temperature

class Calorie:
    """
    Represent the amount of calories needed by
    The Mifflin - St Jeor BMR equation(metric formula)
    """
    def __init__(self, weight:float, height:float, age:int, temperature:float):
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature # this is not user declaring

    def calculate(self):
        bmr = (10 * self.weight) + (6.25 * self.height) \
              - (5 * self.age) - (5 * self.temperature)
        return bmr

if __name__ == "__main__": # meaning if the script is executed directly otherwise don't
    temperature = Temperature(city= 'karur', country= 'India').get_temperature()
    calorie = Calorie(weight= 60, height= 176, age= 17, temperature= temperature)
    print(calorie.calculate())
