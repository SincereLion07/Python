import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


valid_email = "gottin0705@gmail.com"
valid_password = "WnawC4SvdmiK56!"


# driver = webdriver.Chrome()
# driver.implicitly_wait(10)  # неявные ожидания
# implicitly_waits = driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody')  # неявные ожидания


@pytest.fixture(autouse=True)
def driver(headless):
    options = webdriver.ChromeOptions()
    options.headless = headless
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def url():
    url = "https://petfriends.skillfactory.ru/"
    if not url:
        raise Exception("Wrong environment")
    return url


def click():
    pass


def test_show_my_pets():
    # Вводим email
    driver.find_element(By.ID, 'email').send_keys(valid_email)
    # Вводим пароль
    driver.find_element(By.ID, 'pass').send_keys(valid_password)
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    driver.find_element(By.CLASS_NAME, 'navbar-toggler-icon').click()
    driver.find_element(By.XPATH, '//*[contains(text(),"Мои питомцы")]').click()
    try:
        explicit_waits = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, '//*[@id="all_my_pets"]')))  # явные ожидания
        assert explicit_waits == 'all_my_pets'
        print('Элемент найден')
    except TimeoutException:
        print('What???')
    finally:
        driver.quit()

    descriptions = driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody')
    images = driver.find_elements(By.XPATH, '//*[id="all_my_pets"]//img')
    names = driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]//body/tr/td[0]')
    statistics = driver.find_elements(By.XPATH, '//div[@class=".col-sm-4 left"]/text[1]')
    f = filter(str.isdecimal, statistics)
    statistics_2 = "".join(f)  # оставляем только число из текста

    for i in range(len(names)):
        assert statistics_2 == len(descriptions)  # Присутствуют все питомцы
        assert statistics_2 == len(images)  # Хотя бы у половины питомцев есть фото
        assert statistics_2 == len(names)  # У всех питомцев есть имя, возраст и порода


animals_names = ['laki', 'jopka']
unique = []


def test_get_unique_names():  # У всех питомцев разные имена
    for animals_names in unique:
        if animals_names in unique:
            continue
        else:
            unique.append(animals_names)
        return unique


print(test_get_unique_names())
