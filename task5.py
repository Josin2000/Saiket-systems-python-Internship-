import requests

from_cur = str(input("enter currency to convert:")).upper()
to_cur = str(input("enter resultant currency:")).upper()

amount =float(input("enter the amount:"))
response = requests.get(f"https://api.frankfurter.app/latest?amount={amount}&from={from_cur}&to={to_cur}")

print(f"{amount}{from_cur}is {response.json()['rates'][to_cur]}{to_cur}")

