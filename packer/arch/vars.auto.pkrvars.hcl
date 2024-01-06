iso_url           = "http://lon.mirror.rackspace.com/archlinux/iso/2024.01.01/archlinux-2024.01.01-x86_64.iso"
iso_checksum      = "12addd7d4154df1caf5f258b80ad72e7a724d33e75e6c2e6adc1475298d47155"
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
