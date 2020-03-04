//Import this JSON-string in Node-RED:

[
    {
        "id": "aa04f522.120398",
        "type": "tab",
        "label": "Google Calendar API",
        "disabled": false,
        "info": ""
    },
    {
        "id": "b83e2e5b.d5d57",
        "type": "google",
        "z": "aa04f522.120398",
        "name": "",
        "google": "734034bf.de23bc",
        "api": "calendar:v3",
        "operation": "events.list",
        "x": 850,
        "y": 340,
        "wires": [
            [
                "3f2a0d64.87ae22"
            ]
        ]
    },
    {
        "id": "36f7084a.64bcf8",
        "type": "inject",
        "z": "aa04f522.120398",
        "name": "",
        "topic": "",
        "payload": "",
        "payloadType": "date",
        "repeat": "",
        "crontab": "",
        "once": false,
        "onceDelay": 0.1,
        "x": 240,
        "y": 340,
        "wires": [
            [
                "e98536b3.53ab88"
            ]
        ]
    },
    {
        "id": "3f2a0d64.87ae22",
        "type": "debug",
        "z": "aa04f522.120398",
        "name": "Print",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "true",
        "targetType": "full",
        "x": 1030,
        "y": 480,
        "wires": []
    },
    {
        "id": "8059b3d8.60c5e",
        "type": "comment",
        "z": "aa04f522.120398",
        "name": "Enter calendarID here.",
        "info": "",
        "x": 560,
        "y": 300,
        "wires": []
    },
    {
        "id": "224c29ee.0b9d66",
        "type": "comment",
        "z": "aa04f522.120398",
        "name": "Msg object.",
        "info": "",
        "x": 250,
        "y": 300,
        "wires": []
    },
    {
        "id": "36c0bb2a.741f64",
        "type": "comment",
        "z": "aa04f522.120398",
        "name": "Enter authentication here.",
        "info": "",
        "x": 910,
        "y": 300,
        "wires": []
    },
    {
        "id": "60cbe8e9.2e14d8",
        "type": "comment",
        "z": "aa04f522.120398",
        "name": "Documentation.",
        "info": "https://flows.nodered.org/node/node-red-contrib-google\n\nPublic URL to calendar: \nhttps://calendar.google.com/calendar/embed?src=a9j5ckgf6if6sk55nu395va3cc%40group.calendar.google.com&ctz=Europe%2FOslo",
        "x": 240,
        "y": 580,
        "wires": []
    },
    {
        "id": "18f6f29e.e21d8d",
        "type": "comment",
        "z": "aa04f522.120398",
        "name": "Click the various comments to see additional info.",
        "info": "",
        "x": 340,
        "y": 540,
        "wires": []
    },
    {
        "id": "e98536b3.53ab88",
        "type": "function",
        "z": "aa04f522.120398",
        "name": "Msg parameters",
        "func": "msg.payload = {\n    calendarId: \"a9j5ckgf6if6sk55nu395va3cc@group.calendar.google.com\"\n};\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 540,
        "y": 340,
        "wires": [
            [
                "b83e2e5b.d5d57",
                "3f2a0d64.87ae22"
            ]
        ]
    },
    {
        "id": "734034bf.de23bc",
        "type": "google-conn",
        "z": "",
        "name": "Wago Test Project",
        "key": "{\n  \"type\": \"service_account\",\n  \"project_id\": \"wagotestproject\",\n  \"private_key_id\": \"ad5d4f2c627c25ba51057a70d1d675a2fd3cd44d\",\n  \"private_key\": \"-----BEGIN PRIVATE KEY-----\\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCfz3NUP/p4se8D\\n4Zh5urpJQXWAJVpHcELEW3kf9ZNpsZiCbMHRp8ExnDSKVrN+uuszE9JtGmVusrbX\\n4mR7awd4pykSQAuiKdbTuoo35wdxXhFbsXbgqzDCbd34zk66Jb7QeGKLiXXxPxfK\\nP0YrtIkZe1+MaKUXOFEsw9yTEdE0IexgPK6L0ilBLJSXuTJx4IEVVDOqfcR/nt2F\\nK6lgiw81VOGv4Hpn7P2mUPI0+tOqsyZa7seiqpxQfWaZKyW5W5rop7GOTggS3WuJ\\neAeZYviYbpXKVOAiBJZoCQmFTEPh1Hog0r87jPJY03ufkzTaXSq67XovMKw60Yn0\\nH8eWUovRAgMBAAECggEAEUt9ozYDUNGM2OIuwqnDJE9pvHMOaKHND/wIST2l9O/L\\n3f2QIjTh8xEBHKGSblojPxVblgQfyxGbORTeo/6qwdNxXfDBcYzOm35aG/+sLggs\\nn7w+bcUJE1mZhqYpHfscwentXEWFlpSp6fDcErnIhpHz/rmKeE9XdZ1Cv0XT2qzP\\nZNBiXURvVPuCNunAVw622pA6EsCDQ+QJyIi1CaHjTDs3AENxiPHIFmglTxcvZt7x\\nJ53PnVlzHHV8hxKnGxs44MY6s7LzyHbglPUcicz+ZhRmxoHMIfCujYTO0ULSBcBG\\nlM+25UgqDv4RSBtHk9FbExE6JWUg8IMh1niLaYMioQKBgQDLKjapSsq+mx7bPWS0\\nBtAj+tK210KeBt9VbOrNDFjm1UgZtWDUMeLmhIdvhGuYndkWxdZMZvCfpXMQCXAt\\n1pQlOkv1nwTtDIAuwrAhGGmPgMZEN46nD2+SmA6lv43/yOyiN5aJM+dz8ueWpcOE\\nekHf31DIi+MFZB27yb0l2buzOQKBgQDJXuP1fknc6J4YRB16CiX4LGNA6LjifcEd\\nDdKJC/SeghGJiS6bPg8bOM6Xj9JwV3b2bCXPWH3RpZYrJ9yskL4cnj0AI0YqHYf0\\nGzLnEQIQ5JdOKmwuJTtIyB1RKcrH0ktKKjsMbl6AbosiIbGGgJgTKrhjgcw5EgDD\\nn0ysKnolWQKBgFPlN7NK/lQdjG1uecJZuePRtOfqFklZfyowkvlfquqPknmDS9v0\\nScV1XtQvM5tPO5FK2warz5utX8l0jE1xebWx0CI6q3cUHW6x2Leh9B1dSQJsiszz\\n89fuUMYjRwkkOIt4NwKrW12nJfkwtH9lWQSQnDRkh7f3MswUL7aMphUJAoGAZlJO\\nOQ8LzzFwK9pos/t2Ia3EXVYjpArMVswQP80QZn6nFKDdSsr0+Bscds0A3E7FRx/a\\n8on/nMisDo+5xQHjaD1Lt8c0vu+0hmhPrDPrPdQ5weEyiRwoDKqKoxQ+Utzbnvro\\neD+Yy1/gWN6QC01KeOrLONzafeFU/BH07sLCwDkCgYEAxIR59ewmkJRtrzeg6QiR\\nflSpegBcr7vwd1rZpJaa6ZraYNqcFsfGDcKXX2Efu0cMaos9l96etaPr53Az+X7m\\nNemJlUcmFPgGy3UG0hanUy/hhNBbkCJX4a1TXHJqys/6n8PABc2CZlnhv/2pMlTW\\ncobZIXbpnJkiJYQx5GemVzY=\\n-----END PRIVATE KEY-----\\n\",\n  \"client_email\": \"wagotestcredentials@wagotestproject.iam.gserviceaccount.com\",\n  \"client_id\": \"117777735917317666904\",\n  \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",\n  \"token_uri\": \"https://oauth2.googleapis.com/token\",\n  \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\",\n  \"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/wagotestcredentials%40wagotestproject.iam.gserviceaccount.com\"\n}",
        "scopes": "https://www.googleapis.com/auth/calendar"
    }
]
