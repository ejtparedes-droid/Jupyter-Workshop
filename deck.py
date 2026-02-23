import csv
import random
from flashcard import Flashcard


class Deck:
    """
    The 'Manager' - handles Composition by owning a list of Flashcard objects.
    
    Responsibilities:
        - Load flashcard data from a CSV file
        - Shuffle the deck
        - Track the current card index
        - Navigate between cards (next, previous)
    """

    def __init__(self, csv_path: str):
        self.cards: list[Flashcard] = []
        self.current_index: int = 0
        self._load(csv_path)

    def _load(self, csv_path: str):
        """Load flashcards from a headerless CSV file (question, answer)."""
        with open(csv_path, newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) >= 2:
                    question = row[0].strip()
                    answer = row[1].strip()
                    self.cards.append(Flashcard(question, answer))

    def shuffle(self):
        """Shuffle the deck in place and reset index to 0."""
        random.shuffle(self.cards)
        self.current_index = 0

    def current_card(self) -> Flashcard | None:
        """Return the current Flashcard, or None if the deck is empty."""
        if not self.cards:
            return None
        return self.cards[self.current_index]

    def next_card(self):
        """Advance to the next card, looping back to start after the last card."""
        if self.cards:
            self.current_index = (self.current_index + 1) % len(self.cards)

    def prev_card(self):
        """Go back to the previous card, looping to the end from the first card."""
        if self.cards:
            self.current_index = (self.current_index - 1) % len(self.cards)

    def __len__(self):
        return len(self.cards)

    def __repr__(self):
        return f"Deck(cards={len(self.cards)}, current_index={self.current_index})"
