import requests, random, time

payload = {
	"submitted":"1",
	"country":"fr",
	"firstname":"test",
	"lastname":"test",
	"email":"test",
	"message":"test",
	"dataprotextion":"on"
}

def post_request(payload):
	response = requests.post('https://www.gratis-waardebon.com/sc/todo=cp_naturvel', data = payload)
	print(payload)
	print(response)
	return

def main():
	new_payload = payload
	with open('emails.txt', 'r') as username_file:
		usernames = username_file.readlines()
	with open('fnames.txt', 'r') as fname_file:
		firstnames = fname_file.readlines()
	with open('lnames.txt', 'r') as lname_file:
		lastnames = lname_file.readlines()
	with open('msg.txt', 'r') as msg_file:
		messages = msg_file.readlines()


	for i in range(58, len(usernames)):
		new_payload['email'] = ((usernames[i].rstrip()).replace(" ",""))
		new_payload['firstname'] = ((firstnames[i].rstrip().replace(" ","")))
		new_payload['lastname'] = ((lastnames[i].rstrip().replace(" ","")))
		new_payload['message'] = ((messages[i].rstrip().replace(" ","")))

		#new_payload['password'] = (passswords[i].rstrip())
		print(f'Sending data nr # {(i+1)}')
		post_request(payload)
		sleep_time = random.randint(0,10)
		print(f'sleeping for {sleep_time} seconds')
		time.sleep(sleep_time)
		


while True:
	main()
