# How to Calculate Points and Goal Difference
# team = { "name": "Manchester United", "wins": 30, "loss": 3, "draws": 5, "scored": 88, "conceded": 20 }
#
# Total Points = 3 * wins + 0 * loss + 1 * draws = 3 * 30 + 0 * 3 + 5 * 1 = 95 points
# Goal Difference = scored - conceded = 88 - 20 = 68
# Examples
# champions([
#   {
#     "name": "Manchester United",
#     "wins": 30,
#     "loss": 3,
#     "draws": 5,
#     "scored": 88,
#     "conceded": 20,
#   },
#   {
#     "name": "Arsenal",
#     "wins": 24,
#     "loss": 6,
#     "draws": 8,
#     "scored": 98,
#     "conceded": 29,
#   },
#   {
#     "name": "Chelsea",
#     "wins": 22,
#     "loss": 8,
#     "draws": 8,
#     "scored": 98,
#     "conceded": 29,
#   }
# ]) ➞ "Manchester United"
# Examples
# champions([
#   {
#     "name": "Manchester United",
#     "wins": 30,
#     "loss": 3,
#     "draws": 5,
#     "scored": 88,
#     "conceded": 20,
#   },
#   {
#     "name": "Arsenal",
#     "wins": 24,
#     "loss": 6,
#     "draws": 8,
#     "scored": 98,
#     "conceded": 29,
#   },
#   {
#     "name": "Chelsea",
#     "wins": 22,
#     "loss": 8,
#     "draws": 8,
#     "scored": 98,
#     "conceded": 29,
#   }
# ]) ➞ "Manchester United"
# Notes
# Input is a list of teams.

def champions(items):
    max_point = -1
    max_team = ''
    for team in items:
        points = 3 * team['wins'] + 1 * team['draws']
        goal_diff = team['scored'] - team['conceded']
        if points > max_point:
            max_point = points
            max_team = team['name']
        elif points == max_point and goal_diff > 0:
            max_team = team['name']
        return max_team


team = [
    {
        "name": "Manchester United",
        "wins": 30,
        "loss": 3,
        "draws": 5,
        "scored": 88,
        "conceded": 20,
    },
    {
        "name": "Arsenal",
        "wins": 24,
        "loss": 6,
        "draws": 8,
        "scored": 98,
        "conceded": 29,
    },
    {
        "name": "Chelsea",
        "wins": 22,
        "loss": 8,
        "draws": 8,
        "scored": 98,
        "conceded": 29,
    }
]
team1 = [

    {
        "name": "Manchester United",
        "wins": 30,
        "loss": 3,
        "draws": 5,
        "scored": 88,
        "conceded": 20,
    },
    {
        "name": "Arsenal",
        "wins": 24,
        "loss": 6,
        "draws": 8,
        "scored": 98,
        "conceded": 29,
    },
    {
        "name": "Chelsea",
        "wins": 22,
        "loss": 8,
        "draws": 8,
        "scored": 98,
        "conceded": 29,
    }
]
print(champions(team))
