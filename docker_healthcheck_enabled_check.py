from __future__ import annotations

from typing import TYPE_CHECKING

from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.dockerfile.base_dockerfile_check import BaseDockerfileCheck

if TYPE_CHECKING:
    from dockerfile_parse.parser import _Instruction

class Healthcheck_Enabled(BaseDockerfileCheck):
    def __init__(self) -> None:
        name = "Ensure health check instructions are enabled"
        id = "MDB_DOCKER_1"
        supported_instructions = ("*",)
        categories = (CheckCategories.GENERAL_SECURITY,),
        super().__init__(name=name, id=id, categories=categories, supported_instructions=supported_instructions)

    #def scan_resource_conf(self, conf):
    def scan_resource_conf(self, conf: dict[str, list[_Instruction]]) -> tuple[CheckResult, list[_Instruction] | None]:
        for instruction, content in conf.items():
            if instruction == 'HEALTHCHECK':
                return CheckResult.PASSED, content

        return CheckResult.FAILED, None
    
check = Healthcheck_Enabled()