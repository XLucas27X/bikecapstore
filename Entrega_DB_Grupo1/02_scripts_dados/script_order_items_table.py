
# Exclusão da parte nominal de ‘list_price’
def exclusion_list_price(file_input, file_output):
    #abertura do ficheiro de input
    initial_file = open(file_input, "rt")
    #abertura do ficheiro de output, onde o resultado será gravado
    final_file = open(file_output, "wt")
    #para cada linha do ficheiro inicial, será feito:
    for line in initial_file:
        print(line)
        #leitura, fazer o replace e inserção no ficheirp final.
        final_file.write(line.replace("INSERT INTO bikecapstore.order_items(order_id, item_id, product_id, quantity, list_price,discount)",
                                      "INSERT INTO bikecapstore.order_items(order_id, item_id, product_id, quantity,discount)"))
    #fecho dos ficheiros tanto inicial quanto final
    initial_file.close()
    final_file.close()

# Exclusão do valor da coluna list_price em order_items
def exclusion_list_price_value(file_input, file_output):
    #abertura do ficheiro de input
    initial_file = open(file_input, "rt")
    #abertura do ficheiro de output, onde o resultado será gravado
    final_file = open(file_output, "wt")
    separador = ","

    #para cada linha no ficheiro inicial, será feito:
    for line in initial_file:
        if "INSERT INTO bikecapstore.order_items" in line:
            result_1 = line.split(separador, -6)[-2] + separador
            line_replace = line
            new_line = line.replace(result_1, "")

            #leitura, fazer o replace e inserção no ficheiro final.
            final_file.write(line.replace(line_replace, new_line))

        else:
            final_file.write(line)

    #fecho dos ficheiros tanto inicial quanto final
    initial_file.close()
    final_file.close()

if __name__ == '__main__':
    file = "11_order_items_data_teste.sql"
    exclusion_list_price(file, "11_order_items_data_teste_v2.sql")
    exclusion_list_price_value("11_order_items_data_teste_v2.sql", "11_order_items_data_teste_v3.sql")