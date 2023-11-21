from src.config import filepaths, prompts
from src.loggers.general_logger import GeneralLogger
from src.utils.initialisation import initialize
from src.views.home import Home

if __name__ == "__main__":
    GeneralLogger.info(prompts.SYSTEM_START, filepaths.SYSTEM_LOG_FILE)

    try:
        initialize()
        Home.home_menu()

    except Exception as exc:
        GeneralLogger.error(exc, filepaths.SYSTEM_LOG_FILE)

    finally:
        GeneralLogger.info(prompts.SYSTEM_EXIT, filepaths.SYSTEM_LOG_FILE)
