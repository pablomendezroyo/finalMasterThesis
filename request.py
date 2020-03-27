import requests
from datetime import datetime
import json



def get_current_time():

    # datetime object containing current date and time
    now = datetime.now()
    
    print("now =", now)

    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    day_month_year = now.strftime("%Y-%m-%d")
    hour_minute = now.strftime("%H:%M")

    if(now.hour == 00):
        hour_minus1 = "23"
    elif(now.hour != 00):
        hour_minus1 = str(now.hour -1)

    hour_minute_minus1 = hour_minus1 + ":" + str(now.minute)

    print("day_month_year: ",day_month_year)
    print("hour_minute", hour_minute)
    print("hour_minute_minus1", hour_minute_minus1)

    start_date = "start_date=" + day_month_year + "T" + hour_minute_minus1
    end_date = "end_date=" + day_month_year + "T" + hour_minute

    return start_date, end_date

def get_request():

    start_date, end_date = get_current_time()
    time_trunc = "time_trunc=hour"

    url = "https://apidatos.ree.es/es/datos/mercados/precios-mercados-tiempo-real?{}&{}&{}".format(start_date, end_date, time_trunc)
    print("URL:",url)

    response = requests.get(url)
    data = response.json()
    print(data)
    return data

def parse_json(dict_file):
    print("attemp to parse")
    
    for k1, v1 in dict_file.items():
        print(k1)
        if(k1 == 'included'):
            for i in v1:
                print(i)
                for k2, v2 in i.items():
                    if(k2 == 'attributes'):
                        for k3, v3 in v2.items():
                            print(k3)
                            if(k3 == 'values'):
                                for j in v3:
                                    print(j)

        
response = get_request()
parse_json(response)