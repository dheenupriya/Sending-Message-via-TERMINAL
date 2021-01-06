# Sending-Message-via-TERMINAL
Sending Message fron unknown number via Terminal using Textbelt

Execute the following Commands:

commands:
sudo apt install python3.8
sudo apt install python3-pip
pip3 install requests

Now run the command:
python3

Type the following Code in Terminal and Execute:

*In phone no - include country code*
***

import requests
resp=requests.post('https://textbelt.com/text',{
  'phone':'phoneno.',
  'message':'Follow coderart__',
  'key':'textbelt',
})
print(resp.json())

***

