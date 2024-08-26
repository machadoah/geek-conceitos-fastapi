from fastapi import FastAPI, HTTPException
from http import HTTPStatus

app = FastAPI()


cursos = {
    1: {"aulas": 20, "horas": 10, "titulo": "LlamaIndex - Introdução"},
    2: {"aulas": 15, "horas": 8, "titulo": "FastAPI - Introdução"},
}


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/cursos")
async def get_cursos():
    return cursos


@app.get("/cursos/{curso_id}")
async def get_curso(curso_id: int):
    if curso_id not in cursos:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Curso not found")

    curso = cursos[curso_id]
    curso.update({"id": curso_id})
    return curso
