
def sql_to_list(file):
    file_open = open(file, "r")
    data = file_open.read()
    data_to_list = data.split("\n")
    file_open.close()
    return data_to_list

def write_different_files(list):
    df_brands = open("01_brands_data.sql", "w")
    df_categories = open("02_categories_data.sql", "w")
    df_products = open("03_products_data.sql", "w")
    df_customers = open("04_customers_data.sql", "w")
    df_stores = open("05_stores_data.sql", "w")
    df_stocks = open("06_stocks_data.sql", "w")
    df_staffs = open("07_staffs_data.sql", "w")
    df_orders = open("10_orders_data.sql", "w")
    df_order_items = open("11_order_items_data.sql", "w")

    for i in range(len(list)):
        # print(i)
        str = list[i]
        if "INSERT INTO production.brands(brand_id,brand_name)" in str:
            str_replaced = str.replace("production", "bikecapstore")
            df_brands.write(str_replaced + "\n")
        elif "INSERT INTO production.categories(category_id,category_name)" in str:
            str_replaced = str.replace("production", "bikecapstore")
            df_categories.write(str_replaced + "\n")
        elif "INSERT INTO production.products(product_id, product_name, brand_id, category_id, model_year, list_price)" in str:
            str_replaced = str.replace("production", "bikecapstore")
            df_products.write(str_replaced + "\n")
        elif "INSERT INTO sales.customers(first_name, last_name, phone, email, street, city, state, zip_code)" in str:
            str_replaced = str.replace("sales", "bikecapstore")
            df_customers.write(str_replaced + "\n")
        elif "INSERT INTO sales.stores(store_name, phone, email, street, city, state, zip_code)" in str:
            str_replaced = str.replace("sales", "bikecapstore")
            df_stores.write(str_replaced + "\n")
        elif "INSERT INTO production.stocks(store_id, product_id, quantity)" in str:
            str_replaced = str.replace("production", "bikecapstore")
            df_stocks.write(str_replaced + "\n")
        elif "INSERT INTO sales.staffs(staff_id, first_name, last_name, email, phone, active, store_id, manager_id)" in str:
            str_replaced = str.replace("sales", "bikecapstore")
            df_staffs.write(str_replaced + "\n")
        elif "INSERT INTO sales.orders(order_id, customer_id, order_status, order_date, required_date, shipped_date, store_id,staff_id)" in str:
            str_replaced = str.replace("sales", "bikecapstore")
            df_orders.write(str_replaced + "\n")
        elif "INSERT INTO sales.order_items(order_id, item_id, product_id, quantity, list_price,discount)" in str:
            str_replaced = str.replace("sales", "bikecapstore")
            df_order_items.write(str_replaced + "\n")

    df_brands.close()
    df_categories.close()
    df_products.close()
    df_customers.close()
    df_stores.close()
    df_stocks.close()
    df_staffs.close()
    df_orders.close()
    df_order_items.close()

if __name__ == '__main__':
    file = "BikeStores Sample Database - load data.sql"
    data_input = sql_to_list(file)
    write_different_files(data_input)
