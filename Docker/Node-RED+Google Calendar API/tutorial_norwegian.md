# Google Calendar API i Node-RED

Dette dokumentet skal beskrive måten man kan gå frem på for å kunne hente kalenderdata fra Google Calendar i et Node-Red-miljø.

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
    Importer ved å kopiere inn JSON-stringen som er inkludert nederst i dette dokumentet.
2.  Installer “node-red-contrib-google”.
    Under menyen øverst til høyre: velg “Manage Palettes”. 
    Klikk “Install”, og søk opp riktig palette. 
3.  Sett opp “google”-noden:
    Sørg for at API står som “calendar:v3” (med mindre du ønsker å bruke andre APIer).
    Operation kan velges til “events.list”. Her kan man velge andre operations, etter hva som passer. (Dette vil gi forskjellige eventer, lister, kalendere, etc. som output). Events.list vil gi oss en array av nåværende og kommende eventer.
4.  Konfigurer “google-conn”:
    Dette skal gjøres i “Connection” i “google”-noden i forrige steg.
5.  Konfigurer “set”-noden. Legg inn Calendar ID her.

For hjelp: klikk deg inn på Documentation-noden
