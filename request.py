import requests
from datetime import datetime
import json

class Request:

    def __init__(self):
        self.start_date, self.end_date = self.get_current_time()
        self.request = self.get_request(self.start_date, self.end_date)
        self.price = self.parse_json(self.request)

    def __str__(self):
        return "TRANSACTION: start_date: {}, end_date: {}, price PVPC: {}".format(self.start_date, self.end_date, self.price)

    def get_current_time(self):

        # datetime object containing current date and time
        now = datetime.now()

        # dd/mm/YY H:M:S
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        day_month_year = now.strftime("%Y-%m-%d")
        hour_minute = now.strftime("%H:%M")

        if(now.hour == 00):
            hour_minus1 = "23"
        elif(now.hour != 00):
            hour_minus1 = str(now.hour -1)

        hour_minute_minus1 = hour_minus1 + ":" + str(now.minute)

        #print("day_month_year: ",day_month_year)
        #print("hour_minute", hour_minute)
        #print("hour_minute_minus1", hour_minute_minus1)

        start_date = "start_date=" + day_month_year + "T" + hour_minute_minus1
        end_date = "end_date=" + day_month_year + "T" + hour_minute

        return start_date, end_date

    def get_request(self, start_date, end_date):
        time_trunc = "time_trunc=hour"

        url = "https://apidatos.ree.es/es/datos/mercados/precios-mercados-tiempo-real?{}&{}&{}".format(start_date, end_date, time_trunc)
        #print("URL:",url)

        try:
            r = requests.get(url,timeout=3)
            r.raise_for_status()
        except requests.exceptions.HTTPError as errh:
            print ("Http Error:",errh)
        except requests.exceptions.ConnectionError as errc:
            print ("Error Connecting:",errc)
        except requests.exceptions.Timeout as errt:
            print ("Timeout Error:",errt)
        except requests.exceptions.RequestException as err:
            print ("OOps: Something Else",err)

        #response = requests.get(url)
        data = r.json()
        #print(data)
        return data

    def parse_json(self, json_file):
        for k1, v1 in json_file.items():
            if(k1 == 'included'):
                for i in v1:
                    a = False
                    for k3, v3 in i.items():
                        if((k3 == 'type') and (v3 == 'Precio mercado spot (€/MWh)')):
                            a = True
                        elif((k3 == 'type') and (v3 != 'Precio mercado spot (€/MWh)')):
                            a = False
                        if (a == True and k3 == 'attributes'):
                            for k4, v4 in v3.items():
                                if(k4 == 'values'):
                                    for j in v4:
                                        for k5, v5 in j.items():
                                            if(k5 == 'value'):
                                                return v5

def main():
    transaction1 = Request()
    print(transaction1)
    print(transaction1.price)
    

if __name__ == '__main__':
    main()