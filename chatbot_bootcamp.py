def func(x):
    while True:
        if x == "hi":
            print("hello")
            break

        elif x == "who is the developer of it":
            print("manzoor")
            break

        elif x == "how are you":
            print("i am fine , what about you")
            break

        elif x == "what can i call you":
            print("Friday")
            break

        elif x == "do you have a girlfriend":
            print("No i can't do that , as i am a machine")
            break

        elif x == "exit":
            exit(x)

        else:
            print("sorry, i not understand")
            break


while True:
    a = input("enter your message???---")
    func(a)