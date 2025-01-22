words = input().split()
our_dict = {}

for word in words:
    world_lower = word.lower()
    if world_lower not in our_dict:
        our_dict[world_lower] = 0
    our_dict[world_lower] += 1

for k, v in our_dict.items():
    if v % 2 != 0:
        print(k, end=" ")
