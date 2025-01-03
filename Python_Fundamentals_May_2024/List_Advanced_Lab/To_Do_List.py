to_do_list = []

while True:
    command = input()
    if command == "End":
        break

    importance, note = command.split("-", 1)
    importance = int(importance)

    to_do_list.append((importance, note))

to_do_list.sort(key=lambda x: x[0])

sorted_notes = [note for _, note in to_do_list]
print(sorted_notes)
