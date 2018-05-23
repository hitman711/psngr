""" """
import logging
import pandas as pd

logs = logging.getLogger(__name__)


def cache_csv_data(DB_URL, URL_OUTPUT_TYPE):
    """ """
    try:
        return pd.DataFrame(
            pd.read_csv(
                DB_URL + URL_OUTPUT_TYPE,
                sep=",", header=0, index_col=False))
    except Exception as e:
        logs.exception(e)
        return None
