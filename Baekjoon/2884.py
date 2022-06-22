H, M = map(int,input().split()) #map --> int,  split

#시 / 분

if M>44:#45분이상
    print(H,M-45)
    #Print 방식에 따른 차이
elif H>0 and M<45:
    print(H-1,M+15) #60-45
elif H==0:
    print(23,M+15)
    