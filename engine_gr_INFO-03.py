
#-*- coding: utf-8 -*-

import blessed, math, os, time
term = blessed.Terminal()

from remote_play import create_connection, get_remote_orders, notify_remote_orders, close_connection

# other functions
def create_board(board_dictionary):
    """This function uses the informations contained in board_dictionary to create the game board with UTF8 symbols and 
    using blessed functions.
    
    Parameters:
    ----------
    board_dictionary: It's the dictionary with all the game board's informations.(dict)

    Returns
    board: it's the board of the game built with UTF8 symbols.(string)

    Version
    -------
    specification: Abdusamed Mus (v2 07/03/2024)

    """

def create_players_dictionary(board_dictionary):
    """ Creates the dictionary with all the infromations regarding the two players.

    Returns
    -------
    result : return a dictionary with the informations of each player.(dict)
    
    Version
    -------
    specification: Abdusamed Mus (v1 26/02/2024)

    """

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
    
    """

def get_AI_orders(board, player, order):
    """ Receives the order from the AI to play its turn.

    Parameters
    ----------
    board : the informations about the playing board (str).
    player : is it player 1 or player 2 ? (str).
    order : the order of the AI (str).

    Version
    -------
    specification: Abdusamed Mus (v1 26/02/2024)
    
    """

def play_game(file_name, player_1, player_2):
    """This function plays a game of Battle Sheep using the provided board file and player strategies.

    Parameters:
    ----------
    file_name:The name of the file describing the game board.(string)
    player_1: The strategy/order of player 1.(string)
    player_2: The strategy/order of player 2.(string)

    Returns
    None

    Version
    -------
    specification: Malak El Maimouni (v1 26/02/2024)
    
    """

def execute_orders(order):
    """This function executes orders provided for a single game round.
    
    Parameters
    ----------
    order: The given order by the player: (string)
    
    returns
    None

    Version
    -------
    specification: Malak El Maimouni (v1 26/02/2024)
    
    """
def sheep_apparition(board_dictionnary, player, order, nbr_of_grass_tiles):
    """This function allows a sheep to appear each time a player has 30 more grass tiles
     
    Parameters:
    -----------
    board_dictionnary: Represents the current state of the game board.(dict)
    player: Indicates the player's number whose turn it is to make a sheep appear (1 or 2).(int)
    order: Specifies the order for sheep appearances.(str)
    nbr_of_grass_tiles: The total number of grass tiles of the player.(int)
    
    Returns
    None

    Version
    -------
    specification: Malak El Maimouni (v1 26/02/2024)

    """
def grass_growth(nbr_of_game_rounds, board_dictionnary, player):
    """This function handles the growth of grass on the game board over a certain number of game rounds and updates the board parameter with the new grass growth.
    
    Parameters:
    ----------
    nbr_of_game_rounds: The number of game rounds to simulate grass growth.(int)
    board_dictionnary: The current state of the game board.(dict)
    player: The player for whom grass will grow on the board.(int)
    
    Returns
    None

    Version
    -------
    specification: Amrouni Zohra (v1 26/02/2024)

    """
def sheep_fights(board_dictionnary, order):
    """This function handles sheep fights on the game board based on the given order and updates the board parameter with the outcomes of the sheep fights.
    
    Parameters:
    -----------
    board_dictionnary: The current state of the game board.(dict)
    order: The order specifying sheep fights.(string)

    Returns
    None

    Version
    -------
    specification: Amrouni Zohra(Abdu l'a reprise) (v1 26/02/2024)
    
    """
def move_sheep(board_dictionnary, order):
    """This function handles the movement of sheep on the game board based on the given order and updates the board parameter with the new positions of the sheep resulting from the movements.
    
    Parameters:
    ----------
    board_dictionnary: The current state of the game board.(dict)
    order: The order specifying sheep movements.(string)

    Returns
    None

    Version
    -------
    specification: Amrouni Zohra (v1 26/02/2024)

    """
def graze_grass(board_dictionnary, order):
    """This function handles the action of sheep grazing grass on the game board based on the given order and updates the board parameter by removing grass from the tiles where sheep have grazed.
    
    Parameters:
    -----------
    board_dictionnary: The current state of the game board.(dict)
    order: The order specifying sheep grazing actions.(string)
    
    Returns
    None

    Version
    -------
    specification: Amrouni Zohra (v1 26/02/2024)

    """
def capture_seeds(board_dictionnary, order):
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
def check_end_game(board_dictionnary, nbr_of_game_rounds):
    """This function checks whether the game has ended based on the given conditions.
    
    Parameters:
    -----------
    board_dictionnary: The current state of the game board.(dict)
    nbr_of_game_rounds: The total number of game rounds played.(int)
    
    Returns
    Result: 'True' if the game has ended, otherwise it returns 'False'.(bool)

    Version
    -------
    specification: Amrouni Zohra(Malak l'a reprise) (v1 26/02/2024)

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
    
    ...
    ...
    ...

    # create connection, if necessary
    if type_1 == 'remote':
        connection = create_connection(group_2, group_1)
    elif type_2 == 'remote':
        connection = create_connection(group_1, group_2)

    ...
    ...
    ...

    while ...:
    
        ...
        ...
        ...

        # get orders of player 1 and notify them to player 2, if necessary
        if type_1 == 'remote':
            orders = get_remote_orders(connection)
        else:
            orders = get_AI_orders(..., 1)
            if type_2 == 'remote':
                notify_remote_orders(connection, orders)
        
        # get orders of player 2 and notify them to player 1, if necessary
        if type_2 == 'remote':
            orders = get_remote_orders(connection)
        else:
            orders = get_AI_orders(..., 2)
            if type_1 == 'remote':
                notify_remote_orders(connection, orders)
        
        ...
        ...
        ...

    # close connection, if necessary
    if type_1 == 'remote' or type_2 == 'remote':
        close_connection(connection)
        
    ...
    ...
    ...
