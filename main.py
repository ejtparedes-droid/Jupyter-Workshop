"""
main.py — Flashcard App (Frontend)
Streamlit-powered interface. Uses st.session_state for persistence so the deck
doesn't reset on every button click.
"""

import streamlit as st
from deck import Deck

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(page_title="FlashCards", page_icon="🃏", layout="centered")

# ── Custom CSS ───────────────────────────────────────────────────────────────
st.markdown(
    """
    <style>
    .card-box {
        background: linear-gradient(135deg, #1e3a5f 0%, #16213e 100%);
        border-radius: 16px;
        padding: 2.5rem 2rem;
        min-height: 200px;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        color: white;
        font-size: 1.4rem;
        font-weight: 500;
        box-shadow: 0 8px 32px rgba(0,0,0,0.3);
        margin-bottom: 1.5rem;
        line-height: 1.6;
    }
    .answer-box {
        background: linear-gradient(135deg, #2d6a4f 0%, #1b4332 100%);
    }
    .counter {
        text-align: center;
        color: #888;
        font-size: 0.9rem;
        margin-bottom: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ── Session-state initialisation ─────────────────────────────────────────────
CSV_PATH = "flashcards.csv"

if "deck" not in st.session_state:
    st.session_state.deck = Deck(CSV_PATH)
    st.session_state.deck.shuffle()          # shuffle once on first load
    st.session_state.show_answer = False

deck: Deck = st.session_state.deck

# ── Header ───────────────────────────────────────────────────────────────────
st.title("🃏 FlashCard Machine")
st.caption("Beat the Forgetting Curve — one card at a time.")

st.markdown("---")

# ── Card display ─────────────────────────────────────────────────────────────
card = deck.current_card()

if card:
    st.markdown(
        f'<p class="counter">Card {deck.current_index + 1} of {len(deck)}</p>',
        unsafe_allow_html=True,
    )

    # Question is always visible
    st.markdown(
        f'<div class="card-box">❓ {card.question}</div>',
        unsafe_allow_html=True,
    )

    # Answer revealed only when flipped
    if st.session_state.show_answer:
        st.markdown(
            f'<div class="card-box answer-box">✅ {card.flip()}</div>',
            unsafe_allow_html=True,
        )
else:
    st.error("No cards found. Check your flashcards.csv file.")

# ── Buttons ───────────────────────────────────────────────────────────────────
col1, col2, col3, col4 = st.columns([1, 1, 1, 1])

with col1:
    if st.button("⬅️ Prev", use_container_width=True):
        deck.prev_card()
        st.session_state.show_answer = False

with col2:
    flip_label = "🙈 Hide" if st.session_state.show_answer else "👀 Flip"
    if st.button(flip_label, use_container_width=True):
        st.session_state.show_answer = not st.session_state.show_answer

with col3:
    if st.button("➡️ Next", use_container_width=True):
        deck.next_card()
        st.session_state.show_answer = False

with col4:
    if st.button("🔀 Shuffle", use_container_width=True):
        deck.shuffle()
        st.session_state.show_answer = False

# ── Footer ───────────────────────────────────────────────────────────────────
st.markdown("---")
st.caption(
    "💡 **Tip:** Shuffle → go through every card → mark ones you missed → repeat. "
    "Spaced repetition beats cramming every time."
)
