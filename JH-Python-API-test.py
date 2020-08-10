# -*- coding: utf-8 -*-
"""
@author: JH
Python script to ping public API
modified for privacy
"""



#Needed for the publiv and private keys:
from ecdsa import SigningKey, NIST256p
#Needed for requests
import requests

Amount        = 999                                               
Currency      = "USD"                                              
ToAccount     = "999999999999"                                      
KeyId         = "er157YrM1WL"                                      
Provider      = "USA-USA"                                   
Name          = "JH-homework-test"                                     
TransactionId = "abcd1234-efghi5678-jklm-90"             
ClientId      = "JH-homework-test"                                     

# GET request for the test API that was provided.
r = requests.get("https://example-link-to-API.com/.")


# Decryption of Keys:
signing_key = SigningKey.generate(curve=NIST256p)
verifying_key = signing_key.get_verifying_key()

#Retreiving / Decryting Private Key File
with open('private-key.pem', 'wb') as private_key_file:
    private_key_file.write(signing_key.to_pem())

#Retreiving / Decryting Publiv Key File
with open('public-key.pem', 'wb') as public_key_file:
    public_key_file.write(verifying_key.to_pem())
   
# GET Transaction Request
    {
  "requestId": "JH-TEST",
  "transaction": [
    {   
      "key-id": KeyId,                                              
      "client-id": ClientId,                                        
      "transactionId": TransactionId,                               
      "provider": Provider,                                         
      "currency": Currency,
      "recipientAccountId": ToAccount,
      "name": Name,                                                 
      "amount": Amount                                              
    }
   ]
  }
  

# I had some extra time and added some error handling to avoid silly bugs.
if Amount > 0:
    pass
else:
    print("Transaction Failed: Transaction amount must be greater than 0 to send Money.")

# I ran out of time, but I was trying to add some more fancy error handling.
""" 
for x in Currency:
    if x == "USD":
       Provider = "usa-usa"
       print(Provider)
       break
    elif x == "JPY":
       Provider = "jpy-japan"
       print(Provider)
       break
    elif x == "BTC":
       Provider = "usa-bitcoin"
       print(Provider)
       break
    else:
       print("Transaction Failed: Unsupported Provider or Currency")  
"""       
 
# Status Code of 200 is good....Everything else is bad.
if r.status_code == 200:
    print(r.status_code, ": Transaction Successful!")
    print("You sent:", Amount, Currency, "to:", ToAccount )
else:
    print(r.status_code, ": Transaction Failed")
    
    
print("Transaction status code:", r.status_code)
print("Script Complete")

