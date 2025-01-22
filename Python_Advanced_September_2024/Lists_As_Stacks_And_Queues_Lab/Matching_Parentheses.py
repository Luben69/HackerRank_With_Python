string = input()

stack = []

for index in range(len(string)):
    if string[index] == '(':
        stack.append(index)
    elif string[index] == ')':
        recent_found = stack.pop()
        print(string[recent_found:index+1])
