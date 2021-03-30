class Format:
	tags = frozenset(("div", "h1", "p", "span"))

	def div(self,s):
		# self.ar = s
		self.setelah = f"<div>{s}</div>"
		return self.setelah
	def h1(self,s):
		pass

format = Format()
print(format.div("foo"))