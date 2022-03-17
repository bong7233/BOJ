H,M = map(int,input().split( ))

if M >= 45:
    al_M = M - 45
    al_H = H
elif M < 45 and H > 0:
    al_M = M + 15
    al_H = H - 1
elif M < 45 and H == 0:
    al_M = M + 15
    al_H = 23

print(al_H, al_M)
