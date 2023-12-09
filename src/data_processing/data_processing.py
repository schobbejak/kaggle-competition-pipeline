# This file combines all steps and returns a pipeline that can be used to
# process the data.

import pandas as pd

from sklearn.pipeline import Pipeline

from src.data_processing.parsing.parsing import parse_data
from src.data_processing.preprocessing.preprocessing import get_pp_pipeline
from src.data_processing.pretrain.pretrain import get_pt_pipeline
from src.data_processing.feature_engineering.feature_engineering import get_fe_pipeline


def process_data(data_path: str = "", data_store: str = None, pp_pipeline_steps: list = [], fe_pipeline_steps: list = [], pt_pipeline_steps: list = []) -> tuple[Pipeline, pd.DataFrame]:
    """
    Process the data from the raw data files into the dataframes used
    for the analysis.

    Parameters
    ----------
    data_path : str
        The path to the data files.

    Returns
    -------
    pipeline : sklearn.pipeline.Pipeline
        The pipeline used to process the data.
    data: pandas.DataFrame
        The dataframe containing the parsed data.
    """

    # Get the pipeline
    pp_pipeline = get_pp_pipeline(pp_pipeline_steps)
    fe_pipeline = get_fe_pipeline(fe_pipeline_steps)
    pt_pipeline = get_pt_pipeline(pt_pipeline_steps)

    # Create the pipeline
    pipeline = Pipeline([
        ('preprocessing', pp_pipeline),
        ('feature_engineering', fe_pipeline),
        ('pretraining', pt_pipeline),
    ], memory=data_store)

    # Get necessary data
    df = parse_data(data_path)

    return pipeline, df


if __name__ == "__main__":
    process_data(data_path="data/raw/train.csv", data_store="data/processed", pp_pipeline_steps=["mem_reduce"], fe_pipeline_steps=[], pt_pipeline_steps=[])
