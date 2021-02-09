elements = input().split()
length = len(elements)
elements_was_used = list()


def choice(number):
    if number in elements_was_used:
        choice(number - 1)
        choice(number + 1)
    else:
        elements_was_used.append(number)
        if len(elements_was_used) < length:
            choice(number - 1)
            choice(number + 1)
        else:
            for j in elements_was_used:
                print(elements[j], end=' ')
            print()


    elements_was_used = elements_was_used[0 : len(elements_was_used) - 1]


for i in range(length):
    elements_was_used = [i]
    choice(i)