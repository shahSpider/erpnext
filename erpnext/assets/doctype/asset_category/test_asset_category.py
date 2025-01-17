# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# See license.txt

import frappe
import unittest

class TestAssetCategory(unittest.TestCase):
	def test_mandatory_fields(self):
		asset_category = frappe.new_doc("Asset Category")
		asset_category.asset_category_name = "Computers"
		
		self.assertRaises(frappe.MandatoryError, asset_category.insert)
		
		asset_category.total_number_of_depreciations = 3
		asset_category.frequency_of_depreciation = 3
		asset_category.append("accounts", {
			"company_name": "_Test Company",
			"fixed_asset_account": "_Test Fixed Asset - _TC",
			"accumulated_depreciation_account": "_Test Accumulated Depreciations - _TC",
			"depreciation_expense_account": "_Test Depreciations - _TC"
		})
		
		try:
			asset_category.insert()
		except frappe.DuplicateEntryError:
			pass
			