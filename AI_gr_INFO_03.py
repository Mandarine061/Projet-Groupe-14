#-*- coding: utf-8 -*-

import math, random
game = {}


# other functions

def choose_action(board_dictionary, players_dictionary, player_id):
    """
    chooses the best action.
    
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
    already_executed = []


    for rock in board_dictionary['rocks']:
        forbidden_position.append([int(rock[0]), int(rock[1])])
    for spawn in board_dictionary['spawn']:
        forbidden_position.append([int(spawn[1]), int(spawn[2])])
    for seeds in board_dictionary['seeds']:
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
                if -8<=(our_sheep[1][0]-near_sheep[1][0])<=8 and -8<=(our_sheep[1][1]-near_sheep[1][1])<=8 and our_sheep[1] not in already_executed:
                    action.append(['threat',[str(our_sheep[1][0]), str(our_sheep[1][1])], [str(near_sheep[1][0]), str(near_sheep[1][1])]])
                    already_executed.append(our_sheep[1])
                for forbidden_square in range(0, 9):
                    for forbidden_square_bis in range(0,9):
                        if [near_sheep[1][0]+forbidden_square, near_sheep[1][1]+forbidden_square_bis] not in forbidden_position:
                            forbidden_position.append([near_sheep[1][0]+forbidden_square, near_sheep[1][1]+forbidden_square_bis])

                        if [near_sheep[1][0]+forbidden_square, near_sheep[1][1]-forbidden_square_bis] not in forbidden_position:
                            forbidden_position.append([near_sheep[1][0]+forbidden_square, near_sheep[1][1]-forbidden_square_bis])

                        if [near_sheep[1][0]-forbidden_square, near_sheep[1][1]+forbidden_square_bis] not in forbidden_position:
                            forbidden_position.append([near_sheep[1][0]-forbidden_square, near_sheep[1][1]+forbidden_square_bis])

                        if [near_sheep[1][0]-forbidden_square, near_sheep[1][1]-forbidden_square_bis] not in forbidden_position:
                            forbidden_position.append([near_sheep[1][0]-forbidden_square, near_sheep[1][1]-forbidden_square_bis])
            for grass in enemy_grass:
                if -8<=(our_sheep[1][0]-grass[1][0])<=8 and -8<=(our_sheep[1][1]-grass[1][1])<=8 and our_sheep[1] != grass[1] and our_sheep[1] not in already_executed:
                    action.append(['grass', [str(our_sheep[1][0]), str(our_sheep[1][1])], [str(grass[1][0]), str(grass[1][1])]]) 
                    already_executed.append(our_sheep[1])
                if our_sheep[1] == grass[1]:
                    action.append(['graze', [str(our_sheep[1][0]), str(our_sheep[1][1])]])
            for seed in seeds_pos:
                if -8<=(our_sheep[1][0]-seed[0])<=8 and -8<=(our_sheep[1][1]-seed[1])<=8 and our_sheep[1] not in already_executed:
                    action.append(['seed', [str(our_sheep[1][0]), str(our_sheep[1][1])], [str(seed[0]), str(seed[1])]])
                    already_executed.append(our_sheep[1])


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
    attack =  random.randint(1, 2)
    action_forbidden_pos = choose_action(board_dictionary, players_dictionary, player_id)
    actions = action_forbidden_pos[0]
    forbidden_position = action_forbidden_pos[1]
    new_pos_x = random.randint(-8,9)
    new_pos_y = random.randint(-8,9)
    if len(players_dictionary['player_' + str(player_id)]['grass']) >= 30 and len(players_dictionary['player_' + str(player_id)]['sheep']) < 2:
        orders += 'sheep '
    if len(players_dictionary['player_' + str(player_id)]['grass']) >= 60 and len(players_dictionary['player_' + str(player_id)]['sheep']) < 3:
        orders += 'sheep '
    if len(players_dictionary['player_' + str(player_id)]['grass']) >= 90 and len(players_dictionary['player_' + str(player_id)]['sheep']) < 4:
        orders += 'sheep '

    for action in actions:
        for sheep in players_dictionary['player_' + str(player_id)]['sheep']:
            ex_pos_x = sheep[1][0]
            ex_pos_y = sheep[1][1]
            if 'seed' in action:
                if action[2] not in forbidden_position and action[1][0] + '-' + action[1][1] not in orders:
                    orders += action[1][0] + '-' + action[1][1] + ':@' + action[2][0] + '-' + action[2][1] + ' '
            if 'grass' in action:
                if action[2] not in forbidden_position and action[1][0] + '-' + action[1][1] not in orders:
                    orders += action[1][0] + '-' + action[1][1] + ':@' + action[2][0] + '-' + action[2][1] + ' '
            elif 'graze' in action:
                if action[1][0] + '-' + action[1][1] not in orders:
                    orders +=  action[1][0] + '-' + action[1][1] + ':*' + ' '
            elif 'threat' in action and attack == 1 and action[1][0] + '-' + action[1][1] not in orders:
                orders += action[1][0] + '-' + action[1][1] + ':x' + action[2][0] + '-' + action[2][1] + ' '
            elif 'threat' in action and attack == 2 and str(ex_pos_x) + '-' + str(ex_pos_y) not in orders:         
                if ([sheep[1][0] + new_pos_x, sheep[1][1] + new_pos_y] not in forbidden_position):
                    if sheep[1][0] + new_pos_x < 0:
                        sheep[1][0] = 0
                    elif sheep[1][0] + new_pos_x > int(board_dictionary['map'][0]):
                        sheep[1][0] = int(board_dictionary['map'][0])
                    else:
                        sheep[1][0] += new_pos_x
                    if sheep[1][1] + new_pos_y < 0:
                        sheep[1][1] = 0
                    elif sheep[1][1] + new_pos_y > int(board_dictionary['map'][1]):
                        sheep[1][0] = int(board_dictionary['map'][1])
                    else:
                        sheep[1][1] += new_pos_y
                    orders += str(ex_pos_x) + '-' + str(ex_pos_y) + ':@' + str(sheep[1][0]) + '-' + str(sheep[1][1]) + ' '
    return orders



