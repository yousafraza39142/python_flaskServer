from time import sleep

import requests
from os import system

inp = 0

while (inp != 6):
    system("cls")
    print(
        "--------------------\n1)Read all students \n2)Get student by id\n3)Add student\n4)Edit student\n5)Remove student\n6)Exit\n----------------")
    inp = int(input('Input:'))
    if (inp == 1):
        url_server = "http://127.0.0.1:5000/students"
        r = requests.get(url=url_server)
        data = r.json()
        for std in data:
            print("Student: Name=", std["name"], "Email=", std["email"], "year=", std["year"], "ID=", std["id"])
        input("Any key to continue")
    elif inp == 2:
        id = input("give ID:")
        url_server = "http://127.0.0.1:5000/students/" + id
        r = requests.get(url=url_server)
        try:
            std = r.json()
            print("---------------------------\n", "Student: Name=", std["name"], "Email=", std["email"], "year=",std["year"], "ID=", std["id"])
            input("\n\nEnter to continue")
        except:
            print("No Student")
            input()
    elif inp == 3:
        name = input("*)Give Name:")
        email = input("*)Give email:")
        year = int(input("*)Give year:"))
        url_server = "http://127.0.0.1:5000/students/post"
        myda = {
            "name": name,
            "email": email,
            "year": year
        }
        headers = {'content-type': 'application/json'}

        r = requests.get(url=url_server, json=myda, headers=headers)
        print("\n==>Student Added: Name=", name, "Email=", email, "year=",
              year, "ID=", id)

        input("\n\nPress Enter to continue")

    elif inp == 4:
        id = input("*)Give ID:")
        name = input("*)Give Name(Enter to remain as before):")
        email = input("*)Give email(Enter to remain as before):")
        try:
            year = int(input("*)Give year(Enter below zero to not change year):"))
        except:
            year = -1

        url_server = "http://127.0.0.1:5000/students/update/" + id
        myda = {
            "name": name,
            "email": email,
            "year": year
        }
        headers = {'content-type': 'application/json'}

        r = requests.get(url=url_server, json=myda, headers=headers)
        print(r.json())
    elif inp == 5:
        id = input("Give ID:")

        url_server = "http://127.0.0.1:5000/students/delete/" + id
        r = requests.get(url=url_server)
        print(r.json())
    elif inp == 6:
        system("cls")
        print("Addios")
        sleep(1)
        exit(0)
    else:
        print("Wrong Input Enter Again")
