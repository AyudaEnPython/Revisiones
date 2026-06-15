"""AyudaEnPython: https://www.facebook.com/groups/ayudapython"""

from random import randint
from typing import Any, Callable

Choice = tuple[str, str]
Players = list[str]
Scores = list[int]
Leaderboard = dict[str, Scores]
Result = list[tuple[str, int]]
Results = tuple[Result, Result]

MAX_SCORE = 50
MANDATORY_ROLLS = 3
MAX_TURNS = 6


def _safe_io(io_func: Callable[..., Any], *args: Any, **kwargs: Any) -> Any:
    try:
        return io_func(*args, **kwargs)
    except (EOFError, KeyboardInterrupt):
        print("\nInput cancelled. Exiting game execution cleanly.")
        raise SystemExit


def int_input(prompt: str, err_msg: str = "Invalid input. Try again!") -> int:
    while True:
        try:
            return int(_safe_io(input, prompt))
        except ValueError:
            print(err_msg)


def bool_input(
    prompt: str, yes: Choice = ("y", "yes"), no: Choice = ("n", "no")
) -> bool:
    hint = f"({yes[0]}/{no[0]})"
    while True:
        response = _safe_io(input, f"{prompt} {hint}\n> ").strip().lower()
        if response in yes:
            return True
        if response in no:
            return False
        print(f"Please answer with '{yes[0]}' or '{no[0]}'.")


def init_players(quantity: int) -> Players:
    players = []
    for n in range(1, quantity + 1):
        while True:
            nickname = _safe_io(input, f"Player {n:02d} nickname: ").strip()
            if not nickname or "\n" in nickname:
                print("Invalid nickname.")
                continue
            if nickname in players:
                print(f"'{nickname}' is already taken.")
                continue
            players.append(nickname)
            break
    return players


def roll_dice(turn: int) -> int:
    a, b = randint(1, 6), randint(1, 6)
    total = a + b
    print(f"Roll {turn}: {a} and {b} (Sum: {total})")
    return total


def play_turn(nickname: str) -> Scores:
    print(f"\n--- {nickname}'s Turn ---")
    scores = []
    running_score = 0
    for turn in range(1, MAX_TURNS + 1):
        if turn > MANDATORY_ROLLS:
            if running_score >= MAX_SCORE:
                break
            print(f"Current accumulated score: {running_score}")
            if not bool_input("Do you want to roll again?"):
                break
        roll = roll_dice(turn)
        scores.append(roll)
        running_score += roll
        if running_score >= MAX_SCORE:
            break
    print(f"Roll history: {', '.join(map(str, scores))}")
    print(f"{nickname}'s final score: {running_score}")
    if running_score > MAX_SCORE:
        print(f"Busted! You went over {MAX_SCORE}.")
    return scores


def _sorted_results(leaderboard: Leaderboard) -> Results:
    valid_entries = []
    busted_entries = []
    for name, scores in leaderboard.items():
        total = sum(scores)
        if total <= MAX_SCORE:
            valid_entries.append((name, total))
        else:
            busted_entries.append((name, total))
    valid_entries = sorted(valid_entries, key=lambda x: x[1], reverse=True)
    busted_entries = sorted(busted_entries, key=lambda x: x[1])
    return valid_entries, busted_entries


def display_results(leaderboard: Leaderboard) -> None:
    results, busted = _sorted_results(leaderboard)
    if results:
        print("\n--- Leaderboard ---")
        for rank, (name, score) in enumerate(results, start=1):
            print(f"{rank:02d}. {name} - {score} points.")
        winner, top_score = results[0]
        winners = [name for name, score in results if score == top_score]
        print("\n--- Final Result ---")
        if len(winners) == 1:
            print(f"The winner is '{winner}' with {top_score} points.")
        else:
            names = ", ".join(f"'{name}'" for name in winners)
            print(f"It's a tie between {names} with {top_score} points each.")
    else:
        print("\n--- Final Result ---")
        print(f"No winners! Everyone busted over {MAX_SCORE} points.")
    if busted:
        print("\n--- Busted Players ---")
        for name, total in busted:
            print(f"- {name}: {total} points.")


def validate_config() -> bool:
    if MANDATORY_ROLLS < 0 or MAX_TURNS < 1:
        return False
    if MANDATORY_ROLLS > MAX_TURNS:
        return False
    return True


def main():
    if not validate_config():
        print("System Configuration Error: Check rule bounds.")
        return
    quantity = int_input("Number of players: ")
    if quantity <= 0:
        print("You need at least 1 player to start the match.")
        return
    players = init_players(quantity)
    leaderboard = {}
    for nickname in players:
        leaderboard[nickname] = play_turn(nickname)
    display_results(leaderboard)


if __name__ == "__main__":
    main()
