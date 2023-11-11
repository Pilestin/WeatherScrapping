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

def cities_without_trchar():
    """
    Bu fonksiyon Türkiye'nin illerini türkçe karakter olmadan döndürür.
    """    
    
    plakalar = {}
    # iller listesi https://turzifer.com/web/turkiye-il-listesi/ adresinden alındı
    
# plakalar()