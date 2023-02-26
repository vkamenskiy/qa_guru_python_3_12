from selene import have


class Radio:
    def __init__(self, elements):
        self.elements = elements

    def select(self, by_text: str):
        self.elements.element_by(have.value(by_text)).element('..').click()
        return self
