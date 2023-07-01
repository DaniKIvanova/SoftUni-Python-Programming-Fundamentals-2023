sequence_of_cards = input().split()

total_players_team_a = 11
total_players_team_b = 11

removed_players_team_a = []
removed_players_team_b = []

game_is_terminated = False

for given_card in sequence_of_cards:
    given_card = given_card.split("-")
    team = given_card[0]
    player = given_card[1]
    if team == "A":
        if player not in removed_players_team_a:
            total_players_team_a -= 1
            removed_players_team_a.append(player)
    elif team == "B":
        if player not in removed_players_team_b:
            total_players_team_b -= 1
            removed_players_team_b.append(player)
    if total_players_team_b < 7 or total_players_team_a < 7:
        game_is_terminated = True
        break

print(f"Team A - {total_players_team_a}; Team B - {total_players_team_b}")

if game_is_terminated:
    print("Game was terminated")