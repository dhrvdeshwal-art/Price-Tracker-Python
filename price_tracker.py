import requests
from bs4 import BeautifulSoup
import pandas as pd

# 1. Yahan koi bhi Amazon product ka link dalein
url = "https://www.amazon.in/dp/B07HG8S52P" # Example product link
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

# 2. Website se data request karein
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

# 3. Product ka naam aur price extract karein
try:
    product_name = soup.find('span', id='productTitle').text.strip()
    # Amazon ke liye price ka class 'a-price-whole' hota hai
    product_price = soup.find('span', class_='a-price-whole').text.strip()
except AttributeError:
    product_name = "N/A"
    product_price = "N/A"
    print("Data nahi mila, shayad website ne block kar diya hai.")

# 4. Data ko save karein
data = {'Product': [product_name], 'Price': [product_price]}
df = pd.DataFrame(data)
df.to_csv('product_data.csv', index=False)

print(f"Success! Product: {product_name}, Price: {product_price}")
