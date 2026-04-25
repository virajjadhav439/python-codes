import os
import uuid

class ParkingSystem:
    def __init__(self):
        self.TOTAL_CAPACITY = 100
        self.used_space = 0
        self.filename = "UniqueID.txt"
        self.parked_vehicles = {}
        
        # Define vehicle properties: (space_consumed, cost_in_rs)
        self.vehicle_types = {
            '1': {'name': 'Car', 'space': 5, 'cost': 100},
            '2': {'name': 'Normal Bike / Scooty', 'space': 1, 'cost': 20},
            '3': {'name': 'High CC Bike (500cc+)', 'space': 2, 'cost': 50}
        }
        
        self.load_records()

    def load_records(self):
        """Loads existing parked vehicles from UniqueID.txt into memory."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    if len(data) == 4:
                        uid, v_name, space, cost = data
                        self.parked_vehicles[uid] = {
                            'name': v_name,
                            'space': int(space),
                            'cost': int(cost)
                        }
                        self.used_space += int(space)

    def save_records(self):
        """Saves current parked vehicles to UniqueID.txt, overwriting old data."""
        with open(self.filename, 'w') as file:
            for uid, info in self.parked_vehicles.items():
                file.write(f"{uid},{info['name']},{info['space']},{info['cost']}\n")

    def park_vehicle(self, choice):
        """Registers a vehicle, deducts space, generates UID, and updates file."""
        if choice not in self.vehicle_types:
            print("\n[Error] Invalid vehicle choice.")
            return

        vehicle = self.vehicle_types[choice]
        
        if self.used_space + vehicle['space'] > self.TOTAL_CAPACITY:
            print(f"\n[Error] Not enough space for a {vehicle['name']}. Available units: {self.TOTAL_CAPACITY - self.used_space}")
            return
        
        # Generate an 8-character Unique ID
        uid = uuid.uuid4().hex[:8].upper()
        
        # Store in memory
        self.parked_vehicles[uid] = {
            'name': vehicle['name'],
            'space': vehicle['space'],
            'cost': vehicle['cost']
        }
        self.used_space += vehicle['space']
        
        # Update the file
        self.save_records()
        
        print(f"\n[Success] {vehicle['name']} parked successfully!")
        print(f"-> Your UID is: {uid}")
        print(f"-> Available Space Remaining: {self.TOTAL_CAPACITY - self.used_space} units")

    def retrieve_vehicle(self, uid):
        """Retrieves a vehicle using its UID, frees up space, calculates cost, and updates file."""
        uid = uid.strip().upper()
        
        if uid in self.parked_vehicles:
            vehicle = self.parked_vehicles.pop(uid)
            self.used_space -= vehicle['space']
            self.save_records()
            
            print(f"\n[Success] Vehicle retrieved successfully!")
            print(f"-> Vehicle Type: {vehicle['name']}")
            print(f"-> Please pay: {vehicle['cost']} Rs")
        else:
            print("\n[Error] UID not found. Please ensure the ID is correct.")

    def view_status(self):
        """Displays current parking capacity and active UIDs."""
        print("\n--- Parking Status ---")
        print(f"Total Capacity : {self.TOTAL_CAPACITY} units")
        print(f"Used Space     : {self.used_space} units")
        print(f"Free Space     : {self.TOTAL_CAPACITY - self.used_space} units")
        
        if self.parked_vehicles:
            print("\nParked Vehicles:")
            for uid, info in self.parked_vehicles.items():
                print(f" - UID: {uid} | Type: {info['name']} | Space: {info['space']}")
        else:
            print("\nNo vehicles currently parked.")

def main():
    system = ParkingSystem()
    
    while True:
        print("\n" + "="*30)
        print("   PARKING MANAGEMENT SYSTEM")
        print("="*30)
        print("1. Park a Car (Takes 5 spaces, 100 Rs)")
        print("2. Park a Normal Bike/Scooty (Takes 1 space, 20 Rs)")
        print("3. Park a High CC Bike (Takes 2 spaces, 50 Rs)")
        print("4. Retrieve a Vehicle")
        print("5. View Parking Status")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice in ['1', '2', '3']:
            system.park_vehicle(choice)
        elif choice == '4':
            uid_input = input("Enter the UID to retrieve your vehicle: ")
            system.retrieve_vehicle(uid_input)
        elif choice == '5':
            system.view_status()
        elif choice == '6':
            print("\nExiting system. Have a great day!")
            break
        else:
            print("\n[Error] Invalid input. Please select a valid option.")

if __name__ == "__main__":
    main()