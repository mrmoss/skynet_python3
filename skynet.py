#!/usr/bin/env python3
import json
import requests

def make_req(server,uri,post=None):
	try:
		data=requests.get(url=server+uri,allow_redirects=True,data=post)
	except Exception as error:
		raise Exception(str(error))

	if data.status_code!=200:
		raise Exception('Response: '+str(data.status_code))

	try:
		data=data.text
		data=json.loads(data)
	except Exception as error:
		raise Exception('Not a JSON object.')

	if 'error' in data:
		raise Exception('Server Error: '+str(data['error']))

	return data

def list_games(server):
	try:
		return make_req(server,'/?list_games=true')
	except Exception as error:
		raise Exception('Error listing games - '+str(error))

def info_game(server,game_name):
	try:
		return make_req(server,'/?info_game=true','{"name":"'+game_name+'"}')
	except Exception as error:
		raise Exception('Error getting info on game "'+game_name+'" - '+str(error))

def play_game(server,game_name,board):
	try:
		return make_req(server,'/?play_game=true','{"name":"'+game_name+'","board":"'+board+'"}')
	except Exception as error:
		raise Exception('Error playing on game "'+game_name+'" - '+str(error))