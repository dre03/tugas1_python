#pegawai_1
pegawai_1 = ('Ahmad','Islam', 4000000 ,2)
pegawai_2 = ('Alex','Kristen Protestan', 6000000, 5)
tujangan_jabatan = (20/100)
if (pegawai_1 [3] <= 2):
    tujangan_keluarga = 10/100 * pegawai_1[2]
elif (pegawai_1 [3] >2):
    tujangan_keluarga = 20/100 * pegawai_1[2]
else:
    tujangan_keluarga = 0
Gaji_kotor = pegawai_1 [2]+tujangan_jabatan * pegawai_1[2] + tujangan_keluarga
zakat_profesi = 0
if (pegawai_1[1] == "Islam" and Gaji_kotor >=6000000):
    zakat_profesi = 2.5/100*Gaji_kotor
gaji_bersih = Gaji_kotor-zakat_profesi

print ('\nSLIP GAJI PT. XYZ')
print ('------------------')
print ('Nama Pegawai\t\t:',pegawai_1[0])
print ('Agama\t\t\t:',pegawai_1[1])
print ('Jumlah Anak\t\t:',pegawai_1[3])
print ('Gaji Pokok\t\t: Rp.',pegawai_1[2])
print ('Tunjangan Jabatan\t: Rp.',tujangan_jabatan*pegawai_1[2])
print ('Tunjangan Keluarga\t: Rp.', tujangan_keluarga)
print ('Gaji Kotor\t\t: Rp.', Gaji_kotor) 
print ('Zakat Profesi\t\t: Rp.', zakat_profesi)
print ('Teke Home Pay\t\t: Rp.',gaji_bersih)

#pegawai_2

if (pegawai_2 [3] <= 2):
    tujangan_keluarga = 10/100 * pegawai_2[2]
elif (pegawai_2 [3] >2):
    tujangan_keluarga = 20/100 * pegawai_2[2]
else:
    tujangan_keluarga = 0
Gaji_kotor = (pegawai_2 [2]+tujangan_jabatan * pegawai_2[2] + tujangan_keluarga)
zakat_profesi = 0
if (pegawai_2[1] == "islam" and Gaji_kotor >=6000000):
    zakat_profesi = 2.5/100 * Gaji_kotor
gaji_bersih = Gaji_kotor-zakat_profesi

print ('\nSLIP GAJI PT. XYZ')
print ('------------------')
print ('Nama Pegawai\t\t:',pegawai_2[0])
print ('Agama\t\t\t:',pegawai_2[1])
print ('Jumlah Anak\t\t:',pegawai_2[3])
print ('Gaji Pokok\t\t: Rp.',pegawai_2[2])
print ('Tunjangan Jabatan\t: Rp.',tujangan_jabatan*pegawai_2[2])
print ('Tunjangan Keluarga\t: Rp.', tujangan_keluarga)
print ('Gaji Kotor\t\t: Rp.', Gaji_kotor) 
print ('Zakat Profesi\t\t: Rp.', zakat_profesi)
print ('Teke Home Pay\t\t: Rp.', gaji_bersih)