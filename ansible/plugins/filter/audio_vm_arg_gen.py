from ansible.errors import AnsibleFilterTypeError


class FilterModule:
    ''' Gens da args '''

    def filters(self):
        return {
            'audio_vm_arg_gen': self.audio_vm_arg_gen
        }

    def audio_vm_arg_gen(self, config: list[dict[str, str]]):
        ''' takes a string, and return a list of
            the individual path components '''
        if isinstance(config, list):
            audio_translation = {
                "output": "hda-output",
                "duplex": "hda-duplex",
                "input": "hda-input"
            }
            audio_vm_args = []
            for index, config_values in enumerate(config):
                audio_dev_args = [f"-audiodev pa,id=pa{index}","server=unix:/tmp/pulse-socket,out.mixing-engine=off"]
                if config_values['output']:
                    audio_dev_args.append(f"out.name={config_values['output']}")
                if config_values['input']:
                    audio_dev_args.append(f"in.name={config_values['input']}")
                devices = " ".join([
                    ','.join(audio_dev_args),
                    "-device intel-hda",
                    f"-device {audio_translation[config_values['type']]},audiodev=pa{index}"
                ])
                audio_vm_args.append(devices)
            return " ".join(audio_vm_args).encode("utf-8")

        raise AnsibleFilterTypeError("|path_split expects string, got %s instead." % type(path))
