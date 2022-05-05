import dataconverter
from tkinter import *

FONT = '(family="Helvetica",size=36,weight="bold")'


class GUI():
    def __init__(self):

        self.data_dictionary = {f"name": '',
                                "sex": '',
                                "age": ''
                                "hobby: ''"}
        #Tkinker window config

        self.app_window = Tk()
        self.app_window.geometry("250x250")

        #Entry config
        self.ENT_name = Entry(self.app_window, font = FONT)

        self.ENT_name.grid(column = 1, row =0, padx = 5 , pady = 5)

        self.ENT_gender = Entry(self.app_window, font = FONT)

        self.ENT_gender.grid(column = 1, row = 1, padx = 5, pady = 5)

        self.ENT_age = Entry(self.app_window, font = FONT)

        self.ENT_age.grid(column = 1 , row = 2, padx = 5 , pady = 5)

        self.ENT_hobby = Entry(self.app_window, font = FONT)

        self.ENT_hobby.grid(column = 1, row = 3 , padx = 5 , pady = 5)

        # self.ENT

        #Text config

        self.TEX_name = Label(self.app_window, text = "Name:", font = FONT)

        self.TEX_name.grid(column=0, row = 0, padx = 5 , pady = 5)

        self.TEX_gender = Label(self.app_window, text ="Gender:", font = FONT)

        self.TEX_gender.grid(column = 0, row = 1, padx = 5, pady = 5)

        self.TEX_age = Label(self.app_window, text = "Age:", font = FONT)

        self.TEX_age.grid(column = 0, row = 2, padx = 5 , pady = 5)

        self.TEX_hobby = Label(self.app_window, text = "Hobby:", font = FONT)

        self.TEX_hobby.grid(column=0, row = 3, padx = 5 , pady = 5)

        #Buttons config

        self.Quit_butt = Button(text= "Quit", command = self.app_window.destroy, font = FONT)

        self.Quit_butt.grid(column = 0,row = 6, padx = 5 , pady = 5)

        self.Thankyou_butt = Button(text="Thank you!", command=self.gather_data, font=FONT)

        self.Thankyou_butt.grid(column=1, row=6, padx=5, pady=5)



        self.app_window.mainloop()

    def gather_data(self):
        name = self.ENT_name.get()

        male = self.ENT_gender.get()

        age = self.ENT_age.get()

        hobby = self.ENT_hobby.get()

        self.data_dictionary = {f"name": name,
                                "gender": male,
                                "age": age,
                                "hobby": hobby}
        send_data = dataconverter.ConvertInfo(data=self.data_dictionary)





