# Initializing the target timestamp and list of available bus IDs
target_ts, available_buses = 0, []

# Reading from input file
with open('input.txt', 'r') as f:

    # Reading all the lines
    lines = f.readlines()

    # Obtaining the target timestamp
    target_ts = int(lines[0].strip())

    # Obtaining the bus IDs
    available_buses = list(map(int, [bus_id for bus_id in lines[1].strip().split(',') if bus_id != 'x']))

# Initializing the list of departure timestamps
departure_ts = []

# For each available bus ID
for bus_id in available_buses:

    # Checking if the bus departs at the target timestamp
    if (target_ts % bus_id == 0) and (bus_id != 0):
        departure_ts.append(target_ts)
        continue

    # Checking if the bus does not depart at the target timestamp
    if (target_ts % bus_id != 0) and (bus_id != 0):
        departure_ts.append(bus_id * ((target_ts // bus_id) + 1))

# Determining the earliest departing bus
earliest_dep_ts_idx = departure_ts.index(min(departure_ts))
earliest_bus_id = available_buses[earliest_dep_ts_idx]

# Printing the required product
print(f"Required Product: {earliest_bus_id * (departure_ts[earliest_dep_ts_idx] - target_ts)}")