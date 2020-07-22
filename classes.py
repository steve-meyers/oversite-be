class MemberShow:
    def __init__(self, 
                 first_name,
                 last_name,
                 role,
                 phone,
                 address,
                 twitter,
                 youtube,
                 facebook,
                 party,
                 chamber,
                 title,
                 state,
                 district,
                 website,
                 contact_form_url):
        self.first_name = first_name
        self.last_name = last_name
        self.role = role
        self.phone = phone
        self.address = address
        self.twitter = twitter
        self.youtube = youtube
        self.facebook = facebook
        self.party = party 
        self.chamber = chamber
        self.title = title
        self.state = state
        self.district = district
        self.website = website
        self.contact_form_url = contact_form_url

class MemberIndex:
    def __init__(self, 
                 first_name,
                 last_name,
                 role,
                 party):
        self.first_name = first_name
        self.last_name = last_name
        self.role = role
        self.party = party
      
    def serialize(self):  
        return {           
            'first_name': self.first_name,
            'last_name': self.last_name,
            'role': self.role,
            'party': self.party
        }