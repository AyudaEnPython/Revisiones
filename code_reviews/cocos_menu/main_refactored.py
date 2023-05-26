from cocos.director import director
from cocos.scene import Scene
from cocos.menu import (
    Menu,
    ColorMenuItem,
    EntryMenuItem,
    ImageMenuItem,
    MenuItem,
    MultipleMenuItem,
    ToggleMenuItem,
)


class MainMenu(Menu):

    def __init__(self, title):
        super().__init__(title)
        self.create_menu([
            ToggleMenuItem(
                "Sonido: ",
                lambda: None,
                True,
            ),
            MultipleMenuItem(
                "Resolución: ",
                lambda: None,
                ["640x480", "800x600", "1024x480", "1270x720", "1600x900"],
            ),
            ColorMenuItem(
                "Color: ",
                lambda: None,
                [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 200, 200)],
            ),
            EntryMenuItem(
                "Dificultad (1-10): ",
                lambda: None,
                "",
                max_length=2,
            ),
            ImageMenuItem(
                "logo.png",
                lambda: None,
            ),
            MenuItem(
                "Salir",
                director.window.close,
            ),
        ])


if __name__ == "__main__":
    director.init(width=800, height=600, caption="AyudaEnPython")
    menu = MainMenu("Menu Principal")
    director.run(Scene(menu))
