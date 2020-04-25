from time import sleep

import requests
from os import system

inp = 0

while (inp != 6):
    print("--------------------\n"
          "1)Read all students \n"
          "2)Get student by id\n"
          "3)Add student\n"
          "4)Edit student\n"
          "5)Remove student\n"
          "6)Exit\n"
          "----------------")
    inp = int(input('Input:'))
    if inp == 1:
        url_server = "http://127.0.0.1:5000/students"
        r = requests.get(url=url_server)
        data = r.json()
        print("\n")
        for std in data:
            print("Student: Name=", std["name"], "Email=", std["email"], "year=", std["year"], "ID=", std["id"])
        input("\nAny key to continue")
    elif inp == 2:
        id = input("\ngive ID:")
        url_server = "http://127.0.0.1:5000/students/" + id
        r = requests.get(url=url_server)
        try:
            std = r.json()
            print("---------------------------\n", "Student: Name=", std["name"], "Email=", std["email"], "year=",
                  std["year"], "ID=", std["id"])
            input("\n\nEnter to continue")
        except:
            print("No Student Found :(")
            input()
    elif inp == 3:
        name = input("*)Give Name:")
        email = input("*)Give email:")
        year = int(input("*)Give year:"))
        url_server = "http://127.0.0.1:5000/students/"
        my_data = {
            "name": name,
            "email": email,
            "year": year
        }
        headers = {'content-type': 'application/json'}

        r = requests.post(url=url_server, json=my_data, headers=headers)
        if r.status_code == 201:
            print("\nStudent Created")
        else:
            print("Some Error Occurred")
        input("\nPress Enter to continue")

    elif inp == 4:
        id = input("*)Give ID:")
        name = input("*)Give Name(Enter to remain as before):")
        email = input("*)Give email(Enter to remain as before):")
        try:
            year = int(input("*)Give year(Enter below zero to not change year):"))
        except:
            year = -1

        url_server = "http://127.0.0.1:5000/students/" + id
        myda = {
            "name": name,
            "email": email,
            "year": year
        }
        headers = {'content-type': 'application/json'}

        r = requests.put(url=url_server, json=myda, headers=headers)
        if r.status_code == 200:
            print("\nUpdated Successfully")
        elif r.status_code == 404:
            print("\nNo student Found with this ID:", id)
        else:
            print("\nSome Error Occurred")
    elif inp == 5:
        id = input("Give ID:")

        url_server = "http://127.0.0.1:5000/students/" + id
        r = requests.delete(url=url_server)
        if r.status_code == 200:
            print("\nDeleted Successfully")
        elif r.status_code == 404:
            print("\nNo Student Found with this ID")
        else:
            print("Internal Error Occurred")
    elif inp == 6:
        system("cls")
        print("Addios")
        sleep(1)
        exit(0)
    else:
        print("Wrong Input Enter Again")
