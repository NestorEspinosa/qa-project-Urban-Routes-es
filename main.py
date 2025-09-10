import data
import time
from methods import UrbanRoutesPage
from selenium import webdriver



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
        cls.routes_page = UrbanRoutesPage(cls.driver)

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
        self.routes_page.click_taxi()
        self.routes_page.click_comfort()

        assert self.routes_page.get_active_tariff() == "Comfort"

    #Test 3

    def test_fill_number(self):
        self.routes_page.click_number_button()
        number=data.phone_number
        self.routes_page.fill_number(number)
        self.routes_page.click_next_button()
        code=retrieve_phone_code(self.driver)
        self.routes_page.set_code(code)
        self.routes_page.click_confirm_button()
        assert self.routes_page.get_number_label()==number

    #Test 4

    def test_add_new_card(self):
        self.routes_page.click_payment_button()
        self.routes_page.click_add_card_button()
        self.routes_page.set_card_number(data.card_number)
        self.routes_page.click_cvv_number()
        self.routes_page.set_cvv_number(data.card_code)
        self.routes_page.click_add_card()
        self.routes_page.click_close()
        assert self.routes_page.get_card_added()=="Tarjeta"

    #Test 5

    def test_add_message(self):
        self.routes_page.click_message()
        message=data.message_for_driver
        self.routes_page.set_message(message)
        assert self.routes_page.get_message() == message

    #Test 6

    def test_add_blanket(self):
        self.routes_page.select_blanket()
        assert self.routes_page.is_blanket_selected() == True

    #Test 7
    def test_add_ice(self):
        self.routes_page.add_ice()
        self.routes_page.add_ice()
        assert self.routes_page.ice_value() == "2"

    #Test 8
    def test_order_taxi(self):
        self.routes_page.order_taxi()
        assert self.routes_page.is_order_window_visible() == True

    #Test 9
    def test_get_driver(self):

        assert self.routes_page.is_driver_info_visible() == True


    @classmethod
    def teardown_class(cls):
        time.sleep(5)
        cls.driver.quit()
