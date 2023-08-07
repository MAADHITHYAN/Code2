import re

pattern r"gr(ea)*t" # group of ea created = if re.match(pattern, "great"): print("Match ea")

if re.match(pattern, "greaeaeaeaeaeaeat"): print("Match greaeaeaeaeaeaeat")