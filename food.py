restaurants = [
    ("Mango Rice", 4.2, 25),
    ("Pad Thai House", 4.8, 40),
    ("Chicken Rice", 4.6, 15),
    ("Som Tam Corner", 4.6, 25),
    ("Boat Noodles", 4.8, 30),

]

def rat(r):
    return r[1]

def minutes(r):
    return r[2]


choice = input("Sort by (rating/time): ").lower()

if choice == "rating":
    result = sorted(restaurants, key=minutes)
    result = sorted(result, key=rat, reverse=True)

elif choice == "time":
    result = sorted(restaurants, key=rat, reverse=True)
    result = sorted(result, key=minutes)
else:
    print("Unknown option")
    result = []

number = 1

for r in result:
    print(f"{number}. {r[0]}, {r[1]} stars, {r[2]} min")
    number = number + 1