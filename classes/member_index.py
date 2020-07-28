import modules.formattable as format

class MemberIndex:
    def __init__(self, data):
        self.id = data['id']
        self.image = format.image_url(data['id'])
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.role = data['role']
        self.party = format.party_name(data['party'])

    def serialize(self):
        return {
            'id': self.id,
            'image': self.image,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'role': self.role,
            'party': self.party
        }
