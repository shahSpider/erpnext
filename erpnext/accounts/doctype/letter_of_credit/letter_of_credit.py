# -*- coding: utf-8 -*-
# Copyright (c) 2018, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe import _

class LetterofCredit(Document):
	def autoname(self):
		self.name = get_letter_of_credit_autoname(self.naming_prefix, self.letter_of_credit_number, self.reference_text)

	def get_default_letter_of_credit_account(self):
		default_letter_of_credit_account = frappe.get_cached_value('Company',
			{"company_name": self.company},  "default_letter_of_credit_account")

		if not default_letter_of_credit_account:
			frappe.throw(_("Please set Default Letter of Credit Account in Company {0}")
				.format(self.company))

		return default_letter_of_credit_account

def get_letter_of_credit_autoname(naming_prefix, letter_of_credit_number, reference_text=None):
	if reference_text:
		return "{0}{1} ({2})".format(naming_prefix, letter_of_credit_number, reference_text)
	else:
		return "{0}{1}".format(naming_prefix, letter_of_credit_number)

@frappe.whitelist()
def update_name(name, naming_prefix, letter_of_credit_number, reference_text):
	if not frappe.db.exists("Letter of Credit", name):
		return

	frappe.db.set_value("Letter of Credit", name, {
		"naming_prefix": naming_prefix,
		"letter_of_credit_number": letter_of_credit_number,
		"reference_text": reference_text
	}, None)

	new_name = get_letter_of_credit_autoname(naming_prefix, letter_of_credit_number, reference_text)
	if name != new_name:
		frappe.rename_doc("Letter of Credit", name, new_name, ignore_permissions=1)
		return new_name
