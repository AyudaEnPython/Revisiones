"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from fileinput import filename
import pandas as pd
import numpy as np
from typing import Any, Dict, Tuple

Data = Tuple[Any, int, int, pd.DataFrame, pd.DataFrame]
DataMix = Tuple[Tuple[str, ...], Tuple[Any, ...]]
CFG: Dict[str, Dict[int, str]] = {
    "db": {
        -1: "La grafica del S11 bajo {} dB",
        1: "La grafica del S11 subio {} dB",
        0: "La grafica del S11 permaneio en el mismo lugar {} dB",
    },
    "fr": {
        -1: "La grafica se movio a la izquierda {} Hz",
        1: "La grafica se movio a la derecha {} Hz",
        0: "La grafica permaneci en el misma posicion {} Hz",
    }
}


def get_data(filename: str, f1: str, magnitud: str, db: str) -> Data:
    df = pd.read_excel(filename)
    datos = df["# HZ S RI R 50"].str.split(expand=True)
    datos.columns = [f1, "Parte Real", "Parte imaginaria"]
    df = pd.concat([datos], axis=1)
    v = np.array(df)
    x, y = v[:,1], v[:,2]
    df[magnitud] = [((float(x[i])*2+float(y[i])*2)**0.5) for i in range(101)]
    df[db] = np.log10(df[magnitud]) * 20
    min_ = df[db].min()
    idx_min = df[db].idxmin()
    idx_max = df[db].idxmax()
    n_df = df.iloc[[idx_min], [0, 4]]
    return (min_, idx_min, idx_max, n_df, df)


def process_data(data_x: Data, data_y: Data) -> DataMix:
    min_1, idx_min_1, idx_max_1, ndf_1, df_1 = data_x # idx_max_1 is not used
    min_2, idx_min_2, idx_max_2, ndf_2, df_2 = data_y # idx_max_2 is not used
    diferencia1 = abs(min_2 - min_1)
    diff = min_1 - min_2
    fr_1 = int(df_1.at[idx_min_1, "F1"])
    fr_2 = int(df_2.at[idx_min_2, "F2"])
    diferencia2 = fr_2 - fr_1
    return (
        "Ubicacion del minimo de S11(dB)_1:", ndf_1.to_string(), "-"*56,
        "Ubicacion del minimo de S11(dB)_2:", ndf_2.to_string(), "-"*56,
        "Diferencia entre S11(dB)_1 y S11(dB)_2:", str(diferencia1), "-"*56,
        "Diferencia entre F1 y F2:", str(diferencia2)
    ), (diff, diferencia1, diferencia2)
