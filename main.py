from selenium import webdriver
from time import sleep
from secrets import pw


class InstaBot:

    def __init__(self, username, pw):
        self.driver = webdriver.Chrome()
        self.username = username
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath(
            "//button[contains(text(), 'Accept')]").click()

        login = self.driver.find_element_by_xpath(
            "//input[@name='username']").send_keys(username)
        login = self.driver.find_element_by_xpath(
            "//input[@name='password']").send_keys(pw)
        login = self.driver.find_element_by_xpath(
            "//button[@type='submit']").click()
        sleep(4)
        login = self.driver.find_element_by_xpath(
            "//button[contains(text(), 'Not Now')]").click()
        login = self.driver.find_element_by_xpath(
            "//button[contains(text(), 'Not Now')]").click()

    def get_unfollowers(self):
        self.driver.find_element_by_xpath(
            f"//a[contains(@href, '{self.username}')]").click()
        sleep(1)
        self.driver.find_element_by_xpath(
            "//a[contains(@href, 'following')]").click()
        following = self.get_names()
        sleep(1)
        self.driver.find_element_by_xpath(
            "//a[contains(@href, 'followers')]").click()
        followers = self.get_names()
        not_following_back = [
            user for user in following if user not in followers]
        print(not_following_back)

    def get_names(self):
        sleep(1)
        sugs = self.driver.find_element_by_xpath(
            "//div[@role='dialog']")
        sleep(1)
        self.driver.execute_script('arguments[0].scrollIntoView()', sugs)
        scroll_box = self.driver.find_element_by_xpath(
            "/html/body/div[5]/div/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                return arguments[0].scrollHeight;
                """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        # close button
        self.driver.find_element_by_xpath(
            "/html/body/div[5]/div/div/div[1]/div/div[2]/button").click()
        return names


if __name__ == '__main__':
    my_Bot = InstaBot('iamkucserag', pw)
    my_Bot.get_unfollowers()
    sleep(5)
