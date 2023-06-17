bad_words = ["bad", "mad", "vodka", "medvedev"]

while True:
    user_input = input("Me: ")

    for word in bad_words:
        user_input = user_input.lower().replace(word, "*" * len(word))

    print(f"Me: {user_input}")
    # Me: Bad man Medvedev drink vodka and become mad !
    # Me: *** man ******** drink ***** and become *** !
