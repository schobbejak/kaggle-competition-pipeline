from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline


def get_architecture_pipeline(architecture_configuration: dict) -> Pipeline | ColumnTransformer:
    """
    Retrieve the architecture pipeline.
    :param architecture_configuration: The architecture configuration.
    :return: The architecture pipeline.
    """

    # No architecture configuration
    if architecture_configuration is None:
        return ColumnTransformer([])

    architecture_pipeline = Pipeline([])
    return architecture_pipeline
