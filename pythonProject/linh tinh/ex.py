def x(num):
    if num==1:
        return num
    else:
        return num*x(num-1)
print(x(5))