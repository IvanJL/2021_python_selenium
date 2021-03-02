
def revese_int(number):
    aux = str(number)
    aux = aux[::-1]
    if(isinstance(number,int)):
        number = int(aux)
    else:
        number = float(aux)
    return number

x = 12345.234
print(revese_int(x))
