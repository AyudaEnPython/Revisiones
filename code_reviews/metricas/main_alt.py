from statistics import mean, median, mode, stdev
from typing import Final, Sequence


def get_metrics(values: Sequence[int | float]) -> dict[str, int | float]:
    return {
        "Mean": mean(values),
        "Median": median(values),
        "Mode": mode(values),
        "Stdev": stdev(values),
    }


values: Final[list[int]] = [12, 15, 12, 18, 21, 24, 27, 30, 33, 12]
metrics = get_metrics(values)
print(", ".join(f"{k}={v:.2f}" for k, v in metrics.items()))
