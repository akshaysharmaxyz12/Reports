# # Copyright (c) 2024, akshay and contributors
# # For license information, please see license.txt

# import frappe


# # def execute(filters=None):
# # 	columns, data = [], []
# # 	return columns, data

# import frappe
# def execute(filters=None):
#     columns = [
#         {"label": "Warehouse", "fieldname": "warehouse", "fieldtype": "Link", "options": "Warehouse"},
#         {"label": "Item Code", "fieldname": "item_code", "fieldtype": "Link", "options": "Item"},
#         {"label": "Projected Qty", "fieldname": "projected_qty", "fieldtype": "Float"},
#         {"label": "Reserved Qty", "fieldname": "reserved_qty", "fieldtype": "Float"},
#         {"label": "Reserved Qty for Production", "fieldname": "reserved_qty_for_production", "fieldtype": "Float"},
#         {"label": "Reserved Qty for Sub Contract", "fieldname": "reserved_qty_for_sub_contract", "fieldtype": "Float"},
#         {"label": "Actual Qty", "fieldname": "actual_qty", "fieldtype": "Float"},
#         {"label": "Valuation Rate", "fieldname": "valuation_rate", "fieldtype": "Currency"}
#     ]
#     data = []
#     sql_query = """
#         SELECT
#             bin.warehouse,
#             bin.item_code,
#             bin.projected_qty,
#             bin.reserved_qty,
#             bin.reserved_qty_for_production,
#             bin.reserved_qty_for_sub_contract,
#             bin.actual_qty,
#             bin.valuation_rate
#         FROM
#             `tabBin` bin
#         WHERE
#             (bin.projected_qty != 0 OR
#             bin.reserved_qty != 0 OR
#             bin.reserved_qty_for_production != 0 OR
#             bin.reserved_qty_for_sub_contract != 0 OR
#             bin.actual_qty != 0)
#         ORDER BY
#             bin.warehouse,
#             bin.item_code
#     """
#     index_queries = [
#         "CREATE INDEX idx_warehou ON `tabBin` (warehouse, item_code)",
#     ]
#     for query in index_queries:
#         frappe.db.sql(query)
#     stock_entries = frappe.db.sql(sql_query, as_dict=True)
#     for row in stock_entries:
#         data.append(row)
#     return columns, data








# import frappe

# def create_indexes():
#     frappe.db.sql("CREATE INDEX binidx ON `tabBin` (item_code, warehouse, actual_qty)")

#     frappe.db.sql("CREATE INDEX Warehouseidx ON `tabWarehouse` (warehouse_name)")

# def get_stock_data(item_code):
#     sql_query = """
#         SELECT 
#             b.item_code,
#             b.warehouse,
#             b.actual_qty AS bin_qty,
#             w.warehouse_name
#         FROM 
#             `tabBin` b
#         INNER JOIN 
#             `tabWarehouse` w ON b.warehouse = w.name
#         WHERE 
#             b.item_code = %s
#     """


#     stock_data = frappe.db.sql(sql_query, (item_code,), as_dict=True)
#     return stock_data

# def stock_data_query_report(filters):
#     item_code = filters.get('item_code')
#     columns = [
#         {
#             'fieldname': 'item_code',
#             'label': 'Item Code',
#             'fieldtype': 'Data',
#             'width': 100
#         },
#         {
#             'fieldname': 'warehouse',
#             'label': 'Warehouse',
#             'fieldtype': 'Data',
#             'width': 120
#         },
#         {
#             'fieldname': 'bin_qty',
#             'label': 'Bin Quantity',
#             'fieldtype': 'Float',
#             'width': 100
#         },
#         {
#             'fieldname': 'warehouse_name',
#             'label': 'Warehouse Name',
#             'fieldtype': 'Data',
#             'width': 150
#         }
#     ]
#     data = get_stock_data(item_code)
#     return columns, data

# def main():
#     create_indexes()

