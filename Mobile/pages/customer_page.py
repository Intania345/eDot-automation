import time
from multiprocessing.connection import address_type

from appium.webdriver.common.appiumby import AppiumBy
from Mobile.config.scroll import scroll_to_element, scroll_to_text, scroll_down_until_end


class CustomerPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_customer_menu = (AppiumBy.XPATH, "(//android.widget.FrameLayout[@resource-id='id.edot.ework:id/card_icon'])[5]")
        self.new_customer_list_title = (AppiumBy.ID, "id.edot.ework:id/tvTitleHeader")
        self.new_customer_add_button = (AppiumBy.ID, "id.edot.ework:id/tvRegister")

        # Basic
        # Store Information
        self.basic_title = (AppiumBy.ID, "id.edot.ework:id/tv_stepper_customer_data")
        self.store_information_title = (AppiumBy.ID, "id.edot.ework:id/tv_title_reg_customer")
        self.outlet_name_field = (AppiumBy.ID, "id.edot.ework:id/et_outlet_name")
        self.outlet_phone_number_field = (AppiumBy.ID, "id.edot.ework:id/et_outlet_phone")
        self.outlet_email_field = (AppiumBy.ID, "id.edot.ework:id/et_outlet_email")
        self.outlet_contact_person_field = (AppiumBy.ID, "id.edot.ework:id/et_contact_person")

        self.channel_type_field = (AppiumBy.ID, "id.edot.ework:id/et_channel")
        self.channel_type_option = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='id.edot.ework:id/tvName' and @text='Modern Trade (MT)']")
        self.customer_type_field = (AppiumBy.ID, "id.edot.ework:id/et_outlet_type")
        self.customer_type_option = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='id.edot.ework:id/tvName' and @text='Semi Grosir']")
        self.price_list_field = (AppiumBy.ID, "id.edot.ework:id/et_pricelist")
        self.price_list_option = (AppiumBy.ID, "id.edot.ework:id/tvName")
        self.continue_button1 = (AppiumBy.ID, "id.edot.ework:id/button_text")

        self.locations_title = (AppiumBy.ID, "id.edot.ework:id/tv_stepper_payment_data")
        self.address_type_field = (AppiumBy.ID, "id.edot.ework:id/et_address_type")
        self.address_type_option = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='id.edot.ework:id/tvName' and @text='Others']")
        self.address_field = (AppiumBy.ID, "id.edot.ework:id/etAddress")
        self.choose_province_field = (AppiumBy.XPATH, "//android.widget.EditText[@resource-id='id.edot.ework:id/etInput' and @text='Choose Province']")
        self.choose_province_option = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='id.edot.ework:id/txt_name' and @text='PAPUA']")

        self.apply_button = (AppiumBy.XPATH, "//android.widget.Button[@resource-id='id.edot.ework:id/button_text' and @text='Apply']")

        self.choose_city_field = (AppiumBy.XPATH, "//android.widget.EditText[@resource-id='id.edot.ework:id/etInput' and @text='Choose City']")
        self.choose_city_option = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='id.edot.ework:id/txt_name' and @text='KOTA JAYAPURA']")
        self.choose_district_field = (AppiumBy.XPATH, "//android.widget.EditText[@resource-id='id.edot.ework:id/etInput' and @text='Choose District']")
        self.choose_district_option = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='id.edot.ework:id/txt_name' and @text='MUARA TAMI']")
        self.choose_sub_district_field = (AppiumBy.XPATH, "//android.widget.EditText[@resource-id='id.edot.ework:id/etInput' and @text='Choose Sub district']")
        self.choose_sub_district_option = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='id.edot.ework:id/txt_name' and @text='MOSSO']")
        self.choose_postal_code_field = (AppiumBy.XPATH, "//android.widget.EditText[@resource-id='id.edot.ework:id/etInput' and @text='Choose Postal code']")
        self.choose_postal_code_option = (AppiumBy.ID, "id.edot.ework:id/txt_name")
        self.longitude_field = (AppiumBy.ID, "id.edot.ework:id/et_longitude")
        self.latitude_field = (AppiumBy.ID, "id.edot.ework:id/et_latitude")
        self.continue_button = (AppiumBy.XPATH, "//android.widget.Button[@resource-id='id.edot.ework:id/button_text' and @text='Continue']")

        self.confirm1 = (AppiumBy.ID, "id.edot.ework:id/dialog_title")
        self.positive_button = (AppiumBy.ID, "id.edot.ework:id/btn_positive")
        self.negative_button = (AppiumBy.ID, "id.edot.ework:id/btn_negative")
        self.allow1 = (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_button")
        self.allow2 = (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_button")

        self.documents_title = (AppiumBy.ID, "id.edot.ework:id/tv_stepper_location_data")
        self.ktp_field = (AppiumBy.ID, "id.edot.ework:id/etInput")
        self.upload_file_button = (AppiumBy.XPATH, "//android.widget.Button[@resource-id='id.edot.ework:id/button_text' and @text='Upload File']")
        self.capture_button = (AppiumBy.ID, "id.edot.ework:id/btn_capture")
        self.submit_button = (AppiumBy.XPATH, "//android.widget.Button[@resource-id='id.edot.ework:id/button_text' and @text='Submit']")

       # signature
        self.signature_title = (AppiumBy.ID, "id.edot.ework:id/tv_title")
        self.signature_field = (AppiumBy.ID, "id.edot.ework:id/signature_view")
        self.register_button = (AppiumBy.XPATH, "//android.widget.Button[@resource-id='id.edot.ework:id/button_text' and @text='Register']")
        self.confirm2_title = (AppiumBy.ID, "id.edot.ework:id/dialog_title")
        self.confirm2_yes = (AppiumBy.XPATH, "//android.widget.Button[@resource-id='id.edot.ework:id/button_text' and @text='Yes']")
        self.confirm2_cancel = (AppiumBy.XPATH, "//android.widget.Button[@resource-id='id.edot.ework:id/button_text' and @text='Cancel']")

        self.icon_outlet = (AppiumBy.XPATH, "//androidx.recyclerview.widget.RecyclerView[@resource-id='id.edot.ework:id/rvNooCustomer']/android.widget.FrameLayout[6]/android.view.ViewGroup")
        self.customer_profile_view = (AppiumBy.XPATH, "(//android.widget.ImageView[@resource-id='id.edot.ework:id/iv_profile])[5]")
        self.customer_name_view = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='id.edot.ework:id/tv_name']")
        self.customer_reg_number_view = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='id.edot.ework:id/tv_reg_number']")
        self.customer_status_view = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='id.edot.ework:id/tv_status']")
        self.customer_distance_view = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='id.edot.ework:id/tv_distance']")
        self.customer_address_view = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='id.edot.ework:id/tv_address']")


    def go_to_customer_page(self):
        time.sleep(5)
        self.driver.find_element(*self.add_customer_menu).is_displayed()
        self.driver.find_element(*self.add_customer_menu).click()
        time.sleep(5)
        self.driver.find_element(*self.new_customer_add_button).is_displayed()

    def create_customer_basic(self, outlet_name, outlet_phone, outlet_email, outlet_cp):
        self.driver.find_element(*self.new_customer_add_button).click()
        time.sleep(3)
        self.driver.find_element(*self.basic_title).is_displayed()
        # outlet name
        self.driver.find_element(*self.outlet_name_field).send_keys(outlet_phone)
        outlet_name_value = self.driver.find_element(AppiumBy.ID, "id.edot.ework:id/et_outlet_name")
        outlet_name_value.send_keys(outlet_name)
        outlet_name_value = outlet_name_value.text
        print(outlet_name_value)
        # outlet phone
        self.driver.find_element(*self.outlet_phone_number_field).send_keys(outlet_phone)
        outlet_phone_value = self.driver.find_element(AppiumBy.ID, "id.edot.ework:id/et_outlet_phone")
        outlet_phone_value.send_keys(outlet_phone)
        outlet_phone_value = outlet_phone_value.text
        print(outlet_phone_value)
        # outlet email
        self.driver.find_element(*self.outlet_email_field).send_keys(outlet_email)
        outlet_email_value = self.driver.find_element(AppiumBy.ID, "id.edot.ework:id/et_outlet_email")
        outlet_email_value.send_keys(outlet_email)
        outlet_email_value = outlet_email_value.text
        print(outlet_email_value)
        # outlet contact person
        self.driver.find_element(*self.outlet_contact_person_field).send_keys(outlet_cp)
        outlet_cp_value = self.driver.find_element(AppiumBy.ID, "id.edot.ework:id/et_contact_person")
        outlet_cp_value.send_keys(outlet_cp)
        outlet_cp_value = outlet_cp_value.text
        print(outlet_cp_value)
        # choose channel
        element = scroll_to_element(self.driver, AppiumBy.ID, "id.edot.ework:id/et_channel")
        element.click()
        time.sleep(3)
        self.driver.find_element(*self.channel_type_option).click()
        # choose customer type
        # element = scroll_to_element(self.driver, AppiumBy.ID, "id.edot.ework:id/et_outlet_type")
        # element.click()
        time.sleep(3)
        self.driver.find_element(*self.customer_type_field).click()
        self.driver.find_element(*self.customer_type_option).click()
        # choose price list
        time.sleep(3)
        self.driver.find_element(*self.price_list_field).click()
        time.sleep(3)
        self.driver.find_element(*self.price_list_option).click()
        time.sleep(3)
        # tap next
        self.driver.find_element(*self.continue_button1).click()
        time.sleep(5)

    def create_customer_locations(self, address, longitude, latitude):
        self.driver.find_element(*self.locations_title).is_displayed()
        # address type
        self.driver.find_element(*self.address_type_field).click()
        self.driver.find_element(*self.address_type_option).click()
        time.sleep(3)
        # address
        element = scroll_to_element(self.driver, AppiumBy.ID, "id.edot.ework:id/etAddress")
        element.click()
        time.sleep(3)
        self.driver.find_element(*self.address_field).send_keys(address)
        address_value = self.driver.find_element(AppiumBy.ID, "id.edot.ework:id/etAddress")
        address_value.send_keys(address)
        address_value = address_value.text
        print(address_value)
        # choose province
        element = scroll_to_element(self.driver, AppiumBy.XPATH, "//android.widget.EditText[@resource-id='id.edot.ework:id/etInput' and @text='Choose Province']")
        element.click()
        time.sleep(3)
        self.driver.find_element(*self.choose_province_option).click()
        time.sleep(3)
        # choose city
        self.driver.find_element(*self.choose_city_field).click()
        time.sleep(3)
        self.driver.find_element(*self.choose_city_option).click()
        time.sleep(3)
        # choose district
        self.driver.find_element(*self.choose_district_field).click()
        time.sleep(3)
        self.driver.find_element(*self.choose_district_option).click()
        time.sleep(3)
        # choose sub district
        self.driver.find_element(*self.choose_sub_district_field).click()
        time.sleep(3)
        self.driver.find_element(*self.choose_sub_district_option).click()
        time.sleep(3)
        # choose postal code
        element = scroll_to_element(self.driver, AppiumBy.XPATH, "//android.widget.EditText[@resource-id='id.edot.ework:id/etInput' and @text='Choose Postal code']")
        element.click()
        time.sleep(3)
        self.driver.find_element(*self.choose_postal_code_option).is_displayed()
        time.sleep(3)
        self.driver.find_element(*self.choose_postal_code_option).click()
        time.sleep(3)
        # longitude
        element = scroll_to_element(self.driver, AppiumBy.ID, "id.edot.ework:id/et_longitude")
        element.click()
        time.sleep(3)
        self.driver.find_element(*self.longitude_field).is_displayed()
        # latitude
        time.sleep(3)
        element = scroll_to_element(self.driver, AppiumBy.ID, "id.edot.ework:id/et_latitude")
        element.click()
        time.sleep(3)
        self.driver.find_element(*self.latitude_field).is_displayed()
        time.sleep(3)
        # tap continue
        self.driver.find_element(*self.continue_button).click()
        time.sleep(3)

    def create_customer_documents(self, ktp):
        self.driver.find_element(*self.documents_title).is_displayed()
        # fill out ktp
        self.driver.find_element(*self.ktp_field).is_displayed()
        self.driver.find_element(*self.ktp_field).send_keys(ktp)
        time.sleep(3)
        # upload file
        self.driver.find_element(*self.upload_file_button).is_displayed()
        self.driver.find_element(*self.upload_file_button).click()
        time.sleep(5)
        self.driver.find_element(*self.capture_button).click()
        time.sleep(5)
        self.driver.find_element(*self.submit_button).click()
        # signature
        time.sleep(3)
        self.driver.find_element(*self.signature_title).is_displayed()
        self.driver.find_element(*self.signature_field).is_displayed()
        self.driver.find_element(*self.signature_field).click()
        time.sleep(3)
        # tap register button
        self.driver.find_element(*self.register_button).click()
        time.sleep(3)
        # tap confirmation
        self.driver.find_element(*self.confirm2_title).is_displayed()
        self.driver.find_element(*self.confirm2_yes).is_displayed()
        self.driver.find_element(*self.confirm2_cancel).is_displayed()
        self.driver.find_element(*self.confirm2_yes).click()
        time.sleep(5)

    def verify_created_customer(self):
        scroll_down_until_end(self.driver)
        time.sleep(5)
        self.driver.find_element(*self.customer_name_view).is_displayed()
        self.driver.find_element(*self.customer_reg_number_view).is_displayed()
        self.driver.find_element(*self.customer_status_view).is_displayed()
        self.driver.find_element(*self.customer_distance_view).is_displayed()
        self.driver.find_element(*self.customer_address_view).is_displayed()