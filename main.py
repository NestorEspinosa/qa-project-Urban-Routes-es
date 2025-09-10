import data
import time
from methods import UrbanRoutesPage
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


'''
class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        #self.driver.find_element(*self.from_field).send_keys(from_address)
        field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.from_field)
        )
        field.send_keys(from_address)


    def set_to(self, to_address):
        #self.driver.find_element(*self.to_field).send_keys(to_address)
        field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.to_field)
        )
        field.send_keys(to_address)


    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self,from_address,to_address):
        self.set_from(from_address)
        self.set_to(to_address)
'''

class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        from selenium.webdriver.chrome.options import Options

        options = Options()
        options.set_capability("goog:loggingPrefs", {"performance": "ALL"})
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome(options=options)
        cls.urbanroutes = UrbanRoutesPage(cls.driver)

    #Test 1

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to

        routes_page.set_from(address_from)
        routes_page.set_to(address_to)

        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    #Test 2


    def test_select_comfort(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_taxi()
        routes_page.click_comfort()

        assert routes_page.get_active_tariff() == "Comfort"

    #Test 3

    def test_fill_number(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_number_button()
        number=data.phone_number
        routes_page.fill_number(number)
        routes_page.click_next_button()
        code=retrieve_phone_code(self.driver)
        routes_page.set_code(code)
        routes_page.click_confirm_button()
        assert routes_page.get_number_label()==number

    #Test 4

    def test_add_new_card(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_payment_button()
        routes_page.click_add_card_button()
        routes_page.set_card_number(data.card_number)
        routes_page.click_cvv_number()
        routes_page.set_cvv_number(data.card_code)
        routes_page.click_add_card()
        routes_page.click_close()
        assert routes_page.get_card_added()=="Tarjeta"

    #Test 5

    def test_add_message(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_message()
        message=data.message_for_driver
        routes_page.set_message(message)
        assert routes_page.get_message() == message

    #Test 6

    def test_add_blanket(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.select_blanket()
        assert routes_page.is_blanket_selected() == True

    #Test 7
    def test_add_ice(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.add_ice()
        routes_page.add_ice()
        assert routes_page.ice_value() == "2"

    #Test 8
    def test_order_taxi(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.order_taxi()
        assert routes_page.is_order_window_visible() == True

    #Test 9
    def test_get_driver(self):
        routes_page = UrbanRoutesPage(self.driver)

        assert routes_page.is_driver_info_visible() == True


    @classmethod
    def teardown_class(cls):
        time.sleep(5)
        cls.driver.quit()
