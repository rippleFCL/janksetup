iso_url           = "https://www.mirrorservice.org/sites/ftp.archlinux.org/iso/2024.04.01/archlinux-x86_64.iso"
iso_checksum      = "52aea58f88c9a80afe64f0536da868251ef4878de5a5e0227fcada9f132bd7ab"
iso_checksum_type = "sha256"
guest_username    = "ripple"
ansible_username  = "ansible"

http_interface = "vmbr0.10@vmbr0"

proxmox_url       = "10.0.1.30:8006"
proxmox_node      = "pve-workstation"
disk_pool         = "local-lvm"
iso_storage_pool  = "local"
disk_size         = "1000G"
vm_ip_addr        = "10.0.5.30/24"

ansible_inventory_dir = "../../ansible/environment/prod"


network_adaptors = [
    {
        driver  = "virtio",
        adapter = "vmbr0",
        vlan    = 10
    }
]
