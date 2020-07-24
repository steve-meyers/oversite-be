class MemberShow:
    def __init__(self,
                 id,
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
                 state,
                 district,
                 website,
                 contact_form_url):
        self.id = id
        self.image = f'https://theunitedstates.io/images/congress/original/{id}.jpg'
        self.first_name = first_name
        self.last_name = last_name
        self.role = role
        self.phone = phone
        self.address = address
        self.twitter = twitter
        self.youtube = youtube
        self.facebook = facebook
        self.party = self.party_name(party) 
        self.chamber = chamber
        self.state = state
        self.district = district
        self.website = website
        self.contact_form_url = contact_form_url
    
    def party_name(self, party):
        if party == 'R':
          return 'Republican'
        elif party == 'D':
          return 'Democrat'
        elif party == 'I':
          return 'Independent'
        else:
          return party
        
    def serialize(self):  
        return {
            'id' : self.id,
            'first_name' : self.first_name,
            'last_name' : self.last_name,
            'image' : self.image,
            'role' : self.role,
            'phone' : self.phone,
            'address' : self.address,
            'twitter' : self.twitter,
            'youtube' : self.youtube,
            'facebook' : self.facebook,
            'party' : self.party,
            'chamber' : self.chamber,
            'state' : self.state,
            'district' : self.district,
            'website' : self.website,
            'contact_form_url' : self.contact_form_url
        }
class MemberIndex:
    def __init__(self,
                 id,
                 first_name,
                 last_name,
                 role,
                 party):
        self.id = id
        self.image = f'https://theunitedstates.io/images/congress/original/{id}.jpg'
        self.first_name = first_name
        self.last_name = last_name
        self.role = role
        self.party = self.party_name(party)
    
    def party_name(self, party):
        if party == 'R':
          return 'Republican'
        elif party == 'D':
          return 'Democrat'
        elif party == 'I':
          return 'Independent'
        else:
          return party
        
    def serialize(self):  
        return {           
            'id': self.id,
            'image': self.image,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'role': self.role,
            'party': self.party
        }