if __name__ == '__main__':
    companies_list = ["collect_in_store", "CTT", "DHL", "Fedex", "Royal_Mail"]

    df = open("09_shipping_companies.sql", "w")
    for i in range(len(companies_list)):
        df.write("INSERT INTO bikecapstore.shipping_companies(company_id, company_name) VALUES(" + str(i+1) + ", '" + companies_list[i] +"');" + "\n")

    df.close()