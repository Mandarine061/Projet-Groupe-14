#-*- coding: utf-8 -*-

import math, random
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

    for rock in board_dictionary:
        forbidden_position.append([int(rock[0]), int(rock[1])])
    for spawn in board_dictionary:
        forbidden_position.append([int(spawn[1]), int(spawn[2])])
    for seeds in board_dictionary:
        seeds_pos.append([int(seeds[0]), int(seeds[1])])
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
            if -8<=(our_sheep[0]-near_sheep[0])<=8 or -8<=(our_sheep[1]-near_sheep[1])<=8:
                action.append('threat' + str([our_sheep][0]) + str([our_sheep][1]) + str([near_sheep][0]) + str([near_sheep][1])) 
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
                action.append('grass ' + str([our_sheep][0]) + str([our_sheep][1]) + str([grass][0]) + str([grass][1])) 
        for seed in seeds_pos:
            if -8<=(our_sheep[0]-seed[0])<=8 or -8<=(our_sheep[1]-seed[1])<=8:
                action.append('seed  ' + str([our_sheep][0]) + str([our_sheep][1]) + str([seed][0]) + str([seed][1]))

    return [action, forbidden_position]


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
    orders = ''
    attack = random.randint(1, 2)
    actions = choose_action(board_dictionary, players_dictionary, player_id)
    action = actions[0]
    forbidden_position = actions[1]
    for sheep in players_dictionary['player_' + str(player_id)]['sheep']:
        if 'seed  ' in action:
            if sheep[1] == [int(action[7]), int(action[8])] and [int(action[9]), int(action[10])] not in forbidden_position:
                orders += str(action[7]) + '-' + str(action[8]) + ':@' + str(action[9]) + '-' + str(action[10]) + ' '
        elif 'grass ' in action:
            if sheep[1] == [int(action[7]), int(action[8])] and [int(action[9]), int(action[10])] not in forbidden_position:
                orders += str(action[7]) + '-' + str(action[8]) + ':*' + str(action[9]) + '-' + str(action[10]) + ' '
        elif 'threat' in action and attack == 1:
            orders += str(action[7]) + '-' + str(action[8]) + ':x' + str(action[9]) + '-' + str(action[10]) + ' '
        else:
            while sheep[1] == sheep[1]:
                new_pos_x = random.randint(1,8)
                new_pos_y = random.randint(1,8)
                if ([sheep[1][0] + new_pos_x, sheep[1][1] + new_pos_y] not in forbidden_position 
                    and (sheep[1][0] + new_pos_x) >= int(board_dictionary['map'][0]) and (sheep[1][1] + new_pos_y) >= int(board_dictionary['map'][1])):
                    ex_pos_x = sheep[1][0]
                    ex_pos_y = sheep[1][1]
                    sheep[1][0] += new_pos_x
                    sheep[1][1] += new_pos_y
                    orders += str(ex_pos_x) + '-' + str(ex_pos_y) + ':@' + str(sheep[1][0]) + '-' + str(sheep[1][1]) + ' '
    return orders