class CommonLocators:

    @staticmethod
    def span_with_text(text):
        return {'xpath': f'//span[text() = "{text}"]'}

    @staticmethod
    def div_with_text(text):
        return {'xpath': f'//div[text() = "{text}"]'}

    @staticmethod
    def span_with_class_name(class_name):
        return {'xpath': f'//span[@class = "{class_name}"]'}

    @staticmethod
    def div_with_class_name(class_name):
        return {'xpath': f'//div[@class = "{class_name}"]'}

    @staticmethod
    def button_with_text(text):
        return {'xpath': f'//button[text() = "{text}"]'}