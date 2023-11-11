import requests
import bs4
import json 
import time 
from util.helper import city_codes, cities_without_trchar, cities

url_metoffice = "https://www.metoffice.gov.uk/" 
# url_weathercom = "https://weather.com/tr-TR"
# url_havadurumux = "https://www.havadurumux.net"

def get_city_ref():
    """
    İlk kaynak için şehir ve referans bilgilerini alır.
    """
    obj = {}
    
    url = url_metoffice + "weather/world/turkey/list"
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    
    # Alfabetik olarak giden div ögelerini aldık
    all_content = soup.find_all("div", class_="link-group")
    # İçerisinde bulunan ögeler için sırasıyla işlem yapacağız
    for content in all_content:
        # Alfabetik olarak content için : 
        ul = content.find("ul")
        li = ul.find_all("li")
        # Şehirlerin bulunduğu li ögelerini aldık
        for area in li:
            city_in_page = area.find("a").text.strip()
            # Eğer bu sonuç gerçekten bir şehir ise, ilçe değilse
            if city_in_page.lower() in cities:
                # linki aldık ve objemizi oluşturduk
                city_ref = area.find("a")["href"]
                print(city_in_page, city_ref)
                # geçici objemizde bu veriyi sakladık
                obj[city_in_page] = city_ref
            
    return obj
    
def detail_city(obj):
    
    """
    Bu fonksiyon şehirlerin 1 haftalık hava durumunu bulur ve kaydeder.
    obj : şehir ismi(obj.key) ve linki(obj.value) içeren sözlük
    """

    # şehirlerin hava durumunu tutacağımız sözlük
    #  key =  şehir ismi (str)
    #  value =  object (dict)
    #           object.key = tarih (str) 
    #           object.value = [high, low] (list)
    
    result = {}
    sayac = 1 
    # her şehir için içinde bulunan referansı url olarak alıp işlem yapacağız
    for city in obj:
        
        city_ref = obj[city]
        url = url_metoffice + city_ref
        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.text, "html.parser")
        
        ul = soup.find("ul", id="dayNav")
        li = ul.find_all("li")
        
        # şehir için geçici olarak 7 günün hava durumunu tutacağımız sözlük
        one_week_weather = {}
        for day in li:
            # son günde durmaması için (veri yok) try-catch kullandık
            try:
                high = day.find("span", class_="tab-temp-high").text.strip().split("°")[0]
                low  = day.find("span", class_="tab-temp-low").text.strip().split("°")[0]
                # time bilgisini html içerikteki datetime ögesinden(attribute) alıyoruz
                #   ve sadece tarih bilgisini alıyoruz(T'den bölüp ilk elemanı alıyoruz) 
                time = day.find("time").attrs["datetime"].split("T")[0]
                
                one_week_weather[time] = [high, low]
                
            except AttributeError:
                continue 
        # her bir şehir için 7 gün tamamlandığında bu bilgileri sözlüğümüze ekliyoruz
        util_obj = city_codes() # util içerisinden aldığımız dictionary döndüren fonksiyon
        city_code = util_obj[city.lower()]
        # ex: util_obj["adana"] = "06" gibi
        result[city_code] = one_week_weather
        sayac += 1
        
        # if sayac == 3:
        #     break
        
    return result
    
def save_data(data):
    json_veri = json.dumps(data, ensure_ascii=False, indent=4)
    with open('result_data/hava_durumu_metoffice.json', 'w', encoding='utf-8') as dosya:
        dosya.write(json_veri)    

def run_metoffice():
    obj = get_city_ref()
    data = detail_city(obj)
    save_data(data)


