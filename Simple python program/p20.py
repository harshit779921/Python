#waf to print a number to odd or even in strings

def number_chk(a):
  calc = a % 2
  if(calc == 0):
    print("Even")
  else:
    print("Odd")

number_chk(int(input()))