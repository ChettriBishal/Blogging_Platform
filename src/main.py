from config import filepaths, prompts
from loggers.general_logger import GeneralLogger
from utils.initialisation import initialize
from views.home import Home
from models.db_connection import DBConnection

if __name__ == "__main__":
    GeneralLogger.info(prompts.SYSTEM_START, filepaths.SYSTEM_LOG_FILE)

    try:
        initialize()
        Home.home_menu()

    except Exception as exc:
        GeneralLogger.error(exc, filepaths.SYSTEM_LOG_FILE)

    finally:
        GeneralLogger.info(prompts.SYSTEM_EXIT, filepaths.SYSTEM_LOG_FILE)
        DBConnection().close()
