from ansible.errors import AnsibleFilterTypeError


class FilterModule:
    ''' Gens da args '''

    def filters(self):
        return {
            'proxmox_netconf_gen': self.proxmox_netconf_gen
        }

    def proxmox_netconf_gen(self, config: dict[str, str]):
        ''' takes a string, and return a list of
            the individual path components '''
        if isinstance(config, dict):
            netconf = [
                f"virtio={config['mac']}",
                f"bridge={config['bridge']}"
            ]
            if config['firewall']:
                netconf.append(f"firewall={config['firewall']}")
            if config['tag']:
                netconf.append(f"tag={config['tag']}")
            return ",".join(netconf).encode("utf-8")


        raise AnsibleFilterTypeError("|path_split expects string, got %s instead." % type(path))
