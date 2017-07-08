def first_n_primes(qty):
    i = 2
    while i < qty:
        flag = True
        for item in range(2, int(i**0.5)+1):
            if i % item == 0 and i != item:
                flag = False
                break
        if flag:
            yield i
        i += 1

if __name__ == '__main__':
    qty = int(input('Please enter upper bound: '))
    numbers = first_n_primes(qty)
    for item in numbers:
        print(item)
