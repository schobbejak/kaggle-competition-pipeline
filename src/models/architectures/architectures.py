from typing import Optional
from sklearn.pipeline import Pipeline


def get_architecture_pipeline(architecture_configuration: dict) -> Optional[Pipeline]:
    """
    Retrieve the architecture pipeline.
    :param architecture_configuration: The architecture configuration.
    :return: The architecture pipeline.
    """

    # No architecture configuration
    if architecture_configuration is None:
        return

    architecture_pipeline = Pipeline([])
    return architecture_pipeline
