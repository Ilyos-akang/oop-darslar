# class Uy:
#     def __init__(self,raqam,rangi,hajmi,xonalar_soni=0,narx=0):
#         self.raqam=raqam
#         self.rangi=rangi
#         self.hajmi=hajmi
#         self.xonalar_soni=xonalar_soni
#         self.narx=narx

#     def info(self):
#         return f'{self.raqam}-uy {self.rangi} rangli {self.hajmi} sotix {self.xonalar_soni} ta xonasi bor, narxi {self.narx}'
    
# uy1=Uy("11","oq",4.5,5,9000)
# print(uy1.info())


        

# class Kutubxona:
    
#     def __init__(self, nom):
#         self.nom = nom
#         self.kitoblar = {}
    
#     def kitoblar_royxati(self):
#         if len(self.kitoblar):
#             for kitob_nomi, kitob_narxi in self.kitoblar.items():
#                 print(kitob_nomi, kitob_narxi)
#         else:
#             print("kitoblar mavjud emas!")
        
#     def kitob_qoshish(self, kitob_nomi, kitob_narxi):
#         self.kitoblar[kitob_nomi] = kitob_narxi
#         print(f"yangi: {kitob_nomi} kitobi muvofavqiyatli qo'shildi.")

# kutubxona_1 = Kutubxona("davlat 1-kutubxonasi")
# kutubxona_1.kitoblar_royxati()
# kutubxona_1.kitob_qoshish("O'tkan kunlar", 50000)
# kutubxona_1.kitob_qoshish("Yulduzli tunlar", 90000)
# kutubxona_1.kitob_qoshish("COC", 30000)
# kutubxona_1.kitoblar_royxati()
# kutubxona_2 = Kutubxona("kichik kutubxonacha")
# kutubxona_2.kitoblar_royxati()



# class Talaba:
#     def __init__(self,ism,yosh,univer_nomi="TATU"):
#         self.ism=ism
#         self.yosh=yosh
#         self.univer_nomi=univer_nomi

#     def ism_chiqar(self):
#         print( f'Talabaning ismi {self.ism}')
    
#     def yosh_chiqar(self):
#         print(f"Talabaning yoshi {self.yosh}")
    
#     def univesitet(self):
#         print(f" Universitet nomi {self.univer_nomi}")
    
#     def info(self):
#         print(f"Talabaning ismi :{self.ism}\n Talabaning yoshi: {self.yosh}\n Tahsil olayotgan muassasa:{self.univer_nomi}")
    

# talaba1=Talaba("toshmat",20,"INHA")
# talaba2=Talaba("Bobur",22,)
# talaba3=Talaba("ali",18,"Turin")

# talaba1.ism_chiqar()
# talaba1.yosh_chiqar()
# talaba1.univesitet()
# talaba1.info()




class Car:
    def __init__(self,model,narx,rangi,tezligi):
        self.model=model
        self.narx=narx
        self.rangi=rangi
        self.tezligi=tezligi

    def car_model(self):
        print(f"Mashina modeli {self.model}")

    def car_rang(self):
        print(f" mashina rangi {self.rangi}")

    def car_narxi(self):
        print(f"mashina narxi {self.narx}")

    def car_tezlik(self):
        print(f"mashina tezligi: {self.tezligi}")

    def info(self):
        print(f" Mashina modeli: {self.model},mashina rangi {self.rangi},mashina tezligi {self.tezligi}\nBu mashinani siz {self.narx}ga xarid qilishingiz mumkin")


car1=Car("nexia",'5000$',"oq",120)
car1.car_model()
car1.car_narxi()
car1.car_rang()
car1.car_tezlik()
car1.info()
        

car2=Car("malibu","25.000$","qora",220)
car2.info()