import random
import re
import streamlit as st

st.set_page_config(page_title="Business Name Creator", page_icon="💡")

# Word lists used to create name ideas
PREFIXES = {
    "Modern": ["Nova", "Nex", "Bright", "Urban", "Next"],
    "Professional": ["Summit", "Pioneer", "Prime", "Sterling", "Crest"],
    "Playful": ["Happy", "Bumble", "Sunny", "Witty", "Jolly"],
    "Elegant": ["Luna", "Velvet", "Aura", "Golden", "Willow"],
}

SUFFIXES = [
    "Co.", "Works", "Studio", "Group", "Solutions",
    "Collective", "Labs", "House", "Hub", "Partners"
]


def clean_word(text):
    """Remove extra spaces and return a usable word."""
    words = re.findall(r"[A-Za-z0-9]+", text.strip())
    return " ".join(words)


def create_names(business_type, keywords, style, count):
    prefix_options = PREFIXES[style]

    keyword_list = [
        clean_word(word)
        for word in keywords.split(",")
        if clean_word(word)
    ]

    business_type = clean_word(business_type)
    if business_type:
        keyword_list.append(business_type)

    if not keyword_list:
        keyword_list = ["Idea", "Venture", "Business"]

    names = set()
    attempts = 0

    while len(names) < count and attempts < count * 20:
        attempts += 1
        word = random.choice(keyword_list)
        prefix = random.choice(prefix_options)
        suffix = random.choice(SUFFIXES)

        name_style = random.randint(1, 3)
        if name_style == 1:
            name = f"{prefix} {word}"
        elif name_style == 2:
            name = f"{word} {suffix}"
        else:
            name = f"{prefix} {word} {suffix}"

        names.add(name)

    return sorted(names)


st.title("💡 Business Name Creator")
st.write("Enter a few details to generate business name ideas.")

with st.form("name_generator"):
    business_type = st.text_input(
        "What kind of business is it?",
        placeholder="For example: coffee shop, clothing brand, gardening"
    )

    keywords = st.text_input(
        "Keywords (separate with commas)",
        placeholder="For example: fresh, local, green"
    )

    style = st.selectbox(
        "Choose a naming style",
        ["Modern", "Professional", "Playful", "Elegant"]
    )

    count = st.slider("Number of ideas", min_value=5, max_value=30, value=10)

    submitted = st.form_submit_button("Generate names")

if submitted:
    ideas = create_names(business_type, keywords, style, count)

    st.subheader("Name ideas")
    for number, name in enumerate(ideas, start=1):
        st.write(f"{number}. **{name}**")

    st.caption(
        "These are brainstorming ideas. Check that a name is available "
        "before using it for a business, website, or trademark."
    )