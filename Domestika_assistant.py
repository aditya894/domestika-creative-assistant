import streamlit as st
import random

# Custom learning journeys
learning_journeys = {
    "Learn digital illustration": [
        "Week 1: Explore sketching & line art – [Drawing Characters](https://www.domestika.org/en/courses/82-drawing-characters-from-scratch)",
        "Week 2: Create 2 character sketches. Get AI feedback on anatomy & proportions.",
        "Week 3: Practice coloring in Procreate or Photoshop. Share in the peer forum.",
        "Week 4: Upload a final illustration. Get AI suggestions for storytelling & lighting."
    ],
    "Improve video editing": [
        "Week 1: Learn Premiere Pro basics – [Video Editing Course](https://www.domestika.org/en/courses/171-video-production-and-edition-with-dslr-camera-and-adobe-premiere)",
        "Week 2: Edit a 30-sec clip. Get AI feedback on pacing & transitions.",
        "Week 3: Explore color grading & motion graphics. Join peer review.",
        "Week 4: Finalize project. Receive AI co-creation tips like music alternatives."
    ],
    "Get feedback on a painting": [
        "Week 1: Learn composition & color theory – [Oil Painting Techniques](https://www.domestika.org/en/courses/3348-contemporary-oil-painting-techniques)",
        "Week 2: Upload your WIP for AI feedback on balance and depth.",
        "Week 3: Participate in painter critique circles.",
        "Week 4: Share final piece. Get AI tips on framing and exhibition presentation."
    ],
    "Co-create a logo": [
        "Week 1: Study branding & grids – [Logo Design Guide](https://www.domestika.org/en/courses/1454-logo-design-the-ultimate-guide)",
        "Week 2: Draft 2 logo options. Get AI feedback on clarity and balance.",
        "Week 3: Use AI to generate new font and color palettes. Get peer votes.",
        "Week 4: Finalize logo. Get AI-generated mockups for cards & packaging."
    ]
}

sample_feedback = [
    "Great use of color balance. Try adding more contrast for visual interest.",
    "Composition is strong. Consider refining the edges for a polished look.",
    "Good start! For realism, practice more light and shadow studies.",
    "Typography is clean. Try a stronger color pairing for brand impact."
]

# Set up UI
st.set_page_config(page_title="Domestika Creative Assistant", layout="centered")
st.title("🎨 Domestika Creative Assistant")
st.markdown("Your AI guide to **learn faster**, **create better**, and **grow with confidence**.")

# Sidebar – knowledge base link
with st.sidebar:
    st.header("🌐 Explore More Courses")
    st.markdown("[🔍 Browse Domestika Courses](https://www.domestika.org/en/courses)")

# Tabs
tab1, tab2 = st.tabs(["📘 Personalized Learning", "🧠 AI Feedback & Co-Creation"])

# Tab 1
with tab1:
    st.subheader("1. Build Your Learning Path")
    name = st.text_input("What's your name?")
    goal = st.selectbox("What do you want to focus on?", list(learning_journeys.keys()))

    if st.button("Generate Learning Journey"):
        st.success(f"Hi {name or 'creator'}! Here's your AI-guided roadmap to {goal}:")
        for step in learning_journeys[goal]:
            st.markdown(f"- **{step}**")

# Tab 2
with tab2:
    st.subheader("2. Upload Your Work for Feedback")
    uploaded_file = st.file_uploader("Upload your creative work (image or PDF)", type=["jpg", "png", "pdf"])

    if uploaded_file:
        st.image(uploaded_file, caption="Your uploaded work", use_column_width=True)

        if st.button("Get AI Feedback"):
            st.success("AI Feedback:")
            st.markdown(f"📝 {random.choice(sample_feedback)}")

        if st.button("Co-Create a Variation"):
            st.info("🛠️ Feature coming soon: AI-generated variations of your work.")

st.markdown("---")
st.caption("Created for Domestika PM Take-Home by [Your Name]")
