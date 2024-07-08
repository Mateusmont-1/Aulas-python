hora_str = input('Informe que horas são: ')

if hora_str.isdigit():
    hora_int = int(hora_str)
    if hora_int <=11 and hora_int >= 0:
        print('Bom dia')
    elif hora_int <= 17:
        print('Boa tarde')
    elif hora_int <=23:
        print('Boa noite')
    else:
        print('Horario informado incorreto')
else:
    print('Valor incorreto')
