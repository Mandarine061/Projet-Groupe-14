
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
                    if rock[0] == grass_tile[1][0] and rock[1] == grass_tile[1][1]:
                        occupied = True
                    if occupied == False:
                        players_dictionary[player]['grass']+=[1, position]
                        
                
def move_sheep(players_dictionary, order, board_dictionary):
    """This function handles the movement of sheep on the game board based on the given order and updates the board parameter with the new positions of the sheep resulting from the movements.
    
    Parameters:
    ----------
    board_dictionary: The current state of the game board. (dict)
    order: The order specifying sheep movements. (string)

    Returns
    -------
    None

    Version
    -------
    specification: Amrouni Zohra (v1 26/02/2024)
     
       """
    move = order.split(':@')

    sheep_pos = []
    new_pos = []

    sheep_pos.append(move[0])
    new_pos.append(move[1])

    sheep_pos = int(sheep_pos.split('-'))
    new_pos = new_pos.split('-')
    if new_pos not in board_dictionary['rocks']:
        sheep_list = []
        for player in players_dictionary:
            sheep_list.append(players_dictionary[player]['sheep'])
            for sheep in players_dictionary[player]['sheep']:
                if (int(new_pos[0]) != sheep[0] and int(new_pos[1]) != sheep[1]) and (0 < new_pos[0] < int(board_dictionary['map'][0])) and (0 < new_pos[1] < int(board_dictionary['map'][1])):
                    board_dictionary['map'][0] = new_pos[0]
                    board_dictionary['map'][1] = new_pos[1]


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
    grazing = order.split(':*')

    sheep_pos = []
    new_pos = []

    sheep_pos.append(grazing[0])
    new_pos.append(grazing[1])

    found_sheep = False
    index = 0
    while index < len(players_dictionary[player_id]['sheep']) and not found_sheep:
        sheep = players_dictionary[player_id]['sheep'][index]
        if sheep[1] == sheep_pos:
            players_dictionary[player_id]['grass'] = [grass_tile for grass_tile in players_dictionary[player_id]['grass'] if grass_tile[1] != grass_pos]
            found_sheep = True
        index += 1

def capture_seeds(board_dictionary, order):
    """This function handles the action of capturing neutral seeds by sheep on the game board based on the given order and updates the board parameter by changing the ownership of neutral seeds.
    
    Parameters:
    -----------
    board_dictionnary: The current state of the game board.(dict)
    order: The order specifying sheep's actions to capture seeds.(string)
    
    Returns
    None

    Version
    -------
    specification: Amrouni Zohra (v1 26/02/2024)
    """
    player_id, positions = order.split(' ')
    sheep_pos, seed_pos = positions.split('@')
    sheep_pos = tuple(map(int, sheep_pos.split('-')))
    seed_pos = tuple(map(int, seed_pos.split('-')))

    if seed_pos in board_dictionary['seeds']:
        for sheep in board_dictionary['sheep'][player_id]:
            if sheep[1] == sheep_pos:
                board_dictionary['seeds'].remove(seed_pos)
                board_dictionary['grass'][player_id].append([1, seed_pos])
                return  # Sortir de la fonction après avoir trouvé le mouton et effectué l'action
