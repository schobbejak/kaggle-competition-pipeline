import time
from src.configs.parser import YAMLParser
from src.full_pipeline import retrieve_full_pipeline
from src.logging_utils.logger import logger


def run_model(path: str) -> None:
    """
    Main function for running the model.
    :param path: Path to the data
    """

    logger.info("Running model training")
    start_time = time.time()

    # Run model always loads model config from model.yaml
    model_config_parser = YAMLParser(path)
    model_config = model_config_parser.parse()
    model_exists = False

    # TODO: Check if model exists
    if model_exists:
        pass
    else:
        # Train model

        # Get pipeline and data
        logger.info("Retrieving full pipeline")
        assert model_config is not None, "Model configuration is None"
        assert "data_processing" in model_config.keys(
        ), "data_processing is not in the model configuration"
        assert "model" in model_config.keys(
        ), "model is not in the model configuration"
        pipeline, data = retrieve_full_pipeline(
            model_config["data_processing"], model_config["model"])
        logger.info("Retrieved full pipeline")

        # Fit the pipeline
        logger.info("Fitting pipeline")
        pipeline.fit(data)

    end_time = time.time()
    logger.info(
        f"Model training finished: {end_time - start_time:.2f} seconds")


if __name__ == "__main__":

    import coloredlogs
    coloredlogs.install()

    run_model(path="configs/model.yaml")
