from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

def sendsms():
    account_sid = "AC4d6eb543504fe61e94f1ffc384706706"
    auth_token = "df71b1e229aba995762ff472750fbbc7"
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                     body="Congratulation !! You have successfully buy stock from Stockz app",
                     from_='+16206991331',
                     to='+919372532652'
                 )

    print("Message send Successfully")