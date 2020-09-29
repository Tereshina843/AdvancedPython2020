Numbers = list(map(float, input().split()))
Numbers = [i**2 for i in Numbers]
Numbers.sort()
Numbers_new= []
for i in Numbers:
    if i not in Numbers_new:
        Numbers_new.append(i)
for num in Numbers_new:
    if float.is_integer(num):
        print(int(num), end=' ')
    else:
        print(num, end=' ')
