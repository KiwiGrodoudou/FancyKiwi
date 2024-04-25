
from typing import Literal



class ColoredString(str):
    
    def __init__(self,string:str):
        """
        Args:
            string (str): The string to be printed in color (can also be anything that can be converted to a string using str() function)
        """
        super().__init__() # how the hell does this work???
    
    def green(self)->'ColoredString':
        return self.__class__('\033[92m' + self + '\033[0m')
    
    def blue(self)->'ColoredString':
        return self.__class__('\033[94m' + self + '\033[0m')
    
    def red(self)->'ColoredString':
        return self.__class__('\033[91m' + self + '\033[0m')
    
    def yellow(self)->'ColoredString':
        return self.__class__('\033[93m' + self + '\033[0m')
    
    def bold(self)->'ColoredString':
        return self.__class__('\033[1m' + self + '\033[0m')
    
    def underline(self)->'ColoredString':
        return self.__class__('\033[4m' + self + '\033[0m')
    
    def italic(self)->'ColoredString':
        return self.__class__('\033[3m' + self + '\033[0m')
    
    def strikethrough(self)->'ColoredString':
        return self.__class__('\033[9m' + self + '\033[0m')
    
    def highlight(self)->'ColoredString':
        return self.__class__('\033[7m' + self + '\033[0m')
    
    def print(self)->None:
        print(self)
        

class Message:
    
    markers = {
        "success": ["done","ok","success","complete","finish","computed","processed","created","ready"],
        "danger": ["error","fail","fatal","problem","issue","unable"],
        "warning": ["warning","alert","attention","caution"]
    }
    prefix = "[#] "
    
    muted = False
    
    
    def __init__(self,msg:str,typ:Literal["success","warning","danger","neutral"]="neutral") -> None:

        match typ:
            case "success":
                prefix = ColoredString(Message.prefix).green()
            case "warning":
                prefix = ColoredString(Message.prefix).yellow()
            case "danger":
                prefix = ColoredString(Message.prefix).red()
            case "neutral":
                prefix = self._guess_prefix(msg)
            case _:
                prefix = self._guess_prefix(msg)
                
        if not self.muted:
            print(prefix+msg)
    
    def _guess_prefix(self,msg:str)->str:
        msg = msg.lower()
        
        for m in Message.markers["success"]:
            if m in msg:
                return ColoredString(Message.prefix).green()
        
        for m in Message.markers["danger"]:
            if m in msg:
                return ColoredString(Message.prefix).red()
        
        for m in Message.markers["warning"]:
            if m in msg:
                return ColoredString(Message.prefix).yellow()
            
        return Message.prefix
    
    def __repr__(self) -> str:
        return ""
    
    @classmethod
    def mute(cls:type):
        cls.muted = True
    
    @classmethod
    def unmute(cls:type):
        cls.muted = False
        
    @staticmethod
    def red(msg:str)->str:
        return(str(ColoredString(msg).red()))
    
    @staticmethod
    def green(msg:str)->str:
        return(str(ColoredString(msg).green()))
    
    @staticmethod
    def blue(msg:str)->str:
        return(str(ColoredString(msg).blue()))
    
    @staticmethod
    def yellow(msg:str)->str:
        return(str(ColoredString(msg).yellow()))
    
    @staticmethod
    def cstr(msg:str)->ColoredString:
        return ColoredString(msg)