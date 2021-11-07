num_a = int(input())
second_a = set(map(int, input().split()))

input_num = int(input())

for i in range(input_num):

    comm, ne = input().split()
    B = set(map(int, input().split()))

    if comm == 'intersection_update':
        second_a.intersection_update(B)

    elif comm == 'update':
        second_a.update(B)

    elif comm == 'difference_update':
        second_a.difference_update(B)

    elif comm == 'symmetric_difference_update':
        second_a.symmetric_difference_update(B)

print(sum(second_a))
