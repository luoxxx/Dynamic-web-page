'''
 selenium爬取
 优点：直观 简单 直接模拟用户行为
 缺点：易识别 易崩溃 占资源 不容易做成可执行成勋
'''

易识别：
options = webdriver.ChromeOptions()                  # 创建一个配置对象
# options.add_argument('--headless')                     # 开启无界面模式
# options.add_argument("--disable-gpu")                  # 禁用gpu
# options.add_argument('--user-agent=Mozilla/5.0 HAHA')  # 配置对象添加替换User-Agent的命令
# options.add_argument('--window-size=1366,768')         # 设置浏览器分辨率（窗口大小）
# options.add_argument('--start-maximized')              # 最大化运行（全屏窗口）,不设置，取元素会报错
# options.add_argument('--disable-infobars')             # 禁用浏览器正在被自动化程序控制的提示
# options.add_experimental_option('')                    # 防止识别
# options.add_argument('--incognito')                    # 隐身模式（无痕模式）
# options.add_argument('--disable-javascript')           # 禁用javascript
driver = webdriver.Chrome(chrome_options=options)   # 实例化带有配置的driver对象


点击
driver.click()
driver.execute_script('arguments[0].click()',browser.find_element_by_id("isStudentDan") )

延迟
1 time.sleep()
2 显性等待
from selenium.webdriver.support.wait import WebDriverWait
    WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(locator))
    WebDriverWait(driver, 10).until(lambda x : x.find_element_by_id("id"))
from seleninum.webdriver.support import ui
    wait = ui.WebDriverWait(browser,wait_time)
    wait.until()

3 driver.implicitly_wait(10)   # 隐性等待，最长等10秒


鼠标操作
from seleninum.webdriver.common.action_chains import ActionChains
链式操作
browser = webdriver.Chrome()
action = ActionChains(browser)
action.() //点击，悬停等操作
action.perform()
移动操作
browser = webdriver.Chrome()
action = ActionChains(browser)
action.move_by_offset(x,y) 坐标移动
action.perform()

