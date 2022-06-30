def add(x,y,*args):
  sum=x+y
  for i in args:
    sum+=i
  
  return sum

(print(add(10,12,13,14,14,16)))
