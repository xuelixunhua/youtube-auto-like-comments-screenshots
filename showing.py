from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# ===添加Chrome配置，获得原本浏览器登录的账号
# 注：该user data只能供一台浏览器使用，如果有浏览器占用，则打开失败
chromeo = webdriver.ChromeOptions()
chromeo.add_argument(r"user-data-dir=C:\Users\dadi\AppData\Local\Google\Chrome\User Data")

# ===变量设置
chrome = webdriver.Chrome(options=chromeo)  # 打开浏览器

urls = open(r'C:\Users\dadi\Desktop\homework\show.txt').readlines()  # 读取链接

comments = 'I like your video'  # 评论

lable = 'show'  # 标签名


# ===工作
for url in urls:
    chrome.get(url)
    time.sleep(2)
    random_num = str(time.time())  # 截屏所用的时间戳

    # 点赞
    chrome.execute_script(
        "var elems1 = document.querySelector('#top-level-buttons > ytd-toggle-button-renderer:nth-child(1) > a').click()")

    # 向下滑
    js = "var q=document.documentElement.scrollTop=400"
    chrome.execute_script(js)

    # 评论
    element = WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.ID, 'simplebox-placeholder')))  # 等待
    time.sleep(1)
    try:
        element.send_keys(comments, Keys.CONTROL, Keys.ENTER)  # 发评论
    except:
        chrome.find_element_by_xpath('// *[ @ id = "contenteditable-root"]').send_keys(comments, Keys.CONTROL, Keys.ENTER)  # 不同的youtube有不同的链接

    time.sleep(2)

    # 截屏
    chrome.get_screenshot_as_file(r'C:\\Users\\dadi\\Desktop\\homework\\screen_shoot_save\\' + lable + random_num + '.png')

exit()
