from selenium.webdriver.common.by import By
from automation.framework.web.element import Element


class BookHotelPage:

    first_name_text = Element(By.ID, 'first_name')
    last_name_text = Element(By.ID, 'last_name')
    address_text = Element(By.ID, 'address')
    credit_card_number_text = Element(By.ID, 'cc_num')
    credit_card_type_select = Element(By.ID, 'cc_type')
    expiry_month_select = Element(By.ID, 'cc_exp_month')
    expiry_year_select = Element(By.ID, 'cc_exp_year')
    credit_card_cvv_text = Element(By.ID, 'cc_cvv')
    book_now_button = Element(By.ID, 'book_now')

    def book_hotel(self, first_name, last_name, address, credit_card_number, credit_card_type, cc_expiry_month, cc_expiry_year, credit_card_cvv):
        self.first_name_text.text = first_name
        self.last_name_text.text = last_name
        self.address_text.text = address
        self.credit_card_number_text.text = credit_card_number
        self.credit_card_type_select.text = credit_card_type
        self.expiry_month_select.text = cc_expiry_month
        self.expiry_year_select.text = cc_expiry_year
        self.credit_card_cvv_text.text = credit_card_cvv
        self.book_now_button.click()
