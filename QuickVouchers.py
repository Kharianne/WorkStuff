import Functions
from selenium import webdriver
import Variables
import re
import time
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

variables = Functions.urlParserVouchers()
url = str(variables['url'])
print(url)
#url = Functions.urlParser()
domainLanguage = re.findall("^https?://(?:.+?)\.(.+?)\.", url)[0]
language = domainLanguage[2:4]
print(language)
timeStamp = str(int(time.time()))
#print(timeStamp)

today = datetime.datetime.now()
day = datetime.timedelta(days=1)
yesterday = today - day
tomorrow = today + day
yesterdayDate = yesterday.strftime("%y-%m-%d")
tomorrowDate = tomorrow.strftime("%y-%m-%d")


proc = str(variables['proc'])
fix = str(variables['fix'])
cred = str(variables['kred'])
if language == "sk":
    fix = '10'
    cred = '5'

amount = 100

voucherCodeProc = "Procenta-" + proc + "-" + timeStamp
voucherCodeFix = "Fix-" + fix + "-" + timeStamp
voucherCodeCred = "Kredity-" + cred + "-" + timeStamp

url = url + "/admin"
driver = webdriver.PhantomJS(executable_path='/Users/kacenka/Desktop/phantomjs') # or add to your PATH
print(url)
driver.get(url)
driver.set_window_size(1024, 768)


#WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,Variables.usernameXpath)))
driver.find_element_by_xpath(Variables.usernameXpath).send_keys('')
driver.find_element_by_xpath(Variables.passwordXpath).send_keys('')
driver.find_element_by_xpath(Variables.submit).click()

urlNow = driver.current_url
number = re.findall('^https?.+\.cz\/(?:admin\/)(\d)',urlNow)
domain = str(number[0])

url = url + '/' + domain + '/voucher/add'
#print(url)
driver.get(url)

#procenta
driver.find_element_by_xpath("//*[@id='frm-voucherForm-percent']").send_keys(proc)
driver.find_element_by_xpath("//*[@id='frm-voucherForm-name']").send_keys(voucherCodeProc)
driver.find_element_by_xpath("//*[@id='frm-voucherForm-code']").send_keys(voucherCodeProc)
driver.find_element_by_xpath("//*[@id='frm-voucherForm-amount']").send_keys(amount)
driver.find_element_by_xpath("//*[@id='frm-voucherForm-start']").clear()
driver.find_element_by_xpath("//*[@id='frm-voucherForm-start']").send_keys(yesterdayDate)
driver.find_element_by_xpath("//*[@id='frm-voucherForm-end']").clear()
driver.find_element_by_xpath("//*[@id='frm-voucherForm-end']").send_keys(tomorrowDate)
driver.find_element_by_xpath("(//*[@class='radio']//*[contains(text()[normalize-space()], 'Ano')])[1]").click()
driver.find_element_by_xpath("(//*[@class='radio']//*[contains(text()[normalize-space()], 'Ano')])[2]").click()
driver.find_element_by_xpath("//*[@type='submit']").click()
print(voucherCodeProc)

#fix
driver.get(url)
print(url)
WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,"//*[@class='radio']//*[contains(text()[normalize-space()], 'Fixní sleva')]")))
driver.find_element_by_xpath("//*[@class='radio']//*[contains(text()[normalize-space()], 'Fixní sleva')]").click()
driver.save_screenshot("beforefail.png")

WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,"//*[@id='frm-voucherForm-sale']" )))
driver.save_screenshot("fail.png")
driver.find_element_by_xpath("//*[@id='frm-voucherForm-sale']").send_keys(fix)
driver.find_element_by_xpath("//*[@id='frm-voucherForm-name']").send_keys(voucherCodeFix)
driver.find_element_by_xpath("//*[@id='frm-voucherForm-code']").send_keys(voucherCodeFix)
driver.find_element_by_xpath("//*[@id='frm-voucherForm-amount']").send_keys(amount)
driver.find_element_by_xpath("//*[@id='frm-voucherForm-start']").clear()
driver.find_element_by_xpath("//*[@id='frm-voucherForm-start']").send_keys(yesterdayDate)
driver.find_element_by_xpath("//*[@id='frm-voucherForm-end']").clear()
driver.find_element_by_xpath("//*[@id='frm-voucherForm-end']").send_keys(tomorrowDate)
driver.find_element_by_xpath("(//*[@class='radio']//*[contains(text()[normalize-space()], 'Ano')])[1]").click()
driver.find_element_by_xpath("(//*[@class='radio']//*[contains(text()[normalize-space()], 'Ano')])[2]").click()
driver.find_element_by_xpath("//*[@type='submit']").click()
print(voucherCodeFix)

#credits
driver.get(url)
#driver.save_screenshot("kred1.png")

WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,"//*[@class='radio']//*[contains(text()[normalize-space()], 'Kreditový poukaz')]" )))
#driver.save_screenshot("kred2.png")

driver.find_element_by_xpath("//*[@class='radio']//*[contains(text()[normalize-space()], 'Kreditový poukaz')]").click()
#driver.save_screenshot("kred.png")
WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,"//*[@id='frm-voucherForm-sale']" )))
driver.find_element_by_xpath("//*[@id='frm-voucherForm-sale']").send_keys(cred)
driver.find_element_by_xpath("//*[@id='frm-voucherForm-name']").send_keys(voucherCodeCred)
driver.find_element_by_xpath("//*[@id='frm-voucherForm-code']").send_keys(voucherCodeCred)
driver.find_element_by_xpath("//*[@id='frm-voucherForm-amount']").send_keys(amount)
driver.find_element_by_xpath("//*[@id='frm-voucherForm-start']").clear()
driver.find_element_by_xpath("//*[@id='frm-voucherForm-start']").send_keys(yesterdayDate)
driver.find_element_by_xpath("//*[@id='frm-voucherForm-end']").clear()
driver.find_element_by_xpath("//*[@id='frm-voucherForm-end']").send_keys(tomorrowDate)
driver.find_element_by_xpath("(//*[@class='radio']//*[contains(text()[normalize-space()], 'Ano')])[1]").click()
driver.find_element_by_xpath("(//*[@class='radio']//*[contains(text()[normalize-space()], 'Ano')])[2]").click()
driver.find_element_by_xpath("//*[@type='submit']").click()
print(voucherCodeCred)