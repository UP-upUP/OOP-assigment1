
class Vulnerabilities:
	vulnerability = "High"
	type = "Software"

	def __init__(self, alert, tip):
		self.vulnerability = alert
		self.type = tip

	def turn_on(self):
		print("dangerous vulnerqabilities!")

vulnerability1 = Vulnerabilities(alert="High", tip="Software")
vulnerability2 = Vulnerabilities(alert="Low", tip="Software")

print(vulnerability1.vulnerability, vulnerability1.type)
print(vulnerability2.vulnerability, vulnerability2.type)

print(vulnerability1.vulnerability == vulnerability2.vulnerability)
print(vulnerability1.type == vulnerability2.type)
