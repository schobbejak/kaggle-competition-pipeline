from typing import Optional
from sklearn.pipeline import Pipeline
from src.logging_utils.logger import logger


def get_pp_pipeline(pp_pipeline_steps: list = [], data_store: str = None) -> Optional[Pipeline]:
    """
    Get the preprocessing pipeline.
    :param pp_pipeline_steps: The preprocessing steps to include in the pipeline.
    :param data_store: The data store to use for the pipeline.
    :return: The optional preprocessing pipeline.
    """

    steps = []

    # Preprocessing steps is none
    if not pp_pipeline_steps:
        return

    # Add the steps to the pipeline
    for step in pp_pipeline_steps:
        logger.debug(f"Adding step {step} to preprocessing pipeline")
        steps.append(match_step(step, data_store=data_store))

    return Pipeline(steps, memory=data_store)


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
