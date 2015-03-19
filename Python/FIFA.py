import random

teams = {0: "Arsenal",
         1: "Liverpool",
         2: "Inter Milan",
         3: "Fiorentina",
         4: "Chelsea",
         5: "Spurs",
         6: "Manchester United",
         7: "Manchester City",
         8: "PSG",
         9: "VfL Wolfsburg",
         10: "FC Shalke 04",
         11: "FC Bayern",
         12: "Dortmund",
         13: "Bayer Leverkeusen",
         14: "Juventus",
         15: "Lazio",
         16: "AS Monaco",
         17: "AC Milan",
         18: "Napoli",
         19: "Roma",
         20: "Porto",
         21: "SL Benfica",
         22: "Zenit",
         23: "Athletic Bilbao",
         24: "Atletico Madrid",
         25: "Barcelona",
         26: "Real Madrid",
         27: "Sevilla FC",
         28: "Valencia CF",
         }

results = []

while len(results) < 3:
    randKey = random.randint(0, len(teams) - 1)
    if randKey in teams:
        results.append(teams.pop(randKey))

print results

