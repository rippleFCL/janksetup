from typing import Any, Union
from ansible.parsing.yaml.objects import AnsibleUnicode
from typing import Literal
class FilterModule:
    ''' Gens da args '''
    DISTRO_KEY_CONVERT = {
        "Debian": "deb_install",
        "Archlinux": "arch_install"
    }
    def filters(self):
        return {
            'cd_package_extractor': self.cd_package_extractor,
        }

    def _get_value_name(self, value:Union[dict[str, str], str]) -> str:
        if type(value) is AnsibleUnicode:
            return value
        elif type(value) is dict:
            return value["name"]
        else:
            raise ValueError("invalid nested name type: %s" % type(value))

    def cd_package_extractor(self, customizations: list[dict[str, Any]], included_customizations: list[str], os_distro: str):
        ''' takes a customization dict and returns a zip of all packages and if thay are installed'''
        total_packages: list[str] = []
        for customization in filter(lambda cust: cust["name"] in included_customizations, customizations):

            for pip_package in customization.get("pip_packages", []):
                total_packages.append(self._get_value_name(pip_package))

            for package in customization.get("packages", []):
                if isinstance(package, dict):
                    package_name = package.get(self.DISTRO_KEY_CONVERT[os_distro], package["name"])
                    total_packages.append(package_name)

                else:
                    total_packages.append(package)
            for role in customization.get("roles", []):
                if isinstance(role, dict):
                    for package in role.get("provides_pkgs", []):
                        total_packages.append(package)


        return total_packages

