# eWork - Take Home Test
This repository for save all codes for **Take Home Test for QA Automation Engineer** position at **eDOT**.  
It covers automation for both **Web (eSuite)** and **Mobile (eWork - SFA)** platforms using:
- Python  
- Selenium + Pytest (for Web) 
- Appium + Pytest (for Mobile)
- Allure Reporting 


## Automated Scenario
The scenario automated in this script is: <br>
** Web automation :
  1. Login to eSuite 
  2. Create New Company
  3. Verify Company Detail
  4. Allure Reporting Required
<br>     
** Mobile automation :
  1. Login to Mobile App 
  2. Create Customer
 
Manual test case document here : 
```bash
https://docs.google.com/spreadsheets/d/1TwJE2ClQq7wQ2npPMQMVBCJKdN9sDpkrRjCWhK_Ly_c/edit?usp=sharing
```
Each test case includes:
| Field               | Description                              |
| ------------------- | ---------------------------------------- |
| Test Case ID        | Unique ID for each test                  |
| Title / Description | Brief description of the test            |
| Precondition        | Setup or state required before execution |
| Test Steps          | Step by step actions                     |
| Expected Result     | Expected system behavior                 |
| Status              | Pass / Fail                              |



## Project Structure
```
eDot-automation
├── web/
│   ├── pages/                
|       ├── company_page.py        
|       ├── dashboard_page.py           
|       ├── login_page.py      
│   ├── tests/
|       ├── test_create_company.py      
|       ├── test_login.py           
|       ├── test_verify_company.py  
├── Mobile/
│   ├── pages/                
|       ├── customer_page.py        
|       ├── dashboard_page.py           
|       ├── login_page.py      
│   ├── tests/
|       ├── create_customer.py        
|       ├── test_login.py           
│   ├── config/
|       ├── appium_config.py        
|       ├── scroll.py              
│   └── ...
├── allure-results
├── Phase_1_–_Manual_Test_Case_Design.xlsx
├── requirements.txt
└── README.md
```


## Environment Setup
Make sure the following tools are installed:
- Python
- Google Chrome
- Chromedriver
- Node.js
- Appium Server
- Java JDK
- Allure Commandline
- Android Emulator or Real Device (for Mobile test)
- eWork mobile app

Make sure the following package are installed:
- pip
- pytest
- selenium
- appium
- allure-pytest
- webdriver-manager
- faker

## Install Dependencies
1. Clone this repository
   ```bash
   git clone https://github.com/<your-username>/edot-automation.git
   ```
2. Install dependencies of packages.
3. 
  
## How to Run the Script
1.  **Web** 
    <br>Run all web tests:
    ```bash
    pytest web/tests --alluredir=allure-results
    ```
    Run a specific test file:
    ```bash
    pytest web/tests/test_login.py --alluredir=allure-results
    ```
    After run the script, generate and open the Allure report:
    ```bash
    allure serve allure-results
    ```
    
2.  **Mobile**
    Connect device first, then install apk of eWork mobile app in device:
    <br>APK Name : ework - SFA (available in Google PlayStore)
    <br>Run Appium Server in terminal or command line:
    ```bash
    appium
    ```
    or
    ```bash
    appium --allow-cors
    ```
    Run all mobile tests:
    ```bash
    pytest Mobile/tests --alluredir=allure-results
    ```
    Run a specific test file:
    ```bash
    pytest Mobile/tests/test_login.py --alluredir=allure-results
    ```
    After run the script, generate and open the Allure report:
    ```bash
    allure serve allure-results
    ```


## Reporting
   All test executions are integrated with Allure Pytest Reporting.
   Install Allure Pytest adapter:
   ```bash
   pip install allure-pytest
   ```
   To run the Allure report:
   ```bash
   pytest --alluredir=allure-results
   ```
   To generate a live report:
   ```bash
   allure serve allure-results
   ```






<br><br>This is the end of the files. <br>
Thank you.
