from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Player:
    player_id: int
    name: str = "Guest"
    score: int = 0
    attempts: int = 0
    is_active: bool = True

    def make_guess(self) -> None:
        """Increment the attempt counter."""
        self.attempts += 1

    def add_score(self, points: int = 1) -> None:
        """Add points to the player's score."""
        self.score += points

    def reset(self) -> None:
        """Reset player stats for a new game."""
        self.score = 0
        self.attempts = 0

    def __repr__(self) -> str:
        return f"Player(id={self.player_id}, name={self.name}, score={self.score})"
