from __future__ import annotations

from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck

class K8S_Prefix_Enforced(BaseResourceCheck):
    def __init__(self) -> None:
        name = "Ensure namespaces are not created with reserved prefix for kubernetes system namespaces"
        id = "MDB_KUBERNETES_1"
        supported_resources = ['kubernetes_namespace']
        categories = (CheckCategories.KUBERNETES,),
        super().__init__(name=name, id=id, supported_resources=supported_resources, categories=categories)

    def scan_resource_conf(self, conf):
        if "metadata" in conf:
            metadata = conf["metadata"]
            if isinstance(metadata, list):
                metadata = metadata[0]
                if "name" in metadata:
                    name = metadata["name"][0]
                    if name.startswith('kube-'):
                        return CheckResult.FAILED
                else:
                    return CheckResult.PASSED
        else:
            return CheckResult.PASSED

        return CheckResult.PASSED
    
check = K8S_Prefix_Enforced()