num = input("put number")
num = int(num)


if num%2 == 0:
    print("number is even")
else:
    print("number is odd")



if 3>2 and 4>1 :
    print("true")
if 3>2 and 4>5 :
    print("true")
else:
    print("false")
if 3>2 or 4>1 :
    print("true")   


    indian = ["samosa", "daal", "naan"]
    chinese = ["egg roll" , "potstickers" , "fried rice"]
    italian =  ["pasta" , "risoto", "pizza"]

    dish=input("what food item would you like ")


if dish in indian:
    print("indian")
elif dish in chinese:
    print("chinese") 
elif dish in italian :
    print("italian")
else :
    print("we dont have ithat item on our menue at this moment")