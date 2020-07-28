import modules.formatable as format

class MemberIndex:
    def __init__(self, data):
        self.id = data['id']
        self.image = format.image_url(data['id'])
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.role = data['role']
        self.party = self.party_name(data)

    def party_name(self, data):
        party = data['party']
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
