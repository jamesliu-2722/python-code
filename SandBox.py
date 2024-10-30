



events = [
    {"name": "Concert A", "type": "music", "location": "New York"},
    {"name": "Concert B", "type": "music", "location": "Los Angeles"},
    {"name": "Football Game", "type": "sports", "location": "Chicago"},
    {"name": "Art Exhibition", "type": "art", "location": "San Francisco"}
]

print(type(events))
for event in events:
    print(type(event))
    print(event["name"])
    print(event["type"])
    print(event["location"])

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# a = [1, 1, 2, 3, 5]
# b = [1, 2, 3]

def fib(x):
    list = [1,1]
    if x == 2:
        return list
    for i in range(x-2):
        list.append(list[-1] + list[-2])
    return list

print(fib(4))


