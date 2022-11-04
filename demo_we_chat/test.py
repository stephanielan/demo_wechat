import json
import time
from selenium import webdriver


class TestLogin:
    # 使用本地保存的cookie文件扫码登录
    def test_login(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        with open('cookies.yaml', 'r', encoding='utf8') as f:
            cookies = json.loads(f.read())
        # 给浏览器添加cookies
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        time.sleep(3)
        # 刷新网页，cookies才会成功
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
