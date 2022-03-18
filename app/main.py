from fastapi import FastAPI, APIRouter, Depends
from starlette.middleware.cors import CORSMiddleware
from app.config import settings
from app.schema import ClassInfo, FileContent
from app.script_handler import ScriptFileHandler

api_router = APIRouter()
app = FastAPI(title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json")

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin)
                       for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def get_class_info(classname:str, isdraft:bool)->ClassInfo:
    return ClassInfo(
        classname= classname,
        isdraft= isdraft
    )


@api_router.get("/script", response_model=FileContent)
def get_script_file_content(
    *,
    class_info: ClassInfo = Depends(get_class_info))->FileContent:
    script_handler = ScriptFileHandler(class_info)
    return script_handler.get_file_content_read_mode()

@api_router.post("/script", response_model=str)
def save_script_file_content(
    *,
    class_info: ClassInfo = Depends(get_class_info), 
    oFileContent:FileContent) ->str:
    script_handler = ScriptFileHandler(class_info)
    script_handler.save_file_content(f"""{oFileContent.file_content}""")

app.include_router(api_router,  prefix=settings.API_V1_STR)