# -*- coding: utf-8 -*-
# Copyright (c) 2018, Frappe Technologies Pvt. Ltd. and Contributors
# See license.txt

import frappe
import unittest


from erpnext.education.doctype.student.test_student import create_student
from erpnext.education.doctype.student.test_student import get_student
from erpnext.education.doctype.program.test_program import setup_program
from erpnext.education.doctype.course_activity.test_course_activity import make_course_activity

class TestCourseEnrollment(unittest.TestCase):
	def setUp(self):
		setup_program()
		student = create_student({"first_name": "_Test First", "last_name": "_Test Last", "email": "_test_student_1@example.com"})
		program_enrollment = student.enroll_in_program("_Test Program")
		course_enrollment = student.enroll_in_course("_Test Course 1", program_enrollment.name)
		make_course_activity(course_enrollment.name, "Article", "_Test Article 1-1")

	def test_get_progress(self):
		student = get_student("_test_student_1@example.com")
		program_enrollment_name = frappe.get_list("Program Enrollment", filters={"student": student.name, "Program": "_Test Program"})[0].name
		course_enrollment_name = frappe.get_list("Course Enrollment", filters={"student": student.name, "course": "_Test Course 1", "program_enrollment": program_enrollment_name})[0].name
		course_enrollment = frappe.get_doc("Course Enrollment", course_enrollment_name)
		progress = course_enrollment.get_progress(student)
		finished = {'content': '_Test Article 1-1', 'content_type': 'Article', 'is_complete': True}
		self.assertTrue(finished in progress)
		frappe.db.rollback()



