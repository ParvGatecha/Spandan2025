import requests

# URL to send the POST request
# url = "http://spandan.iiitb.ac.in:8001/api/sports/"
url = "http://127.0.0.1:8000/api/sports/"

# List of objects to be sent as request body
objects = [
    {"name": "Badminton-MS", "category": "Badminton", "min_team_size": 1, "max_team_size": 1, "min_females": 0, "min_males": 0},
    {"name": "Badminton-MD", "category": "Badminton", "min_team_size": 2, "max_team_size": 2, "min_females": 0, "min_males": 0},
    {"name": "Badminton-WS", "category": "Badminton", "min_team_size": 1, "max_team_size": 1, "min_females": 1, "min_males": 1},
    {"name": "Badminton-WD", "category": "Badminton", "min_team_size": 2, "max_team_size": 2, "min_females": 2, "min_males": 2},
    {"name": "Badminton-MiD", "category": "Badminton", "min_team_size": 2, "max_team_size": 2, "min_females": 1, "min_males": 1},
    {"name": "TableTennis-MS", "category": "TableTennis", "min_team_size": 1, "max_team_size": 1, "min_females": 0, "min_males": 0},
    {"name": "TableTennis-MD", "category": "TableTennis", "min_team_size": 2, "max_team_size": 2, "min_females": 0, "min_males": 0},
    {"name": "TableTennis-WS", "category": "TableTennis", "min_team_size": 1, "max_team_size": 1, "min_females": 1, "min_males": 1},
    {"name": "TableTennis-WD", "category": "TableTennis", "min_team_size": 2, "max_team_size": 2, "min_females": 2, "min_males": 2},
    {"name": "TableTennis-MiD", "category": "TableTennis", "min_team_size": 2, "max_team_size": 2, "min_females": 1, "min_males": 1},
    {"name": "Throwball", "category": "Throwball", "min_team_size": 8, "max_team_size": 10, "min_females": 2, "min_males": 6},
    {"name": "Football", "category": "Football", "min_team_size": 6, "max_team_size": 9, "min_females": 0, "min_males": 9},
    {"name": "Cricket", "category": "Cricket", "min_team_size": 10, "max_team_size": 12, "min_females": 0, "min_males": 12},
    {"name": "Volleyball", "category": "Volleyball", "min_team_size": 7, "max_team_size": 9, "min_females": 0, "min_males": 9},
    {"name": "Basketball", "category": "Basketball", "min_team_size": 5, "max_team_size": 8, "min_females": 0, "min_males": 8},
    {"name": "Basketball-M3", "category": "Basketball", "min_team_size": 3, "max_team_size": 4, "min_females": 0, "min_males": 0},
    {"name": "Basketball-3", "category": "Basketball", "min_team_size": 3, "max_team_size": 4, "min_females": 0, "min_males": 0},
    {"name": "Basketball-5", "category": "Basketball", "min_team_size": 5, "max_team_size": 8, "min_females": 0, "min_males": 0},
    {"name": "Basketball-W", "category": "Basketball", "min_team_size": 3, "max_team_size": 4, "min_females": 3, "min_males": 4},
    {"name": "Valorant", "category": "NonMajor", "min_team_size": 5, "max_team_size": 5, "min_females": 0, "min_males": 5},
    {"name": "CodM", "category": "NonMajor", "min_team_size": 5, "max_team_size": 5, "min_females": 0, "min_males": 5},
    {"name": "Fifa-S", "category": "NonMajor", "min_team_size": 1, "max_team_size": 1, "min_females": 0, "min_males": 1},
    {"name": "Fifa-D", "category": "NonMajor", "min_team_size": 2, "max_team_size": 2, "min_females": 0, "min_males": 2},
    {"name": "GullyCricket", "category": "NonMajor", "min_team_size": 5, "max_team_size": 6, "min_females": 1, "min_males": 0},
    {"name": "ClashRoyale", "category": "NonMajor", "min_team_size": 1, "max_team_size": 1, "min_females": 0, "min_males": 0},
    {"name": "BGMI", "category": "NonMajor", "min_team_size": 1, "max_team_size": 4, "min_females": 0, "min_males": 0},
    {"name": "Chess", "category": "NonMajor", "min_team_size": 1, "max_team_size": 1, "min_females": 0, "min_males": 1},
    {"name": "Powerlifting", "category": "NonMajor", "min_team_size": 1, "max_team_size": 1, "min_females": 0, "min_males": 0},
    {"name": "Powerlifting-W", "category": "NonMajor", "min_team_size": 1, "max_team_size": 1, "min_females": 1, "min_males": 0},
    {"name": "Carroms", "category": "NonMajor", "min_team_size": 2, "max_team_size": 2, "min_females": 0, "min_males": 2},
    {"name": "TugOfWar", "category": "NonMajor", "min_team_size": 5, "max_team_size": 7, "min_females": 0, "min_males": 7},
    {"name": "TugOfWar-W", "category": "NonMajor", "min_team_size": 5, "max_team_size": 7, "min_females": 5, "min_males": 0},
    {"name": "Tennis-MS", "category": "Tennis", "min_team_size": 1, "max_team_size": 1, "min_females": 0, "min_males": 0},
    {"name": "Tennis-MD", "category": "Tennis", "min_team_size": 2, "max_team_size": 2, "min_females": 0, "min_males": 0},
    {"name": "Pentathlon", "category": "NonMajor", "min_team_size": 1, "max_team_size": 1, "min_females": 0, "min_males": 0},
    {"name": "Pentathlon-W", "category": "NonMajor", "min_team_size": 1, "max_team_size": 1, "min_females": 0, "min_males": 0},
]

# Iterate over each object and send a POST request
for obj in objects:
    response = requests.post(url, json=obj)
    print(response.status_code, response.content)
