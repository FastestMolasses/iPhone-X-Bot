import json
from time import sleep

# Checks whether the input is equal to one of the ones in the list
def checkInput(inp, x):
    while True:
        for i in x:
            if inp == i:
                return inp
        inp = input('Please enter one of these ' + str(x) + ' exactly as displayed!\n')

# Possible inputs
colors = ['space-gray', 'silver']
storages = ['64gb', '256gb']

# Intro
print('\nThis bot needs information from you in order to pre-order the iPhone X.')
sleep(1)
print('None of the entered information is being shared!!')
sleep(1)
print('Please make sure that the entered information is CORRECT.')
sleep(1)

print('\n--------------------------------------------------------------------\n')

# Ask for the color
color = input('\nWhich color iPhone? Enter exactly: %s\n' % str(colors))
color = checkInput(color, colors)

# Ask for storage capacity
storage = input('\nHow much storage? Enter exactly: %s\n' % str(storages))
storage = checkInput(storage, storages)

# Ask for first name and last name
print('\nApple asks to verify your shipping information.')
firstName = input('What is your first name?\n')
lastName = input('\nWhat is your last name?\n')

# Ask for phone information
phoneAreaCode = input('\nWhat is your phone area code?\n')
if (len(phoneAreaCode) > 3):
    phoneAreaCode = phoneAreaCode[1:4]

phoneNum = input('\nWhat is your wireless number? (Not including area code)\n')

# Ask for shipping information
address1 = input('\nWhat is your street address 1?\n')
address2 = input('\nWhat is your street address 2? Leave blank if none.\n')
city = input('\nPlease enter your town / city\n')
province = input('\nPlease enter your province\n')
postalCode = input('\nPlease enter your (no spaces or dashes)\n')

# Ask for Apple email and password
print('\nIn order to sign you in to buy the iPhone, your email and password is required. Your information is not being shared!!')
email = input('What is your Apple email?\n')
password = input('\nWhat is your Apple password?\n')

# Ask for the security code of the card
print('\nTo verify that you can purchase the phone, Apple asks to verify the security code of the card you are paying with.')
securityCode = input('Please input your security code\n')

# Prepare the information to be saved into a JSON
information = {
    'Color': color,
    'Storage': storage,
    'WirelessNumber': phoneNum,
    'SecurityCode': securityCode,
    'Email': email,
    'Password': password,
    'FirstName': firstName,
    'LastName': lastName,
    'AreaCode': phoneAreaCode,
    'Address1': address1,
    'Address2': address2,
    'City': city,
    'Province': province,
    'PostalCode': postalCode,
}

# Save the dictionary to JSON
with open('info.json', 'w') as f:
    json.dump(information, f, indent=4)

print('\nSetup is finished! You may now exit.')
