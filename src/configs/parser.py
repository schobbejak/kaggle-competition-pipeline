import json
import yaml

from abc import ABC, abstractmethod


class Parser(ABC):
    @abstractmethod
    def parse(self) -> dict:
        """Parse the config file and return a dictionary"""
        pass


class YAMLParser(Parser):
    def __init__(self, filepath) -> None:
        """
        Initialize the YAML parser with the filepath
        :param filepath: The path to the YAML config file
        """
        self.filepath = filepath

    def parse(self) -> dict:
        """
        Parse the YAML config file and return a dictionary
        :return: The dictionary containing the config data
        """
        with open(self.filepath, 'r') as file:
            data = yaml.safe_load(file)
        return data


class JSONParser(Parser):
    def __init__(self, filepath) -> None:
        """
        Initialize the JSON parser with the filepath
        :param filepath: The path to the JSON config file
        """
        self.filepath = filepath

    def parse(self) -> dict:
        """
        Parse the JSON config file and return a dictionary
        :return: The dictionary containing the config data
        """
        with open(self.filepath, 'r') as file:
            data = json.load(file)
        return data