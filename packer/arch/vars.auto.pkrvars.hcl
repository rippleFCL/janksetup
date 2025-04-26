iso_url           = "https://www.mirrorservice.org/sites/ftp.archlinux.org/iso/2025.04.01/archlinux-2025.04.01-x86_64.iso"
iso_checksum      = "1155af9c142387c45eb6fbdbf32f5652fb514ce15a4d17a83e6056a996895026"
iso_checksum_type = "sha256"
guest_username    = "ripple"
ansible_username  = "ansible"

http_interface = "vmbr1"

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
        adapter = "vmbr1",
    }
]
