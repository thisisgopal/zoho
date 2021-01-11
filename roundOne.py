# Round - 1
def fn(n):
    for x in range(n+1):
        for y in range(n):
            if y >= x:
                print("{}".format(n-x), end='')
        print('\n')
    return "\n"


n = int(input("Enter a number\n").strip())
print(fn(n))
