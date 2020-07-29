# oversite-BACKEND

<img width="405" alt="Screen Shot 2020-07-29 at 2 04 17 PM" src="https://user-images.githubusercontent.com/49219371/88853381-7e2de480-d1a4-11ea-8700-8d7cf59b8c26.png">

## Team Members:

- [Steve Meyers GitHub](https://github.com/smg289)
- [Raymond Nguyen GitHub](https://github.com/itemniner)
- [Jenny Klich GitHub](https://github.com/jklich151)
- [Elliot Mackinnon GitHub](https://github.com/emackinnon1)
- [Taras Tarlov GitHub](https://github.com/ttarlov)

## Overview
OverSite was our final cross pollination project at [Turing School of Software and Design](http://turing.io). The goal for this project was to build a full stack application from ideation to production in just 14 days. The emphasis was on was on creating a professional agile workflow with a combination of front-end and back-end developers.
The core mission of OverSite is to amalgamate civic information into one easy to use application that allows the user to easily find Senator and Representative contact information, and Tweet at them directly through the app. Currently the user can search by state and access their local district level representatives throught their profile. 
[Live Site](https://oversite-app.herokuapp.com/)

**Technologies Used:**
***Front End:***
React.js, React Router, React Hooks, Cypress, Heroku, Circle CI  
***Back End:**
Python on Flask, SQLAlchamy, Travis CI, Heroku, Pytest, Nightmare.js (Express/Node microservice), Postgres DB

![express_node_js](https://user-images.githubusercontent.com/49219371/88857711-a2d98a80-d1ab-11ea-8f91-5af3f4a38ffa.jpeg)
![heroku](https://user-images.githubusercontent.com/49219371/88857716-a40ab780-d1ab-11ea-8690-5a0c8b908ed7.png)
![flask](https://user-images.githubusercontent.com/49219371/88857723-a5d47b00-d1ab-11ea-8c37-21f80e27d6e7.png)
![TravisCI](https://user-images.githubusercontent.com/49219371/88857727-a705a800-d1ab-11ea-9055-fcff6d0edb4a.png)
![Postgresql_logo](https://user-images.githubusercontent.com/49219371/88858000-272c0d80-d1ac-11ea-86fd-162e52b5a79d.png)
![python](https://user-images.githubusercontent.com/49219371/88857886-ec29da00-d1ab-11ea-8372-07551e33ed9a.png)
![sqlalchemy](https://user-images.githubusercontent.com/49219371/88857896-efbd6100-d1ab-11ea-92f5-c5a1d74b63ad.jpeg)
![nightmare](https://user-images.githubusercontent.com/49219371/88857694-9e14d680-d1ab-11ea-826b-620bc1633f33.png)


**Challenges:**
The main challenge of this project was connecting a front end and backend into a working deployed production application while implementing continues integration with testing. On the back-end, challenges included build a REST API using an entirely new language and framework. On the front end using Cypress with CI was a challenge that we hope to continue working on in future iterations.  
**Future Iterations**
1. Ability to search for representatives by name, district, and other parameters.
2. Log-in with Google OAuth. 
3. Other means of messaging representative via Sendgrid. 
4. "In The News" feature that will show the most recent news article using Google API for the chosen representative.    


## Set-Up

1. $ install pip
2. $ pip3 install pipenv
3. $ pipenv install 
4. $ pipenv install virtualenv
5. $ virtualenv env
6. $ source env/bin/activate
7. $ python3 manage.py runserver
8.  Add .env file to root directory & Add API key to file shown below. (https://www.propublica.org/datastore/apis)
```
export APP_SETTINGS="config.DevelopmentConfig"
export DATABASE_URL="postgresql://localhost/oversite"
PROP_API= <API KEY HERE>
```
* ...

## API EndPoints 
Params: State(ex: CO,TX,FL,CA)
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
        { "first_name": "Kamala",
          "last_name": "Harris",
          "party": "D",
          "role": "Senator, 3rd Class"}]},
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
