import random
import string
import discord
import names
from time import sleep
from discord import SyncWebhook
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


a = input('Webhook url? y/n: ')
if a == 'y':
    webhook_url = input('What is their discord webhook url?: ')
else:
    pass
catchall = input('What is their catchall? EX @nolanmastro.xyz: ')
address =  input('What is their address?: ')
city = input('What is their city?: ')
zip_code = input('What is their zip code?: ')
how_many = int(input('How many did they order?: '))


shipping_codes = ['RACKA']
jig = ['apt. ', 'APT. ','apt ','Unit ','unit ']




def main():
    count = 0
    options = webdriver.ChromeOptions()
    driver = driver = webdriver.Chrome(service=Service(ChromeDriverManager(cache_valid_range=30).install()),options=options)
    for i in range(how_many + 1):
        create_account(driver)
        count = count + 1
        print(count)
    
def create_account(driver):
    driver.get('https://gamersupps.gg/products/free-trial-sample-packs')
    #add to cart/go to checkout
    WebDriverWait(driver, 205).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#product-form-8761784259-template--14618453770337__main > buy-buttons > button'))).click()
    WebDriverWait(driver, 205).until(EC.element_to_be_clickable((By.NAME, 'checkout'))).click()
    #set all info
    random_email = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
    random_email = random_email + catchall
    first_name = names.get_first_name()
    last_name = names.get_last_name()
    phone = '408' + ''.join(random.choice(string.digits) for _ in range(7))
    #enter info
    WebDriverWait(driver, 105).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#checkout_email'))).send_keys(random_email)
    sleep(0.2)
    driver.find_element(By.NAME, 'checkout[shipping_address][first_name]').send_keys(first_name)
    sleep(0.2)
    driver.find_element(By.NAME, 'checkout[shipping_address][last_name]').send_keys(last_name)
    sleep(0.4)
    driver.find_element(By.NAME, 'checkout[shipping_address][address1]').send_keys(address)
    sleep(0.4)
    elem = driver.find_element(By.NAME, 'checkout[shipping_address][address2]')
    elem.send_keys(random.choice(jig))
    sleep(0.4)
    elem.send_keys(random.randint(10,999))
    sleep(0.4)
    driver.find_element(By.NAME, 'checkout[shipping_address][city]').send_keys(city)
    sleep(0.4)
    sel = Select(driver.find_element(By.CSS_SELECTOR, '#checkout_shipping_address_province'))
    sel.select_by_index(48)
    sleep(0.5)
    driver.find_element(By.NAME, 'checkout[shipping_address][zip]').send_keys(zip_code)
    #free shipping
    sleep(0.4)
    driver.find_element(By.NAME, 'checkout[reduction_code]').send_keys(random.choice(shipping_codes))
    WebDriverWait(driver, 205).until(EC.element_to_be_clickable((By.NAME, 'checkout[submit]'))).click()
    sleep(1)
    driver.find_element(By.NAME, 'checkout[shipping_address][phone]').send_keys(phone)
    driver.find_element(By.NAME, 'button').click()
    #checkout
    WebDriverWait(driver, 250).until(EC.presence_of_element_located((By.NAME, 'button'))).click()
    WebDriverWait(driver, 250).until(EC.element_to_be_clickable((By.NAME, 'button'))).click()
    WebDriverWait(driver, 250).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.content > div > div > main > div.step > div.step__sections > div:nth-child(1) > div > div > span')))
    order_number = driver.find_element(By.CSS_SELECTOR, 'body > div.content > div > div > main > div.step > div.step__sections > div:nth-child(1) > div > div > span').text.strip()
    #send info to webhook
    embed=discord.Embed(title="Success!", color=0x5b0085)
    embed.add_field(name="Email: ", value=random_email, inline=False)
    embed.add_field(name="Address: ", value=address, inline=False)
    embed.add_field(name="Order Number: ", value=order_number, inline=False)
    webhook.send(embed=embed)
    


main()