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
3. Erstellen Sie das Datenbank Schema.
```sql
CREATE DATABASE IF NOT EXISTS `ip_mapper`;
USE `ip_mapper`;

CREATE TABLE IF NOT EXISTS `mapping` (
  `uuid` varchar(255) NOT NULL DEFAULT '',
  `ip` varchar(50) DEFAULT NULL,
  `timeStamp` varchar(255) DEFAULT NULL,
  `creationTime` varchar(255) DEFAULT NULL,
  `organisation` varchar(255) DEFAULT NULL,
  `port` int(11) DEFAULT NULL,
  `user` varchar(255) DEFAULT NULL,
  `city` varchar(255) DEFAULT NULL,
  `region` varchar(255) DEFAULT NULL,
  `region_code` varchar(255) DEFAULT NULL,
  `country` varchar(255) DEFAULT NULL,
  `country_code` varchar(255) DEFAULT NULL,
  `country_code_iso3` varchar(255) DEFAULT NULL,
  `latitude` float DEFAULT NULL,
  `longitude` float DEFAULT NULL,
  PRIMARY KEY (`uuid`)
)
```
4. Bei Bedarf können Sie einige Testadaten einfügen.
```sql
INSERT INTO `mapping` (`uuid`, `ip`, `timeStamp`, `creationTime`, `organisation`, `port`, `user`, `city`, `region`, `region_code`, `country`, `country_code`, `country_code_iso3`, `latitude`, `longitude`) VALUES ('0dafdc2024934e20a3d11d6f2af8b1d7', 'xx.xxx.xx.xx', 'Jan22 - 17:24:47', '2023-01-24 21:42:17.010315', 'Novotelecom Ltd', 58368, 'Ubnt', 'Novosibirsk', 'Novosibirsk Oblast', 'NVS', 'Russia', 'RU', 'RUS', 54.9022, 83.0335);
INSERT INTO `mapping` (`uuid`, `ip`, `timeStamp`, `creationTime`, `organisation`, `port`, `user`, `city`, `region`, `region_code`, `country`, `country_code`, `country_code_iso3`, `latitude`, `longitude`) VALUES ('0777812a31a749bda830380b92281f38', 'xxx.xx.xxx.xxx', 'Jan22 - 09:45:04', '2023-01-24 21:42:07.575596', 'Flyservers S.A.', 24478, 'Debian', 'Moscow', 'Moscow', 'MOW', 'Russia', 'RU', 'RUS', 55.7483, 37.6171);
INSERT INTO `mapping` (`uuid`, `ip`, `timeStamp`, `creationTime`, `organisation`, `port`, `user`, `city`, `region`, `region_code`, `country`, `country_code`, `country_code_iso3`, `latitude`, `longitude`) VALUES ('18deb65ea43f4c179fb5ac1757a35ee0', 'xxx.xxx.xx.xx', 'Jan22 - 08:25:01', '2023-01-24 21:42:06.275201', 'Digicel Trinidad and Tobago Ltd.', 37479, 'Guest', 'Port of Spain', 'Port of Spain', 'POS', 'Trinidad and Tobago', 'TT', 'TTO', 10.65, -61.5167);
INSERT INTO `mapping` (`uuid`, `ip`, `timeStamp`, `creationTime`, `organisation`, `port`, `user`, `city`, `region`, `region_code`, `country`, `country_code`, `country_code_iso3`, `latitude`, `longitude`) VALUES ('1ff91b7b1fb74f94bb64394e17cb634b', 'xxx.xxx.xxx.xxx', 'Jan22 - 07:13:13', '2023-01-24 18:54:29.977619', 'Bharti Airtel Ltd., Telemedia Services', 52412, 'Guest', 'Coimbatore', 'Tamil Nadu', 'TN', 'India', 'IN', 'IND', 11.0142, 76.9941);
INSERT INTO `mapping` (`uuid`, `ip`, `timeStamp`, `creationTime`, `organisation`, `port`, `user`, `city`, `region`, `region_code`, `country`, `country_code`, `country_code_iso3`, `latitude`, `longitude`) VALUES ('2e5a0617e3d0470784c849b810fea387', 'xx.xxx.xxx.xx', 'Jan22 - 16:12:17', '2023-01-24 21:42:15.766084', 'Link3 Technologies Ltd.', 58740, 'Blank', 'Dhaka', 'Dhaka Division', 'C', 'Bangladesh', 'BD', 'BGD', 23.7272, 90.4093);
INSERT INTO `mapping` (`uuid`, `ip`, `timeStamp`, `creationTime`, `organisation`, `port`, `user`, `city`, `region`, `region_code`, `country`, `country_code`, `country_code_iso3`, `latitude`, `longitude`) VALUES ('2a135f673def4ed286c268ccc5a5e8f8', 'xxx.xxx.xxx.xx', 'Jan22 - 09:00:56', '2023-01-24 21:42:06.898307', 'Rede Regional Telecom', 36442, 'Ubnt', 'Codó', 'Maranhao', 'MA', 'Brazil', 'BR', 'BRA', -4.5995, -43.856);
```
6. Konfigurieren Sie die Datenbankverbindung im Skript.
7. Stellen Sie sicher, dass das Skript die erforderlichen Berechtigungen zum Lesen der auth.log-Datei hat.

## Grafana Dashboard
![image](https://user-images.githubusercontent.com/76694468/214549453-e62ad1e2-bd8d-4531-b4a8-167fa47f45ce.png)


## Verwendung
1. Führen Sie das Skript aus, indem Sie den folgenden Befehl ausführen:
```bash
python main.py
```
2. Das Skript beginnt mit dem Lesen der Datei auth.log und dem Extrahieren der erforderlichen Informationen. 
3. Die extrahierten Informationen werden dann in der MariaDB-Datenbank gespeichert. 

## Hinweis 
Bitte stellen Sie sicher, dass Sie die erforderlichen Berechtigungen zum Lesen der Datei auth.log haben.
