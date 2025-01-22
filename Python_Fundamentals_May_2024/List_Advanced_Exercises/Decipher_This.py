our_words = input().split()
end_of_task = []

for el in range(len(our_words)):
    whole_string_of_word = ""
    result = ""
    i = 0
    while our_words[el][i].isdigit():
        whole_string_of_word += our_words[el][i]
        i += 1

    length_of_nums = len(whole_string_of_word)
    result += chr(int(whole_string_of_word)) + our_words[el][length_of_nums::]
    second_letter = result[1]
    last_letter = result[-1]

    if len(result) > 2:
        final_result = result[0] + last_letter + result[2:-1] + second_letter
        end_of_task.append(final_result)
    else:
        end_of_task.append(result)

print(*end_of_task)

