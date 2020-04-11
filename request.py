import requests
from datetime import datetime
import json

class Transaction:

    def __init__(self, number):
        self.number = number
        
        self.start_date, self.end_date = self.get_current_time()
        self.request = self.get_request(self.start_date, self.end_date)
        self.price = self.parse_json(self.request)
        #self.transaction = [ self.number, self.request, self.price]
    def __str__(self):
        return "TRANSACTION: start_date: {}, end_date: {}, price PVPC: {}".format(self.start_date, self.end_date, self.price)


    def get_current_time(self):

        # datetime object containing current date and time
        now = datetime.now()

        #print("now =", now)

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

        #start_date, end_date = get_current_time()
        time_trunc = "time_trunc=hour"

        url = "https://apidatos.ree.es/es/datos/mercados/precios-mercados-tiempo-real?{}&{}&{}".format(start_date, end_date, time_trunc)
        #print("URL:",url)

        response = requests.get(url)
        data = response.json()
        #print(data)
        return data

    def parse_json(self, json_file):
        #print("attemp to parse")

        for k1, v1 in json_file.items():
            #print(k1)
            if(k1 == 'included'):
                for i in v1:
                    #print(i)
                    a = False
                    for k3, v3 in i.items():
                        if((k3 == 'type') and (v3 == 'Precio mercado spot (€/MWh)')):
                            #print(k3,v3)
                            a = True
                        elif((k3 == 'type') and (v3 != 'Precio mercado spot (€/MWh)')):
                            a = False
                        if (a == True and k3 == 'attributes'):
                            for k4, v4 in v3.items():
                                if(k4 == 'values'):
                                    #print(v4)
                                    for j in v4:
                                        for k5, v5 in j.items():
                                            if(k5 == 'value'):
                                                #self.items.append(v5)
                                                return v5

transaction1 = Transaction(1)

print(transaction1)



#response = get_request()
#parse_json(response)