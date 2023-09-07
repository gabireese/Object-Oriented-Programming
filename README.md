# Object-Oriented-Programming

The purpose of this program was to practice object programming based on a real world setting. 

For the car class, the atrributes were:

manufacturer - stores the car's manufacturer name

model- stores the car's model

year- stores the year of the car as an integer

mileage- stores the car's mileage as a float or integer

engine- stores the car's engine information

transmission- stores information about the type of transmission the car drives with (automatic, manual, etc.)

drivetrain- stores the car's drivetrain information (whether it's front-wheel drive, all-wheel drive, etc.)

mpg- displays the miles per gallon of the car as an int or string 

exterior_color- stores the exterior color of the car

interior_color- stores the interior color of the car

accident_status- Displays the car's accident history. Used bool to indicate if the car has been in an accident (True) or not (False)

car_price- Stores the car's price. Used float due to the monetary value of the cars

Methods for car class:
Used the constructor method (initializers) to initialize the object's attributes

For seller class, the attributes were:

name- Stores the seller's name (e.g. Kars Today, etc.)

rating- displays the rating of the sellers using float

inventory- lists that displays the available cars

Methods in seller class:

def Buy(self, car) is used to take car that's not in the inventory as the input and adds to the sellers inventory
def Sell(self, car) used to take the car that's in the sellers inventory as an input and removes it from the inventory

Limitations in both classes-

Car class: Modify_Price- when the new price is less than 1 the car is discounted and ask user to confirm if the discounted price is the desired amount

Seller class: if car is not in the inventory, car is added to the inventory
