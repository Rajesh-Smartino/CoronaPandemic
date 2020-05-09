from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager #Error Correc



driver = webdriver.Chrome(ChromeDriverManager().install()) #Error Correc

#driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

name = input("Enter Contact or group name")
msg = input("Enter the message to be sent")
count = int(input("Enter the count"))

input("Enter anything after QR Code Scanning")



user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_class_name('_1Plpp') #_13mgZ #_3FeAD _1PRhq NW

for i in range(count):
	msg_box.send_keys(msg)
	button = driver.find_element_by_class_name('_35EW6') #hnQHL NW #_3M-N- #weEq5
	button.click()
