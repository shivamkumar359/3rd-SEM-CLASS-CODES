# Python projgramm to count even and odd in list 

#list of numbers 
list = [1,4,5,2,45,65,78,14,21,35,99,77,28,68]
even_count, odd_count = 0,0

# Iterating each number in list 
for num in list :

  #checking condition 
  if num % 2 == 0:
    even_count += 1

  else :
    odd_count += 1

print("Even number in list of numbers are :" , even_count)
print("Odd number in list of numbrs are : " , odd_count)
