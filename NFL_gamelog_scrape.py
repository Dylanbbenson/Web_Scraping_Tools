import numpy as np
import pandas as pd
import random as rdom
import argparse
import time
import datetime

currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
current_year = date.strftime("%Y")

def get_user_input():
    team = input("Enter the team (empty = get all teams): ")
    season = input("Enter the season (empty = current season only): ")
    if season == '':
        season = current_year
    return team, season

## Main script Logic
def main(team, season):
    
    teams = ['crd', 'atl', 'rav', 'buf', 'car', 'chi', 'cin', 'cle', 'dal', 'den', 'det', 'gnb', 'htx', 'clt', 'jax', 'kan', 'sdg', 'ram', 'rai', 'mia', 'min', 'nwe', 'nor', 'nyg', 'nyj', 'phi', 'pit', 'sea', 'sfo', 'tam', 'oti', 'was']

    if team != '':
        teams = [team]
    seasons = [str(season) for season in range(int(season), int(current_year))]

    print(f"Scraping gamelog data...")
    
    gamelog_df = pd.DataFrame()
    for season in seasons:
        for team in teams:
            url = 'https://www.pro-football-reference.com/teams/' + team +'/' + season + '/gamelog/'

            offense_df = pd.read_html(url, header=1, attrs={'id':'gamelog' + season})[0]

            defense_df = pd.read_html(url, header=1, attrs={'id':'gamelog_opp' + season})[0]

            team_df = pd.concat([offense_df, defense_df], axis=1)

            team_df.insert(loc=0, column='Season', value=season)
            team_df.insert(loc=2, column='Team', value=team.upper())

            gamelog_df = pd.concat([gamelog_df, team_df], ignore_index=True)

            time.sleep(rdom.randint(4,5))

    if len(teams) > 1:
        gamelog_df.to_csv("./data/nfl_gamelogs.csv", index=False)
        print(f"Gamelog data for seasons {season} - {current_year} successfully pulled for all teams")
    else:
        gamelog_df.to_csv("./data/"+team+"_gamelogs.csv", index=False)
        print(f"Gamelog data for seasons {season} - {current_year} successfully pulled for: {team}")
            
            
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--team", help="Team Name")
    parser.add_argument("--season", help="Season")
    args = parser.parse_args()

    if args.team and args.season:
        main(args.team, args.season)
    else:
        team, season = get_user_input()
        main(team, season)
