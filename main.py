from src.services import home
from src.common import filepaths, prompts
from src.loggers.general_logger import GeneralLogger
from src.utils.initialisation import initialize

if __name__ == "__main__":
    GeneralLogger.info(prompts.SYSTEM_START, filepaths.SYSTEM_LOG_FILE)

    try:
        initialize()
        home.home_menu()

    except Exception as exc:
        GeneralLogger.error(exc, filepaths.SYSTEM_LOG_FILE)

    finally:
        GeneralLogger.info(prompts.SYSTEM_EXIT, filepaths.SYSTEM_LOG_FILE)
