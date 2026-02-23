class Flashcard:
    """
    The 'Brick' - defines what a flashcard is and what it does.
    
    Attributes:
        question (str): The front of the card
        answer (str): The back of the card
    """

    def __init__(self, question: str, answer: str):
        self.question = question
        self.answer = answer

    def __repr__(self):
        return f"Flashcard(question={self.question!r}, answer={self.answer!r})"

    def flip(self) -> str:
        """Return the answer side of the card."""
        return self.answer
