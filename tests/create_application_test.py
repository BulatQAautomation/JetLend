from page_objects.base_page import BasePage
from page_objects.create_application_page import CreateApplicationPage


class TestCreateApplicationPage:
    def test_create_application(
            self, browser, base_url
    ):
        base_page = BasePage(
            driver=browser,
            base_url=base_url
        )

        create_application_page = CreateApplicationPage(
            driver=browser,
            base_url=base_url
        )

        base_page.open()
        create_application_page.fill_application()
