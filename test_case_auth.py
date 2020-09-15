
from .page import *

time.sleep(1)
def case_auth(self):
    self.page.loger('\n Запуск Тест кейс авторизация \n')

    self.page.login_matchtv(self, '9776410337', 'Alex92bykov')


    #def login(self):
#     time.sleep(3)
#     self.driver = webdriver.Chrome("C:\chromedriver\chromedriver.exe")
#     self.driver.find_element_by_xpath('.//button[@class="reset-button pm-gate__button"]').click()
#     time.sleep(3)
#     self.driver.find_element_by_xpath('.//button[@data-action="click->pm-auth#login"]').click()
#     time.sleep(3)
#     self.driver.find_element_by_xpath('.//input[@type="tel"]').send_keys('9776410337')
#     time.sleep(2)
#     self.driver.find_element_by_xpath('.//button[@type="submit"]').click()
#     time.sleep(2)
#     self.driver.find_element_by_xpath('.//input[@type="password"]').send_keys('Alekseybykov126')
#     time.sleep(3)
#     self.driver.find_element_by_xpath('.//button[@type="submit"]').click()
#     time.sleep(4)
#
#
# # def test_case_auth(self):
# #     return None
# def test_case_auth():
#     return None