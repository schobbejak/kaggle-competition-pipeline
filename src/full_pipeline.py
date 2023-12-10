from numpy import ndarray
from pandas import DataFrame
from sklearn.pipeline import Pipeline

from src.data_processing.data_processing import process_data
from src.logging_utils.logger import logger
from src.models.models import get_model


def retrieve_full_pipeline(data_configuration: dict, model_configuration: dict) -> tuple[Pipeline, ndarray | DataFrame]:
    """
    Retrieve the full pipeline for the model training.
    :param model_configuration: The model configuration.
    :param data_configuration: The data configuration.
    """

    # Assert that the data configuration is correct
    assert data_configuration is not None, "Data configuration is None"
    assert "data_store" in data_configuration.keys(
    ) and data_configuration["data_store"], "data_store is not in the data configuration"
    assert "data_path" in data_configuration.keys(
    ) and data_configuration["data_path"], "data_path is not in the data configuration"
    assert "pp_pipeline_steps" in data_configuration.keys(
    ), "pp_pipeline_steps is not in the data configuration"
    assert "fe_pipeline_steps" in data_configuration.keys(
    ), "fe_pipeline_steps is not in the data configuration"
    assert "pt_pipeline_steps" in data_configuration.keys(
    ), "pt_pipeline_steps is not in the data configuration"

    # Assert that the model configuration is correct
    assert model_configuration is not None, "Model configuration is None"
    assert "architecture" in model_configuration.keys(
    ), "architecture is not in the model configuration"
    assert "post_processing" in model_configuration.keys(
    ), "post_processing is not in the model configuration"

    # Get the data pipeline
    logger.debug(
        f"Retrieving data pipeline, data store: {data_configuration['data_store']}, data path: {data_configuration['data_path']}")
    data_pipeline, data = process_data(data_store=data_configuration["data_store"],
                                       data_path=data_configuration["data_path"],
                                       pp_pipeline_steps=data_configuration["pp_pipeline_steps"],
                                       fe_pipeline_steps=data_configuration["fe_pipeline_steps"],
                                       pt_pipeline_steps=data_configuration["pt_pipeline_steps"])
    if not data_pipeline:
        logger.error("Data pipeline is None")
    assert data is not None, "Data is None"
    logger.debug("Retrieved data pipeline")

    # Get the model pipeline
    logger.debug(
        f"Retrieving model pipeline, architecture: {model_configuration['architecture']}, post-processing: {model_configuration['post_processing']}")
    model_pipeline = get_model(
        model_configuration["architecture"], model_configuration["post_processing"])
    if not model_pipeline:
        logger.error("Model pipeline is None")
    logger.debug("Retrieved model pipeline")

    full_pipeline = Pipeline([
        ('data_processing', data_pipeline),
        ('model', model_pipeline)
    ])
    return full_pipeline, data
