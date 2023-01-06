def p():
    import msvcrt
    from colorama import Back, Fore, init, Style, Cursor;
    import os;
    init(autoreset=True)
    x, y=(1,1)
    x=x+1
    y=y+1
    a=':)';
    b='+';
    print(Fore.LIGHTYELLOW_EX+Cursor.POS(2,9)+a,end='');
    print(Fore.LIGHTYELLOW_EX+b,end='');
    while True:
        tecla=ord(msvcrt.getch())
        if tecla==72: #arriba...
            os.system('cls');
            print(Cursor.POS(1,1)+'hOLA')
            print(Fore.LIGHTGREEN_EX+Cursor.POS(2,14)+a)
            print('se a movido')
            continue;
    input();
p();