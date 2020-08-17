import requests
from requests.auth import HTTPBasicAuth
from access_token import generate_access_token
import keys





def registerurl():
  access_token= generate_access_token()
  api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
  headers = {"Authorization": "Bearer %s" % access_token}
  request = {
       "ShortCode": keys.shortCode,
      "ResponseType": "completed ",
      "ConfirmationURL": "https://jmacharia.co.ke/confirmation",
      "ValidationURL": "https://jmacharia.co.ke/validation_url"}
  
  response = requests.post(api_url, json = request, headers=headers)
  
  print (response.text)

registerurl()

def simulate_c2b_transaction():
    
  
  access_token= generate_access_token()
  api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
  headers = {"Authorization": "Bearer %s" % access_token}
  request = { 
      "ShortCode":keys.shortCode,
    "CommandID":"CustomerPayBillOnline",
    "Amount":"2",
    "Msisdn":keys.msisdn,
    "BillRefNumber":"33206786" }
  
  response = requests.post(api_url, json = request, headers=headers)
  
  print (response.text)

simulate_c2b_transaction()