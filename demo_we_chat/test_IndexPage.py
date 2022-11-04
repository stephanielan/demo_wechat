import time
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestIndexPage:
    #打开浏览器
    def test_add_address(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        cookies = yaml.safe_load(open("cookies.yaml"))
        # 给浏览器添加cookies
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        time.sleep(3)
        # 刷新网页，cookies才会成功
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        time.sleep(3)
        self.driver.find_element(By.LINK_TEXT,"通讯录").click()
        self.driver.find_element(By.LINK_TEXT, "添加成员").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "username").send_keys("test08")
        time.sleep(1)
        self.driver.find_element(By.ID, "memberAdd_acctid").click()
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys("account08")
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys("15900000008")
        self.driver.find_element(By.LINK_TEXT, "保存").click()
    def test_add_dep(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        cookies = yaml.safe_load(open("cookies.yaml"))
        # 给浏览器添加cookies
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        time.sleep(3)
        # 刷新网页，cookies才会成功
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        time.sleep(3)
        self.driver.find_element(By.LINK_TEXT, "通讯录").click()
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, ".member_colLeft_top_addBtn").click()
        self.driver.find_element(By.LINK_TEXT, "添加部门").click()
        time.sleep(2)
        self.driver.find_element(By.NAME, "name").send_keys("测试部")
        self.driver.find_element(By.LINK_TEXT, "选择所属部门").click()
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR,"div.jstree:nth-child(1)").click()
        self.driver.find_element(By.LINK_TEXT, "确定").click()




