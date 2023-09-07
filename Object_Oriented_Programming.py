#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Car:
    ##Listing the attributes below##
    manufacturer: str
    model: int or str
    year: int
    mileage: int or float 
    engine: int or str
    transmission: str
    drivetrain: int or str
    mpg: int or str 
    exterior_color: str
    interior_color: str
    accident: bool 
    car_price: float
    ##Creating method for car class##    
    def __init__(self,manufacturer, model, year, mileage, engine, transmission, drivetrain, mpg, exterior_color, interior_color, accident, 
    car_price):
      self.manufacturer = manufacturer
      self.model = model
      self.year = year
      self.mileage = mileage
      self.engine = engine
      self.transmission = transmission
      self.drivetrain = drivetrain
      self.mpg = mpg
      self.exterior_color = exterior_color
      self.interior_color = interior_color
      self.accident = accident
      self.car_price = car_price
       
    def Paint(self, new_color):
        self.exterior_color = new_color
        print(f"The car's exterior color has been changed to {new_color}.")

    def Repair(self, part_to_replace, new_part):
        if part_to_replace == "engine":
            self.engine = new_part
        elif part_to_replace == "transmission":
            self.transmission = new_part
        elif part_to_replace == "drivetrain":
            self.drivetrain = new_part
        else:
            print("Invalid part name. Please choose from 'engine', 'transmission', or 'drivetrain'.")

    def Reupholster(self, new_color):
        self.interior_color = new_color
        print(f"The car's interior color has been changed to {new_color}.")

    def Drive(self, miles_driven):
        self.mileage += miles_driven
        print(f"The car has been driven {miles_driven} miles. New mileage: {self.mileage} miles.")

    def Modify_Price(self, new_price):
        if new_price < 1:
            discount_amount = abs(new_price)
            self.car_price -= discount_amount
            print(f"The car price has been discounted by ${discount_amount}.")
            confirmation = input("Is this the desired price? (yes/no): ").strip().lower()
            if confirmation == 'no':
                print(f"The car price has been reset to ${self.car_price}.")
            else:
                print(f"The new price is ${self.car_price}.")
        else:
            self.car_price = new_price
            print(f"The car price has been updated to ${new_price}.")

#Example Input##
car1 = Car("Acura", "ILX Hybrid 1.5L", 2013, 92945, "1.5L I-4 i-VTEC variable valve control, engine with 90HP", "Automatic", "Front-wheel drive", 39-38, "Black", "Parchment", False, 13988)
car1.Paint("Pink")
car1.Repair("engine", "V6")
car1.Reupholster("White")
car1.Drive(100)
car1.Modify_Price(18000)


# In[2]:


class Seller:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating
        self.inventory = []

    def Buy(self, car):
        if car not in self.inventory:
            self.inventory.append(car)
            print(f"{self.name} has bought a {car.year} {car.manufacturer} {car.model} and added it to their inventory.")
        else:
            print(f"{self.name} already has this car in their inventory.")

    def Sell(self, car):
        if car in self.inventory:
            self.inventory.remove(car)
            print(f"{self.name} has sold a {car.year} {car.manufacturer} {car.model} from their inventory.")
        else:
            print(f"{self.name} does not have this car in their inventory.")

# Example Input##
car1 = Car("Hyundai", "Venue", 2023, 2000, "121-hp 1.6L DPI 4-cylinder engine", "Automatic", "Front-wheel drive", "29-33", "Scarlet Red Pearl", "Black", False, 2000)

seller1 = Seller("John's Auto", 4.7)
seller1.Buy(car1)
seller1.Sell(car1)


# In[3]:


import csv

class Car:
    def __init__(self, manufacturer, model, year, mileage, engine, transmission, drivetrain, mpg, exterior_color, interior_color, accident_status, car_price):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.mileage = mileage
        self.engine = engine
        self.transmission = transmission
        self.drivetrain = drivetrain
        self.mpg = mpg
        self.exterior_color = exterior_color
        self.interior_color = interior_color
        self.accident = accident
        self.car_price = car_price

class Seller:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating
        self.inventory = []

    def Buy(self, car):
        if car not in self.inventory:
            self.inventory.append(car)

# Read the CSV file and create Seller and Car objects
sellers = {}
cars = []

with open("/Users/gabi_reese/Downloads/cars.csv", mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Extract data from the CSV row
        manufacturer = row['manufacturer']
        model = row['model']
        year = int(row['year'])
        
        ##Kept getting value error because mileage is a float so used try-except to round the float##
        try:
            mileage = round(float(row['mileage']))
        except ValueError:
            mileage = 0
        engine = row['engine']
        transmission = row['transmission']
        drivetrain = row['drivetrain']
        mpg = str(row['mileage'])
        exterior_color = row['exterior_color']
        interior_color = row['interior_color']
        accident = row['accidents_or_damage'].lower() == 'new'
        car_price = float(row['price'])

        # Create a Car object
        car = Car(manufacturer, model, year, mileage, engine, transmission, drivetrain, mpg, exterior_color, interior_color, accident, car_price)
        cars.append(car)

        # Create or update the Seller object
        seller_name = row['seller_name']
        ## Kept kept getting value error due to empty cells so used try-except to convert empty cells to 0 ##
        try:
            seller_rating = float(row['seller_rating'])
        except ValueError:
            seller_rating = 0.0
        
        if seller_name not in sellers:
            seller = Seller(seller_name, seller_rating)
            sellers[seller_name] = seller
        else:
            seller = sellers[seller_name]

        # Add the car to the seller's inventory
        seller.Buy(car)

# Example usage:
# Access seller and car data from the created objects
for seller_name, seller in sellers.items():
    print(f"Seller: {seller_name}, Rating: {seller.rating}")
    print("\nInventory:")
    for car in seller.inventory:
        print(f"\n  {car.year} {car.manufacturer} {car.model}" +"\n")

