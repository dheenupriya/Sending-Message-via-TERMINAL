import requests
resp=requests.post('https://textbelt.com/text',{
  'phone':'phoneno.',
  'message':'Follow coderart__',
  'key':'textbelt',
})
print(resp.json())
