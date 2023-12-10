# This file combines all steps and returns a pipeline that can be used to
# process the data.

from typing import Optional
import pandas as pd

from sklearn.pipeline import Pipeline

from src.data_processing.parsing.parsing import parse_data
from src.data_processing.preprocessing.preprocessing import get_pp_pipeline
from src.data_processing.pretrain.pretrain import get_pt_pipeline
from src.data_processing.feature_engineering.feature_engineering import get_fe_pipeline


def process_data(data_path: str = "", data_store: str = None, pp_pipeline_steps: list = [], fe_pipeline_steps: list = [], pt_pipeline_steps: list = []) -> tuple[Optional[Pipeline], pd.DataFrame]:
    """
    Process the data from the raw data files into the dataframes used
    for the analysis.
    :param data_path: The path to the data
    :param data_store: The path to the data store
    :param pp_pipeline_steps: The preprocessing pipeline steps
    :param fe_pipeline_steps: The feature engineering pipeline steps
    :param pt_pipeline_steps: The pretraining pipeline steps
    :return: The pipeline and the dataframe
    """

    # Get the pipeline
    steps = []
    pp_pipeline = get_pp_pipeline(pp_pipeline_steps)
    if pp_pipeline:
        steps.append(("preprocessing", pp_pipeline))

    fe_pipeline = get_fe_pipeline(fe_pipeline_steps)
    if fe_pipeline:
        steps.append(("feature_engineering", fe_pipeline))

    pt_pipeline = get_pt_pipeline(pt_pipeline_steps)
    if pt_pipeline:
        steps.append(("pretraining", pt_pipeline))

    # Get necessary data
    df = parse_data(data_path)

    if not steps:
        return None, df

    # Create the pipeline
    pipeline = Pipeline(steps, memory=data_store)

    return pipeline, df


if __name__ == "__main__":
    x = process_data(data_path="data/raw", data_store="data/processed",
                     pp_pipeline_steps=[], fe_pipeline_steps=[], pt_pipeline_steps=[])
    print(x[0])
    print(x[1].head())
