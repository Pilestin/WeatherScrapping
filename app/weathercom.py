import requests
import bs4
import json
import time
from datetime import datetime , timedelta
from util.helper import util_weathercom

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 10 günlük veriyi almak için kullanacağımız url
url_weathercom = "https://weather.com/tr-TR" 

# util_weathercom() fonksiyonu ile şehir isimlerinin listesini aldık 
# ex : Eskişehir, Eskişehir şeklinde tekrarlı şehir listesi 
def get_city_codes(input_data=util_weathercom):
    """
        Bu kod selenium kullanarak sitede inputları tek tek girer ve url içerisinden şehir kodlarını alır.
        Bunları bir liste olarak döndürür.
        Args:
            input_data (list, ) : ["Ankara, Ankara", . . . , "Eskişehir, Eskişehir"]
    """
    
    driver = webdriver.Chrome("util/driver/chromedriver.exe")
    driver.get("https://weather.com/tr-TR/")
    wait = WebDriverWait(driver, 10)
    city_urls = {}
    
    for input in input_data:
        try:
            # input kutusunu al
            search_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "LocationSearch_input")))
            # input kutusuna şehir ismini yaz
            search_box.send_keys(input)
            driver.implicitly_wait(2)
            # sitedeki sonuçları al
            buttons = driver.find_elements(By.CLASS_NAME , "SearchedLocations--ListboxOption--3uuhH")
            # ilk sonucu al (doğru olan eşleşme bu)
            driver.implicitly_wait(2)
            buttons[0].send_keys(Keys.ENTER)
            
            wait.until(lambda driver: driver.current_url != "https://weather.com/tr-TR/")
            
             # url içerisinden şehir id'sini al 
            now_url = driver.current_url.split("/")[-1]
            city_name = input.split(",")[0] 
            city_urls[city_name] = now_url
            driver.implicitly_wait(1)
            search_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "LocationSearch_input")))
            search_box.clear()
        except Exception as e:
            print("Hata oluştu : ")
            continue

        finally:
            print("bitti")
    
    return city_urls

def save_links(city_urls):
    """ 
        Bu fonksiyon selenium tarafından çekilen şehir url'lerini json olarak kaydeder.
        Böylelikle her defasında selenium çalıştırmadan bu verileri kullanabiliriz.
    """
    
    file_name = "result_data/links_weathercom.json"
    json_data = json.dumps(city_urls, indent=4, ensure_ascii=False)
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(json_data)
        file.close()

def get_saved_links(file_name="result_data/links_weathercom.json"):
    """ 
        Bu fonksiyon daha önceden kaydedilen şehir url'lerini json olarak okur.
    """
    with open(file_name, "r", encoding="utf-8") as file:
        links = json.load(file)
        file.close()
    return links

def get_weather(links):
    """ 
        Bu fonksiyon verilen şehir url'lerini kullanarak hava durumu verilerini çeker.
    """
    data = {}
    for num, i in enumerate(links, 1):
        
        count = 0
        
        
        print(num, i , links[i])
        
        # yeni url'imiz şehir kodu ile birlikte oluşacak
        url = url_weathercom + "/weather/tenday/l/" + links[i]
        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.text, "html.parser") 
        # 10 günlük hava durumu için tablo içerisindeki verileri al
        rows = soup.find_all("div", class_="DetailsSummary--temperature--1kVVp")

        # site içerisinde gün bilgisi uygun değil, bu yüzden el ile yapıldı
        day = datetime.now()
        
        # bir haftalık veriyi tutacağımız sözlük
        one_week_weather = {}
        # satırlar arasında dolaş
        for row in rows:
            if count == 7:
                break
            
            high = row.find("span", class_="DetailsSummary--highTempValue--3PjlX").text.split("°")[0]
            low  = row.find("span", class_="DetailsSummary--lowTempValue--2tesQ").text.split("°")[0]
            
            print(day.strftime("%Y-%m-%d") , high, low)
            one_week_weather[day.strftime("%Y-%m-%d")] = [high, low]
            count+= 1 
            day += timedelta(days=1)
        
        data[num] = one_week_weather
        
    return data    


def save_data(data, file_name="hava_durumu_weathercom.json"):
    """ 
        Bu fonksiyon verilen datayı json olarak kaydeder.
    """
    json_data = json.dumps(data, indent=4, ensure_ascii=False)
    file_name = "result_data/" + file_name
    with open( file_name , "w", encoding="utf-8") as file:
        file.write(json_data)
        file.close()


def run_weathercom():
    """ 
        weather.com sitesi için çalıştırılacak fonksiyon
    """
    
     # İstediğiniz şehirleri ekleyin
    input_data = util_weathercom()
    # city_urls = get_city_codes(input_data)
    # save_links(city_urls)
    links = get_saved_links()
    data = get_weather(links) 
    save_data(data)
    
    print("weather.com bitti")
    # return data