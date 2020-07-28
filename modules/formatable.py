def image_url(member_id):
    return f'https://theunitedstates.io/images/congress/original/{member_id}.jpg'

def party_name(party):
    if party == 'R':
      return 'Republican'
    elif party == 'D':
      return 'Democrat'
    elif party == 'I':
      return 'Independent'
    else:
      return party
