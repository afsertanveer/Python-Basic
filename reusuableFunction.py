def convert_emoji(message):
    words = message.split(' ')
    print(words)
    emojis = {
        ":)": "😊",
        ":(": "😞"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "

    return output


message = input(">")

print(convert_emoji(message))