from typing import Any
class FilterModule:
    ''' Gens da args '''
    DISTRO_KEY_CONVERT = {
        "Debian": "deb_install",
        "Archlinux": "arch_install"
    }
    def filters(self):
        return {
            'customizations_flattener': self.customizations_flattener,
        }

    def customizations_flattener(self, customizations: list[dict[str, Any]], os_distro: str):
        customization_dict = []
        for customization in customizations:
            new_customization = dict()
            new_customization["name"] = customization["name"]
            if "apt_sources" in customization:
                new_customization["apt_sources"] = customization["apt_sources"]

            packages = []
            for package in customization.get("packages", []):
                if type(package) is dict:
                    package_name = package.get(self.DISTRO_KEY_CONVERT[os_distro], package["name"])
                    if package_name != False:
                        packages.append(package_name)
                else:
                    packages.append(package)
            new_customization["packages"] = packages
            pip_packages = []
            for pip_package in customization.get("pip_packages", []):
                if type(pip_package) is dict:
                    pip_packages.append(pip_package["install"])
                else:
                    pip_packages.append(pip_package)
            new_customization["pip_packages"] = pip_packages
            roles = []
            for role in customization.get("roles", []):
                if type(role) is dict:
                    if role.get(self.DISTRO_KEY_CONVERT[os_distro], True):
                        roles.append(role["name"])
                else:
                    roles.append(role)
            new_customization["roles"] = roles
            customization_dict.append(new_customization)
        return customization_dict
