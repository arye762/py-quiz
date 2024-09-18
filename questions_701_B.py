questions_701_B = [
#200
{
    "question": "A user is installing a new display on a desktop computer that has only a single DVI port for video input and a single HDMI port for video output. Which of the following does the technician need to complete the setup?",
    "options": [
        "Digital-to-analog converter",
        "A/V switcher",
        "DisplayPort to HDMI adapter",
        "DVI to HDMI cable"
    ],
    "correct_answer": 4,
    "description": "The correct answer is **DVI to HDMI cable**. To connect the display with an HDMI port to the desktop computer with a DVI port, a DVI to HDMI cable is needed. This cable will allow the HDMI output from the computer to be connected to the display's HDMI input.\n\n- **Digital-to-analog converter** is not needed here since both DVI and HDMI are digital interfaces.\n- **A/V switcher** is used for selecting between multiple audio/video sources and is not necessary for a direct connection.\n- **DisplayPort to HDMI adapter** is not applicable since the computer does not have a DisplayPort but rather a DVI port."
},
#201
{
    "question": "A technician is troubleshooting a classroom projector that shuts down after fifteen minutes of use. Which of the following should the technician do to resolve the issue?",
    "options": [
        "Replace the video input cable",
        "Change the bulb",
        "Clean the air filter",
        "Swap the power cord"
    ],
    "correct_answer": 3,
    "description": "The correct answer is **Clean the air filter**. Projectors often shut down due to overheating, which can be caused by a clogged or dirty air filter. Cleaning the air filter can help ensure proper ventilation and prevent the projector from shutting down prematurely.\n\n- **Replacing the video input cable** is unlikely to address the shutdown issue, which is related to overheating rather than connectivity.\n- **Changing the bulb** might be necessary if the bulb is old or failing, but the shutdown after a specific time suggests an overheating problem rather than a bulb issue.\n- **Swapping the power cord** is not likely to resolve the issue, as the power supply is typically stable unless there are specific signs of a problem."
},
#202
{
    "question": "A technician is working on a desktop PC and wants to verify its NIC is functional. Which of the following should the technician use?",
    "options": [
        "Cable tester",
        "Loopback plug",
        "Toner probe",
        "Network tap"
    ],
    "correct_answer": 2,
    "description": "The correct answer is **Loopback plug**. A loopback plug is used to test the functionality of the NIC by sending data from the NIC to itself and verifying that it can both send and receive data correctly. This helps confirm that the NIC is operational.\n\n- **Cable tester** is used to check the integrity of network cables rather than the NIC itself.\n- **Toner probe** is used for tracing and identifying cables, not for testing NIC functionality.\n- **Network tap** is used for monitoring network traffic and is not typically used to test the NIC's operational status."
},
#204
{
    "question": "A user reports that a computer will not turn on. The technician verifies the power cord and the outlet the computer is plugged into are both working properly. Which of the following is the hardware component that has MOST likely failed?",
    "options": [
        "PSU",
        "CPU",
        "RAM",
        "GPU"
    ],
    "correct_answer": 1,
    "description": "The correct answer is **PSU (Power Supply Unit)**. If the computer does not turn on and the power cord and outlet are confirmed to be working, the PSU is the most likely component to have failed. The PSU is responsible for providing power to all the components of the computer.\n\n- **CPU (Central Processing Unit)** could cause the system to fail to boot, but it is less likely to be the cause of the computer not turning on at all.\n- **RAM (Random Access Memory)** or **GPU (Graphics Processing Unit)** issues might prevent the computer from booting properly or displaying, but they would not typically prevent the system from turning on entirely."
},
#205
{
    "question": "Which of the following networking devices will MOST likely need to be installed in between the ISP and the LAN in a SOHO environment?",
    "options": [
        "Switch",
        "Firewall",
        "Cable modem",
        "Router",
        "Access point"
    ],
    "correct_answer": 4,
    "description": "The correct answer is **Router**. In a Small Office/Home Office (SOHO) environment, a router is typically installed between the ISP (Internet Service Provider) and the LAN (Local Area Network) to manage and direct traffic between the external internet and the internal network. The router provides NAT (Network Address Translation), DHCP (Dynamic Host Configuration Protocol), and often includes firewall capabilities.\n\n- **Switch** is used to connect multiple devices within a LAN but is not used to connect the LAN to the ISP.\n- **Firewall** provides security features and might be integrated into the router, but it is not typically the primary device connecting the ISP to the LAN.\n- **Cable modem** is used to convert the ISP's signal into a digital signal that the router can use but does not handle the routing function.\n- **Access point** is used to provide wireless connectivity within the LAN but does not connect directly to the ISP."
},
#206
{
    "question": "A technician is configuring a desktop computer and the hard drive must be encrypted. Which of the following will the technician need to verify is enabled to complete this configuration?",
    "options": [
        "ATX",
        "NIC",
        "TPM",
        "ARM"
    ],
    "correct_answer": 3,
    "description": "The correct answer is **TPM (Trusted Platform Module)**. TPM is a hardware-based security feature that stores encryption keys securely and is commonly required for full-disk encryption solutions such as BitLocker. Verifying that TPM is enabled ensures that the encryption can be managed securely.\n\n- **ATX** (Advanced Technology eXtended) refers to the motherboard form factor and is not related to encryption.\n- **NIC** (Network Interface Card) is used for network connectivity and is not relevant to disk encryption.\n- **ARM** (Advanced RISC Machine) is a type of processor architecture and does not relate to disk encryption."
},
#208
{
    "question": "A technician is building a new computer for a customer. The computer must use an ITX-sized motherboard and have a RAID 5 array with all drives using the same interface. Which of the following drive types will the technician MOST likely utilize?",
    "options": [
        "SCSI",
        "PCIe",
        "NVMe",
        "SATA"
    ],
    "correct_answer": 4,
    "description": "The correct answer is **SATA**. SATA (Serial ATA) is commonly used for RAID configurations in ITX-sized motherboards due to its widespread compatibility and ease of use. RAID 5 requires multiple drives with the same interface, and SATA drives are a common choice for such setups. \n\n- **SCSI (Small Computer System Interface)** is less common in modern consumer-grade systems and is typically used in enterprise environments.\n- **PCIe (Peripheral Component Interconnect Express)** is a high-speed interface used primarily for expansion cards and NVMe drives, but RAID arrays often use SATA drives.\n- **NVMe (Non-Volatile Memory Express)** is a protocol used with PCIe drives for high-speed storage but is not as commonly used for RAID 5 arrays compared to SATA."
},
#209
{
    "question": "Which of the following should a user do FIRST when upgrading the power supply on a gaming PC?",
    "options": [
        "Update the BIOS",
        "Disconnect the system memory",
        "Check the wattage rating",
        "Reseat the graphics card"
    ],
    "correct_answer": 3,
    "description": "The correct answer is **Check the wattage rating**. Before upgrading the power supply, it is crucial to verify the wattage rating to ensure that the new power supply provides sufficient power for all components in the gaming PC. This helps avoid potential issues related to insufficient power.\n\n- **Updating the BIOS** is not directly related to upgrading the power supply.\n- **Disconnecting the system memory** is unnecessary when upgrading the power supply and does not address wattage requirements.\n- **Reseating the graphics card** is not needed for a power supply upgrade unless you’re encountering specific issues with the graphics card."
},
#211
{
    "question": "A user reports a monitor, keyboard, mouse, and headset are no longer functioning. The user has restarted the laptop and tested an alternative headset and monitor, but the issue persists. The technician notices the user has a printer, USB-C hub, and AC adapter plugged into the laptop. Which of the following should the technician do to MOST likely resolve the issue?",
    "options": [
        "Verify the AC adapter voltage",
        "Repair the operating system",
        "Replace the user's USB-C hub",
        "Reinstall the drivers for affected devices",
        "Make sure the printer is not drawing too much power"
    ],
    "correct_answer": 1,
    "description": "The correct answer is **Verify the AC adapter voltage**. If multiple peripherals are not functioning and the user is using a USB-C hub, it is possible that the power supply through the AC adapter is insufficient or faulty. Verifying the AC adapter's voltage ensures that it is providing the necessary power to the laptop and connected peripherals.\n\n- **Replacing the user's USB-C hub** could be considered if the hub were suspected to be faulty, but verifying power is a more immediate step.\n- **Repairing the operating system** is a more drastic measure and less likely to be necessary if the issue is related to power.\n- **Reinstalling drivers** might not address a power-related problem.\n- **Making sure the printer is not drawing too much power** is less likely to be the issue since the problem affects multiple peripherals and is more likely related to overall power delivery."
},
#212
{
    "question": "Which of the following virtualization technologies allows Linux and Windows operating systems to run concurrently?",
    "options": [
        "Test environment",
        "Sandbox",
        "Legacy OS",
        "Cross-platform"
    ],
    "correct_answer": 4,
    "description": "The correct answer is **Cross-platform**. Cross-platform virtualization technologies enable different operating systems, such as Linux and Windows, to run concurrently on the same hardware. Examples include virtual machine software like VMware Workstation, Oracle VM VirtualBox, and Microsoft Hyper-V.\n\n- **Test environment** refers to a setup used for testing software or configurations and does not specifically address running multiple operating systems concurrently.\n- **Sandbox** is used to isolate and run applications securely but does not necessarily support running multiple different operating systems concurrently.\n- **Legacy OS** refers to older operating systems and is not a technology for running different OSes concurrently."
},
#213
{
    "question": "Sensitive data was leaked from a user's smartphone. A technician discovered an unapproved application was installed, and the user has full access to the device's command shell. Which of the following is the NEXT step the technician should take to find the cause of the leaked data?",
    "options": [
        "Restore the device to factory settings",
        "Uninstall the unapproved application",
        "Disable the ability to install applications from unknown sources",
        "Ensure the device is connected to the corporate WiFi network"
    ],
    "correct_answer": 2,
    "description": "The correct answer is **Uninstall the unapproved application**. The unapproved application is likely a significant factor in the data leak. Removing this application will help in determining whether it was responsible for the leak and will prevent further unauthorized access to the device.\n\n- **Restoring the device to factory settings** is a drastic step and may not immediately help in identifying the cause of the leak. It could be considered if other steps fail.\n- **Disabling the ability to install applications from unknown sources** is a preventive measure and does not address the immediate issue with the current unapproved application.\n- **Ensuring the device is connected to the corporate WiFi network** is not directly related to identifying or resolving the data leak issue."
},
#215
{
    "question": "A user reports that a printer is leaving streaks on printed pages. The paper type and the toner have been replaced. Which of the following should the technician check NEXT to resolve the issue?",
    "options": [
        "System board",
        "Paper tray",
        "Memory",
        "Fuser"
    ],
    "correct_answer": 4,
    "description": "The correct answer is **Fuser**. The fuser is responsible for applying heat and pressure to bond the toner to the paper. If the fuser is damaged or worn out, it can cause streaks or other print quality issues. Checking and potentially replacing the fuser is a logical next step after replacing the toner and paper.\n\n- **System board** issues are less likely to cause streaks and are more related to broader hardware malfunctions.\n- **Paper tray** is unlikely to be the cause if the paper type has already been addressed.\n- **Memory** issues might affect printing but are less likely to cause streaks specifically."
},
#216
{
    "question": "A technician needs to recommend an internet connection for a customer who travels around the world and wants to have connectivity while visiting remote camping locations. Some of the locations the customer visits have limited or unreliable cellular service. Which of the following connection types should the technician recommend?",
    "options": [
        "Satellite",
        "DSL",
        "Fiber",
        "Hotspot"
    ],
    "correct_answer": 1,
    "description": "The correct answer is **Satellite**. Satellite internet is ideal for remote locations with limited or unreliable cellular service, as it provides coverage globally by connecting to satellites in space. This allows for internet access in areas where other types of connections might not be available.\n\n- **DSL** and **Fiber** are not suitable for remote or camping locations as they require wired infrastructure that is typically not available in such areas.\n- **Hotspot** relies on cellular networks, which may be unreliable or unavailable in remote locations, making it less suitable for consistent connectivity in those environments."
},
#218
{
    "question": "A technician is troubleshooting an issue with a computer that contains sensitive information. The technician determines the computer needs to be taken off site for repair. Which of the following should the technician do NEXT?",
    "options": [
        "Remove the HDD and then send the computer for repair",
        "Check corporate policies for guidance",
        "Delete the sensitive information before the computer leaves the building",
        "Get authorization from the manager"
    ],
    "correct_answer": 2,
    "description": "The correct answer is **Check corporate policies for guidance**. Before taking any action, it's important to understand and follow corporate policies regarding the handling of sensitive information. This ensures that the technician complies with organizational security protocols and legal requirements.\n\n- **Removing the HDD** might be a necessary step but should be done according to corporate policies.\n- **Deleting sensitive information** might not be appropriate without policy guidance and could lead to unintended data loss.\n- **Getting authorization from the manager** is important but comes after reviewing and understanding the corporate policies."
},
#219
{
    "question": "A user has decided to build a new computer with parts purchased from a popular online vendor. The user has referenced online resources to assemble the unit. However, when the user presses the power button, the new computer does not load the operating system's installer. Instead, the onboard speaker beeps and immediately reports an issue on the screen. Which of the following is the MOST likely issue with the new build?",
    "options": [
        "The user did not plug in the processor's fan",
        "The user did not apply thermal paste to the CPU",
        "The user did not seat the GPU correctly",
        "The user did not install the power supply"
    ],
    "correct_answer": 1,
    "description": "The correct answer is **The user did not plug in the processor's fan**. Many motherboards have a safety feature that prevents the computer from booting if the CPU fan is not connected. This is to protect the CPU from overheating. The beeping sound is often a signal from the motherboard indicating a hardware issue, such as a missing CPU fan connection.\n\n- **Not applying thermal paste** is critical for thermal management but would likely not cause the beeping issue; it could lead to overheating if the system did boot.\n- **Not seating the GPU correctly** could cause display issues but typically wouldn't result in beeping errors unless there is a specific error code related to GPU seating.\n- **Not installing the power supply** would prevent the computer from powering on at all, so it's less likely to be the issue if the system is showing a beeping error."
},
#221
{
    "question": "A technician is setting up a new desktop computer and will be installing the hard drive directly on the motherboard without using cables to connect it. Which of the following will the technician be installing?",
    "options": [
        "Thunderbolt",
        "eSATA",
        "M.2",
        "SCSI"
    ],
    "correct_answer": 3,
    "description": "The correct answer is **M.2**. M.2 is a type of interface that allows for direct connection of storage devices to the motherboard without the need for cables. It is commonly used for high-speed SSDs in modern desktops and laptops.\n\n- **Thunderbolt** is an interface used for high-speed data transfer and connecting peripherals, not specifically for internal storage.\n- **eSATA** is an external SATA connection used for connecting external hard drives and requires cables.\n- **SCSI** (Small Computer System Interface) is an older standard for connecting drives and other peripherals and typically uses cables for connections."
},
#222
{
    "question": "An insurance company wants to implement cloud computing and would like a cloud solution in which the infrastructure is shared with businesses in the same industry. Which of the following cloud models BEST addresses the company's need?",
    "options": [
        "Community",
        "Private",
        "Public",
        "Hybrid"
    ],
    "correct_answer": 1,
    "description": "The correct answer is **Community**. A community cloud model involves sharing infrastructure among organizations with similar interests or in the same industry, which fits the insurance company's requirement to share infrastructure with other businesses in the same sector.\n\n- **Private** cloud is dedicated to a single organization and does not share infrastructure with other businesses.\n- **Public** cloud is shared with the general public and is not industry-specific.\n- **Hybrid** cloud combines private and public clouds but does not specifically address the need for shared infrastructure within a particular industry."
},
#223
{
    "question": "A home user has purchased a subscription for a service that blocks malicious sites by preventing them from resolving correctly. Which of the following settings MOST likely needs to be changed on the user's router to enable this functionality?",
    "options": [
        "DNS server",
        "Port forwarding",
        "Perimeter network",
        "Universal PnP",
        "DHCP server"
    ],
    "correct_answer": 1,
    "description": "The correct answer is **DNS server**. To enable a service that blocks malicious sites by preventing them from resolving correctly, the user needs to configure the router to use the DNS servers provided by the service. This ensures that DNS queries are directed through the service that blocks harmful sites.\n\n- **Port forwarding** is used for directing traffic to specific devices within a network but does not relate to DNS functionality.\n- **Perimeter network** (or DMZ) is used to isolate a network from external threats but does not involve DNS resolution.\n- **Universal PnP** (Plug and Play) is related to automatic network device configuration and is not related to DNS blocking.\n- **DHCP server** provides IP addresses to devices on the network and does not directly affect DNS resolution."
},
#225
{
    "question": "A technician is troubleshooting a projector that will not display any images. The technician has verified the computer output and cable are providing a good video signal. Which of the following should the technician do NEXT?",
    "options": [
        "Calibrate the image",
        "Replace the bulb",
        "Test the output resolution",
        "Clean the fans"
    ],
    "correct_answer": 2,
    "description": "The correct answer is **Replace the bulb**. If the projector is not displaying any images despite a good video signal and cable connection, the most likely issue is a burned-out or faulty bulb. Replacing the bulb is a standard troubleshooting step for this issue.\n\n- **Calibrating the image** and **testing the output resolution** are important steps but are less likely to address a complete lack of image display.\n- **Cleaning the fans** might help with overheating issues but does not directly address the problem of no image display."
},
#226
{
    "question": "A user's Windows computer started running slowly after the installation of a CAD program. The computer has intermittent timeouts and often has to be rebooted to restore functionality. The computer seems to work correctly if the application is not running. Which of the following should the technician do NEXT to help troubleshoot the issue? (Choose two.)",
    "options": [
        "Replace the video card",
        "Research the requirements of the application",
        "Install a new case fan",
        "Run chkdsk on the HDD",
        "Check the Event Viewer logs",
        "Reinstall the application"
    ],
    "correct_answer": [2, 5],
    "description": "The correct answers are **Research the requirements of the application** and **Check the Event Viewer logs**.\n\n- **Research the requirements of the application** to ensure that the computer meets the necessary hardware and software specifications for running the CAD program. Inadequate resources could lead to slow performance and timeouts.\n- **Check the Event Viewer logs** to identify any errors or warnings that may provide insights into the cause of the issues when the application is running.\n\n- **Replacing the video card** and **installing a new case fan** may not be directly related to the specific problem described and should be considered after verifying application requirements and logs.\n- **Running chkdsk on the HDD** is useful for diagnosing disk errors but may not address performance issues specifically related to the CAD application.\n- **Reinstalling the application** could be considered if other troubleshooting steps do not resolve the issue, but it is more effective to first confirm that system requirements are met and check for relevant errors."
},
#227
{
    "question": "A user's device needs more memory, so a technician installs extra RAM with the following specifications:\n\n2 x 8Gb DDR3-1066 (PC3-8500)\n1 x 16Gb DDR3-1333 (PC3-10600)\n\nWhich of the following speeds would maximize reliability?",
    "options": [
        "1,066",
        "1,333",
        "8,500",
        "10,600"
    ],
    "correct_answer": 1,
    "description": "The correct answer is **1,066**. When mixing RAM modules with different speeds, the system typically operates at the speed of the slowest module to ensure compatibility and stability. In this case, since one of the RAM modules is DDR3-1066, the system will operate all the RAM at this slower speed to maintain reliability.\n\n- **1,333** represents the speed of the faster module, but the system will default to the slower speed to ensure stable operation.\n- **8,500** and **10,600** refer to the memory's bandwidth rating (PC3-8500 and PC3-10600), not the clock speed. The actual operating speed of the RAM is more relevant to reliability."
},
#228
{
    "question": "A user reports that a computer has a virus on it. Which of the following is the FIRST step the technician should take?",
    "options": [
        "Determine a plan of action to resolve the problem",
        "Run antivirus software to remove the virus from the computer",
        "Ask the user about the symptoms the computer is experiencing",
        "Make a backup of the user's data on an external drive"
    ],
    "correct_answer": 3,
    "description": "The correct answer is **Ask the user about the symptoms the computer is experiencing**. The first step in addressing a potential virus infection is to gather information about the symptoms and any unusual behavior observed by the user. This helps in understanding the nature of the issue and informs the subsequent steps in the troubleshooting and resolution process.\n\n- **Determining a plan of action** is important but should come after gathering detailed information about the symptoms.\n- **Running antivirus software** is a crucial step, but it should be done after understanding the issue and potentially backing up data if needed.\n- **Making a backup of the user's data** is a good practice, but asking about symptoms first helps to ensure that any actions taken are appropriate for the specific situation."
},
#229
{
    "question": "A user lost a wallet containing credit and debit cards and is unable to purchase merchandise. Which of the following mobile phone technologies would allow the user to complete transactions?",
    "options": [
        "GSM",
        "MFA",
        "PRL",
        "NFC"
    ],
    "correct_answer": 3,
    "description": "The correct answer is **NFC**. Near Field Communication (NFC) technology allows mobile phones to make transactions by enabling contactless payments, such as through digital wallets or mobile payment apps. This would allow the user to complete transactions even if they have lost their physical cards.\n\n- **GSM** (Global System for Mobile Communications) is related to mobile phone network standards and does not facilitate transactions.\n- **MFA** (Multi-Factor Authentication) enhances security but is not directly related to making payments.\n- **PRL** (Preferred Roaming List) is used for managing network connections and roaming but does not pertain to payment transactions."
},
#230
{
    "question": "A company uses legacy accounting software, and no replacement is available. Which of the following virtualization solutions will the company MOST likely select?",
    "options": [
        "Network",
        "Storage",
        "Desktop",
        "Sandbox"
    ],
    "correct_answer": 3,
    "description": "The correct answer is **Desktop**. Desktop virtualization allows the company to run legacy accounting software in a virtualized environment on a modern operating system. This is useful for continuing to use outdated software that may not be compatible with current hardware or operating systems.\n\n- **Network** virtualization focuses on creating virtual network environments and is not directly related to running specific software.\n- **Storage** virtualization deals with abstracting physical storage into virtual storage but does not address software compatibility.\n- **Sandbox** virtualization is used to create isolated environments for testing and running potentially risky applications but may not be the best fit for long-term use of legacy software."
},
#231
{
    "question": "The owner of a restaurant reports that wireless network connections are lost intermittently throughout the day. Which of the following steps should a technician take to troubleshoot the issue? (Choose two.)",
    "options": [
        "Identify the location of devices that utilize 2.4GHz",
        "Check to see if the phones are UTP or STP lines",
        "Test to see if the copper electrical wires are causing interference",
        "Map all of the wireless signals in the restaurant",
        "Verify T568B is being used in the wiring closet patch panel",
        "Schedule timed router reboots throughout the day"
    ],
    "correct_answer": [1, 4],
    "description": "The correct answers are **Identify the location of devices that utilize 2.4GHz** and **Map all of the wireless signals in the restaurant**.\n\n- **Identifying the location of devices that utilize 2.4GHz** helps to determine if there are too many devices or sources of interference on the 2.4GHz band, which is commonly used by many devices and can cause congestion and connectivity issues.\n- **Mapping all of the wireless signals** helps to identify areas with weak or overlapping signals, interference sources, or other issues affecting connectivity.\n\n- **Checking if the phones are UTP or STP lines** and **verifying T568B wiring** are not directly related to wireless network issues.\n- **Testing if the copper electrical wires are causing interference** may be less relevant compared to checking wireless signal mapping.\n- **Scheduling timed router reboots** could temporarily address the issue but does not solve the underlying cause of intermittent connectivity."
},
#233
{
    "question": "A web developer needs to test the compatibility of web functions across multiple different browsers and versions of those browsers. The web developer only has one machine and cannot install multiple browser versions. Which of the following should the developer do to BEST resolve the issue?",
    "options": [
        "Purchase more machines",
        "Deploy application virtualization",
        "Test using a virtual desktop",
        "Set up a multiboot configuration"
    ],
    "correct_answer": 3,
    "description": "The correct answer is **Test using a virtual desktop**. Testing using a virtual desktop allows the web developer to create multiple virtual environments with different browser versions and configurations on a single physical machine. This approach provides flexibility and isolation for testing various browser compatibility issues without needing additional hardware or complex setup.\n\n- **Purchasing more machines** is not necessary if virtualization can provide the needed environments.\n- **Deploying application virtualization** is generally more focused on running specific applications in isolation rather than providing different browser versions.\n- **Setting up a multiboot configuration** could be complex and cumbersome compared to using virtual desktops for testing multiple environments."
},
#235
{
    "question": "A technician is replacing all RJ45 cables in a customer environment. Which of the following are the BEST tools to execute the task? (Choose two.)",
    "options": [
        "Optical fiber tester",
        "Scissors",
        "Cable tester",
        "Crimper",
        "Coaxial cable",
        "Screwdriver"
    ],
    "correct_answer": [3, 4],
    "description": "The correct answers are **Cable tester** and **Crimper**.\n\n- **Cable tester** is used to verify that the newly installed RJ45 cables are correctly wired and functioning properly. It helps ensure that there are no faults or wiring issues in the cables.\n- **Crimper** is used to attach RJ45 connectors to the ends of the network cables. It is essential for creating properly terminated Ethernet cables.\n\n- **Optical fiber tester** is used for fiber optic cables, not RJ45 cables.\n- **Scissors** may be used to cut the cable, but they are not the primary tool for terminating or testing cables.\n- **Coaxial cable** is unrelated to RJ45 cables, which are used for Ethernet.\n- **Screwdriver** might be useful for other tasks but is not specifically required for replacing or testing RJ45 cables."
},
#236
{
    "question": "A technician needs to configure a printer for network communications. Which of the following must the technician configure? (Choose three.)",
    "options": [
        "PCL",
        "Dots per inch",
        "Gateway",
        "Subnet mask",
        "MAC address",
        "IMEI",
        "IP address",
        "Drivers"
    ],
    "correct_answer": [3, 4, 7],
    "description": "The correct answers are **Gateway**, **Subnet mask**, and **IP address**.\n\n- **IP address** is essential for identifying the printer on the network and enabling communication with other devices.\n- **Gateway** is needed to route traffic between different networks, such as from the local network to the internet.\n- **Subnet mask** is used to define the network portion of the IP address and to help with proper routing within the network.\n\n- **PCL** (Printer Command Language) is related to printing language rather than network configuration.\n- **Dots per inch (DPI)** relates to print quality and resolution, not network settings.\n- **MAC address** is useful for network management but is not typically configured directly on the printer for network communication.\n- **IMEI** is related to mobile devices, not printers.\n- **Drivers** are necessary for the printer to function with computers but are not part of network configuration."
},
#237
{
    "question": "Which of the following allows a switch to be divided into separate logical networks?",
    "options": [
        "VLAN",
        "SSL VPN",
        "NAT",
        "RADIUS"
    ],
    "correct_answer": 1,
    "description": "The correct answer is **VLAN**. Virtual Local Area Network (VLAN) allows a switch to be divided into separate logical networks. This segmentation enables better management and isolation of network traffic within a single physical switch.\n\n- **SSL VPN** provides secure remote access to a network but does not segment a switch into logical networks.\n- **NAT** (Network Address Translation) translates private IP addresses to public IP addresses but does not create logical network separation within a switch.\n- **RADIUS** (Remote Authentication Dial-In User Service) is used for authentication and authorization but does not handle network segmentation."
},
#238
{
    "question": "An administrator chose a shared-tenant model for a cloud deployment. Which of the following is the MOST likely reason the administrator chose this model?",
    "options": [
        "Cost savings",
        "Highly available",
        "Dedicated hardware",
        "Increased security"
    ],
    "correct_answer": 1,
    "description": "The correct answer is **Cost savings**. In a shared-tenant model, multiple customers share the same physical infrastructure and resources, which significantly reduces costs compared to dedicated hardware models. This cost efficiency is a primary reason organizations opt for shared-tenant cloud deployments.\n\n- **Highly available** is a benefit of many cloud models but not specific to the shared-tenant model.\n- **Dedicated hardware** is characteristic of a private cloud or dedicated instance, not a shared-tenant model.\n- **Increased security** is generally associated with private or dedicated cloud models where resources are not shared among multiple tenants."
},
#239
{
    "question": "A user is having an issue with the touch screen on a mobile device. When the user touches the screen, the intended target is not selected. Which of the following would be the BEST action for a technician to take to resolve the issue?",
    "options": [
        "Calibrate the touch screen",
        "Reset the mobile device",
        "Replace the LED screen",
        "Update the mobile device"
    ],
    "correct_answer": 1,
    "description": "The correct answer is **Calibrate the touch screen**. If the touch screen is not accurately selecting the intended targets, calibration can help align touch input with the on-screen elements. This process adjusts the touch screen settings to improve its responsiveness and accuracy.\n\n- **Resetting the mobile device** might resolve software issues but is less targeted to fixing touch screen accuracy problems.\n- **Replacing the LED screen** is usually unnecessary unless there is physical damage to the screen, as this issue seems to be related to touch input accuracy rather than screen damage.\n- **Updating the mobile device** could potentially fix software-related issues but calibration directly addresses touch screen alignment problems."
},
#240
{
    "question": "A user submitted a help desk ticket to report that the Wi-Fi connection drops every time the microwave is used. A technician suspects the issue is related to interference. Which of the following should the technician do to provide the BEST long-term solution for the issue?",
    "options": [
        "Change the Wi-Fi operation channel",
        "Configure the Wi-Fi AP to 5GHz",
        "Increase the power output of the AP",
        "Change the SSID to hidden"
    ],
    "correct_answer": 2,
    "description": "The correct answer is **Configure the Wi-Fi AP to 5GHz**. Microwaves operate on the 2.4 GHz frequency, which is also used by many Wi-Fi networks. Switching the Wi-Fi access point (AP) to the 5 GHz band can help avoid interference from the microwave, as the 5 GHz band is less susceptible to interference and has less overlap with common household devices.\n\n- **Changing the Wi-Fi operation channel** might help reduce interference on the 2.4 GHz band, but configuring the AP to 5 GHz provides a more robust and long-term solution.\n- **Increasing the power output of the AP** does not address the root cause of interference and might not resolve the issue effectively.\n- **Changing the SSID to hidden** does not mitigate interference problems and is more related to hiding the network from discovery."
},
#241
{
    "question": "To which of the following should a technician connect individual pairs of a Cat 6 cable in order to provide a connection to a switch?",
    "options": [
        "Access point",
        "Patch panel",
        "Hub",
        "Firewall",
        "Wall jack"
    ],
    "correct_answer": 2,
    "description": "The correct answer is **Patch panel**. A patch panel is used to organize and connect individual network cables, including Cat 6 cables, to network equipment like switches. It provides a central point for managing network connections.\n\n- **Access point** is used to connect wireless devices to a network, not for connecting individual cable pairs.\n- **Hub** is an older network device that connects multiple Ethernet devices but is less commonly used today compared to switches.\n- **Firewall** is used for network security and does not typically connect individual cable pairs.\n- **Wall jack** is a network interface point on the wall where cables are connected but does not organize or manage connections like a patch panel does."
},
#242
{
    "question": "Which of the following describes traffic used to resolve the FQDN of a site into an IP address to help locate and browse websites appropriately?",
    "options": [
        "DNS",
        "AAA",
        "SCADA",
        "IoT",
        "SQL"
    ],
    "correct_answer": 1,
    "description": "The correct answer is **DNS**. Domain Name System (DNS) is used to resolve Fully Qualified Domain Names (FQDNs) into IP addresses, enabling users to access websites using human-readable domain names rather than numerical IP addresses.\n\n- **AAA** (Authentication, Authorization, and Accounting) refers to security protocols related to user access and permissions, not domain resolution.\n- **SCADA** (Supervisory Control and Data Acquisition) is used in industrial control systems, not for resolving domain names.\n- **IoT** (Internet of Things) refers to networked devices and smart technologies, not specifically to domain resolution.\n- **SQL** (Structured Query Language) is used for database management and queries, not for resolving domain names."
},
#243
{
    "question": "A business purchased a new multifunction printer that will be used to photocopy documents with hundreds of pages. A technician is configuring the printer. Which of the following features should the technician ensure is set up?",
    "options": [
        "SMB",
        "PCL",
        "ADF",
        "SSH"
    ],
    "correct_answer": 3,
    "description": "The correct answer is **ADF** (Automatic Document Feeder). An ADF allows the printer to automatically feed multiple pages through the scanning or copying process, which is essential for handling large volumes of documents efficiently.\n\n- **SMB** (Server Message Block) is a network file sharing protocol and is not directly related to the physical handling of documents.\n- **PCL** (Printer Command Language) is a page description language used for communication between a printer and a computer but does not affect the document handling capability.\n- **SSH** (Secure Shell) is a protocol for secure network communications and does not relate to the physical document handling capabilities of the printer."
},
#245
{
    "question": "Which of the following network devices operates as a bridge function?",
    "options": [
        "Hub",
        "Wireless access point",
        "Transceiver",
        "Media converter"
    ],
    "correct_answer": 2,
    "description": "The correct answer is **Wireless access point**. A wireless access point can operate in a bridge mode to connect two or more network segments, extending the network range and enabling communication between wired and wireless networks.\n\n- **Hub** is a basic networking device that broadcasts data to all connected devices and does not have bridging capabilities.\n- **Transceiver** is used to transmit and receive data signals but does not perform bridging functions.\n- **Media converter** is used to convert between different types of network media (e.g., fiber to copper) but does not function as a network bridge."
},
#246-250
    {
        "question": "A user's touch-screen tablet is having an issue with the screen orientation. Which of the following is MOST likely causing this issue?",
        "options": [
            "The screen rotation is locked.",
            "The screen protector on the tablet is damaged.",
            "The touch-screen digitizer is malfunctioning.",
            "The inverter is misconfigured."
        ],
        "correct_answer": 1,
        "description": "The correct answer is **The screen rotation is locked**. If a tablet's screen orientation isn't adjusting correctly, it is most likely due to screen rotation being locked, which prevents automatic changes in orientation.\n\n- **The screen protector on the tablet is damaged** would more likely affect touch sensitivity, not screen orientation.\n- **The touch-screen digitizer is malfunctioning** would generally affect touch functionality, not orientation.\n- **The inverter is misconfigured** is not relevant for touch-screen devices, as it pertains to the backlight of LCD screens."
    },
    {
        "question": "The GPS on a user's phone has been unreliable. Which of the following will MOST likely resolve the issue?",
        "options": [
            "Enabling high-accuracy mode",
            "Replacing the battery",
            "Disabling Wi-Fi connections",
            "Utilizing a third-party map application"
        ],
        "correct_answer": 1,
        "description": "The correct answer is **Enabling high-accuracy mode**. High-accuracy mode utilizes GPS, Wi-Fi, and mobile networks to improve location accuracy, which is the best approach for resolving GPS reliability issues.\n\n- **Replacing the battery** is unlikely to affect GPS performance.\n- **Disabling Wi-Fi connections** would likely reduce the accuracy of location services rather than improve it.\n- **Utilizing a third-party map application** does not directly address the GPS accuracy issue."
    },
    {
        "question": "A user is no longer able to start the OS on a computer and receives an error message indicating there is no OS found. A technician reviews the audit logs and notes that the user's system posted a S.M.A.R.T. error just days before this issue. Which of the following is the MOST likely cause of this issue?",
        "options": [
            "Boot order",
            "Malware",
            "Drive failure",
            "Windows updates"
        ],
        "correct_answer": 3,
        "description": "The correct answer is **Drive failure**. A S.M.A.R.T. error indicates that the hard drive has potential issues, which is consistent with an error stating that no OS is found, likely due to a failing or failed drive.\n\n- **Boot order** issues would prevent the system from finding the OS but wouldn’t be indicated by a S.M.A.R.T. error.\n- **Malware** could cause boot issues but isn’t typically indicated by S.M.A.R.T. errors.\n- **Windows updates** are less likely to cause an OS not found error, especially when accompanied by S.M.A.R.T. warnings."
    },
    {
        "question": "A customer reports that, after a technician replaced a laptop screen, the laptop is only able to connect to a Wi-Fi network if it is positioned very close to a wireless access point. Which of the following should the technician verify FIRST?",
        "options": [
            "The internal antennas are connected.",
            "The device has the latest OS updates.",
            "The wireless device drivers are the latest version.",
            "Airplane mode is disabled.",
            "The battery is charging."
        ],
        "correct_answer": 1,
        "description": "The correct answer is **The internal antennas are connected**. After a screen replacement, it's possible that internal Wi-Fi antennas were disconnected or not properly reconnected, affecting the Wi-Fi signal strength.\n\n- **The device has the latest OS updates** is less likely to cause a sudden change in Wi-Fi connectivity after hardware replacement.\n- **The wireless device drivers are the latest version** is important but less likely to be the immediate cause if the problem arose directly after hardware work.\n- **Airplane mode is disabled** is not directly related to the issue if the laptop was functioning previously.\n- **The battery is charging** does not affect Wi-Fi performance."
    },
    {
        "question": "Which of the following is used to explain issues that may occur during a change implementation?",
        "options": [
            "Scope change",
            "End-user acceptance",
            "Risk analysis",
            "Rollback plan"
        ],
        "correct_answer": 3,
        "description": "The correct answer is **Risk analysis**. Risk analysis is used to identify and evaluate potential issues that might arise during a change implementation. It helps in understanding the risks associated with the change and planning accordingly.\n\n- **Scope change** refers to modifications in the project scope, not specifically to addressing potential issues.\n- **End-user acceptance** involves ensuring that users are satisfied with the changes, rather than addressing potential issues.\n- **Rollback plan** is a strategy to revert changes if something goes wrong, but risk analysis is used to predict potential issues before they occur."
    },
#251-260
    {
        "question": "Which of the following server roles does RADIUS perform?",
        "options": [
            "DNS",
            "AAA",
            "Mail server",
            "Syslog"
        ],
        "correct_answer": 2,
        "description": "The correct answer is **AAA**. RADIUS (Remote Authentication Dial-In User Service) is used for authentication, authorization, and accounting, which are collectively referred to as AAA.\n\n- **DNS** (Domain Name System) resolves domain names to IP addresses.\n- **Mail server** manages and delivers email.\n- **Syslog** is used for logging system messages."
    },
    {
        "question": "When a page that was printed on a laser printer is touched, the image on the paper smears. Which of the following is MOST likely the cause of this issue?",
        "options": [
            "Duplexing assembly",
            "Fuser",
            "Toner",
            "Transfer belt"
        ],
        "correct_answer": 2,
        "description": "The correct answer is **Fuser**. The fuser unit in a laser printer heats the toner powder to fuse it onto the paper. If the fuser is not working correctly, the toner may not adhere properly, causing smearing.\n\n- **Duplexing assembly** is related to printing on both sides of the paper.\n- **Toner** issues usually manifest as poor print quality, not smearing.\n- **Transfer belt** is responsible for transferring toner to the paper but would not typically cause smearing."
    },
    {
        "question": "A technician is troubleshooting a smartphone that has a large dark area on the screen. The screen has no damage to indicate that it is cracked. Which of the following BEST describes why a blot is on the screen?",
        "options": [
            "Digitizer damage",
            "Improper charging",
            "Ambient light sensor damage",
            "Liquid damage"
        ],
        "correct_answer": 4,
        "description": "The correct answer is **Liquid damage**. Liquid damage can cause dark areas or blotches on a smartphone screen even if there is no visible crack.\n\n- **Digitizer damage** would more likely affect touch functionality.\n- **Improper charging** does not typically cause screen blotches.\n- **Ambient light sensor damage** would affect screen brightness or automatic adjustments but not cause dark areas."
    },
    {
        "question": "An office worker requests dual-screen capability with a laptop. Which of the following peripherals is required to fulfill this request?",
        "options": [
            "Docking station",
            "HD webcam",
            "KVM switch",
            "USB hub"
        ],
        "correct_answer": 1,
        "description": "The correct answer is **Docking station**. A docking station allows a laptop to connect to multiple monitors and other peripherals, making it suitable for setting up dual screens.\n\n- **HD webcam** is used for video communication.\n- **KVM switch** allows control of multiple computers with a single set of peripherals.\n- **USB hub** expands the number of USB ports but does not facilitate dual-screen setups."
    },
    {
        "question": "A technician is preparing laptops for deployment to a medical department. The laptops require SSD-level encryption to be enabled, but BitLocker refuses to turn it on. An error message states that a BIOS-level setting has not been turned on. Which of the following should the technician check FIRST when troubleshooting this issue?",
        "options": [
            "Reorder the priority in Windows Boot Manager.",
            "Check to make sure Secure Boot is turned on.",
            "Ensure that the Trusted Platform Module is enabled.",
            "Verify that the latest updates are installed."
        ],
        "correct_answer": 3,
        "description": "The correct answer is **Ensure that the Trusted Platform Module is enabled**. BitLocker encryption requires TPM (Trusted Platform Module) to be enabled in the BIOS for encryption functionalities.\n\n- **Reorder the priority in Windows Boot Manager** is not directly related to BitLocker encryption issues.\n- **Check to make sure Secure Boot is turned on** is important for system security but not directly related to BitLocker requirements.\n- **Verify that the latest updates are installed** is a good practice but does not address the TPM requirement."
    },
    {
        "question": "Which of the following BEST describes a lab environment in which virtual machines can be created, rebooted, and shut down without affecting the production network?",
        "options": [
            "SCADA",
            "Sandbox",
            "Honeypot",
            "Hybrid cloud"
        ],
        "correct_answer": 2,
        "description": "The correct answer is **Sandbox**. A sandbox is an isolated environment where virtual machines and applications can be tested or run without impacting the production network.\n\n- **SCADA** (Supervisory Control and Data Acquisition) systems are used for industrial control systems and are not related to virtual machine testing environments.\n- **Honeypot** is a security mechanism designed to attract and trap potential attackers, not for testing virtual machines.\n- **Hybrid cloud** involves a combination of on-premises and cloud resources, not specifically for isolated virtual machine environments."
    },
    {
        "question": "A SOHO customer would like to purchase network hardware to enhance security. The hardware should perform stateful packet inspection. Which of the following would BEST address the customer's need?",
        "options": [
            "Switch",
            "Firewall",
            "Router",
            "Proxy"
        ],
        "correct_answer": 2,
        "description": "The correct answer is **Firewall**. A firewall performs stateful packet inspection to monitor and control network traffic based on predefined security rules.\n\n- **Switch** primarily manages network traffic within a LAN and does not handle security inspection.\n- **Router** directs traffic between networks but may not perform stateful packet inspection unless it is a specific type of router with integrated firewall capabilities.\n- **Proxy** serves as an intermediary for requests from clients seeking resources but does not perform stateful packet inspection."
    },
    {
        "question": "An IT manager is evaluating ticket resolution times. While reviewing the data, the manager notices repetitive issues are taking longer than expected to resolve. Which of the following changes should the manager implement to resolve repetitive issues more quickly?",
        "options": [
            "Require the technicians to spend more time testing theories to determine the root causes of issues.",
            "Require the technicians to verify full system functionality when resolving issues.",
            "Require the technicians to gather more information when speaking with users about issues.",
            "Require the technicians to document the findings, actions, and outcomes of issues."
        ],
        "correct_answer": 4,
        "description": "The correct answer is **Require the technicians to document the findings, actions, and outcomes of issues**. Proper documentation helps in building a knowledge base of common issues and solutions, which can speed up the resolution of repetitive problems.\n\n- **Require the technicians to spend more time testing theories to determine the root causes of issues** may delay resolution times.\n- **Require the technicians to verify full system functionality when resolving issues** is important but may not address the specific issue of repetitive problems.\n- **Require the technicians to gather more information when speaking with users about issues** helps but documentation provides a broader solution for repetitive issues."
    },
    {
        "question": "A technician is troubleshooting a laptop that has a blank LCD panel. The technician shines a flashlight into the LCD and sees a faint image. Which of the following BEST describes the issue?",
        "options": [
            "Defective inverter",
            "Incompatible video driver",
            "Incorrect input source",
            "Burned-out bulb"
        ],
        "correct_answer": 1,
        "description": "The correct answer is **Defective inverter**. If a faint image is visible under a flashlight, the issue is likely with the inverter, which is responsible for providing backlight to the LCD screen.\n\n- **Incompatible video driver** would not affect the backlight of the LCD panel.\n- **Incorrect input source** would affect the signal but not the visibility of a faint image.\n- **Burned-out bulb** is related to older LCDs and not applicable to most modern laptops."
    },
#261-266
    {
        "question": "A technician is adding one more line at the demarcation point. Which of the following tools would be MOST useful to accomplish this task?",
        "options": [
            "Toner",
            "Punchdown",
            "Network tap",
            "Crimper"
        ],
        "correct_answer": 2,
        "description": "The correct answer is **Punchdown**. A punchdown tool is used to insert wires into a punchdown block or patch panel at the demarcation point.\n\n- **Toner** is used for tracing cables and identifying their location.\n- **Network tap** is used for monitoring network traffic.\n- **Crimper** is used to attach connectors to the ends of cables."
    },
    {
        "question": "Which of the following is the default GUI and file manager in macOS?",
        "options": [
            "Disk Utility",
            "Finder",
            "Dock",
            "FileVault"
        ],
        "correct_answer": 2,
        "description": "The correct answer is **Finder**. Finder is the default file manager and GUI interface used to navigate files and folders in macOS.\n\n- **Disk Utility** is used for managing disks and volumes.\n- **Dock** is a feature of the macOS interface used to launch applications and access documents.\n- **FileVault** is a disk encryption program for securing files."
    },
    {
        "question": "A user called the help desk to report an issue with a laptop. Recently, the user has been unable to click the buttons on the track pad or press some keys on the keyboard. The technician inspects the laptop but does not find any physical damage caused by the user. Which of the following is the MOST likely cause of the issue?",
        "options": [
            "Damaged digitizer",
            "Swollen battery",
            "Distended capacitors",
            "Failed accelerometer"
        ],
        "correct_answer": 2,
        "description": "The correct answer is **Swollen battery**. A swollen battery can exert pressure on internal components, affecting the functionality of the trackpad and keyboard.\n\n- **Damaged digitizer** would affect touch functionality, not physical buttons.\n- **Distended capacitors** would likely cause power issues or display problems, not trackpad or keyboard issues.\n- **Failed accelerometer** affects device orientation detection, not keyboard or trackpad functionality."
    },
    {
        "question": "Following a scheduled power outage, users report they cannot access the local intranet. A technician is able to ping the IP address of the server that is hosting the website. Which of the following servers is MOST likely offline?",
        "options": [
            "Web",
            "DNS",
            "File",
            "DHCP"
        ],
        "correct_answer": 2,
        "description": "The correct answer is **DNS**. If users can ping the server's IP address but cannot access the local intranet, it suggests that DNS services may be down, preventing the resolution of hostnames to IP addresses.\n\n- **Web** server would affect access to the website but not the ability to ping the IP address.\n- **File** server issues would affect file access, not general network connectivity.\n- **DHCP** server issues would usually prevent IP address assignment, affecting network access entirely."
    },
    {
        "question": "A server administrator is building a new application server. Which of the following RAID levels provides MAXIMUM performance and redundancy?",
        "options": [
            "RAID 0",
            "RAID 1",
            "RAID 5",
            "RAID 10"
        ],
        "correct_answer": 4,
        "description": "The correct answer is **RAID 10**. RAID 10 (1+0) provides both maximum performance and redundancy by combining RAID 1 (mirroring) and RAID 0 (striping).\n\n- **RAID 0** offers maximum performance but no redundancy.\n- **RAID 1** provides redundancy but only moderate performance.\n- **RAID 5** offers a balance of performance, redundancy, and storage efficiency but does not match RAID 10 in performance."
    },
#268-277
    {
        "question": "A customer has a Wi-Fi-capable laptop to use when traveling for work. Which of the following will allow the laptop to stay connected when the user travels?",
        "options": [
            "Cellular card",
            "Wi-Fi extender",
            "Bluetooth",
            "GPS"
        ],
        "correct_answer": 1,
        "description": "The correct answer is **Cellular card**. A cellular card allows the laptop to connect to the internet through mobile data when traveling and Wi-Fi is unavailable.\n\n- **Wi-Fi extender** is used to extend the range of a Wi-Fi signal but won't help when traveling.\n- **Bluetooth** is used for short-range connections to other devices and does not provide internet access.\n- **GPS** is for location services, not internet connectivity."
    },
    {
        "question": "A department submits a ticket to report a printer is not working. The responding technician sees paper stuck to the fuser, which is much hotter than normal. The fuser was just installed a few weeks ago, as indicated by the service history. Which of the following should the technician do NEXT?",
        "options": [
            "Disconnect the printer power for troubleshooting.",
            "Install a printer roller kit.",
            "Replace the overheating fuser.",
            "Replace the paper with thicker paper stock."
        ],
        "correct_answer": 3,
        "description": "The correct answer is **Replace the overheating fuser**. Since the fuser is overheating, it's most likely defective and should be replaced to avoid further issues.\n\n- **Disconnecting the printer power** is a safety precaution but doesn't resolve the root cause.\n- **Installing a printer roller kit** won't fix the fuser overheating problem.\n- **Replacing the paper** will not affect the temperature of the fuser."
    },
    {
        "question": "Which of the following does a DHCP reservation MOST likely apply to?",
        "options": [
            "Smart TV",
            "Mobile device",
            "Workstation",
            "Printer"
        ],
        "correct_answer": 4,
        "description": "The correct answer is **Printer**. A DHCP reservation is often used for printers to ensure they always get the same IP address, making them easier to manage in the network.\n\n- **Smart TVs** and **mobile devices** typically don't require static IPs.\n- **Workstations** may have reservations, but printers are the most common."
    },
    {
        "question": "A technician is working to connect an RS-232 serial signature pad to a customer's ultralightweight laptop. Which of the following should the technician use to install the device?",
        "options": [
            "Port replicator",
            "Wi-Fi Direct",
            "Hotspot",
            "USB-C cable"
        ],
        "correct_answer": 1,
        "description": "The correct answer is **Port replicator**. Since the ultralightweight laptop may not have an RS-232 port, using a port replicator provides additional ports, including serial connections.\n\n- **Wi-Fi Direct** and **Hotspot** are wireless technologies unrelated to serial connections.\n- **USB-C cable** is not compatible with RS-232 without an adapter."
    },
    {
        "question": "Which of the following wireless networking protocols will support both 2.4GHz and 5GHz devices?",
        "options": [
            "802.11ac",
            "802.11ax",
            "802.11b",
            "802.11g"
        ],
        "correct_answer": 2,
        "description": "The correct answer is **802.11ax**. This protocol supports both 2.4GHz and 5GHz frequencies, making it compatible with a wide range of devices.\n\n- **802.11ac** supports only 5GHz.\n- **802.11b** and **802.11g** support only 2.4GHz."
    },
    {
        "question": "A customer reports that access to the network fileshare has become much slower than usual, but local applications do not seem to have trouble. The technician checks the bandwidth to other servers and finds no issues. Which of the following should the technician check NEXT?",
        "options": [
            "Level of network utilization",
            "Customer use of two-factor authentication",
            "Amount of local drive space",
            "RAID array drive health"
        ],
        "correct_answer": 4,
        "description": "The correct answer is **RAID array drive health**. Since the issue seems to be specific to the fileshare, the problem might be with the RAID array where the files are stored, affecting performance.\n\n- **Network utilization** has already been checked.\n- **Two-factor authentication** and **local drive space** are unrelated to the slowdown of the network fileshare."
    },
    {
        "question": "A virtual file server in the cloud is configured to automatically add compute resources during times of high load on the server. Which of the following describes this cloud feature?",
        "options": [
            "File synchronization",
            "High availability",
            "Rapid elasticity",
            "Shared resources"
        ],
        "correct_answer": 3,
        "description": "The correct answer is **Rapid elasticity**. This cloud feature allows resources to automatically scale up or down based on demand, ensuring the server can handle high load periods without performance issues.\n\n- **File synchronization** refers to keeping files up to date across devices.\n- **High availability** ensures systems remain operational.\n- **Shared resources** is a general term for using common resources in a cloud environment."
    },
    {
        "question": "A technician is on site troubleshooting a customer's laptop. The technician needs to download a software update, but the company’s proxy is blocking updates. Which of the following would be the MOST appropriate action for the technician to take to get the update?",
        "options": [
            "Connect to a hotspot",
            "Request a traffic exemption",
            "Change the DNS address to 1.1.1.1",
            "Update the Group Policy settings"
        ],
        "correct_answer": 2,
        "description": "The correct answer is **Request a traffic exemption**. This will allow the technician to bypass the proxy's restrictions and download the update without violating company policies.\n\n- **Connecting to a hotspot** may bypass the proxy, but it's not the most appropriate solution in a controlled network environment.\n- **Changing the DNS address** will not help if the proxy is the source of the block.\n- **Updating the Group Policy settings** requires administrative privileges and is unlikely to solve the issue."
    },
    {
        "question": "An integrated webcam on a user's laptop broke, so a technician installed a temporary, external webcam. Since the external webcam installation, other users can only see part of the user's face during videoconferences. Which of the following BEST describes the reason for this issue?",
        "options": [
            "The webcam is not on a level surface.",
            "The webcam driver should be updated.",
            "The webcam is plugged into the wrong USB port.",
            "The webcam is not compatible with the OS."
        ],
        "correct_answer": 1,
        "description": "The correct answer is **The webcam is not on a level surface**. If only part of the user's face is visible, the webcam's physical positioning is likely causing the issue.\n\n- **Driver updates**, **USB port issues**, and **OS compatibility** would cause different issues such as the webcam not functioning properly, but not partial visibility."
    },
    {
        "question": "A network engineer recently deployed a new application server in a cloud environment. Which of the following should be implemented to prevent a single point of failure within the system?",
        "options": [
            "Rapid elasticity",
            "RAID",
            "High availability",
            "Shared resources"
        ],
        "correct_answer": 3,
        "description": "The correct answer is **High availability**. This ensures that the application server remains operational by providing redundancy and failover solutions, preventing a single point of failure.\n\n- **Rapid elasticity** is about scaling resources based on demand.\n- **RAID** provides redundancy for data storage but does not address server availability.\n- **Shared resources** refers to using common resources but doesn't ensure availability."
    },
#278-285
    {
        "question": "A user needs to transfer files from an Apple phone to a workstation. Which of the following connection types should the user utilize?",
        "options": [
            "USB-C",
            "Serial",
            "Lightning",
            "NFC"
        ],
        "correct_answer": 3,
        "description": "The correct answer is **Lightning**. Apple phones (such as iPhones) typically use Lightning connectors for wired connections to other devices like workstations.\n\n- **USB-C** is used in newer devices but not older Apple phones.\n- **Serial** and **NFC** are not relevant for file transfers from an iPhone."
    },
    {
        "question": "A technician is installing a USB Wi-Fi card. Which of the following would be the MOST appropriate way for the technician to receive the latest official drivers for the device?",
        "options": [
            "Download the drivers from the vendor's website.",
            "Allow the OS to install the drivers automatically.",
            "Utilize a third-party, non-OEM driver.",
            "Run the autoinstall CD."
        ],
        "correct_answer": 1,
        "description": "The correct answer is **Download the drivers from the vendor's website**. This ensures the technician gets the latest drivers directly from the manufacturer, which are often more updated than those found on CDs or installed automatically by the OS.\n\n- **Allowing the OS to install the drivers automatically** might not guarantee the latest version.\n- **Third-party drivers** may not be reliable, and **auto-install CDs** might contain outdated drivers."
    },
    {
        "question": "A user reports that all print jobs sent to a laser printer have random and incorrect characters throughout the pages. Which of the following actions should the technician do to resolve this issue?",
        "options": [
            "Replace the fuser.",
            "Adjust the rollers.",
            "Update the driver.",
            "Shake the toner."
        ],
        "correct_answer": 3,
        "description": "The correct answer is **Update the driver**. Random and incorrect characters are often caused by incorrect or outdated printer drivers, so updating the driver should resolve the issue.\n\n- **Replacing the fuser** or **adjusting rollers** are related to hardware issues, and **shaking the toner** won’t fix printing errors like this."
    },
    {
        "question": "An end user needs to upgrade the hard drive on a laptop and wants one that is fast and shock resistant. Which of the following is the BEST option for this end user?",
        "options": [
            "Hybrid HHD/SSD",
            "5,400rpm HDD",
            "7,200rpm HDD",
            "NVMe SDD"
        ],
        "correct_answer": 4,
        "description": "The correct answer is **NVMe SSD**. NVMe solid-state drives are faster and more shock resistant than traditional hard drives or hybrid drives.\n\n- **Hybrid HHD/SSD** has some speed improvements but is still slower and less shock resistant than a full SSD.\n- **5,400rpm** and **7,200rpm HDDs** are traditional hard drives that are less shock resistant and slower."
    },
    {
        "question": "Which of the following connectors can be plugged into a Thunderbolt 3 port on a laptop?",
        "options": [
            "miniUSB",
            "microUSB",
            "USB-A",
            "USB-C"
        ],
        "correct_answer": 4,
        "description": "The correct answer is **USB-C**. Thunderbolt 3 ports use the USB-C connector, allowing Thunderbolt or USB-C devices to be connected to the laptop.\n\n- **miniUSB**, **microUSB**, and **USB-A** connectors are not compatible with Thunderbolt 3 ports."
    },
    {
        "question": "A technician is attempting to fix a computer that does not turn on when the power button is pressed. Which of the following should the technician perform NEXT to troubleshoot the issue?",
        "options": [
            "Verify the output voltages from the power supply unit.",
            "Open the computer cabinet and replace the power button.",
            "Remove and reconnect all cables that are plugged into the motherboard.",
            "Reseat the power cable and confirm the outlet is providing energy."
        ],
        "correct_answer": 4,
        "description": "The correct answer is **Reseat the power cable and confirm the outlet is providing energy**. Before investigating internal components, it’s important to ensure that the power cable is properly connected and that the outlet is working.\n\n- Checking the **output voltages**, **replacing the power button**, or **reconnecting cables** would be the next steps if the basic power connections are confirmed to be functional."
    },
#286-299
    {
        "question": "Which of the following cables should be used to terminate ST connectors on each end?",
        "options": [
            "Optical fiber",
            "Coaxial",
            "Shielded twisted pair",
            "HDMI"
        ],
        "correct_answer": 1,
        "description": "The correct answer is **Optical fiber**. ST (Straight Tip) connectors are used with optical fiber cables for high-speed data transmission.\n\n- **Coaxial**, **shielded twisted pair**, and **HDMI** are not compatible with ST connectors."
    },
    {
        "question": "Which of the following cloud-computing concepts describes an application that is hosted on the internet but can be used and configured as needed internally per organization?",
        "options": [
            "Hybrid cloud",
            "Public cloud",
            "IaaS",
            "SaaS",
            "PaaS"
        ],
        "correct_answer": 4,
        "description": "The correct answer is **SaaS** (Software as a Service). SaaS is a cloud computing concept where applications are hosted on the internet and provided to organizations, allowing them to use and configure it internally without managing the infrastructure."
    },
    {
        "question": "A user reports a tablet restarts on its own every five to ten minutes. In addition, the tablet has intermittent issues with charging. The technician gives the user a new power adapter and charging cable, and the technician also tries resetting the OS, but the issue persists. Which of the following is the MOST likely cause of the issue?",
        "options": [
            "Water damage",
            "Incorrect OS version",
            "Faulty battery",
            "Damaged charging port"
        ],
        "correct_answer": 3,
        "description": "The correct answer is **Faulty battery**. Restarting and charging issues are commonly caused by a malfunctioning or defective battery."
    },
    {
        "question": "A technician verifies the slow boot time and slow OS performance of a tower server with a RAID 5 on a PCIe RAID card that does not support hot swapping. Which of the following steps should the technician take NEXT to verify RAID health?",
        "options": [
            "Verify S.M.A.R.T. operation on the RAID card.",
            "Replace the failed drive while users are connected.",
            "Physically clean the HDDs and connectors.",
            "Shut down the server and check the RAID controller's status."
        ],
        "correct_answer": 4,
        "description": "The correct answer is **Shut down the server and check the RAID controller's status**. Since the RAID card does not support hot-swapping, the technician needs to power down the server to safely check the RAID controller’s status."
    },
    {
        "question": "A technician needs to implement a database in the cloud but does not want to manage any server infrastructure. Which of the following solutions would BEST meet this requirement?",
        "options": [
            "IaaS",
            "PaaS",
            "SaaS",
            "DaaS"
        ],
        "correct_answer": 2,
        "description": "The correct answer is **PaaS** (Platform as a Service). PaaS provides a platform that allows users to develop, run, and manage applications without dealing with the infrastructure."
    },
    {
        "question": "A technician receives an alert indicating all VMs are down. After some troubleshooting, the technician discovers the network is out of space. To resolve the issue, the technician decides to add more space. Which of the following network types will the technician be working with?",
        "options": [
            "SCSI",
            "NAC",
            "SAN",
            "WISP"
        ],
        "correct_answer": 3,
        "description": "The correct answer is **SAN** (Storage Area Network). A SAN is used to provide shared storage for VMs, and running out of space in the SAN can cause VMs to fail."
    },
    {
        "question": "A cloud engineer, who is designing a cloud architecture, needs to ensure the solution is able to immediately fail over to another region in case of an outage and also scale up in the event of high utilization. Which of the following should the engineer implement? (Choose two.)",
        "options": [
            "High availability",
            "Elasticity",
            "Cold storage",
            "Machine learning",
            "Metered utilization",
            "Virtualization"
        ],
        "correct_answer": [1, 2],
        "description": "The correct answers are **High availability** and **Elasticity**. High availability ensures failover in the event of an outage, and elasticity allows the system to scale up or down based on utilization."
    },
    {
        "question": "A user wants RAID to be configured on a desktop to allow the fastest speed and maximum storage capacity. Which of the following RAID types should a technician configure to accommodate this request?",
        "options": [
            "0",
            "1",
            "5",
            "10"
        ],
        "correct_answer": 1,
        "description": "The correct answer is **RAID 0**. RAID 0 provides maximum speed and storage capacity by striping data across multiple disks without redundancy."
    },
    {
        "question": "Which of the following printing initiatives would be BEST to accomplish environmentally friendly objectives?",
        "options": [
            "Requiring user authentication for printing",
            "Locking down printing to only certain individuals",
            "Modifying duplex settings to double-sided",
            "Changing the print quality settings to best"
        ],
        "correct_answer": 3,
        "description": "The correct answer is **Modifying duplex settings to double-sided**. Printing double-sided reduces paper usage, which supports environmental sustainability."
    },
    {
        "question": "A user calls the help desk about a 4K monitor that will not output an image from a desktop. The monitor was working previously but now shows a black screen with a message stating a signal is not detected. The desktop is connected via HDMI, and the monitor has an empty DVI port. Which of the following steps should the technician perform FIRST? (Choose two.)",
        "options": [
            "Check the version of the HDMI cable.",
            "Check the input source.",
            "Set up the desktop for DVI.",
            "Replace the HDMI cable.",
            "Install OS updates.",
            "Initiate a system restore."
        ],
        "correct_answer": [1, 2],
        "description": "The correct answers are **Check the version of the HDMI cable** and **Check the input source**. Ensuring that the correct input source is selected and that the HDMI cable version supports 4K output are essential first steps."
    },
    {
        "question": "A user's iPhone was permanently locked after several failed login attempts. Which of the following will restore access to the device?",
        "options": [
            "Fingerprint and pattern",
            "Facial recognition and PIN code",
            "Primary account and password",
            "Secondary account and recovery code"
        ],
        "correct_answer": 3,
        "description": "The correct answer is **Primary account and password**. Restoring access to a locked iPhone typically requires the user’s Apple ID (primary account) and password."
    },
    {
        "question": "While on a VoIP call, one user is unable to understand the other because the audio is breaking up. Which of the following BEST describes what is occurring on the call?",
        "options": [
            "High latency",
            "External interference",
            "No connectivity",
            "Port flapping"
        ],
        "correct_answer": 1,
        "description": "The correct answer is **High latency**. Audio breaking up during a VoIP call is typically caused by high latency, where there is a significant delay in data transmission."
    },
#305-315

    {
        "question": "A network technician is working to locate an end user's Cat 6 cable within a network rack. The server rack is poorly documented, and a cable management system has not been implemented. Which of the following would be the BEST tool to BEST identify the correct cable?",
        "options": [
            "Cable tester",
            "Network tap",
            "Toner probe",
            "Loopback plug"
        ],
        "correct_answer": 3,
        "description": "The correct answer is **Toner probe**. A toner probe is used to trace the cable from one end to the other, especially in environments where cables are not labeled or documented."
    },
    {
        "question": "A technician connects a new computer to the internet and then opens the wiring closet. Even though all of the wires are terminated, nothing in the wiring closet is labeled. Which of the following tools should the technician use to complete the task?",
        "options": [
            "Cable tester",
            "Loopback plug",
            "Toner probe",
            "Punchdown tool"
        ],
        "correct_answer": 3,
        "description": "The correct answer is **Toner probe**. The toner probe helps identify which wire corresponds to which port or device, making it ideal in situations where wires are not labeled."
    },
    {
        "question": "An IT technician is inspecting the internal components of a desktop computer to assess a suspected power issue with the motherboard. Which of the following connectors should the IT technician inspect further?",
        "options": [
            "RJ45",
            "Straight tip",
            "DB9",
            "Molex"
        ],
        "correct_answer": 4,
        "description": "The correct answer is **Molex**. Molex connectors provide power to the internal components of a desktop, such as hard drives and optical drives."
    },
{
    "question": "A systems administrator is attempting to resolve a ticket regarding an issue with an email server. The administrator is covering for a coworker who was previously working on the ticket. The coworker already gathered facts about the issue and spoke with users concerning their missing emails. The coworker also discovered the email server's retention policy was updated shortly before users first noticed the issue. Which of the following should the systems administrator do NEXT to resolve the email issue?",
    "options": [
        "Escalate the ticket to a higher level to resolve the email server issue.",
        "Test a theory to determine the cause of the email server issue.",
        "Establish a theory of probable cause for the email server issue.",
        "Create a plan of action to resolve the email server issue."
    ],
    "correct_answer": 3,
    "description": "The correct answer is **Establish a theory of probable cause for the email server issue**. After gathering facts, the next step is to establish a theory of probable cause before testing it or taking further actions."
},
    {
        "question": "A user uploads a file to a storage location that is accessible via a web browser and a client application. The user's coworkers can access the file as well. The service that the file is stored with is provided by a third party for a monthly fee. The third party's service is available to any business or consumer who would like to use the service. Which of the following BEST describes the type of service that is in use?",
        "options": [
            "Hybrid cloud",
            "Infrastructure as a service",
            "Public cloud",
            "Private cloud"
        ],
        "correct_answer": 3,
        "description": "The correct answer is **Public cloud**. A public cloud is a service offered by third parties and available to businesses or consumers for a fee."
    },
    {
        "question": "Which of the following frequency bands do 802.11b and 802.11g operate in?",
        "options": [
            "1GHz",
            "2.4GHz",
            "5GHz",
            "6GHz"
        ],
        "correct_answer": 2,
        "description": "The correct answer is **2.4GHz**. Both 802.11b and 802.11g operate in the 2.4GHz frequency band."
    },
    {
        "question": "Which of the following protocols operates without a port number assignment?",
        "options": [
            "SNMP",
            "TCP",
            "SSH",
            "DHCP"
        ],
        "correct_answer": 2,
        "description": "The correct answer is **TCP**. TCP is a transport protocol and does not have a specific port number assigned to it. Instead, it is used in conjunction with various port numbers for specific applications."
    },
    {
        "question": "A desktop support technician receives an escalated ticket regarding a computer that displays the following message upon booting up: The amount of system memory has changed. Which of the following components is failing?",
        "options": [
            "GPU",
            "HDD",
            "RAM",
            "CPU"
        ],
        "correct_answer": 3,
        "description": "The correct answer is **RAM**. This message typically indicates an issue with the system memory (RAM), such as a faulty or improperly seated RAM module."
    },
    {
        "question": "Using the output below:\n\nIPv4 Address: 172.25.1.39 -\n\nSubnet Mask: 255.255.255.0 -\n\nRouter: 172.25.1.252 -\n\nName Server: 172.25.1.4 -\n\nWhich of the following is the default gateway?",
        "options": [
            "172.25.1.252",
            "172.25.1.39",
            "172.25.1.4",
            "255.255.255.0"
        ],
        "correct_answer": 1,
        "description": "The correct answer is **172.25.1.252**. The default gateway is the IP address that routes traffic to other networks, and in this case, it is the router."
    },
    {
        "question": "A technician is working on a critical warehouse machine that will not turn on. The technician has determined the power supply for the machine failed. The warehouse manager is looking for a solution that will prevent downtime in the future. Which of the following devices should the technician install to meet this requirement?",
        "options": [
            "Grounded power supply",
            "Modular power supply",
            "220V power supply",
            "Redundant power supply"
        ],
        "correct_answer": 4,
        "description": "The correct answer is **Redundant power supply**. A redundant power supply provides backup power in case of a failure, preventing downtime."
    },
    {
        "question": "A help desk technician receives a ticket stating a printer has jammed several times today. The technician removes the jammed paper and notices the paper supply is low and the paper in the tray is wrinkled. Which of the following MOST likely caused the paper jams?",
        "options": [
            "High latency",
            "Page orientation",
            "Driver mismatch",
            "Multipage misfeed"
        ],
        "correct_answer": 4,
        "description": "The correct answer is **Multipage misfeed**. Wrinkled and low paper supplies can lead to multiple pages feeding incorrectly into the printer, causing jams."
    },
#316-329


    {
        "question": "A user reported that a laptop would no longer turn on after the battery was depleted, even though the laptop was charged the night before. An on-site technician was dispatched with a spare laptop and verified that the AC adapter and power cord were functional. Which of the following was the MOST likely cause of the issue?",
        "options": [
            "Swollen battery",
            "Calibration corruption",
            "Excessive wattage",
            "Damaged port"
        ],
        "correct_answer": 1,
        "description": "The correct answer is **Swollen battery**. A swollen battery can cause power issues and prevent the laptop from turning on."
    },
    {
        "question": "A technician installed a new SSD in a computer that needed additional storage. The technician properly formatted and partitioned the drive. The BIOS recognizes the drive, but the drive does not appear as an available drive in My Computer. Which of the following should the technician do to resolve the issue?",
        "options": [
            "Replace the defective drive.",
            "Make sure a drive letter has been assigned.",
            "Check Device Manager.",
            "Initialize the disk in Disk Management."
        ],
        "correct_answer": 4,
        "description": "The correct answer is **Initialize the disk in Disk Management**. If the drive is not appearing in My Computer, it may need to be initialized in Disk Management."
    },
    {
        "question": "A user is unable to access the internet on a PC. A technician examines the PC and runs the following commands: ipconfig /all, ping 8.8.8.8, ping comptia.org. Which of the following steps in the troubleshooting process does this series of commands represent?",
        "options": [
            "Establish a theory.",
            "Verify full system functionality.",
            "Establish a plan of action.",
            "Identify the problem."
        ],
        "correct_answer": 4,
        "description": "The correct answer is **Identify the problem**. Running these commands helps in identifying where the issue might be occurring in the network connectivity."
    },
    {
        "question": "A technician installed a new router at a small office. After the installation, the technician notices that all devices have a 169.254.x.x IP address. Printers and fileshares are still working, but PCs cannot access the internet. Which of the following should the technician configure on the router to enable devices to connect to the internet?",
        "options": [
            "APIPA",
            "DNS",
            "DHCP",
            "SMB"
        ],
        "correct_answer": 3,
        "description": "The correct answer is **DHCP**. Devices with a 169.254.x.x IP address indicate that they are not receiving an IP address from the DHCP server. Configuring DHCP on the router will resolve this issue."
    },
    {
        "question": "A technician is troubleshooting a laptop that shuts down intermittently. When the laptop is repositioned, the technician notices a noise coming from inside of it. The technician removes the bottom cover. Which of the following should the technician do NEXT?",
        "options": [
            "Turn on the laptop and move it again to replicate the issue.",
            "Reseat the memory modules and the SSD.",
            "Remove the internal battery and look for loose parts.",
            "Inspect the connections for a damaged cable."
        ],
        "correct_answer": 3,
        "description": "The correct answer is **Remove the internal battery and look for loose parts**. The noise could be due to loose or damaged components inside the laptop."
    },
    {
        "question": "Which of the following would MOST likely be used to extend the life of a device?",
        "options": [
            "Battery backup",
            "Electrostatic discharge mat",
            "Proper ventilation",
            "Green disposal"
        ],
        "correct_answer": 3,
        "description": "The correct answer is **Proper ventilation**. Proper ventilation helps prevent overheating and extends the life of the device."
    },
    {
        "question": "A user is attempting to connect a streaming media device to a hotel's free wireless internet. However, the user is unable to pass through the captive portal. Which of the following would MOST likely allow the user to connect the device to the internet?",
        "options": [
            "Connecting to the hotspot on the user's device",
            "Disabling the Wi-Fi security on the device",
            "Asking the hotel to disable the captive portal on the Wi-Fi",
            "Adjusting the date and time stamps on the device to reflect another country"
        ],
        "correct_answer": 1,
        "description": "The correct answer is **Connecting to the hotspot on the user's device**. This can bypass the captive portal on the hotel's network by using an alternative connection method."
    },
    {
        "question": "A user working in the field reported the GPS stopped working on a phone. The user's older, in-car GPS continued to function. Later, the user reported that the phone's GPS started working again. Which of the following MOST likely caused the phone's GPS to fail?",
        "options": [
            "The cell phone was in conservation mode.",
            "The cell phone had lost service to the carrier.",
            "The cell phone received a firmware update.",
            "The cell phone had overheated."
        ],
        "correct_answer": 2,
        "description": "The correct answer is **The cell phone had lost service to the carrier**. Loss of service can impact GPS functionality, and it might be restored once the service is re-established."
    },
    {
        "question": "A technician responds to a user who has reported that a laptop is too hot. The technician notices the laptop is not able to sit level on the workspace. Which of the following BEST describes the issue with the laptop?",
        "options": [
            "The docking station is improperly installed.",
            "The hard drive is disconnected.",
            "The CPU fan is too powerful.",
            "The battery is damaged."
        ],
        "correct_answer": 4,
        "description": "The correct answer is **The battery is damaged**. A damaged battery can cause the laptop to become uneven and potentially overheat."
    },
    {
        "question": "Users report that all copies produced on a copier have a solid black line, but printing is unaffected. Which of the following is the MOST likely cause?",
        "options": [
            "Failing imaging drum",
            "A scratch on the scanning bed",
            "Bad output tray",
            "Damaged fuser"
        ],
        "correct_answer": 2,
        "description": "The correct answer is **A scratch on the scanning bed**. A solid black line on copies is typically caused by a scratch or other defect on the scanning bed."
    },
    {
        "question": "A desktop technician has received reports that a user's PC is slow to load programs and saved files. The technician investigates and discovers an older HDD with adequate free space. Which of the following should the technician use to alleviate the issue first?",
        "options": [
            "Disk Management",
            "Disk Defragment",
            "Disk Cleanup",
            "Device Manager"
        ],
        "correct_answer": 2,
        "description": "The correct answer is **Disk Defragment**. Fragmented files on an HDD can slow down system performance, so defragmenting the disk can help improve speed."
    },
#331-350
    {
        "question": "A user is experiencing an issue when trying to use a camera on a corporate mobile device to take pictures. The camera on the device is working. However, when the user tries to access the pictures via a USB cable connected to a PC, the user is unable to copy the pictures to the PC. Which is the following BEST describes the likely cause of the issue?",
        "options": [
            "Settings are preventing the transfer of data from the device's camera.",
            "A technician needs to change the camera settings on the device.",
            "The device has corrupted picture files due to an update.",
            "The device needs to have the OS reinstalled."
        ],
        "correct_answer": 1,
        "description": "The correct answer is **Settings are preventing the transfer of data from the device's camera**. The issue likely stems from settings that restrict data transfer, even though the camera itself is functioning."
    },
    {
        "question": "A technician who works in a high-security environment needs to set up a laptop with triple monitors for a new security employee. All USB ports are disabled due to security policies. Which of the following should the technician do to BEST meet the requirements?",
        "options": [
            "Install a splitter cable.",
            "Install a discrete graphics card.",
            "Use an HDMI switch.",
            "Implement a docking station."
        ],
        "correct_answer": 4,
        "description": "The correct answer is **Implement a docking station**. A docking station can support multiple monitors and does not require USB ports if it connects through other interfaces like DisplayPort or HDMI."
    },
    {
        "question": "A technician is upgrading a desktop’s storage with the fastest option available. The desktop's motherboard is equipped with SATA III, NVMe, and IDE. Which of the following should the technician choose for the best performance?",
        "options": [
            "PCIe SSD connected via NVMe interface",
            "3.5in (8.9cm) 10.000rpm HDD connected via IDE interface",
            "M.2 SSD connected via SATA interface",
            "2.5in (6.35cm) SSD connected via SATA interface"
        ],
        "correct_answer": 1,
        "description": "The correct answer is **PCIe SSD connected via NVMe interface**. NVMe SSDs provide the highest performance compared to SATA and IDE interfaces."
    },
    {
        "question": "A technician needs to provide data redundancy on a user’s workstation. Which of the following RAID levels provides redundancy with the FEWEST disks?",
        "options": [
            "RAID 0",
            "RAID 1",
            "RAID 5",
            "RAID 10"
        ],
        "correct_answer": 2,
        "description": "The correct answer is **RAID 1**. RAID 1 provides redundancy with only two disks by mirroring the data."
    },
    {
        "question": "A user's wireless laptop stopped working. A technician replaced the wireless card, but the wireless range is now limited. Which of the following should the technician perform NEXT?",
        "options": [
            "Verify the antenna's connection.",
            "Switch from a 2.4GHz band to a 5GHz band.",
            "Change the channels of the Wi-Fi card settings.",
            "Upgrade the wireless driver."
        ],
        "correct_answer": 1,
        "description": "The correct answer is **Verify the antenna's connection**. Limited range after a wireless card replacement often indicates an issue with the antenna connection."
    },
    {
        "question": "A technician installed a Cat 5 UTP cable approximately 275ft (84m) from a network switch in an office to a workstation located on a factory floor. The technician sees both a flashing green LED and a flashing orange LED on the workstation's NIC. Which of the following should the technician do FIRST?",
        "options": [
            "Check for loose connections, pinched bends, and physical damage.",
            "Install a powered hub as close as possible to the halfway point in the Cat 5 UTP cable run.",
            "Replace the entire run of Cat 5 UTP cable with Cat 5 STP cable.",
            "Upgrade the entire cable run to multimode fiber."
        ],
        "correct_answer": 1,
        "description": "The correct answer is **Check for loose connections, pinched bends, and physical damage**. This is the first step to ensure there are no physical issues with the cable installation."
    },
    {
        "question": "In a SOHO environment, a user wants to make sensitive scanned documents available to other users on the domain. The logs need to indicate who accessed the documents and at what time they were accessed. Which of the following settings should a technician set up on the MFP device?",
        "options": [
            "Scan to email",
            "ADF tray",
            "PCL",
            "SMB share"
        ],
        "correct_answer": 4,
        "description": "The correct answer is **SMB share**. Setting up an SMB share will allow access control and logging for document access."
    },
    {
        "question": "A user reports that a display is slow to turn on, and the colors are distorted and discolored. Once the display turns on, it appears to have lines going through the image and intermittently goes blank. Which of the following is the most likely cause of the issue?",
        "options": [
            "Incorrect data source",
            "Incorrect resolution settings",
            "Physical cabling issues",
            "Incorrect refresh rate",
            "Display burn-in"
        ],
        "correct_answer": 3,
        "description": "The correct answer is **Physical cabling issues**. Problems with the display’s physical connections can cause the symptoms described."
    },
    {
        "question": "A regularly used laser printer is printing vertical lines on each page. Which of the following should the technician do first?",
        "options": [
            "Lower the printing contrast.",
            "Change the paper type.",
            "Install a new fuser.",
            "Replace the toner cartridge."
        ],
        "correct_answer": 4,
        "description": "The correct answer is **Replace the toner cartridge**. Vertical lines on prints often indicate a problem with the toner cartridge."
    },
    {
        "question": "A technician recently installed a new printer that is being shared over the network via a 64-bit Windows Print Server. Two users, who have computers with a legacy OS, are unable to print to this new printer. Which of the following should the technician do to resolve this issue?",
        "options": [
            "Enable 32-bit drivers on the Print Server.",
            "Enable Print Spooler and restart the computer.",
            "Run Windows Update on the users' computers.",
            "Update the computers to a 64-bit driver."
        ],
        "correct_answer": 1,
        "description": "The correct answer is **Enable 32-bit drivers on the Print Server**. Legacy OS systems require 32-bit drivers to print to a 64-bit print server."
    },
    {
        "question": "A technician is replacing a failed drive in a RAID 5 array. Which of the following is the first step the technician should take before hot swapping the drive out of the array?",
        "options": [
            "Document the replacement date.",
            "Shut down the array.",
            "Safely dispose of the failed drive.",
            "Perform a full backup."
        ],
        "correct_answer": 4,
        "description": "The correct answer is **Perform a full backup**. Ensuring that a full backup is completed is crucial before performing any hardware replacements in a RAID array."
    },
    {
        "question": "An administrator notices that on an intermittent basis the virtual machines are running slowly. The virtual machines are correctly sized, and the hardware has enough free resources to cope with demand. Which of the following is most likely the cause?",
        "options": [
            "The physical servers are not able to draw enough power.",
            "The physical servers do not have enough network bandwidth.",
            "The physical servers are throttling due to overheating.",
            "The physical servers are contending for resources."
        ],
        "correct_answer": 3,
        "description": "The correct answer is **The physical servers are throttling due to overheating**. Intermittent performance issues may occur when the physical servers are overheating and throttling their performance."
    },
        {
            "question": "Which of the following technologies can be used to harden guest virtual machines?",
            "options": [
                "Containerization",
                "Network isolation",
                "Resource reservation",
                "vTPM"
            ],
            "correct_answer": 4,
            "description": "The correct answer is **vTPM**. Virtual Trusted Platform Module (vTPM) helps in hardening virtual machines by providing a secure cryptographic foundation."
        },
    #351-380
    {
        "question": "A technician is attempting to connect the wired LANs at two nearby buildings by installing a wireless point-to-point connection. Which of the following should the technician consider?",
        "options": [
            "NFC protocol data rate",
            "RFID frequency range",
            "Bluetooth version compatibility",
            "Allowable limits for transmit power"
        ],
        "correct_answer": 4,
        "description": "The correct answer is **Allowable limits for transmit power**. For a wireless point-to-point connection between buildings, it is important to ensure that the transmit power complies with local regulations and is sufficient to cover the distance between the two points.\n\n- **NFC protocol data rate**: NFC is designed for close-range communication (within a few centimeters), making it irrelevant for connecting LANs over a distance.\n- **RFID frequency range**: RFID is used primarily for tracking and identification, not for establishing wireless LAN connections.\n- **Bluetooth version compatibility**: Bluetooth is designed for short-range communication, generally within a few meters, and is not suitable for long-distance LAN connections."
    },
    {
        "question": "An analyst has replaced the motherboard in a desktop computer that previously overheated. The analyst presses the power button, hears three beeps, and sees the screen is black. Which of the following is the best action for the analyst to take to fix this issue?",
        "options": [
            "Replace the power supply.",
            "Reseat the RAM.",
            "Reattach the hard drive.",
            "Flash the BIOS."
        ],
        "correct_answer": 2,
        "description": "The correct answer is **Reseat the RAM**. The three beeps typically indicate a memory-related issue, such as improperly seated RAM, so reseating the RAM is the best course of action.\n\n- **Replace the power supply**: If the power supply were the issue, the system likely wouldn’t power on at all.\n- **Reattach the hard drive**: The hard drive isn’t involved in POST, so this isn’t related to the issue.\n- **Flash the BIOS**: This step wouldn’t be necessary for a memory error, which is the likely cause based on the beep code."
    },
    {
        "question": "A technician is troubleshooting a network issue and needs to check the status of a local network device in the least disruptive manner possible. Which of the following tools should the technician use to accomplish this task?",
        "options": [
            "Network tap",
            "Cable tester",
            "Multimeter",
            "Tone generator"
        ],
        "correct_answer": 1,
        "description": "The correct answer is **Network tap**. A network tap allows monitoring of network traffic without disrupting communication on the network.\n\n- **Cable tester**: This is used to check the functionality of network cables, not to monitor a device's network status.\n- **Multimeter**: A multimeter is used for electrical testing, not for network diagnostics.\n- **Tone generator**: This helps trace cables, but it doesn’t monitor network status."
    },
    {
        "question": "A technician is working to replace a single DDR3 RAM module on a laptop that has two occupied slots. When the technician tries to turn on the laptop, the computer starts beeping and does not pass POST. The technician double-checks the newly installed RAM and notices a motherboard message indicating low voltage. Which of the following is the most likely cause of this issue?",
        "options": [
            "Faulty power adapter",
            "Incorrect BIOS settings",
            "Failing CMOS battery",
            "Unsupported memory"
        ],
        "correct_answer": 4,
        "description": "The correct answer is **Unsupported memory**. A voltage mismatch can indicate that the RAM is not supported by the laptop’s motherboard.\n\n- **Faulty power adapter**: This would cause power issues, not low memory voltage errors.\n- **Incorrect BIOS settings**: BIOS settings typically don’t cause this specific error unless overclocking is involved.\n- **Failing CMOS battery**: A dead CMOS battery would affect the system clock and BIOS settings, not cause memory voltage issues."
    },
    {
        "question": "A technician is creating a new RAID array for a customer. After interviewing the customer, the technician decides to implement a RAID array of striping without parity. Which of the following reasons would lead the technician to choose striping without parity instead of striping with parity?",
        "options": [
            "Uptime is the customer's biggest concern.",
            "Speed is the most important consideration.",
            "Redundancy and speed are equally important.",
            "Available storage space needs to be maximized."
        ],
        "correct_answer": 2,
        "description": "The correct answer is **Speed is the most important consideration**. RAID 0 (striping without parity) improves read/write speed but offers no redundancy.\n\n- **Uptime is the customer's biggest concern**: If uptime were critical, RAID 1 or RAID 5 with redundancy would be a better choice.\n- **Redundancy and speed are equally important**: RAID 1 or RAID 5 would provide both redundancy and speed.\n- **Available storage space needs to be maximized**: While RAID 0 maximizes available space, speed is its primary benefit."
    },
    {
        "question": "A classroom projector, which is turned on, displays a flashing LED code but does not have any video output. Which of the following should a technician do to resolve the issue?",
        "options": [
            "Replace the bulb.",
            "Adjust the input resolution.",
            "Clean the air filter.",
            "Change the input source."
        ],
        "correct_answer": 1,
        "description": "The correct answer is **Replace the bulb**. A flashing LED code often indicates that the projector bulb has failed and needs to be replaced.\n\n- **Adjust the input resolution**: This would affect the quality of the image, not the absence of video output.\n- **Clean the air filter**: While important for maintenance, this wouldn’t cause the video to stop working.\n- **Change the input source**: Changing the input source wouldn’t resolve the issue if the projector isn’t displaying any output at all."
    },
    {
        "question": "A user is having difficulty using a personal all-in-one printer. When the user scans a single-page document in flatbed mode, the scan appears correctly; however, when using the printer's document feeder, the scan has a vertical line going across the page. Which of the following should a technician perform FIRST to resolve this issue?",
        "options": [
            "Replace the printer's ADF.",
            "Install a pickup roller replacement kit.",
            "Clean the separation pad.",
            "Use a microfiber cloth to clean the glass."
        ],
        "correct_answer": 4,
        "description": "The correct answer is **Use a microfiber cloth to clean the glass**. A vertical line on scans is commonly caused by dirt or debris on the scanner glass, particularly where the document feeder reads the pages.\n\n- **Replace the printer's ADF**: The issue is more likely related to a dirty glass, not a faulty ADF.\n- **Install a pickup roller replacement kit**: Pickup rollers help move paper through the printer but don’t affect scan quality.\n- **Clean the separation pad**: This helps with paper handling, not scanning quality."
    },
    {
        "question": "A user tries to turn on a computer but gets the following error message: Bootable device not found. The computer had no issues yesterday. Which of the following is the most likely reason for this error?",
        "options": [
            "The HDD is malfunctioning.",
            "The mouse and keyboard are not connected.",
            "A misconfigured boot device is in the BIOS.",
            "The network cable is unplugged."
        ],
        "correct_answer": 3,
        "description": "The correct answer is **A misconfigured boot device is in the BIOS**. This error commonly occurs when the BIOS settings are incorrect, pointing to the wrong boot device.\n\n- **The HDD is malfunctioning**: While possible, this isn’t as likely as a BIOS misconfiguration unless there are other signs of drive failure.\n- **The mouse and keyboard are not connected**: This would not cause a 'bootable device not found' error.\n- **The network cable is unplugged**: This would only affect internet connectivity, not the system’s boot process."
    },
    {
        "question": "A technician receives a smartphone that has been experiencing screen-related issues. The display is barely visible, and the battery indicates the charge level is very low. The technician connects the device to a power source, but the screen remains dim. Which of the following should the technician perform FIRST to resolve the issue?",
        "options": [
            "Enable airplane mode on the smartphone.",
            "Reset the smartphone to factory settings.",
            "Manually restart the smartphone.",
            "Remove and reinsert the smartphone's battery."
        ],
        "correct_answer": 3,
        "description": "The correct answer is **Manually restart the smartphone**. Restarting the smartphone is a quick and non-invasive step to resolve screen-related issues.\n\n- **Enable airplane mode on the smartphone**: This will disable network connectivity but won’t address the screen issue.\n- **Reset the smartphone to factory settings**: This is a more drastic measure and should only be done after other troubleshooting steps.\n- **Remove and reinsert the smartphone's battery**: While possible, this is less likely needed for a screen issue and can be avoided by a restart."
    },
    {
        "question": "A user tripped on an Ethernet cable and disconnected it from the wall jack. A technician visually inspects the cable and notices that the plastic prong on the connector of the cable is completely missing. Which of the following tools should the technician use to resolve this issue? (Choose two.)",
        "options": [
            "Cable stripper",
            "Network crimper",
            "Toner probe",
            "Punchdown tool",
            "Multimeter",
            "Loopback plug"
        ],
        "correct_answer": [1, 2],
        "description": "The correct answers are **Cable stripper** and **Network crimper**. The technician would need a cable stripper to prepare the cable and a network crimper to attach a new RJ45 connector to the Ethernet cable.\n\n- **Toner probe**: This tool is used to trace cables but won’t help repair the connector.\n- **Punchdown tool**: This is used for terminating cables at a patch panel or keystone jack, not for repairing connectors.\n- **Multimeter**: A multimeter measures electrical signals and won’t fix the physical issue.\n- **Loopback plug**: This is used to test network connectivity, not repair connectors."
    },
    {
        "question": "A customer purchased an active touch pen for a tablet PC. After the customer used the pen for a few days, it stopped working. Which of the following is most likely causing the issue?",
        "options": [
            "The tablet screen is scratched.",
            "The pen software is out of date.",
            "The pen batteries need recharging.",
            "Software updates disabled the pen."
        ],
        "correct_answer": 3,
        "description": "The correct answer is **The pen batteries need recharging**. Active touch pens typically have batteries that need to be charged, and if the pen stops working, it’s likely because the battery has drained.\n\n- **The tablet screen is scratched**: A scratched screen wouldn’t prevent the pen from working entirely.\n- **The pen software is out of date**: Outdated software could cause issues, but a dead battery is more likely if the pen was working initially.\n- **Software updates disabled the pen**: While possible, this is less common than a battery issue."
    },
    {
        "question": "An IT technician is working on a help desk ticket concerning a user's inability to create a virtual machine. The technician has already checked the RAM and HDD space in the user's machine. Which of the following settings should the technician check next to help troubleshoot the issue?",
        "options": [
            "BitLocker",
            "MSConfig",
            "BIOS",
            "Secure Boot"
        ],
        "correct_answer": 3,
        "description": "The correct answer is **BIOS**. Virtualization settings are typically controlled in the BIOS, and if virtualization isn’t enabled, the user won’t be able to create virtual machines.\n\n- **BitLocker**: This is for drive encryption and wouldn’t affect the ability to create virtual machines.\n- **MSConfig**: This tool is used to manage startup programs and services, not virtualization.\n- **Secure Boot**: This is a BIOS feature that ensures only trusted software is loaded but isn’t directly related to virtualization."
    },
    {
        "question": "Isolating email attachments in a safe place until the attachments can be scanned for malware is defined as:",
        "options": [
            "An approve listing.",
            "A screened subnet.",
            "Cross-platform virtualization.",
            "Sandboxing."
        ],
        "correct_answer": 4,
        "description": "The correct answer is **Sandboxing**. Sandboxing isolates potentially harmful files, such as email attachments, in a controlled environment where they can be tested for malware without risking the rest of the system.\n\n- **An approve listing**: This refers to allowing only certain approved programs to run, not isolating files.\n- **A screened subnet**: This is a portion of a network separated for security purposes, not for handling email attachments.\n- **Cross-platform virtualization**: This allows different operating systems to run on the same machine but doesn’t isolate email attachments."
    },
    #381-400


    {
        "question": "A systems administrator is working to ensure access to corporate laptops is limited to authorized users. The administrator has already implemented a password policy. Which of the following would be the best option to help the administrator secure the corporate resources?",
        "options": [
            "Trusted Platform Module",
            "Biometric scanner",
            "Laptop lock",
            "Encryption"
        ],
        "correct_answer": 2,
        "description": "The correct answer is **Biometric scanner**. Biometric authentication ensures that only authorized individuals, based on unique physical traits, can access the system.\n\n- **Trusted Platform Module**: TPM secures hardware-based encryption but does not directly limit user access.\n- **Laptop lock**: A laptop lock physically secures the device but does not protect it from unauthorized access.\n- **Encryption**: Encryption protects data, but biometric authentication directly controls user access."
    },
    {
        "question": "A technician is working with a vendor to resolve an issue that a user reported. The vendor indicates that the technician's next step is to update the firmware. Which of the following is the most important step the technician should take before proceeding?",
        "options": [
            "Verify the device is fully charged and connected to a power supply",
            "Ensure the device has adequate storage space for the update",
            "Verify administrative access on the device",
            "Export the user's settings so they can be imported after the upgrade"
        ],
        "correct_answer": 1,
        "description": "The correct answer is **Verify the device is fully charged and connected to a power supply**. Ensuring the device is adequately powered is crucial during firmware updates to prevent interruptions that could result in system failure or data corruption.\n\n- **Verify the device is fully charged and connected to a power supply**: Critical to avoid power loss during the update process.\n- **Ensure the device has adequate storage space for the update**: Necessary for successful updates, but power is more immediate.\n- **Verify administrative access on the device**: Important for making changes but less critical than ensuring the device is powered during the update.\n- **Export the user's settings so they can be imported after the upgrade**: Helpful for preserving settings but not as crucial as ensuring power stability."
    },
    {
        "question": "A user frequently edits large files and saves them locally on a laptop. The user has recently begun experiencing performance issues and needs a cost-effective hardware upgrade. Which of the following the best way to meet the user's requirements?",
        "options": [
            "Upgrade the memory.",
            "Upgrade to a larger GPU.",
            "Upgrade to an SSD.",
            "Upgrade to a faster CPU."
        ],
        "correct_answer": 3,
        "description": "The correct answer is **Upgrade to an SSD**. Solid-state drives provide faster read/write speeds, significantly improving performance when working with large files.\n\n- **Upgrade the memory**: While increasing memory may help, SSDs offer more noticeable performance improvements for storage-heavy tasks.\n- **Upgrade to a larger GPU**: A GPU upgrade is useful for graphics tasks but won’t necessarily improve general file handling.\n- **Upgrade to a faster CPU**: A CPU upgrade can improve performance but isn’t as cost-effective as switching to an SSD."
    },
    {
        "question": "A restaurant calls the support line about its 3in (2.5cm) point-of-sale printer that is only printing fully black receipts. Which of the following should the technician check in order to resolve the issue? (Choose two.)",
        "options": [
            "Power supply",
            "Humidity",
            "Rollers",
            "Fuser",
            "Heating element",
            "Room temperature"
        ],
        "correct_answer": [3, 5],
        "description": "The correct answers are **Rollers** and **Heating element**. For a thermal printer, issues with the rollers or heating element can lead to printing problems, such as fully black receipts. The rollers could be misaligned or dirty, affecting the paper feed and print quality, while the heating element may be malfunctioning and causing excessive heat to be applied.\n\n- **Power supply**: A faulty power supply would prevent the printer from functioning, not cause fully black prints.\n- **Humidity**: While humidity can affect some printers, it's unlikely the cause in this case.\n- **Fuser**: This component is typically found in laser printers, not thermal printers.\n- **Room temperature**: This is unlikely to cause fully black prints unless extremely high."
    },
    {
        "question": "Multiple users contact the help desk to report issues with the network fileshares. Files are accessible, but performance is very slow. Which of the following should a technician perform first?",
        "options": [
            "Defragment the files on the network share.",
            "Ask the users to perform a network speed test.",
            "Check the RAID drive status LEDs.",
            "Start the process of rebuilding the array."
        ],
        "correct_answer": 3,
        "description": "The correct answer is **Check the RAID drive status LEDs**. Checking RAID status is a quick way to determine if there are hardware issues causing performance degradation.\n\n- **Defragment the files on the network share**: This could help, but hardware issues should be ruled out first.\n- **Ask the users to perform a network speed test**: This might help diagnose network issues, but checking the RAID array is a more efficient first step.\n- **Start the process of rebuilding the array**: This should be done if RAID issues are detected, but it is not the first step."
    },
    {
        "question": "An engineer is installing a 500W power supply in a server that requires continuous availability. Which of the following is the most suitable type of power supply for the application?",
        "options": [
            "Redundant",
            "Modular",
            "Switched-mode",
            "Semi-modular"
        ],
        "correct_answer": 1,
        "description": "The correct answer is **Redundant**. Redundant power supplies ensure that if one power supply fails, another takes over to maintain continuous availability.\n\n- **Modular**: Modular power supplies allow customization of the cables used but don’t ensure continuous availability.\n- **Switched-mode**: This describes a power supply’s method of converting power, but it’s not a feature related to redundancy.\n- **Semi-modular**: Semi-modular power supplies offer limited customization and aren’t necessarily redundant."
    },
    {
        "question": "An internet service provider is delivering service through a copper medium with shared customer bandwidth. Which of the following services has most likely been installed?",
        "options": [
            "Fiber",
            "Cable",
            "NIC",
            "DSL"
        ],
        "correct_answer": 2,
        "description": "The correct answer is **Cable**. Cable internet uses copper wires and typically shares bandwidth among multiple customers in the same area.\n\n- **Fiber**: Fiber-optic connections use light rather than copper, providing faster, dedicated bandwidth.\n- **NIC**: This is a network interface card, which is hardware inside a computer, not a service type.\n- **DSL**: DSL also uses copper but usually provides dedicated bandwidth rather than shared."
    },
    {
        "question": "A help desk technician receives a ticket regarding a non-functioning printer. The ticket states the printer is no longer producing legible prints, and everything that prints appears as symbols. Which of the following is the most likely cause of this issue?",
        "options": [
            "Driver",
            "Fuser",
            "Access control list",
            "Malware"
        ],
        "correct_answer": 1,
        "description": "The correct answer is **Driver**. Incorrect or corrupted printer drivers can cause printed output to appear as symbols instead of readable text.\n\n- **Fuser**: A faulty fuser would affect print quality, not the content of what is printed.\n- **Access control list**: This restricts access to the printer, but wouldn’t affect print content.\n- **Malware**: Malware could cause many issues, but a driver issue is more likely when symbols are printed."
    },
    {
        "question": "A technician wants to stress test multiple applications while maintaining the ability to easily reset those environments back to the initial state. Which of the following is the best way to accomplish this task?",
        "options": [
            "Honeypot",
            "Hybrid cloud",
            "Sandbox",
            "Production network"
        ],
        "correct_answer": 3,
        "description": "The correct answer is **Sandbox**. A sandbox is an isolated environment where applications can be tested and reset easily to their original state without affecting the broader system.\n\n- **Honeypot**: A honeypot is used to lure attackers, not for application testing.\n- **Hybrid cloud**: A hybrid cloud combines public and private cloud environments, but isn’t typically used for isolated testing environments.\n- **Production network**: Testing applications on a production network could disrupt operations and isn’t easily reset."
    },
    {
        "question": "A technician replaces a laptop hard drive with an M.2 SSD. When the technician reboots the laptop, the laptop does not detect the SSD. Which of the following should the technician configure for the system?",
        "options": [
            "HSM",
            "Boot options",
            "UEFI settings",
            "TPM"
        ],
        "correct_answer": 3,
        "description": "The correct answer is **UEFI settings**. The UEFI firmware needs to be configured properly to detect the new M.2 SSD, especially if it requires specific boot settings or compatibility mode adjustments.\n\n- **HSM**: A hardware security module deals with encryption but doesn’t affect SSD detection.\n- **Boot options**: Adjusting boot options may be necessary, but configuring UEFI settings comes first.\n- **TPM**: Trusted Platform Module is related to encryption and security, not SSD detection."
    }

]
