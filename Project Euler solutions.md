##### Problem 1
```python
sum_num = 0

for num in range(0,1000):
    if num % 3 == 0 or num % 5 == 0:
        sum_num += num

print(sum_num)

#5 lines
```

#####Problem 2
```python
value1 = 1
value2 = 1
alist = []
result = 0

while value1 < 4000000 or value2 < 4000000:
    value1 += value2
    alist.append(value1)
    value2 += value1
    alist.append(value2)
    
for num in alist:
    if num % 2 == 0 and num < 4000000:
        result += num

print(result)

#13 lines
```

#####Problem 3
```python
prime_list = set()
value = 600851475143

for num in range(2, (value//2) + 1):
    if value % num == 0:
        #print(f"{num} is a factor of {value}." )
        value = (value / num)
        #print(f"value changing to {value} because num after it aren't factors.")
        #print(f"Check prime in range {(num//2) + 2}")
        if value == 1:
            #print(f"Adding {num} to prime_list")
            prime_list.add(num)
            break
        for num2 in range(2, (num//2) + 2):
            #print(f"Checking if {num} can be divided by {num2}")
            if num%num2 == 0 and num2 != num:
                #print(f"It can be divided and it's not {num}, so it's not a prime.")
                break
            else:
                #print(f"Adding {num} to prime_list")
                prime_list.add(num)
    else:
        #print(f"{num} is not a factor of {value}.")

prime_list = list(prime_list)
prime_list.sort()            
print(prime_list[-1])

#15 lines

#Below is an alternate answer. Only true because of the question's specific value.

prime_list = []
value = 600851475143

for num in range(2, (value + 1) // 2):
    if value == 1:
        break
    if value % num == 0:
        value = (value / num)
        prime_list.append(num)

print(prime_list[-1])

#9 lines
```

#####Problem 4
```python
list_pali = []
pali_num = 1

for num1 in range(100, 1000):
    for num2 in range(100, 1000):
        #print(f"Multiplying {num1} with {num2}")
        result = num1 * num2
        #print(f"Got {result}. Checking for palidrome")
        pali_check = list(str(result))
        #print(f"pali_check list is: {pali_check}")
        #print(f"Checking from 0 to {len(pali_check)}")
        for place in range (0, len(pali_check)):
            #print(f"comparing placement {place} and {-(place +1)}")
            if pali_check[place] != pali_check[-(place + 1)]:
                #print("They are not the same!")
                break
            if place == len(pali_check) - 1:
                #print(f"{result} is the largest palidrome for {num1}!")
                list_pali.append(result)
                break
        if len(list_pali) == pali_num:
            pali_num += 1
            break

list_pali.sort()
print(list_pali[-1])

#17 lines
```

#####Problem 5
```python

```