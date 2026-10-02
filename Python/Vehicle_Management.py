list_vehicle=[]
def entry (vehicle_number:int, duration_parking:float, entry_time: float):
    info=(vehicle_number, duration_parking, entry_time)
    global list_vehicle
    fee= duration_parking * 10
    list_vehicle.append(info)
    print("Vehicle entry recorded successfully.")
    print("Vehicle Number:", vehicle_number)
    print("Duration of Parking:", duration_parking)
    print("Entry Time:", entry_time)
    print("Parking Fee: Rupees-", fee)

def exit(vehicle_number:int, exit_time: float):
    global list_vehicle
    for vehicle in list_vehicle:
        if vehicle[0] == vehicle_number:
            actual_parking_duration = exit_time - vehicle[2]
            if(actual_parking_duration > vehicle[1]):
                extra_duration = actual_parking_duration - vehicle[1]
                extra_fee = extra_duration * 10
                total_fee = (vehicle[1] * 10) + extra_fee
                print("Vehicle exit recorded successfully.")
                print("Vehicle Number:", vehicle_number)
                print("Actual Parking Duration:", actual_parking_duration)
                print("Extra Duration:", extra_duration)
                print("Extra Fee: Rupees-", extra_fee)
                print("Total Parking Fee: Rupees-", total_fee)
            else:
                total_fee = actual_parking_duration * 10
                print("Vehicle exit recorded successfully.")
                print("Vehicle Number:", vehicle_number)
                print("Actual Parking Duration:", actual_parking_duration)
                print("Total Parking Fee: Rupees-", total_fee)
        else:
            print("Vehicle not found in the parking lot.")
print("Vehicle Management System")
while True:
    print("---------Menu---------")
    print("1. Enter Vehicle")
    print("2. Exit Vehicle")
    print("3. Display Vehicle Information")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        vehicle_number = int(input("Enter Vehicle Number: "))
        duration_parking = float(input("Enter Duration of Parking (in hours): "))
        entry_time = float(input("Enter Entry Time (in hours): "))
        entry(vehicle_number, duration_parking, entry_time)
    elif choice == 2:
        vehicle_number = int(input("Enter Vehicle Number: "))
        exit_time = float(input("Enter Exit Time (in hours): "))
        exit(vehicle_number, exit_time)
    elif choice == 3:
        print("---------------------------")
        print("Vehicle Information:")
        for vehicle in list_vehicle:
            print("Vehicle Number:", vehicle[0])
            print("Duration of Parking:", vehicle[1])
            print("Entry Time:", vehicle[2])
            print("------------------------")
            print()
    elif choice == 4:
        print("Exiting the Vehicle Management System.")
        break
    else:
        print("Invalid choice. Please try again.")


