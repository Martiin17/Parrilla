import csv
import os
import datetime
import os
from dotenv import load_dotenv

load_dotenv()

FILE_PATH_PRODUCTS = os.getenv('FILE_PATH_PRODUCTS')
FILE_PATH_SALES = os.getenv('FILE_PATH_SALES')

def show_menu():
    print("\n ------------------ WELCOME ------------")
    print(" Menu: ")

    with open(FILE_PATH_PRODUCTS, mode='r', encoding='utf-8') as file_products:
        reader = csv.reader(file_products)
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
            else:
                last_id = 0
    else:
        last_id = 0

    return last_id

def write_csv(path, new_id, products, total):
    with open(path, mode='a', newline='', encoding='utf-8') as file_sales:
        writer = csv.writer(file_sales)

        now = datetime.datetime.now()
        date = now.date()
        time = now.time()

        writer.writerow([new_id, products, total, date, time])

def get_products_list(path):
    with open(path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            reader_list = list(reader)

            return reader_list

def main():
    finish = False
    total = 0.0

    products_added = []

    new_id = get_last_id() + 1

    products_list = get_products_list(FILE_PATH_PRODUCTS)

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
            write_csv(FILE_PATH_SALES, new_id, products_added, total)

            print(f"Total: {total}")
            print("Thanks for buying here!")
            finish = True

        else:
            price = float(products_list[option - 1][1])
            total += price
            products_added.append(products_list[option - 1][0])
            print(f"Added item. Current total: {total}")

if __name__ == "__main__":
    main()