def not_even_num_gen(n):
    for i in range(1, n + 1, 2):
        yield i

not_even_num = not_even_num_gen(11)
print(type(not_even_num))
print(not_even_num.__next__())
print(not_even_num.__next__())
print(*not_even_num)
print(not_even_num.__next__())




