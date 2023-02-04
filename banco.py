total = 20000
ruta = "$HOME/vstudio/python/os/banco.py"

from os import system
from colorama import Fore , Back , Style


def limpiar():
    system("clear")
print(Back.BLACK + Fore.WHITE + Style.BRIGHT)

def saldo():
    limpiar();
    print("\tSaldo total de su cuenta :",total)

def condicionales():    
    try:
        entry = input("\nDesea consignar(c) o retirar(r): ")  
        if entry == "c":
            saldo()
            
            consignar = int(input("\nCuando desea consignar: "))
            limpiar()
            suma = total + consignar

            cadena = "sed -i 's/{}/{}/g' {}".format(total, suma, ruta)
            system(cadena)
            
            print("Su saldo es: ",Fore.GREEN)
            system("head -n 1 $HOME/vstudio/python/os/banco.py | cut -c 9-25")
            
        elif entry == "q":
            exit
                                   
        elif entry == "r":
            saldo()
                        
            retirar = int(input("\nCuanto desea retirar: "))
            limpiar()
            resta = total - retirar

            cadena = "sed -i 's/{}/{}/g' {}".format(total, resta, ruta)            
            system(cadena)
            
            print("Su saldo es: ",Fore.RED)
            system(" head -n 1 $HOME/vstudio/python/os/banco.py | cut -c 9-25")
            
        else:
            print(Fore.RED,"\nLas opciones solo son (c) y (r) vuelva a intentarlo...")  
        
                                  
    except ValueError:
        limpiar()
        print(Fore.RED,"¡Solo numeros!")
        
#-----------------------------------------------------------------------------------------------

def main():
    try:
        saldo()
        condicionales()            
    except KeyboardInterrupt:
        limpiar()    
        
if __name__ == "__main__":
    main()
    
    