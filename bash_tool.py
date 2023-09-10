from abc import ABC
from superagi.tools.base_tool import BaseToolkit, BaseTool
from typing import Type, List
import subprocess
import shlex
from pydantic import BaseModel, Field

class BashCommandInput(BaseModel):
    command: str = Field(..., description="Bash command to be executed")

# Function to validate bash command
def validate_command(command: str) -> bool:
    try:
        shlex.split(command)
        return True
    except ValueError:
        return False

class BashCommandTool(BaseTool):
    """
    Bash Command Tool
    """
    name: str = "Bash Command Tool"
    args_schema: Type[BaseModel] = BashCommandInput
    description: str = "Executes a Bash Command"  # Fixed indentation here

    def _execute(self, command: str = None):
        if not validate_command(command):
            return "Invalid bash command."
        
        try:
            result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE)
            return result.stdout.decode('utf-8')
        except subprocess.CalledProcessError as e:
            return f"Command '{command}' returned non-zero exit status {e.returncode}."