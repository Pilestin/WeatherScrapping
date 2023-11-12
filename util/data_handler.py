import json
from datetime import datetime, timedelta
from util.mongo_operation import insert_data_to_mongo



def get_data(file_name):
    
    with open(file_name, "r", encoding="utf-8") as file:
        data = json.load(file) 
        file.close()

    return data 


def handle_data():
    """ 
        Bu fonksiyon 3 sitenin sonuçlarını bir obje olarak birleştirir.
        Bu objeyi kaydetmesi için insert_data_to_mongo fonksiyonuna gönderir.
    """
    
    data_metoffice = get_data("result_data/hava_durumu_metoffice.json")
    data_weathercom = get_data("result_data/hava_durumu_weathercom.json") 
    data_havadurumux = get_data("result_data/hava_durumu_xnet.json")

    
    for i in range(1,82):
        city_code = str(i)
        city_one_week_info = []
        print("---------------------")
        print("Şehir Kodu : ", city_code)
        
        try :
            metoffice_week_data = data_metoffice[city_code] if city_code in data_metoffice else {}
            weathercom_week_data = data_weathercom[city_code] if city_code in data_weathercom else {}
            havadurumux_week_data = data_havadurumux[city_code] if city_code in data_havadurumux else {}
            date = datetime.now()
            print("Tarih : ", date.strftime("%Y-%m-%d"))      
            
            for s in range(7):
                day = date.strftime("%Y-%m-%d")
                
                metoffice_week_data[day] = ["", ""] if day not in metoffice_week_data else metoffice_week_data[day]
                weathercom_week_data[day] = ["", ""] if day not in weathercom_week_data  else weathercom_week_data[day]
                havadurumux_week_data[day] = ["", ""] if day not in havadurumux_week_data else havadurumux_week_data[day]
                
                # if weathercom_week_data == {}:
                #     weathercom_week_data[day] = ["", ""]
                
                # if havadurumux_week_data == {}:
                #     havadurumux_week_data[day] = ["", ""]
                    
                obj = {
                    "provincial_plate" : city_code,
                    "date" : day, 
                    "weather" : {
                        "metoffice" : {
                            "up" : metoffice_week_data[day][0],
                            "down" : metoffice_week_data[day][1]
                        },
                        "weathercom" : {
                            "up" : weathercom_week_data[day][0],
                            "down" : weathercom_week_data[day][1]
                        },
                        "havadurumux" : {
                            "up" : havadurumux_week_data[day][0],
                            "down" : havadurumux_week_data[day][1]
                        }
                    }
                } 
                # print(obj)
                city_one_week_info.append(obj)
                date += timedelta(days=1)
            insert_data_to_mongo(city_one_week_info)
                
        except Exception as e:
            print("Hata : ", e)
