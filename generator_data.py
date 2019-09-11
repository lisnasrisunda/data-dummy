import random
import time

class my_dictionary(dict):
    #__init__ function
    def __init__(self):
        self = dict()

    # Function to add key:value
    def add(self, key, value):
        self[key] = value
    
#create data to csv
def createData(name,datas):
    f = open("data/"+str(name)+".csv","w+")

    # keys = datas[0].keys()
    # print(keys[0])
    pjg = len(datas[0].keys())
    num1=0
    num2=0
    for data in datas:
        num3=[]
        for key in datas[0].keys():
            if num1==0:
                if num2== pjg-1:
                    f.write(str(key))
                else:
                    f.write(str(key)+",")
            num2+=1
            num3.append(data.get(str(key)))
        if num1==0:
            f.write("\n")
        writeData(num3,f)
        num1+=1
    f.close

def writeData(listdata,f):
    i = 0
    for data in listdata:
        if i == len(listdata)-1:
            f.write(str(data)+"\n")
        else:
            f.write(str(data)+",")
        i +=1

#jamke = jam ke- dari jadwal (max. jam ke-6)
def createTimeSchedule(jamke):
    listTime = ["07:00","07:45","08:30","09:15","10:00","10:45","11:30"]
    time = listTime[jamke-1] + "-" + listTime[jamke]
    return time

#return random list of integer
def randomNumbers(jml):
    choices = list(range(jml))
    random.shuffle(choices)
    return choices

#jml = jumlah kategori yang dibuat(max 7)
def createKategoriPenilaian(jml):
    f_kategori = open("resources/kategori_penilaian.txt","r")
    listkategori = f_kategori.readlines()
    f_kategori.close()
    list_kategori = []
    i = 0
    for kategori in listkategori:
        dictionary = my_dictionary() 
        dictionary.add("id_kategori", i+1)
        dictionary.add("nama_kategori_penilaian", kategori.rstrip('\n'))
        list_kategori.append(dictionary)
        i +=1
        if i == jml:
            break

    return list_kategori

#for add spritual aspect at aspek_penilaian.txt, must add at the start txt
#for add sosial aspect at aspek_penilaian.txt, must add at the end txt
def createSikap():
    f = open("resources/aspek_penilaian.txt","r")
    fs = f.readlines()
    f.close()
    jenis = ["Spiritual","Sosial"]
    sosial = False
    list_sikap = []
    i = 0
    for sikap in fs:
        dictionary = my_dictionary()
        dictionary.add("id_sikap", i+1)
        if(sikap.rstrip('\n')=="Kepedulian"):
            sosial = True
        if(sosial):
            dictionary.add("jenis",jenis[1])
        else:
            dictionary.add("jenis",jenis[0])
        dictionary.add("aspek_penilaian",sikap.rstrip('\n'))
        list_sikap.append(dictionary)
        i +=1
    return list_sikap

#jml jumlah pertemuan setiap mapel
def createRPP(jml):
    f_mapel = open("resources/mapel.txt","r")
    listmapel = f_mapel.readlines()
    list_rpp = []
    i = 0
    for mapel in listmapel:
        for pertemuan in range(0,jml):
            dicti = my_dictionary()
            dicti.add("id_rpp",i+1)
            dicti.add("username","")
            dicti.add("pertemuan",pertemuan+1)
            dicti.add("nama_rpp","RPP "+mapel.rstrip('\n')+" - "+str(pertemuan+1))
            dicti.add("create_date","")
            dicti.add("update_date","")
            dicti.add("created_by","")
            dicti.add("updated_by","")
            list_rpp.append(dicti)
            i += 1
    f_mapel.close()
    return list_rpp

#jml jumlah siswa
def createMasukan(jml):
    f_masukan = open("resources/masukan.txt","r")
    list_masukan = f_masukan.readlines()
    f_masukan.close()
    ln = randomNumbers(len(list_masukan))
    l = []
    i = 0
    for id in range(0,jml):
        dicti = my_dictionary()
        dicti.add("id_masukan", id+1)
        dicti.add("username","")
        dicti.add("catatan",list_masukan[ln[i]].rstrip('\n'))
        l.append(dicti)
        i += 1
        if i == len(list_masukan):
            i = 0
    return l

def test():
    # sikap= createSikap()
    # createData("sikap",sikap)
    # rpp = createRPP(3)
    # createData("RPP",rpp)
    masukan = createMasukan(10)
    createData("Masukan",masukan)

test()