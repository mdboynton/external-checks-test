from __future__ import annotations

from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck

class AKS_RBAC_Enforced(BaseResourceCheck):
    def __init__(self) -> None:
        name = "Ensure Azure AKS enable role-based access control (RBAC) is enforced"
        id = "MDB_AZURE_1"
        supported_resources = ['azurerm_kubernetes_cluster']
        #categories = [CheckCategories.KUBERNETES]
        categories = (CheckCategories.KUBERNETES,),
        super().__init__(name=name, id=id, supported_resources=supported_resources, categories=categories)

    def scan_resource_conf(self, conf):
        if "azure_active_directory_role_based_access_control" in conf:
            rbac = conf["azure_active_directory_role_based_access_control"]
            if isinstance(rbac, list):
                rbac = rbac[0]
                enabled = rbac["azure_rbac_enabled"][0]
                if enabled == False:
                    return CheckResult.FAILED
        else:
            return CheckResult.FAILED

        return CheckResult.PASSED
    
check = AKS_RBAC_Enforced()