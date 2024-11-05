nums = [1, 2, 3, 4, 5]


#section 1

for num in nums:
    if num == 3:
        print("found")
        break  #or you can put continue for this line
    print(num)

#section 2

for num in nums:
    for letter in 'abc':
        print(num , letter)

#section 3

x = 0

while  x < 10 :     # Y ou can use "True" instead of "x < 10"
    if x ==5:
        break
    print(x)
    x+=1
