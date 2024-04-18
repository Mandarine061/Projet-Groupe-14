#-*- coding: utf-8 -*-

import math
game = {}


# other functions

def choose_action(board_dictionary, players_dictionary, player_id):
    """
    chooses the best action
    
    Paramaters
    ----------
    board_dictionary: The dictionary with all the game board's informations.(dict)
    players_dictionary: The dictionary with all player's informations (dict)
    player_id: player id of AI (int)

    Retruns
    -------
    chosen_action : the action chosen by the AI (str)
    """
    forbidden_position = []
    owned_sheep = []
    enemy_sheep = []
    seeds_pos = []
    enemy_grass = []
    action = []

    """
    for position_x in range(int(board_dictionary['map'][0])):
        forbidden_position.append([position_x, -1]) # 0 ???? parce que dans le BD on commence avec 0 mais si on change et qu'on commence avec 1 ALORS CHANGER ICI AUSSI 
        forbidden_position.append([position_x, int(board_dictionary['map'][1])+1])
    for position_y in range(int(board_dictionary['map'][1])):
        forbidden_position.append([-1, position_y]) 
        forbidden_position.append([int(board_dictionary['map'][0])+1, position_y])# NE PAS OUBLIER LES LIMITES AUX BORDS DU TABLEAU (LES COINS)
    """    

    for rock in board_dictionary:
        forbidden_position.append([int(rock[0]), int(rock[1])])
    for spawn in board_dictionary:
        forbidden_position.append([int(spawn[1]), int(spawn[2])])
    for seeds in board_dictionary:
        seeds_pos.append([int(seeds[0]), int(seeds[1])])
    # ne pas oublier les limites de la map à mettre dans get ai orders, c'est elle qui va bouger le moutons de place
    for player in players_dictionary:
        if player == 'player_1':
            nb = 1
        else:
            nb = 2  
        for sheep in players_dictionary[player]['sheep']:
            if nb == player_id:
                owned_sheep.append(sheep)
            else:
                enemy_sheep.append(sheep)
        for grass in players_dictionary[player]['grass']:
            if nb != player_id:
                enemy_grass.append(grass)

    for our_sheep in owned_sheep: 
        for near_sheep in enemy_sheep:
            for forbidden_square in range(0, 5):
                for forbidden_square_bis in range(0,5):
                    if [near_sheep[0]+forbidden_square, near_sheep[1]+forbidden_square_bis] not in forbidden_position:
                        forbidden_position.append([near_sheep[0]+forbidden_square, near_sheep[1]+forbidden_square_bis])

                    if [near_sheep[0]+forbidden_square, near_sheep[1]-forbidden_square_bis] not in forbidden_position:
                        forbidden_position.append([near_sheep[0]+forbidden_square, near_sheep[1]-forbidden_square_bis])

                    if [near_sheep[0]-forbidden_square, near_sheep[1]+forbidden_square_bis] not in forbidden_position:
                        forbidden_position.append([near_sheep[0]-forbidden_square, near_sheep[1]+forbidden_square_bis])

                    if [near_sheep[0]-forbidden_square, near_sheep[1]-forbidden_square_bis] not in forbidden_position:
                        forbidden_position.append([near_sheep[0]-forbidden_square, near_sheep[1]-forbidden_square_bis])
        for grass in enemy_grass:
            if -8<=(our_sheep[0]-enemy_grass[0])<=8 or -8<=(our_sheep[1]-enemy_grass[1])<=8:
                action.append('grass' + str([our_sheep][0]) + str([our_sheep][1]) + str([grass][0]) + str([grass][1])) 
        for seed in seeds_pos:
            if -8<=(our_sheep[0]-seed[0])<=8 or -8<=(our_sheep[1]-seed[1])<=8:
                action.append('seed ' + str([our_sheep][0]) + str([our_sheep][1]) + str([seed][0]) + str([seed][1]))

    return [action, forbidden_position]
            




"""
la fonction est censée regarder chaque mouton(boucle) et choisir la meilleure action possible en mettant une suite de if et elif afin que si par 
exemple un mouton adverse est très proche, alors faut l'attaquer, en revanche, si c'est une case de graines qui est plus proche alors idéalement,
déplacer le mouton vers cette case afin qu'il les broute et soit propriétaire de cette case

ne pas oublier que on peut AJOUTER du codes aux squelettes 

c'est le module de l'IA qu'on va importer sur le module du jeu
"""





# main function - if necessary, other parameters can be used
def get_AI_orders(board_dictionary, players_dictionary, player_id):
    """Return orders of AI.
    
    Parameters
    ----------
    board_dictionary: The dictionary with all the game board's informations.(dict)
    players_dictionary: The dictionary with all player's informations (dict)
    player_id: player id of AI (int)

    Returns
    -------
    orders: orders of AI (str)
    
    """
    actions = choose_action(board_dictionary, players_dictionary, player_id)
    action = actions[0]
    forbidden_position = actions[1]
    for sheep in players_dictionary['player_' + str(player_id)]['sheep']:
        if 'seed ' in action or 'grass' in action:
            if sheep[1] == [int(action[6]), int(action[7])]:
                
          for player in players_dictionary:
                if player == 'player_1':
                    nb = 1
                else:
                    nb = 2 
    if nb == player_id:
        if 'menaced' in action:
            our_sheep = [sheep[8], sheep[9]] #en faire des listes our_sheep et enemy_sheep
            enemy_sheep = [sheep[10], sheep[11]]

          
            


        #for sheep in players_dictionary['player_' + str(player_id)]['sheep']: ????
        #faire en sorte que notre mouton aille suffisament loin de l'autre (8 cases) et si au passage il y'a des trucs à manger dans les cases qui sont ok alors on y va 
        #faire aussi en sorte queles alentours de tous les moutons ennemis soient en position interdite
    ...
    ...
    
    return action