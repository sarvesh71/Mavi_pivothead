#! python3
import requests
import time
from os import system as ubuntu

tenGetTime = 0
tenTime = 0
for i in range(10):
	start_time = time.time()
	try:
		r = requests.get('http://192.168.240.1:8080/cgi-bin/cgi?take_photo')
	except:
		print("Couldn't open URL. Make sure you're connected to the correct network.")
		exit()

	get_request_time = time.time()

	if r.json()["result"] == 1:
		json_result_check_time = time.time()
		print("Got the image")
		imagePath=r.json()["msg"]
		json_msg_time = time.time()
		imageName=imagePath.split("/")[-1]
		print(imagePath)
		time_before_wget = time.time()
		ubuntu("wget "+imagePath)
		time_after_wget = time.time()
	else:
		print("Couldn't capture image")
	print('iteration: ', i)
	print('time taken in get request: ', get_request_time - start_time)
	# print('time taken in checking if(result): ', json_result_check_time - get_request_time)
	# print('time taken in Json msg: ', json_msg_time - json_result_check_time)
	print('time taken in wget: ', time_after_wget - time_before_wget)
	print('Total time taken: ', time.time() - start_time)
	print('\n')
	tenGetTime = tenGetTime + get_request_time - start_time
	tenTime = tenTime + time.time() - start_time
print('Total time taken in Get: ', tenGetTime)
print('Total time taken: ', tenTime)