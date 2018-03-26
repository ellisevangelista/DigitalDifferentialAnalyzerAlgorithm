print("Point A:")
print("Enter x1: ")
x1 = input()
x1 = int(x1)
print("Enter y1: ")
y1 = input()
y1 = int(y1)

print("Point B:")
print("Enter x2: ")
x2 = input()
x2 = int(x2)
print("Enter y2: ")
y2 = input()
y2 = int(y2)


num = y2-y1
denom = x2-x1

num = abs(num)
denom = abs(denom)

slope = float(num/denom)
print("\nSlope of the line:")
print(slope)

if num > denom:
    y = []
    if y1 < y2:
        for j in range(y1, y2+1):
            y.append(j)
        print("\ny-coordinates:")
        print(y)
    else:
        for j in range(y1, y2-1, -1):
            y.append(j)
        print("\ny-coordinates:")
        print(y)
    x = []
    z = []
    x.append(x1)
    z.append(x1)
    xB = 0
    for j in range(0, len(y)-2):
        if slope < 1:
            xB = z[j] + slope
        else:
            xB = z[j] + 1/slope
        z.append(xB)
        x.append(round(xB,))
    x.insert(len(x), x2)
    print("\nx-coordinates:")
    print(x)
else:
    x = []
    if x1 < x2:
        for i in range(x1, x2 + 1):
            x.append(i)
        print("\nx-coordinates:")
        print(x)
    else:
        for i in range(y1, y2 - 1, -1):
            x.append(i)
        print("\nx-coordinates:")
        print(x)
    y = []
    z = []
    y.append(y1)
    z.append(y1)
    yB = 0
    for i in range(0, len(x) - 2):
        if slope < 1:
            yB = z[i] + slope
        else:
            yB = z[i] + 1 / slope
        z.append(yB)
        y.append(round(yB, ))
    y.insert(len(y), y2)
    print("\ny-coordinates:")
    print(y)
