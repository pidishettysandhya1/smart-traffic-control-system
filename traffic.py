import random
import matplotlib.pyplot as plt
roads = ["North", "South", "East", "West"]

# ---- Generate Traffic ----
def get_traffic_density():
    traffic = {}
    for road in roads:
        traffic[road] = random.randint(5, 50)
    return traffic


# ---- Emergency Detection ----
def check_emergency():
    # Randomly choose one road or no emergency
    return random.choice(roads + [None])


# ---- Smart AI Decision (Heuristic) ----
def smart_signal_selection(traffic):
    # Select road with highest vehicles
    return max(traffic, key=traffic.get)


# ---- Static Signal Selection ----
def static_signal_selection(index):
    # Fixed rotation
    return roads[index % len(roads)]
def visualize_traffic(traffic, selected_road):
    values = list(traffic.values())

    plt.figure()
    bars = plt.bar(roads, values, color='skyblue')


    plt.title("Traffic Density per Road")
    plt.xlabel("Roads")
    plt.ylabel("Number of Vehicles")

    for i in range(len(roads)):
        if roads[i] == selected_road:
            bars[i].set_color('red')

    plt.show()


# ---- Traffic Control System ----
def traffic_control(mode="smart"):
    print("\nSmart Traffic Control System Started\n")

    static_index = 0
    cycles = 4   # Number of signal cycles

    for cycle in range(cycles):

        print(f"\nCycle {cycle + 1}")

        traffic = get_traffic_density()

        # Print traffic data
        for road in roads:
            print(f"{road}: {traffic[road]} vehicles")

    # ---- Congestion Level Indicator ----
            if traffic[road] > 35:
                print("   🚦 High Congestion")
            elif traffic[road] >= 20:
                print("   🚦 Medium Congestion")
            else:
                print("   🚦 Low Congestion")

    


        # Check emergency
        emergency_road = check_emergency()

        if emergency_road:
            print(f"\n🚑 Emergency detected on {emergency_road} road!")
            selected = emergency_road

        else:
            if mode == "smart":
                selected = smart_signal_selection(traffic)
            else:
                selected = static_signal_selection(static_index)
                static_index += 1

        green_time = min(traffic[selected] // 2, 20)

        print(f"\n➡ Green Signal: {selected}")
        print(f"⏱ Green Time: {green_time} seconds")
        visualize_traffic(traffic, selected)


    print("\nTraffic Simulation Completed.\n")


# ---- Run Program ----
if __name__ == "__main__":

    print("Choose Mode:")
    print("1 - Smart Mode (AI Based)")
    print("2 - Static Mode (Fixed Rotation)")

    choice = input("Enter choice (1 or 2): ")

    if choice == "1":
        traffic_control(mode="smart")
    else:
        traffic_control(mode="static")

