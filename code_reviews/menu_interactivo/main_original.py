"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import os, keyboard, time

def colored_background(r, g, b, text):
    return f'\033[48;2;{r};{g};{b}m{text}\033[0m'

def print_options(selected_index,options):
    os.system('cls')
    for  i, option in enumerate(options):
        if i == selected_index:
            colored_text = colored_background(0, 0, 255, option)
            print(colored_text)
        else:
            print(option)

def choose_option(options):
    option_index = 0
    print_options(option_index,options)

    while True:
        key =keyboard.read_key()
        if key == "up":
            if option_index>0:
                option_index -=1
            print_options(option_index,options)
        elif key == "down":
            if option_index< len(options)-1 :
                option_index +=1
                print_options(option_index,options)
        elif key == "enter":
            os.system("cls")
            break
        time.sleep(0.3) 
    return option_index

if __name__ == "__main__":
    options = ["Frutilla", "Manzana", "Pera"]
    selected_option = choose_option(options)
    print(f"Su eleccion fue {options[selected_option]}")