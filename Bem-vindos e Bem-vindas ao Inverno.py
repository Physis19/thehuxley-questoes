temperaturas = input().split()
dia1 = int(temperaturas[0])
dia2 = int(temperaturas[1])
dia3 = int(temperaturas[2])

if dia2 < dia1 and dia2 <= dia3:
    print(':)')

elif dia3 - dia2 >= dia2 - dia1:
    print(':)')

elif dia2 - dia3 < dia1 - dia2:
    print(':)')

elif dia1 == dia2 and dia3 > dia2:
    print(':)')

else:
    print(':(')