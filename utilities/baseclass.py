import inspect
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest


@pytest.mark.usefixtures("setup")
class Baseclass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger

    # def wait_element(self, ele):
    #     WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID,'ele'))
