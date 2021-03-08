from selenium import webdriver
from pybloom_live import BloomFilter
import time

# browser = webdriver.Chrome()
browser = webdriver.PhantomJS()
browser.get('https://www.amazon.cn/gp/bestsellers/wireless/665002051/ref=sv_cps_2')
# browser.maximize_window()  # 最大窗口化
# nowhandle = browser.current_window_handle  # 初始句柄
browser.implicitly_wait(3) # 隐性等待
while True:
    try:
        mobile = browser.find_elements_by_xpath('//div[@class="a-section a-spacing-none aok-relative"]')
        for m in mobile:
            rank = m.find_element_by_xpath('./div/span/span').text
            phone = m.find_element_by_xpath('./span/a/div').text
            print(rank, phone)
        next_page = browser.find_element_by_xpath("//li[@class='a-last']/a")
        browser.execute_script('arguments[0].click()', next_page)
        time.sleep(10)
    except:
        print('完结')
        break
browser.get('https://www.amazon.cn/gp/bestsellers/wireless/665002051/ref=sv_cps_2')
currentPageUrl = browser.current_url
print("当前页面的url是：", currentPageUrl)
time.sleep(1)
browser.quit()

# bulong = BloomFilter(capacity=1000)

# 手机 //div class=p13n-sc-truncate-desktop-type2 p13n-sc-truncated
#     //div class=p13n-sc-truncate-desktop-type2 p13n-sc-truncated
# //div[@class="a-section a-spacing-none aok-relative"]/div/span/span
# //div[@class="a-section a-spacing-none aok-relative"]/span/a/div/
