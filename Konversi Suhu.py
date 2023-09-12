# Meminta pilihan awal dari user
print("Masukkan Jenis Suhu dengan cara dibawah :")
print("Celcius (Masukkan C)")
print("Fahrenheit (Masukkan F)")
print("Kelvin (Masukkan K)")
print("Reamur (Masukkan R)")
suhu_awal = input("Masukkan Jenis Suhu Yang Akan Dikonversikan : ")

# Meminta pilihan hasil dari user
suhu_akhir = input("Masukkan Jenis Suhu Yang Akan Terkonversikan : ")

# Meminta berapa derajat suhu yang akan dikonversikan dari user
suhu = input("Masukkan Angka yang akan dikonversikan : ")

# Rumus dan Hasil Konversi yang berbeda-beda
if suhu_awal == "C" and suhu_akhir == "F":
  hasil_konversi_CF = (9/5) * int(suhu) + 32
  print (f"{suhu}°C setara dengan {hasil_konversi_CF}°F")
  
elif suhu_awal == "C" and suhu_akhir == "K":
  hasil_konversi_CK = int(suhu) + 273.15
  print (f"{suhu}°C setara dengan {hasil_konversi_CK}°K")
  
elif suhu_awal == "C" and suhu_akhir == "R":
  hasil_konversi_CR = 4 / 5 * int(suhu)
  print (f"{suhu}°C setara dengan {hasil_konversi_CR}°R")
  
elif suhu_awal == "F" and suhu_akhir == "C":
  hasil_konversi_FC = ((int(suhu) - 32) * 5 / 9)
  print (f"{suhu}°F setara dengan {hasil_konversi_FC}°C")
  
elif suhu_awal == "F" and suhu_akhir == "K":
  hasil_konversi_FK = ((int(suhu) + 459.67) * 5 / 9)
  print (f"{suhu}°F setara dengan {hasil_konversi_FK}°K")

elif suhu_awal == "F" and suhu_akhir == "R":
  hasil_konversi_FR = (int(suhu) + 459.67)
  print (f"{suhu}°F setara dengan {hasil_konversi_FR}°R")

elif suhu_awal == "K" and suhu_akhir == "C":
  hasil_konversi_KC = (int(suhu) - 273.15)
  print (f"{suhu}°K setara dengan {hasil_konversi_KC}°C")

elif suhu_awal == "K" and suhu_akhir == "F":
  hasil_konversi_KF = (int(suhu) * 9 / 5 - 459.67)
  print (f"{suhu}°K setara dengan {hasil_konversi_KF}°F")

elif suhu_awal == "K" and suhu_akhir == "R":
  hasil_konversi_KR = (4 / 5 * (int(suhu) - 273))
  print (f"{suhu}°K setara dengan {hasil_konversi_KR}°R")

elif suhu_awal == "R" and suhu_akhir == "C":
  hasil_konversi_FR = (int(suhu) / 0.8)
  print (f"{suhu}°R setara dengan {hasil_konversi_RC}°C")

elif suhu_awal == "R" and suhu_akhir == "F":
  hasil_konversi_RF = ((int(suhu) * 2,25) + 32)
  print (f"{suhu}°R setara dengan {hasil_konversi_RF}°F")

elif suhu_awal == "R" and suhu_akhir == "K":
  hasil_konversi_RK = ((int(suhu) / 0.8  ) + 273.15)
  print (f"{suhu}°R setara dengan {hasil_konversi_RK}°K")
  
else:
  print ("Input tidak valid")
