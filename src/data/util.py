import os.path
import sys

import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from base import DATA_DIR

def save_to_csv(data, fname):
    data.to_csv(os.path.join(DATA_DIR, fname), index=False)
def load_from_excel(fname, **kwargs):
    return pd.read_excel(os.path.join(DATA_DIR, fname), **kwargs)
def load_from_csv(fname, **kwargs):
    return pd.read_csv(filepath_or_buffer=os.path.join(DATA_DIR, fname), **kwargs)
def apply_and_save(df: pd.DataFrame, func, fname, **kwargs):
    new_df = func(df.copy(deep=True), **kwargs)
    new_df.to_csv(os.path.join(DATA_DIR, fname), index=False)
    return new_df