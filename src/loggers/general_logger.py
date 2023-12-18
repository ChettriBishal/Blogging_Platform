"""This module defines the general logger which will be used to logging across different files"""

import logging
from src.config.filepaths import APP_LOG_FILE

logging.basicConfig(
    format="%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
    datefmt="%d-%m-%Y %H:%M:%S",
    level=logging.DEBUG,
    filename=APP_LOG_FILE
)


class GeneralLogger:
    """
    Class contains various methods to set logs based on logging levels
    """
    logger = logging.getLogger("general_logger")

    @classmethod
    def set_file_handler(cls, file_name: str) -> None:
        """
        This sets the file handler after clearing the previous one
        """
        cls.logger.handlers.clear()

        formatter = logging.Formatter(
            "%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s"
        )

        file_handler = logging.FileHandler(file_name)
        file_handler.setFormatter(formatter)

        cls.logger.addHandler(file_handler)

    @classmethod
    def debug(cls, message: str, file_name: str) -> None:
        """
        This function allows `debug` logging level
        """
        cls.set_file_handler(file_name)

        cls.logger.debug(message)

    @classmethod
    def info(cls, message: str, file_name: str) -> None:
        """
        This function allows `info` logging level
        """
        cls.set_file_handler(file_name)

        cls.logger.info(message)

    @classmethod
    def warning(cls, message: str, file_name: str) -> None:
        """
        This function allows `warning` logging level
        """
        cls.set_file_handler(file_name)

        cls.logger.warning(message)

    @classmethod
    def error(cls, message: str, file_name: str) -> None:
        """
        This function allows `error` logging level
        """
        cls.set_file_handler(file_name)

        cls.logger.error(message)

    @classmethod
    def critical(cls, message: str, file_name: str) -> None:
        """
        This function allows `critical` logging level
        """
        cls.set_file_handler(file_name)

        cls.logger.critical(message)
