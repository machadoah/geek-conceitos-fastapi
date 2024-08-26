from typing import Dict, List

from fastapi import FastAPI, HTTPException, status, Path, Query, Header, Depends

from geek_conceitos_fastapi.models import CursoBD, Curso, cursos

from time import sleep

app = FastAPI(
    title="API de Cursos",
    version="0.1.0",
    description="Uma API para estudo do **FastAPI**",
)


def fake_db():
    try:
        print("Abrindo conexão com banco de dados ...")
        sleep(1)
    finally:
        print("Fechando conexão com banco de dados ...")
        sleep(1)


@app.get("/")
async def root(db=Depends(fake_db)):
    return {"message": "Hello World"}


@app.get(
    path="/cursos",
    response_model=List[Curso],
    description="Retorna todos os cursos ou uma lista vazia.",
    summary="Retorna todos os cursos",
)
async def get_cursos(db=Depends(fake_db)):
    return cursos


@app.get("/cursos/{curso_id}")
async def get_curso(
    curso_id: int = Path(title="ID do curso", description="Deve se inteiro"),
    db=Depends(fake_db),
):
    curso = [curso for curso in cursos if curso.id == curso_id]
    if not curso:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado."
        )

    return curso


@app.post("/cursos", status_code=status.HTTP_201_CREATED, response_model=CursoBD)
async def create_curso(curso: CursoBD, db=Depends(fake_db)):
    id = len(cursos) + 1
    cursos.append(Curso(id=id, **curso.model_dump()))

    return curso


@app.put("/cursos/{curso_id}")
async def update_curso(curso_id: int, curso: CursoBD, db=Depends(fake_db)):
    curso_found = [curso for curso in cursos if curso.id == curso_id]
    if not curso_found:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado."
        )

    cursos[curso_id - 1] = curso
    return curso


@app.delete("/cursos/{curso_id}")
async def delete_curso(curso_id: int, db=Depends(fake_db)):
    curso = [curso for curso in cursos if curso.id == curso_id]
    if not curso:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado."
        )
    else:
        del cursos[curso_id - 1]
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
