from selenium.webdriver.common.by import By



class UrbanRoutesLocators:
        from_field = (By.ID, 'from')
        to_field = (By.ID, 'to')

        #Localizadores de prueba 2
        take_taxi = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[1]/div[3]/div[1]/button')
        # Localizador del botón Comfort
        comfort = (By.XPATH, "//div[contains(@class, 'tcard-title') and text()='Comfort']")

        # Localizador de la tarjeta activa (para el assert)
        active_tariff = (By.XPATH,
                               "//div[contains(@class, 'tcard') and contains(@class, 'active')]//div[@class='tcard-title']")

        #Localizadores de prueba 3

        number_button = (By.CLASS_NAME, 'np-button')
        number_label = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[1]/div')
        fill_number = (By.ID, 'phone')
        next_button = (By.CLASS_NAME, 'button')
        code_number = (By.ID, 'code')
        confirm_button = (By.XPATH, '//button[text()="Confirmar"]')

        # Localizadores de prueba 4

        add_payment_button = (By.CLASS_NAME, 'pp-button')
        add_card = (By.CLASS_NAME, 'pp-plus-container')
        card_number = (By.XPATH, '//*[@id="number"]')
        cvv = (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[2]/form/div[1]/div[2]/div[2]/div[2]/input')  # <-- Localizador del CVV actualizado
        plc = (By.CLASS_NAME, 'plc')  # <-- Este localizador ya no es necesario, usaremos Keys.TAB
        add_button = (By.XPATH, '//button[text()="Agregar"]')
        close_payment = (By.XPATH, '//div[text()="Método de pago"]/preceding-sibling::button')
        card_added = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[2]/div[2]/div[1]')

        # Localizadores de prueba 5
        message = (By.XPATH, '//*[@id="comment"]')

        # Localizadores de prueba 6
        header_blanket= (By.CLASS_NAME, "reqs-head")
        blanket_checkbox = (By.XPATH, "//div[text()='Manta y pañuelos']/following-sibling::div//input[@type='checkbox']")

        # Localizadores de prueba 7
        header_ice_bucket= (By.CLASS_NAME, "r-group-title")
        add_ice= (By.CLASS_NAME, "counter-plus")
        ice_value= (By.CLASS_NAME, "counter-value")

        # Localizadores de prueba 8
        #//*[@id="root"]/div/div[3]/div[4]/button
        order_taxi = (By.CLASS_NAME, "smart-button")
        order_body = (By.CLASS_NAME, 'order-body')


        # Localizadores de prueba 9

        order_header_title = (By.CLASS_NAME, 'order-header-title')
        order_number = (By.CLASS_NAME, 'order-number')