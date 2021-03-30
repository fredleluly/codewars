def ensure_question(s):
    return f"{s}?" if "?" not in s else s

print(ensure_question(""),"?","Expected: '?'")
print(ensure_question("Yes"),"Yes?","Expected: '?'")
print(ensure_question("No?"),"No?","Expected: '?'")
