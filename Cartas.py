c1, c2, c3, c4, c5= input().split()
if int(c1) < int(c2) and int(c2) < int(c3) and int(c3) < int(c4) and int(c4) < int(c5):
    print('C')
elif int(c1) > int(c2) and int(c2) > int(c3) and int(c3) > int(c4) and int(c4) > int(c5):
    print('D')
else:
    print('N')