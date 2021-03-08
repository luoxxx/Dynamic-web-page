'''
    爬取淘宝手机信息 手机型号 原价 现在价格 商店 月销
    反爬： 无法直接得到手机信息，动态页面
    方法： js逆向  使用selenium用户模拟 爬取数据
'''

from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from 动态网页爬取.save import taobaosql
from 动态网页爬取.CONSTANT import URL

browser = webdriver.Chrome()
browser.maximize_window()
for url in URL:
# url = 'https://uland.taobao.com/sem/tbsearch?refpid=mm_26632258_3504122_32538762&keyword=%E6%89%8B%E6%9C%BA&clk1=57a7282b8b117d6cb2d7f8bedc0c45ba&upsId=57a7282b8b117d6cb2d7f8bedc0c45ba&spm=a2e0b.20350158.search.1&pid=mm_26632258_3504122_32538762&union_lens=recoveryid%3A201_11.1.33.17_3780656_1615174981797%3Bprepvid%3A201_11.1.33.17_3780656_1615174981797'
    page = 0
    browser.get(url)
    browser.implicitly_wait(5)
    mobile = browser.find_elements_by_xpath('//ul[@class="pc-search-items-list"]/li')
    next_page = browser.find_element_by_xpath('//div[@id="J_pc-search-page-nav"]/span[3]')
    while page < 17:
        sql_conn = taobaosql.SavePhone()
        id = sql_conn.maxindex()+1
        try:
            for res in mobile:
                phone = res.find_element_by_xpath('./a/div[1]/span').text
                price = '￥'+res.find_element_by_xpath('./a/div[2]/span[2]').text
                original_price = res.find_element_by_xpath('./a/div[2]/span[3]').text
                shop = res.find_element_by_xpath('./a/div[3]/div').text
                monthly_sales = res.find_element_by_xpath('./a/div[4]/div[2]').text
                sql_conn.insert((id, phone, price, original_price, shop, monthly_sales))
                id += 1
            print("下载完成了%d" % id)
            next_page = WebDriverWait(browser, 60).until(lambda x: x.find_element(By.XPATH, '//div[@id="J_pc-search-page-nav"]/span[3]'))
            browser.execute_script('arguments[0].click()', next_page)
            page += 1
            mobile = browser.find_elements_by_xpath('//ul[@class="pc-search-items-list"]/li')
            next_page = browser.find_element_by_xpath('//div[@id="J_pc-search-page-nav"]/span[3]')
            time.sleep(10)
        except Exception as e:
            print("停止下载, {}".format(e))
            break
        finally:
            sql_conn.close_sql()
    currentPageUrl = browser.current_url
    print("当前页面的url是：", currentPageUrl)
time.sleep(1)
browser.quit()

# 手机型号 phone //ul/li/a/div[1]/span
# 售价   ￥+price   //ul/li/a/div[2]/span[2]
# 原价  original_price  //ul/li/a/div[2]/span[3]
# 商店  shop   //ul/li/a/div[3]/div
# 月销 monthly_sales  //ul/li/a/div[4]/div[2]