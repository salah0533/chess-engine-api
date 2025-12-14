from fastapi import APIRouter, Depends
from app.services.fen_validator import FenRequest
from app.services.engine_service import get_engine

router = APIRouter(prefix="/engine", tags=["engine"])


@router.post("/best-move")
def find_best_move(
    data: FenRequest,
    engine = Depends(get_engine)
):
    engine.set_fen_position(data.fen)
    move = engine.get_best_move()
    return {"best_move": move}
