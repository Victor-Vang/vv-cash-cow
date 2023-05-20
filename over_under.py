import argparse
import inquirer
import project_utils


class BettingMatchup: 
    def __init__(self, sport: str):
        self.sport = sport.lower()
        self.data = None

    def load_data(self):
        self.data = project_utils.loadYamlAsObject(f"{self.sport}.yaml")
        
        return self.data

    def select_team(self):
        # team_choices = [inquirer.Choice(name=team.name["name"], value=abbreviation) for abbreviation, team in self.data.teams]

        # team_choices = [team_data["name"] for team_data in self.data.teams_iterator()]

        # team_choices = [{"name": team_data["name"], "value": abbreviation} for abbreviation, team_data in self.data.teams.items()]
        team_choices = [team.name for team in self.data.teams.__dict__.values()]

        print(team_choices)
        questions = [inquirer.List("team", message="Please select a team", choices=team_choices)]
        
        team_choice = inquirer.prompt(questions)
        
        return team_choice.get("team")

# [!!!]

parser = argparse.ArgumentParser(description="Over/Under Analysis Tool")
parser.add_argument("--sport", choices=["NBA", "NCAAF", "NFL", "WNBA",], help="Select a sport: NBA, NCAAF NFL, WNBA")
args = parser.parse_args()
sport_selection = args.sport

if not sport_selection:
    sports_options = [inquirer.List("sport", message="Please select a sport", choices=["NBA", "NCAAF", "NFL", "WNBA"]),]

    answers = inquirer.prompt(sports_options)
    sport_selection = answers["sport"]

sport = ""

if sport_selection == "WNBA":
    sport = "WNBA"

print(sport)
bet = BettingMatchup(sport)
data = bet.load_data()
bet.select_team()
