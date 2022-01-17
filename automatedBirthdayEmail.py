import pandas as pd 
import datetime
import smtplib
from email.message import EmailMessage
import os

def sendEmail(to, sub, msg):
    print(f"email to {to} \nsend with subject: {sub} \n message: {msg}")
    email = EmailMessage()
    email ['from'] = 'Jon Higgins'
    email ['to'] = f'{to}'
    email ['subject'] = f'{sub}'

    email.set_content(f'{msg}')

    with smtplimb.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('Email', 'password')
        smtp.send_message(email)
    pass 

if __name__ == "__main__":
    df = pd.read_excel("HBD_Data_Python.xlsx")
    print(df)
    today = datetime.datetime.now().strftime("%d-%m")
    update = []
    yearnow = datetime.datetime.now().strftime("%Y")

    for index, item in df.iterrows():
        bday = item['Birthday'].strftime("%d-%m")
        if(bday == today) and yearnow not in str(item["Year"]):
            sendEmail(item['Email'],"Happy Birthday "+item["Name"], item['message'])
            update.append(index)
            
    for i in update:
        yr = df.loc[i, 'Year']
        df.loc[i, 'Year'] = f"{yr}, {yearnow}"
    df.to_excel("HBD_Data_Python.xlsx", index=False)