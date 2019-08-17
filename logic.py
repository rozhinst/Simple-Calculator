class Logic:

    def __init__(self, text):
        self.text = text
        self.operator = ''

    def click_button(self, number):
        self.operator = self.operator + str(number)
        self.text.set(self.operator)

    def equlbut(self):
        self.text.set(str(eval(self.operator)))
        self.operator = ''

    def clear_button(self):
        self.text.set("")
        self.operator = ''