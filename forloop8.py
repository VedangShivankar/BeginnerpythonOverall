#section 1
exp = [2340, 2500, 2100, 3100, 2980]
total = 0
for i in range(len(exp)):
    print('Month:', (i+1), 'Expense', exp[i])
    total = total + exp[i]

print('total expense', total)

#section 2

key_location = "chair"
locations = ["garage", "living room", "chair" , "closet"]
for f in locations:
    if f == key_location:
        print("key is found in", f)
        break
    else:
        print("key is not found in" ,f)

#section 3
v = 1
while v<5:
    print(v)
v = v+1