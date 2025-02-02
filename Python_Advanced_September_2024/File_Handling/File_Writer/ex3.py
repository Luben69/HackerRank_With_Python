file = open("my_first_file.txt")
content = file.read()
print(content)

# OR:


other_way_file = open("my_first_file.txt", "w")
other_way_file.write("I just created my first file!")
