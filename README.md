# janksetup

A collection of scripts, Ansible playbooks, Packer templates, and possibly Terraform (Tofu) configurations designed to transform an already janky hypervisor into an even more janky hypervisor. This setup configures Proxmox to run completely headless. ([rippleFCL/janksetup: a collection of scrips, ansible, packer ... - GitHub](https://github.com/rippleFCL/janksetup?utm_source=chatgpt.com))

## Features

- **Headless Proxmox Configuration**: Automates the setup of a headless Proxmox environment.
- **Automation Tools**: Utilizes Ansible for configuration management and Packer for image building.
- **Potential Terraform Integration**: May include Terraform (Tofu) scripts for infrastructure provisioning. ([rippleFCL/janksetup: a collection of scrips, ansible, packer ... - GitHub](https://github.com/rippleFCL/janksetup?utm_source=chatgpt.com), [rippleFCL - GitHub](https://github.com/rippleFCL?utm_source=chatgpt.com))

## Getting Started

### Prerequisites

- Proxmox VE installed on your hypervisor.
- Ansible installed on your control machine.
- Packer installed for image building.
- Python dependencies listed in `req.txt`. ([rippleFCL/janksetup: a collection of scrips, ansible, packer ... - GitHub](https://github.com/rippleFCL/janksetup?utm_source=chatgpt.com))

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/rippleFCL/janksetup.git
   cd janksetup
   ```


2. **Install Python Dependencies**:

   ```bash
   pip install -r req.txt
   ```


3. **Run Ansible Playbooks**:

   Navigate to the `ansible` directory and execute the playbooks as needed.

   ```bash
   cd ansible
   ansible-playbook playbook.yml
   ```


4. **Build Images with Packer**:

   Navigate to the `packer` directory and build images.

   ```bash
   cd ../packer
   packer build template.json
   ```


## Directory Structure

- `ansible/`: Contains Ansible playbooks for configuring Proxmox.
- `packer/`: Contains Packer templates for building VM images.
- `.vscode/`: Visual Studio Code settings.
- `req.txt`: Python dependencies required for the setup.
- `LICENSE`: MIT License file. ([rippleFCL/janksetup: a collection of scrips, ansible, packer ... - GitHub](https://github.com/rippleFCL/janksetup?utm_source=chatgpt.com), [XRPLF/rippled: Decentralized cryptocurrency blockchain ... - GitHub](https://github.com/XRPLF/rippled?utm_source=chatgpt.com))

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

*Note: This setup is intended for educational and experimental purposes. Use at your own risk.* 
