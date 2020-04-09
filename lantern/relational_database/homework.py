from typing import List
import psycopg2


def task_1_add_new_record_to_db(con) -> None:

    """
    Add a record for a new customer from Singapore
    {
        'customer_name': 'Thomas',
        'contactname': 'David',
        'address': 'Some Address',
        'city': 'London',
        'postalcode': '774',
        'country': 'Singapore',
    }

    Args:
        con: psycopg connection

    Returns: 92 records

    """
    new_customer = {
        'customer_name': 'Thomas',
        'contactname': 'David',
        'address': 'Some Address',
        'city': 'London',
        'postalcode': '774',
        'country': 'Singapore',
    }
    cursor = con.cursor()
    cursor.execute(
        "insert into customers (CustomerName, ContactName,"
        "Address, City, PostalCode, Country)"
        "values (%(customer_name)s, %(contactname)s, %(address)s,"
        "%(city)s, %(postalcode)s, %(country)s);",
        {**new_customer}
    )
    con.commit()
    cursor.execute(
        """
        select * from customers;
        """
    )
    return cursor.fetchall()


def task_2_list_all_customers(cur) -> list:
    """
    Get all records from table Customers

    Args:
        cur: psycopg cursor

    Returns: 91 records

    """
    cur.execute(
        """
        select * from customers;
        """
    )
    return cur.fetchall()


def task_3_list_customers_in_germany(cur) -> list:
    """
    List the customers in Germany

    Args:
        cur: psycopg cursor

    Returns: 11 records
    """
    country = 'Germany'
    cur.execute(
        """
        select * from customers where country = %s;
        """,
        (country,)
    )
    return cur.fetchall()


def task_4_update_customer(con):
    """
    Update first customer's name (Set customername equal to  'Johnny Depp')
    Args:
        cur: psycopg cursor

    Returns: 91 records with updated customer

    """
    customer = 'Johnny Depp'
    cur = con.cursor()
    cur.execute(
        """
        update customers set CustomerName=%s where CustomerID=1;
        """,
        (customer,)
    )
    con.commit()
    cur.execute(
        """
        select * from customers;
        """
    )
    return cur.fetchall()


def task_5_delete_the_last_customer(con) -> None:
    """
    Delete the last customer

    Args:
        con: psycopg connection
    """
    cur = con.cursor()
    cur.execute(
        """
        delete from customers where CustomerID = (select max(CustomerID) from customers);
        """
    )
    con.commit()


def task_6_list_all_supplier_countries(cur) -> list:
    """
    List all supplier countries

    Args:
        cur: psycopg cursor

    Returns: 29 records

    """
    cur.execute(
        """
        select Country from suppliers;
        """
    )
    return cur.fetchall()


def task_7_list_supplier_countries_in_desc_order(cur) -> list:
    """
    List all supplier countries in descending order

    Args:
        cur: psycopg cursor

    Returns: 29 records in descending order

    """
    cur.execute(
        """
        select Country from suppliers order by Country desc;
        """
    )
    return cur.fetchall()


def task_8_count_customers_by_city(cur):
    """
    List the number of customers in each city

    Args:
        cur: psycopg cursor

    Returns: 69 records in descending order

    """
    cur.execute(
        """
        select distinct count(city), city from customers group by city order by count desc;
        """
    )
    return cur.fetchall()


def task_9_count_customers_by_country_with_than_10_customers(cur):
    """
    List the number of customers in each country. Only include countries with more than 10 customers.

    Args:
        cur: psycopg cursor

    Returns: 3 records
    """
    cur.execute(
        """
        select count(Country), Country from customers group by Country having count(*) > 10;
        """
    )
    return cur.fetchall()


def task_10_list_first_10_customers(cur):
    """
    List first 10 customers from the table

    Results: 10 records
    """
    cur.execute(
        """
        select * from customers limit 10;
        """
    )
    return cur.fetchall()


def task_11_list_customers_starting_from_11th(cur):
    """
    List all customers starting from 11th record

    Args:
        cur: psycopg cursor

    Returns: 11 records
    """
    cur.execute(
        """
        select * from customers offset 11;
        """
    )
    return cur.fetchall()


def task_12_list_suppliers_from_specified_countries(cur):
    """
    List all suppliers from the USA, UK, OR Japan

    Args:
        cur: psycopg cursor

    Returns: 8 records
    """
    countries = ('USA', 'UK', 'Japan')
    cur.execute(
        """
        select supplierid, suppliername, contactname, city, country 
        from suppliers where country in %s;
        """,
        (countries,)
    )
    return cur.fetchall()


def task_13_list_products_from_sweden_suppliers(cur):
    """
    List products with suppliers from Sweden.

    Args:
        cur: psycopg cursor

    Returns: 3 records
    """
    country = 'Sweden'
    cur.execute(
        """
        select ProductName from products where supplierid in (select supplierid from suppliers where country = %s)
        """,
        (country, )
    )
    return cur.fetchall()


def task_14_list_products_with_supplier_information(cur):
    """
    List all products with supplier information

    Args:
        cur: psycopg cursor

    Returns: 77 records
    """
    cur.execute(
        """
        select
            products.productid, 
            products.productname,
            products.unit,
            products.price,
            suppliers.country,
            suppliers.city,
            suppliers.suppliername
            from suppliers, products where suppliers.supplierid = products.supplierid;
        """
    )
    return cur.fetchall()

def task_15_list_customers_with_any_order_or_not(cur):
    """
    List all customers, whether they placed any order or not.

    Args:
        cur: psycopg cursor

    Returns: 213 records
    """
    cur.execute(
        """
        select
         customers.customername, 
         customers.contactname, 
         customers.country, 
         orders.orderid 
         from customers 
         full outer join orders on customers.customerid = orders.customerid;
        """
    )
    return cur.fetchall()

def task_16_match_all_customers_and_suppliers_by_country(cur):
    """
    Match all customers and suppliers by country

    Args:
        cur: psycopg cursor

    Returns: 194 records
    """
    cur.execute(
        """
        select
        customers.customername,
        customers.address,
        customers.country as customercountry,
        suppliers.country as suppliercountry,
        suppliers.suppliername
        from customers full join suppliers on customers.country = suppliers.country
        order by customers.country, suppliers.country;
        """
    )
    return cur.fetchall()
