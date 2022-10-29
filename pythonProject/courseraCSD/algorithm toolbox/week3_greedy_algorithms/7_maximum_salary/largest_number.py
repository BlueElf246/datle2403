#Uses python3

import sys

def largest_number(a):
    one_digit=[]
    two_digit=[]
    for x in a:
        if x<10:
            one_digit.append(x)
        elif x>=10 and x<100:
            two_digit.append(x)
    result=''
    two_digit.sort(reverse=True)
    one_digit.sort(reverse=True)
    if len(two_digit)==0:
        result=str(one_digit)
    elif len(one_digit)==0:
        result=str(two_digit)
    else:
        for x in one_digit:
            appear=0
            for y in two_digit:
                if appear>0:
                    continue
                if x > int(str(y)[0]):
                    result+=str(x)
                    appear+=1
                elif x == int(str(y)[0]):
                    if int(str(y)[1]) >=x:
                        result+=str(y)
                    else:
                        result+=str(x)
                else:
                    result+=str(y)

    print(result)
largest_number([21,2])
# if __name__ == '__main__':
#     input = sys.stdin.read()
#     data = input.split()
#     a = data[1:]
#     print(largest_number(a))
    
