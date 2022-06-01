"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from typing import Any, Dict

Configuration = Dict[str, Dict[str, Any]]
CFG: Configuration = {
    "btn": {
        "fg": "white",
        "bg": "#0051C8",
        "bd": 2,
        "relief": "flat",
        "cursor": "hand1",
        "overrelief": "raise",
    },
    "btn_cancel": {
        "fg": "white",
        "bg": "#E81123",
        "bd": 2,
        "relief": "flat",
        "cursor": "hand1",
        "overrelief": "raise",
    },
    "lbl": {
        "font": (8),
        "fg": "white",
        "bg": "#314252",
    },
    "ent": {
        "font": ("Arial", 12),
        "bg": "#E7E7E7",
        "relief": "flat",
    }
}
