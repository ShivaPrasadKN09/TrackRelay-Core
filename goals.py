# TrackRelay: Target Time Finder
current_time = float(input("Enter your current 400m time: "))
target_improvement = 0.05 # Aiming for 5% faster

target_time = current_time * (1 - target_improvement)

print(f"To improve by 5%, your target time is: {target_time:.2f} seconds")
