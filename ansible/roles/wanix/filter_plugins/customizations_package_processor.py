from typing import Any, Union
from ansible.parsing.yaml.objects import AnsibleUnicode

class FilterModule:
    ''' Gens da args '''
    DISTRO_KEY_CONVERT = [
        ("Debian", "deb_install"),
        ("Archlinux", "arch_install")
    ]
    def filters(self):
        return {
            'cd_package_extractor': self.cd_package_extractor,
            'cd_app_name_extractor': self.cd_app_name_extractor
        }

    def _get_value_name(self, value:Union[dict[str, str], str], enabled: bool) -> tuple[str, bool]:
        if type(value) is AnsibleUnicode:
            return (value, enabled)
        elif type(value) is dict:
            return (value["name"], enabled)
        else:
            raise ValueError("invalid nested name type: %s" % type(value))

    def cd_package_extractor(self, customizations: list[dict[str, Any]], included_customizations: list[str], os_distro: str):
        ''' takes a customization dict and returns a zip of all packages and if thay are installed'''
        total_packages: list[tuple[str, bool]] = []
        for customization in customizations:
            included_customization = customization["name"] in included_customizations

            total_packages += [self._get_value_name(package, included_customization) for package in customization.get("pip_packages", [])]
            for package in customization.get("packages", []):
                if type(package) is dict:
                    for distro, key_name in self.DISTRO_KEY_CONVERT:
                        package_name = package.get(key_name, package["name"])
                        if  package_name != False:
                            total_packages.append((package_name, included_customization and distro == os_distro))

                else:
                    total_packages.append((package, included_customization))
            for role in customization.get("roles", []):
                if type(role) is dict:
                    role_packages = role.get("provides_pkgs", [])
                    total_packages += list(zip(role_packages, [included_customization]*len(role_packages)))
        return sorted(set(total_packages))

    def cd_app_name_extractor(self, customizations: list[dict[str, Any]], included_customizations: list[str]):
        ''' takes a customization dict and returns a zip of all packages and if thay are installed'''
        total_packages: list[tuple[str, bool]] = []
        for customization in customizations:
            included_customization = customization["name"] in included_customizations
            total_packages += [self._get_value_name(package, included_customization) for package in customization.get("packages", [])]

        return sorted(set(total_packages))

