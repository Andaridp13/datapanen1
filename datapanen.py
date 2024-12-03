data_panen = {
    'lokasi1': {
        'nama_lokasi' : 'Kebun A',
        'hasil_panen' : {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi':'Kebun B',
        'hasil_panen':{
            'padi':1500,
            'jagung':900,
            'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi':'Kebun C',
        'hasil_panen':{
            'padi':1100,
            'jagung':750,
            'kedelai': 600
        }
    },
    'lokasi4': {
        'nama_lokasi':'Kebun D',
        'hasil_panen':{
            'padi':1300,
            'jagung':850,
            'kedelai': 550
        }
    },
    'lokasi5': {
        'nama_lokasi':'Kebun E',
        'hasil_panen':{
            'padi':1400,
            'jagung':950,
            'kedelai': 480
        }
    }   
}

# Tampilkan seluruh data
for lokasi, data in data_panen.items():
    print(f"Lokasi: {lokasi}")
    print(f"Nama Lokasi: {data['nama_lokasi']}")
    print("Hasil Panen:")
    for jenis, jumlah in data['hasil_panen'].items():
        print(f"  {jenis.capitalize()}: {jumlah}")
    print()

#Tampilkan jumlah hasil panen jagung dari lokasi2
print("Jumlah hasil panen jagung dari lokasi2:",
      data_panen['lokasi2']['hasil_panen']['jagung'])

#Tampilkan nama lokasi dari lokasi3
print("Nama lokasi dari lokasi3:", data_panen['lokasi3']['nama_lokasi'])

#Masukkan jumlah hasil panen padi dan kedelai setiap lokasi ke dalam variabel yang berbeda
hasil_padi = {lokasi: data['hasil_panen']['padi'] for lokasi, data in data_panen.items()}
hasil_kedelai = {lokasi: data['hasil_panen']['kedelai'] for lokasi, data in data_panen.items()}
print("Hasil panen padi:", hasil_padi)
print("Hasil panen kedelai:", hasil_kedelai)

#Buat percabangan untuk mengecek kondisi lokasi
for lokasi, data in data_panen.items():
    padi = data['hasil_panen']['padi']
    jagung = data['hasil_panen']['jagung']
    if padi > 1300 or jagung > 800:
        print(f"{data['nama_lokasi']} memerlukan perhatian khusus.")
    else:
        print(f"{data['nama_lokasi']} dalam kondisi baik.")

