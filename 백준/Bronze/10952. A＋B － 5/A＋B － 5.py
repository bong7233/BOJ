total = 1

while total !=0:
    a,b = map(int, input().split())
    total = a+b
    if total == 0:
      break
    else:
      print(total)
