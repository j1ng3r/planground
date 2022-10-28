class Solution:
	def minRemoveToMakeValid(self, s: str) -> str:
		med = ""
		count = 0
		for c in s:
			if c == "(":
				count += 1
				med = c + med
			elif c == ")":
				if count > 0:
					count -= 1
					med = c + med
			else: med = c + med
		count = 0
		res = ""
		for c in med:
			if c == ")":
				count += 1
				res = c + res
			elif c == "(":
				if count > 0:
					count -= 1
					res = c + res
			else: res = c + res
		return res
