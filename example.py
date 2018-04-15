#!/usr/bin/env python3

import skynet
import pprint

if __name__=='__main__':
	try:
		#Get a list of all games from the server
		print('Listing games')
		server='https://skynet.cs.uaf.edu'
		games=skynet.list_games(server)
		pprint.pprint(games)
		print()

		#Get info on a specific game
		print('Getting info on a specific game')
		game_name='test'
		game_info=skynet.info_game(server,game_name)
		pprint.pprint(game_info)
		print()

		#Making a move on a game (an empty object returning is a good thing)
		print('Making a move on a game')
		board='rrrrrrrrr_rr_r______bbbbbbbbbbbb'
		game_move=skynet.play_game(server,game_name,board)
		pprint.pprint(game_move)
		print()

	except KeyboardInterrupt:
		print('Exiting...')
		exit(1)

	except Exception as error:
		print(error)
		exit(1)