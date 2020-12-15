import sys
from threading import Thread, Lock

result = {}
lock = Lock()



def add_factor(number, factor):
    lock.acquire()

    if number not in result:
        result[number] = [factor]
    else:
        result[number].append(factor)

    lock.release()



def calculate_factors(number):
    n = number
    d = 2
    while d * d <= n:
        if n % d == 0:
            add_factor(number, factor=d)
            n //= d
        else:
            d += 1

    if not n == 1:
        add_factor(number, factor=n)


if len(sys.argv) > 1:
    threads = []

    for number in sys.argv[1:]:
        new_thread = Thread(target=calculate_factors, args=(int(number),))
        new_thread.start()
        threads.append(new_thread)


    for thread in threads:
        if thread.is_alive():
            thread.join()


    for number in sys.argv[1:]:
        print(int(number), ': ', end='')
        for factor in result[int(number)]:
            print(factor, end=' ')
        print()  
