import time

from page_objects.base_page import BasePage
from page_objects.locators import CommonLocators


class CreateApplicationPage(BasePage):

    def fill_application(self):
        self.click(CommonLocators.span_with_text(text="Далее"))
        self.click(CommonLocators.span_with_text(text="Новый продукт"))
        self.click(CommonLocators.span_with_text(text="Создать заявку"))
        self.ac_drag_and_drop(CommonLocators.div_with_class_name(class_name="range_knob__button__1b8NM"))
        self.click(CommonLocators.span_with_text(text="Продолжить"))
        self.wait_visible_element(CommonLocators.div_with_text(text="Загрузите паспорта директора и бенефициаров"))
        self.scroll_page_down()
        self.click(CommonLocators.span_with_text(text="Продолжить"))
        time.sleep(2)
        self.scroll_page_down()
        ## pause for changing place of the button presented below
        self.click(CommonLocators.div_with_text(text="Загрузить с компьютера"))
        self.wait_visible_element(CommonLocators.div_with_text(text="Загруженные выписки"))
        self.scroll_page_down()
        self.click(CommonLocators.span_with_text(text="Получить решение"))
        self.wait_visible_element(
            CommonLocators.div_with_text(text="Возобновляемая кредитная линия предварительно одобрена"))
        self.scroll_page_down()
        self.click(CommonLocators.span_with_class_name(class_name="button_button__text__1Txl9"))
        self.click(CommonLocators.span_with_text(text="Выбрать время"))
        self.click(CommonLocators.button_with_text(text="10:00-11:30"))
        self.scroll_page_down()
        self.click(CommonLocators.span_with_text(text="Прикрепить"))
        self.wait_invisibility_element(CommonLocators.div_with_text("Верификация данных"))
        assert self.wait_element_present(CommonLocators.div_with_text("ВКЛ Активирована")), "Кредит не одобрен"
