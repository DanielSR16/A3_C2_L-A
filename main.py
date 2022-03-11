import re
import string


mayusculas = list(string.ascii_uppercase)
minusculas = list(string.ascii_lowercase)
letra = minusculas + mayusculas

entrada = 'select daniel from edgar;'
nuevaEntrada = entrada.replace(';',' ;')
listaEntrada = nuevaEntrada.split()

nuevoNombre1 = list(listaEntrada[1])
nuevoNombre2 = list(listaEntrada[3])

listaEntrada[1] = nuevoNombre1
listaEntrada[3] =  nuevoNombre2

print(listaEntrada)
def main():
    resultado = False
    if select(listaEntrada[0]) == True:
            
            if palabra(listaEntrada[1],0) == True:
                
                if fro_m(listaEntrada[2]) == True:

                    if palabra(listaEntrada[3],0) == True:

                        if punto_coma(listaEntrada[4]) == True:
                            resultado = True
                        
                        else:
                            return resultado
                            
                    else:
                    
                        return resultado

                else:
                   
                    return resultado

            else:
               
                  return resultado
    else:
       
        return resultado
    return resultado
   
        


def select(dato):
    validacion = False
    if dato == 'select':
        validacion = True
    return validacion



def fro_m(dato):
    validacion = False
    if dato == 'from':
        validacion = True
    return validacion


def punto_coma(dato):
    validacion = False
    if dato == ';':
        validacion = True
    return validacion


def palabra(datos,contador):
    validacion = False
    if letra_metodo(datos[contador]) == True:
        contador = contador + 1
        validacion = complemento(datos,contador)
        return validacion
    elif letra_metodo(datos[contador]) == False:
        validacion = False
        return validacion
    return validacion
        

def letra_metodo(dato):
    validacion = False
    esLetra = dato in letra

    if esLetra == True:
        validacion = True
    else:
        validacion = False
    return validacion


def complemento(dato,contador):
    bandera = False
    
    while bandera == False :
        resultadoLetra = letra_metodo(dato[contador])
    
        
        if resultadoLetra == False:
            validacion = False
            bandera = True
            break
        
        elif len(dato)-1 == contador:
            validacion = True
            bandera = True


        elif resultadoLetra == True:
            contador = contador + 1 
           

        
          
        
    return validacion
    


print('Resultado:',main())


