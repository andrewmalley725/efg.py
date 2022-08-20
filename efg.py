import pandas as pd

df = pd.read_csv('./data/shots_data.csv').to_dict('records')
stats = []
teams = []
totals = []
for i in df: 
    if i['team'] not in teams:
        teams.append(i['team'])

def eFG(FGM, _3PM, FGA):
    if FGA == 0:
        return 'N/A'
    return (FGM + (.5 * _3PM)) / FGA

for i in teams:
    team_stats = {
        'team': i,
        'C3PA': 0,
        'C3PM': 0,
        'NC3PA': 0,
        'NC3PM': 0,
        '2PTA': 0,
        '2PTM': 0,
        'FGA': 0
    }
    for j in df:
        if j['team'] == i:
            if abs(j['y']) > 7.8 and abs(j['x']) > 23.75:
                if j['fgmade']:
                    team_stats['NC3PM'] += 1
                team_stats['NC3PA'] += 1
            elif abs(j['y']) <= 7.8 and abs(j['x']) > 22:
                if j['fgmade']:
                    team_stats['C3PM'] += 1
                team_stats['C3PA'] += 1
            else:
                if j['fgmade']:
                    team_stats['2PTM'] += 1
                team_stats['2PTA'] += 1
            team_stats['FGA'] += 1
    stats.append(team_stats)

for i in stats:
    FGA = i['NC3PA'] + i['C3PA'] + i['2PTA']
    dit = {
        'team' : i['team'],
        'FGA' : FGA,
        '2PCT' : i['2PTA'] / FGA,
        '2PTefG' : eFG(i['2PTM'], (i['NC3PM'] + i['C3PM']), i['2PTA']), 
        'NC3PCT' : i['NC3PA'] / FGA,
        'NC3PeFG' : eFG(i['NC3PM'], (i['NC3PM'] + i['C3PM']), i['NC3PA']),
        'C3PCT' : i['C3PA'] / FGA,
        'C3PeFG': eFG(i['C3PM'], (i['NC3PM'] + i['C3PM']), i['C3PA'])
    }
    totals.append(dit)

print(totals)

