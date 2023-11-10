import logging

class AutomationTestLogging:
    def __init__(self):
        self.logger = logging.getLogger("mobile_automation_test_logging")
        log_handler = logging.StreamHandler()
        log_handler.setFormatter(
            logging.Formatter(
                fmt="%(asctime)s : %(filename)s : %(funcName)s : %(message)s",
                datefmt="%d-%m-%Y %I:%M:%S",
            )
        )
        self.logger.addHandler(log_handler)
        self.logger.setLevel(logging.INFO)
        self.logger.propagate = False
