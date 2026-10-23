#This program is to simulate the occupancy of a bus over a period of time. It will track the number of passengers boarding and alighting at each stop, and calculate the total occupancy at any given time. The program will also provide insights into peak hours and average occupancy rates. 
capacity = 40
passengers = 0

for stop in range(1, 5):
    off = int(input("Passengers getting off at stop " + str(stop) + ": "))
    on = int(input("Passengers boarding at stop " + str(stop) + ": "))

    if off > passengers:
        print("Stop", stop, ": invalid, more passengers getting off than are on the bus")
    else:
        passengers = passengers - off + on
        print("Stop", stop, ": off", off, ", on", on, "->", passengers, "passengers")
        if passengers > capacity:
            print("Capacity exceeded by", passengers - capacity)

print("Final passengers on the bus:", passengers)