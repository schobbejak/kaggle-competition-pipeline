from typing import Optional
from sklearn.pipeline import Pipeline

from src.logging_utils import logger


def get_fe_pipeline(fe_pipeline_steps: list = []) -> Optional[Pipeline]:
    """
    Get the feature engineering pipeline.
    :fe_pipeline_steps: The feature engineering pipeline steps.
    :return: The feature engineering pipeline.
    """

    steps = []

    # Feature engineering steps is none
    if fe_pipeline_steps is None:
        return

    # Add the steps to the pipeline
    for step in fe_pipeline_steps:
        logger.debug(f"Adding step {step} to feature engineering pipeline")
        steps.append((step, match_step(step)))

    return Pipeline(steps)


def match_step(step: str) -> Pipeline:
    """
    Match the step to the pipeline.
    :param step: The step to match.
    :return: The pipeline.
    """

    step_pipeline = None

    match step:
        case _:
            raise ValueError(f"Step {step} not recognized.")

    return step_pipeline
