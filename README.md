# Startside
## Docker, Support and Documentation
>Dette repoet er tiltenkt å veilede, inspirere og å dokumentere nye og gamle konsepter med Wago. Det gjelder i hovedsak nye fremgangsmåter som har blitt muliggjort på grunn av Wagos nye generasjon med PLS'er. Repoet vil utforske og veilede nye fremgangsmåter ved bruk av Linux og Docker, men ikke bare det. Veiledningene her vil variere i vanskelighetsgrad, men vi forsøker å gjøre dette åpent for alle. For kontakt: se informasjon i bunnen.

### Initiellt Oppsett

Under følger hovedtrinnene for å starte programutvikling på Wago Ethernet PLS.
1. Start ved å koble spenningstilførsel (24V) og Ethernet til PLS'en
<div align="center">
   <br>
  <img src="img\hardware_setup.PNG" width="600"><br><br>
</div>

2. Foruten riktig tilførsel (24V), krever et vellykket oppsett at PLS og PC eksisterer på samme IP-subnett.\
Dette betyr at de tre første siffergruppene i begge IP-adressene må være identiske, for eksempel: 192.168.1.\<X>\
Sett derfor IP adressen på PC'en i henhold til dette

<div align="center">
   <br>
  <img src="img\IP_Setup.PNG" width="600"><br><br>
</div>

3. Gjør deretter en link-verifisering ved å logge inn på 192.168.1.\<X> og sjekke at nettsiden for PLS'en er tilgjengelig.\
Logg deretter inn med `brukernavn / passord = admin / wago`



### Videoer for veiledning og inspirasjon

[Fagskolen i Hordaland](https://www.youtube.com/playlist?list=PLRHOiD0CfKwpTfXd76A2cvOdlkmPCcgjC)\
[Kurt Braun](http://www.youtube.com/user/WagoKurt)\
[Jesse Cox](https://www.youtube.com/channel/UCXEwdiyGgzVDJD48f7rWOAw)\
[Wago Tyskland](https://www.youtube.com/user/WagoKontakttechnik)


### Dokumentasjon

[Datablad & Manualer](http://www.wago.com/wagoweb/documentation/index_e.htm)\
[Sertifikater & Standarder](https://www.wago.com/wagoweb/documentation/750/eng_dat/d0750xxxx_xxxxxxxx_12en.pdf)


### Starter-Kit for vanlige applikasjonsområder

[Ethernet](https://www.wago.com/global/d/12983)\
[KNX/IP](https://www.wago.com/global/d/7189)\
[BACnet/IP](https://www.wago.com/global/d/7193)

Om applikasjonen du leter etter ikke er listet opp kan du fort finne den ved et søk blant [alle applikasjoner](https://www.wago.com/global/search?q=*:downloadcontainerdate:resultType:download:docCategory1:DL_3:docCategory1:DL_58&ststate=eyJkb3dubG9hZCI6Ii9zZWFyY2g/cVx1MDAzZColM0FyZWxldmFuY2UlM0FyZXN1bHRUeXBlJTNBZG93bmxvYWQlM0Fkb2NDYXRlZ29yeTElM0FETF8zXHUwMDI2c29ydFx1MDAzZGRvd25sb2FkY29udGFpbmVyZGF0ZSJ9).\
Det fins også en nyttig [Verktøykasse](http://www.wago.no/automasjon/tools/WagoBasicTools.html) med alle vanlige Wago verktøy.


### Viderekommen bruk

Hvis du er softwareutvikler eller en erfaren bruker, og du ønsker å utnytte utstyrets kapabilitet til det fulleste, er Wago's nyeste PLS'er midt i blinken. Her har vi åpnet PLS'ene og gjort kildekoden open source med et eget [firmware SDK](https://github.com/WAGO/pfc-firmware-sdk). Dette gir uante muligheter og knytter sammen automasjons-, og softwareutviklingsverden.
En av våre nyeste PLS'er PFC200 G2, støtter Docker, som er et verktøy laget for å gjøre det enklere å lage, installere, og kjøre applikasjoner ved bruk av containere. Containere gir utviklere muligheten til å pakke ferdig en applikasjon med alle delene som trengs, som biblioteker og andre avhengigheter, og sende alt ut som en ferdig pakke. Du kan finne mer informasjon og hvordan sette opp PLS'en med Docker og mye mer i vårt [Docker-Support](https://github.com/Wago-Norge/Docker-Support) repo.

Wago Tyskland har også laget en fin samling med [how-to's](https://github.com/WAGO/pfc-howtos) for forskjellige applikasjonsmuligheter på PCF100, PFC200 og PFC200 G2.


### Kontaktinformasjon

Vår tekniske supportavdeling har telefontid hverdager 8-16, hele året utenom helligdager.

| Stilling          | Navn              | Kontor   | Mobil    |
| ----------------- |:-----------------:| :-------:| :-------:|
| Teknisk leder     | Torgeir Sundet    | 22309453 | 97195836 |
| Teknisk konsulent | Kristian Syversen | 22309458 | 93605571 |
| Teknisk konsulent | Thorgrim Jansrud  | 22309464 | 91146947 |
| Teknisk konsulent | Håkon Skaug I.    | 22309478 | 97479678 |

Vi hjelper gjerne med fjernhjelp via [TeamViewer](https://download.teamviewer.com/download/TeamViewerQS.exe), og du kan også nå oss på [support.no@wago.com](mailto:support.no@wago.com)


### EOF
