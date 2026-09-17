# PROJECT: Durban July Tickets Shop - With Receipts
# AUTHOR: Sithembiso Mazibuko
# DATE: 16 September 2026
# MY FIRST PROJECT - Made in Mandeni

from datetime import datetime

seats = 500
price = 250
total_money = 0

while seats > 0:
    print("Seats left:", seats)
    buy = int(input("How many tickets do you want? "))
    if buy <= seats:
        seats = seats - buy
        cost = buy * price
        total_money = total_money + cost
        
        now = datetime.now()
        receipt_name = f"receipt_{now.strftime('%H%M%S')}.txt"
        
        with open(receipt_name, "w") as f:
            f.write("================================\n")
            f.write("  DURBAN JULY TICKET SHOP\n")
            f.write("  Mandeni - KZN\n")
            f.write("  Developed by Sithembiso Mazibuko\n")
            f.write("================================\n")
            f.write(f"Date: {now}\n")
            f.write(f"Tickets: {buy}\n")
            f.write(f"Price each: R{price}\n")
            f.write(f"TOTAL PAID: R{cost}\n")
            f.write("================================\n")
            f.write("  Thank you! Enjoy the show!\n")
        
        print(f"Great! You bought {buy} ticket for R {cost}")
        print(f"Receipt saved as {receipt_name} - You can PRINT it now!")
        print("Total money made: R", total_money)
    else:
        print("Sorry, we only have", seats, "left")

print("All sold out! Final money: R", total_money)
