i = 0
k = 10
z = "0"

l = input()
l = int(l)

j = 10 ** l - 1
l = l - 1

while i <= j:
    if i < k:
        print(z * l + "%d" % (i))
        i += 1
    if i == k:
        l = l - 1
        k = k * 10
    if i > j:
        exit()