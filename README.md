# oversite-BACKEND

<img width="405" alt="Screen Shot 2020-07-29 at 2 04 17 PM" src="https://user-images.githubusercontent.com/49219371/88853381-7e2de480-d1a4-11ea-8700-8d7cf59b8c26.png">
## Team Members:
[Steve Meyers GitHub](https://github.com/smg289)
[Raymond Nguyen GitHub](https://github.com/itemniner)
[Jenny Klich GitHub](https://github.com/jklich151)
[Elliot Mackinnon GitHub](https://github.com/emackinnon1)
[Taras Tarlov GitHub](https://github.com/ttarlov)

## Overview
OverSite was our final cross pollination project at [Turing School of Software and Design](http://turing.io). The goal for this project was to build a full stack application from ideation to production in just 14 days. The emphasis was on was on creating a professional agile workflow with a combination of front-end and back-end developers.
The core mission of OverSite is to amalgamate civic information into one easy to use application that allows the user to easily find Senator and Representative contact information, and Tweet at them directly through the app. Currently the user can search by state and access their local district level representatives throught their profile. 
[Live Site](https://oversite-app.herokuapp.com/)

**Technologies Used:**
***Front End:***
React.js, React Router, React Hooks, Cypress, Heroku, Circle CI  
***Back End:**
Python on Flask, SQLAlchamy, Travis CI, Heroku, Pytest, Nightmare.js (Express/Node microservice), Postgres DB

![express_node_js](https://user-images.githubusercontent.com/49219371/88857256-ccde7d00-d1aa-11ea-9cc5-bda3317b9cdb.jpeg)
![flask](https://user-images.githubusercontent.com/49219371/88857257-cd771380-d1aa-11ea-8353-42c7a486f3cf.png)
![heroku](https://user-images.githubusercontent.com/49219371/88857259-ce0faa00-d1aa-11ea-9e3f-fd0d12459fa9.png)
![Postgresql_logo](https://user-images.githubusercontent.com/49219371/88857260-ce0faa00-d1aa-11ea-9cb5-b3b2a802b624.png)
![python](https://user-images.githubusercontent.com/49219371/88857262-cea84080-d1aa-11ea-8b52-9e08e5e50c38.png)
![sqlalchemy](https://user-images.githubusercontent.com/49219371/88857264-cea84080-d1aa-11ea-8b4b-f73a1fe89f0e.jpeg)
![TravisCI](https://user-images.githubusercontent.com/49219371/88857266-cf40d700-d1aa-11ea-95b9-aff1822154aa.png)
![nightmare](https://user-images.githubusercontent.com/49219371/88857357-ff887580-d1aa-11ea-8e05-4080e585b310.png)

**Challenges:**
The main challenge of this project was connecting a front end and backend into a working deployed production application while implementing continues integration with testing. On the back-end, challenges included build a REST API using an entirely new language and framework. On the front end using Cypress with CI was a challenge that we hope to continue working on in future iterations.  
**Future Iterations**
1. Ability to search for representatives by name, district, and other parameters.
2. Log-in with Google OAuth. 
3. Other means of messaging representative via Sendgrid. 
4. "In The News" feature that will show the most recent news article using Google API for the chosen representative.    


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
        }
      ]
    }
  ]
}
```
