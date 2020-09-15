from .page import * 

time.sleep(1)
def case_1_4(self, full_screen):

    self.page.loger('\n Запуск Тест кейс № 1_4 tvweb_new-1_4: Проверка перехода по разделам \n')
    #Эфир
    self.driver.find_element_by_xpath('.//li[@data-flexible-navigation-index="0"]').click()
    self.page.loger('Шаг 1 Клик по разделу Эфир')
    time.sleep(3)

    self.driver.waitForElementVisible('.//h1[@class="heading caption__heading"][contains(., "Прямой эфир")]')
    self.page.loger('Осуществлен переход в раздел Эфир')
    time.sleep(2)

    #ТОП-СОБЫТИЯ
    self.driver.find_element_by_xpath('.//li[@data-flexible-navigation-index="1"]').click()
    self.page.loger('Шаг 2 Клик по разделу ТОП-СОБЫТИЯ')
    time.sleep(3)

    self.driver.waitForElementVisible('.//a[@class="button-subscribe"][contains(., "Купить подписку")]')
    self.page.loger('Осуществлен переход в раздел ТОП-СОБЫТИЯ')
    time.sleep(2)

    #Телепрограмма
    self.driver.find_element_by_xpath('.//li[@data-flexible-navigation-index="2"]').click()
    self.page.loger('Шаг 3 Клик по разделу Телепрограмма')
    time.sleep(3)

    self.driver.waitForElementVisible('.//div[@class="block__title"][contains(., "Телепрограмма")]')
    self.page.loger('Осуществлен переход в раздел Телепрограмма')
    time.sleep(2)

    #Новости
    self.driver.find_element_by_xpath('.//li[@data-flexible-navigation-index="3"]').click()
    self.page.loger('Шаг 4 Клик по разделу Новости')
    time.sleep(3)

    self.driver.waitForElementVisible('.//h1[@class="styles__title--376FJ heading"][contains(., "Новости спорта")]')
    self.page.loger('Осуществлен переход в раздел Новости')
    time.sleep(2)

    #Трансляции
    self.driver.find_element_by_xpath('.//li[@data-flexible-navigation-index="4"]').click()
    self.page.loger('Шаг 5 Клик по разделу Трансляции')
    time.sleep(3)

    self.driver.waitForElementVisible('.//h1[@class="styles__title--2Us9-"][contains(., "Трансляции")]')
    self.page.loger('Осуществлен переход в раздел Трансляции')
    time.sleep(2)

    #Матч Премьер
    #main_window = self.driver.current_window_handle
    self.driver.find_element_by_xpath('.//li[@data-flexible-navigation-index="5"]').click()
    self.page.loger('Шаг 6 Клик по разделу Матч Премьер')
    time.sleep(3)
    self.driver.switch_to.window(self.driver.window_handles[1])

    self.driver.waitForElementVisible('.//div[@class="container-fluid topBlock"]')
    self.page.loger('Осуществлен переход в раздел Матч Премьер')


    self.driver.close()
    self.driver.switch_to.window(self.driver.window_handles[0])
    time.sleep(2)

    #видео
    self.driver.find_element_by_xpath('.//li[@data-flexible-navigation-index="6"]').click()
    self.page.loger('Шаг 7 Клик по разделу Видео')
    time.sleep(3)

    self.driver.waitForElementVisible('.//div[@class="container-fluid topBlock"]')
    self.page.loger('Осуществлен переход в раздел Видео')

    #передачи
    self.driver.find_element_by_xpath('.//li[@data-flexible-navigation-index="7"]').click()
    self.page.loger('Шаг 8 Клик по разделу передачи')
    time.sleep(3)

    self.driver.waitForElementVisible('.//h1[@class="styles__title--2Us9-"][contains(., "Телепередачи")]')
    self.page.loger('Осуществлен переход в раздел Передачи')

    # Матч! Cтрана
    self.driver.find_element_by_xpath('.//li[@data-flexible-navigation-index="8"]').click()
    self.page.loger('Шаг 9 Клик по разделу Матч! Cтрана')
    time.sleep(3)
    self.driver.switch_to.window(self.driver.window_handles[1])

    self.driver.waitForElementVisible('.//h1[@class="heading caption__heading"][contains(., "Матч! Cтрана")]')
    self.page.loger('Осуществлен переход в раздел Матч! Cтрана')
    time.sleep(1)

    self.driver.close()
    self.driver.switch_to.window(self.driver.window_handles[0])
    time.sleep(2)

    self.driver.quit()






    # emailt = 'ttvzavr126@mail.ru'
    # passw = '111111'
    #
    # summa = "1"
    # name = "Proxy Test"
    #
    # time.sleep(2)
    # self.page.click_f('Клик_Вход', 1)
    # time.sleep(1)
    # #self.page.send_f('Ввод_логина_вход', emailt, 2)
    # self.driver.find_element_by_xpath('.//input[@class="authorization__login textbox"]').send_keys(emailt)
    # time.sleep(2)
    #
    # #self.page.send_f('Ввод_пароля_вход', passw, 3)
    # self.driver.find_element_by_xpath('.//input[@class="authorization__password textbox"]').send_keys(passw)
    # time.sleep(2)
    #
    # self.page.click_f('Клик_Войти_auth', 4)
    # time.sleep(2)
    #
    # self.prof.click_f('Клик_значок_пользователя', 5)
    #
    # cash_1 = self.driver.find_element_by_xpath("//span[@class='__userbalance currency- currency currency-RUB']") # проверка личного счета до пополнения
    # cash_1 = cash_1.get_attribute('innerHTML')
    # self.page.loger('Счёт до пополнения: ' + cash_1)
    # cash_1 = int(cash_1)
    #
    # time.sleep(1)
    # self.prof.click_f('Клик_Личный_счет', 6)
    # time.sleep(1)
    #
    # self.prof.click_f('Клик_Пополнить', 7)
    # time.sleep(2)
    # self.page.send_f('Ввод_суммы_пополнения_счета', summa, 8)
    # time.sleep(2)
    # self.card.click_f('Клик_Оплатить_личный_счет', 9) # подразумевается, что карта для оплаты сохранена
    # time.sleep(15)  # время на прохождение оплаты
    # self.prof.click_f('Клик_значок_пользователя', 10)
    # time.sleep(1)
    #
    # cash_2 = self.driver.find_element_by_xpath("//span[@class='__userbalance currency- currency currency-RUB']") # проверка личного счета после пополнения
    # cash_2 = cash_2.get_attribute('innerHTML')
    # self.page.loger('Счёт после пополнения: ' + cash_2)
    # cash_2 = int(cash_2)
    #
    # if cash_1 < cash_2:
    #     self.page.loger('Счёт успешно пополнен!')
    # else:
    #     self.page.loger('Счёт не пополнен')
    #     assert()
    #
    # self.prof.click_f('Клик_Выйти', 11)
    # time.sleep(1)
    # self.driver.quit()