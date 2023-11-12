import time

from collector.metoffice import run_metoffice
from collector.havadurumux import run_havadurumux
from collector.weathercom import run_weathercom
from util.data_handler import handle_data

from multiprocessing import Process




if __name__ == "__main__":

   
    start_time = time.time()  # Kodun başlangıç zamanını al
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

    handle_data()
    
    end_time = time.time()
    elapsed_time = end_time - start_time  # Geçen süreyi hesapla
    print(f"Kodun çalışma süresi: {elapsed_time} saniye")
    