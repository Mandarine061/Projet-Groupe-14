#-*- coding: utf-8 -*-

import blessed, math, os, time
term = blessed.Terminal()

from remote_play import create_connection, get_remote_orders, notify_remote_orders, close_connection



# other functions

def create_board_dictionary(file_bsh):
    """ Creates the board dictionary with all the infromations regarding the playing board found in the bsh file (on webcampus).
    
    Parameters
    -----------
    file_bsh : a file with all the information needed to create the dictionary (file).

    Returns
    -------
    board_dictionnary: return a dictionary with the informations of the board, the dictionary only has data for the relevent squares.(dict)
    
    Version
    -------
    specification: Abdusamed Mus (v1 07/03/2024)
    implémentation: Abdusamed Mus (v1 20/03/2024)
    
    """

    file = open(file_bsh, 'r')
    raw_list = file.readlines() # create a raw list with the content of the bsh file
    file.close()

    clean_list = []
    for raw_lines in raw_list:
        clean_lines = raw_lines.strip() # clean the raw list (remove the unnecessary whitespace and the \n)
        clean_lines = clean_lines.split(' ') # remove the whitespace to put commas instead + return every lines in  form of list
        clean_list.append(clean_lines)

    board_dictionary = {}
    board_dimension = clean_list[1] # the dimension are always going to be number 1 in the index 
    board_dictionary['map'] = board_dimension # put the board dimension in the board_dictionary

    spawn_1 = clean_list[3] # the spawns are always going to bu number 3 and 4
    spawn_2 = clean_list[4]
    board_dictionary['spawn'] = [spawn_1, spawn_2]  # put the board dimension in the board_dictionary

    seeds = []
    rocks = []
    # index of the 'seeds:' line is always going to be 5
    for lines in range(len(clean_list)):
        if (clean_list[lines] == ['rocks:']):
            start_of_rocks = lines # finds the index of the 'rocks' line in the clean list  
   
    for elements in range(len(clean_list)):
        if (5 < elements < start_of_rocks): # uses the indexes to isolate the seeds and put them in the board dictionary
            seeds.append(clean_list[elements]) 
        board_dictionary['seeds'] = seeds

        if (start_of_rocks < elements):
            rocks.append(clean_list[elements]) # put the rocks in the dictionary
        board_dictionary['rocks'] = rocks

    return board_dictionary

def create_players_dictionary(board_dictionary):
    """ Creates the dictionary with all the infromations regarding the two players at the beginning of the game only.

    Parameters
    ----------
    board_dictionary: The dictionary with all the game board's informations.(dict)

    Returns
    -------
    result : return a dictionary with the informations of each player.(dict)
    
    Version
    -------
    specification: Abdusamed Mus (v2 23/03/2024)
    implémentation: Abdusamed Mus (v1 23/03/2024)

    """

    players_dictionary = {} 
    for spawn in board_dictionary['spawn']:
        if (int(spawn[0])==1): 
            players_dictionary['player_1'] = {'sheep':[3, [int(spawn[1]), int(spawn[2])]], 'grass':[]}
        else: 
            players_dictionary['player_2'] = {'sheep':[3, [int(spawn[1]), int(spawn[2])]], 'grass':[]}

    return players_dictionary 

