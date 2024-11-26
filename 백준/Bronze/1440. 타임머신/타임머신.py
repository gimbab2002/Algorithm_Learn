a, b, c = map(int, input().split(":"))

if(a > 59 or b>59 or c>59 or a<0 or b<0 or c < 0): print('0')
elif((a >= 1 and a <= 12) and (b >= 1 and b <= 12) and (c >= 1 and c <= 12)):
    print('6')
elif((a >= 1 and a <= 12 and b >= 1 and b <= 12) 
    or (b >= 1 and b <= 12 and c >= 1 and c <= 12) 
    or (a >= 1 and a <= 12 and c >= 1 and c <= 12)):
    print('4')
elif((a >= 1 and a <= 12) 
    or (b >= 1 and b <= 12)
    or (c >= 1 and c <= 12)):
    print('2')
else: print('0')    
        