def beautify(string, tab = True) -> str:
    lines = string.splitlines()
    if tab == False:
        return "\n".join(line + "\n" for line in lines)
    

print(beautify(string="My name is Simeon."))

