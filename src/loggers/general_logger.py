import logging
from src.common.filepaths import APP_LOG_FILE

logging.basicConfig(
    format="%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
    datefmt="%d-%m-%Y %H:%M:%S",
    level=logging.DEBUG,
    filename= APP_LOG_FILE
)


class GeneralLogger:
    logger = logging.getLogger("general_logger")

    @classmethod
    def set_file_handler(cls, file_name):
        cls.logger.handlers.clear()

        formatter = logging.Formatter(
            "%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s"
        )

        file_handler = logging.FileHandler(file_name)
        file_handler.setFormatter(formatter)

        cls.logger.addHandler(file_handler)

    @classmethod
    def debug(cls, message, file_name):
        cls.set_file_handler(file_name)

        cls.logger.debug(message)

    @classmethod
    def info(cls, message, file_name):
        cls.set_file_handler(file_name)

        cls.logger.info(message)

    @classmethod
    def warning(cls, message, file_name):
        cls.set_file_handler(file_name)

        cls.logger.warning(message)

    @classmethod
    def error(cls, message, file_name):
        cls.set_file_handler(file_name)

        cls.logger.error(message)

    @classmethod
    def critical(cls, message, file_name):
        cls.set_file_handler(file_name)

        cls.logger.critical(message)
