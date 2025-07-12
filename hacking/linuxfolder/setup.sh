#!/bin/bash

# Màu sắc cho output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${GREEN}Starting installation of hacking tools...${NC}"

# Cập nhật hệ thống
echo -e "${YELLOW}Updating system...${NC}"
sudo pacman -Syu --noconfirm

# Cài đặt các công cụ cơ bản
echo -e "${YELLOW}Installing basic tools...${NC}"
sudo pacman -S --noconfirm nmap wireshark-qt tcpdump netcat aircrack-ng

# Cài đặt các công cụ web security
echo -e "${YELLOW}Installing web security tools...${NC}"
sudo pacman -S --noconfirm burpsuite sqlmap nikto dirb wfuzz

# Cài đặt các công cụ password
echo -e "${YELLOW}Installing password tools...${NC}"
sudo pacman -S --noconfirm john hashcat hydra

# Cài đặt các công cụ exploitation
echo -e "${YELLOW}Installing exploitation tools...${NC}"
sudo pacman -S --noconfirm metasploit exploit-db gdb radare2

# Cài đặt các công cụ forensics
echo -e "${YELLOW}Installing forensics tools...${NC}"
sudo pacman -S --noconfirm volatility autopsy binwalk

# Cài đặt các công cụ bổ sung
echo -e "${YELLOW}Installing additional tools...${NC}"
sudo pacman -S --noconfirm python-pip python-virtualenv git

# Tạo môi trường Python ảo
echo -e "${YELLOW}Creating Python virtual environment...${NC}"
python -m venv .venv
source .venv/bin/activate

# Cài đặt các thư viện Python
echo -e "${YELLOW}Installing Python packages...${NC}"
pip install -r requirements.txt

# Tải wordlists
echo -e "${YELLOW}Downloading wordlists...${NC}"
cd wordlists
wget https://github.com/danielmiessler/SecLists/archive/master.zip
unzip master.zip
mv SecLists-master/* .
rm -rf SecLists-master master.zip
cd ..

# Cấu hình Metasploit
echo -e "${YELLOW}Configuring Metasploit...${NC}"
sudo systemctl start postgresql
sudo systemctl enable postgresql
sudo msfdb init

# Cấu hình Wireshark
echo -e "${YELLOW}Configuring Wireshark...${NC}"
sudo usermod -a -G wireshark $USER

echo -e "${GREEN}Installation completed!${NC}"
echo -e "${YELLOW}Please logout and login again to apply all changes.${NC}"
echo -e "${YELLOW}Don't forget to activate the virtual environment with: source .venv/bin/activate${NC}" 