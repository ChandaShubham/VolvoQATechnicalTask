class locators():
    
    # Common locators
    
    cookie_element_id = "onetrust-accept-btn-handler"
    
    # Home page object
    
    allModel_element_xpath = "//h2[contains(text(),'All models')]"
    suv_element_xpath = "//p[contains(text(),'SUV (')]"
    sedan_element_xpath = "//p[contains(text(),'Sedan (')]"
    quick_link_element_xpath = "//p[contains(text(),'Quick Links')]"
    support_object_xpath = "//p[contains(text(),'Support')]"

    # List
    
    suv_models_xpath_list = [
            "//span[contains(text(),'C40 Recharge')]" ,
            "//span[contains(text(),'XC40 Recharge')]",
            "//span[contains(text(),'XC60')]",
            "//span[contains(text(),'XC90')]"
    ]
    
    sedan_models_xpath_list = ["//span[contains(text(),'S90')]"]
    
    support_xpath_list = [
            "//p[contains(text(),'Car information')]",
            "//span[contains(text(),'Electrification')]",
            "//span[contains(text(),'Volvo Cars app')]",
            "//span[contains(text(),'Maintenance and repair')]",
            "//span[contains(text(),'Profile and billings')]",
            "//span[contains(text(),'About us')]"
    ]