def recommend_haircuts(face_shape, preferences):
    gender = preferences['gender']
    hair_type = preferences['hair_type']
    style_pref = preferences['style_pref']
    short_hair_ok = preferences['short_hair_ok']

    # Rule-based example haircut recommendations
    recommendations = {
        "Oval": {
            "male": ["Pompadour", "Crew Cut", "Quiff"],
            "female": ["Long Layers", "Bob Cut", "Beach Waves"]
        },
        "Round": {
            "male": ["Undercut", "Spiky Hair", "Faux Hawk"],
            "female": ["Layered Bob", "Side Swept Bangs", "Pixie Cut"]
        },
        "Square": {
            "male": ["Buzz Cut", "Slick Back", "Side Part"],
            "female": ["Soft Waves", "Textured Lob", "Side Part Bob"]
        },
        "Heart": {
            "male": ["Side Swept Fringe", "Fade with Top Volume"],
            "female": ["Long Side Bangs", "Curtain Bangs", "Wavy Layers"]
        }
    }

    default_styles = ["Classic Cut", "Taper Fade", "Simple Ponytail"]

    # Get recommendation based on face shape + gender
    haircut_options = recommendations.get(face_shape, {}).get(gender, default_styles)

    # Apply filters (e.g., short hair restriction)
    if not short_hair_ok:
        haircut_options = [cut for cut in haircut_options if "Long" in cut or "Wavy" in cut or "Layers" in cut]

    # Fallback if empty
    if not haircut_options:
        haircut_options = default_styles

    return haircut_options


# For testing
if __name__ == "__main__":
    face_shape = "Oval"
    preferences = {
        "gender": "female",
        "hair_type": "wavy",
        "style_pref": "casual",
        "short_hair_ok": False
    }

    recommended = recommend_haircuts(face_shape, preferences)
    print("\nRecommended Haircuts:")
    for cut in recommended:
        print(f"- {cut}")
