from sklearn.pipeline import Pipeline
from src.models.architectures.architectures import get_architecture_pipeline
from src.models.post_processing.post_processing import get_post_processing_pipeline


def get_model(model_architecture: dict, post_processing: dict) -> Pipeline:
    """
    Retrieve the model pipeline.
    :param model_configuration: The model configuration.
    :param post_processing: The post-processing configuration.
    :return: The model pipeline.
    """
    # Assert that the model configuration is correct
    assert model_architecture is not None, "Model architecture is None"

    # Assert that the post-processing configuration is correct
    assert post_processing is not None, "Post-processing configuration is None"
    assert "post_processing_steps" in post_processing.keys(
    ), "post_processing_steps is not in the post-processing configuration"

    # Get the individual pipelines
    architecture_pipeline = get_architecture_pipeline(
        model_architecture)
    post_processing_pipeline = get_post_processing_pipeline(
        post_processing)

    # Get the model pipeline
    model_pipeline = Pipeline([
        ('architecture', architecture_pipeline),
        ('post_processing', post_processing_pipeline)
    ])
    return model_pipeline
