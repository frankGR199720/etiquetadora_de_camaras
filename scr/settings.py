from dotenv import load_dotenv
import os
from dataclasses import dataclass

@dataclass(frozen=False)
class Settings:
    PATH_DE_VARIABLE: str 
    PATH_PLANTILLA: str 
    PATH_HISTORIAL: str
    

load_dotenv()


PATH_DE_VARIABLE = os.getenv("PATH_DE_VARIABLE")
PATH_PLANTILLA = os.getenv("PATH_PLANTILLA")
PATH_HISTORIAL = os.getenv("PATH_HISTORIAL")

settings = Settings(PATH_DE_VARIABLE=PATH_DE_VARIABLE, PATH_PLANTILLA=PATH_PLANTILLA, PATH_HISTORIAL=PATH_HISTORIAL)