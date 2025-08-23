def dialog(speaker, phrase):
    if speaker == "inspector":
        print(f"{f"'{phrase}' >>":>70}")
    elif speaker == "applicant":
        print(f"<< '{phrase}'")