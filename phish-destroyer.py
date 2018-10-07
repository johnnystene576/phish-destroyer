import json, requests, string, random, sys, os # Import needed libraries

print("Loading names...")
names = json.loads(open("names.json").read()) # Open names.json

#Get website data from user
print("Please type request URL to POST.")
url = input(">")
print("Please type username field name.")
uname = input(">")
print("Please type password field name.")
pword = input(">")
print("How many times should I send the full name list?")
amt = int(input("INT>"))
print("How long should the fake passwords be?")
length = int(input("INT>"))

charset = string.ascii_letters + string.digits + '!@#$%^&*()' # Get list of allowed password characters
random.seed = os.urandom(1024) # Seed the random number generator

email_providers = ["@yahoo.com", "@gmail.com", "@hotmail.com", "@outlook.com", "@aol.com"] # Email suffix list, makes it look more legit and ultimately ruins the scammer's DB
fail_count = 0 # Fail count

for i in range(amt):
	for name in names:
		try:
			name_suffix = ''.join(random.choice(string.digits)) # Add numbers after name
			username = name.lower() + name_suffix + random.choice(email_providers) # Generate an email address
			password = ''
			for i in range(length): # Generate a random password.
				password = password + random.choice(charset)
			
			# Send username and password to scammer's site
			requests.post(url, allow_redirects=False, data = {
				uname: username,
				pword: password
			})
			print("Sent fake login! " + username + ":" + password)
			fail_count = 0 # Succeeded, so reset faliure count
		except:
			print("Failed to send fake login!")
			# If we fail more than 50 times in a row, the site is probably down.
			fail_count = fail_count + 1
			if(fail_count > 50):
				print("Fail count exceeds 50 - Server is probably shut down. Oops...")
				sys.exit(0)
