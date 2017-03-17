#! python3
import requests
import time
from os import system as ubuntu
import sys

while(1):
	# try:
	# 	r = requests.get("http://192.168.240.1:8080/cgi-bin/cgi?STOP_STREAM")
	# except:
	# 	print("Couldn't open URL to stop stream. Make sure you're connected to the correct network.")
	# 	exit()
	# print(r.json())

	# if r.json()["result"] == 1:
	# # json_result_check_time = time.time()
	# 	print("Resolution stop Stream")

	# else:
	# 	print("Couldn't stop stream")

	try:
		r = requests.get("http://192.168.240.1:8080/cgi-bin/cgi?GET_BATTERY_LEVEL")
	except:
		print("Couldn't open URL to get battery level. Make sure you're connected to the correct network.")
		# exit()
	print(r.json())
	if r.json()["result"] == 1:
	# json_result_check_time = time.time()
		print("battery level:: ", r.json()["msg"])

	
	else:
		print("Couldn't get battery life")

	
	time.sleep(20)