def create_board(board_dictionary, players_dictionary):
    """This function uses the informations contained in board_dictionary to create the game board with UTF8 symbols and 
    using blessed functions.
    
    Parameters:
    ----------
    board_dictionary: The dictionary with all the game board's informations.(dict)
    players_dictionary: The dictionary with all player's informations (dict)

    Version
    -------
    specification: Abdusamed Mus (v2 07/03/2024)
    implémentation: Abdusamed Mus (v2 24/03/2024)

    """

    print(term.home + term.clear + term.hide_cursor) # clears the screen and hides the cursor

    nb_row = int(board_dictionary['map'][0]) # defines the number of rows and columns based on the size of the map
    nb_col = int(board_dictionary['map'][1])
    # a  dictionary with all the colors of the grasses based on their level
    grass_colors = {1 : term.on_darkseagreen1, 2 : term.on_darkseagreen2, 3 : term.on_palegreen1, 4 : term.on_palegreen3, 5 : term.on_chartreuse3, 6 : term.on_chartreuse2,
            7 : term.on_green2, 8 : term.on_green3, 9 : term.on_green4, 10 : term.on_darkgreen, 11 : term.on_darkgreen}

    for coord_x in range(nb_row):
        for coord_y in range(nb_col): # two 'for' loops to set the location of all the squares
            couleur_1 = term.on_darkgoldenrod
            couleur_2 = term.on_orangered4
            char = ' ' # if none of the condition below are fulfilled, the character is a blank space
            if (coord_x == int(board_dictionary['spawn'][0][1]) and coord_y == int(board_dictionary['spawn'][0][2]) or coord_x == int(board_dictionary['spawn'][1][1]) and coord_y == int(board_dictionary['spawn'][1][2])):
                char = '*' # sets a '*' for the spawns
            for seeds in board_dictionary['seeds']:
                if (coord_x == int(seeds[0]) and coord_y == int(seeds[1])):
                    char = 's' # sets an 's' for each seed
            for rocks in board_dictionary['rocks']:
                if (coord_x == int(rocks[0]) and coord_y == int(rocks[1])):
                    char = 'r' # sets an 'r' for each rock
            for players in players_dictionary: # another loop to find the information for each player in the players_dictionary
                for sheep in players_dictionary[players]['sheep']:
                    if coord_x == int(sheep[1][0]) and coord_y == int(sheep[1][1]):
                        char = 'M' # sets a 'M' for each sheeps
                for grass in players_dictionary[players]['grass']:
                    if (grass[1][0] == coord_x and coord_y == grass[1][1]):
                        couleur_1 = grass_colors[grass[0]] # changes the color of the background for the grass (takes the colors based on the level of the grass 
                        couleur_2 = grass_colors[grass[0]] # in the 'grass_colors' dictionary

            
            if ((coord_x+coord_y) % 2): # a condition to take one square after another and make it a pattern
                # print two little squares on the terminal to make an actual square of the board (the charachter only appears on actual square of the board)
                # the color changes below to make a pattern unless it is a grass square
                print(term.move_yx(coord_x, coord_y*2) + couleur_1 + char + term.normal, end='') 
                print(term.move_yx(coord_x, (coord_y*2)+1) + couleur_1 + ' ' + term.normal, end='')
                
            else:
                print(term.move_yx(coord_x, coord_y*2) + couleur_2 + char + term.normal, end='')
                print(term.move_yx(coord_x, (coord_y*2)+1) + couleur_2 + ' ' + term.normal, end='')


