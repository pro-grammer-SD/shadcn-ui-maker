class Accordion:
    def __init__(self):
        pass
    
...

class Badge:
    def __init__(self, name):
        self.script = f"""
import { Badge } from "@/components/ui/badge"
<Badge variant="default |outline | secondary | destructive">{name}</Badge>
"""

    def get_script(self):
        return self.script

class Button:
    """A class representing a button element.

    Attributes:
        name(str): Name of the button, defaults to "Button"
        styling(str): CSS styling for the button, defaults to "flex flex-wrap items-center gap-2 md:flex-row"
    """
    def __init__(self, name: str = "Button", styling: str = "flex flex-wrap items-center gap-2 md:flex-row"):
        self.script = f"<Button>{name}</Button>"
    
    def connect(self, action: str):
        return "onClick={() => " + f"{action}" + "}"
        
    def get_script(self):
        return self.script
    