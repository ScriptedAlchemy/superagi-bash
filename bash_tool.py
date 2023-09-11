from abc import ABC
from superagi.tools.base_tool import BaseToolkit, BaseTool
from superagi.models.agent import Agent
from superagi.helper.resource_helper import ResourceHelper
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
        # input_directory = ResourceHelper.get_root_input_dir()
        output_directory = ResourceHelper.get_root_output_dir()
        if "{agent_id}" in output_directory:
            output_directory = ResourceHelper.get_formatted_agent_level_path(agent=Agent
                                                                            .get_agent_from_id(session=self
                                                                                               .toolkit_config.session,
                                                                                               agent_id=self.agent_id),
                                                                            path=output_directory)

        print(output_directory)
        try:
            result = subprocess.run(f'cd ./workspace && {command}', shell=True, check=True, stdout=subprocess.PIPE)
            return result.stdout.decode('utf-8') + self.agent_id
        except subprocess.CalledProcessError as e:
            return f"Command '{command}' returned non-zero exit status {e.returncode}."
