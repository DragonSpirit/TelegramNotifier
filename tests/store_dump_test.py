import unittest, pickle
from src.bot import dumpName, updateSubscribersDump

class TestStore(unittest.TestCase):

    #Тест, проверяющий работу хранилища подписчиков

    def test_store(self):
        test_data = set("123")
        updateSubscribersDump(test_data)
        subscribersList = open(dumpName, "rb")
        subscribers = pickle.load(subscribersList)
        subscribersList.close()
        self.assertEqual(subscribers, test_data)

if __name__ == '__main__':
    unittest.main()