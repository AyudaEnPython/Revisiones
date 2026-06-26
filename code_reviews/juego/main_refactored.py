"""AyudaEnPython: https://www.facebook.com/groups/ayudapython"""

from dataclasses import dataclass
from random import randint
from typing import Iterator

GOAL = 25


@dataclass(frozen=True)
class SquareEffect:
    delta: int = 0
    bonus: int = 0
    message: str = ""


MSG = {
    "welcome": "¡BIENVENIDO AL JUEGO DE LA CASILLA 25!",
    "play_intent": "¿Deseas iniciar una partida?",
    "farewell": "¡Hasta la próxima!",
    "prompt_1": "Nombre del Primer Jugador: ",
    "prompt_2": "Nombre del Segundo Jugador: ",
    "start_game": "\n¡A jugar!\nGana quien llegue primero a la casilla {goal}.",
    "turn_header": "Turno de: {player}",
    "roll_prompt": "Presiona Enter para lanzar el dado...",
    "die_rolled": "Dado lanzado: {roll}",
    "player_moved": "{name} avanzó a la casilla {position} (+{roll} puntos).",
    "overshot": "¡Te pasaste! Regresas a tu posición y no sumas puntos.",
    "loop_detected": "¡Bucle de efecto detectado! Deteniendo resolución.",
    "clamp_low": " -> Posición ajustada al límite inferior: Casilla 0.",
    "clamp_high": " -> Posición ajustada al límite superior: Casilla {goal}.",
    "invalid_answer": "Respuesta no válida. Por favor responde 'si' o 'no'.",
    "winner": "¡GANADOR: {name} con {points} puntos!",
    "runner_up": "Segundo lugar: {name} (Casilla {position}, {points} puntos)",
}

BOARD_MSG = {
    "effect_5": "Mala suerte: retrocede 4 casillas.",
    "effect_8": "¡Suerte! Saltas a la 13 y sumas +3 puntos.",
    "effect_9": "¡Excelente! +5 puntos.",
    "effect_10": "Trampa con truco: vuelves a la 8 y sumas +3 puntos.",
    "effect_14": "¡Ouch! Regresas a la casilla 6.",
    "effect_15": "¡Genial! Avanzas a la 20 y ganas +5 puntos.",
    "points_added": " -> Puntos: +{bonus} (Total: {points}).",
    "moved_direction": (
        " -> Desplazamiento: {direction} {abs_delta} "
        "casillas (Casilla actual: {position})."
    ),
}

CONFIG: dict[int, SquareEffect] = {
    5: SquareEffect(delta=-4, message="effect_5"),
    8: SquareEffect(delta=5, bonus=3, message="effect_8"),
    9: SquareEffect(bonus=5, message="effect_9"),
    10: SquareEffect(delta=-2, bonus=3, message="effect_10"),
    14: SquareEffect(delta=-8, message="effect_14"),
    15: SquareEffect(delta=5, bonus=5, message="effect_15"),
}


def roll_die(min_val: int = 1, max_val: int = 6) -> int:
    return randint(min_val, max_val)


@dataclass
class Player:
    name: str
    position: int = 0
    points: int = 0

    def apply_move(self, steps: int) -> None:
        self.position += steps
        self.points += steps

    def restore_state(self, position: int, points: int) -> None:
        self.position = position
        self.points = points

    def __str__(self) -> str:
        return f"{self.name} (Casilla: {self.position}, Puntos: {self.points})"


class Board:
    def __init__(
        self, effects: dict[int, SquareEffect] | None = None, goal: int = GOAL
    ):
        self.effects = effects or {}
        self.goal = goal

    def resolve(self, player: Player) -> Iterator[str]:
        visited: set[int] = set()
        while player.position in self.effects:
            if player.position in visited:
                yield MSG["loop_detected"]
                break
            visited.add(player.position)
            effect = self.effects[player.position]
            if effect.message:
                yield BOARD_MSG[effect.message]
            if effect.bonus:
                player.points += effect.bonus
                yield BOARD_MSG["points_added"].format(
                    bonus=effect.bonus, points=player.points
                )
            if effect.delta:
                player.position += effect.delta
                direction = "adelante" if effect.delta > 0 else "atrás"
                yield BOARD_MSG["moved_direction"].format(
                    direction=direction,
                    abs_delta=abs(effect.delta),
                    position=player.position,
                )
                if player.position < 0:
                    player.position = 0
                    yield MSG["clamp_low"]
                elif player.position > self.goal:
                    player.position = self.goal
                    yield MSG["clamp_high"].format(goal=self.goal)
            else:
                break


class Game:
    def __init__(self, p1_name: str, p2_name: str, board: Board | None = None):
        self.board = board or Board(CONFIG, GOAL)
        self.players = [
            Player(p1_name.strip() or "Jugador 1"),
            Player(p2_name.strip() or "Jugador 2"),
        ]
        self.current_index = 0

    @property
    def current(self) -> Player:
        return self.players[self.current_index]

    @property
    def opponent(self) -> Player:
        return self.players[1 - self.current_index]

    def switch_turn(self) -> None:
        self.current_index = 1 - self.current_index

    def execute_turn(self, roll: int) -> list[str]:
        player = self.current
        turn_logs = [MSG["die_rolled"].format(roll=roll)]
        prev_pos, prev_pts = player.position, player.points
        player.apply_move(roll)
        turn_logs.append(
            MSG["player_moved"].format(
                name=player.name, position=player.position, roll=roll
            )
        )
        if player.position > self.board.goal:
            player.restore_state(prev_pos, prev_pts)
            turn_logs.append(MSG["overshot"])
        else:
            turn_logs.extend(self.board.resolve(player))
        return turn_logs

    def is_over(self) -> bool:
        return self.current.position == self.board.goal


def prompt_yes_no(question: str) -> bool:
    while True:
        ans = input(f"{question} (si/no): ").strip().lower()
        if ans in ("si", "s", "yes", "y"):
            return True
        if ans in ("no", "n"):
            return False
        print(MSG["invalid_answer"])


def main() -> None:
    print(f"{'=' * 50}\n{MSG['welcome']}\n{'=' * 50}")
    if not prompt_yes_no(MSG["play_intent"]):
        print(MSG["farewell"])
        return
    game = Game(input(MSG["prompt_1"]).strip(), input(MSG["prompt_2"]).strip())
    print(MSG["start_game"].format(goal=game.board.goal))
    while True:
        player = game.current
        print("-" * 50)
        print(MSG["turn_header"].format(player=player))
        input(MSG["roll_prompt"])
        for line in game.execute_turn(roll_die()):
            print(line)
        if game.is_over():
            print("=" * 50)
            print(MSG["winner"].format(name=player.name, points=player.points))
            print(
                MSG["runner_up"].format(
                    name=game.opponent.name,
                    position=game.opponent.position,
                    points=game.opponent.points,
                )
            )
            print("=" * 50)
            break
        game.switch_turn()


if __name__ == "__main__":
    main()
