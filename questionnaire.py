def ask_user_preferences():
    print("\nPlease answer the following questions to personalize your haircut suggestions:\n")

    gender = input("What is your gender? (male/female): ").strip().lower()
    hair_type = input("What is your hair type? (straight/wavy/curly): ").strip().lower()
    style_pref = input("What style do you prefer? (professional/casual/edgy): ").strip().lower()
    hair_length = input("Are you okay with short haircuts? (yes/no): ").strip().lower()

    preferences = {
        "gender": gender,
        "hair_type": hair_type,
        "style_pref": style_pref,
        "short_hair_ok": hair_length == "yes"
    }

    return preferences


# For testing
if __name__ == "__main__":
    user_prefs = ask_user_preferences()
    print("\nCollected Preferences:")
    print(user_prefs)
