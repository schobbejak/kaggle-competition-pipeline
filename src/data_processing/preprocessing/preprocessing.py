from typing import Optional
from sklearn.pipeline import Pipeline

from src.logging_utils.logger import logger


def get_pp_pipeline(pp_pipeline_steps: list = []) -> Optional[Pipeline]:
    """
    Get the preprocessing pipeline.
    :param pp_pipeline_steps: The preprocessing steps to include in the pipeline.
    :return: The preprocessing pipeline.
    """

    steps = []

    # Preprocessing steps is none
    if not pp_pipeline_steps:
        return

    # Add the steps to the pipeline
    for step in pp_pipeline_steps:
        logger.debug(f"Adding step {step} to preprocessing pipeline")
        steps.append((step, match_step(step)))

    return Pipeline(steps)


def match_step(step: str) -> Pipeline:
    """
    Match the step to the corresponding pipeline.
    :param step: The step to match.
    :return: The pipeline corresponding to the step.
    """

    step_pipeline = None

    match step:
        case _:
            raise ValueError(f"Step {step} not recognized.")

    return step_pipeline
