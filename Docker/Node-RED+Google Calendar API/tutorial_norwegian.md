# Google Calendar API i Node-RED
Dette dokumentet skal beskrive måten man kan gå frem på for å kunne hente kalenderdata fra Google Calendar i et Node-Red-miljø. Eksempelet som er inkludert i ```import.txt``` bruker en kalender og autentisering som er generert i Wago for å kunne illustrere dette programmets virkemåte. For å bruke dette til eget bruk, må stegene nedenfor følges.


### Sett opp Google:
1.  Lag en Google-konto (gmail).
2.  Gå til: ```https://console.developers.google.com/```
3.  Velg “Select a project”, og deretter “New Project”. Sett dette deretter opp slik du ønsker.
4.  Øverst skal du nå kunne se at du er under ditt nye prosjekt. Rett under (“Dashboard”) skal du kunne trykke “Enable APIs and services”. Klikk her, og velg “Google Calendar API” lengre ned. Trykk “Enable”.
5.  Trykk på “Google APIs” eller menyen øverst til venstre, og deretter “Dashboard”. 
    Gå til “Credentials”, og trykk: “Create credentials” > “Service account key” > “New service account”: Skriv inn et passende navn og rolle. Velg “JSON” og deretter “Create”. 
6.  Du vil nå få forespørsel om å laste ned en JSON-fil. Dette er en tekststring som inneholder autentiseringen for å nå kalenderen. Denne stringen skal limes inn i en node i neste del i Node-Red.
7.  Til slutt må du ha en kalender som du ønsker å bruke i prosjektet. Gå til: ```https://calendar.google.com/calendar/r```
    Hvis du ikke har en spesifikk kalender fra før: opprett en ny.
    Gå deretter inn på kalenderens innstillinger, og sett kalenderen til offentlig.
8.  Nederst på siden for kalenderens innstillinger kan du se “Calendar ID”. Kopier IDen. Denne skal brukes i neste del.


### Sett opp Node-Red flow:
1.  Importer flow for Node-Red:
    Gå til grensesnittet for Node-Red ```(typisk 192.168.1.xx:1880)```.
    Under menyen øverst til høyre: velg “Import”.
    Importer ved å kopiere inn JSON-stringen som er inkludert i denne mappen: ```import.txt```.
2.  Installer biblioteket:
    Under menyen øverst til høyre: velg “Manage Palettes”. 
    Klikk “Install”, og søk opp riktig palette: ```node-red-contrib-google```. 
3.  Sett opp “google”-noden:
    Sørg for at API står som “calendar:v3” (med mindre du ønsker å bruke andre APIer).
    Operation kan velges til “events.list”. Her kan man velge andre operations, etter hva som passer. (Dette vil gi forskjellige             resultater. Events.list vil gi oss en array av nåværende og kommende eventer.
4.  Konfigurer “google-conn”:
    Dette skal gjøres i “Connection” i “google”-noden i forrige steg.
5.  Konfigurer “Msg parameters”-noden. Legg inn Calendar ID her.

### API-kall med parametre
Ved å sende en msg med spesifikke parametre gjennom Google-noden, får vi et spesifikt svar tilbake. De forskjellige parametrene kan finnes i linken helt nederst.
Et msg-objekt ser gjerne slik ut:
```
msg = {
    _msgid: "7aacba.c7ac34",
    topic: "",
    payload: "",
}
```
Vi kan legge parametrene vi ønsker å kalle med under msg.payload, som følger:
```
msg.payload = {
    calendarId: hypotheticalEmail_lh2luhofjq8jj2nhib0@group.calendar.google.com,
    timeMin: "2020-01-27T15:51:31.151Z",
    timeMax: "2020-01-27T18:40:00.000Z",
    orderBy: "startTime",
    singleEvents: true
}
```
Disse kan være nyttige parametre for å filtrere resultatet som mottas fra Google. KalenderID er hvilken kalender du er koblet til. timeMin og timeMax filtrerer ut resultater utenfor dette tidsperspektive. Du kan gjerne bare bruke én av disse. orderBy sorterer resultatene etter når de starter - ikke når de ble laget.

Tips: 
-   API'et foretrekker å få tiden gitt i formatet ovenfor. Ved å bruke biblioteket node-red-contrib-moment kan du enkelt formatere tiden slik, i tillegg til å kunne justere tiden for tidssoner, sommer- og vintertid, og lignende.

For hjelp: 
-   https://developers.google.com/calendar/v3/reference/events/list
-   Klikk deg inn på Documentation-noden
