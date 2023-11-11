import requests
import bs4
import json 
import time 
from app.metoffice import run_metoffice
from app.havadurumux import run_havadurumux


if __name__ == "__main__":
    
    start_time = time.time()  # Kodun başlangıç zamanını al
    # run_metoffice()
    run_havadurumux()
    end_time = time.time()
    elapsed_time = end_time - start_time  # Geçen süreyi hesapla
    print(f"Kodun çalışma süresi: {elapsed_time} saniye")
