def main():
    str = input()
    print(TextToEmoji(str))

def TextToEmoji(text):
    # Not the craziest solution, but it works and I can't really find an understandable way to do it differently yet
    return text.replace(":(", "🙁").replace(":)", "🙂")
    
main()