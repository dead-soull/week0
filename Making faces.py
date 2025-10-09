def main():
    str = input()
    print(TextToEmoji(str))

def TextToEmoji(text):
    return text.replace(":(", "🙁").replace(":)", "🙂")
    
main()