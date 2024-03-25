import blessed, math, os, time
term = blessed.Terminal()

# from remote_play import create_connection, get_remote_orders, notify_remote_orders, close_connection

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
    specification: Amrouni Zohra (v1 26/02/2024)
    implémentation: Mus Abdusamed ()
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
    implémentation : Mus Abdusamed ()
    """