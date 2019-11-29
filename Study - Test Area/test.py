class TestClass:

	def __init__(self):
		self.start_url = [self.ask_user()]

	def ask_user(self):
		url = "Examplelink.com"
		return url

test1 = TestClass()

test1.ask_user()

print(test1.start_url)