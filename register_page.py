# login_page.py
import time
from selenium.webdriver.common.by import By
from common.basepage import BasePage
from selenium.webdriver.remote.webdriver import WebDriver


class RegisterPage(BasePage):
    register = (By.ID, 'registerButton')  # 注册
    phone_number = (By.CSS_SELECTOR, 'input[placeholder="请输入注册手机号"]')  # 注册手机号
    user_password = (By.CSS_SELECTOR, '#register>div input[placeholder="请输入密码"]')  # 密码输入框
    user_password2 = (By.CSS_SELECTOR, '#register>div input[placeholder="确认密码"]')  # 确认密码
    company = (By.CSS_SELECTOR, '#register>div input[placeholder="公司名称"]')  # 公司名称
    agreement = (By.CSS_SELECTOR, 'input[name="Agreement"] + div>i')  # 协议
    register_btn = (By.ID, 'smtregister')  # 注册按钮
    tips = (By.CLASS_NAME, 'layui-layer-content')  # 界面提示

    # Interface_tips = (By.CSS_SELECTOR, 'div[type="dialog"]')  # 界面提示

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def page_switch(self):
        self.click_element(self.register, '切换到注册页')

    def page_operation(self, phone, pwd, pwd2, company_name):
        """
        海拓通用户注册
        :param phone: 手机
        :param pwd: 密码
        :param pwd2: 确认密码
        :param company_name: 公司名称
        :return: 注册提示
        """
        self.input_text(self.phone_number, phone, '输入注册手机')
        self.input_text(self.user_password, pwd, '输入密码')
        self.input_text(self.user_password2, pwd2, '确认密码')
        self.input_text(self.company, company_name, '输入公司名称')
        if phone == '15888888888':
            pass
        else:
            self.click_element(self.agreement, '勾选协议')
        self.click_element(self.register_btn, '点击注册')
        time.sleep(0.5)
        text = self.get_text(self.tips, '登录界面提示')
        return text
