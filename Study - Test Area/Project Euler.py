maxnum = 20
numlist = []
rem = []
fac = []

divider = 2
wasdivided = None
answer = 1

def make_list():
    for num in range(maxnum//2, maxnum +1):
        numlist.append(num)

make_list()

while divider != maxnum//2:
    for num in numlist:
        print(f"dividing {num} with {divider}")
        
        if num//2 < divider and num != divider:
            print(f"{num} isn't worth trying to divide by {divider}.")
            rem.append(num)
               
        elif num % divider == 0:
            print(f"{num} can be divided by {divider}!"
                   f"\nDividing then putting {num//2} in rem")
            rem.append(num//divider)
            wasdivided = True
                
        elif num % divider != 0:
            print(f"{num} can't be divided by {divider}."
                   f"Putting {num} in rem.")
            rem.append(num)
    
    print(f"rem: {rem}")
    if wasdivided:
        fac.append(divider)
        wasdivided = 0
    elif not wasdivided:
        divider += 1
        
    numlist = rem.copy()
    print(f"numlist: {numlist}")
    rem = []

for _ in fac:
    answer *= _
    
for _ in numlist:
    answer *= _


print(answer)