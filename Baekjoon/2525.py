H, M = map(int,input().split()) #map --> int,  split
TIME = int(input())

H += TIME//60
M += TIME%60

if M>=60:
    H+=1
    M-=60

if H>=24:
    H-=24

print(H,M)