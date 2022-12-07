from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException, \
    ElementClickInterceptedException
from selenium.webdriver import ActionChains


def make_screenshot_on_error(f):
    def wrapper(self, *args, **kwargs):
        try:
            return f(self, *args, **kwargs)
        except (TimeoutException, IndexError, AssertionError, NoSuchElementException,
                StaleElementReferenceException, ElementClickInterceptedException) as err:
            print(f'\nОшибка {err}, создан скриншот')
            print(f'Вызываемый метод {f.__name__}, параметры позиционные {args}, именованные {kwargs}')
            self.driver.save_screenshot("{}.png".format(self.driver.session_id))
            raise err

    return wrapper


class BasePage:
    def __init__(self, driver=None, base_url=None, session=None):
        self.driver = driver
        self.base_url = base_url
        self.session = session

    def open(self):
        self.driver.get(self.base_url)

    def element(self, selector: dict, index: int):
        by = None
        if 'xpath' in selector.keys():
            by = By.XPATH
            selector = selector['xpath']
        return self.driver.find_elements(by, selector)[index]

    @make_screenshot_on_error
    def click(self, selector: dict, index=0):
        self.wait_for_clickable(selector, wait=20)
        self.wait_visible_element(selector, wait=20)
        self.element(selector, index).click()

    @make_screenshot_on_error
    def click_ac(self, selector, index=0):
        ActionChains(self.driver).move_to_element(self.element(selector, index)).click().perform()

    @make_screenshot_on_error
    def ac_drag_and_drop(self, selector: dict, index=0):
        draggable = self.element(selector, index)
        ActionChains(self.driver).drag_and_drop_by_offset(draggable, 100, 0).perform()

    @make_screenshot_on_error
    def wait_for_clickable(self, selector, wait=15):
        by = None
        if 'xpath' in selector.keys():
            by = By.XPATH
            selector = selector['xpath']
        WebDriverWait(self.driver, wait).until(EC.element_to_be_clickable((by, selector)))

    @make_screenshot_on_error
    def wait_visible_element(self, selector, wait=15):
        by = None
        if 'xpath' in selector.keys():
            by = By.XPATH
            selector = selector['xpath']
        WebDriverWait(self.driver, wait).until(EC.visibility_of_element_located((by, selector)))

    def scroll_page_down(self):
        self.driver.execute_script("window.scrollTo(100000, 100000);")
