from frappe import _

def get_data():
	return {
		'fieldname': 'blanket_order',
		'transactions': [
			{
				'items': ['Purchase Order', 'Sales Order']
			}
		]
	}
