

def ShopingOnline(app, date, price):
	Ship = 20
	if app == "Shopee":
		if date == "10/10":
			Ship = 0
			price = price - price*0.3
		elif price >= 500:
			price = price - price*0.3
		elif price >= 250 and price < 500:
			price = price -price*0.15
		elif price >= 100 and price < 250:
			Ship = 0
		elif price < 100 and price >= 0:
			pass
		elif price < 0:
			return "không hợp lệ"
	elif app == "Tiki":
		if price >= 500:
			price = price - price*0.2
		elif price >= 250 and price < 500:
			price = price -price*0.15
		elif price >= 100 and price < 250:
			Ship = 0
		elif price < 100 and price >=0:
			pass
		elif price < 0:
			return "không hợp lệ"

		if date == "10/10" and (price < 100 or (price >= 250 and price < 500)):
			Ship = 0

	price = price + Ship
	return price


# TestCase kiểm thử bảng kiểm định

AppShopee1 = [["Shopee", "10/10", 300],
			 ["Shopee", "9/10", 550  ],
			 ["Shopee", "9/10", 300 ],
			 ["Shopee", "9/10", 150 ],
			 ["Shopee", "9/10", 50],
			 ["Shopee", "9/10", -1],
			 ["Tiki", "10/10", 550],
			 ["Tiki", "10/10", 300],
			 ["Tiki", "10/10", 200],
			 ["Tiki", "10/10", 50],
			 ["Tiki", "9/10", 550],
			 ["Tiki", "9/10", 300],
			 ["Tiki", "9/10", 150],
			 ["Tiki", "9/10", 50],
			 ["Tiki", "9/10", -1],]

for app, date, price in AppShopee1:
	print(ShopingOnline(app, date, price))

# Kiem thử bảng tương đương
#app = (shopee) (tiki)
#date = (10/10) (các ngày khác)
#price= (>=500k) (>=250k and < 500k) (>=100k and <250k) (<100K) (<0k)

AppShopee2 = [["Shopee", "10/10", 300],
			 ["Shopee", "10/10", 300 ],
			 ["Shopee", "10/10", 150 ],
			 ["Shopee", "10/10", 50],
			 ["Tiki", "9/10", 550],
			 ["Tiki", "9/10", -1]]

for app, date, price in AppShopee2:
	print(ShopingOnline(app, date, price))

