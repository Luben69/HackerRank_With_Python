rows, columns = [int(x) for x in input().split(", ")]

matrix = []

for _ in range(rows):
    row_data = [int(x) for x in input().split(", ")]
    matrix.append(row_data)

max_sum = float("-inf")
sub_matrix = []

for row_index in range(rows-1):
    for col_index in range(columns-1):
        element = matrix[row_index][col_index]
        next_element = matrix[row_index][col_index+1]
        below_element = matrix[row_index+1][col_index]
        diagonal_element = matrix[row_index+1][col_index+1]

        sum_elements = element + next_element + below_element + diagonal_element
        if sum_elements > max_sum:
            max_sum = sum_elements
            sub_matrix = [[element, next_element], [below_element, diagonal_element]]

print(*sub_matrix[0])
print(*sub_matrix[1])

print(max_sum)
