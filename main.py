import csv
with open('fruits.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Nama buah'])
    writer.writerow([ " Apel"])
    writer.writerow([ " Salak"])
    writer.writerow([" Pisang "])
f = open('fruits.csv', 'r')
reader = csv.reader(f)
for row in reader:
    print (row)
f.close()
print ("===================================")
confirm = input ("Apakah anda ingin menambahkan data? y/n : ")
if confirm == "y" :
      loop = False  
fruits = []
data = 0
loop = True 
while loop :
      data=input("Masukkan data buah :")
      if(data=="=") :
       break
      fruits.append(data)
      print (fruits)
print("=======================================")
print ("hasil Tambahan data buah:")
with open ('fruits.csv','a', newline='') as file:
  reader = csv.writer(file)
  reader.writerow(fruits)
f = open('fruits.csv', 'r')
reader = csv.reader(f)
for row in reader:
    print (row)
f.close()
print ("====================================")
cari  = input ("Data yang ingin dicari:")
for x in range (len(fruits)):
    if (fruits[x]== cari):
      print ("ketemu")
      print ("Data ditemukan pada indeks:", x)
      break
    else :
      print("Data tidak ditemukan")
print("==================================")
pilihan = input("pop/remove?:")
if pilihan =="pop":
  fruits.pop()
  print (fruits)
elif pilihan == "remove":
  s=int(input ("masukkan indeks yang akan dihapus:"))
  fruits.remove(fruits[s])
  print (fruits)



