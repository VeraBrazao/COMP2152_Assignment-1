"""
Author: VERA AFONSO BRAZAO
Assignment: #1
"""

# Step b: Create 4 variables - with data types on comments
gym_member = "Alex Alliton "    # this is string
print(gym_member)
preferred_weight_kg = 20.5      # this is float
print(preferred_weight_kg)
hihest_reps = 25                # this is an integer
print(hihest_reps)
membership_active = True        # this is a boolean
print(membership_active)

# Step c: Create a dictionary named workout_stats - the strings are the friend's names
#  and tuples are the timing of each activity that is represented by integers(numbers)
workout_stats ={
    "Alex": (30, 45, 20),
    "Jamie": (15, 30, 30),
    "Taylor": (20, 60, 25)
}
friends = ["Alex", "Jamie", "Taylor"]
print(workout_stats)

# Step d: Calculate total workout minutes using a loop and add to dictionary
for friend, minutes in list(workout_stats.items()):
    total = sum(minutes)
    workout_stats[friend + "Total"] = total

print(f"{friend} total workout: {total}")

# Step e: Create a 2D nested list called workout_list
# The 2D nested list is a list of a lists, here we can see a list with a name of each friend and the time(minutes) per each activity 
workout_list = []
for friend in workout_stats:
    if "Total" not in friend:
        minutes = workout_stats[friend]
        workout_list.append([friend, list(minutes)])

print(workout_list) 

# Step f: Slice the workout_list
# for all friends the amount of time of yoga and running
for friend in workout_list:
    print(friend[1][:2])

# for the 2 last friend the minutes of weighlifting
for friend in workout_list [-2:]:
    print(friend[1][2])

# Step g: Check if any friend's total >= 120
for friend, minutes in workout_stats.items():
    if isinstance(minutes, tuple):
        total = sum(minutes)
    if total >= 120:
        print(f"Great job staying Active, {friend}!")

# Step h: User input to look up a friend
def get_username():
    username = input("Enter a friend's name: ")
    return username

name = get_username()

if name in workout_stats:
    minutes = workout_stats[name]
    total = sum(minutes)

    print(f"{name}'s workout minutes:")
    print("Yoga:", minutes[0])
    print("Running:", minutes[1])
    print("Weightlifting:", minutes[2])
    print("Total:", total)

else:
    print(f"Friend {name} not found in the records.")

# Step i: Friend with highest and lowest total workout minutes

total = {}

for friend in workout_stats:
    if "Total" not in friend:
        total[friend] = sum(workout_stats[friend])

print(f"Friend with the highest total workout minutes:", max(total, key=total.get))
print(f"Friend with the lowest total workout minutes:", min(total, key=total.get))         
