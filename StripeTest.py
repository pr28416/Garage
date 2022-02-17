import stripe

stripe.api_key = 'sk_test_51KLCctK74HITVnXOf98Q032KnPN1DUA8jr7xoAwV732LZBDAhvjuM6zFv60p58r6cw0UzK3XVsNFkwo4Zn2wCawH00bZMFHcoK'

inventory = {
    "apples": {'price':499, 'description':'charge on apples'},
    "bananas": {'price':699, 'description':'charge on bananas'},
    "iphone 13": {'price':82900, 'description':'charge on iphone 13'}
}

def openMarket():
    while True:
        item = input("Enter item you wish to buy: ")
        if item == 'q': break
        elif item not in inventory: print(item, 'not found in inventory')
        else:
            user_info = {
                'item': item,
                'name': input("Enter your name: "),
                'phone': input("Enter phone number (including extension): "),
                'address': {
                    'line1': input("Address line 1 (street, PO box, company name): "),
                    'city': input("City: "),
                    'state': input("State/County/Province/Region: "),
                    'postal_code': input("ZIP/Postal Code: "),
                    "country": input("Country (Two-letter code): ")
                }
            }
            try:
                charge = stripe.Charge.create(
                    amount=inventory[user_info['item']]['price'],
                    currency='usd',
                    source='tok_amex',
                    description='Testing stripe charges with ' + user_info['item'],
                    shipping={
                        'address': user_info['address'],
                        'name': user_info['name'],
                        'phone': user_info['phone']
                    }
                )
            except stripe.error.StripeError as e:
                print("Error in transaction:", e)
            else:
                print("Successful transaction!")
                print(charge)

# openMarket()
# charges = stripe.Charge.list(limit=3)
# for charge in charges.auto_paging_iter():
#     print(charge)

# for k,v in inventory.items():
#     stripe.Product.create(name=k, price=v['price'], description=v['description'])
#
# products = stripe.Product.list(limit=3)
# for product in products.auto_paging_iter():
#     print(product)