#     item_code = '0005'
#     stock_data = get_stock_data(item_code)
#     print(stock_data)

# if __name__ == "__main__":
#     main()




# import frappe

# def execute(filters=None):
#     columns = [
#         {"label": "Warehouse", "fieldname": "warehouse", "fieldtype": "Link", "options": "Warehouse"},
#         {"label": "Item Code", "fieldname": "item_code", "fieldtype": "Link", "options": "Item"},
#         {"label": "Projected Qty", "fieldname": "projected_qty", "fieldtype": "Float"},
#         {"label": "Reserved Qty", "fieldname": "reserved_qty", "fieldtype": "Float"},
#         {"label": "Reserved Qty for Production", "fieldname": "reserved_qty_for_production", "fieldtype": "Float"},
#         {"label": "Reserved Qty for Sub Contract", "fieldname": "reserved_qty_for_sub_contract", "fieldtype": "Float"},
#         {"label": "Actual Qty", "fieldname": "actual_qty", "fieldtype": "Float"},
#         {"label": "Valuation Rate", "fieldname": "valuation_rate", "fieldtype": "Currency"}
#     ]
#     data = []
    
#     sql_query = """
#         SELECT 
#             b.item_code,
#             b.warehouse,
#             b.actual_qty AS bin_qty,
#             w.warehouse_name
#         FROM 
#             `tabBin` b
#         INNER JOIN 
#             `tabWarehouse` w ON b.warehouse = w.name
#         WHERE 
#             b.item_code = %s
#     """
    
#     index_queries = [
#         "CREATE INDEX bin33 ON `tabBin` (warehouse, item_code)",
#         "CREATE INDEX Warehouseaa ON `tabWarehouse` (warehouse_name)",
#     ]
    
#     for query in index_queries:
#         frappe.db.sql(query)
        
#     stock_entries = frappe.db.sql(sql_query, as_dict=True)
    
#     for row in stock_entries:
#         data.append(row)
        
#     return columns, data



	
# import frappe

# def execute(filters=None):
#     columns = [
#         {"label": "Warehouse", "fieldname": "warehouse", "fieldtype": "Link", "options": "Warehouse"},
#         {"label": "Item Code", "fieldname": "item_code", "fieldtype": "Link", "options": "Item"},
#         {"label": "Projected Qty", "fieldname": "projected_qty", "fieldtype": "Float"},
#         {"label": "Reserved Qty", "fieldname": "reserved_qty", "fieldtype": "Float"},
#         {"label": "Reserved Qty for Production", "fieldname": "reserved_qty_for_production", "fieldtype": "Float"},
#         {"label": "Reserved Qty for Sub Contract", "fieldname": "reserved_qty_for_sub_contract", "fieldtype": "Float"},
#         {"label": "Actual Qty", "fieldname": "actual_qty", "fieldtype": "Float"},
#         {"label": "Valuation Rate", "fieldname": "valuation_rate", "fieldtype": "Currency"}
#     ]
#     data = []
    
#     item_code = filters.get("item_code") if filters else None  # Retrieve item_code from filters
    
#     sql_query = """
#         CREATE INDEX IF NOT EXISTS warehousaaa ON `tabBin` (warehouse, item_code);
#         CREATE INDEX IF NOT EXISTS Warehouseidxaaa ON `tabWarehouse` (warehouse_name);

#         SELECT 
#             b.item_code,
#             b.warehouse,
#             b.actual_qty AS bin_qty,
#             w.warehouse_name
#         FROM 
#             `tabBin` b
#         INNER JOIN 
#             `tabWarehouse` w ON b.warehouse = w.name
#         WHERE 
#             b.item_code = %s
#     """
    
#     stock_entries = frappe.db.sql(sql_query, (item_code,), as_dict=True)  # Pass item_code as parameter
    
#     for row in stock_entries:
#         data.append(row)
        
#     return columns, data
