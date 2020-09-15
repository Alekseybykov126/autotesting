from .page import *

time.sleep(1)
def case_1_3(self, full_screen):

    self.page.loger('\n Запуск Тест кейс № 1_3 tvweb_new-1_3: Проверка наличия коэффициентов фонбет на главной \n')
    time.sleep(2)

    self.driver.find_element_by_xpath('.//button[@class="reset-button cookie-notice__button"]').click()
    time.sleep(2)

    num_koef = len(self.driver.find_elements_by_xpath('.//div[@class="fonbet_koef"]'))
    print('Количество коэффициентов ' + str(num_koef))

    if num_koef < 2:
        assert False
        self.page.loger('Коэффициентов слишком мало, меньше 2')

    target = self.driver.find_element_by_xpath('.//h2[@class="heading caption__heading"][contains (., "Новости")]')  # скролл до плеера прямой эфир
    target.location_once_scrolled_into_view  # скролл
    time.sleep(3)

    num_koef2 = len(self.driver.find_elements_by_xpath('.//div[@class="news-item__title"]'))
    print('Количество новостей ' + str(num_koef2))

    b = random.randint(0, (num_koef2 - 1)) #возможно надо минус 1, т.к. начинает с нуля
    print(b)

    #res_txt = str(self.result.find_link("li", "news-feed__item")[b].text)  # название фильма

    res_txt = str(self.driver.find_elements_by_xpath('.//li[@class="news-feed__item"]')[b].text)
    self.page.loger('Заголовок Новости: ' + res_txt.strip())
    time.sleep(2)

    self.driver.find_elements_by_xpath('.//div[@class="news-item__title"]')[b].click()
    time.sleep(3)

    resic = str(self.result.find_link("h1", "headline name"))
    time.sleep(1)
    assert (resic) in res_txt
