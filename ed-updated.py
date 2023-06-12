
class Vulnerabilities:
	vulnerability = "High"
	type = "Software"

	def __init__(self, alert, tip):
		self.vulnerability = alert
		self.type = tip
		self.danger = 1
		self.dangerlevel = 1

	def turn_on(self):
		print("dangerous vulnerabilities!")

	def makedanger(self, danger):
		self.danger = danger

	def get_dangerlevel(self):
		self.dangerlevel += self.danger
		return self.danger


class Vulnerability1:
	def __eq__(self, other):
		print('high')
		return self is other

class Vulnerability2:
	def __eq__(self, other):
		print('medium')
		return self is other

my_1 = Vulnerability1()
my_2 = Vulnerability2()

is_eq = (my_1 == my_2)
is_eq = (my_2 == my_1)
is_eq = (my_1 == my_1)



"""
vulnerability1 = Vulnerabilities(alert="High", tip="Software")
vulnerability2 = Vulnerabilities(alert="Low", tip="Software")

print(vulnerability1.vulnerability, vulnerability1.type)
print(vulnerability2.vulnerability, vulnerability2.type)

print(vulnerability1.vulnerability == vulnerability2.vulnerability)
print(vulnerability1.type == vulnerability2.type)
"""
