# IP-Mapper

Der IP-Mapper ist ein Python-Skript, das Informationen aus dem Linux-Protokoll "auth.log" ausliest und fehlgeschlagene Anmeldeversuche herausfiltert. Es extrahiert dann interessante Informationen wie die IP, den versuchten Port und den Benutzer. Die IP-Adresse wird dann mit der API von https://ipapi.co/ lokalisiert und alle Informationen werden dann in einer MariaDB-Datenbank gespeichert. Dadurch können schöne Statistiken erstellt werden.
Das Skript ist so konzipiert, dass es die API schont, indem es bereits vorhandene IP-Adressen in der Datenbank überprüft und prüft, ob ein Eintrag (zu einem bestimmten Zeitpunkt) bereits gespeichert wurde. Das bedeutet, dass das Skript als Cron-Job alle x Minuten/Stunden ausgeführt werden kann, ohne die API zu überlasten.

## Anforderungen
- Python 3.x
- mariadb-Bibliothek
- requests-Bibliothek

## Installation
1. Installieren Sie die erforderlichen Bibliotheken, indem Sie den folgenden Befehl ausführen:
```bash
pip install mariadb requests
```
2. Klonen Sie das Repository oder laden Sie das Skript herunter.
3. Stellen Sie sicher, dass MariaDB läuft und Sie die erforderlichen Anmeldeinformationen zur Verbindung mit der Datenbank haben.
4. Konfigurieren Sie die Datenbankverbindung im Skript.
5. Stellen Sie sicher, dass das Skript die erforderlichen Berechtigungen zum Lesen der auth.log-Datei hat.

## Grafana Dashboard
![image](https://user-images.githubusercontent.com/76694468/214429802-f930666f-9999-4762-bbcc-2da71420c856.png)


## Verwendung
1. Führen Sie das Skript aus, indem Sie den folgenden Befehl ausführen:
```bash
python main.py
```
2. Das Skript beginnt mit dem Lesen der Datei auth.log und dem Extrahieren der erforderlichen Informationen. 
3. Die extrahierten Informationen werden dann in der MariaDB-Datenbank gespeichert. 

## Hinweis 
Bitte stellen Sie sicher, dass Sie die erforderlichen Berechtigungen zum Lesen der Datei auth.log haben.
