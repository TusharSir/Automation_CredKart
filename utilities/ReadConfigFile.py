import configparser

config = configparser.RawConfigParser()


config.read("D:\\Credence Python Projects by Tushar Sir\\Automation_Credkart\\Configuration\\Config.ini")

class ReadConfig():

    @staticmethod
    def getUsername():
        username = config.get('login data', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('login data', 'password')
        return password


