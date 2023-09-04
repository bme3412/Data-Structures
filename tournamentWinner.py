competitions = [
    ['HTML', 'C#'],
    ['C#', 'Python'],
    ['Python', 'HTML']
] # in the form of [homeTeam, awayTeam]

results = [0,0,1]
# 1 = home team won, #0 = away team won



def tournamentWinner(competitons, results):
    
    for i in range(len(competitons)):
        if results[i] == 1:
            return competitons[i][0]
        else:
            return competitons[i][1]
    

print(tournamentWinner(competitions, results))