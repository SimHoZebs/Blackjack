num = 1
for i in range(1,20):
    if num <= i:
        num = num*i
    else:
        if num%i == 0:
            num = num
        else:
            if i%(num%i)==0:
                num = num*(i//(num%i))
            else:
                num = num*i
print(num)