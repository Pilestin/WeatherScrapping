import time
from datetime import datetime 
import json
from app.metoffice import run_metoffice
from app.havadurumux import run_havadurumux
from app.weathercom import run_weathercom
from multiprocessing import Process, Pool


def get_data(file_name):
    
    with open(file_name, "r", encoding="utf-8") as file:
        data = json.load(file) 
        file.close()

    return data 


def combine_data():
    
    data_metoffice = get_data("result_data/hava_durumu_metoffice.json")
    data_weathercom = get_data("result_data/hava_durumu_weathercom.json") 
    data_havadurumux = get_data("result_data/hava_durumu_xnet.json")

    for i in range(1,82):
        city_code = str(i)
        try : 
            print("---------------------")
            print(city_code)
            metoffice_week_data = data_metoffice[city_code] if data_metoffice[city_code] else  None
            weathercom_week_data = data_weathercom[city_code] if data_weathercom[city_code] else  None
            havadurumux_week_data = data_havadurumux[city_code] if data_weathercom[city_code] else  None

            
        except KeyError:
            continue


if __name__ == "__main__":

   
    # start_time = time.time()  # Kodun başlangıç zamanını al
    # processes = [
    #     Process(target=run_metoffice),
    #     Process(target=run_weathercom),
    #     Process(target=run_havadurumux)
    # ]
    
    # # Her bir işlemi başlatma
    # for process in processes:
    #     process.start()

    # # Her bir işlemin tamamlanmasını bekler
    # for process in processes:
    #     process.join()
    
    
    # end_time = time.time()
    # elapsed_time = end_time - start_time  # Geçen süreyi hesapla
    # print(f"Kodun çalışma süresi: {elapsed_time} saniye")

    combine_data()