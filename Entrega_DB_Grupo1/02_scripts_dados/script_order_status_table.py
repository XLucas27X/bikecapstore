if __name__ == '__main__':
    status_list = ["Pending", "Processing", "Rejected", "Completed"]

    df = open("08_order_status.sql", "w")
    for i in range(len(status_list)):
        df.write("INSERT INTO bikecapstore.order_status(status_id,status_name) VALUES(" + str(i+1) + ", '" + status_list[i] +"');" + "\n")

    df.close()