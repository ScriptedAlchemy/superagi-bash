from abc import ABC
from superagi.tools.base_tool import BaseToolkit, BaseTool
from typing import Type, List
import subprocess
import shlex
from pydantic import BaseModel, Field
from greetings_tool import BashCommandTool

# Update the Toolkit class
class BashCommandToolkit(BaseToolkit, ABC):
    name: str = "Bash Command Toolkit"
    description: str = "Toolkit contains all tools related to Bash Command execution"

    def get_tools(self) -> List[BaseTool]:
        return [BashCommandTool()]

    # def get_env_keys(self) -> List[str]:
    #     return []
