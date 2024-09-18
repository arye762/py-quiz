questions_701_C = [
# 401-420
{
  "question": "An administrator is responding to a network server outage. The administrator has logged in to the server to troubleshoot the outage. Which of the following is the first step the administrator should take when attempting to troubleshoot the issue?",
  "options": [
    "Document the results",
    "Analyze the error logs",
    "Check the physical connections",
    "Upgrade the server firmware"
  ],
  "correct_answer": 3,
  "description": "The correct answer is **Check the physical connections**. In many cases, server outages can result from simple physical issues like disconnected cables or faulty connections, which are the easiest to check first.\n\n- **Document the results**: While documentation is crucial, it typically happens after troubleshooting or after actions are taken to resolve the issue.\n- **Analyze the error logs**: Analyzing logs is important but should be done after verifying physical connections, as it may take more time.\n- **Upgrade the server firmware**: This is not the first step, and updating firmware during an outage could potentially make things worse without thorough checks."
},
{
  "question": "A computer freezes shortly after loading the operating system. A technician inspects the computer and obtains the following diagnostic information:\n\nCPU: 3.4GHz 6 core\nVcore: 1.25V\nFan speed: 5000rpm\nTemperature: 93C\n\nGPU: PCIe\nMemory: 4GB\nGPU voltage: 1.093V\nGPU temperature: 75C\n\nMainboard: ATX\nRAM: (4x) 8GB DDR4 2400\nRAM frequency: 2133\nTemperature: 38C\nSecure boot: On\n\nPower supply: 750W\n3.3V rail: 3.24V\n12V rail: 11.78V\n5V rail: 4.87V\n\nHard drive S.M.A.R.T. data:\n- Raw read error rate: 200\n- Seek error rate: 200\n- Reallocated sector count: 100\n\nWhich of the following should the technician investigate further?",
  "options": [
    "The memory clock speed settings",
    "The integrity of the hard drive",
    "The CPU temperatures",
    "The power supply voltage",
    "The GPU temperatures"
  ],
  "correct_answer": 3,
  "description": "The correct answer is **The CPU temperatures**. The CPU is running at a very high temperature (93°C), which is likely causing the system to freeze. The technician should focus on cooling the CPU to avoid damage or further system instability.\n\n- **The memory clock speed settings**: While the RAM frequency is lower than expected, this would not typically cause system freezes.\n- **The integrity of the hard drive**: The S.M.A.R.T. data indicates no significant issues with the hard drive, so this is unlikely the cause of the problem.\n- **The power supply voltage**: The voltages are within acceptable ranges for a 750W power supply, so no immediate concern here.\n- **The GPU temperatures**: The GPU temperature (75°C) is high but not critical for most GPUs under load."
},

  {
    "question": "Which of the following is considered a connectionless protocol?",
    "options": [
      "SSH",
      "TCP",
      "HTTPS",
      "UDP"
    ],
    "correct_answer": 4,
    "description": "The correct answer is **UDP**. UDP (User Datagram Protocol) is a connectionless protocol that sends data without establishing a connection beforehand.\n\n- **SSH**: A protocol used for secure remote access but is connection-oriented.\n- **TCP**: Transmission Control Protocol, which establishes a connection before transmitting data.\n- **HTTPS**: A secure version of HTTP, which uses TCP for communication."
  },
  {
    "question": "An IT technician is troubleshooting an issue with connecting a new laptop to a company's wireless network. Which of the following diagnostic steps should the technician take first?",
    "options": [
      "Review the network settings in the OS.",
      "Install the latest firmware updates on the WAPs.",
      "Increase the signal strength of the router.",
      "Reset the router and reconfigure the wireless settings."
    ],
    "correct_answer": 1,
    "description": "The correct answer is **Review the network settings in the OS**. The first step is to check the settings on the laptop to ensure the network configuration is correct.\n\n- **Install the latest firmware updates on the WAPs**: This should not be done until more basic diagnostic steps are completed.\n- **Increase the signal strength of the router**: Signal strength adjustments are not usually the first troubleshooting step unless the signal is already confirmed as weak.\n- **Reset the router and reconfigure the wireless settings**: Resetting the router is a more disruptive step and should be avoided until simpler steps have been taken."
  },
  {
    "question": "A technician is installing a storage solution for a computer that requires data redundancy with the fewest drives possible. Which of the following would best meet this requirement?",
    "options": [
      "RAID 0",
      "RAID 1",
      "RAID 5",
      "RAID 10"
    ],
    "correct_answer": 2,
    "description": "The correct answer is **RAID 1**. RAID 1 requires the fewest drives (only 2) to provide data redundancy through mirroring.\n\n- **RAID 0**: Does not provide data redundancy, only improves performance.\n- **RAID 5**: Requires at least 3 drives but offers both redundancy and performance.\n- **RAID 10**: Requires a minimum of 4 drives and provides both redundancy and performance."
  },
  {
    "question": "Which of the following ports allows for secure communications?",
    "options": [
      "20",
      "22",
      "23",
      "25"
    ],
    "correct_answer": 2,
    "description": "The correct answer is **Port 22**. Port 22 is used for SSH (Secure Shell), which provides secure remote access to devices.\n\n- **Port 20**: Used for FTP data transfer, which is not secure.\n- **Port 23**: Used for Telnet, which is not secure.\n- **Port 25**: Used for sending emails through SMTP, but it is not inherently secure."
  },
  {
    "question": "A company laptop uses a docking station with an integrated NIC and is unable to access a wired SOHO network using DHCP. A technician runs ipconfig and discovers the laptop has an IPv4 assignment of 169.254.0.9. The NIC does not have any link or activity lights on. Which of the following should the technician do next?",
    "options": [
      "Restart the laptop in safe mode.",
      "Reboot the DHCP server.",
      "Reset the network adapter.",
      "Replace the laptop.",
      "Reset the laptop in the docking station."
    ],
    "correct_answer": 3,
    "description": "The correct answer is **Reset the network adapter**. Since there are no link or activity lights, it’s likely a problem with the network adapter itself.\n\n- **Restart the laptop in safe mode**: This option would not directly address the issue with the network adapter.\n- **Reboot the DHCP server**: The problem is likely with the laptop, not the server, as indicated by the APIPA address.\n- **Replace the laptop**: This step is drastic and would be premature at this stage.\n- **Reset the laptop in the docking station**: Reseating the laptop might help, but resetting the network adapter is a more targeted solution."
  },
  {
    "question": "A user contacted the help desk about files that disappeared from a laptop. The technician discovered during troubleshooting that the drive was corrupt due to a possible mechanical failure, but the files were still readable. Which of the following actions did the technician take during troubleshooting? (Choose two.)",
    "options": [
      "Checked S.M.A.R.T. information",
      "Made sure the replacement drive was compatible",
      "Ran CHKDSK",
      "Reseated the HDD connector",
      "Increased the page file size",
      "Updated the firmware"
    ],
    "correct_answers": [1, 3],
    "description": "The correct answers are **Checked S.M.A.R.T. information** and **Ran CHKDSK**. These are the most relevant actions for diagnosing and attempting to resolve a mechanical failure on a hard drive.\n\n- **Made sure the replacement drive was compatible**: This is a later step if the drive needs replacing, but the technician hasn't reached this point yet.\n- **Reseated the HDD connector**: Could be useful, but since the files are readable, the connection is likely fine.\n- **Increased the page file size**: Not relevant to hardware troubleshooting.\n- **Updated the firmware**: This would not address mechanical failure."
  },
  {
    "question": "A laptop is experiencing slow performance writing data. Which of the following is the best component for a technician to upgrade to fix the issue?",
    "options": [
      "RAM",
      "HDD",
      "TPM",
      "CPU"
    ],
    "correct_answer": 2,
    "description": "The correct answer is **HDD**. Upgrading the hard drive, especially to an SSD, would improve the laptop's data write performance.\n\n- **RAM**: Increasing RAM may improve overall system performance, but it does not specifically target slow data writes.\n- **TPM**: TPM relates to security, not performance.\n- **CPU**: While upgrading the CPU might help overall performance, it would not specifically address the data write issue."
  },

  #421-440


  {
    "question": "A user purchased a new smartphone and headset and is trying to connect them. Which of the following is the best way to connect the devices?",
    "options": [
      "Enable pairing.",
      "Use a hotspot.",
      "Use NFC.",
      "Enable synchronization."
    ],
    "correct_answer": 1,
    "description": "The correct answer is **Enable pairing**. Pairing is used for Bluetooth devices like headsets to connect to smartphones.\n\n- **Use a hotspot**: This would provide internet sharing, not a connection between the phone and headset.\n- **Use NFC**: Near Field Communication is for close-range data transfers, not for connecting a headset.\n- **Enable synchronization**: Synchronization is related to syncing data between devices, not establishing a connection for media playback."
  },
  {
    "question": "A user needs a portable, low-cost storage solution that is small enough to carry in a pocket and has the largest capacity possible. Which of the following is the best solution for the user?",
    "options": [
      "Flash drive",
      "DVD-R",
      "M.2",
      "Memory card"
    ],
    "correct_answer": 1,
    "description": "The correct answer is **Flash drive**. A flash drive is portable, inexpensive, and has large capacity options, making it ideal for carrying in a pocket.\n\n- **DVD-R**: Limited storage capacity and not easily portable compared to a flash drive.\n- **M.2**: Used for internal storage, not portable in the same way as a flash drive.\n- **Memory card**: Typically smaller in capacity compared to flash drives, though still portable."
  },
  {
    "question": "Which of the following scenarios best illustrate a need for VDI? (Choose two.)",
    "options": [
      "An IT engineer who is designing and showcasing organization user experiences for multiple clients",
      "A company that needs to store 10PB worth of data",
      "A manufacturing plant that has high turnover",
      "A bank that has security concerns regarding employee activity",
      "A payment processor that is planning on implementing virtual currency",
      "An application developer who needs to configure network settings for an application"
    ],
    "correct_answers": [3, 4],
    "description": "The correct answers are **A manufacturing plant that has high turnover** and **A bank that has security concerns regarding employee activity**. VDI (Virtual Desktop Infrastructure) allows companies to create a virtualized desktop environment that can be easily scaled or monitored.\n\n- **IT engineer designing user experiences**: May benefit from virtual environments, but VDI is more about user access.\n- **Company storing 10PB of data**: Storage needs are not necessarily a reason to implement VDI.\n- **Payment processor implementing virtual currency**: This use case is unrelated to VDI needs.\n- **Application developer configuring network settings**: VDI is typically more user access-centric than this."
  },
  {
    "question": "Which of the following network types is used for pairing a Bluetooth device to a smartphone?",
    "options": [
      "PAN",
      "WAN",
      "LAN",
      "MAN"
    ],
    "correct_answer": 1,
    "description": "The correct answer is **PAN**. Personal Area Network (PAN) is the type of network used for short-range wireless connections such as Bluetooth between devices like smartphones and headsets.\n\n- **WAN**: Wide Area Network is for large-scale networks, like the internet.\n- **LAN**: Local Area Network is typically used for wired or wireless networks in a small area.\n- **MAN**: Metropolitan Area Network is for city-wide network connections."
  },
  {
    "question": "A company wants to save money by leveraging the cloud while still being able to customize the infrastructure. Which of the following cloud models would best address the company's needs?",
    "options": [
      "Private",
      "Public",
      "Hybrid",
      "Community"
    ],
    "correct_answer": 3,
    "description": "The correct answer is **Hybrid**. A hybrid cloud model allows a company to combine the cost savings of public cloud services with the ability to customize certain parts of its infrastructure using a private cloud.\n\n- **Private**: Allows full customization but is more costly.\n- **Public**: Cheaper but with limited customization.\n- **Community**: Shares infrastructure with other organizations, but customization might be limited."
  },
  {
    "question": "Which of the following is the best way to protect the data of a virtual machine in the event of hardware failure?",
    "options": [
      "Redundant hardware",
      "UPS",
      "Cloud-based backup",
      "RAID"
    ],
    "correct_answer": 3,
    "description": "The correct answer is **Cloud-based backup**. Backing up the virtual machine to the cloud ensures that data can be recovered in the event of hardware failure.\n\n- **Redundant hardware**: While important for avoiding downtime, it doesn't directly protect data.\n- **UPS**: Uninterruptible power supply prevents sudden shutdowns, but doesn’t directly protect data.\n- **RAID**: RAID provides redundancy for drives, but not a comprehensive backup solution."
  },
  {
    "question": "A customer reports that a printer is only printing misaligned images. Which of the following should the technician do to correct the issue?",
    "options": [
      "Clean the printheads.",
      "Perform a calibration.",
      "Replace the ink cartridge.",
      "Scan the document."
    ],
    "correct_answer": 2,
    "description": "The correct answer is **Perform a calibration**. Calibrating the printer will help to align the print heads and resolve any misalignment issues.\n\n- **Clean the printheads**: This is useful for print quality but not for alignment.\n- **Replace the ink cartridge**: This could help with print quality, but it won't resolve alignment.\n- **Scan the document**: Not relevant to the printer’s misalignment issue."
  },
  {
    "question": "A user's laptop will not turn on for a meeting in a conference room. However, the laptop turns on correctly when connected to the external monitor, mouse, and keyboard at the user's desk. Which of the following should a technician do to ensure that the laptop functions everywhere in the office?",
    "options": [
      "Reinstall the laptop's operating system.",
      "Enable a remote desktop account.",
      "Issue a peripheral set for use in the conference room.",
      "Replace the laptop's battery."
    ],
    "correct_answer": 4,
    "description": "The correct answer is **Replace the laptop's battery**. The laptop works when connected to external power sources, indicating a battery issue. Replacing the battery should resolve the issue so the laptop can function anywhere.\n\n- **Reinstall the laptop's operating system**: Not necessary, as the issue seems related to power, not software.\n- **Enable a remote desktop account**: This wouldn't resolve a power issue.\n- **Issue a peripheral set for use in the conference room**: This would not address the laptop's power issue."
  },
  {
    "question": "A company's cloud server has recently become unresponsive due to overwhelming e-commerce traffic. Which of the following cloud technologies could be dynamically assigned to mitigate this issue?",
    "options": [
      "High availability",
      "Shared resources",
      "Metered utilization",
      "Rapid elasticity"
    ],
    "correct_answer": 4,
    "description": "The correct answer is **Rapid elasticity**. Rapid elasticity allows for resources to be dynamically allocated and scaled based on the current demand, making it ideal for handling sudden traffic spikes.\n\n- **High availability**: Refers to ensuring services remain up, but it doesn’t dynamically scale resources.\n- **Shared resources**: Involves resource pooling but doesn’t necessarily help with dynamic scaling.\n- **Metered utilization**: Tracks usage for billing purposes but doesn’t affect performance."
  },
  {
    "question": "A PC’s boot drive is showing signs of imminent failure, and a technician needs to recover the data. Which of the following should the technician do first?",
    "options": [
      "Clone the drive to another one.",
      "Access the Device Manager.",
      "Download the drive manufacturer's diagnostic tool.",
      "Uninstall the drive in the Device Manager.",
      "Replace the drive with a new one."
    ],
    "correct_answer": 1,
    "description": "The correct answer is **Clone the drive to another one**. Cloning the drive allows the technician to create an exact copy of the failing drive before the data is lost.\n\n- **Access the Device Manager**: Won’t help with data recovery.\n- **Download the drive manufacturer's diagnostic tool**: May help identify the problem but doesn't protect the data.\n- **Uninstall the drive in the Device Manager**: Not helpful for data recovery.\n- **Replace the drive with a new one**: Replacing the drive without first cloning the data could lead to data loss."
  },

  #441-460
  
  {
    "question": "A user attempts to connect a laptop to a projector but receives the following message from the projector: Out of Range. Which of the following needs to be addressed first?",
    "options": [
      "Change the resolution settings.",
      "Check the video cable and replace it if necessary.",
      "Set the computer's display settings to extend/duplicate.",
      "Verify that the laptop video card driver is the most up-to-date version."
    ],
    "correct_answer": 1,
    "description": "The correct answer is **Change the resolution settings**. 'Out of Range' typically indicates that the resolution set on the laptop is higher than what the projector can support. Lowering the resolution should fix the issue."
  },
  {
    "question": "A user with a custom hosts file is having difficulty connecting to a locally hosted site on a small office network. The technician cannot ping the server hostname from the user’s computer. Which of the following should the technician ensure on the server?",
    "options": [
      "The server is configured with a static IP address.",
      "The server does not have an APIPA.",
      "The appropriate services are enabled on the server.",
      "The server's secondary NIC is functioning."
    ],
    "correct_answer": 1,
    "description": "The correct answer is **The server is configured with a static IP address**. A static IP address ensures that the server hostname in the hosts file is resolved to the correct IP. Without a static IP, the address might change, causing connection issues."
  },
  {
    "question": "A user reports that a laptop correctly connects to the internet when docked at the office but is unable to access the internet when at home. Which of the following should the technician do first?",
    "options": [
      "Contact the user's home ISP.",
      "Give the user a dock to use at home.",
      "Disable network security settings.",
      "Enable the wireless adapter."
    ],
    "correct_answer": 4,
    "description": "The correct answer is **Enable the wireless adapter**. If the laptop connects fine when docked but not at home, the issue could be that the wireless adapter is disabled when the user is away from the office docking station."
  },
  {
    "question": "A technician is configuring the settings on a multifunction printer so the device can be shared across the LAN. Which of the following should the technician do to enable the printer to be shared across the network?",
    "options": [
      "Install the correct print driver.",
      "Configure the IP settings.",
      "Enable the web services.",
      "Enable the network scanning feature."
    ],
    "correct_answer": 2,
    "description": "The correct answer is **Configure the IP settings**. To share the printer on the network, it must have the correct network IP configuration to communicate with other devices."
  },
  {
    "question": "Which of the following provides the highest level of isolation from the host operating system?",
    "options": [
      "Type II hypervisor",
      "Resource pooling",
      "Hardware-assisted virtualization",
      "Single-node clustering"
    ],
    "correct_answer": 3,
    "description": "The correct answer is **Hardware-assisted virtualization**. This provides the highest level of isolation, allowing virtual machines to run directly on the hardware with minimal interaction with the host OS."
  },
  {
    "question": "A user recently purchased a second monitor and wants to extend the Windows desktop to the new screen. Which of the following Control Panel options should a technician adjust to help the user?",
    "options": [
      "Color Management",
      "System",
      "Troubleshooting",
      "Device Manager",
      "Administrative Tools"
    ],
    "correct_answer": 2,
    "description": "The correct answer is **System**. The 'Display' section within 'System' in the Control Panel contains the settings to extend the desktop to multiple monitors."
  },
  {
    "question": "A technician needs to secure and optimize traffic on a local network by separating client workstations from web servers. The technician only has administrative permissions on the Layer 2 switch to which all of the devices are connected. Which of the following should the technician complete to accomplish this goal?",
    "options": [
      "Create a separate DHCP scope for the web servers.",
      "Implement an ACL on the switch.",
      "Place the web servers in a DMZ.",
      "Configure the web servers in a separate VLAN.",
      "Set up the web servers on a different domain."
    ],
    "correct_answer": 4,
    "description": "The correct answer is **Configure the web servers in a separate VLAN**. VLANs (Virtual Local Area Networks) can logically separate network traffic at Layer 2, optimizing and securing network traffic between client workstations and web servers."
  },
  {
    "question": "Which of the following DNS records is used to look up the IP address assigned to a domain name?",
    "options": [
      "A",
      "MX",
      "NS",
      "SPF"
    ],
    "correct_answer": 1,
    "description": "The correct answer is **A**. An 'A' record (Address record) in DNS is used to map a domain name to its corresponding IPv4 address."
  },
  {
    "question": "Which of the following is a characteristic of cloud computing that prioritizes reliability?",
    "options": [
      "Shared resources",
      "High availability",
      "Rapid elasticity",
      "Hybrid"
    ],
    "correct_answer": 2,
    "description": "The correct answer is **High availability**. High availability in cloud computing ensures that services remain accessible even if there are issues with some parts of the infrastructure."
  },
  {
    "question": "Which of the following technologies can be used to connect a home PC to a company's network?",
    "options": [
      "VLAN",
      "VM",
      "VPN",
      "VoIP"
    ],
    "correct_answer": 3,
    "description": "The correct answer is **VPN**. A Virtual Private Network (VPN) is used to securely connect a home PC to a company's network, providing access to resources as if the user were on-site."
  },
  #461-480
  
{
  "question": "A user’s laptop has been slow to respond for the past few days. The user has run a virus scan, deleted temporary files, closed unnecessary programs, and rebooted the laptop, but the issue persists. Which of the following steps should the technician take next?",
  "options": [
    "Perform a RAM upgrade.",
    "Replace the laptop's hard drive.",
    "Bench test the laptop.",
    "Run a firmware update."
  ],
  "correct_answer": 3,
  "description": "The correct answer is **Bench test the laptop**. Since the user has already attempted basic troubleshooting steps, the next action would be to perform a bench test to identify if there are any underlying hardware issues."
},
  {
    "question": "A technician is unable to connect to a network device via SSH. Which of the following cables should the technician use as an alternative connection method with a laptop?",
    "options": [
      "Serial",
      "HDMI",
      "Parallel",
      "Lightning"
    ],
    "correct_answer": 1,
    "description": "The correct answer is **Serial**. A serial cable is often used for direct access to network devices, especially when SSH or other network methods are unavailable."
  },
  {
    "question": "A network technician needs to provide better wireless connectivity throughout a SOHO location. Which of the following should the technician deploy to best improve connectivity?",
    "options": [
      "Access point",
      "Managed switch",
      "PoE hub",
      "Wi-Fi router"
    ],
    "correct_answer": 1,
    "description": "The correct answer is **Access point**. Deploying an additional access point can help extend and improve wireless connectivity within a SOHO network."
  },
  {
    "question": "A technician is setting up a projector for a videoconferencing system. The laptop that the technician is using is set to the correct resolution. The projector is receiving a signal, but the image is distorted. Which of the following most likely explains the issue?",
    "options": [
      "The projector's aspect ratio is set incorrectly.",
      "The laptop's video card has failed.",
      "The projector's bulb is burned out.",
      "The display brightness needs to be adjusted."
    ],
    "correct_answer": 1,
    "description": "The correct answer is **The projector's aspect ratio is set incorrectly**. A distorted image is often caused by a mismatch between the aspect ratio of the projector and the signal being sent from the laptop."
  },
  {
    "question": "A technician is troubleshooting a workgroup printer that has stopped printing after several days of heavy use. The technician runs the diagnostic tool in the printer's administrator menu. Which of the following issues is the technician most likely to encounter?",
    "options": [
      "Corrupt job in print spooler",
      "Insufficient space in the printer",
      "Network connectivity issues",
      "Improperly installed drivers"
    ],
    "correct_answer": 1,
    "description": "The correct answer is **Corrupt job in print spooler**. After heavy use, a printer may stop working due to a corrupt print job stuck in the print spooler, which prevents new jobs from being processed."
  },
  {
    "question": "A customer recently installed a new graphics card, but the card's HDMI port is not getting a signal when connected to the monitor. When the monitor is connected to the original HDMI port, located next to the USB ports, everything works as expected. Which of the following should the technician do next?",
    "options": [
      "Change the input source selection on the monitor.",
      "Check to see whether the UEFI setting for PCIe graphics is enabled.",
      "Install a higher wattage power supply.",
      "Test the new graphics card with an HDMI to DVI adapter."
    ],
    "correct_answer": 2,
    "description": "The correct answer is **Check to see whether the UEFI setting for PCIe graphics is enabled**. If the new graphics card isn’t being recognized, it’s possible that the UEFI/BIOS settings have not been configured to use PCIe graphics as the primary display."
  },
  {
    "question": "An administrator is replacing a cable that uses a DB9 connector. Which of the following cables is the administrator replacing?",
    "options": [
      "Parallel",
      "Serial",
      "Optical",
      "USB"
    ],
    "correct_answer": 2,
    "description": "The correct answer is **Serial**. DB9 connectors are commonly used for serial cables, which are typically used for direct connections to devices like switches or routers."
  },
  {
    "question": "A technician is troubleshooting a user's laptop that randomly turns off. The technician disassembles the laptop and notices that various pieces of small sticker paper within the device have changed color from red to blue. Which of the following is the most likely cause of the laptop's issues?",
    "options": [
      "Broken screen",
      "Liquid damage",
      "Swollen battery",
      "Overheating"
    ],
    "correct_answer": 2,
    "description": "The correct answer is **Liquid damage**. The color-changing stickers inside the device are liquid damage indicators, which change color when exposed to moisture, suggesting that liquid damage may be causing the laptop's random shutdowns."
  },
  {
    "question": "A technician is running a 279ft (85m) network cable between buildings that will share conduit with a large power cable. Which of the following is the most appropriate cable for the technician to use for this project?",
    "options": [
      "Fiber",
      "Coaxial",
      "Cat 5e",
      "Cat 6"
    ],
    "correct_answer": 1,
    "description": "The correct answer is **Fiber**. Fiber optic cables are immune to electromagnetic interference (EMI), making them ideal for running close to power cables in shared conduits."
  },
#481-510

{
  "question": "A technician attempts to join a Windows client to a domain but receives the following error: An attempt to resolve the hostname has failed. The technician generates the display shown below utilizing ipconfig /all. Physical Address: 80-3F-6C-33-32-C5 IPv4 Address: 192.168.12.144 Subnet Mask: 255.255.255.0 Default Gateway: 192.168.12.254 DNS Server: 127.0.0.1 Which of the following is the most likely reason for the error?",
  "options": [
    "DNS",
    "Physical address",
    "Subnet mask",
    "IPv4 address",
    "Default gateway"
  ],
  "correct_answer": 1,
  "description": "The most likely reason for the error is DNS. The DNS Server is set to 127.0.0.1, which is a loopback address. This indicates that the client is trying to resolve DNS queries locally, preventing it from accessing external DNS servers for domain resolution."
},


  {
    "question": "A user reports a workstation is having the following issues: • OS performance is slow • The workstation turns off randomly from time to time • The fans are running loudly. Which of the following is most likely the cause?",
    "options": [
      "The system is infected with malware.",
      "The CPU is overheating.",
      "The hard drive is failing.",
      "The power supply is insufficient."
    ],
    "correct_answer": 2,
    "description": "The correct answer is **The CPU is overheating**. The loud fans and random shutdowns suggest an overheating issue, which can cause slow performance and forced shutdowns to protect hardware."
  },
  {
    "question": "A user recently connected multiple monitors to a dock and would like to use the monitors as an extended laptop display. Which of the following connection methods would be best to use to connect the dock to the laptop?",
    "options": [
      "NFC",
      "Lightning",
      "Bluetooth",
      "USB-C"
    ],
    "correct_answer": 4,
    "description": "The correct answer is **USB-C**. USB-C offers fast data transfer and power delivery, making it ideal for connecting multiple monitors through a dock."
  },
  {
    "question": "A technician is configuring the BIOS of a new workstation. The machine will be used for data analytics, and the technician would like to maximize the performance of the CPU. Which of the following BIOS settings should the technician verify?",
    "options": [
      "Virtualization technology",
      "GPU settings",
      "BIOS update",
      "Hyperthreading"
    ],
    "correct_answer": 4,
    "description": "The correct answer is **Hyperthreading**. Enabling hyperthreading can maximize CPU performance by allowing multiple threads to be processed at once, which is essential for data analytics workloads."
  },
  {
    "question": "A technician is troubleshooting a wireless network issue. The users are all connected to the network, but the throughput is slow, and connections often drop. Which of the following should the technician check first?",
    "options": [
      "Encryption cipher",
      "Channel interference",
      "Number of connected devices",
      "Antenna type"
    ],
    "correct_answer": 2,
    "description": "The correct answer is **Channel interference**. Wireless channels may be overcrowded, causing slow performance and dropped connections, which can be addressed by selecting a less congested channel."
  },
  {
    "question": "A user reports having an issue charging a laptop from home. When the user connects the USB-C adapter that is attached to the office workstation to the laptop charging port, the laptop charges correctly. When the user connects the home USB-C adapter to the laptop charging port, the laptop does not charge. Which of the following should the technician do to ensure the user can work at home and in the office?",
    "options": [
      "Provide a UPS for the user's home office.",
      "Give the user an OEM power supply for home use.",
      "Replace the user's laptop with a desktop, and enable remote log-in.",
      "Instruct the user to use a USB-C hub when working at home."
    ],
    "correct_answer": 2,
    "description": "The correct answer is **Give the user an OEM power supply for home use**. Using a proper, compatible power adapter from the manufacturer ensures reliable charging."
  },
  {
    "question": "A technician is configuring a desktop RAID to allow for the best I/O performance and the most storage capacity possible. Which of the following RAID types should the technician use?",
    "options": [
      "RAID 0",
      "RAID 5",
      "RAID 6",
      "RAID 10"
    ],
    "correct_answer": 1,
    "description": "The correct answer is **RAID 0**. RAID 0 offers the highest performance and storage capacity by striping data across multiple drives, but it does not provide redundancy."
  },
  {
    "question": "Which of the following is used to define a range of IP addresses available to assign using DHCP?",
    "options": [
      "Scope",
      "Address",
      "Lease",
      "Reservation"
    ],
    "correct_answer": 1,
    "description": "The correct answer is **Scope**. A DHCP scope defines the range of IP addresses that can be assigned to clients on the network."
  },
  {
    "question": "Which of the following should the label on a network jack faceplate refer to?",
    "options": [
      "MAC address",
      "Patch panel port",
      "Switch port in use",
      "VLAN identification"
    ],
    "correct_answer": 2,
    "description": "The correct answer is **Patch panel port**. Faceplate labels typically refer to the patch panel port, so the connection can be easily traced back to the panel for maintenance."
  },
  {
    "question": "Which of the following protocols is the most appropriate to use for inventory tracking in a small warehouse?",
    "options": [
      "Near-field communication",
      "Radio-frequency identification",
      "Bluetooth",
      "802.11"
    ],
    "correct_answer": 2,
    "description": "The correct answer is **Radio-frequency identification (RFID)**. RFID is commonly used for inventory tracking in warehouses due to its ability to track items using radio waves."
  },
  {
    "question": "An administrator wants to replace a fiber-optic cable. Which of the following should the administrator most likely use?",
    "options": [
      "LC",
      "Bayonet Neill Concelman (BNC)",
      "RJ45",
      "DB9"
    ],
    "correct_answer": 1,
    "description": "The correct answer is **LC**. LC (Lucent Connector) is a commonly used connector for fiber-optic cables."
  },

#510-539
  {
    "question": "A user's laptop is having performance issues when the user downloads large files over the internet. Other users with newer laptops are not experiencing any performance issues. Which of the following components should the technician replace?",
    "options": [
      "Hard drive",
      "Wi-Fi card",
      "RAM",
      "CPU"
    ],
    "correct_answer": 2,
    "description": "The correct answer is **Wi-Fi card**. Since the issue arises when downloading large files over the internet and newer laptops are unaffected, the most likely culprit is the Wi-Fi card."
  },
  {
    "question": "After a new network printer is installed and added to the print server, users are unable to install the printer. However, the technician is able to install the printer when logged in to a user's computer as an administrator. Which of the following is the best option to allow all users to print to the new printer?",
    "options": [
      "Install all applicable print drivers on the print server.",
      "Map the users to a print share for driver installation.",
      "Give all users temporary administrator rights to install the new printer.",
      "Remotely log in to all users’ computers and install the printer."
    ],
    "correct_answer": 1,
    "description": "The correct answer is **Install all applicable print drivers on the print server**. Installing the necessary drivers on the print server will allow all users to connect to the printer without needing administrator privileges."
  },
  {
    "question": "A frequently used projector continuously shows a message to clean the air filters. The technician checks the filters, and they are clean. Which of the following preconfigured settings is causing the projector to show the message frequently?",
    "options": [
      "Image calibration",
      "Hours of use",
      "Temperature",
      "Image source"
    ],
    "correct_answer": 2,
    "description": "The correct answer is **Hours of use**. Many projectors are set to display a cleaning message after a certain number of hours of use, regardless of the actual condition of the filters."
  },
  {
    "question": "A technician receives a phone call from a traveling sales representative indicating that the maps application on a phone is not working. The representative runs a speed test on the phone and gets ~10Mbps in both directions. Which of the following settings should the technician check first to troubleshoot the issue?",
    "options": [
      "Airplane mode",
      "PRL",
      "GPS",
      "LTE"
    ],
    "correct_answer": 3,
    "description": "The correct answer is **GPS**. Since the issue is related to a maps application, the technician should check if GPS is enabled on the phone."
  },
  {
    "question": "A user reports that a software application functioned as expected the previous day, but this morning, the user is unable to launch the application. Which of the following describes what the technician should do next?",
    "options": [
      "Research the symptoms.",
      "Identify any changes the user has made.",
      "Determine which steps need to be performed.",
      "Check the vendor’s website for guidance."
    ],
    "correct_answer": 2,
    "description": "The correct answer is **Identify any changes the user has made**. The most logical first step is to determine if any changes were made that could affect the application’s performance."
  },
  {
    "question": "Which of the following describes the difference between a DNS server and a DHCP server?",
    "options": [
      "DNS is used for address translation, while DHCP is used for IP address assignment.",
      "DNS is used for routing, while DHCP is used for name resolution.",
      "DNS only assigns private IP addresses, while DHCP only assigns public IP addresses.",
      "DNS is used to route traffic between networks, while DHCP is used to allocate subnets."
    ],
    "correct_answer": 1,
    "description": "The correct answer is **DNS is used for address translation, while DHCP is used for IP address assignment**. DNS translates domain names to IP addresses, while DHCP assigns IP addresses to devices."
  },
  {
    "question": "Which of the following is the maximum distance Cat 5, Cat 5e, Cat 6, and Cat 6a cables can be run?",
    "options": [
      "295ft (90m)",
      "328ft (100m)",
      "361ft (110m)",
      "394ft (120m)"
    ],
    "correct_answer": 2,
    "description": "The correct answer is **328ft (100m)**. The maximum distance for all Cat 5, Cat 5e, Cat 6, and Cat 6a cables is 100 meters, or approximately 328 feet."
  },
  {
    "question": "Which of the following differentiates PAN from LAN?",
    "options": [
      "PAN creates a wireless connection between smart devices.",
      "PAN creates a highly secure environment.",
      "PAN creates a faster connection.",
      "PAN needs regular maintenance to function properly."
    ],
    "correct_answer": 1,
    "description": "The correct answer is **PAN creates a wireless connection between smart devices**. A Personal Area Network (PAN) typically involves short-range wireless connections between devices such as smartphones and tablets."
  },
  {
    "question": "A technician is asked to set up a new laptop for a coworker. Which of the following storage devices and interfaces will provide the best performance? (Choose two.)",
    "options": [
      "15,000rpm HDD",
      "M.2 SSD",
      "10,000rpm HDD",
      "NVMe interface",
      "SATA interface",
      "mSATA interface"
    ],
    "correct_answer": [2, 4],
    "description": "The correct answers are **M.2 SSD** and **NVMe interface**. M.2 SSDs with an NVMe interface offer the fastest storage performance, ideal for a high-performing laptop."
  },
  {
    "question": "A user brings a laptop to work every morning, correctly seats it in the docking station, and then opens the laptop to begin work with no issues. After the user left the laptop at home during a two-week vacation, the laptop is no longer working. Upon returning to the office, the user reports that the keyboard and display are no longer working. Which of the following should the technician ask the user to do first?",
    "options": [
      "Ensure the docking station is plugged in.",
      "Press and release the laptop power button.",
      "Plug the laptop in and let it charge overnight.",
      "Connect the laptop directly to the network."
    ],
    "correct_answer": 1,
    "description": "The correct answer is **Ensure the docking station is plugged in**. The technician should first confirm that the docking station has power, as it might have been disconnected during the user's absence."
  },

  #540-550

 
 {
  "question": "A company issued smartphones to users who work from home. The devices are enrolled and configured within the company's MDM, and hardening profiles were deployed to each device for greater security. Which of the following services best enhances security for remote users accessing company resources? (Choose two.)",
  "options": [
    "Two-factor authentication",
    "Managed corporate applications",
    "Cloud data synchronization",
    "Automated device setup",
    "GPS location tracking",
    "PIN code enforcement"
  ],
  "correct_answers": [1, 2],
  "description": "The correct answers are Two-factor authentication and Managed corporate applications. Two-factor authentication adds an extra layer of security, while managed corporate applications ensure that only secure, company-approved apps are used."
},
    {
      "question": "Which of the following cloud-computing concepts describes an environment in which various internal VM servers for a specific organization are stored within both a physical server and a cloud environment?",
      "options": [
        "Private",
        "Hybrid",
        "Community",
        "Public"
      ],
      "correct_answer": 2,
      "description": "The correct answer is Hybrid. A hybrid cloud combines both on-premise (physical) servers and cloud environments to store and run VMs."
    },
    {
      "question": "A department is upgrading its printers and wants to save money on consumables. Which of the following printer features would allow the department to cut costs?",
      "options": [
        "Collate",
        "Duplex",
        "Secure print",
        "Scanner"
      ],
      "correct_answer": 2,
      "description": "The correct answer is Duplex. Duplex printing allows for printing on both sides of a sheet, cutting paper consumption in half."
    },
    {
      "question": "When a user tries to print a document on a laser printer, vertical lines appear on the printout. Which of the following should the technician replace?",
      "options": [
        "Mirror",
        "Fuser",
        "Drum",
        "Toner"
      ],
      "correct_answer": 3,
      "description": "The correct answer is Drum. Vertical lines on a laser printout typically indicate an issue with the drum unit."
    },
    {
      "question": "A user's computer is experiencing poor performance. A technician runs a diagnostic tool on the hard drive, and the results show a significant increase in the number of reallocated sectors. Which of the following steps should the technician take next?",
      "options": [
        "Run sfc /scannow on the hard drive.",
        "Replace the hard drive.",
        "Run chkdsk /f on the hard drive.",
        "Reformat the hard drive."
      ],
      "correct_answer": 2,
      "description": "The correct answer is Replace the hard drive. A significant increase in reallocated sectors indicates a failing hard drive."
    },
    {
      "question": "A user reports that a projector was previously working, but the screen now displays the following error message: No Source Found. Which of the following actions should the technician take first? (Choose two.)",
      "options": [
        "Check the projector bulb and replace it with a new one.",
        "Verify the projector settings and make sure the correct input is selected.",
        "Replace the video cable and check the laptop settings.",
        "Set the laptop display settings to extend or duplicate.",
        "Verify the projector is turned on.",
        "Check the projector settings and the laptop for the correct resolution."
      ],
      "correct_answers": [2, 5],
      "description": "The correct answers are Verify the projector settings and make sure the correct input is selected and Verify the projector is turned on. These are the first steps to ensure the basic functionality of the projector."
    },
    {
      "question": "A user wants to create a VM on a computer. Which of the following should the user check first?",
      "options": [
        "Installed RAM amount",
        "Hard drive space",
        "BIOS CPU settings",
        "Graphics card compatibility"
      ],
      "correct_answer": 3,
      "description": "The correct answer is BIOS CPU settings. The user should verify that virtualization technology is enabled in the BIOS CPU settings before attempting to create a VM."
    },
    {
      "question": "A large office is eliminating all personal printers for VIP staff members and replacing these devices with one enterprise MFR Human resources staff members are concerned about printing confidential documents on the new device. Which of the following best addresses this concern?",
      "options": [
        "Central printer server",
        "Secure print",
        "Audit logs",
        "Wi-Fi direct printing"
      ],
      "correct_answer": 2,
      "description": "The correct answer is Secure print. This feature ensures that sensitive documents are only printed when the user is physically present at the printer, protecting confidential information."
    },
    {
  "question": "A user's smartphone battery capacity has started going from full to empty within an hour. The user has not recently installed any new applications on the smartphone. An IT technician notices that the smartphone has very high network utilization and thinks this issue might be related to the battery drain. Which of the following troubleshooting steps should the technician attempt next?",
  "options": [
    "Disable Bluetooth.",
    "Connect the smartphone to a Wi-Fi network.",
    "Restart the smartphone.",
    "Update the mobile OS."
  ],
  "correct_answer": 3,
  "description": "The correct answer is Restart the smartphone. Restarting can resolve temporary system issues, which could help reduce the network utilization and alleviate the battery drain problem."
},
#551-570
  {
    "question": "A technician is upgrading a user's laptop from an HDD to an SSD. The user's laptop only has a single bay for a hard drive. Which of the following characteristics of the SSD is the most important in this scenario?",
    "options": [
      "Partition type",
      "Storage size",
      "Form factor",
      "Transfer speed"
    ],
    "correct_answers": [3],
    "description": "The correct answer is Form factor. Since the laptop only has one bay, the form factor of the SSD must match the bay size to ensure compatibility."
  },
  {
    "question": "A user wants to overclock a GPU but is concerned about potential overheating. Which of the following would best address the user's concern?",
    "options": [
      "Thicker thermal pads",
      "Liquid cooling",
      "Larger heat sink",
      "Fan upgrade"
    ],
    "correct_answers": [2],
    "description": "The correct answer is Liquid cooling. Liquid cooling provides superior heat dissipation compared to other cooling methods, which is crucial for managing the increased heat from overclocking."
  },
  {
    "question": "A company is deploying tablets to all branch offices. The company needs a way to set security settings and configure which applications can be installed on the tablets. Which of the following is the best way for the company to remotely perform these tasks?",
    "options": [
      "SSH",
      "RDP",
      "VPN",
      "MDM"
    ],
    "correct_answers": [4],
    "description": "The correct answer is MDM (Mobile Device Management). MDM allows for remote configuration and management of security settings and applications on mobile devices."
  },
  {
    "question": "Which of the following cloud models provides the most control?",
    "options": [
      "IaaS",
      "SaaS",
      "DaaS",
      "PaaS"
    ],
    "correct_answers": [1],
    "description": "The correct answer is IaaS (Infrastructure as a Service). IaaS provides the most control over the underlying infrastructure, including operating systems, storage, and networks."
  },
  {
    "question": "After a heavily used color laser printer was serviced to remove excessive dust, the image quality decreased. Which of the following should a technician most likely check on the printer?",
    "options": [
      "Toner",
      "Calibration",
      "Fuser",
      "Drum"
    ],
    "correct_answers": [4],
    "description": "The correct answer is Drum. The drum can be affected by dust and may need to be cleaned or replaced to restore image quality."
  },
  {
    "question": "Which of the following scenarios best illustrate a need for VDI? (Choose two.)",
    "options": [
      "An employee needs the ability to work remotely on a non-company-provided computer",
      "A company that needs to store 10PB worth of data",
      "An employee has latency-sensitive workflow requirements",
      "A bank that has security concerns regarding employee activity",
      "A payment processor that is planning on implementing virtual currency",
      "An application developer who needs to configure network settings for an application"
    ],
    "correct_answers": [1, 4],
    "description": "The correct answers are An employee needs the ability to work remotely on a non-company-provided computer and A bank that has security concerns regarding employee activity. VDI (Virtual Desktop Infrastructure) provides secure, remote access and can address security concerns by centralizing data."
  },
  {
    "question": "A user purchased a retail router and would like to set up a private network. Which of the following network address ranges should the user configure?",
    "options": [
      "170.50.0.0 to 170.50.255.255",
      "172.16.0.0 to 172.31.255.255",
      "224.0.0.0 to 224.255.255.255",
      "239.0.0.0 to 239.255.255.255"
    ],
    "correct_answers": [2],
    "description": "The correct answer is 172.16.0.0 to 172.31.255.255. This range is part of the private IP address ranges used for internal networks."
  },
  {
    "question": "A user is reporting that a computer has been very slow in recent days. The technician looks into the problem and finds pop-ups are randomly appearing on the screen. Which of the following is the next step the technician must take?",
    "options": [
      "Establish a knowledge base.",
      "Establish a theory of probable cause.",
      "Establish a new theory and consider escalating.",
      "Establish a plan of action."
    ],
    "correct_answers": [2],
    "description": "The correct answer is Establish a theory of probable cause. Since the symptoms suggest potential malware or other issues, formulating a theory helps in diagnosing the problem."
  },
  {
    "question": "A company wants to add virtual servers to handle unusually high web traffic usage. Which of the following is the most efficient way?",
    "options": [
      "Community cloud",
      "File synchronization",
      "Rapid elasticity",
      "Cloud VDI"
    ],
    "correct_answers": [3],
    "description": "The correct answer is Rapid elasticity. Rapid elasticity allows the company to quickly scale up virtual servers to handle increased traffic."
  },
  {
    "question": "A printer unexpectedly runs out of consumables in the middle of a print job. The printer requires polylactic acid (PLA) consumables. Which of the following printers is being used?",
    "options": [
      "Impact printer",
      "3-D printer",
      "Laser printer",
      "Inkjet printer"
    ],
    "correct_answers": [2],
    "description": "The correct answer is 3-D printer. PLA is a type of filament used in 3-D printers."
  },

##571-590

  {
    "question": "A user plugs in a laptop to the corporate network and the laptop is automatically assigned an IP address. Which of the following server types was used to assign the IP address?",
    "options": [
      "DNS",
      "AAA",
      "DHCP",
      "Web"
    ],
    "correct_answers": [3],
    "description": "The correct answer is DHCP (Dynamic Host Configuration Protocol). DHCP servers automatically assign IP addresses to devices on the network."
  },
  {
    "question": "Which of the following cloud service models is most likely to provide application patching?",
    "options": [
      "PaaS",
      "DaaS",
      "IaaS",
      "SaaS"
    ],
    "correct_answers": [4],
    "description": "The correct answer is SaaS (Software as a Service). SaaS providers handle application updates and patching."
  },
  {
    "question": "A user reports being unable to access the network. A help desk technician notices an APIPA on the user's workstation. Which of the following services should the technician investigate first?",
    "options": [
      "RADIUS",
      "DHCP",
      "AAA",
      "DNS"
    ],
    "correct_answers": [2],
    "description": "The correct answer is DHCP (Dynamic Host Configuration Protocol). APIPA (Automatic Private IP Addressing) indicates that the DHCP server is not assigning an IP address."
  },
  {
    "question": "A user states that the touch pad cursor shows a trail when moved. The issue started after a coworker used the machine. Which of the following setting areas should be used to fix this issue?",
    "options": [
      "Ease of Access",
      "User Settings",
      "Display",
      "Mouse"
    ],
    "correct_answers": [4],
    "description": "The correct answer is Mouse settings. The cursor trail issue can be adjusted or disabled in the mouse settings."
  },
  {
    "question": "A user reports that a new brand of paper works well in all but one printer in the office. For that printer, the paper seems to be too heavy or too thick to feed in from the printer tray. Which of the following will correct the print issues?",
    "options": [
      "Replacing the printer pickup rollers",
      "Changing the printer spooler settings",
      "Using OEM-branded paper for this printer",
      "Increasing the corona wire voltage"
    ],
    "correct_answers": [1],
    "description": "The correct answer is Replacing the printer pickup rollers. Worn-out rollers can cause issues with feeding paper, especially thicker paper."
  },
  {
    "question": "Following a security breach that revealed employee username and password information, an organization would like to implement additional security for users logging in to company devices. Which of the following would be the best solution for the organization to use?",
    "options": [
      "Biometric authentication",
      "Peer-reviewed log-ins",
      "Log-in scripts",
      "One-time tokens"
    ],
    "correct_answers": [1],
    "description": "The correct answer is Biometric authentication. Biometric methods provide an additional layer of security beyond just usernames and passwords."
  },
  {
    "question": "A desktop technician is helping a customer choose a laptop configuration for the customer's child. The child will use the computer primarily for school-related activities, and the computer should be as inexpensive as possible. Which of the following disk configurations should the technician suggest to the customer?",
    "options": [
      "RAID",
      "eMMC",
      "HDD",
      "NVMe"
    ],
    "correct_answers": [2],
    "description": "The correct answer is eMMC (embedded MultiMediaCard). eMMC is cost-effective and suitable for basic computing tasks, making it ideal for an inexpensive laptop."
  },
  {
    "question": "Which of the following devices is designed to monitor and filter incoming and outgoing network traffic?",
    "options": [
      "Switch",
      "Access point",
      "Firewall",
      "Hub"
    ],
    "correct_answers": [3],
    "description": "The correct answer is Firewall. Firewalls are used to monitor and filter network traffic based on security rules."
  },
  {
  "question": "A user’s computer frequently freezes and requires multiple hard restarts to recover functionality. A technician confirms the hardware components have not been recently upgraded or replaced. Which of the following should the technician do first to troubleshoot the issue?",
  "options": [
    "Check the temperature of the CPU.",
    "Update the device driver.",
    "Read the event logs.",
    "Replace the power supply."
  ],
  "correct_answers": [3],
  "description": "The correct answer is Read the event logs. Event logs can provide information on what might be causing the system to freeze, such as hardware or software errors, and should be reviewed first."
},
  {
    "question": "A company needs to secure remote user data with minimal interaction. Which of the following should the company do?",
    "options": [
      "Configure self-encrypting hardware.",
      "Update firewall rule sets.",
      "Enable BIOS passwords.",
      "Remove physical ROM drives."
    ],
    "correct_answers": [1],
    "description": "The correct answer is Configure self-encrypting hardware. Self-encrypting hardware provides automatic data protection with minimal user interaction."
  },
  {
    "question": "A field technician is responding to a ticket about an animated sign with double images. One image is stationary, and the other image is live. Which of the following is the cause of the issue?",
    "options": [
      "Bad display cable",
      "Burned out bulbs",
      "Display burn-in",
      "Incorrect color settings"
    ],
    "correct_answers": [3],
    "description": "The correct answer is Display burn-in. Display burn-in can cause images to persist on the screen, leading to visual artifacts like double images."
  },
##591-610

  {
    "question": "A technician needs to ensure all data communications on all network devices are encrypted when logging in to the console. Which of the following protocols should the technician enable?",
    "options": [
      "SSH",
      "LDAP",
      "FTPS",
      "SMTP"
    ],
    "correct_answers": [1],
    "description": "The correct answer is SSH (Secure Shell). SSH encrypts data communications and is commonly used for secure remote access to network devices."
  },
  {
    "question": "A management team is concerned about enterprise devices that do not have any controls in place. Which of the following should an administrator implement to address this concern?",
    "options": [
      "MDM",
      "MFA",
      "VPN",
      "SSL"
    ],
    "correct_answers": [1],
    "description": "The correct answer is MDM (Mobile Device Management). MDM provides controls for managing and securing enterprise devices."
  },
  {
    "question": "A security team wants to implement compliance controls that only permits the installation of company-approved software on user laptops. Which of the following should the IT department deploy?",
    "options": [
      "EDR",
      "VPN",
      "MDM",
      "SaaS"
    ],
    "correct_answers": [3],
    "description": "The correct answer is MDM (Mobile Device Management). MDM can enforce policies that restrict the installation of unauthorized software."
  },
  {
    "question": "An administrator is setting up a conference room for an important board of directors meeting. The chief operating officer has asked the administrator to make sure a redundant internet connection is available. The office only has one ISP, and the conference room equipment is currently configured using Ethernet. Which of the following should the administrator set up in order to ensure redundancy?",
    "options": [
      "Wireless access point",
      "Near-field communication",
      "Hotspot",
      "Bluetooth"
    ],
    "correct_answers": [3],
    "description": "The correct answer is Hotspot. A mobile hotspot can provide a backup internet connection if the primary ISP fails."
  },
  {
    "question": "A laptop is displaying vertical lines in different colors on the screen. Which of the following components should a technician replace to most likely correct this issue?",
    "options": [
      "Inverter",
      "Motherboard",
      "Low-voltage differential signaling cable",
      "Liquid crystal display"
    ],
    "correct_answers": [4],
    "description": "The correct answer is Liquid crystal display. Vertical lines on the screen are often indicative of issues with the LCD."
  },
  {
    "question": "Every time a user submits a print job, the user receives an error from the printer requesting A4 paper. No other users in the office are having printing issues. Which of the following is the best way to address the user's issue?",
    "options": [
      "Reinstall the printer driver on the user's computer.",
      "Print to a different printer in the office.",
      "Set the printer defaults in the Control Panel to print to letter-sized paper.",
      "Have the user check the page size on every print job."
    ],
    "correct_answers": [3],
    "description": "The correct answer is Set the printer defaults in the Control Panel to print to letter-sized paper. Adjusting the default paper size can resolve the issue for the user."
  },
  {
    "question": "A technician needs to assign an IP address to a Windows PC, but a network connection is unavailable. Which of the following tools would be best for the technician to use?",
    "options": [
      "DHCP",
      "TFTP",
      "APIPA",
      "DNS"
    ],
    "correct_answers": [3],
    "description": "The correct answer is APIPA (Automatic Private IP Addressing). APIPA allows a computer to assign itself an IP address if a DHCP server is unavailable."
  },
  {
    "question": "A technician needs to configure a multifunction printer that will be used to scan highly confidential data, which must be securely distributed to a select group of executives. Which of the following options is the most secure way to accomplish this task?",
    "options": [
      "Set up the device to email the documents to a group address.",
      "Make copies of the documents and have an office administrator manually distribute them.",
      "Implement badge access on the printer.",
      "Configure scanning to an SMB share with executive access."
    ],
    "correct_answers": [4],
    "description": "The correct answer is Configure scanning to an SMB share with executive access. This method ensures that scanned documents are securely stored and accessible only to authorized personnel."
  },
{
  "question": "Which of the following combinations of specifications and frequencies delivers the greatest speed and compatibility for IoT devices?",
  "options": [
    "A and 5GHz",
    "B and 2.4GHz",
    "G and 5GHz",
    "N and 2.4GHz"
  ],
  "correct_answers": [4],
  "description": "The correct answer is N and 2.4GHz. The 802.11n specification on the 2.4GHz band offers a good balance of speed and compatibility for IoT devices."
},
  {
    "question": "A software developer used client-side virtualization on a developer PC to configure a web application. Although the application is working locally on the software developer's PC, other users on the LAN are not able to access the application. Which of the following would allow other users to access the application?",
    "options": [
      "Bridge networking",
      "Application virtualization",
      "Virtual desktop",
      "Site-to-site VPN"
    ],
    "correct_answers": [1],
    "description": "The correct answer is Bridge networking. Bridge networking allows a virtual machine to appear as a separate entity on the network, enabling LAN access."
  },
  {
    "question": "A VM was set up to deny access to the host computer and any network resources. Which of the following describes this scenario?",
    "options": [
      "Sandbox",
      "Cross-platform virtualization",
      "Legacy application",
      "Hypervisor"
    ],
    "correct_answers": [1],
    "description": "The correct answer is Sandbox. A sandbox environment isolates the VM from the host and other network resources for security."
  },
  {
    "question": "A user is experiencing an issue with a network printer. The technician tests the printer and notices shadows on some of the attempted test prints, with others having a line down the page and faded text. Which of the following should the technician replace to resolve the printer issue?",
    "options": [
      "Printhead",
      "Fuser assembly",
      "Pickup rollers",
      "Carriage belt"
    ],
    "correct_answers": [1],
    "description": "The correct answer is Printhead. Shadows, lines, and faded text are often caused by a failing printhead."
  },
  {
    "question": "A SOHO user's network printer has been without power for the last few days. After turning the printer back on, the user cannot connect to it. Which of the following is the most probable cause?",
    "options": [
      "The printer has a static IP address.",
      "The printer has a dynamic IP address.",
      "The printer has an APIPA.",
      "The printer has a public IP address."
    ],
    "correct_answers": [3],
    "description": "The correct answer is The printer has an APIPA. If the printer was turned off and not assigned a new IP address, it might have reverted to an Automatic Private IP Addressing address."
  },

{
  "question": "A technician is reviewing the following network settings for a workstation that is having trouble accessing the internet:\n\nIPv4 address . . . . . . . : 192.168.10.5\nNetmask . . . . . . . . . : 255.255.255.0\nGateway . . . . . . . . . : 192.168.1.1\n\nWhich of the following is causing the issue?",
  "options": [
    "Networking was not configured using DHCP.",
    "IPv6 should be used instead of IPv4.",
    "The netmask is wrong.",
    "The workstation has the incorrect gateway."
  ],
  "correct_answers": [4],
  "description": "The correct answer is The workstation has the incorrect gateway. The IP address and netmask suggest that the workstation is on the 192.168.10.0 network, while the gateway is set to 192.168.1.1, which is not on the same network."
},



#610-625

  {
    "question": "Which of the following best describes the concept of a DHCP lease?",
    "options": [
      "A definition of the scope of addresses to be assigned to a device on the network",
      "A reservation of an IP configuration for a device on the network",
      "A temporary assignment of an IP configuration to a device on the network",
      "A translation of network names to IP addresses for a device on the network"
    ],
    "correct_answers": [3],
    "description": "The correct answer is A temporary assignment of an IP configuration to a device on the network. A DHCP lease refers to the time period during which an IP address is assigned to a device by a DHCP server."
  },
  {
    "question": "A user arrives at the office and is unable to access the company's network on a smartphone. The user enables Wi-Fi on the smartphone, but it only shows the 5G symbol. Which of the following device settings should the user configure to fix this issue?",
    "options": [
      "Autoconnect",
      "VPN",
      "Encryption",
      "WPS"
    ],
    "correct_answers": [1],
    "description": "The correct answer is Autoconnect. The 5G symbol indicates the device is connected to a mobile network, not Wi-Fi. Enabling Wi-Fi autoconnect might automatically connect the smartphone to the office network."
  },
  {
    "question": "In which of the following cloud models is the customer not responsible for hardware and OS layers but is responsible for the data and the application?",
    "options": [
      "PaaS",
      "SaaS",
      "IaaS",
      "CaaS"
    ],
    "correct_answers": [1],
    "description": "The correct answer is SaaS (Software as a Service). In SaaS, the provider manages the infrastructure and platform, while the customer is responsible for the data and application settings."
  },
  {
    "question": "A technician wants to upgrade a computer to a new Windows version. The Windows Upgrade Advisor states that the computer is not compatible with the new Windows version due to a lack of TPM 2.0 support. Which of the following should the technician do next?",
    "options": [
      "Enable the module in the UEFI BIOS.",
      "Install an HSM in the computer.",
      "Perform a clean install of the new Windows version.",
      "Implement BitLocker on the computer."
    ],
    "correct_answers": [1],
    "description": "The correct answer is Enable the module in the UEFI BIOS. TPM 2.0 must be enabled in the BIOS for the Windows version to be compatible."
  },
  {
    "question": "A help desk technician is tasked with moving a user's computer to a makeshift office for renovations. Upon moving the computer, the technician notices the network card will not utilize anything beyond 10Mbps half duplex. Which of the following is the most likely issue?",
    "options": [
      "The computer is connected with DSL.",
      "The computer is connected to an unmanaged switch.",
      "The computer is configured for NIC teaming.",
      "The computer is connected to a hub."
    ],
    "correct_answers": [4],
    "description": "The correct answer is The computer is connected to a hub. Hubs operate at lower speeds and only support 10Mbps half duplex."
  },
  {
    "question": "Which of the following is an email authentication method designed to detect email spoofing by attaching a digital signature to outgoing email?",
    "options": [
      "SPF",
      "DKIM",
      "DNS pointer",
      "MX records"
    ],
    "correct_answers": [2],
    "description": "The correct answer is DKIM (DomainKeys Identified Mail). DKIM attaches a digital signature to outgoing emails to verify the sender and detect spoofing."
  },
  {
    "question": "Which of the following components enables finger-based screen input for two-in-one laptops?",
    "options": [
      "Fingerprint scanner",
      "Digitizer",
      "Stylus",
      "Inverter"
    ],
    "correct_answers": [2],
    "description": "The correct answer is Digitizer. A digitizer enables touch input on a screen, including finger-based input."
  },
  {
    "question": "A human resources department uses a network shared with other departments to produce a variety of printed resources for legal retention. The human resources department only wants its members to have access to these materials. Which of the following should the technician implement?",
    "options": [
      "Security groups",
      "Audit logs",
      "Time-of-day access",
      "Print server"
    ],
    "correct_answers": [1],
    "description": "The correct answer is Security groups. Implementing security groups ensures that only authorized HR members have access to the printed resources."
  }

]
