from typing import Any


class FilterModule:
    ''' Gens da args '''
    DISTRO_KEY_CONVERT = {
        "Debian": "deb_install",
        "Archlinux": "arch_install"
    }

    def filters(self):
        return {
            'customisations_flattener': self.customisations_flattener,
        }

    def customisations_flattener(self, customisations: list[dict[str, Any]], os_distro: str):
        customisation_dict = []
        for customisation in customisations:
            new_customisation = dict()
            new_customisation["name"] = customisation["name"]
            if "apt_sources" in customisation:
                new_customisation["apt_sources"] = customisation["apt_sources"]

            packages = []
            for package in customisation.get("packages", []):
                if type(package) is dict:
                    package_name = package.get(
                        self.DISTRO_KEY_CONVERT[os_distro], package["name"])
                    if package_name != False:
                        packages.append(package_name)
                else:
                    packages.append(package)
            new_customisation["packages"] = packages
            pip_packages = []
            for pip_package in customisation.get("pip_packages", []):
                if type(pip_package) is dict:
                    pip_packages.append(pip_package["install"])
                else:
                    pip_packages.append(pip_package)
            new_customisation["pip_packages"] = pip_packages
            roles = []
            for role in customisation.get("roles", []):
                if type(role) is dict:
                    if role.get(self.DISTRO_KEY_CONVERT[os_distro], True):
                        roles.append(role["name"])
                else:
                    roles.append(role)
            new_customisation["roles"] = roles
            customisation_dict.append(new_customisation)
        return customisation_dict
