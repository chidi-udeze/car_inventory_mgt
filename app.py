import json
from pathlib import Path


class Vehicle:
    def __init__(
        self, brand, model, type, gas_tank_size, current_fuel_level
    ):
        # unique id, brand, model, type, gas_tank_size,current_fuel_level
        self.brand = brand
        self.model = model
        self.type = type
        self.gas_tank_size = gas_tank_size
        self.current_fuel_level = current_fuel_level

    def __str__(self) -> str:
        return f"the car brand is {self.brand}, the car model is  {self.model}"

    def write_json(self, filename, data_list=None):
        # save details of car to a json file
        if data_list is None:
            data_list = [
                {
                    "brand": self.brand,
                    "model": self.model,
                    "type": self.type,
                    "gas_tank_size": self.gas_tank_size,
                    "current_fuel_level": self.current_fuel_level,
                }
            ]
        else:
            data_list.append(
                {
                    "brand": self.brand,
                    "model": self.model,
                    "type": self.type,
                    "gas_tank_size": self.gas_tank_size,
                    "current_fuel_level": self.current_fuel_level,
                }
            )
        with open(filename, "w") as f:
            json.dump(data_list, f, indent=4)

    def read_json(self, filename):
        # read from filename
        with open(filename, "r") as f:
            data = json.load(f)
        return data


# 1. Get input from the User
vehicle_brand = input("please enter the brand ")
vehicle_model = input("please enter the model ")
vehicle_type = input("please enter the type ")
vehicle_tank_capacity = input("please enter the tank capacity ")
vehicle_current_fuel_level = input("please enter the current_fuel_level ")

# 2. Create a car object
car = Vehicle(
    vehicle_brand,
    vehicle_model,
    vehicle_type,
    vehicle_tank_capacity,
    vehicle_current_fuel_level,
)

# 3. Append the json file with new data
filename = "database.json"

# Step 3.1: read json file
data = None
if Path(filename).exists():
    data = car.read_json(filename)

# 3.2: pass it to the write function
car.write_json(filename, data)
