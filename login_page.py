# login_page.py
import time

from selenium.webdriver.common.by import By
from common.basepage import BasePage
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage(BasePage):
    username = (By.CSS_SELECTOR, 'input[placeholder="请输入用户名"]')  # 用户名输入框
    user_password = (By.CSS_SELECTOR, 'input[placeholder="请输入密码"]')  # 密码输入框
    username_login_btn = (By.ID, 'smtlogin')  # 登录按钮
    api_tips = (By.CLASS_NAME, 'layui-layer-content')  # 接口消息提示
    Interface_tips = (By.CSS_SELECTOR, 'div[type="dialog"]')  # 界面提示
    user_id = (By.ID, 'usercode')  # 用户ID

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def page_operation(self, user, pwd):
        """
        海拓通用户登录
        :param user: 手机
        :param pwd: 密码
        :return: 登录成功

        """
        if user == '':
            pass
        else:
            self.input_text(self.username, user, '输入用户名')
        if pwd == '':
            pass
        else:
            self.input_text(self.user_password, pwd, '输入用户名')
        self.click_element(self.username_login_btn, '登录')
        time.sleep(0.5)
        text = self.get_text(self.Interface_tips, '登录界面提示')
        if text == '登录成功！':
            userid = self.get_text(self.user_id, '用户ID')
            return text, userid
        else:
            return text
