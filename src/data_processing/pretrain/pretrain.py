from typing import Optional
from sklearn.pipeline import Pipeline
from src.logging_utils.logger import logger


def get_pt_pipeline(pt_pipeline_steps: list = [], data_store: str = None) -> Optional[Pipeline]:
    """
    Get the pretraining pipeline.
    :param pt_pipeline_steps: The steps to include in the pretraining pipeline.
    :param data_store: The data store to use for the pipeline.
    :return: The pretraining pipeline.
    """

    steps = []

    # Pretraining steps is none
    if pt_pipeline_steps is None:
        return

    # Add the steps to the pipeline
    for step in pt_pipeline_steps:
        logger.debug(f"Adding step {step} to pretraining pipeline")
        steps.append(match_step(step, data_store=data_store))

    return Pipeline(steps)


def match_step(step: dict, data_store: str = None) -> tuple[str, Pipeline]:
    """
    Match the step to the corresponding pipeline.
    :param step: The step to match.
    :param data_store: The data store to use for the pipeline.
    :return: The pipeline corresponding to the step.
    """

    step_pipeline = None

    # Check step has a name key, used to match the step
    assert "name" in step.keys(), "Step does not have a name key."

    # Match the step
    name = step["name"]

    match name:
        case _:
            raise ValueError(f"Step {step} not recognized.")

    return (name, step_pipeline)
