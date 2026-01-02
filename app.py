
with open("note.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
# Not a lot but still
with open("happy.txt","w") as f:
    content = f.write('help')
    print('help')