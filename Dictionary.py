universiteler = ({"İngiltere": "Essex Üniversitesi\n"
                  
                   "Northumbria Üniversitesi\n" ,
               "İskoçya": "Edinburgh üniveristesi\n" ,
               "USA": "Stanford Üniversitesi\n",
               "Türkiye": "Marmara Üniveristes\n"})

#for universite in universite:
 #   print(universite)

print(universiteler)
print("-----")

universite = universiteler.copy()
print(universite)
print("-------")

print(universiteler["İngiltere"])
print("--------")
print(universiteler["İskoçya"])
print("--------")
print(universiteler.get("USA"))
print("--------")
print(universiteler.keys())
print("---------")
print(universiteler.values())
print("-------")

for p in universiteler:
    print(universiteler[p])
print("---------")


universiteler["İngiltere"] = "Oxford University"
universiteler["USA"] = "Harvard University"
print("Updated Dictionary = \n" , universiteler)
print("----------")

universiteler["Rating"] = 4
print("Updated Dictionary = \n" , universiteler)
print("---------")

del universiteler["USA"]
print("Updated Dictionary = \n" , universiteler)
print("----------")

print(len(universiteler))
print("---------")

universiteler.clear()
print(universiteler)
print("-----")

sehirler = ({"İngiltere": "London"            "NewCastle" ,
             "İskoçya":   "Edinburgh"         "Aberdeen" ,
             "USA":       "Washington D.C."   "New York" ,
             "Türkiye":   "İstanbul"          "Ankara"})

print(sehirler)
print("-----")

sehir = sehirler.copy()
print(sehir)
print("-------")

print(sehirler["İngiltere"])
print("--------")
print(sehirler.get("Türkiye"))
print("--------")
print(sehirler.keys())
print("---------")
print(sehirler.values())
print("-------")

for p in sehirler:
    print(sehirler[p])
print("---------")


sehirler["İngiltere"] = "Oxford"
sehirler["USA"] = "Chicago"
print("Updated Dictionary = \n" , sehirler)
print("----------")

sehirler["Almanya"] = "Berlin" , "Münih" 
print("Updated Dictionary = \n" , sehirler)
print("---------")

del sehirler["USA"]
print("Updated Dictionary = \n" , sehirler)
print("----------")


print(len(sehirler))
print("---------")

sehirler.clear()
print(sehirler)
print("-----")





