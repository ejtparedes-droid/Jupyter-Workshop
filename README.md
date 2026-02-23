# 🃏 FlashCard Machine

A Streamlit web app that combats the Forgetting Curve using spaced repetition flashcards.

---

## Project Structure

```
flashCards/
├── flashcard.py      # The "Brick" — Flashcard class
├── deck.py           # The "Manager" — Deck class (Composition)
├── main.py           # The "Face" — Streamlit frontend
├── flashcards.csv    # Study data (headerless: question,answer)
└── README.md
```

---

## Quick Start

```bash
# 1. Install dependencies
pip install streamlit

# 2. Run the app
streamlit run main.py
```

Open `http://localhost:8501` in your browser.

---

## Architecture (Separation of Concerns)

| Layer | File | Responsibility |
|-------|------|---------------|
| Data | `flashcards.csv` | Raw study material |
| Logic | `flashcard.py` + `deck.py` | OOP backend |
| Interface | `main.py` | Streamlit UI |

---

## Implementation Checklist

- ✅ **Data Load** — All CSV rows appear in the app via `Deck._load()`
- ✅ **Persistence** — `st.session_state` stores the Deck object across button clicks
- ✅ **Logic** — `Flip` calls `card.flip()` which returns `card.answer`
- ✅ **Looping** — `next_card()` uses modulo (`%`) to wrap after the last card

---

## OOP Evaluation Q&A

### 1. What is a Class, and how is it different from an Object?
A **class** is a blueprint — it defines the structure and behaviour that objects of that type will have. An **object** is a concrete *instance* of that class: the blueprint turned into something real that occupies memory and holds its own data.  
*In this project:* `Flashcard` is the class; `Flashcard("What is OOP?", "A paradigm…")` is an object.

### 2. What are Attributes and Methods?
**Attributes** are variables bound to an object — they store its state (`self.question`, `self.answer`).  
**Methods** are functions defined inside a class that operate on that state (`flip()`, `shuffle()`).

### 3. What is Composition, and how did you use it?
**Composition** is a "has-a" relationship: one class owns instances of another class rather than inheriting from it.  
`Deck` *has a* list of `Flashcard` objects — it composes `Flashcard` without extending it. This keeps the two classes independently changeable and testable.

### 4. What is Encapsulation?
Encapsulation bundles data and the methods that act on it inside a class, hiding internal details from outside code.  
`Deck._load()` is a private helper (prefixed `_`) — callers use `Deck` without knowing how CSV parsing works.

### 5. Why did you use `st.session_state`?
Streamlit reruns the entire script on every user interaction. Without `session_state`, a new `Deck` would be created each time a button is clicked, losing the shuffle order and the current index. Storing the `Deck` object in `st.session_state` gives it **persistence** across reruns.

### 6. How does the deck loop back to the first card?
`next_card()` computes the new index as `(current_index + 1) % len(cards)`. The modulo operator (`%`) returns the remainder after division, so when `current_index` reaches the last position, the remainder is `0` — wrapping back to the first card automatically.
