universite = ({"İngiltere": "Essex Üniversitesi\n" "Northumbria Üniversitesi\n" ,
               "İskoçya": "Edinburgh üniveristesi\n" ,
               "USA": "Stanford Üniversitesi"})

#for universite in universite:
 #   print(universite)


print(universite["İngiltere"])
print("--------")
print(universite.get("USA"))
print("--------")
print(universite.keys())
print("---------")
print(universite.values())
print("-------")


print(universite)
universite["İngiltere"] = "Oxford University"
universite["USA"] = "Harvard University"
print("Updated Dictionary = \n" , universite)
