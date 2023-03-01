import time
import unittest

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import Key


class Chrome(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("D:/webdriver/chromedriver.exe")
        self.driver = driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()

    # As per unittest module, individual test should start with test_
    def test_TelAviv_chrome(self):
        driver: WebDriver = self.driver
        driver.get(Key.keyNew) #my key
        time.sleep(0.1)
        wait = WebDriverWait(driver, 0.1)

        #WebDriverWait(driver, 3).until(
            #EC.visibility_of_element_located((By.XPATH, "//a[@href='https://doska.orbita.co.il/my/']")))
        #print("Ok")

        time.sleep(0.1)
        driver.get('https://doska.orbita.co.il/my/add/')
        time.sleep(0.1)
        driver.find_element(By.XPATH, "//select[@name='board']/option[@value='11']").click()

        time.sleep(0.1)
        driver.find_element(By.XPATH, "//option[@value='c81']").click()  # city c81-T-A, c10 Bat-Jam, c23-Herzlia,
        time.sleep(0.1)  # c24-Givataim, c88-Holon,c76-Rishon Le Cion, c70-Petah Tikva, c72-Ramat Gan
        driver.find_element(By.XPATH, "//textarea[@class='form-control input-sm']").clear()
        driver.find_element(By.XPATH, "//textarea[@class='form-control input-sm']"). \
            send_keys("РЕМОНТ и НАСТРОЙКА КОМПЬЮТЕРОВ и НОУТБУКОВ у вас дома или в офисе:\n"
                      "- Установка программ\n- Подключение принтеров\n- Диагностика и лечение вирусов\n"
                      "- Возможна работа по удаленному доступу\n- Услуги сетевого администратора\n"
                      "- Стаж более 20 лет работы с компьютерами\n- Консультации бесплатно\n"
                      "\n \n тел. 053 5964792 Дмитрий\n")
        time.sleep(0.1)

        driver.find_element(By.XPATH, "//input[@name='photo[]']").send_keys("D://HOMEWORK_QA/2.jpg")
        time.sleep(0.1)
        driver.find_element(By.XPATH, "//div[2]/div[2]/input").send_keys("D://HOMEWORK_QA/1.jpeg")

        time.sleep(0.1)
        driver.find_element(By.XPATH, "//option[@value='90']").click()
        driver.find_element(By.NAME, "phonenum").send_keys("5964792")
        driver.find_element(By.NAME, "terms").click()
        time.sleep(0.1)

        driver.find_element(By.XPATH, "//input[@value='Добавить объявление']").submit()
        time.sleep(300)

    def test_RamatGan_chrome(self):
        driver: WebDriver = self.driver
        driver.get(Key.keyNew)  #MY KEY!!!
        time.sleep(0.1)
        wait = WebDriverWait(driver, 0.1)

        #WebDriverWait(driver, 3).until(
            #EC.visibility_of_element_located((By.XPATH, "//a[@href='https://doska.orbita.co.il/my/']")))
        #print("Ok")

        time.sleep(0.1)
        driver.get('https://doska.orbita.co.il/my/add/')
        time.sleep(0.1)
        driver.find_element(By.XPATH, "//select[@name='board']/option[@value='11']").click()

        time.sleep(0.1)
        driver.find_element(By.XPATH, "//option[@value='c72']").click()  # city c81-T-A, c10 Bat-Jam, c23-Herzlia,
        time.sleep(0.1)  # c24-Givataim, c88-Holon,c76-Rishon Le Cion, c70-Petah Tikva, c72-Ramat Gan
        driver.find_element(By.XPATH, "//textarea[@class='form-control input-sm']").clear()
        driver.find_element(By.XPATH, "//textarea[@class='form-control input-sm']"). \
            send_keys("РЕМОНТ и НАСТРОЙКА КОМПЬЮТЕРОВ и НОУТБУКОВ у вас дома или в офисе:\n"
                      "- Установка программ\n- Подключение принтеров\n- Диагностика и лечение вирусов\n"
                      "- Возможна работа по удаленному доступу\n- Услуги сетевого администратора\n"
                      "- Стаж более 20 лет работы с компьютерами\n- Консультации бесплатно\n"
                      "\n \n тел. 053 5964792 Дмитрий\n")
        time.sleep(0.1)

        driver.find_element(By.XPATH, "//input[@name='photo[]']").send_keys("D://HOMEWORK_QA/2.jpg")
        time.sleep(0.1)
        driver.find_element(By.XPATH, "//div[2]/div[2]/input").send_keys("D://HOMEWORK_QA/1.jpeg")

        time.sleep(0.1)
        driver.find_element(By.XPATH, "//option[@value='90']").click()
        driver.find_element(By.NAME, "phonenum").send_keys("5964792")
        driver.find_element(By.NAME, "terms").click()
        time.sleep(0.1)

        driver.find_element(By.XPATH, "//input[@value='Добавить объявление']").submit()
        time.sleep(300)

    def test_BatJam_chrome(self):
        driver: WebDriver = self.driver
        driver.get(Key.keyNew) #My key!!
        time.sleep(0.1)
        wait = WebDriverWait(driver, 0.1)

        wait.until(
            EC.visibility_of_element_located((By.XPATH, "//a[@href='https://doska.orbita.co.il/my/']")))
        print("Ok")

        time.sleep(0.1)
        driver.get('https://doska.orbita.co.il/my/add/')
        time.sleep(0.1)
        driver.find_element(By.XPATH, "//select[@name='board']/option[@value='11']").click()

        time.sleep(0.1)
        driver.find_element(By.XPATH, "//option[@value='c10']").click()  # city c81-T-A, c10 Bat-Jam, c23-Herzlia,
        time.sleep(0.1)  # c24-Givataim, c88-Holon,c76-Rishon Le Cion, c70-Petah Tikva, c72-Ramat Gan
        driver.find_element(By.XPATH, "//textarea[@class='form-control input-sm']").clear()
        driver.find_element(By.XPATH, "//textarea[@class='form-control input-sm']"). \
            send_keys("РЕМОНТ и НАСТРОЙКА КОМПЬЮТЕРОВ и НОУТБУКОВ у вас дома или в офисе:\n"
                      "- Установка программ\n- Подключение принтеров\n- Диагностика и лечение вирусов\n"
                      "- Возможна работа по удаленному доступу\n- Услуги сетевого администратора\n"
                      "- Стаж более 20 лет работы с компьютерами\n- Консультации бесплатно\n"
                      "\n \n тел. 053 5964792 Дмитрий\n")
        time.sleep(0.1)

        driver.find_element(By.XPATH, "//input[@name='photo[]']").send_keys("D://HOMEWORK_QA/2.jpg")
        time.sleep(0.1)
        driver.find_element(By.XPATH, "//div[2]/div[2]/input").send_keys("D://HOMEWORK_QA/1.jpeg")

        time.sleep(0.1)
        driver.find_element(By.XPATH, "//option[@value='90']").click()
        driver.find_element(By.NAME, "phonenum").send_keys("5964792")
        driver.find_element(By.NAME, "terms").click()
        time.sleep(0.1)

        driver.find_element(By.XPATH, "//input[@value='Добавить объявление']").submit()
        time.sleep(300)

    def test_Holon_chrome(self):
        driver: WebDriver = self.driver
        driver.get(Key.keyNew) #My Key!
        time.sleep(0.1)
        wait = WebDriverWait(driver, 0.1)

        wait.until(
            EC.visibility_of_element_located((By.XPATH, "//a[@href='https://doska.orbita.co.il/my/']")))
        print("Ok")

        time.sleep(0.1)
        driver.get('https://doska.orbita.co.il/my/add/')
        time.sleep(0.1)
        driver.find_element(By.XPATH, "//select[@name='board']/option[@value='11']").click()

        time.sleep(0.1)
        driver.find_element(By.XPATH, "//option[@value='c88']").click()  # city c81-T-A, c10 Bat-Jam, c23-Herzlia,
        time.sleep(0.1)  # c24-Givataim, c88-Holon,c76-Rishon Le Cion, c70-Petah Tikva, c72-Ramat Gan
        driver.find_element(By.XPATH, "//textarea[@class='form-control input-sm']").clear()
        driver.find_element(By.XPATH, "//textarea[@class='form-control input-sm']"). \
            send_keys("РЕМОНТ и НАСТРОЙКА КОМПЬЮТЕРОВ и НОУТБУКОВ у вас дома или в офисе:\n"
                      "- Установка программ\n- Подключение принтеров\n- Диагностика и лечение вирусов\n"
                      "- Возможна работа по удаленному доступу\n- Услуги сетевого администратора\n"
                      "- Стаж более 20 лет работы с компьютерами\n- Консультации бесплатно\n"
                      "\n \n тел. 053 5964792 Дмитрий\n")
        time.sleep(0.1)

        driver.find_element(By.XPATH, "//input[@name='photo[]']").send_keys("D://HOMEWORK_QA/2.jpg")
        time.sleep(0.1)
        driver.find_element(By.XPATH, "//div[2]/div[2]/input").send_keys("D://HOMEWORK_QA/1.jpeg")

        time.sleep(0.1)
        driver.find_element(By.XPATH, "//option[@value='90']").click()
        driver.find_element(By.NAME, "phonenum").send_keys("5964792")
        driver.find_element(By.NAME, "terms").click()
        time.sleep(0.1)

        driver.find_element(By.XPATH, "//input[@value='Добавить объявление']").submit()
        time.sleep(300)

    def test_RishonLeTsiyon_chrome(self):
        driver: WebDriver = self.driver
        driver.get(Key.keyNew) #my key
        time.sleep(0.5)
        wait = WebDriverWait(driver, 0.1)

        #WebDriverWait(driver, 3).until(
            #EC.visibility_of_element_located((By.XPATH, "//a[@href='https://doska.orbita.co.il/my/']")))
        #print("Ok")

        time.sleep(0.5)
        driver.get('https://doska.orbita.co.il/my/add/')
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//select[@name='board']/option[@value='11']").click()

        time.sleep(0.5)
        driver.find_element(By.XPATH, "//option[@value='c76']").click()  # city c81-T-A, c10 Bat-Jam, c23-Herzlia,
        time.sleep(0.5)  # c24-Givataim, c88-Holon,c76-Rishon Le Cion, c70-Petah Tikva, c72-Ramat Gan
        driver.find_element(By.XPATH, "//textarea[@class='form-control input-sm']").clear()
        driver.find_element(By.XPATH, "//textarea[@class='form-control input-sm']"). \
            send_keys("РЕМОНТ и НАСТРОЙКА КОМПЬЮТЕРОВ и НОУТБУКОВ у вас дома или в офисе:\n"
                      "- Установка программ\n- Подключение принтеров\n- Диагностика и лечение вирусов\n"
                      "- Возможна работа по удаленному доступу\n- Услуги сетевого администратора\n"
                      "- Стаж более 20 лет работы с компьютерами\n- Консультации бесплатно\n"
                      "\n \n тел. 053 5964792 Дмитрий\n")
        time.sleep(0.5)

        driver.find_element(By.XPATH, "//input[@name='photo[]']").send_keys("D://HOMEWORK_QA/2.jpg")
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//div[2]/div[2]/input").send_keys("D://HOMEWORK_QA/1.jpeg")

        time.sleep(0.5)
        driver.find_element(By.XPATH, "//option[@value='90']").click()
        driver.find_element(By.NAME, "phonenum").send_keys("5964792")
        driver.find_element(By.NAME, "terms").click()
        time.sleep(0.5)

        driver.find_element(By.XPATH, "//input[@value='Добавить объявление']").submit()
        time.sleep(300)

    def test_Givataim_chrome(self):
        driver: WebDriver = self.driver
        driver.get(Key.keyNew) #My KEY!!
        time.sleep(0.1)
        wait = WebDriverWait(driver, 0.1)

        WebDriverWait(driver, 0.1).until(
            EC.visibility_of_element_located((By.XPATH, "//a[@href='https://doska.orbita.co.il/my/']")))
        print("Ok")

        time.sleep(0.1)
        driver.get('https://doska.orbita.co.il/my/add/')
        time.sleep(0.1)
        driver.find_element(By.XPATH, "//select[@name='board']/option[@value='11']").click()

        time.sleep(0.1)
        driver.find_element(By.XPATH, "//option[@value='c24']").click()  # city c81-T-A, c10 Bat-Jam, c23-Herzlia,
        time.sleep(0.1)  # c24-Givataim, c88-Holon,c76-Rishon Le Cion, c70-Petah Tikva, c72-Ramat Gan
        driver.find_element(By.XPATH, "//textarea[@class='form-control input-sm']").clear()
        driver.find_element(By.XPATH, "//textarea[@class='form-control input-sm']"). \
            send_keys("РЕМОНТ и НАСТРОЙКА КОМПЬЮТЕРОВ и НОУТБУКОВ у вас дома или в офисе:\n"
                      "- Установка программ\n- Подключение принтеров\n- Диагностика и лечение вирусов\n"
                      "- Возможна работа по удаленному доступу\n- Услуги сетевого администратора\n"
                      "- Стаж более 20 лет работы с компьютерами\n- Консультации бесплатно\n"
                      "\n \n тел. 053 5964792 Дмитрий\n")
        time.sleep(0.1)

        driver.find_element(By.XPATH, "//input[@name='photo[]']").send_keys("D://HOMEWORK_QA/2.jpg")
        time.sleep(0.1)
        driver.find_element(By.XPATH, "//div[2]/div[2]/input").send_keys("D://HOMEWORK_QA/1.jpeg")

        time.sleep(0.1)
        driver.find_element(By.XPATH, "//option[@value='90']").click()
        driver.find_element(By.NAME, "phonenum").send_keys("5964792")
        driver.find_element(By.NAME, "terms").click()
        time.sleep(0.1)

        driver.find_element(By.XPATH, "//input[@value='Добавить объявление']").submit()
        time.sleep(300)

    def test_Herzliya_chrome(self):
        driver: WebDriver = self.driver
        driver.get(Key.keyNew) #My key
        time.sleep(0.1)
        wait = WebDriverWait(driver, 0.1)

        WebDriverWait(driver, 0.1).until(
            EC.visibility_of_element_located((By.XPATH, "//a[@href='https://doska.orbita.co.il/my/']")))
        print("Ok")

        time.sleep(0.1)
        driver.get('https://doska.orbita.co.il/my/add/')
        time.sleep(0.1)
        driver.find_element(By.XPATH, "//select[@name='board']/option[@value='11']").click()

        time.sleep(0.1)
        driver.find_element(By.XPATH, "//option[@value='c23']").click()  # city c81-T-A, c10 Bat-Jam, c23-Herzlia,
        time.sleep(0.1)  # c24-Givataim, c88-Holon,c76-Rishon Le Cion, c70-Petah Tikva, c72-Ramat Gan
        driver.find_element(By.XPATH, "//textarea[@class='form-control input-sm']").clear()
        driver.find_element(By.XPATH, "//textarea[@class='form-control input-sm']"). \
            send_keys("РЕМОНТ и НАСТРОЙКА КОМПЬЮТЕРОВ и НОУТБУКОВ у вас дома или в офисе:\n"
                      "- Установка программ\n- Подключение принтеров\n- Диагностика и лечение вирусов\n"
                      "- Возможна работа по удаленному доступу\n- Услуги сетевого администратора\n"
                      "- Стаж более 20 лет работы с компьютерами\n- Консультации бесплатно\n"
                      "\n \n тел. 053 5964792 Дмитрий\n")
        time.sleep(0.1)

        driver.find_element(By.XPATH, "//input[@name='photo[]']").send_keys("D://HOMEWORK_QA/2.jpg")
        time.sleep(0.1)
        driver.find_element(By.XPATH, "//div[2]/div[2]/input").send_keys("D://HOMEWORK_QA/1.jpeg")

        time.sleep(0.1)
        driver.find_element(By.XPATH, "//option[@value='90']").click()
        driver.find_element(By.NAME, "phonenum").send_keys("5964792")
        driver.find_element(By.NAME, "terms").click()
        time.sleep(0.1)

        driver.find_element(By.XPATH, "//input[@value='Добавить объявление']").submit()
        time.sleep(300)

    def test_GaneiTikva_chrome(self):
        driver: WebDriver = self.driver
        driver.get(Key.keyNew) #My key
        time.sleep(0.1)
        wait = WebDriverWait(driver, 0.1)

        WebDriverWait(driver, 0.1).until(
            EC.visibility_of_element_located((By.XPATH, "//a[@href='https://doska.orbita.co.il/my/']")))
        print("Ok")

        time.sleep(0.1)
        driver.get('https://doska.orbita.co.il/my/add/')
        time.sleep(0.1)
        driver.find_element(By.XPATH, "//select[@name='board']/option[@value='11']").click()

        time.sleep(0.1)
        driver.find_element(By.XPATH, "//option[@value='c22']").click()  # city c81-T-A, c10 Bat-Jam, c23-Herzlia,
        time.sleep(0.1)  # c24-Givataim, c88-Holon,c76-Rishon Le Cion, c70-Petah Tikva, c72-Ramat Gan
        driver.find_element(By.XPATH, "//textarea[@class='form-control input-sm']").clear()
        driver.find_element(By.XPATH, "//textarea[@class='form-control input-sm']"). \
            send_keys("РЕМОНТ и НАСТРОЙКА КОМПЬЮТЕРОВ и НОУТБУКОВ у вас дома или в офисе:\n"
                      "- Установка программ\n- Подключение принтеров\n- Диагностика и лечение вирусов\n"
                      "- Возможна работа по удаленному доступу\n- Услуги сетевого администратора\n"
                      "- Стаж более 20 лет работы с компьютерами\n- Консультации бесплатно\n"
                      "\n \n тел. 053 5964792 Дмитрий\n")
        time.sleep(0.1)

        driver.find_element(By.XPATH, "//input[@name='photo[]']").send_keys("D://HOMEWORK_QA/2.jpg")
        time.sleep(0.1)
        driver.find_element(By.XPATH, "//div[2]/div[2]/input").send_keys("D://HOMEWORK_QA/1.jpeg")

        time.sleep(0.1)
        driver.find_element(By.XPATH, "//option[@value='90']").click()
        driver.find_element(By.NAME, "phonenum").send_keys("5964792")
        driver.find_element(By.NAME, "terms").click()
        time.sleep(0.1)

        driver.find_element(By.XPATH, "//input[@value='Добавить объявление']").submit()
        time.sleep(300)

    def test_chrome_1120x550(self):
        driver = self.driver
        driver.set_window_size(1120, 550)
        # driver: WebDriver = self.driver
        driver.get(Key.keyNew) #My key
        time.sleep(3)
        wait = WebDriverWait(driver, 3)

        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located((By.XPATH, "//a[@href='https://doska.orbita.co.il/my/']")))
        print("Ok")

        time.sleep(3)
        driver.get('https://doska.orbita.co.il/my/add/')
        time.sleep(3)
        driver.find_element(By.XPATH, "//select[@name='board']/option[@value='11']").click()

        time.sleep(3)
        driver.find_element(By.XPATH, "//option[@value='c70']").click()  # city c81-T-A, c10 Bat-Jam, c23-Herzlia,
        time.sleep(3)  # c24-Givataim, c88-Holon,c76-Rishon Le Cion, c70-Petah Tikva, c72-Ramat Gan
        driver.find_element(By.XPATH, "//textarea[@class='form-control input-sm']").clear()
        driver.find_element(By.XPATH, "//textarea[@class='form-control input-sm']"). \
            send_keys("РЕМОНТ и НАСТРОЙКА КОМПЬЮТЕРОВ и НОУТБУКОВ у вас дома или в офисе:\n"
                      "- Установка программ\n- Подключение принтеров\n- Диагностика и лечение вирусов\n"
                      "- Возможна работа по удаленному доступу\n- Услуги сетевого администратора\n"
                      "- Стаж более 20 лет работы с компьютерами\n- Консультации бесплатно\n"
                      "\n \n тел. 053 5964792 Дмитрий\n")
        time.sleep(3)

        driver.find_element(By.XPATH, "//input[@name='photo[]']").send_keys("D://HOMEWORK_QA/2.jpg")
        time.sleep(3)
        driver.find_element(By.XPATH, "//div[2]/div[2]/input").send_keys("D://HOMEWORK_QA/1.jpeg")

        time.sleep(3)
        driver.find_element(By.XPATH, "//option[@value='90']").click()
        driver.find_element(By.NAME, "phonenum").send_keys("5964792")
        driver.find_element(By.NAME, "terms").click()
        time.sleep(3)

        driver.find_element(By.XPATH, "//input[@value='Добавить объявление']").submit()
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()


