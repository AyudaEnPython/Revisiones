"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from datetime import datetime, timedelta

import pandas as pd
from requests import get
from requests.exceptions import HTTPError
from prototools import progressbar, text_align
from prototools.constants import MESES

URL = "https://www.datos.gov.co/resource/sgfv-3yp8.json?{}"
PARAMS = "$where=fechaobservacion between '{}' and '{}'"


def _get_dates(yy, mm, format_="%Y-%m-%dT%H:%M:%S"):
    start = datetime(yy, mm, 1)
    if mm == 12:
        end = datetime(yy + 1, 1, 1) - timedelta(seconds=1)
    else:
        end = datetime(yy, mm + 1, 1) - timedelta(seconds=1)
    return start.strftime(format_), end.strftime(format_)


def set_params(yy, mm):
    return PARAMS.format(*_get_dates(yy, mm))


def get_data(params):
    try:
        response = get(URL.format(params))
        response.raise_for_status()
        data = response.json()
    except HTTPError as http_err:
        print(f"HTTP error: {http_err}")
    except Exception as err:
        print(f"Error: {err}")
    else:
        return data


def main():
    text_align("Start")
    for y in range(2008, 2011):
        with pd.ExcelWriter(f"{y}.xlsx") as w:
            for m in progressbar(range(1, 13)):
                data = get_data(set_params(y, m))
                df = pd.DataFrame(data)
                df.to_excel(w, sheet_name=f"{MESES[m-1]}")
        text_align(f"{y} files done!")
    text_align("Finish")


if __name__ == "__main__":
    main()
