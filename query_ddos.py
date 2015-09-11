#!/usr/bin/python


class Shape:

	def __init__(self,message):
		self.message = message


	def print_message(self):
		print self.message


shape = Shape("message")
shape.print_message

