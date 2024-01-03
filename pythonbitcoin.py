import sys
import requests
if len(sys.argv) ==2 :
    try:
        value = float(sys.argv[1])
    except:
        print("Command-line argument is not a number")
else:
    print("Missing command-line argument")
    sys.exit(1)


try:
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    response = r.json()
    bitcoin = response['bpi']['USD']['rate_float']
    total_amount = bitcoin*value
    print(f"${total_amount:,.4f}", end = "")

except requests.RequestException:
    print("RequestsException")
    sys.exit(1)
