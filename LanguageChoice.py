def Choose_Language():
    languages = {"Azerbaijani":"az","English":"en", "Turkish" : "tr", "Spain":"eu-ES","Russian":"ru","French":"fr","Chinese":"yue-Hant-HK","Japanese":"ja-JP"}
    list_lan = ["Azerbaijani", "English", "Turkish", "Spain", "Russian", "French", "Chinese", "Japanese"]
    print("1-Azerbaijani\n2-English\n3-Turkish\n4-Russian\n5-French\n6-Chinese\n7-Japanese\n8-Spanish")
    while True:
        try:
            language_num = int(input("Choose one of the above languages:"))

            while language_num <= 0 or language_num > 8:
                print("\n\n")
                print("1-Azerbaijani\n2-English\n3-Turkish\n4-Russian\n5-French\n6-Chinese\n7-Japanese\n8-Spanish")
                language_num = int(input("Choose one of the above languages:"))

            return languages[list_lan[language_num - 1]]
        except:
            pass
