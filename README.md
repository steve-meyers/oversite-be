# oversite-be

## Set-Up

* $ install pip

* $ pip3 install pipenv

* $ pipenv install 

* $ pipenv install virtualenv

* $ virtualenv env

* $ source env/bin/activate

* $ python3 manage.py runserver

* Add .env file to root directory & Add API key to file shown below. (https://www.propublica.org/datastore/apis)

```
export APP_SETTINGS="config.DevelopmentConfig"
export DATABASE_URL="postgresql://localhost/oversite"

PROP_API= <API KEY HERE>
```

* ...

## API EndPoints 
* "/members_by_state/<state_>"
```

{
  "results": [
    {
      "senate": [
        {
          "first_name": "Dianne",
          "last_name": "Feinstein",
          "party": "D",
          "role": "Senator, 1st Class"
        },
        {
          "first_name": "Kamala",
          "last_name": "Harris",
          "party": "D",
          "role": "Senator, 3rd Class"
        }
      ]
    },
    {
      "house": [
        {
          "first_name": "Tom",
          "last_name": "McClintock",
          "party": "R",
          "role": "Representative"
        },
        {
          "first_name": "Ken",
          "last_name": "Calvert",
          "party": "R",
          "role": "Representative"
        },
        {
          "first_name": "Jim",
          "last_name": "Costa",
          "party": "D",
          "role": "Representative"
        },
        {
          "first_name": "Susan",
          "last_name": "Davis",
          "party": "D",
          "role": "Representative"
        },
        {
          "first_name": "Anna",
          "last_name": "Eshoo",
          "party": "D",
          "role": "Representative"
        },
        {
          "first_name": "Zoe",
          "last_name": "Lofgren",
          "party": "D",
          "role": "Representative"
        },
        {
          "first_name": "Barbara",
          "last_name": "Lee",
          "party": "D",
          "role": "Representative"
        },
        {
          "first_name": "Doris",
          "last_name": "Matsui",
          "party": "D",
          "role": "Representative"
        },
        {
          "first_name": "Kevin",
          "last_name": "McCarthy",
          "party": "R",
          "role": "Representative"
        },
        {
          "first_name": "Jerry",
          "last_name": "McNerney",
          "party": "D",
          "role": "Representative"
        },
        {
          "first_name": "Grace",
          "last_name": "Napolitano",
          "party": "D",
          "role": "Representative"
        },
        {
          "first_name": "Devin",
          "last_name": "Nunes",
          "party": "R",
          "role": "Representative"
        },
        {
          "first_name": "Lucille",
          "last_name": "Roybal-Allard",
          "party": "D",
          "role": "Representative"
        },
        {
          "first_name": "Brad",
          "last_name": "Sherman",
          "party": "D",
          "role": "Representative"
        },
        {
          "first_name": "Adam",
          "last_name": "Schiff",
          "party": "D",
          "role": "Representative"
        },
        {
          "first_name": "Linda",
          "last_name": "Sánchez",
          "party": "D",
          "role": "Representative"
        },
        {
          "first_name": "Maxine",
          "last_name": "Waters",
          "party": "D",
          "role": "Representative"
        },
        {
          "first_name": "Jackie",
          "last_name": "Speier",
          "party": "D",
          "role": "Representative"
        },
        {
          "first_name": "John",
          "last_name": "Garamendi",
          "party": "D",
          "role": "Representative"
        },
        {
          "first_name": "Nancy",
          "last_name": "Pelosi",
          "party": "D",
          "role": "Representative"
        },
        {
          "first_name": "Judy",
          "last_name": "Chu",
          "party": "D",
          "role": "Representative"
        },
        {
          "first_name": "Mike",
          "last_name": "Thompson",
          "party": "D",
          "role": "Representative"
        },
        {
          "first_name": "Karen",
          "last_name": "Bass",
          "party": "D",
          "role": "Representative"
        },
        {
          "first_name": "Doug",
          "last_name": "LaMalfa",
          "party": "R",
          "role": "Representative"
        },
        {
          "first_name": "Jared",
          "last_name": "Huffman",
          "party": "D",
          "role": "Representative"
        },
        {
          "first_name": "Paul",
          "last_name": "Cook",
          "party": "R",
          "role": "Representative"
        },
        {
          "first_name": "Eric",
          "last_name": "Swalwell",
          "party": "D",
          "role": "Representative"
        },
        {
          "first_name": "Julia",
          "last_name": "Brownley",
          "party": "D",
          "role": "Representative"
        },
        {
          "first_name": "Tony",
          "last_name": "Cárdenas",
          "party": "D",
          "role": "Representative"
        },
        {
          "first_name": "Mark",
          "last_name": "Takano",
          "party": "D",
          "role": "Representative"
        },
        {
          "first_name": "Alan",
          "last_name": "Lowenthal",
          "party": "D",
          "role": "Representative"
        },
        {
          "first_name": "Juan",
          "last_name": "Vargas",
          "party": "D",
          "role": "Representative"
        },
        {
          "first_name": "Ami",
          "last_name": "Bera",
          "party": "D",
          "role": "Representative"
        },
        {
          "first_name": "Raul",
          "last_name": "Ruiz",
          "party": "D",
          "role": "Representative"
        },
        {
          "first_name": "Scott",
          "last_name": "Peters",
          "party": "D",
          "role": "Representative"
        },
        {
          "first_name": "Mark",
          "last_name": "DeSaulnier",
          "party": "D",
          "role": "Representative"
        },
        {
          "first_name": "Ted",
          "last_name": "Lieu",
          "party": "D",
          "role": "Representative"
        },
        {
          "first_name": "Norma",
          "last_name": "Torres",
          "party": "D",
          "role": "Representative"
        },
        {
          "first_name": "Pete",
          "last_name": "Aguilar",
          "party": "D",
          "role": "Representative"
        },
        {
          "first_name": "Ro",
          "last_name": "Khanna",
          "party": "D",
          "role": "Representative"
        },
        {
          "first_name": "Jimmy",
          "last_name": "Panetta",
          "party": "D",
          "role": "Representative"
        },
        {
          "first_name": "Salud",
          "last_name": "Carbajal",
          "party": "D",
          "role": "Representative"
        },
        {
          "first_name": "Nanette",
          "last_name": "Barragán",
          "party": "D",
          "role": "Representative"
        },
        {
          "first_name": "J.",
          "last_name": "Correa",
          "party": "D",
          "role": "Representative"
        },
        {
          "first_name": "Jimmy",
          "last_name": "Gomez",
          "party": "D",
          "role": "Representative"
        },
        {
          "first_name": "Josh",
          "last_name": "Harder",
          "party": "D",
          "role": "Representative"
        },
        {
          "first_name": "TJ",
          "last_name": "Cox",
          "party": "D",
          "role": "Representative"
        },
        {
          "first_name": "Gilbert",
          "last_name": "Cisneros",
          "party": "D",
          "role": "Representative"
        },
        {
          "first_name": "Katie",
          "last_name": "Porter",
          "party": "D",
          "role": "Representative"
        },
        {
          "first_name": "Harley",
          "last_name": "Rouda",
          "party": "D",
          "role": "Representative"
        },
        {
          "first_name": "Mike",
          "last_name": "Levin",
          "party": "D",
          "role": "Representative"
        },
        {
          "first_name": "Mike",
          "last_name": "Garcia",
          "party": "R",
          "role": "Representative"
        }
      ]
    }
  ]
}
```
