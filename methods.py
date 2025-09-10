from locators import UrbanRoutesLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import Keys


class UrbanRoutesPage:

    def __init__(self, driver):
        self.driver = driver
        self.locators = UrbanRoutesLocators()

    #Métodos prueba 1

    def set_from(self, from_address):
        #self.driver.find_element(*self.from_field).send_keys(from_address)
        field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locators.from_field)
        )
        field.send_keys(from_address)


    def set_to(self, to_address):
        #self.driver.find_element(*self.to_field).send_keys(to_address)
        field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locators.to_field)
        )
        field.send_keys(to_address)


    def get_from(self):
        return self.driver.find_element(*self.locators.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.locators.to_field).get_property('value')

    # Métodos prueba 2

    def click_taxi(self):
        field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locators.take_taxi)
        )
        field.click()

    def click_comfort(self):
        field = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(self.locators.comfort)
        )
        # Scroll hasta el botón
        self.driver.execute_script("arguments[0].scrollIntoView(true);", field)
        # Espera que sea clickable después de hacer scroll
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.locators.comfort)
        ).click()

    def get_active_tariff(self):
        # Obtener el texto de la tarifa activa
        return self.driver.find_element(*self.locators.active_tariff).text

    # Métodos prueba 3

    def click_number_button(self):
        field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locators.number_button)
        )
        field.click()

    def fill_number(self,number):
        field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locators.fill_number)
        )
        # Espera que sea clickable después de hacer scroll
        #WebDriverWait(self.driver, 5).until(
            #EC.element_to_be_clickable(self.locators.fill_number)
        #)
        field.send_keys(number)

    def click_next_button(self):
        field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locators.next_button)
        )
        field.click()

    def set_code(self,code):
        field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locators.code_number)
        )
        field.send_keys(code)

    def click_confirm_button(self):
        field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locators.confirm_button)
        )
        field.click()

    def get_number_label(self):
        return self.driver.find_element(*self.locators.number_label).text


    # Métodos prueba 4


    def click_payment_button(self):
        field = WebDriverWait(self.driver, 15).until(
        EC.presence_of_element_located(self.locators.add_payment_button)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", field)
        WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable(self.locators.add_payment_button)
         ).click()

    def click_add_card_button(self):
        field = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(self.locators.add_card)
        )
        field.click()

    def set_card_number(self, card_number):
         field = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.locators.card_number))
         field.send_keys(card_number)

    def click_cvv_number(self):
        field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.locators.cvv)
        )
        field.click()

    def set_cvv_number(self, cvv):
         field = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.locators.cvv))
         field.send_keys(cvv)
         field.send_keys(Keys.TAB)

    def click_close(self):
        field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.locators.close_payment)
        )
        field.click()

    def click_add_card(self):
        field = WebDriverWait(self.driver, 10).until(
             EC.element_to_be_clickable(self.locators.add_button)  # <-- Espera a que el botón sea clickeable
           )
        field.click()

    def get_card_added(self):
        return self.driver.find_element(*self.locators.card_added).text


    # Métodos prueba 5

    def click_message(self):
        field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.locators.message)
        )
        # Use JavaScript to click the element directly
        self.driver.execute_script("arguments[0].click();", field)

    def set_message(self, messages):
         field = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.locators.message))
         field.send_keys(messages)


    def get_message(self):
        return self.driver.find_element(*self.locators.message).get_attribute("value")

    # Métodos prueba 6

    def select_blanket(self):
        checkbox = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locators.blanket_checkbox)
        )
        header = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locators.header_blanket)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", header)
        self.driver.execute_script("arguments[0].click();", checkbox)

    def is_blanket_selected(self):
        #Verifica si el checkbox de Manta y pañuelos está seleccionado.
        checkbox = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locators.blanket_checkbox)
        )
        return checkbox.is_selected()

    # Métodos prueba 7

    def add_ice(self):
        field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locators.add_ice)
        )
        header = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locators.header_ice_bucket)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", header)
        field.click()

    def ice_value(self):
        return self.driver.find_element(*self.locators.ice_value).text


    # Métodos prueba 8

    def order_taxi(self):
        field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locators.order_taxi)
        )
        field.click()

    def is_order_window_visible(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.locators.order_body)
            )
            return True
        except:
            return False

    # Métodos prueba 9

    def is_driver_info_visible(self):
        #Verifica que el título de la orden ha cambiado y que la información del conductor es visible.

        try:
            # Espera a que el título cambie del texto 'Buscar automóvil'
            WebDriverWait(self.driver, 50).until_not(
                EC.text_to_be_present_in_element(self.locators.order_header_title, 'Buscar automóvil')
            )
            # Espera a que el elemento con el número de orden sea visible
            WebDriverWait(self.driver, 50).until(
                EC.visibility_of_element_located(self.locators.order_number)
            )
            return True
        except:
            return False