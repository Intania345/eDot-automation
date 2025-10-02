import time
import allure
from faker import Faker
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType

fake = Faker()

class CompanyPage:
    def __init__(self, driver):
        self.driver = driver

        # locator for company page menu
        self.company_menu = (By.XPATH, "//a[@href='/companies']")
        self.company_marker = (By.XPATH, "//span[contains(text(), 'My Company')]")
        self.company_add_button = (By.XPATH, "//button[contains(text(), '+ ')]")

        self.company_register_step1_marker = (By.XPATH, "//span[contains(text(), 'Register Company')]")
        self.company_register_step1_companyName_field = (By.XPATH, "//*[@placeholder='Input Company Name']")
        self.company_register_step1_email_field = (By.XPATH, "//*[@placeholder='Input Email']")
        self.company_register_step1_phone_field = (By.XPATH, "//*[@placeholder='Input Phone']")
        self.company_register_step1_industryType_field = (By.XPATH, "//span[contains(text(), 'Choose Industry Type')]")
        self.company_register_step1_industryType_option = (By.XPATH, "//span[contains(text(), 'Retail')]")
        self.company_register_step1_companyType_field = (By.XPATH, "//span[contains(text(), 'Choose Company Type')]")
        self.company_register_step1_companyType_option = (By.XPATH, "//span[contains(text(), 'Marketplace')]")
        self.company_register_step1_language_field = (By.XPATH, "//span[contains(text(), 'Choose Language')]")
        self.company_register_step1_language_option = (By.XPATH, "//span[contains(text(), 'English')]")
        self.company_register_step1_streetAddress_field = (By.XPATH, "//*[@placeholder='Input Address']")
        self.company_register_step1_country_field = (By.XPATH, "//span[contains(text(), 'Choose Country')]")
        self.company_register_step1_country_option = (By.XPATH, "//span[contains(text(), 'Indonesia')]")
        self.company_register_step1_province_field = (By.XPATH, "//span[contains(text(), 'Choose Province')]")
        self.company_register_step1_search = (By.XPATH, "//*[@placeholder='Search']")
        self.company_register_step1_province_search = "Jakarta"
        self.company_register_step1_province_option = (By.XPATH, "//div[contains(text(), 'DKI JAKARTA')]")
        self.company_register_step1_city_field = (By.XPATH, "//span[contains(text(), 'Choose City')]")
        self.company_register_step1_city_option = (By.XPATH, "//div[contains(text(), 'JAKARTA PUSAT')]")
        self.company_register_step1_district_field = (By.XPATH, "//span[contains(text(), 'Choose District')]")
        self.company_register_step1_district_option = (By.XPATH, "//div[contains(text(), 'TANAH ABANG')]")
        self.company_register_step1_subDistrict_field = (By.XPATH, "//span[contains(text(), 'Choose Sub District')]")
        self.company_register_step1_subDistrict_option = (By.XPATH, "//div[contains(text(), 'BENDUNGAN HILIR')]")
        self.company_register_step1_postalCode_field = (By.ID, "//*[@id='radix-:rag:']")
        self.company_register_next_button = (By.XPATH, "//button[contains(text(), 'Next')]")

        self.company_register_step2_registerLegal_marker = (By.XPATH, "//span[contains(text(), 'Register Legal')]")

        self.company_register_step3_branch_marker = (By.XPATH, "//span[contains(text(), 'Create Your Branch')]")
        self.company_register_step3_branchName_field = (By.XPATH, "//*[@placeholder='Input Branch Name']")
        self.company_register_step3_branch_fillData_button = (By.XPATH, "//button[contains(text(), 'Fill in with the same data from the Company records')]")
        self.company_reset_button = (By.XPATH, "//button[contains(text(), 'Reset')]")
        self.company_register_step3_streetAddress_field = (By.XPATH, "//*[@placeholder='Input Address']")
        self.company_register_step3_country_field = (By.XPATH, "//span[contains(text(), 'Indonesia')]")
        self.company_register_step3_province_field = (By.XPATH, "//span[contains(text(), 'DKI JAKARTA')]")
        self.company_register_step3_city_field = (By.XPATH, "//span[contains(text(), 'JAKARTA PUSAT')]")
        self.company_register_step3_district_field = (By.XPATH, "//span[contains(text(), 'TANAH ABANG')]")
        self.company_register_step3_subDistrict_field = (By.XPATH, "//span[contains(text(), 'BENDUNGAN HILIR')]")
        self.company_register_step3_postalCode_field = (By.XPATH, "//*[@id='radix-:rcs:']")
        self.company_register_step3_agreementSection = (By.XPATH, "//*[@class='Label ml-4']")
        self.company_register_step3_agreementCheckbox = (By.XPATH, "//*[@id='select-all']")
        self.company_register_button = (By.XPATH, "//button[contains(text(), 'Register')]")


        # locator for company detail page

        self.company_manage_button = (By.XPATH, "//button[contains(text(), 'Manage')]")
        self.backToCompany_button = (By.XPATH, "//span[contains(text(), 'Back to Company List')]")
        self.detail_companyName = (By.XPATH, "//*[@class='text-xl font-bold']")
        self.detail_companyText = (By.XPATH, "//span[contains(text(), 'Company')]")
        self.detail_companyProfileAccount = (By.XPATH, "//div[contains(text(), 'Profile Account')]")

        self.detail_companyDetailsText = (By.XPATH, "//h3[contains(text(), 'Company Details')]")
        self.detail_companyName_field = (By.XPATH, "//input[@placeholder='Input Company Name']")
        self.detail_companyId_field = (By.XPATH, "//*[@placeholder='Input Company ID']")
        self.detail_industryType_field = (By.XPATH, "//span[contains(text(), 'Retail')]")
        self.detail_companyType_field = (By.XPATH, "//span[contains(text(), 'Marketplace')]")
        self.detail_country_field = (By.XPATH, "//span[contains(text(), 'Indonesia')]")
        self.detail_province_field = (By.ID, "//span[contains(text(), 'DKI JAKARTA')]")
        self.detail_city_field = (By.ID, "//span[contains(text(), 'JAKARTA PUSAT')]")
        self.detail_district_field = (By.ID, "//span[contains(text(), 'TANAH ABANG')]")
        self.detail_subDistrict_field = (By.ID, "//span[contains(text(), 'BENDUNGAN HILIR')]")
        self.detail_postalCode_field = (By.XPATH, "//*[@placeholder='Choose Postal Code']")

        self.detail_mailingContactText = (By.XPATH, "//h3[contains(text(), 'Mailing & Contact')]")
        self.detail_email_field = (By.XPATH, "//*[@placeholder='Input Email']")
        self.detail_mobileNumber_field = (By.XPATH, "//*[@placeholder='Input Mobile Number']")
        self.detail_companyAddress_field = (By.XPATH, "//*[@placeholder='Input Company Address']")



    # keyword for company page flow

    def go_to_company_page(self):
        # self.driver.get("https://esuite.edot.id/companies")
        self.driver.find_element(*self.company_menu).is_displayed()
        self.driver.find_element(*self.company_menu).click()
        time.sleep(5)

    def verify_company_page(self):
        self.driver.find_element(*self.company_marker).is_displayed()
        self.driver.find_element(*self.company_add_button).click()
        time.sleep(3)

    def complete_register_company_step1(self, company_name, company_email, company_phone, company_address):
        self.driver.find_element(*self.company_register_step1_marker).is_displayed()
        self.driver.find_element(*self.company_register_step1_companyName_field).send_keys(company_name)
        company_name_text = company_name
        self.driver.find_element(*self.company_register_step1_email_field).send_keys(company_email)
        company_email_text = company_email
        self.driver.find_element(*self.company_register_step1_phone_field).send_keys(company_phone)
        company_phone_text = company_phone
        self.driver.execute_script("window.scrollTo(0, 500);")
        # choose industry type
        self.driver.find_element(*self.company_register_step1_industryType_field).click()
        self.driver.find_element(*self.company_register_step1_industryType_option).click()
        industry_type = self.get_industry_type()
        # choose company type
        self.driver.find_element(*self.company_register_step1_companyType_field).click()
        self.driver.find_element(*self.company_register_step1_companyType_option).click()
        company_type = self.get_company_type()
        # choose language
        self.driver.find_element(*self.company_register_step1_language_field).click()
        self.driver.find_element(*self.company_register_step1_language_option).click()
        language = self.get_language()
        # fill out street address
        self.driver.find_element(*self.company_register_step1_streetAddress_field).send_keys(company_address)
        company_address_text = company_address
        # choose country
        self.driver.find_element(*self.company_register_step1_country_field).click()
        self.driver.find_element(*self.company_register_step1_country_option).click()
        country = self.get_country()
        # choose province
        self.driver.find_element(*self.company_register_step1_province_field).click()
        self.driver.find_element(*self.company_register_step1_search).click()
        self.driver.find_element(*self.company_register_step1_search).send_keys("Jakarta")
        self.driver.find_element(*self.company_register_step1_province_option).click()
        province = self.get_province()
        self.driver.execute_script("window.scrollTo(0, 500);")
        # choose city
        self.driver.find_element(*self.company_register_step1_city_field).click()
        self.driver.find_element(*self.company_register_step1_city_option).click()
        city = self.get_city()
        # choose district
        self.driver.find_element(*self.company_register_step1_district_field).click()
        self.driver.find_element(*self.company_register_step1_district_option).click()
        district = self.get_district()
        # choose sub district
        self.driver.find_element(*self.company_register_step1_subDistrict_field).click()
        self.driver.find_element(*self.company_register_step1_subDistrict_option).click()
        sub_district = self.get_sub_district()
        sub_district = self.get_sub_district()
        postal_code = self.get_postal_code()
        time.sleep(2)

    def click_next_button(self):
        self.driver.find_element(*self.company_register_next_button).click()
        time.sleep(5)

    def get_company_name(self) -> None:
        company_name_text = self.driver.find_element(By.XPATH, "//*[@placeholder='Input Company Name']")
        company_name_text = company_name_text.text
        print("Company Name: ", company_name_text)

    def get_company_email(self) -> None:
        company_email_text = self.driver.find_element(By.XPATH, "//*[@placeholder='Input Email']")
        company_email_text = company_email_text.text
        print("Company Email: ", company_email_text)

    def get_company_phone(self) -> None:
        company_phone_text = self.driver.find_element(By.XPATH, "//*[@placeholder='Input Phone']")
        company_phone_text = company_phone_text.text
        print("Company Email: ", company_phone_text)

    def get_industry_type(self) -> None:
        industry_type_text = self.driver.find_element(By.XPATH, "//span[contains(text(), 'Retail')]")
        industry_type_text = industry_type_text.text
        print("Industry Type: ", industry_type_text)

    def get_company_type(self):
        company_type_text = self.driver.find_element(By.XPATH, "//span[contains(text(), 'Marketplace')]")
        company_type_text = company_type_text.text
        print("Company Type: ", company_type_text)

    def get_language(self) -> None:
        language_text = self.driver.find_element(By.XPATH, "//span[contains(text(), 'English')]")
        language_text = language_text.text
        print("Language: ", language_text)

    def get_country(self) -> None:
        country_text = self.driver.find_element(By.XPATH, "//span[contains(text(), 'Indonesia')]")
        country_text = country_text.text
        print("Country: ", country_text)

    def get_province(self) -> None:
        province_text = self.driver.find_element(By.XPATH, "//span[contains(text(), 'DKI JAKARTA')]")
        province_text = province_text.text
        print("Province: ", province_text)

    def get_city(self) -> None:
        city_text = self.driver.find_element(By.XPATH, "//span[contains(text(), 'JAKARTA PUSAT')]")
        city_text = city_text.text
        print("City: ", city_text)

    def get_district(self) -> None:
        district_text = self.driver.find_element(By.XPATH, "//span[contains(text(), 'TANAH ABANG')]")
        district_text = district_text.text
        print("District: ", district_text)

    def get_sub_district(self) -> None:
        sub_district_text = self.driver.find_element(By.XPATH, "//span[contains(text(), 'BENDUNGAN HILIR')]")
        sub_district_text = sub_district_text.text
        print("Sub District: ", sub_district_text)

    def get_postal_code(self) -> None:
        postal_code_text = "10210"
        print("Postal Code: ", postal_code_text)

    def take_screenshot(self, name="screenshot"):
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name=name,
            attachment_type=AttachmentType.PNG
        )

    def complete_register_company_step2(self):
        self.driver.find_element(*self.company_register_step2_registerLegal_marker).is_displayed()

    def complete_register_company_step3(self):
        self.driver.find_element(*self.company_register_step3_branch_marker).is_displayed()
        branch_name = self.get_branch_name()
        self.driver.find_element(*self.company_register_step3_branch_fillData_button).click()
        time.sleep(3)
        self.driver.find_element(*self.company_reset_button).is_displayed()
        self.driver.execute_script("window.scrollTo(0, 500);")
        self.driver.find_element(*self.company_register_step3_streetAddress_field).is_displayed()
        self.driver.find_element(*self.company_register_step3_country_field).is_displayed()
        self.driver.find_element(*self.company_register_step3_province_field).is_displayed()
        self.driver.execute_script("window.scrollTo(0, 500);")
        self.driver.find_element(*self.company_register_step3_city_field).is_displayed()
        self.driver.find_element(*self.company_register_step3_district_field).is_displayed()
        self.driver.find_element(*self.company_register_step3_subDistrict_field).is_displayed()
        self.driver.execute_script("window.scrollTo(0, 500);")
        self.driver.find_element(*self.company_register_step3_agreementSection).is_displayed()
        self.driver.find_element(*self.company_register_step3_agreementCheckbox).is_displayed()
        self.driver.find_element(*self.company_register_step3_agreementCheckbox).click()
        time.sleep(3)
        self.driver.find_element(*self.company_register_button).click()
        time.sleep(8)

    def get_branch_name(self) -> None:
        branch_name_text = "Headquarter"
        print("Branch Name: ", branch_name_text)

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
        return element

    def verify_after_create_company(self, company_name):
        company_name_value = company_name
        scroll_company = f"//div[contains(text(), '{company_name_value}')]"
        element = self.scroll_to_element((By.XPATH, scroll_company))
        time.sleep(5)
        assert element.is_displayed(), "Company is successfully created and displayed in company list"
        print(f"Company '{company_name}' is successfully created and displayed in company list")

    def open_company_detail(self):
        self.driver.find_element(*self.company_manage_button).is_displayed()
        elements = self.driver.find_elements(By.XPATH, "//button[contains(text(), 'Manage')]")
        last_index = len(elements)
        last_xpath = f"(//button[contains(text(), 'Manage')])[{last_index}]"
        print(f"XPath: {last_xpath}")
        last_element = self.driver.find_element(By.XPATH, last_xpath)
        last_element.click()
        time.sleep(5)

    def verify_company_detail_page(self):
        time.sleep(5)
        self.driver.find_element(*self.backToCompany_button).is_displayed()
        self.driver.find_element(*self.detail_companyName).is_displayed()
        self.driver.find_element(*self.detail_companyText).is_displayed()
        self.driver.find_element(*self.detail_companyProfileAccount).is_displayed()
        self.driver.find_element(*self.detail_companyDetailsText).is_displayed()
        self.driver.find_element(*self.detail_companyName_field).is_displayed()
        self.driver.find_element(*self.detail_companyId_field).is_displayed()
        self.driver.execute_script("window.scrollTo(0, 500);")
        time.sleep(3)
        self.driver.find_element(*self.detail_industryType_field).is_displayed()
        self.driver.find_element(*self.detail_companyType_field).is_displayed()
        self.driver.execute_script("window.scrollTo(0, 500);")
        time.sleep(3)
        self.driver.find_element(*self.detail_country_field).is_displayed()
        self.driver.execute_script("window.scrollTo(0, 500);")
        self.driver.find_element(*self.detail_mailingContactText).is_displayed()
        self.driver.execute_script("window.scrollTo(0, 500);")
        self.driver.find_element(*self.detail_email_field).is_displayed()
        self.driver.find_element(*self.detail_mobileNumber_field).is_displayed()
        self.driver.find_element(*self.detail_companyAddress_field).is_displayed()

    def get_company_detail(self):
        self.driver.execute_script("window.scrollTo(0, -1000);")
        time.sleep(5)
        industry_type_value = self.driver.find_element(*self.detail_industryType_field).text
        company_type_value = self.driver.find_element(*self.detail_companyType_field).text
        self.driver.execute_script("window.scrollTo(0, 500);")
        country_value = self.driver.find_element(*self.detail_country_field).text
        return {
            "industry_type_value": industry_type_value,
            "company_type_value": company_type_value,
            "country_value": country_value
        }
