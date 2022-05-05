import tkinter.messagebox

import requests
from tkinter import messagebox
class ConvertInfo():
    def __init__(self,data):
        print("It worked")
        print(data)

        try:
            self.get_name_infos(data)
            self.get_hobby_infos(data)
            self.create_note(data)
        except:
            tkinter.messagebox.showerror("Error", "You didn't pass all information or you didn't have provided API keys")




    def get_name_infos(self,data):

        Api_Key_Name_Info = 'Api key from parser name'


        n_d = requests.get(f"https://api.parser.name/?api_key={Api_Key_Name_Info}&endpoint=parse&name={data['name']}")


        self.name = n_d.json()['data'][0]['name']['firstname']['name']

        self.country = n_d.json()['data'][0]['country']['name']

        self.frequency = n_d.json()['data'][0]['name']['firstname']['country_frequency']

        self.currency = n_d.json()['data'][0]['country']['currency']

        self.language = n_d.json()['data'][0]['country']['primary_language']




    def get_hobby_infos(self,data):
        # Hobbys Infos
        Hobby_API_KEY = "Api key from newscatchapi"

        hb = {f"x-api-key": Hobby_API_KEY}

        params = {f"q": data["hobby"],
                  "lang": 'en'}

        h_d = requests.get("https://api.newscatcherapi.com/v2/search", headers=hb, params = params)



        expect = h_d.json()["articles"]

        self.news_headlines = []

        self.news_links = []

        self.news_contens = []

        for n in range(0,2):
            self.news_headlines.append(expect[n]['title'])

            self.news_links.append(expect[n]['link'])

            self.news_contens.append(expect[n]['summary'])

    def create_note(self,data):
        with open("Note.txt", "w") as file:

            file.write(f"Name: {data['name']}\nGender: {data['gender']}\nCountry: {self.country}\n"
                       f"Propably language: {self.language}\nName frequency in country: {self.frequency}\n"
                       f"Currency: {self.currency}\n")

        with open("Note.txt", "a") as file:


            file.writelines(f"May be interested in: {self.news_headlines[0]} \nWhat is that about: {self.news_contens[0]} \n"
                       f"Links: {self.news_links[0]}\n")
            file.writelines(
                f"May be interested in: {self.news_headlines[1]} \nWhat is that about: {self.news_contens[1]} \n"
                f"Links: {self.news_links[1]}\n")
