# TrackRelay: Team Data Entry System
team_times = []

print("Enter times for 4 relay runners (in seconds):")

for i in range(1, 5):
    time = float(input(f"Runner {i} time: "))
    team_times.append(time)

total_time = sum(team_times)
average_time = total_time / 4

print("\n--- Relay Team Report ---")
print(f"Total Team Time: {total_time:.2f}s")
print(f"Average Split: {average_time:.2f}s")
