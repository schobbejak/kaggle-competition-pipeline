from sklearn.pipeline import Pipeline

from src.logging_utils import logger


def get_fe_pipeline(fe_pipeline_steps: list = []) -> Pipeline:
    """
    Get the feature engineering pipeline.
    :fe_pipeline_steps: The feature engineering pipeline steps.
    :return: The feature engineering pipeline.
    """

    steps = []

    # Feature engineering steps is none
    if fe_pipeline_steps is None:
        return Pipeline(steps)

    # Add the steps to the pipeline
    for step in fe_pipeline_steps:
        logger.debug(f"Adding step {step} to feature engineering pipeline")
        steps.append((step, match_step(step)))

    return Pipeline(steps)


def match_step(step: str) -> Pipeline:
    """
    Match the step to the corresponding function.

    Parameters
    ----------
    step : str
        The step to match.

    Returns
    -------
    function : function
        The function corresponding to the step.
    """

    step_pipeline = None

    match step:
        case _:
            raise ValueError(f"Step {step} not recognized.")

    return step_pipeline
