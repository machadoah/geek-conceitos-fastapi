from fastapi import FastAPI, HTTPException, status, Path, Query, Header

from geek_conceitos_fastapi.models import CursoBD

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
async def get_curso(
    curso_id: int = Path(title="ID do curso", description="Deve se inteiro", gt=0, lt=3)
):
    if curso_id not in cursos:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado."
        )

    curso = cursos[curso_id]
    return curso


@app.post("/cursos", status_code=status.HTTP_201_CREATED)
async def create_curso(curso: CursoBD):
    id = len(cursos) + 1
    cursos[id] = curso.model_dump()

    return curso


@app.put("/cursos/{curso_id}")
async def update_curso(curso_id: int, curso: CursoBD):
    if curso_id not in cursos:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Curso não existe."
        )
    else:
        cursos[curso_id] = curso.model_dump()
        return curso


@app.delete("/cursos/{curso_id}")
async def delete_curso(curso_id: int):
    if curso_id not in cursos:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Curso não existe."
        )
    else:
        del cursos[curso_id]
        return f"curso de id {curso_id} deletado."


@app.get("/calc")
async def calc(
    a: int = Query(default=0),
    b: int = Query(default=0),
    c: int = Query(default=0),
    x_header: str = Header(default=None),
):
    print(f"X-HEADER = {x_header}")
    return {"result": a + b + c}
