sehirler =["Munich", "Dortmund",  "Istanbul", "London", "Paris"]
print(sehirler)
print("-----")
# sehirler = "Munich"
# print(sehirler[1])
# print(sehirler[0])
# print(sehirler[2])
# print(sehirler[3])
# print(sehirler[4])
sehirler.insert(1,"Tokyo")
sehirler.insert(0, "Berlin")
sehirler.insert(2, "Chicago")
sehirler.insert(4, "New York")
print(sehirler)
print("---------")

sehirler.append("Roma, Varsova")
print(sehirler)
print("--------")

sehirler.remove("Istanbul")
print(sehirler)
print("-----")

sehirler.sort()
print(sehirler)
print("------")

sehirler.reverse()
print(sehirler)
print("------")

Ulkeler =["Almanya", "İspanya", "Fransa", "İngiltere", "İskoçya"]

sehirler.extend(Ulkeler)
print(sehirler)
print("--------")

sehirler =["Munich", "Dortmund",  "Istanbul", "London", "Paris", "Dortmund"]
sehirler.copy()
print(sehirler)
print("------")


sehirler.clear()
print(sehirler)



#for full_name in sehirler:
   # print(full_name)

print("-----------")
sayilar = [1, 10, 15, 26, 37]


sayilar.insert(1,5)
sayilar.insert(1,6)
sayilar.insert(2,13)
sayilar.insert(4,30)
print(sayilar)
print("---------")

sayilar.append("38, 40")
print(sayilar)
print("--------")

sehirler.reverse()
print(sehirler)
print("------")

Ulkeler =["Almanya", "İspanya", "Fransa", "İngiltere", "İskoçya"]

sayilar.extend(Ulkeler)
print(sayilar)
print("--------")

sayilar =["1, 10, 15, 26, 37"]
sayilar.copy()
print(sayilar)
print("------")

sayilar.clear()
print(sayilar)