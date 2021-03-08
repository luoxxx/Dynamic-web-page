'''
 爬取英雄联盟网站
 selenium爬取
 优点：直观 简单 直接模拟用户行为
 缺点：易识别 已崩溃 占资源 不容易做成可执行成勋
'''
from selenium import webdriver
import time

# 参数配置
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument("--disable-gpu")
url='http://www.op.gg/champion/soraka/statistics/support/matchup'
brower = webdriver.Chrome(options=options)

brower.get(url)
time.sleep(3)
res = brower.find_elements_by_xpath('//div[@class="champion-matchup-champion-list"]/div')
# print(res)
for r in res:
    print(r.get_attribute("data-champion-name"))

brower.quit()