def sheep_fights(players_dictionary, board_dictionary, order):
    """This function handles sheep fights on the game board based on the given order and updates the board parameter with the outcomes of the sheep fights.
    
    Parameters:
    -----------
    board_dictionnary: The current state of the game board.(dict)
    order: The order specifying sheep fights.(string)

    Returns
    None

    Version
    -------
    specification: Amrouni Zohra (v1 26/02/2024)
    implémentation: Mus Abdusamed ()
    """

    # 5 cases sauf si rocher mort moutons  +1 case (imaginer si encore mouton) encore et en dehors du plateau mouru UN MONTON PEUT ALLER DANS LES 8 CASES AUTOUR DE LUI MËME EN DIAGO
    # attaque peut se faire sur un moutons dans les 8 cases environnant notre mouton, mouton 1 reste sur sa case 
    # calculer Ancienne pos et nouvelle pos si case est bien dans les 8 case environnante 
    # MODIFIER MOVE SHEEP EN CONSEQUENCE SINON LE FOUDRE S ABATRA SUR VOUSSSSSSSS 
    # mettre dasn execute orders tout en int [[19,20],[20-18]] et mofier move sheep en conséquence 
    correct_distance = False
    if ((-8<=(order[0][0]-order[1][0])<=8) and (-8<=(order[0][1]-order[1][1])<=8)): # checks if the distance between the two positions of the sheeps
        correct_distance = True
    rocks_int = []
    for rocks in board_dictionary['rocks']:
        rocks_int += [int(rocks[0]), int(rocks[1])] # converts all the rocks coordinates to integers
    for player in players_dictionary:
            for other_player in players_dictionary:
                if (other_player != player):
                    for sheep in players_dictionary[player]['sheep']:
                        for enemy_sheep in players_dictionary[other_player]['sheep']:
                            if (sheep[1] == order[0] and enemy_sheep[1] == order[1] and correct_distance == True): 
                                if (enemy_sheep[0] > 1): # if the sheep has more than 1 life, withdraw one life 
                                    enemy_sheep[0]-=1 
                                    diff_x = order[0][0]-order[1][0] # calculates the difference between the coordinates to determine the direction of the recoil 
                                    diff_y = order[1][0]-order[0][1]
                                    if (diff_x < 0):
                                        diff_x *= -1
                                    if (diff_y < 0):
                                        diff_y *= -1
                                    if (diff_x <= diff_y): 
                                        recoil = 5 # the base recoil is 5
                                        for other_sheep in players_dictionary[player]['sheep']: # if there is already a sheep, the enemy sheep goes 5 squares away again  
                                            if (enemy_sheep == other_sheep):
                                                recoil += 5 
                                        if (order[0][0]-order[1][0] <= order[1][0]-order[0][1]): # determines the direction of the recoil
                                            enemy_sheep[1][1]-=recoil
                                        else:
                                            enemy_sheep[1][1]+=recoil
                                    else:
                                        if (order[0][0]-order[1][0] > order[1][0]-order[0][1]):
                                            enemy_sheep[1][0]-=recoil
                                        else:
                                            enemy_sheep[1][0]+=recoil
                                    for rocks in rocks_int: # if there is a rock on the new position of the enemy sheep, it dies
                                        if (enemy_sheep[1] == rocks or enemy_sheep[1][0] > int(board_dictionary['map'][0]) or enemy_sheep[1][1] > int(board_dictionary['map'][1])):
                                            enemy_sheep = []
                                else: # else, it dies
                                    enemy_sheep = []
def execute_orders(board_dictionary, players_dictionary, orders):
    """This function executes orders provided for a single game round.
    
    Parameters
    ----------
    orders: The given order(s) by the player(string)
    board_dictionary: The dictionary with all the game board's informations.(dict)
    players_dictionary: The dictionary with all player's informations (dict)

    Returns
    None

    Version
    -------
    specification: Malak El Maimouni (v1 26/02/2024)
    implementation : Malak El Maimouni (v1 18/03/2024)   
    """
    orders = orders.split(' ') # cuts the differents order in the strings
    for order in orders:
        action = order.split(':')
        if action[1] == '*': # analyses all the action and calls the right function to execute them
            action = action[0]
            action = action.split('-')
            action_int = []
            for coords in action:
                action_int.append(int(coords))
            graze_grass(players_dictionary, action_int) # to graze grass
        elif action[1][0] == 'x':
            action[1] = action[1].strip('x')
            action_int = []
            for coords in action:
                action_int.append(int(coords[0]), int(coords[1]))
            sheep_fights(players_dictionary, action_int) # to make the sheep fights
        elif action[1][0] == '@':
            action[1] = action[1].strip('@')
            move_sheep(players_dictionary, action_int ,board_dictionary) # to move the sheep

