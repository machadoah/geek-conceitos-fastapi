from pydantic import BaseModel
from typing import Optional


class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int


class CursoBD(BaseModel):
    titulo: str
    aulas: int
    horas: int


cursos = [
    Curso(id=1, titulo="LlamaIndex - Introdução", aulas=1, horas=2),
    Curso(id=2, titulo="FastAPI - Introdução", aulas=1, horas=3),
    Curso(id=3, titulo="FastAPI - Avançado", aulas=1, horas=4),
]
