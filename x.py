l = [1, 2, 3]

s = "!lpkr eekay01"

#print(s[0:s.index(" ")].replace("!lp", ""))

region = s[0:s.index(" ")].replace("!lp", "")
name = s.replace(f"!lp{region} ", "")
region = "na1" if region=="" else region
print(f"{name},{region}")