import requests

url = "https://adsense.lazada.co.th/newOffer/link-convert.json"  # Replace with the correct endpoint

# Payload with the given data
payload = {
    "jumpUrl": "https://pages.lazada.co.th/products/life-life-zinc-plus-vitamin-c-30-2-i5448717774-s23115859732.html?actualItemId=3880623562&actualSkuId=14866936442&winner_type=1",
    "subIdTemplateKey": ""
}

# Send POST request
response = requests.post(url, data=payload)

# Check response status
if response.status_code == 200:
    print("Request succeeded!")
    print(response.text)  # Output the response data (if any)
else:
    print(f"Request failed with status code {response.status_code}")

