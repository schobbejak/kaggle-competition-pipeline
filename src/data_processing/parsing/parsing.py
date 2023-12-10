# This file contains the functions used to parse the data from the
# raw data files into the dataframes used for the analysis.
import pandas as pd
from numpy import ndarray


def parse_data(data_path: str) -> pd.DataFrame | ndarray:
    """
    Parse the data from the raw data files into the dataframes used for the analysis.
    :param data_path: The path to the data

    """
    # Read in the train data
    x = False
    #assert x is True, "Custom parsing for competition data not implemented yet"

    data_path = data_path + "/train.csv"
    df = pd.read_csv(data_path)

    return df
