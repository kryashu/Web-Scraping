import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options,executable_path="C:\Users\kryas\Desktop\web scraping\chromedriver.exe")
url = "https://www.investing.com/equities/trending-stocks"
driver.get(url)

def get_trend_stock():
    dic=[]
    trend_stock = []
    for i in range(6):
       xpath =["/html/body/div[5]/section/div[7]/div/div[1]/div["+str(i+1)+"]/div/a","/html/body/div[5]/section/div[7]/div/div[1]/div["+str(i+1)+"]/div/div[1]/div","/html/body/div[5]/section/div[7]/div/div[1]/div["+str(i+1)+"]/div/div[1]/span[1]","/html/body/div[5]/section/div[7]/div/div[1]/div["+str(i+1)+"]/div/div[1]/span[2]"]
       dic.append(xpath)
    for xpath in dic: 
       res=[]
       for i in xpath:
          element = driver.find_element_by_xpath(i)
          pair=element.text
          res.append(pair)
       #print res
       trend_stock.append(res)
    return trend_stock

def get_trend_pop():
    trend_stock= []
    driver.get(url)
    for i in range(15):
        path = '#highcharts-0 > svg > g.highcharts-series-group > g.highcharts-series.highcharts-tracker > rect:nth-child('+str(i+1)+')'
        element = driver.find_element_by_css_selector(path)
        action = ActionChains(driver)
        action.move_to_element(element)
        action.perform()
        name = wait(driver, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'#highcharts-0 > div > span > div > p:nth-child(1) > i' ))).text
        popularity = wait(driver, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'#highcharts-0 > div > span > div > p:nth-child(2)' ))).text
        trend_stock.append({"name":name,"popularity":popularity})

def get_trend_sector():
    trend_stock= []
    for i in range(7):
        path = "#highcharts-2 > svg > g.highcharts-series-group > g:nth-child(1) > rect:nth-child("+str(i+1)+")"
        element = driver.find_element_by_css_selector(path)
        element = driver.find_element_by_css_selector(path)
        action = ActionChains(driver)
        action.move_to_element(element)
        action.perform()
        data = wait(driver, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'#highcharts-2 > div > span > div' ))).text
        data = map(str,data.split('\n'))
        trend_stock.append(data)

def get_trend_price():
    element = driver.find_element_by_css_selector("#filter_price")
    element.click()
    time.sleep(5)
    result = []
    for i in range(30):
        li = []
        for j in range(2,10):
            if j==2:
                tbody = driver.find_element_by_xpath('//*[@id="trendingInnerContent"]/table/tbody/tr['+str(i+1)+']/td['+str(j)+']/a')
                li.append(str(tbody.text))
            else:
                tbody = driver.find_element_by_xpath('//*[@id="trendingInnerContent"]/table/tbody/tr['+str(i+1)+']/td['+str(j)+']')
                li.append(str(tbody.text))
        result.append(li)
    return result
def get_trend_performance():
    element = driver.find_element_by_css_selector("#filter_performance")
    element.click()
    time.sleep(5)
    result = []    
    for i in range(30):
        li = []
        for j in range(2,9):
            if j==2:
                tbody = driver.find_element_by_xpath('/html/body/div[5]/section/div[7]/div/div[9]/table/tbody/tr['+str(i+1)+']/td['+str(j)+']/a')
                li.append(str(tbody.text))
            else:
                tbody = driver.find_element_by_xpath('/html/body/div[5]/section/div[7]/div/div[9]/table/tbody/tr['+str(i+1)+']/td['+str(j)+']')
                li.append(str(tbody.text))
        result.append(li)
    print result
    return result
def get_trend_fundamental():
    element = driver.find_element_by_css_selector("#filter_fundamental")
    element.click()
    time.sleep(5)
    result = []    
    for i in range(30):
        li = []
        for j in range(2,7):
            if j==2:
                tbody = driver.find_element_by_xpath('/html/body/div[5]/section/div[7]/div/div[9]/table/tbody/tr['+str(i+1)+']/td['+str(j)+']/a')
                li.append(str(tbody.text))
            else:
                tbody = driver.find_element_by_xpath('/html/body/div[5]/section/div[7]/div/div[9]/table/tbody/tr['+str(i+1)+']/td['+str(j)+']')
                li.append(str(tbody.text))
        result.append(li)
    print result
    return result
def get_trend_technical():
    element = driver.find_element_by_css_selector("#filter_technical")
    element.click()
    time.sleep(5)
    result = []    
    for i in range(30):
        li = []
        for j in range(2,7):
            if j==2:
                tbody = driver.find_element_by_xpath('/html/body/div[5]/section/div[7]/div/div[9]/table/tbody/tr['+str(i+1)+']/td['+str(j)+']/a')
                li.append(str(tbody.text))
            else:
                tbody = driver.find_element_by_xpath('/html/body/div[5]/section/div[7]/div/div[9]/table/tbody/tr['+str(i+1)+']/td['+str(j)+']')
                li.append(str(tbody.text))
        result.append(li)
    print result
    return result

trend_stock = get_trend_stock()
trend_stock_pop = get_trend_pop()
trend_stock_sector = get_trend_sector()
trend_stock_performance = get_trend_performance()
trend_stock_technical = get_trend_technical()
trend_stock_fundamental = get_trend_fundamental()
