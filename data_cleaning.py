import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Buka file
data = pd.read_csv("movie_sample.csv")

#Menampilan baris dan kolom pada data
pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)

#Menhapus data tidakk representatif
data.drop(['color','language'],axis=1, inplace=True)

#File ini memiliki data dengan jumlah 99 baris dan 11 kolom, dimana setiap kolom menampilkan judul/nama dari data
#Dan pada case ini (data cleaning) akan mencari value yang hilang dan outliers pada setiap data

#Pertama, pisahkan antara data yang terdapat missing value dan outliers, sebelum itu dilakukan pengecekan pada setiap baris data
print(data.info()) #tentu saja, terdapat beberapa data yang memiliki baris yang janggal 
print(data.isnull().any()) #menentukan data yang memiliki missing value
print("\ntotal data hilang =",data.isnull().sum().sum(),"\n")#menjumlahkan semuaa missing value

#Mencari missing value pada data director_name
print('Mencari missing value : \n', data['director_name'].unique(), 
      '\nData missing value berjumlah : ', data['director_name'].isnull().sum(),'\n')
#Mengganti missing value pada data director name dengan value kosong
data['director_name'] = np.where(data['director_name'] != data['director_name' or 'Nan' or 'Null'],
                        ' ', data['director_name'])
print('\nData setelah missing value dihapus : \n',data['director_name'])

#Mengecek outliers pada data duration
print('\nData Durasi : \n', data['duration'].unique())
#Mengimplementasikan data ke dalam bloxplot
plt.boxplot(data['duration'])
if input("Tunjukkan Grafik Plot ?(y/n) ") == 'y':
    #menampilkan data dalam bentuk grafik
    plt.show()
else:
    pass
#Mengganti outliers pada data duration dengan value 0
data['duration'] = np.where(data['duration'] < 60, 0, data['duration'])
print('\nData duration setelah diperbaiki: \n', data['duration'],'\n ##Note : Data ini bisa diperbaiki setelah mengetahui data riilnya##')

#Mencari missing value pada data gross
pd.set_option('display.max_rows', None)
print('\nData gross :\n',data['gross'].unique, '\nJumlah data yang hilang : ', data['gross'].isnull().sum(),'\n')
#Mengganti missing value pada data gross dengan value nol
print('\nData gross setelah missing value diganti dengan nol : \n', data['gross'].fillna(0))

#Mencari missing value pada data genre
print('\nData Genre : \n', data['genres'], '\nJumlah data yang hilang : ',data['genres'].isnull().sum(),'\n')
#Mengganti missing value pada data genres dengan value General
print('\nData genre setelah missing value diperbaiki : \n', data['genres'].fillna('General').head(15))

#Mengecek outliers pada data title_year
print('\nData Title Years : ', data['title_year'].unique())
#Mengimplementasikan data ke dalam bloxplot dan mengatur skala sumbu y antara 90-3000
plt.boxplot(data['title_year']),plt.ylim([90,3000])
if input("Tunjukkan Grafik Plot ?(y/n) ") == 'y':
    #menampilkan data dalam bentuk grafik
    plt.show()
else:
    pass
#Mengganti value 202 menjadi 2002 dan value 205 menjadi 2005 pada data title_year
data['title_year'] = np.where(data['title_year'] == 202, 2002, data['title_year'])
data['title_year'] = np.where(data['title_year'] == 205, 2005, data['title_year']) 
print('\n Data title_year setelah diperbaiki : \n', data['title_year'])

#Mengecek format penulisan pada data country
print('\nData Country : ', data['country'].unique())
data['country'] = data['country'].str.upper() #mengubah semua isi data menjadi huruf besar
data['country'] = np.where(data['country'] == 'UNITED STATES', 'USA', data['country'])
print('\n Data Country setelah diperbaiki : \n', data['country'].unique())

#Mengecek outliers pada data budget
print('\nData Budget : \n', data['budget'].unique())
#Mengganti outliers pada data budget dengan value 0
print('Data budget setelah diperbaiki : \n',data['budget'].fillna(0))

#Mengecek outliers pada data imdb
print('\nData Imdb : \n', data['imdb_score'].unique())
#Mengimplementasikan data ke dalam bloxplot dan mengatur skala sumbu y antara -10 sampai 10
plt.boxplot(data['imdb_score']), plt.ylim([-10,10])
if input("Tunjukkan Grafik Plot ?(y/n) ") == 'y':
    #menampilkan data dalam bentuk grafik
    plt.show()
else:
    pass
#Mengubah nilai negatif menjadi positif pada data imdb 
data['imdb_score'] = np.where(data['imdb_score'] < 0, -1*data['imdb_score'], data['imdb_score'])
print('\n Data imdb setelah diperbaiki \n',data['imdb_score'].unique())

#Menampilkan semua hasil data setelah diperbaiki
print('\nData Akhir : \n', data.head(99))
if input('Tampilkan semua data?(y/n)') == 'y':
    pd.set_option('display.max_columns', None)
    print('Data Akhir : \n', data.head(99))
else:
    pass
input('\nTekan enter untuk mengakhiri')
