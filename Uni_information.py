# Yazım biçimi (Naming convention) : snake_case tercih edilir. Çünkü: python' ın resmi sitil rehberi PEP 8 tarafından önerilir. 
universities = [
    {   
        "country": "England",
        "university_name": "Essex University",
        "course": "Artificial Intelligence",
        "year": "3"
    },
    {
        "country": "England",
        "university_name": "Exeter University",
        "course": "Art",
        "year": "4"
    },
    {
        "country": "England",
        "university_name": "Oxford University",
        "course": "Computer Science",
        "year": "3",
    },
    {
        "country": "England",
        "university_name": "Northumbria University",
        "course": "Biology",
        "year": "4"
    },
    {
        "country": "Zürich",
        "university_name": "ETH Zürih",
        "course": "Civl Engineer",
        "year": "4"
    },
    {
        "country": "China",
        "university_name": "Beijing University",
        "course": "Architecture",
        "year": "5"
    }
]
print("")
print("Country    University Name     Course     Year")
print("-----------------------------------")

for university in universities:
    print(university["country"], university["university_name"], university["course"], university["year"])
