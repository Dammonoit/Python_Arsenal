#python walrus example
l=[1,2,3,4]
if (n:=len(l))>3:
  print(f"list is too long with length {n}. However, expected length is <=3")