# login_page.py
import time
from selenium.webdriver.common.by import By
from common.basepage import BasePage
from selenium.webdriver.remote.webdriver import WebDriver


class PredictionBoxPage(BasePage):
    # 中转入库预报
    transfer = (By.CSS_SELECTOR, 'nav[flex-box="1"] li:nth-child(1)')  # 货物中转
    management = (By.CSS_SELECTOR, '#transferinorder .htt-icon')  # 入库管理
    prediction = (By.CSS_SELECTOR, '#transferinorder #createinorder')  # 入库预报
    country = (By.CSS_SELECTOR, '#CountryCode + div input[placeholder="请选择"]')  # 寄往国家
    country_option = (By.CSS_SELECTOR, 'dd[lay-value="US"]')  # 寄往国家选项
    Warehouse = (By.CSS_SELECTOR, '#WarehouseCode + div input[placeholder="请选择"]')  # 寄往仓库
    Warehouse_option = (By.CSS_SELECTOR, 'dd[lay-value="USDB"]')  # 寄往仓库选项
    order_number = (By.CSS_SELECTOR, 'input[placeholder="请输入客户订单号"]')  # 客户订单号
    Arrival_time = (By.CSS_SELECTOR, 'input[placeholder="请选择日期"]')  # 到货时间
    now_time = (By.CSS_SELECTOR, 'span[lay-type="now"]')  # 选择现在时间
    Remark = (By.CLASS_NAME, 'layui-textarea')  # 备注
    box_number = (By.CSS_SELECTOR, 'input[placeholder="请输入入库预报箱数"]')  # 预报箱数
    company = (By.CSS_SELECTOR, '#BatAttributes + div input')  # 箱子属性
    company_option = (By.CSS_SELECTOR, '#BatAttributes + div dl dd[lay-value="普货"]')  # 箱子属性选项
    add_box = (By.ID, 'addBox')  # 添加箱子
    zy_box = (By.CSS_SELECTOR, 'input[placeholder="请输入自有箱号"][data-index="1"]')  # 自有箱号1
    delete_box = (By.CSS_SELECTOR, 'a[lay-event="del"][data-index="1"]')  # 删除按钮
    Submit = (By.ID, '#saveData')  # 提交
    jm_tips = (By.CLASS_NAME, 'layui-layer-content')  # 界面提示
    iframe = (By.CSS_SELECTOR, 'iframe[tab-id="1"]')  # 切换界面
    # 完成页信息
    success_tips = (By.CSS_SELECTOR, '#finishpage h2')  # 成功提示
    Interface_order_code = (By.ID, 'ordercodelabel')  # 入库订单单号
    details = (By.ID, 'godetail')  # 查看详情
    # 详情页信息
    InOrderCode = (By.ID, 'InOrderCode')  # 入库订单号
    OrderStatus = (By.ID, 'OrderStatus')  # 入库订单状态
    boxcode = (By.CSS_SELECTOR, 'td[data-field="BoxCode"]')  # 箱子号

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def page_operation_right(self, number_order, re, number_box, zy_box_name, zy_box_patch):
        """
        入库预报正常流程
        :param number_order: 客户订单号
        :param re: 备注
        :param number_box: 入库预报箱数
        :param zy_box_name: 自有箱号
        :param zy_box_patch: 填写自有箱号位置
        """
        self.click_element(self.transfer, '点击货物中转')
        self.click_element(self.management, '点击入库管理')
        self.click_element(self.prediction, '点击入库预报')
        self.driver.switch_to.frame(self.get_element(self.iframe, '获取切换ifram位置'))
        self.click_element(self.country, '点击寄往国家')
        time.sleep(0.2)
        self.click_element(self.country_option, '选择寄件国家')
        self.click_element(self.Warehouse, '点击寄往仓库')
        time.sleep(0.2)
        self.click_element(self.Warehouse_option, '选择寄往仓库')
        self.input_text(self.order_number, number_order, '填写客户订单号')
        self.click_element(self.Arrival_time, '点击预计到货时间')
        time.sleep(0.2)
        self.click_element(self.now_time, '选择到货时间选择')
        self.input_text(self.Remark, re, '输入备注')
        self.input_text(self.box_number, number_box, '输入入库预报箱数')
        self.click_element(self.company, '点击箱子属性')
        time.sleep(0.2)
        self.click_element(self.company_option, '选择箱子属性')
        self.click_element(self.add_box, '点击添加箱子')
        time.sleep(0.2)
        # 填写自有箱号,通过位置参数改变
        self.input_text((By.CSS_SELECTOR, 'input[placeholder="请输入自有箱号"][data-index="{0}"]'.format(zy_box_patch)), zy_box_name, '填写自有箱号')
        return self.common()

    def page_operation_Required(self, number_box, box_type, country, warehouse, now_time):
        """
        入库预报必填项验证流程
        :param number_box: 箱子数
        :param box_type: 箱子属性
        :param country: 国家
        :param warehouse: 仓库
        :param now_time: 时间
        """
        time.sleep(2)
        self.click_element(self.transfer, '点击货物中转')
        self.click_element(self.management, '点击入库管理')
        self.click_element(self.prediction, '点击入库预报')
        self.driver.switch_to.frame(self.get_element(self.iframe, '获取切换ifram位置'))
        self.input_text(self.box_number, number_box, '输入入库预报箱数')
        if int(number_box) <= 0 or int(number_box) > 200:  # 箱数填写错误
            self.click_element(self.company, '点击箱子属性')
            time.sleep(0.2)
            self.click_element(self.company_option, '选择箱子属性')
            self.click_element(self.add_box, '点击添加箱子')
            time.sleep(0.5)
            tips = self.get_text(self.jm_tips, '获取界面提示')
            return tips
        if box_type == '':  # 不填写箱子类型
            self.click_element(self.add_box, '点击添加箱子')
            time.sleep(0.5)
            tips = self.get_text(self.jm_tips, '获取界面提示')
            return tips
        self.click_element(self.company, '点击箱子属性')
        time.sleep(0.2)
        self.click_element(self.company_option, '选择箱子属性')
        self.click_element(self.add_box, '点击添加箱子')
        if country == '':  # 不填写国家
            return self.common_tips()
        self.click_element(self.country, '点击寄往国家')
        time.sleep(0.2)
        self.click_element(self.country_option, '选择寄件国家')
        if warehouse == '':  # 不填写仓库
            return self.common_tips()
        self.click_element(self.Warehouse, '点击寄往仓库')
        time.sleep(0.2)
        self.click_element(self.Warehouse_option, '选择寄往仓库')
        if now_time == '':  # 不填写时间
            return self.common_tips()
        self.click_element(self.Arrival_time, '点击预计到货时间')
        time.sleep(0.2)
        self.click_element(self.now_time, '选择到货时间选择')
        return self.common()

    def page_operation_box(self, number_order, re, number_box, zy_box_name):
        """
        入库预报箱子增加删除流程
        :param number_order: 客户订单号
        :param re: 备注
        :param number_box: 入库预报箱数
        :param zy_box_name: 自有箱号
        """
        self.click_element(self.transfer, '点击货物中转')
        self.click_element(self.management, '点击入库管理')
        self.click_element(self.prediction, '点击入库预报')
        self.driver.switch_to.frame(self.get_element(self.iframe, '获取切换ifram位置'))
        self.click_element(self.country, '点击寄往国家')
        time.sleep(0.2)
        self.click_element(self.country_option, '选择寄件国家')
        self.click_element(self.Warehouse, '点击寄往仓库')
        time.sleep(0.2)
        self.click_element(self.Warehouse_option, '选择寄往仓库')
        self.input_text(self.order_number, number_order, '填写客户订单号')
        self.click_element(self.Arrival_time, '点击预计到货时间')
        time.sleep(0.2)
        self.click_element(self.now_time, '选择到货时间选择')
        self.input_text(self.Remark, re, '输入备注')
        self.input_text(self.box_number, number_box, '输入入库预报箱数')
        self.click_element(self.company, '点击箱子属性')
        time.sleep(0.2)
        self.click_element(self.company_option, '选择箱子属性')
        self.click_element(self.add_box, '点击添加箱子')
        time.sleep(0.2)
        self.input_text(self.zy_box, zy_box_name, '填写自有箱号')
        return self.common()

    def common(self):
        """获取详情信息"""
        ele = self.get_elements(self.boxcode, '获取创建箱号')
        new_box_list = []  # 新建箱子列表
        for i in ele:  # 循环添加列表箱子号
            new_box_list.append(i.text)
        self.click_element(self.Submit, '点击提交')
        jm_orderid = self.get_text(self.Interface_order_code, '成功展示的订单号')
        self.click_element(self.details, '点击详情')
        xq_orderid = self.get_text(self.InOrderCode, '入库订单号')  # 入库订单号
        status = self.get_text(self.OrderStatus, '入库订单状态')  # 入库订单状态
        ele = self.get_elements(self.boxcode, '获取详情箱号')
        xq_box_list = []  # 详情箱子列表
        for i in ele:  # 循环添加详情箱子号
            xq_box_list.append(i.text)

        return jm_orderid, xq_orderid, status, new_box_list, xq_box_list

    def common_tips(self):
        """获取页面提示信息"""
        self.click_element(self.Submit, '点击提交')
        time.sleep(0.2)
        tips = self.get_text(self.jm_tips, '获取界面提示')
        return tips
