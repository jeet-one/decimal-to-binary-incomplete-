#n = input('Enter the number: ')
#n = int(n)
def binary(n):
  
  if n == 0:
    return 1
  else:
    return n % 2 + binary(n //2)   



print(binary(10))e)