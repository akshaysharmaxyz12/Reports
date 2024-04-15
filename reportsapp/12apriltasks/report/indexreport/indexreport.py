import frappe

def create_indexes():
    frappe.db.sql("CREATE INDEX binidx ON `tabBin` (item_code, warehouse, actual_qty)")
    frappe.db.sql("CREATE INDEX Warehouseidx ON `tabWarehouse` (warehouse_name)")

def get_stock_data(item_code):
    sql_query = """
        SELECT 
            b.item_code,
            b.warehouse,
            b.actual_qty AS bin_qty,
            w.warehouse_name
        FROM 
            `tabBin` b
        INNER JOIN 
            `tabWarehouse` w ON b.warehouse = w.name
        WHERE 
            b.item_code = %s
    """

    stock_data = frappe.db.sql(sql_query, (item_code,), as_dict=True)
    return stock_data

def main():
    create_indexes()

    item_code = '0005'
    stock_data = get_stock_data(item_code)
    print(stock_data)

if __name__ == "__main__":
    main()
