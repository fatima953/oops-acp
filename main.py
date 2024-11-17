class dog:
    def __init__(self, max_speed, mileage):
        self.mileage = mileage
        self.max_speed = max_speed
    def car(self, brand):#<- everythind that is inside the braket is an argument.
        print("I have a", brand,"car")
modleX = dog(240, 18)
print("Model Max Speed:",modleX.max_speed)
print("Model Mileage:", modleX.mileage)
modleX.dog("white dog")
modleX.dog("brown dog")