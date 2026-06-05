numbers = ['11' , '5', '8', '32', '15', '3', '20', '132', '21', '4', '555', '9', '20']

for num_str in numbers:
    num = int(num_str)  
    if num % 3 == 0 and num < 30:
     print(num)
     