from typing import Any
from ansible.parsing.yaml.objects import AnsibleUnicode
from pathlib import Path

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

    def file_copy_processor(self, files: list[dict[str, str]], packages: list[str], customisations: list[str], copy_info_data: list[dict[str, str]], dep_map: list[dict[str, Any]], user_home: str):
        ''' takes a customisation dict and returns a zip of all packages and if thay are installed'''
        files_to_copy: list[dict[str, str]] = []
        if isinstance(files, dict):
            files = [files]
        for file in files:
            fullpath = str(Path(file["root"]) / file["path"])
            for dependency in dep_map:
                if dependency["path"] in fullpath:
                    package_dep_check = [
                        package in packages for package in dependency.get("packages", [])]
                    if False in package_dep_check:
                        break
                    customisations_dep_check = [
                        customisation in customisations for customisation in dependency.get("customisations", [])]
                    if False in customisations_dep_check:
                        break
            else:
                dest_info = {"path": ""}
                for copy_info in copy_info_data:
                    if copy_info["source"] in fullpath:
                        dest_info.update({
                            "mode": copy_info.get("mode", dest_info.get("mode", "")),
                            "user": copy_info.get("user", dest_info.get("user", "")),
                            "group": copy_info.get("group", dest_info.get("group", ""))
                        })

                        if "link_home_relative" in copy_info or "link_root_relative" in copy_info:
                            file["state"] = "link"

                        if "link_home_relative" in copy_info:
                            file["src"] = str(Path(user_home) / copy_info["link_home_relative"] / file["path"])
                        elif "link_root_relative" in copy_info:
                            file["src"] = str(Path(copy_info["link_root_relative"]) / file["path"])

                        if "home_relative" in copy_info:
                            dest_info["path"] = str(Path(user_home) / copy_info["home_relative"] / file["path"])
                        elif "root_relative" in copy_info:
                            dest_info["path"] = str(Path(copy_info["root_relative"]) / file["path"])

                missing_keys = list(filter(lambda x: not x[1], [(key,bool(value)) for key, value in dest_info.items()]))
                if missing_keys:
                    raise Exception(f"missing dest info keys: {', '.join(map(lambda x: x[0], missing_keys))}")

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