class Firefox(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.maximize_window()

    # As per unittest module, individual test should start with test_
    def test_firefox_1250_850(self):
        driver = self.driver
        driver.set_window_size(1250, 850)
        driver.get(Key.keyNew) #My key
        time.sleep(3)
        wait = WebDriverWait(driver, 3)

        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located((By.XPATH, "//a[@href='https://doska.orbita.co.il/my/']")))
        print("Ok")

        time.sleep(3)
        driver.get('https://doska.orbita.co.il/my/add/')
        time.sleep(3)
        driver.find_element(By.XPATH, "//select[@name='board']/option[@value='11']").click()

        time.sleep(3)
        driver.find_element(By.XPATH, "//option[@value='c76']").click()  # city c81-T-A, c10 Bat-Jam, c23-Herzlia,
        time.sleep(3)  # c24-Givataim, c88-Holon,c76-Rishon Le Cion, c70-Petah Tikva, c72-Ramat Gan
        driver.find_element(By.XPATH, "//textarea[@class='form-control input-sm']").clear()
        driver.find_element(By.XPATH, "//textarea[@class='form-control input-sm']"). \
            send_keys("РЕМОНТ и НАСТРОЙКА КОМПЬЮТЕРОВ и НОУТБУКОВ у вас дома или в офисе:\n"
                      "- Установка программ\n- Подключение принтеров\n- Диагностика и лечение вирусов\n"
                      "- Возможна работа по удаленному доступу\n- Услуги сетевого администратора\n"
                      "- Стаж более 20 лет работы с компьютерами\n- Консультации бесплатно\n"
                      "\n \n тел. 053 5964792 Дмитрий\n")
        time.sleep(3)

        driver.find_element(By.XPATH, "//input[@name='photo[]']").send_keys("D://HOMEWORK_QA/2.jpg")
        time.sleep(3)
        driver.find_element(By.XPATH, "//div[2]/div[2]/input").send_keys("D://HOMEWORK_QA/1.jpeg")

        time.sleep(3)
        driver.find_element(By.XPATH, "//option[@value='90']").click()
        driver.find_element(By.NAME, "phonenum").send_keys("5964792")
        driver.find_element(By.NAME, "terms").click()
        time.sleep(3)

        driver.find_element(By.XPATH, "//input[@value='Добавить объявление']").submit()
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()
