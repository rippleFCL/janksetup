from typing import Any
from ansible.parsing.yaml.objects import AnsibleUnicode


class FilterModule:
    ''' Gens da args '''
    DISTRO_KEY_CONVERT = {
        "Debian": "deb_install",
        "Archlinux": "arch_install"
    }

    def filters(self):
        return {
            'file_copy_processor': self.file_copy_processor,
            'filter_types': self.filter_types
        }

    def file_copy_processor(self, files: list[dict[str, str]], packages: list[str], customizations: list[str], copy_info_data: list[dict[str, str]], dep_map: list[dict[str, Any]], user_home: str):
        ''' takes a customization dict and returns a zip of all packages and if thay are installed'''
        files_to_copy: list[dict[str, str]] = []
        if isinstance(files, dict):
            files = [files]
        for file in files:
            fullpath = file["root"] + file["path"]
            for dependency in dep_map:
                if dependency["path"] in fullpath:
                    package_dep_check = [
                        package in packages for package in dependency.get("packages", [])]
                    if False in package_dep_check:
                        break
                    customizations_dep_check = [
                        customization in customizations for customization in dependency.get("customizations", [])]
                    if False in customizations_dep_check:
                        break
            else:
                dest_info = {"path": ""}
                for copy_info in copy_info_data:
                    if copy_info["source"] in fullpath:
                        dest_info["mode"] = copy_info.get("mode", dest_info.get("mode", ""))
                        dest_info["user"] = copy_info.get("user", dest_info.get("user", ""))
                        dest_info["group"] = copy_info.get("group", dest_info.get("group", ""))

                        if "home_relative" in copy_info:
                            dest_info["path"] = user_home + \
                                copy_info["home_relative"] + file["path"]
                        elif "root_relative" in copy_info:
                            dest_info["path"] = copy_info["root_relative"] + \
                                file["path"]

                if False in [bool(value) for value in dest_info.values()]:
                    raise Exception("missing dest info")

                file_data = {
                    "src": fullpath,
                    "dest": dest_info["path"].replace(".j2", ""),
                    "link": file["src"] if file["state"] != "directory" else "",
                    "type": "template" if ".j2" in dest_info["path"] else file["state"],
                    "user": dest_info["user"],
                    "group": dest_info["group"],
                    "mode": dest_info["mode"]
                }
                files_to_copy.append(file_data)

        return files_to_copy

    def filter_types(self, file_infos: list[dict[str, str]], type_filer: str):
        return [file_info for file_info in file_infos if file_info["type"] == type_filer]
