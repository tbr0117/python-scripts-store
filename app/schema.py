from typing import Optional
from pydantic import BaseModel
from typing import Optional

class FileContent(BaseModel):
    is_file_exists: Optional[bool]
    file_content: str

class ClassInfo(BaseModel):
    classname: str
    isdraft: bool