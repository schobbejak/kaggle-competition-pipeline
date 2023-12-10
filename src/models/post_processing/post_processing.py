from typing import Optional
from sklearn.pipeline import Pipeline


def get_post_processing_pipeline(configuration: dict) -> Optional[Pipeline]:
    """
    Retrieve the post-processing pipeline.
    :param configuration: The post-processing configuration.
    :return: The post-processing pipeline.
    """

    # No post-processing configuration
    if configuration is None:
        return

    post_processing_pipeline = Pipeline([])
    return post_processing_pipeline
