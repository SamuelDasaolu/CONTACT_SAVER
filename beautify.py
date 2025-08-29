def beautify(string) -> str:
    lines = string.splitlines()
    return "\n".join(line + "\n" for line in lines)
    

print(beautify(string="My name is Simeon."))

