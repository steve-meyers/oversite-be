from api.app import app
from api.classes.member_index import MemberIndex

def test_initialize():
  data = {
          "id": "D000197",
          "name": "Diana DeGette",
          "first_name": "Diana",
          "middle_name": None,
          "last_name": "DeGette",
          "suffix": None,
          "role": "Representative",
          "gender": "F",
          "party": "D",
          "times_topics_url": None,
          "twitter_id": "RepDianaDeGette",
          "facebook_account": "DianaDeGette",
          "youtube_id": "RepDianaDeGette",
          "seniority": "24",
          "next_election": "2020",
          "api_uri": "https://api.propublica.org/congress/v1/members/D000197.json",
          "district": "1",
          "at_large": None
  }
  state = 'co'

  member = MemberIndex(data, state)

  assert member.id == 'D000197'
  assert member.image == 'https://theunitedstates.io/images/congress/original/D000197.jpg'
  assert member.first_name == 'Diana'
  assert member.last_name == 'DeGette'
  assert member.role == 'Representative'
  assert member.party == 'Democrat'
  assert member.state == 'Colorado'
