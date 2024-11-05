tom_exp_list = [2100,3400, 3500]
joe_exp_list = [200, 500, 700]

total = 0

for item in tom_exp_list:
    total=total+item
print("tom total expenses" , total)


total = 0 
for item in joe_exp_list:
    total = total+item
print("joes total expense", total)


#section 2

def calculate_total(exp):  
    total = 0
    for item in exp:
        total=total+item
    return total 

tom_exp_list = [2100,3400, 3500]
joe_exp_list = [200, 500, 700]

toms_total = calculate_total(tom_exp_list)
joes_total = calculate_total(joe_exp_list)

print("toms ", toms_total)
print("joes " ,joes_total)


#section 3
all = 0

def sum(a,b=0):
    print("A:",a)
    print("B:",b)
    all = a+b
    print("inside",all)
    return all

z = sum(5)
print(z)