COPY Users FROM '/usr/src/users.csv' DELIMITER ',' CSV;

COPY Carts FROM '/usr/src/carts.csv' DELIMITER ',' CSV;

COPY Order_status FROM '/usr/src/order_statuses.csv' DELIMITER ',' CSV;

COPY Orders FROM '/usr/src/orders.csv' DELIMITER ',' CSV;

COPY Categories FROM '/usr/src/categories.csv' DELIMITER ',' CSV;

COPY Products FROM '/usr/src/products.csv' DELIMITER ',' CSV;

COPY Cart_products FROM '/usr/src/cart_products.csv' DELIMITER ',' CSV;