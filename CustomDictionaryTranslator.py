import subprocess


words = {
    "awdw": "hello",
    "grt": "friend",
    "dd": "welcome",
    "tjmi": "to",
    "jkoyjkmo": "this",
    "dwaihdb": "world",
}

text = "hello friend, welcome to this world!"


def copy2clip(txt):
    cmd = "echo " + txt.strip() + "|clip"
    return subprocess.check_call(cmd, shell=True)


keys = words.keys()

for key in keys:
    text = text.replace(words[key], "${" + key + "}")

print(text)
copy2clip(text)
