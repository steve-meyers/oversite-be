from api.app import app
from api.classes.member_show import MemberShow

def test_initialize():
  data = {
      "id": "D000197",
      "member_id": "D000197",
      "first_name": "Diana",
      "last_name": "DeGette",
      "url": "https://degette.house.gov",
      "twitter_account": "RepDianaDeGette",
      "facebook_account": "DianaDeGette",
      "youtube_account": "RepDianaDeGette",
      "crp_id": "N00006134",
      "google_entity_id": "/m/024z95",
      "rss_url": "https://degette.house.gov/rss.xml",
      "in_office": True,
      "current_party": "D",
      "roles": [
          {
            "congress": "116",
              "chamber": "House",
              "title": "Representative",
              "short_title": "Rep.",
              "state": "CO",
              "party": "D",
              "leadership_role": None,
              "fec_candidate_id": "H6CO01141",
              "district": "1",
              "ocd_id": "ocd-division/country:us/state:co/cd:1",
              "start_date": "2019-01-03",
              "end_date": "2021-01-03",
              "office": "2111 Rayburn House Office Building",
              "phone": "202-225-4431",
              "fax": None,
              "contact_form": None,
              "next_election": "2020",
              "total_votes": 868,
              "missed_votes": 6,
              "total_present": 0,
              "bills_sponsored": 24,
              "bills_cosponsored": 395,
              "missed_votes_pct": 0.69,
              "votes_with_party_pct": 98.61,
              "votes_against_party_pct": 1.28
          }]
  }

  member = MemberShow(data)

  assert member.id == 'D000197'
  assert member.image == 'https://theunitedstates.io/images/congress/original/D000197.jpg'
  assert member.first_name == 'Diana'
  assert member.last_name == 'DeGette'
  assert member.role == 'Representative'
  assert member.phone == '202-225-4431'
  assert member.address == '2111 Rayburn House Office Building'
  assert member.twitter_url == 'https://twitter.com/RepDianaDeGette'
  assert member.twitter_handle == 'RepDianaDeGette'
  assert member.youtube == 'https://www.youtube.com/user/RepDianaDeGette'
  assert member.facebook == 'https://www.facebook.com/DianaDeGette'
  assert member.party == 'Democrat'
  assert member.chamber == 'House'
  assert member.state == 'Colorado'
  assert member.district == '1'
  assert member.website == 'https://degette.house.gov'
  assert member.contact_form_url == None
