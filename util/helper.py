import requests
import bs4


# iller listesi https://turzifer.com/web/turkiye-il-listesi/ adresinden alındı.
cities = ["adana", "adiyaman", "afyonkarahisar", "agri", "amasya", "ankara", "antalya", "artvin", "aydin", "balikesir", "bilecik", "bingol", "bitlis", "bolu", "burdur", "bursa", "canakkale", "cankiri", "corum", "denizli", "diyarbakir", "edirne", "elazig", "erzincan", "erzurum", "eskisehir", "gaziantep", "giresun", "gumushane", "hakkari", "hatay", "isparta", "mersin", "istanbul", "izmir", "kars", "kastamonu", "kayseri", "kirklareli", "kirsehir", "kocaeli", "konya", "kutahya", "malatya", "manisa", "kahramanmaras", "mardin", "mugla", "mus", "nevsehir", "nigde", "ordu", "rize", "sakarya", "samsun", "siirt", "sinop", "sivas", "tekirdag", "tokat", "trabzon", "tunceli", "sanliurfa", "usak", "van", "yozgat", "zonguldak", "aksaray", "bayburt", "karaman", "kirikkale", "batman", "sirnak", "bartin", "ardahan", "igdir", "yalova", "karabuk", "kilis", "osmaniye", "duzce"]

def city_codes():
    """
    Bu fonksiyon Türkiye'nin illerini ve plaka kodlarını bir sözlük olarak döndürür.
    Ayrıca plakalar.txt dosyasına da kaydeder.
    """    
    
    # list comprehensive ile plaka kodlarını oluşturuyoruz.
    nums = [ x for x in range(1,82) ]
    
    # plakalar zip edildi ve dict yapısına dönüştürüldü.
    obj = dict(zip(cities,nums))
    
    # verileri dosyaya kaydet (plakalar.txt)
    with open("result_data/plakalar.txt", "w") as f:
        for city, code in obj.items():
            f.write(str(code) + " : " + city + "\n")

        f.close()
    
    return obj

def cities_with_trchar():
    """
    Bu fonksiyon Türkiye'nin illerini Türkçe karakterleri ile birlikte ve ilk harfi büyük olarak döndürür.
    weather.com sitesindeki şehirlerin isimleri bu şekildedir.
    """    
    tr_city = ["Adana", "Adıyaman", "Afyonkarahisar", "Ağrı", "Amasya", "Ankara", "Antalya", "Artvin", "Aydın", "Balıkesir", "Bilecik", "Bingöl", "Bitlis", "Bolu", "Burdur", "Bursa", "Çanakkale", "Çankırı", "Çorum", "Denizli", "Diyarbakır", "Edirne", "Elazığ", "Erzincan", "Erzurum", "Eskişehir", "Gaziantep", "Giresun", "Gümüşhane", "Hakkari", "Hatay", "Isparta", "Mersin", "İstanbul", "İzmir", "Kars", "Kastamonu", "Kayseri", "Kırklareli", "Kırşehir", "Kocaeli", "Konya", "Kütahya", "Malatya", "Manisa", "Kahramanmaraş", "Mardin", "Muğla", "Muş", "Nevşehir", "Niğde", "Ordu", "Rize", "Sakarya", "Samsun", "Siirt", "Sinop", "Sivas", "Tekirdağ", "Tokat", "Trabzon", "Tunceli", "Şanlıurfa", "Uşak", "Van", "Yozgat", "Zonguldak", "Aksaray", "Bayburt", "Karaman", "Kırıkkale", "Batman", "Şırnak", "Bartın", "Ardahan", "Iğdır", "Yalova", "Karabük", "Kilis", "Osmaniye", "Düzce"]
    # iller listesi https://turzifer.com/web/turkiye-il-listesi/ adresinden alındı
    return tr_city
    
    
def util_weathercom():
    """ 
    Bu fonksiyon yukarıdaki fonksiyondan aldığı listeyi weather.com sitesinde arama formatına uyarlar 
    ex : Eskişehir ->  Eskişehir, Eskişehir
    """
    format_cities = [f"{i}, {i}" for i in cities_with_trchar() ]
    
    return format_cities

