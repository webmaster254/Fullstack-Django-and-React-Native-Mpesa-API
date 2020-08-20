
import requests
from requests.auth import HTTPBasicAuth

from access_token import generate_access_token
from encode import generate_password
from utils import get_timestamp
import keys




def lipa_na_mpesa():
    formatted_time=get_timestamp()
    decoded_password=generate_password(formatted_time)
    access_token = generate_access_token()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = { "Authorization": "Bearer %s" % access_token }
    request = {
        "BusinessShortCode": keys.Business_shortCode,
        "Password":decoded_password,
        "Timestamp": formatted_time ,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": "1",
        "PartyA": keys.Phone_number ,
        "PartyB": keys.Business_shortCode ,
        "PhoneNumber": keys.Phone_number ,
        "CallBackURL": "https://jmacharia.co.ke/lipanampesa/",
        "AccountReference": "33206786 ",
        "TransactionDesc": " pay fees"
    }
    
    response = requests.post(api_url, json = request, headers=headers)
    
    print (response.text)

lipa_na_mpesa()