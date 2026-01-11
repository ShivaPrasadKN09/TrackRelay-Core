# TrackRelay: Speed and Pace Calculator
print("--- TrackRelay Performance Tool ---")

name = input("Enter Athlete Name: ")
distance = float(input("Enter distance (meters): "))
time_seconds = float(input("Enter time (seconds): "))

# Calculation: Speed = Distance / Time
speed = distance / time_seconds

print(f"\nResults for {name}:")
print(f"Speed: {speed:.2f} meters per second")

# Logic to check for 'Elite' status (Standard for 400m)
if speed > 8.5:
    print("Status: Elite Performance")
else:
    print("Status: Developing Athlete")
