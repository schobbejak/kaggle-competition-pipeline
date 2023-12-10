from typing import Optional
from sklearn.pipeline import Pipeline

from src.logging_utils import logger


def get_pt_pipeline(pt_pipeline_steps: list = []) -> Optional[Pipeline]:
    """
    Get the pretraining pipeline.
    :param pt_pipeline_steps: The steps to include in the pretraining pipeline.
    :return: The pretraining pipeline.
    """

    steps = []

    # Pretraining steps is none
    if pt_pipeline_steps is None:
        return

    # Add the steps to the pipeline
    for step in pt_pipeline_steps:
        logger.debug(f"Adding step {step} to pretraining pipeline")
        steps.append((step, pt_pipeline_steps[step]))

    return Pipeline(steps)


def match_step(step: str) -> Pipeline:
    """
    Match the step to the corresponding function.
    :param step: The step to match.
    :return: The pipeline corresponding to the step.
    """

    step_pipeline = None

    match step:
        case _:
            raise ValueError(f"Step {step} not recognized.")

    return step_pipeline
