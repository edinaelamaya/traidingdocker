from fastapi.responses import JSONResponse
from fastapi import APIRouter
# folder = FastAPI()
get_nombre = APIRouter(tags=['create_detail'])

@get_nombre.get("/private/excel_rejection_detail")
def analitys_routes(nombre: str, edad: int):
    print(f"minombre es {nombre} y mi edad es {edad}")
    response = {
        "nombre": nombre,
        "edad": edad,
        "status": 200
    }
    return JSONResponse(content=response)