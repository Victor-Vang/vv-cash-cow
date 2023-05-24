import argparse
import inquirer
import project_utils


class SportSelector:
    def __init__(self):
        self.sport = None

    def select_sport(self):
        parser = argparse.ArgumentParser(description="Over/Under Analysis Tool")
        parser.add_argument("--sport", choices=["NBA", "NCAAF", "NFL", "WNBA",], help="Select a sport: NBA, NCAAF NFL, WNBA")
        args = parser.parse_args()
        self.sport = args.sport

        if not self.sport:
            sports_options = [inquirer.List("sport", message="Please select a sport", choices=["NBA", "NCAAF", "NFL", "WNBA"]),]
            answers = inquirer.prompt(sports_options)
            self.sport = answers["sport"]
        
        print(f"You selected the {self.sport}!\n")

        return self.sport


class BettingMatchup: 
    def __init__(self, sport: str):
        self.sport = sport.lower()
        self.data = None
        self.team_name = None
        self.team_abbreviation = None

    def load_data(self):
        if self.sport != "wnba":
            raise ValueError("This sport has yet to be implimented! Patience!")
        self.data = project_utils.loadYamlAsObject(f"{self.sport}.yaml")
        
        return self.data


    def select_team(self):
        team_choices = [team.name for team in self.data.teams.__dict__.values()]
        questions = [inquirer.List("team", message="Please select a team", choices=team_choices)]
        team_choice = inquirer.prompt(questions)
        selected_team = team_choice.get("team")

        self.extract_team_info(selected_team)

        print(f"You chose the {self.team_name}!")

        attribute = getattr(self.data.teams, self.team_abbreviation.lower())
        print(attribute.urls)

        return selected_team
    
    def extract_team_info(self, selected_team: str):
        parts = selected_team.split(" (")
        self.team_name = parts[0]
        self.team_abbreviation = parts[1][:-1]
    

if __name__ == "__main__":
    selector = SportSelector()
    sport = selector.select_sport()

    matchup = BettingMatchup(sport)
    matchup.load_data()
    chosen_team = matchup.select_team()
