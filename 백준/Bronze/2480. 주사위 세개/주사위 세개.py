a,b,c = map(int,input().split())

dice_list = [a,b,c]
dice_set = set(dice_list)

if len(dice_set) == 1:
    print(dice_list[0]*1000 + 10000)
    
elif len(dice_set) == 3:
    print(max(dice_list)*100)
    
else:
    print(max(dice_list, key=dice_list.count)*100 + 1000)