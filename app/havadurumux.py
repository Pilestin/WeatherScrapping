import requests
import bs4
import json
from datetime import datetime
from util.helper import cities,  city_codes
# Türkçe ay ve gün isimlerini ayarla
import locale
locale.setlocale(locale.LC_TIME, 'tr_TR')

url_havadurumux = "https://www.havadurumux.net" 

def get_weather():
    """ 
        Util içerisinden alınan şehir listesinin her ögesi için url düzenleyip şehirlere göre hava durumunu alır.
    """
    result = {}
    
    # her bir şehir için işlem yapacağız
    for city in cities:
        try:
            # url'i şehre göre oluştur ve gerekli bilgileri bul
            url = url_havadurumux + "/" + city + "-hava-durumu"
            response = requests.get(url) 
            soup = bs4.BeautifulSoup(response.text, "html.parser")
            table = soup.find("table" , id="hor-minimalist-a")
            tbody = table.find("tbody")
            tr = tbody.find_all("tr")
            
            counter = 0
            # 1 hhaftalık hava durumunu tutacağımız sözlük
            one_week_weather = {}
            for row in tr:
                # eğer 7 günlük hava durumu alındıysa döngüden çık
                if counter == 7:
                    break 
                # tarih, yüksek ve düşük sıcaklığı al
                # "17 Kasım 2023, Cuma" ---> 2023-11-17 00:00:00
                date = row.contents[0].text
                format_date = datetime.strptime(date, "%d %B %Y, %A")
                high = row.contents[2].text.split("°")[0]
                low  = row.contents[3].text.split("°")[0]
                
                one_week_weather[format_date.strftime("%Y-%m-%d")] = [high, low]
                
                counter += 1
                        
            # her bir şehir için 7 gün tamamlandığında bu bilgileri sözlüğümüze ekliyoruz
            util_obj = city_codes() # util içerisinden aldığımız dictionary döndüren fonksiyon
            city_code = util_obj[city.lower()]
            # ex: util_obj["adana"] = "06" gibi
            result[city_code] = one_week_weather
                
        except AttributeError:
            print("Hata oluştu : attribute error")
            continue
        except Exception as e:
            print("Hata oluştu : ", e)
            continue
        
    return result    
        
def save_data(data):
    """ 
        Bu fonksiyon verilen datayı json olarak kaydeder.
    """
    json_veri = json.dumps(data, ensure_ascii=False, indent=4)
    with open('result_data/hava_durumu_xnet.json', 'w', encoding='utf-8') as dosya:
        dosya.write(json_veri) 


def run_havadurumux():
    """ 
        havadurumux.com sitesi için çalıştırılacak fonksiyon
    """
    data = get_weather()
    save_data(data)
    
    print("havadurumux bitti")
    # return data
