import requests
import sys
import json
def main():
    if len(sys.argv)!=2:
        print("Missing Command Line Argument")
        sys.exit(1)
    try:
        n=float(sys.argv[1])
        response = requests.get(f"https://rest.coincap.io/v3/assets/bitcoin?apiKey=681c1ce84bb0be5e741d6b3725f99554ce3b414e06a4815bb5de86268d82fb1a")
        coin=response.json()
        price=coin["data"]["priceUsd"]
        price=round(n*float(price),4)
        print(f"${price:,}")

    except ValueError:
        print("Not a number")
        sys.exit(1)
    except requests.RequestException:
        print("Could not process request")

main()
