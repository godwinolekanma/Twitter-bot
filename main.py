from internetCheck import TwitterBot

email = "godwinolekanma12@gmail.com"
password = "Olekanma12"
phone = "3162525998"
promised_speed = "1000down/1000up"

test = TwitterBot()
internetSpeed = test.get_internet_speed()
message = f"Hey internet provider, why is my internet speed {internetSpeed} when i pay for {promised_speed}?"

test.tweet(email=email, phone=phone, password=password, msg=message)
