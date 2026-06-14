from collections.abc import Sequence
from dataclasses import asdict, dataclass
from numbers import Real
from statistics import mean, median, mode, stdev
from typing import Final


@dataclass(frozen=True, slots=True)
class Metrics:
    mean: float
    median: float
    mode: float
    stdev: float


def validate_values(values: Sequence[int | float]) -> None:
    if len(values) < 2:
        raise ValueError("At least two values are required.")
    if not all(isinstance(v, Real) and not isinstance(v, bool) for v in values):
        raise TypeError("All elements must be numeric.")


def get_metrics(values: Sequence[int | float]) -> Metrics:
    return Metrics(
        mean=float(mean(values)),
        median=float(median(values)),
        mode=float(mode(values)),
        stdev=float(stdev(values)),
    )


def main():
    values: Final[list[int]] = [12, 15, 12, 18, 21, 24, 27, 30, 33, 12]
    try:
        validate_values(values)
        metrics = asdict(get_metrics(values))
        print(", ".join(f"{k}={v:.2f}" for k, v in metrics.items()))
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
