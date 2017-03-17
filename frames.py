#! python3
import requests
import time
from os import system as ubuntu
import sys

fps = sys.argv[1]
resolution = sys.argv[2]

accepted_strings_reso = {'1080P', '720P', 'WVGA', 'WVGA_2M', 'WVGA_1M', 'WVGA_750K', 'WVGA_500K', 'WVGA_300K'}


if resolution in accepted_strings_reso:
	ubuntu("rm -rf ~/Desktop/MAVI/frames/*.png")

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

	try:
		r = requests.get("http://192.168.240.1:8080/cgi-bin/cgi?SET_STREAM_RESO("+str(resolution)+"))")
	except:
		print("Couldn't open URL to set reso. Make sure you're connected to the correct network.")
		exit()
	print(r.json())
	if r.json()["result"] == 1:
	# json_result_check_time = time.time()
		print("Resolution Set Successfully")
	
	else:
		print("Couldn't set resolution")

	try:
		r = requests.get("http://192.168.240.1:8080/cgi-bin/cgi?START_STREAM")
	except:
		print("Couldn't open URL to start stream. Make sure you're connected to the correct network.")
		exit()
	print(r.json())
	if r.json()["result"] == 1:
	# json_result_check_time = time.time()
		print("Resolution Start Stream")
	
	else:
		print("Couldn't start stream")

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

	ubuntu("ffmpeg -i rtsp://192.168.240.1:554/live -vf fps="+fps+" ~/Desktop/MAVI/frames/out%d.png")



else:
	print('resolution string incorrect format')
	exit()


# http://192.168.3.160/cgi-bin/cgi?set_stream_reso(wvga)&html