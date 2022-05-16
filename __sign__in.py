from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Using chrome as a web browser
driver = webdriver.Chrome(ChromeDriverManager().install())
def signin():
    # copy and paste the wikipedia link
    url = "https://en.wikipedia.org/wiki/List_of_sister_cities_in_Europe"
    driver.get(url)
    driver.maximize_window()