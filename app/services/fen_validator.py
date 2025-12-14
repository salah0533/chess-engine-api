import chess
from pydantic import BaseModel, field_validator


class FenRequest(BaseModel):
    fen: str

    @field_validator("fen")
    @classmethod
    def validate_fen(cls, fen: str):
        try:
            chess.Board(fen)
        except ValueError:
            raise ValueError("Invalid FEN")
        return fen
