from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def test_example():
    driver = webdriver.Firefox()
    driver.get("http://vagga.readthedocs.org/")
    assert "Welcome to Vagga" in driver.title
    driver.close()


if __name__ == '__main__':
    test_example()