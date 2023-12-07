iso_url           = "http://www.mirrorservice.org/sites/ftp.archlinux.org/iso/2023.12.01/archlinux-2023.12.01-x86_64.iso"
iso_checksum      = "50c688670abf27345b3effa03068b0302810f8da0db80d06d11a932c3ef99056"
iso_checksum_type = "sha256"
guest_username    = "ripple"
ansible_username  = "ansible"

proxmox_url       = "10.0.1.30:8006"
proxmox_node      = "pve-workstation"
disk_pool         = "local-lvm"
iso_storage_pool  = "local"
disk_size         = "20G"
vm_ip_addr        = "10.0.5.30/24"

ansible_inventory_dir = "../../ansible/environment/prod"


network_adaptors = [
    {
        driver  = "virtio",
        adapter = "vmbr0",
        vlan    = 70
    }
]