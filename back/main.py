import csv
import os
import datetime

FILE_PATH_PRICES = '/home/martin/Desktop/Parrilla/files/precios.csv'
FILE_PATH_SALES = '/home/martin/Desktop/Parrilla/files/ventas.csv'

def show_menu():
    print("\n ------------------ WELCOME ------------")
    print(" Menu: ")

    with open(FILE_PATH_PRICES, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        i = 0
        for row in reader:
            i +=1
            print(f"{i}) {row[0]:<17} | price: ${row[1]:>5}")

    i +=1
    print(f"{i}) Exit")

    return i

def get_last_id():
    if os.path.exists(FILE_PATH_SALES):
        with open(FILE_PATH_SALES, mode='r', encoding='utf-8') as file_sales:
            reader = list(csv.reader(file_sales))
            
            if len(reader) > 0:
                last_id = int(reader[-1][0])
                print(f"El último ID es: {last_id}")
            else:
                last_id = 0
    else:
        last_id = 0

    return last_id

def main():
    finish = False
    total = 0.0

    products = []

    new_id = get_last_id() + 1

    with open(FILE_PATH_PRICES, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        reader_list = list(reader)

    while finish == False:
        lenght = show_menu()
        try:
            option = int(input("Select the product: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if option > lenght or option <= 0:
            print("Invalid Option")
        elif option == lenght:
            with open(FILE_PATH_SALES, mode='a', newline='', encoding='utf-8') as file_sales:
                writer = csv.writer(file_sales)

                now = datetime.datetime.now()
                date = now.date()
                time = now.time()

                writer.writerow([new_id, products, total, date, time])

            print(f"Total: {total}")
            print("Thanks for buying here!")
            finish = True
        else:
            price = float(reader_list[option - 1][1])
            total += price
            products.append(reader_list[option - 1][0])
            print(f"Added item. Current total: {total}")

if __name__ == "__main__":
    main()