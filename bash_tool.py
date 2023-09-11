from abc import ABC
from superagi.tools.base_tool import BaseToolkit, BaseTool
from typing import Type, List
import subprocess
import shlex
from pydantic import BaseModel, Field
import os

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
    agent_id: int = None
    description: str = "Executes a Bash Command"

    def _execute(self, command: str = None):
        if not validate_command(command):
            return "Invalid bash command."
        
        print("zzh")
        print(f'{self.agent_id}')
        print(f'{agent_id}')

        try:
            result = subprocess.run(f'cd ./workspace && {command}', shell=True, check=True, stdout=subprocess.PIPE)
            return result.stdout.decode('utf-8') + self.agent_id
        except subprocess.CalledProcessError as e:
            return f"Command '{command}' returned non-zero exit status {e.returncode}."
