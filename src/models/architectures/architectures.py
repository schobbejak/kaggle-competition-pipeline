from sklearn.pipeline import Pipeline


def get_architecture_pipeline(architecture_configuration: dict) -> Pipeline:
    """
    Retrieve the architecture pipeline.
    :param architecture_configuration: The architecture configuration.
    :return: The architecture pipeline.
    """
    architecture_pipeline = Pipeline([])
    return architecture_pipeline