def check_end_game(players_dictionary, nbr_of_game_rounds):
    """This function checks whether the game has ended based on the given conditions.
    
    Parameters:
    -----------
    board_dictionnary: The current state of the game board.(dict)
    nbr_of_game_rounds: The total number of game rounds played.(int)
    
    Returns
    Result: 'True' if the game has ended, otherwise it returns 'False'.(bool)

    Version
    -------
    specification: Malak El maimouni (v1 26/02/2024)
    implementation : Malak El Maimouni (v1 18/03/2024)
    """
       
    for player in players_dictionary:
        nbr_of_grass_tiles = len(players_dictionary[player]['seeds'])

    if nbr_of_grass_tiles > 100 or nbr_of_game_rounds >= 20:
        return True
    
    return False

def grass_growth(players_dictionary, board_dictionary):
    """This function handles the growth of grass on the game board over a certain number of game rounds and updates the board parameter with the new grass growth.
    
    Parameters:
    ----------
    players_dictionary: The current state of each player. (dict)
    board_dictionnary: The current state of the game board.(dict)
    
    Returns
    None

    Version
    -------
    specification: Amrouni Zohra (v1 26/02/2024)

    """

    for player in players_dictionary:
        for grass_tile in players_dictionary[player]['grass']:
            if grass_tile[0] == 10:
                adjacent_positions = [[grass_tile[1][0]-1, grass_tile[1][1]], 
                                        [grass_tile[1][0]+1, grass_tile[1][1]],
                                        [grass_tile[1][0], grass_tile[1][1]-1],
                                        [grass_tile[1][0], grass_tile[1][1]+1]]
                occupied = False
                for position in adjacent_positions:
                    for other_grass_tile in players_dictionary[player]['grass']:
                        if other_grass_tile[1] == position:
                            occupied = True
                for rock in board_dictionary['rocks']:
                    if int(rock[0]) == grass_tile[1][0] and int(rock[1]) == grass_tile[1][1]:
                        occupied = True
                if occupied == False:
                    players_dictionary[player]['grass']+=[1, position]
                        
                
def move_sheep(players_dictionary, order, board_dictionary):
    """This function handles the movement of sheep on the game board based on the given order and updates the board parameter with the new positions of the sheep resulting from the movements.
    
    Parameters:
    ----------
    board_dictionary: The current state of the game board. (dict)
    order: The order specifying sheep movements. (string) #list

    Returns
    -------
    None

    Version
    -------
    specification: Amrouni Zohra (v1 26/02/2024)
     
       """

    sheep_pos = order[0].split('-') #list de str
    new_pos = order[1].split('-') #list de str

    if new_pos not in board_dictionary['rocks']:
        for player in players_dictionary:
            for sheep in players_dictionary[player]['sheep']:
                for other_sheep in players_dictionary[player]['sheep']:
                    if ((int(sheep_pos[0]) == sheep[0]) and (int(sheep_pos[1]) == sheep[1]) 
                        and (int(new_pos[0]) != other_sheep[0]) and (int(new_pos[1]) != other_sheep[1]) 
                        and (0 < new_pos[0] <= board_dictionary['map'][0]) and (0 < new_pos[1] <= board_dictionary['map'][1])
                        and (-8 <= (new_pos[0]-sheep_pos[0]) <= 8) and (-8 <= new_pos[1]-sheep_pos[1] <= 8)):
                            players_dictionary[player][sheep][1] = [int(new_pos[0]), int(new_pos[1])] 


def graze_grass(players_dictionary, order):
    """This function handles the action of sheep grazing grass on the game board based on the given order and updates the board parameter by removing grass from the tiles where sheep have grazed.
    
    Parameters:
    -----------
    players_dictionary: The current state of each player. (dict)
    order: The order specifying sheep grazing actions. (string)
    
    Returns
    -------
    None
    
    Version
    -------
    specification: Amrouni Zohra (v1 26/02/2024)
    """
    for player in players_dictionary:
        for other_player in players_dictionary:
            if (player != other_player):
                for grass in players_dictionary[other_player]['gass']:
                    if grass[1] == order: 
                        players_dictionary[other_player]['grass']-=[grass] 
    
