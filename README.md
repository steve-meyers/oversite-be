# OverSite-Backend

<img width="405" alt="Screen Shot 2020-07-29 at 2 04 17 PM" src="https://user-images.githubusercontent.com/49219371/88853381-7e2de480-d1a4-11ea-8700-8d7cf59b8c26.png">

## Team Members:

- [Steve Meyers GitHub](https://github.com/smg289)
- [Raymond Nguyen GitHub](https://github.com/itemniner)
- [Jenny Klich GitHub](https://github.com/jklich151)
- [Elliot Mackinnon GitHub](https://github.com/emackinnon1)
- [Taras Tarlov GitHub](https://github.com/ttarlov)

## Overview
OverSite was our final cross pollination project at [Turing School of Software and Design](http://turing.io). The goal for this project was to build a full stack application from ideation to production in just 14 days. The emphasis was on creating a professional agile workflow with a combination of front-end and back-end developers.
The core mission of OverSite is to amalgamate civic information into one easy to use application that allows the user to easily find Senator and Representative contact information, and Tweet at them directly through the app. Currently the user can search by state and access their local district level representatives throught their profile. 
[Live Site](https://oversite-app.herokuapp.com/)

**Technologies Used:**

**Front End:**
React.js, React Router, React Hooks, Cypress, Heroku, Circle CI  
**Back End:**
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
The main challenge of this project was connecting a front end and back end into a working deployed production application while implementing continuous integration with testing. On the back end, challenges included build a REST API using an entirely new language and framework. On the front end using Cypress with CI was a challenge that we hope to continue working on in future iterations.  

**Future Iterations:**
1. Ability to search for representatives by name, district, and other parameters.
2. Log-in with Google OAuth. 
3. Other means of messaging representative such as an email via Sendgrid. 
4. "In The News" feature that will show the most recent news article using the Google API for the chosen representative.    
5. For the Tweet bot to use the Twitter authentication.


## Set-Up:

1. Clone down the repo
2. $ `install pip`
3. $ `pip3 install pipenv`
4. $ `pipenv install`
5. $ `pipenv install virtualenv`
6. $ `virtualenv env`
7. $ `source env/bin/activate`
8. $ `python3 manage.py runserver`
9. Obtain an API Key from (https://www.propublica.org/datastore/apis)
10. Add a `.env` file to the root directory & add your API key as shown below. 
```
export APP_SETTINGS="config.DevelopmentConfig"
export DATABASE_URL="postgresql://localhost/oversite"
PROP_API= <API KEY HERE>
```


## API EndPoints 
https://oversite-api.herokuapp.com/

* "/"<br>

Response: 
```
Welcome to the OverSite API
```

### Search Representative By State
Params: State(ex: CO,TX,FL,CA)
* "/members_by_state/<state_>"
```
{
    "results": [
        {
            "senate": [
                {
                    "first_name": "Dianne",
                    "id": "F000062",
                    "image": "https://theunitedstates.io/images/congress/original/F000062.jpg",
                    "last_name": "Feinstein",
                    "party": "Democrat",
                    "role": "Senator, 1st Class",
                    "state": "California"
                },
                {
                    "first_name": "Kamala",
                    "id": "H001075",
                    "image": "https://theunitedstates.io/images/congress/original/H001075.jpg",
                    "last_name": "Harris",
                    "party": "Democrat",
                    "role": "Senator, 3rd Class",
                    "state": "California"
                }
            ]
        },
        {
            "house": [
                {
                    "first_name": "Tom",
                    "id": "M001177",
                    "image": "https://theunitedstates.io/images/congress/original/M001177.jpg",
                    "last_name": "McClintock",
                    "party": "Republican",
                    "role": "Representative",
                    "state": "California"
                },
                {
                    "first_name": "Ken",
                    "id": "C000059",
                    "image": "https://theunitedstates.io/images/congress/original/C000059.jpg",
                    "last_name": "Calvert",
                    "party": "Republican",
                    "role": "Representative",
                    "state": "California"
                },
                {
                    "first_name": "Jim",
                    "id": "C001059",
                    "image": "https://theunitedstates.io/images/congress/original/C001059.jpg",
                    "last_name": "Costa",
                    "party": "Democrat",
                    "role": "Representative",
                    "state": "California"
                }...
            ]
        }
    ]
}
```


### Representatives from the User's district
Params: User ID from Database
* "/users_reps/<user_id_>"
```
{
    "results": [
        {
            "senate": [
                {
                    "first_name": "Cory",
                    "id": "G000562",
                    "image": "https://theunitedstates.io/images/congress/original/G000562.jpg",
                    "last_name": "Gardner",
                    "party": "Republican",
                    "role": "Senator, 2nd Class",
                    "state": "Colorado"
                },
                {
                    "first_name": "Michael",
                    "id": "B001267",
                    "image": "https://theunitedstates.io/images/congress/original/B001267.jpg",
                    "last_name": "Bennet",
                    "party": "Democrat",
                    "role": "Senator, 3rd Class",
                    "state": "Colorado"
                }
            ]
        },
        {
            "house": [
                {
                    "first_name": "Ed",
                    "id": "P000593",
                    "image": "https://theunitedstates.io/images/congress/original/P000593.jpg",
                    "last_name": "Perlmutter",
                    "party": "Democrat",
                    "role": "Representative",
                    "state": "Colorado"
                }
            ]
        }
    ]
}
```


### Member Show Page Response
Params: Representative ID 
* "/member/<id_>"
```
{
    "results": [
        {
            "address": "354 Russell Senate Office Building",
            "chamber": "Senate",
            "contact_form_url": "https://www.gardner.senate.gov/contact-cory/email-cory",
            "district": null,
            "facebook": "https://www.facebook.com/SenCoryGardner",
            "first_name": "Cory",
            "id": "G000562",
            "image": "https://theunitedstates.io/images/congress/original/G000562.jpg",
            "last_name": "Gardner",
            "party": "Republican",
            "phone": "202-224-5941",
            "role": "Senator, 2nd Class",
            "state": "Colorado",
            "twitter_handle": "SenCoryGardner",
            "twitter_url": "https://twitter.com/SenCoryGardner",
            "website": "https://www.gardner.senate.gov",
            "youtube": null
        }
    ]
}
```

### Sending a Tweet Response
* GET request given reps handle and message/tweet sent to Express Microservice to tweet given message to representative 
Params: handle: "<reps handle>", message: "<message>" 
* "/tweet"
```
{
 message: "message sent"
}
```



