import json
import requests

harga = requests.get('https://jibs.my.id/api/harga_komoditas')
hargaSuccess = harga.json()

def Main() :
    BahanPokok = ['Daging Ayam', 'Beras', 'Bawang Merah', 'Cabai Merah']
    for i in BahanPokok :
        print(i)

def All(name) :
    data = hargaSuccess['national_commodity_price']
    for i in data['Daging Ayam']:
        for j in data['Beras']:
            for k in data['Bawang Merah'] :
                for l in data['Cabai Merah'] :
                    if name.title() == i['name'] and name.title() == j['name'] and name.title() == k['name'] and name.title() == l['name'] :
                        print("Nama Provinsi\t\t:", i['name'].title())
                        print("Harga Daging Ayam\t:", i['display'])
                        print("Harga Beras\t\t:", j['display'])
                        print("Harga Bawang Merah\t:", k['display'])
                        print("Harga Cabai Merah\t:", l['display'])
    else :
        print("Data tidak ditemukan")
  

name = input()
All(name)