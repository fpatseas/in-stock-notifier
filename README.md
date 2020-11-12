# Product Stock Notifier
A Python script that utilizes Selenium to check product stock availability from a list of products that you have defined, and sends email notification for each available to purchase.

## Getting started
```
# Clone repository
git clone https://github.com/fpatseas/in-stock-notifier

cd in-stock-notifier

# Copy products.example.json as products.json, to include the products you want to check on their availability
copy products.example.json products.json

# Install dependencies
pip install -r requirements.txt

cd instock_notifier

# Copy config.example.py as config.py, and edit it as you wish
copy config.example.py config.py

cd ..

# Run
python instock_notifier
```
