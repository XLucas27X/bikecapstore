
import numpy as np

# Inserção nominal de ‘company_id’ na tabela ‘orders’
def insert_company_id(file):
    #read input file
    fin = open(file, "rt")
    #read file contents to string
    data = fin.read()
    #replace all occurrences of the required string
    data = data.replace("INSERT INTO bikecapstore.orders(order_id, customer_id, order_status, order_date, required_date, shipped_date, store_id,staff_id)",
                        "INSERT INTO bikecapstore.orders(order_id, customer_id, status_id, order_date, required_date, shipped_date, store_id, staff_id, company_id)")
    #close the input file
    fin.close()
    #open the input file in write mode
    fin = open(file, "wt")
    #overrite the input file with the resulting data
    fin.write(data)
    #close the file
    fin.close()

# Inserção de company_id na tabela orders com distribuição normal
def insert_company_id_distribution(file_input, file_output):
    #input file
    initial_file = open(file_input, "rt")
    #output file to write the result to
    final_file = open(file_output, "wt")
    #for each line in the input file
    for line in initial_file:
        if "INSERT INTO bikecapstore.orders" in line:
            line_replace = line
            comp_number = np.random.binomial(n=4, p=0.5, size=1)[0]
            new_line = line[:-3] + ',' + str(comp_number + 1) + ');\n'

            #read replace the string and write to output file
            final_file.write(line.replace(line_replace, new_line))

        else:
            final_file.write(line)

    #close input and output files
    initial_file.close()
    final_file.close()


if __name__ == '__main__':
    file = "10_orders_data_teste.sql"
    insert_company_id(file)
    insert_company_id_distribution(file, "10_orders_data_teste_v2.sql")