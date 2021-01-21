from selenium import webdriver
from os import system, name

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _= system('clear')

topic = input("What do you want to learn today ? (html or css or js):")
topic = topic.lower()

search = input("Enter the "+topic+" concept you want to learn(e.g, headings, lists, syntax, Object, arrays, etc):")
search = topic +" "+ search
search = search.replace(" ", "_")

options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(options = options)

url = 'https://www.w3schools.com/' + topic + '/' + search + ".asp"

driver.get(url)
el = driver.find_element_by_id('main')

clear()

print("----------------------------------------------"+search+"___________________________________")
print(el.text)

driver.close()
