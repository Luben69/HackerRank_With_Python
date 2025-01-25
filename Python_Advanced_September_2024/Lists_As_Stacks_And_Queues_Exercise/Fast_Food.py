from collections import deque

quantity = int(input())
sequence_of_integers = deque(int(x) for x in input().split())

print(max(sequence_of_integers))

while sequence_of_integers and sequence_of_integers[0] <= quantity:
    quantity -= sequence_of_integers.popleft()

if not sequence_of_integers:
    print('Orders complete')
else:
    print('Orders left:', *sequence_of_integers)
