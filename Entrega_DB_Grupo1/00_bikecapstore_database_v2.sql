-- Script para criar a base de dados

-- CREATE DATABASE bikecapstore;


-- Tabelas simples
CREATE TABLE bikecapstore.categories (
	category_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	category_name VARCHAR (255) NOT NULL
);

CREATE TABLE bikecapstore.brands (
	brand_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	brand_name VARCHAR (255) NOT NULL
);

CREATE TABLE bikecapstore.customers (
	customer_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	first_name VARCHAR (255) NOT NULL,
	last_name VARCHAR (255) NOT NULL,
	phone VARCHAR (25),
	email VARCHAR (255) NOT NULL,
	street VARCHAR (255),
	city VARCHAR (50),
	state VARCHAR (25),
	zip_code VARCHAR (5)
);

CREATE TABLE bikecapstore.shipping_companies (
	company_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	company_name VARCHAR (255) NOT NULL
);

CREATE TABLE bikecapstore.order_status (
	status_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	status_name VARCHAR (255) NOT NULL
);

CREATE TABLE bikecapstore.stores (
	store_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	store_name VARCHAR (255) NOT NULL,
	phone VARCHAR (25),
	email VARCHAR (255),
	street VARCHAR (255),
	city VARCHAR (255),
	state VARCHAR (10),
	zip_code VARCHAR (5)
);





-- Tabelas mais complexas
-- Alterei o delete nas chaves estrangeiras de cascade para restrict
CREATE TABLE bikecapstore.products (
	product_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	product_name VARCHAR (255) NOT NULL,
	brand_id INT NOT NULL,
	category_id INT NOT NULL,
	model_year SMALLINT NOT NULL,
	list_price DECIMAL (10, 2) NOT NULL,
	FOREIGN KEY (category_id) REFERENCES bikecapstore.categories (category_id) ON DELETE RESTRICT ON UPDATE CASCADE, 
	FOREIGN KEY (brand_id) REFERENCES bikecapstore.brands (brand_id) ON DELETE RESTRICT ON UPDATE CASCADE
);

-- O atributo active também não temos significado para ele
-- Alterei o delete do store_id de cascade para restrict
-- Alterei o delete e o update do manager_id de no action para restrict e cascade respectivamente
CREATE TABLE bikecapstore.staffs (
	staff_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	first_name VARCHAR (50) NOT NULL,
	last_name VARCHAR (50) NOT NULL,
	email VARCHAR (255) NOT NULL UNIQUE,
	phone VARCHAR (25),
	active tinyint NOT NULL,
	store_id INT NOT NULL,
	manager_id INT,
	FOREIGN KEY (store_id) REFERENCES bikecapstore.stores (store_id) ON DELETE RESTRICT ON UPDATE CASCADE,
	FOREIGN KEY (manager_id) REFERENCES bikecapstore.staffs (staff_id) ON DELETE RESTRICT ON UPDATE CASCADE
);

-- Alterei o delete nas chaves estrangeiras de cascade para restrict
CREATE TABLE bikecapstore.stocks (
	store_id INT,
	product_id INT,
	quantity INT,
	PRIMARY KEY (store_id, product_id),
	FOREIGN KEY (store_id) REFERENCES bikecapstore.stores (store_id) ON DELETE RESTRICT ON UPDATE CASCADE,
	FOREIGN KEY (product_id) REFERENCES bikecapstore.products (product_id) ON DELETE RESTRICT ON UPDATE CASCADE
);

-- Alterei o delete nas chaves estrangeiras de cascade para restrict (customer_id, store_id, company_id)
-- Alterei o delete e o update de no action para restrict e cascade respectivamente (staff_id, status_id)
CREATE TABLE bikecapstore.orders (
	order_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	customer_id INT,
	status_id INT NOT NULL,
	order_date DATE NOT NULL,
	required_date DATE NOT NULL,
	shipped_date DATE,
	store_id INT NOT NULL,
	staff_id INT NOT NULL,
	company_id INT,
	FOREIGN KEY (customer_id) REFERENCES bikecapstore.customers (customer_id) ON DELETE RESTRICT ON UPDATE CASCADE,
	FOREIGN KEY (store_id) REFERENCES bikecapstore.stores (store_id) ON DELETE RESTRICT ON UPDATE CASCADE,
	FOREIGN KEY (staff_id) REFERENCES bikecapstore.staffs (staff_id) ON DELETE RESTRICT ON UPDATE CASCADE,
	FOREIGN KEY (company_id) REFERENCES bikecapstore.shipping_companies (company_id) ON DELETE RESTRICT ON UPDATE CASCADE,
	FOREIGN KEY (status_id) REFERENCES bikecapstore.order_status (status_id) ON DELETE RESTRICT ON UPDATE CASCADE
);

-- Alterei o delete nas chaves estrangeiras de cascade para restrict
CREATE TABLE bikecapstore.order_items (
	order_id INT,
	item_id INT,
	product_id INT NOT NULL,
	quantity INT NOT NULL,
	discount DECIMAL (4, 2) NOT NULL DEFAULT 0,
	PRIMARY KEY (order_id, item_id),
	FOREIGN KEY (order_id) REFERENCES bikecapstore.orders (order_id) ON DELETE RESTRICT ON UPDATE CASCADE,
	FOREIGN KEY (product_id) REFERENCES bikecapstore.products (product_id) ON DELETE RESTRICT ON UPDATE CASCADE
);