def capture_seeds(players_dictionary, board_dictionary):
    """This function handles the action of capturing neutral seeds by sheep on the game board based on the given order and updates the board parameter by changing the ownership of neutral seeds.
    
    Parameters:
    -----------
    players_dictionary: The current state of each player. (dict)
    board_dictionnary: The current state of the game board.(dict)
    
    Returns
    None

    Version
    -------
    specification: Amrouni Zohra (v1 26/02/2024)
    """
    index_seed = 0
    for player in players_dictionary:
        for sheep in players_dictionary[player]['sheep']:
            for seed in board_dictionary['seeds']:
                seed_int = []
                seed_int.append(int(seed[0]), int(seed[1]))
                if seed_int == sheep[1]:
                    board_dictionary['seeds'][index_seed] = []
                    players_dictionary[player]['grass'] += [1, seed_int]
                else:
                    index_seed +=1

def get_AI_orders(players_dictionary, board_dictionary, player_nbr):
    """
    """
# main function
def play_game(map_path, group_1, type_1, group_2, type_2):
    """Play a game.
    
    Parameters
    ----------
    map_path: path of map file (str)
    group_1: group of player 1 (int)
    type_1: type of player 1 (str)
    group_2: group of player 2 (int)
    type_2: type of player 2 (str)
    
    Notes
    -----
    Player type is either 'human', 'AI' or 'remote'.
    
    If there is an external referee, set group id to 0 for remote player.
    
    """
    
    board_dictionary = create_board_dictionary('map.bsh')
    players_dictionary = create_players_dictionary (board_dictionary)
    nbr_of_game_rounds = 0
    fst_sheep = False
    scd_sheep = False
    trd_sheep = False

    # create connection, if necessary
    if type_1 == 'remote':
        connection = create_connection(group_2, group_1)
    elif type_2 == 'remote':
        connection = create_connection(group_1, group_2)

    ...
    ...
    ...

    while check_end_game(players_dictionary, nbr_of_game_rounds):
        
        for player in players_dictionary:
            if player == 'player_1':
                nb = 1
            else:
                nb = 2
            nbr_of_grass_tiles = len(players_dictionary[player]['seeds']) # allows a player to have an additcional sheep every 30 new grass tiles
            for spawn in board_dictionary['spawn']:
                if nbr_of_grass_tiles >= 30 and spawn[0] == nb and fst_sheep == False:
                    players_dictionary[player]['sheep'].append([3, spawn[1], spawn[2]])
                    fst_sheep = True
                if nbr_of_grass_tiles >= 60 and spawn[0] == nb and scd_sheep == False:
                    players_dictionary[player]['sheep'].append([3, spawn[1], spawn[2]])
                    scd_sheep = True
                if nbr_of_grass_tiles >= 90 and spawn[0] == nb and trd_sheep == False:
                    players_dictionary[player]['sheep'].append([3, spawn[1], spawn[2]])
                    trd_sheep = True
        capture_seeds(players_dictionary, board_dictionary)
        create_board(board_dictionary, players_dictionary)
        ...
        ...
        ...


        # get orders of player 1 and notify them to player 2, if necessary
        if type_1 == 'remote':
            orders = get_remote_orders(connection)
        else:
            orders = get_AI_orders(players_dictionary, board_dictionary, 1)
            if type_2 == 'remote':
                notify_remote_orders(connection, orders)
        
        # get orders of player 2 and notify them to player 1, if necessary
        if type_2 == 'remote':
            orders = get_remote_orders(connection)
        else:
            orders = get_AI_orders(players_dictionary, board_dictionary, 2)
            if type_1 == 'remote':
                notify_remote_orders(connection, orders)
        
        ...
        ...
        nbr_of_game_rounds += 1

    # close connection, if necessary
    if type_1 == 'remote' or type_2 == 'remote':
        close_connection(connection)
        
    ...
    ...
    ...