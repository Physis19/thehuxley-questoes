valores_glicose=[]
while True:
    glicose = int(input())
    if glicose == 0:
        break
    valores_glicose.append(int(glicose))

qtd_glicose = len(valores_glicose)
media_glicose =  sum(valores_glicose) / qtd_glicose

if media_glicose < 110:
    print('Glicose Normal')
elif media_glicose >= 200:
    print('Glicose Muito Alta')
else:
    print('Glicose Alterada')


    
