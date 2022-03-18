import os
from io import TextIOWrapper
from typing import List
from app.schema import FileContent, ClassInfo


class ScriptFileHandler():
    def __init__(self, class_info: ClassInfo):
        self.oClassInfo = class_info
        self.seprator = "/"
        self.script_root_folder = os.getenv('PY_CUSTOM_SCRIPTS_ROOT_PATH')

        self.script_draft_folder = f"{self.script_root_folder}{self.seprator}draft"
        self.script_active_folder = f"{self.script_root_folder}{self.seprator}active"
        self.__set_module_path()
        self.__check_script_folders()

    def __check_script_folders(self):
        # Script Folder
        if os.path.isdir(self.script_root_folder) == False:
            os.mkdir(self.script_root_folder) # create root folder

        if os.path.isdir(self.script_draft_folder) == False:
            os.mkdir(self.script_draft_folder) # create daft folder

        if os.path.isdir(self.script_active_folder) == False:
            os.mkdir(self.script_active_folder) # create active folder
    
    def __set_module_path(self):
        self.script_file_path = ""
        sFileName = """%s.py""" % (self.oClassInfo.classname)
        if self.oClassInfo.isdraft == True:
            self.script_file_path = f"{self.script_draft_folder}{self.seprator}{sFileName}"
        else:
            self.script_file_path = f"{self.script_active_folder}{self.seprator}{sFileName}"

        self.script_module_path = self.script_file_path
        self.script_module_path = self.script_module_path.replace(self.seprator, ".")
        self.script_module_path = self.script_module_path.replace(".py", "")
        self.script_module_name = self.script_module_path
        if self.script_module_path[0] == ".":
            self.script_module_name = self.script_module_path[1:]
    
    def is_file_exists(self):
        return os.path.isfile(self.script_file_path)

    def open_file_by_read_mode(self) -> str:
        if self.is_file_exists() == False:
            return ""
        sFileContent = ""    
        with open(self.script_file_path, "r") as oFile:
            sFileContent = oFile.read()
        
        return sFileContent
    
    def save_file_by_create_mode(self, sFileContent:str):
        with open(self.script_file_path, "x") as oFile:
            oFile.write("""%s""" % (sFileContent))
    
    def save_file_by_update_mode(self, sFileContent:str):
        with open(self.script_file_path, "r+") as oFile:
            oFile.write("""%s""" % (sFileContent))

    def buetify_file(self):
        os.system("black " + str(self.script_file_path))

    def save_file_content(self, sFileContent:str):
        if self.is_file_exists():
            self.save_file_by_update_mode(sFileContent)
        else:
            self.save_file_by_create_mode(sFileContent)
        
        self.buetify_file()

    def get_file_content_read_mode(self)-> FileContent:
        return FileContent(
            is_file_exists= self.is_file_exists(),
            file_content= self.open_file_by_read_mode()
        )
        

