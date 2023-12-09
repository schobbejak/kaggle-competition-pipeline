from sklearn.pipeline import Pipeline


def get_post_processing_pipeline(configuration: dict) -> Pipeline:
    """
    Retrieve the post-processing pipeline.
    :param configuration: The post-processing configuration.
    :return: The post-processing pipeline.
    """
    post_processing_pipeline = Pipeline([])
    return post_processing_pipeline
