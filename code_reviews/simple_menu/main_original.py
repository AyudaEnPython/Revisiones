"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import pyfiglet
from colorama import init , Fore

while 1:
    init()
    Banner = pyfiglet.figlet_format("CODIGO XD")
    
    print(Fore.RED , Banner , Fore.GREEN , """[+] 1 Saludar
    [+] 2 Presentarse
    [+] 3 Pedir informacion
    [+] 4 Despedirse """)
    
    try:
        p = int(input('\nopcion >> '))
    except ValueError:
        print('\nes cribe numeros no letras numeros')
    try:
        def mi (p):
            if p == 1:
                n = input("\nTu nombre >> ")
                print(f'\nHola {n} ')
            elif p == 2:
                print('\n¿como te presentarias dime ?')
            else:
                print("FIN ...")
        mi(p)
    except NameError:
        print("\nbuelve a intentarlo")