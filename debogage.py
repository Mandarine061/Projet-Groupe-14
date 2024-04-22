def choose_action(board_dictionary, players_dictionary, player_id):
    """
    chooses the best action
    
    Paramaters
    ----------
    board_dictionary: The dictionary with all the game board's informations.(dict)
    players_dictionary: The dictionary with all player's informations (dict)
    player_id: player id of AI (int)

    Returns
    -------
    chosen_action : the action chosen by the AI (list)
    """
    forbidden_position = []
    owned_sheep = []
    enemy_sheep = []
    seeds_pos = []
    enemy_grass = []
    action = [] 
    already_executed = []

    # Populate the lists with relevant data
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

    # Debug messages
    print("Owned Sheep:", owned_sheep)
    print("Enemy Sheep:", enemy_sheep)
    print("Seeds Position:", seeds_pos)
    print("Enemy Grass:", enemy_grass)
    print("Forbidden Positions:", forbidden_position)

    # Process each owned sheep
    for our_sheep in owned_sheep:
        for near_sheep in enemy_sheep:
            if -8<=(our_sheep[1][0]-near_sheep[1][0])<=8 or -8<=(our_sheep[1][1]-near_sheep[1][1])<=8 and our_sheep[1] not in already_executed:
                print(our_sheep[1])
                print(already_executed)
                action.append(['threat',[str(our_sheep[1][0]), str(our_sheep[1][1])], [str(near_sheep[1][0]), str(near_sheep[1][1])]])
                already_executed.append(our_sheep[1])
            for forbidden_square in range(0, 5):
                for forbidden_square_bis in range(0,5):
                    if [near_sheep[1][0]+forbidden_square, near_sheep[1][1]+forbidden_square_bis] not in forbidden_position:
                        forbidden_position.append([near_sheep[1][0]+forbidden_square, near_sheep[1][1]+forbidden_square_bis])

                    if [near_sheep[1][0]+forbidden_square, near_sheep[1][1]-forbidden_square_bis] not in forbidden_position:
                        forbidden_position.append([near_sheep[1][0]+forbidden_square, near_sheep[1][1]-forbidden_square_bis])

                    if [near_sheep[1][0]-forbidden_square, near_sheep[1][1]+forbidden_square_bis] not in forbidden_position:
                        forbidden_position.append([near_sheep[1][0]-forbidden_square, near_sheep[1][1]+forbidden_square_bis])

                    if [near_sheep[1][0]-forbidden_square, near_sheep[1][1]-forbidden_square_bis] not in forbidden_position:
                        forbidden_position.append([near_sheep[1][0]-forbidden_square, near_sheep[1][1]-forbidden_square_bis])
        for grass in enemy_grass:
            if -8<=(our_sheep[1][0]-grass[1][0])<=8 or -8<=(our_sheep[1][1]-grass[1][1])<=8 and our_sheep[1] not in already_executed:
                print(our_sheep[1])
                print(already_executed)
                action.append(['grass', [str(our_sheep[1][0]), str(our_sheep[1][1])], [str(grass[1][0]), str(grass[1][1])]]) 
                already_executed.append(our_sheep[1])
        for seed in seeds_pos:
            if -8<=(our_sheep[1][0]-seed[0])<=8 or -8<=(our_sheep[1][1]-seed[1])<=8 and our_sheep[1] not in already_executed:
                print(our_sheep[1])
                print(already_executed)
                action.append(['seed', [str(our_sheep[1][0]), str(our_sheep[1][1])], [str(seed[0]), str(seed[1])]])
                already_executed.append(our_sheep[1])

    # Debug messages
    print("Action:", action)
    
    print("Already Executed:", already_executed)

    return [action]

board_dictionary = {'rocks':[['1','2'], ['3','6'], ['9','11'], ['4','16']], 
                    'map':['20','20'], 
                    'spawn':[['1','12','5'], ['2','6','8']],
                    'seeds':[['13','13'], ['3', '4'], ['7','8'], ['9','8']]}
             
             
players_dictionary = {'player_1':{'sheep':[[1, [4 ,6]], [3, [6, 6]]],
                      'grass': [[2, [4, 12]], [2, [5, 12]], [2, [4, 11]], [2, [4, 13]]]},
                      'player_2':{'sheep':[[2, [15, 17]], [2, [6, 12]]],
                      'grass': [[11, [16, 13]], [1, [16, 12]], [1, [17, 13]], [1, [15, 13]], [1, [16, 14]]]}}

print(choose_action(board_dictionary, players_dictionary, 1))
