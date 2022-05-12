"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from prototools import Menu, write_letters, magenta, cyan, yellow

menu = Menu(
    cyan("Asesor Personal"),
    yellow("Just a demo"),
    exit_option_text=magenta("Despedirse"),
    exit_option_color=magenta,
)
menu.add_options(
    ("Saludar",
        lambda: print("Bienvenido")),
    ("Presentarse",
        lambda: print("Soy tu asesor personal")),
    ("Pedir Informacion",
        lambda: print(f"Hola {input('¿Cuál es tu nombre? ')}")),
)
menu.settings(
    subtitle_align="center",
    style="double",
    color=magenta,
    options_color=yellow,
    separators=True,
)
menu.run()
write_letters("Hasta la proxima!")
