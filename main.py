import datetime

import requests
import mariadb
import sys
import uuid


def get_location(ipAdress):
    ip_address = str(ipAdress)
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "region_code": response.get("region_code"),
        "country": response.get("country_name"),
        "country_code": response.get("country_code"),
        "country_code_iso3": response.get("country_code_iso3"),
        "latitude": response.get("latitude"),
        "longitude": response.get("longitude"),
        "org": response.get("org")
    }
    return location_data


try:
    conn = mariadb.connect(
        user="root",
        password="passwort",
        host="127.0.0.1",
        port=3306,
        database="ip_mapper"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

cur = conn.cursor()


def insert_data(ipAdress, time, port, user, location_data):
    try:
        command = "INSERT INTO mapping (uuid, ip, timeStamp, creationTime, organisation, port, user, city, region, region_code, country, country_code, country_code_iso3, latitude, longitude) VALUES ({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {})".format(
            uuid.uuid4().hex, ipAdress, time, datetime.datetime.now(), location_data.get("org"), port, str(user),
            location_data.get("city"),
            location_data.get("region"), location_data.get("region_code"), location_data.get("country"),
            location_data.get("country_code"), location_data.get("country_code_iso3"), location_data.get("latitude"),
            location_data.get("longitude"))
        cur.execute(command)
    except mariadb.Error as e:
        print("Error: " + str(e))


file1 = open('auth.log', 'r')
count = 0

for line in file1:
    count += 1
    currentLine = line.strip()
    if currentLine.__contains__("Failed password") or currentLine.__contains__("Invalid user"):
        currentLineSplitted = currentLine.split()
        user = ""
        port = ""
        ipAdress = ""
        time = currentLineSplitted[0] + currentLineSplitted[1] + " - " + currentLineSplitted[2]
        if currentLine.__contains__("Failed password"):
            user = currentLineSplitted[10]
            port = currentLineSplitted[14]
            ipAdress = currentLineSplitted[12]
            location_data = get_location(ipAdress)
            insert_data(ipAdress, time, port, user, location_data)
        else:
            user = currentLineSplitted[7]
            port = currentLineSplitted[11]
            ipAdress = currentLineSplitted[9]
            location_data = get_location(ipAdress)

# Closing files
file1.close()
