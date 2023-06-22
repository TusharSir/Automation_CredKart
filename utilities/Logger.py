import inspect
import logging


class LogGenerator:

    @staticmethod
    def loggen():
        name = inspect.stack()[1][3]
        logger = logging.getLogger(name)
        file = logging.FileHandler("D:\\Credence Python Projects by Tushar "
                                   "Sir\\Automation_Credkart\\Logs\\Automation_Cart.log")
        format = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(lineno)s : %(message)s")
        file.setFormatter(format)
        logger.addHandler(file)
        logger.setLevel(logging.INFO)
        return logger


