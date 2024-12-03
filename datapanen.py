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
