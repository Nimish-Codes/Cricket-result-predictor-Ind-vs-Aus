import pandas as pd
import streamlit as st

def evaluate_player_performance(players):
    players['Performance'] = players['TotRuns'] + players['Hunds'] * 100 + players['Fifties'] * 50

def compare_teams(team1, team2):
    total_performance_team1 = team1['Performance'].sum()
    total_performance_team2 = team2['Performance'].sum()

    if total_performance_team1 > total_performance_team2:
        return "Team Ind wins!"
    elif total_performance_team1 < total_performance_team2:
        return "Team Aus wins!"
    else:
        return "It's a tie!"

# Read CSV files
table1 = pd.read_csv('IndTim.csv')
table2 = pd.read_csv('AusTim.csv')

# Create Streamlit app
st.title("Cricket Team Result Predictor For Ind vs Aus")
st.subheader("Now make your own team and see which team wins")

# Team 1 multiselect
selected_players_team1 = st.multiselect("Select 11 players from Team Ind:", table1['Name'], key='team1')

# Team 2 multiselect
selected_players_team2 = st.multiselect("Select 11 players from Team Aus:", table2['Name'], key='team2')

# Button to evaluate teams
if st.button("Evaluate Teams"):
    # Check if both teams have 11 players selected
    if len(selected_players_team1) != 11 or len(selected_players_team2) != 11:
        st.error("Please select exactly 11 players for each team.")
    else:
        # Get the selected players
        selected_players_table1 = table1[table1['Name'].isin(selected_players_team1)]
        selected_players_table2 = table2[table2['Name'].isin(selected_players_team2)]

        # Evaluate player performance
        evaluate_player_performance(selected_players_table1)
        evaluate_player_performance(selected_players_table2)

        # Compare teams
        result = compare_teams(selected_players_table1, selected_players_table2)

        # Display selected players and result
        st.write("Selected Players from Team Ind:")
        st.dataframe(selected_players_table1)

        st.write("\nSelected Players from Team Aus:")
        st.dataframe(selected_players_table2)

        st.write("\n*Result:", result)

        st.warning("\nDisclaimer: The provided prediction is based on player's previous T20 stats.\n\nThere may be some alter values in the app's data according to sources.")
