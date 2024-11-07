questions_set_C = [
# 401-420


{
    "question": "A user's iPhone was permanently locked after several failed log-in attempts. Which of the following authentication methods are needed to restore access, applications, and data to the device?",
    "options": [
        "Fingerprint and pattern.",
        "Facial recognition and PIN code.",
        "Primary account and password.",
        "Recovery contact and recovery key."
    ],
    "correct_answer": 3,
    "description": "The correct answer is primary account and password. When an iPhone is permanently locked, the most common method of restoring access involves using the primary Apple account credentials (usually the Apple ID and password). \n\n- Fingerprint and pattern are used for unlocking but do not restore access after the device is locked permanently. \n- Facial recognition and PIN code are also local authentication methods but cannot restore data if the device is locked. \n- Recovery contact and key may be used for account recovery but are not as common as the primary account and password method."
},
{
    "question": "A company-owned mobile device is displaying a high number of ads, receiving data-usage limit notifications, and experiencing slow response. After checking the device, a technician notices the device has been jailbroken. Which of the following should the technician do next?",
    "options": [
        "Run an antivirus and enable encryption.",
        "Restore the defaults and reimage the corporate OS.",
        "Back up the files and do a system restore.",
        "Undo the jailbreak and enable an antivirus."
    ],
    "correct_answer": 2,
    "description": "The correct answer is restore the defaults and reimage the corporate OS. Jailbreaking compromises the integrity of the device, so restoring it to the corporate OS ensures security and removes unauthorized modifications. \n\n- Running an antivirus and enabling encryption would not fix the jailbreak issue or remove unauthorized apps. \n- Backing up files and doing a system restore could retain the jailbroken state. \n- Undoing the jailbreak alone is not sufficient for corporate devices that need to follow strict security policies."
},
{
    "question": "A remote user is experiencing issues with Outlook settings and asks a technician to review the settings. Which of the following can the technician use to access the user's computer remotely?",
    "options": [
        "VPN.",
        "RDP.",
        "RMM.",
        "SSH."
    ],
    "correct_answer": 3,
    "description": "The correct answer is RMM (Remote Monitoring and Management). RMM tools allow technicians to access and manage remote devices, including troubleshooting Outlook settings, without the need for direct user intervention. \n\n- VPN is for securing connections to a network but does not provide system access. \n- RDP is used to fully control a remote machine but is often limited in environments without prior configuration. \n- SSH is typically used for command-line access and is not ideal for GUI-based issues like Outlook settings."
},
{
    "question": "A workstation is displaying a message indicating that a user must exchange cryptocurrency for a decryption key. Which of the following is the best way for a technician to return the device to service safely?",
    "options": [
        "Run an AV scan.",
        "Reinstall the operating system.",
        "Install a software firewall.",
        "Perform a system restore.",
        "Comply with the on-screen instructions."
    ],
    "correct_answer": 2,
    "description": "The correct answer is reinstall the operating system. In cases of ransomware, it is safest to wipe the system and reinstall the OS to ensure that no malware remains on the device. \n\n- Running an AV scan may not fully remove the ransomware. \n- Installing a firewall does not address the existing ransomware. \n- A system restore may not remove the malware entirely. \n- Complying with the on-screen instructions would likely result in further issues and is not recommended."
},
{
    "question": "A salesperson's computer is unable to print any orders on a local printer that is connected to the computer. Which of the following tools should the salesperson use to restart the print spooler?",
    "options": [
        "Control Panel.",
        "Processes.",
        "Startup.",
        "Services."
    ],
    "correct_answer": 4,
    "description": "The correct answer is services. The print spooler is managed under the 'Services' application, where it can be restarted to resolve printing issues. \n\n- Control Panel allows access to printers but not to restart the spooler. \n- Processes are for viewing and managing running applications but do not provide access to the print spooler. \n- Startup relates to programs that start when the system boots up and is unrelated to the spooler."
},
{
    "question": "Which of the following helps ensure that a piece of evidence extracted from a PC is admissible in a court of law?",
    "options": [
        "Data integrity form.",
        "Valid operating system license.",
        "Documentation of an incident.",
        "Chain of custody."
    ],
    "correct_answer": 4,
    "description": "The correct answer is chain of custody. This refers to the documentation that tracks the handling and transfer of evidence, ensuring that it remains untampered and is admissible in court. \n\n- A data integrity form may be useful, but the chain of custody is more critical in legal situations. \n- An operating system license has no bearing on the admissibility of evidence. \n- Incident documentation is important but does not ensure the legal admissibility of evidence."
},
{
    "question": "A network technician is deploying a new machine in a small branch office that does not have a DHCP server. The new machine automatically receives the IP address of 169.254.0.2 and is unable to communicate with the rest of the network. Which of the following would restore communication?",
    "options": [
        "Static entry.",
        "ARP table.",
        "APIPA address.",
        "NTP specification."
    ],
    "correct_answer": 1,
    "description": "The correct answer is static entry. Without a DHCP server, the technician must manually assign a static IP address in the appropriate subnet for the machine to communicate with the network. \n\n- The ARP table is for resolving IP addresses to MAC addresses but will not fix the issue here. \n- The APIPA address (169.254.x.x) is automatically assigned when a device cannot reach a DHCP server, but it won't allow network communication. \n- NTP specification deals with time synchronization, not network communication."
},
{
    "question": "A user wants to back up a Windows 10 device. Which of the following should the user select?",
    "options": [
        "Devices and Printers.",
        "Email and Accounts.",
        "Update and Security.",
        "Apps and Features."
    ],
    "correct_answer": 3,
    "description": "The correct answer is Update and Security. Windows 10 includes backup options such as File History and system image backup under 'Update and Security'. \n\n- Devices and Printers is for managing connected hardware, not backups. \n- Email and Accounts manages email configurations and linked accounts. \n- Apps and Features is for uninstalling or modifying installed programs."
},
{
    "question": "A technician is unable to completely start up a system. The OS freezes when the desktop background appears, and the issue persists when the system is restarted. Which of the following should the technician do next to troubleshoot the issue?",
    "options": [
        "Disable applicable BIOS options.",
        "Load the system in safe mode.",
        "Start up using a flash drive OS and run System Repair.",
        "Enable Secure Boot and reinstall the system."
    ],
    "correct_answer": 2,
    "description": "The correct answer is load the system in safe mode. Safe mode starts the system with minimal drivers and processes, which can help troubleshoot whether a software or driver issue is causing the freeze. \n\n- Disabling BIOS options might affect hardware but won't resolve an OS freeze. \n- Starting up using a flash drive and running system repair could work but is a more drastic step compared to safe mode. \n- Enabling Secure Boot is a security feature and unrelated to this issue."
},
{
    "question": "A remote user contacts the help desk about an email that appears to be distorted. The technician is unsure what the user means and needs to view the email to assist with troubleshooting. Which of the following should the technician use to assist the user?",
    "options": [
        "VNC.",
        "SSH.",
        "VPN.",
        "RMM."
    ],
    "correct_answer": 1,
    "description": "The correct answer is VNC (Virtual Network Computing). VNC allows a technician to remotely access and view the user's desktop, including their email client, to troubleshoot the distortion. \n\n- SSH is for secure command-line access and would not help in viewing a graphical issue. \n- VPN is for secure network connections but does not provide remote desktop access. \n- RMM is for monitoring and managing devices but may not allow direct viewing of the user's screen."
},
{
    "question": "A technician is familiar with most personnel at a customer's location and has clearance to work unsupervised. Which of the following describes how the technician should handle personal communication while on site?",
    "options": [
        "Respond to calls and text messages while on site but not when working directly with personnel.",
        "Respond to calls and text messages only from family.",
        "Respond to calls and text messages only when an emergency situation requires a response.",
        "Respond to calls and text messages discreetly while on site."
    ],
    "correct_answer": 3,
    "description": "The correct answer is respond to calls and text messages only when an emergency situation requires a response. It is professional to minimize personal communication during work hours unless it's an emergency. \n\n- Responding while on site, even discreetly, can come across as unprofessional, especially when interacting with personnel. \n- Restricting responses only to family members isn't a sufficient guideline; the focus should be on emergencies."
},
{
    "question": "Which of the following Windows 10 editions is the most appropriate for a single user who wants to encrypt a hard drive with BitLocker?",
    "options": [
        "Professional.",
        "Home.",
        "Enterprise.",
        "Embedded."
    ],
    "correct_answer": 1,
    "description": "The correct answer is Professional. Windows 10 Professional supports BitLocker, which allows users to encrypt their hard drives. \n\n- Windows 10 Home does not include BitLocker. \n- Enterprise also supports BitLocker but is more suited for large organizations, not single users. \n- Embedded is a specialized edition not designed for general desktop use."
},
{
    "question": "A user connected a smartphone to a coffee shop's public Wi-Fi and noticed the smartphone started sending unusual SMS messages and registering strange network activity. A technician thinks a virus or other malware has infected the device. Which of the following should the technician suggest the user do to best address these security and privacy concerns? (Choose two.)",
    "options": [
        "Disable Wi-Fi autoconnect.",
        "Stay offline when in public places.",
        "Uninstall all recently installed applications.",
        "Schedule an antivirus scan.",
        "Reboot the device.",
        "Update the OS."
    ],
    "correct_answer": [1, 4],
    "description": "The correct answers are disable Wi-Fi autoconnect and schedule an antivirus scan. Disabling Wi-Fi autoconnect prevents the device from automatically connecting to insecure public networks, while running an antivirus scan can detect and remove malware. \n\n- Staying offline in public is a precaution but not a solution. \n- Uninstalling applications is only relevant if one of them is responsible for the infection. \n- Rebooting the device may not solve the issue entirely. \n- Updating the OS is good for security but does not address immediate threats."
},
{
    "question": "In an organization with a standardized set of installed software, a developer submits a request to have new software installed. The company does not currently have a license for this software, but the developer already downloaded the installation file and is requesting that the technician install it. The developer states that the management team approved the business use of this software. Which of the following is the best action for the technician to take?",
    "options": [
        "Contact the software vendor to obtain the license for the user, and assist the user with installation once the license is purchased.",
        "Run a scan on the downloaded installation file to confirm that it is free of malicious software, install the software, and document the software installation process.",
        "Indicate to the developer that formal approval is needed; then, the IT team should investigate the software and the impact it will have on the organization before installing the software.",
        "Install the software and run a full system scan with antivirus software to confirm that the operating system is free of malicious software."
    ],
    "correct_answer": 3,
    "description": "The correct answer is indicate to the developer that formal approval is needed; then, the IT team should investigate the software and the impact it will have on the organization before installing the software. Proper approval ensures that the software is vetted for security and compliance before use. \n\n- Contacting the vendor may be necessary later, but the first step is to follow internal procedures. \n- Scanning the file is good practice, but formal approval should come first. \n- Installing the software without proper checks could introduce security risks."
},
{
    "question": "A technician needs to reimage a desktop in an area without network access. Which of the following should the technician use? (Choose two.)",
    "options": [
        "USB.",
        "PXE.",
        "Optical media.",
        "Partition.",
        "Boot record.",
        "SMB."
    ],
    "correct_answer": [1, 3],
    "description": "The correct answers are USB and optical media. Both methods allow a technician to reimage a desktop without relying on network access. \n\n- PXE (Preboot Execution Environment) requires network access, so it is not suitable in this scenario. \n- A partition may contain recovery tools but isn't relevant to reimaging. \n- Boot record relates to how the system boots but is not directly involved in reimaging. \n- SMB is a network protocol and is not applicable without network access."
},

#416-430


    {
        "question": "A customer has a USB-only printer attached to a computer. A technician is configuring an arrangement that allows other computers on the network to use the printer. In which of the following locations on the customer's desktop should the technician make this configuration?",
        "options": [
            "Printing Preferences/Advanced tab",
            "Printer Properties/Sharing tab",
            "Printer Properties/Security tab",
            "Printer Properties/Ports tab"
        ],
        "correct_answer": 2,
        "description": "The correct answer is Printer Properties/Sharing tab. The Sharing tab allows the printer to be shared across the network, enabling other computers to access it. \n\n- The Advanced tab in Printing Preferences is used to configure printing options but not sharing settings. \n- The Security tab controls user permissions but does not facilitate network sharing. \n- The Ports tab is related to connection settings but does not handle network sharing."
    },
   {
    "question": "A technician requires graphical remote access to various Windows, Linux, and macOS desktops on the company LAN. The security administrator asks the technician to utilize a single software solution that does not require an external internet connection. Which of the following remote access tools is the technician most likely to install?",
    "options": [
        "NC",
        "RMM",
        "RDP",
        "SSH"
    ],
    "correct_answer": 1,
    "description": "The correct answer is NC (Netcat). NC (Netcat) can be used for network-related tasks, including setting up connections between systems within a local network, and it can be configured to facilitate remote access without requiring an external internet connection. \n\n- RMM (Remote Monitoring and Management) focuses more on monitoring and managing devices rather than direct graphical access. \n- RDP (Remote Desktop Protocol) is primarily for graphical remote access on Windows systems but is not typically configured for use across all operating systems in this context. \n- SSH is for secure command-line access and does not provide the graphical access needed for this scenario."
	},
    {
        "question": "Which of the following combinations meets the requirements for mobile device multifactor authentication?",
        "options": [
            "Password and PIN",
            "Password and swipe",
            "Fingerprint and password",
            "Swipe and PIN"
        ],
        "correct_answer": 3,
        "description": "The correct answer is Fingerprint and password. Multifactor authentication (MFA) combines two or more factors such as something you know (password) and something you are (fingerprint) for higher security. \n\n- Password and PIN are both knowledge factors and do not fulfill the MFA requirement. \n- Password and swipe both fall under knowledge factors, so they don't qualify as MFA. \n- Swipe and PIN are also both knowledge-based factors, not meeting the MFA standard."
    },
    {
        "question": "A help desk technician needs to remotely access and control a customer's Windows PC by using a secure session that allows the technician the same control as the customer. Which of the following tools provides this type of access?",
        "options": [
            "FTP",
            "RDP",
            "SSH",
            "VNC"
        ],
        "correct_answer": 4,
        "description": "The correct answer is VNC (Virtual Network Computing). VNC allows the technician to control the user's desktop remotely, providing the same access level as the user. \n\n- FTP (File Transfer Protocol) is for transferring files, not for remote desktop control. \n- RDP (Remote Desktop Protocol) is a valid option but may not provide the same user control depending on the setup. \n- SSH (Secure Shell) is primarily for command-line access and not suitable for full desktop control."
    },
    {
        "question": "A corporate smartphone was stored for five months after setup. During this time, the company did not have any system updates. When the phone is turned on, an application runs, but it crashes intermittently. Which of the following should a technician do next?",
        "options": [
            "Restart the phone.",
            "Reimage the OS.",
            "Reinstall the application.",
            "Clear the cache."
        ],
        "correct_answer": 3,
        "description": "The correct answer is Reinstall the application. Since the application crashes intermittently, reinstalling it may resolve the issue without affecting other system functions. \n\n- Restarting the phone may provide a temporary fix but won't solve the underlying issue. \n- Reimaging the OS is too drastic for a single app issue. \n- Clearing the cache may help in some cases, but a reinstallation is more effective when an app is crashing."
    },
    {
        "question": "A remote user's smartphone is performing very slowly. The user notices that the performance improves slightly after rebooting but then reverts back to performing slowly. The user also notices that the phone does not get any faster after connecting to the company's corporate guest network. A technician sees that the phone has a large number of applications installed on it. Which of the following is the most likely cause of the issue?",
        "options": [
            "The user is in a poor signal area.",
            "The user has too many processes running.",
            "The smartphone has malware on it.",
            "The smartphone has been jailbroken."
        ],
        "correct_answer": 2,
        "description": "The correct answer is The user has too many processes running. A large number of applications could be using up system resources, leading to poor performance. \n\n- Poor signal area would affect network speed but not overall phone performance. \n- Malware can slow down devices, but the user did not mention suspicious behavior beyond slowness. \n- Jailbreaking is unlikely the issue if the user has not explicitly mentioned it."
    },
    {
        "question": "A technician is installing RAM in a new workstation and needs to protect against electrostatic discharge. Which of the following will best resolve this concern?",
        "options": [
            "Battery backup",
            "Thermal paste",
            "ESD strap",
            "Consistent power"
        ],
        "correct_answer": 3,
        "description": "The correct answer is ESD strap (Electrostatic Discharge strap). An ESD strap prevents electrostatic discharge by grounding the technician while handling sensitive components like RAM. \n\n- Battery backup protects against power loss but not electrostatic discharge. \n- Thermal paste is for improving heat conductivity, unrelated to ESD protection. \n- Consistent power does not prevent electrostatic discharge."
    },
    {
        "question": "A technician is trying to connect to a user's laptop in order to securely install updates. Given the following information about the laptop:\n\nHostname: corp-laptop-222\nIP Address: 192.168.0.45\nGateway: 192.168.1.1\nSubnet Mask: 255.255.252.0\nOpen Ports: 21, 22, 80, 443\n\nWhich of the following should the technician do to connect via RDP?",
        "options": [
            "Confirm the user can ping the default gateway.",
            "Change the IP address on the user's laptop.",
            "Change the subnet mask on the user's laptop.",
            "Open port 3389 on the Windows firewall."
        ],
        "correct_answer": 4,
        "description": "The correct answer is Open port 3389 on the Windows firewall. RDP uses port 3389 by default, and opening it on the firewall will allow the remote connection. \n\n- Pinging the default gateway tests network connectivity but does not affect RDP access. \n- Changing the IP or subnet mask is unnecessary unless there's a conflict, which is not indicated here."
    },
    {
        "question": "Which of the following is the most likely to use NTFS as the native filesystem?",
        "options": [
            "macOS",
            "Linux",
            "Windows",
            "Android"
        ],
        "correct_answer": 3,
        "description": "The correct answer is Windows. NTFS (New Technology File System) is the default filesystem used by Windows for its internal drives. \n\n- macOS primarily uses the APFS or HFS+ file systems. \n- Linux typically uses ext4 or other Linux-native file systems. \n- Android relies on file systems like ext4 for internal storage."
    },
    {
        "question": "A user is unable to access several documents saved on a work PC. A technician discovers the files were corrupted and must change several system settings within Registry Editor to correct the issue. Which of the following should the technician do before modifying the registry keys?",
        "options": [
            "Update the anti-malware software.",
            "Create a restore point.",
            "Run the PC in safe mode.",
            "Roll back the system updates."
        ],
        "correct_answer": 2,
        "description": "The correct answer is Create a restore point. Creating a restore point allows the system to be restored to a previous state in case something goes wrong during the registry modifications. \n\n- Updating anti-malware software is unrelated to the current issue. \n- Running the PC in safe mode can be useful, but it does not protect against incorrect registry modifications. \n- Rolling back system updates is not necessary unless the issue is directly related to a recent update."
    },
    {
        "question": "After a security event, a technician removes malware from an affected laptop and disconnects the laptop from the network. Which of the following should the technician do to prevent the operating system from automatically returning to an infected state?",
        "options": [
            "Enable System Restore.",
            "Disable System Restore.",
            "Enable antivirus.",
            "Disable antivirus.",
            "Educate the user."
        ],
        "correct_answer": 2,
        "description": "The correct answer is Disable System Restore. Disabling System Restore ensures that the malware doesn't get restored if the system is rolled back to a previous infected state. \n\n- Enabling System Restore would keep the risk of restoring malware. \n- Enabling antivirus is important for prevention but won't resolve the System Restore issue. \n- Educating the user is helpful for future prevention but does not address this specific issue."
    },
    {
        "question": "Which of the following file types allows a user to easily uninstall software from macOS by simply placing it in the trash bin?",
        "options": [
            ".exe",
            ".dmg",
            ".app",
            ".rpm",
            ".pkg"
        ],
        "correct_answer": 3,
        "description": "The correct answer is .app. In macOS, applications with the .app extension can be easily uninstalled by dragging them to the trash bin. \n\n- .exe files are used for Windows executable programs. \n- .dmg is a disk image file used for installing applications but not for uninstallation. \n- .rpm is for Linux package management. \n- .pkg is a macOS package installer format but is not uninstalled by moving to the trash."
    },
    {
        "question": "A user's application is unresponsive. Which of the following Task Manager tabs will allow the user to address the situation?",
        "options": [
            "Startup",
            "Performance",
            "Application history",
            "Processes"
        ],
        "correct_answer": 4,
        "description": "The correct answer is Processes. The Processes tab in Task Manager allows users to identify and end unresponsive applications. \n\n- The Startup tab manages which applications run when the system starts. \n- The Performance tab provides system performance statistics but doesn’t help with unresponsive applications. \n- Application history shows past usage but doesn't allow users to terminate tasks."
    },
    {
        "question": "A new spam gateway was recently deployed at a small business. However, users still occasionally receive spam. The management team is concerned that users will open the messages and potentially infect the network systems. Which of the following is the most effective method for dealing with this issue?",
        "options": [
            "Adjusting the spam gateway",
            "Updating firmware for the spam appliance",
            "Adjusting AV settings",
            "Providing user training"
        ],
        "correct_answer": 4,
        "description": "The correct answer is Providing user training. Educating users on how to identify and avoid phishing attempts or suspicious emails is the most effective way to prevent accidental infections. \n\n- Adjusting the spam gateway may improve filtering but is not foolproof. \n- Updating the spam appliance firmware can improve performance but will not eliminate all spam. \n- Adjusting AV settings may enhance protection but won't teach users how to handle suspicious emails."
    },
    {
        "question": "An employee has repeatedly contacted a technician about malware infecting a work computer. The technician has removed the malware several times, but the user's PC keeps getting infected. Which of the following should the technician do to reduce the risk of future infections?",
        "options": [
            "Configure the firewall",
            "Restore the system from backups",
            "Educate the end user",
            "Update the antivirus program"
        ],
        "correct_answer": 3,
        "description": "The correct answer is Educate the end user. Educating the user on how to avoid malware, such as not clicking on suspicious links or opening unknown attachments, will help prevent future infections. \n\n- Configuring the firewall can help block malicious traffic but won’t address user behavior. \n- Restoring the system from backups may help temporarily but won't prevent future infections. \n- Updating the antivirus program improves detection but doesn’t solve the underlying cause of recurring infections."
    },

#431-450

    {
        "question": "A user clicks a link in an email. A warning message in the user's browser states the site's certificate cannot be verified. Which of the following is the most appropriate action for a technician to take?",
        "options": [
            "Click proceed.",
            "Report the employee to the human resources department for violating company policy.",
            "Restore the computer from the last known backup.",
            "Close the browser window and report the email to IT security."
        ],
        "correct_answer": 4,
        "description": "The correct answer is to close the browser window and report the email to IT security. This approach prevents potential malware infection and ensures the incident is handled by security professionals. \n\n- Clicking proceed could expose the user to a malicious site. \n- Reporting the employee to HR is not the priority in this situation, as the immediate concern is handling the potential threat. \n- Restoring the computer from a backup is not necessary without confirming any infection."
    },
    {
        "question": "A user reports a hardware issue to the help desk. Which of the following should the help desk technician do first when responding to the user?",
        "options": [
            "Ask the user for the model number of the hardware.",
            "Offer a temporary replacement device to the user.",
            "Submit the issue to the manufacturer.",
            "Remotely install updates to the device driver."
        ],
        "correct_answer": 1,
        "description": "The correct answer is to ask the user for the model number of the hardware. This provides the technician with necessary details about the hardware, allowing for precise troubleshooting and determining the next steps. \n\n- Offering a replacement may not be feasible without diagnosing the issue first. \n- Submitting the issue to the manufacturer is premature without further details. \n- Installing updates to the device driver remotely may not solve the problem if the root cause is unknown."
    },
    {
        "question": "An IT services company that supports a large government contract replaced the Ethernet cards on several hundred desktop machines to comply with regulatory requirements. Which of the following disposal methods for the non-compliant cards is the most environmentally friendly?",
        "options": [
            "Incineration",
            "Resale",
            "Physical destruction",
            "Dumpster for recycling plastics"
        ],
        "correct_answer": 2,
        "description": "The correct answer is resale. Reselling non-compliant cards enables reuse, reducing waste and minimizing environmental impact. \n\n- Incineration releases harmful pollutants into the environment. \n- Physical destruction may be necessary in certain cases for security but is not ideal for environmental sustainability. \n- Recycling plastics is beneficial but doesn’t address all card materials and may not be as environmentally friendly as reuse."
    },
    {
        "question": "Which of the following file extensions should a technician use for a PowerShell script?",
        "options": [
            ".ps1",
            ".py",
            ".sh",
            ".bat",
            ".cmd"
        ],
        "correct_answer": 1,
        "description": "The correct answer is .ps1. PowerShell scripts use the .ps1 file extension, which allows Windows to recognize and execute these scripts in the PowerShell environment. \n\n- .py is used for Python scripts. \n- .sh is the extension for shell scripts, typically on Unix/Linux systems. \n- .bat and .cmd are used for batch files in Windows but not specifically for PowerShell."
    },


#435-436 is an image question



{
    "question": "A user receives a call from someone claiming to be a technical support agent. The caller asks the user to log in to the computer. Which of the following security measures should the user take to ensure security and privacy?",
    "options": [
        "Only accept calls from known people.",
        "Disregard any suspicious emails.",
        "Update the antivirus software.",
        "Enable two-factor authentication.",
        "Install a malware scanner."
    ],
    "correct_answer": 1,
    "description": "The correct answer is to only accept calls from known people, ensuring the caller’s identity is recognized to help prevent social engineering attempts.\n\n- Disregarding suspicious emails protects against phishing but does not address phone-based social engineering.\n- Updating antivirus software is good for general protection but not specifically related to call security.\n- Enabling two-factor authentication adds security but does not prevent scams conducted by phone.\n- Installing a malware scanner helps with software threats but doesn't address unauthorized access via calls."
},

{
    "question": "A user reports that an air-gapped computer may have been infected with a virus after the user transferred files from a USB drive. The technician runs a computer scan with Windows Defender but does not find an infection. Which of the following actions should the technician take next? (Choose two.)",
    "options": [
        "Examine the event logs",
        "Connect to the network",
        "Document the findings",
        "Update the definitions",
        "Reimage the computer",
        "Enable the firewall"
    ],
    "correct_answer": [1, 4],
    "description": "The correct answers are to examine the event logs and update the definitions. Checking the event logs provides insight into any suspicious activities, while updating the definitions ensures the latest virus signatures are in place, which is essential for detecting newer threats.\n\n- Connecting to the network compromises air-gapped security and is inappropriate for isolated systems.\n- Documenting the findings is helpful but not immediately actionable in this context.\n- Reimaging is a drastic step without confirmed evidence of infection.\n- Enabling the firewall is not relevant for an already isolated, air-gapped system."
},

 {
        "question": "An administrator needs to select a method to dispose of SSDs containing sensitive data. Which of the following are the most appropriate methods? (Choose two.)",
        "options": [
            "Degauss",
            "Delete",
            "Incinerate",
            "Recycle",
            "Format",
            "Shred"
        ],
        "correct_answer": [3, 6],
        "description": "The correct answers are incinerate and shred, which are secure disposal methods for sensitive data on SSDs.\n\n- Degaussing is ineffective on SSDs, which lack magnetic storage.\n- Deleting and formatting are inadequate for secure deletion of sensitive data.\n- Recycling without data destruction risks data exposure."
    },





    {
        "question": "A technician has verified a computer is infected with malware. The technician isolates the system and updates the anti-malware software. Which of the following should the technician do next?",
        "options": [
            "Run one scan and schedule future scans.",
            "Back up the uninfected files and reimage the computer.",
            "Restore the clean backup copies of the infected files.",
            "Run repeated remediation scans until the malware is removed."
        ],
        "correct_answer": 4,
        "description": "The correct answer is to run repeated remediation scans until the malware is removed, ensuring all traces of the malware are eradicated.\n\n- Running one scan and scheduling future scans may miss some malware.\n- Backing up files before removal may back up infected files.\n- Restoring files without removal leaves the malware on the system."
    },
    {
        "question": "A technician needs to configure security settings on a Windows 10 workstation. Which of the following should the technician configure to limit password attempts?",
        "options": [
            "Account Lockout Policy",
            "User Access Control",
            "System Protection",
            "Firewall"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Account Lockout Policy, which limits login attempts to secure accounts.\n\n- User Access Control restricts permission levels but does not manage login attempts.\n- System Protection handles system restoration.\n- Firewall settings secure network traffic, not user login attempts."
    },

{
    "question": "Which of the following protocols supports fast roaming between networks?",
    "options": [
        "WEP",
        "WPA",
        "WPA2",
        "LEAP",
        "PEAP"
    ],
    "correct_answer": 3,
    "description": "The correct answer is WPA2, as it includes enhancements that support faster, secure transitions between access points when roaming.\n\n- WEP lacks both security and roaming capabilities.\n- WPA offers security improvements but is less optimized for fast roaming than WPA2.\n- LEAP does support fast roaming but is considered outdated and less secure.\n- PEAP is primarily used for secure authentication and does not facilitate fast roaming."
},

{
        "question": "A technician is setting up a SOHO router in a user’s home. The user wants the router to be configured to prevent access to malicious content and apply internet access protection. Which of the following settings should the technician configure?",
        "options": [
            "Port forwarding",
            "Content filtering",
            "Firmware updates",
            "DHCP reservations"
        ],
        "correct_answer": 2,
        "description": "The correct answer is content filtering, which blocks access to harmful sites.\n\n- Port forwarding manages traffic routing but does not prevent malicious content.\n- Firmware updates improve router performance but don’t filter content.\n- DHCP reservations assign specific IPs and are unrelated to content protection."
    },
    {
        "question": "A user's computer unexpectedly shut down immediately after the user plugged in a USB headset. Once the user turned the computer back on, everything was functioning properly, including the headset. Which of the following Microsoft tools would most likely be used to determine the root cause?",
        "options": [
            "Event Viewer",
            "System Configuration",
            "Device Manager",
            "Performance Monitor"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Event Viewer, which logs hardware events and errors, helping troubleshoot shutdown causes.\n\n- System Configuration manages startup options, not detailed event logs.\n- Device Manager shows device statuses but does not track previous issues.\n- Performance Monitor tracks system performance but lacks specific event logs."
    },
    {
        "question": "A developer reports that a workstation’s database file extensions have been changed from .db to .enc. The developer is also unable to open the database files manually. Which of the following is the best option for recovering the data?",
        "options": [
            "Accessing a restore point.",
            "Rebooting into safe mode.",
            "Utilizing the backups.",
            "Using an AV to scan the affected files."
        ],
        "correct_answer": 3,
        "description": "The correct answer is utilizing the backups, which provides unaltered versions of the database files.\n\n- Accessing a restore point may not restore specific data files.\n- Rebooting into safe mode may not resolve file encryption issues.\n- Using an antivirus may help if malware is present, but backup recovery is more reliable."
    },
    {
        "question": "A large company is changing its password length requirements. The Chief Information Officer is mandating that passwords now be at least 12 characters long, instead of 10. Which of the following should be used to adjust this setting?",
        "options": [
            "Group Policy",
            "User accounts",
            "Access control lists",
            "Authenticator applications"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Group Policy, which manages password policies across networked systems.\n\n- User accounts control individual access but do not enforce password rules.\n- Access control lists specify permissions but not password requirements.\n- Authenticator applications handle 2FA, not password length."
    },
    {
        "question": "Multiple users routinely record log-in information in readily accessible areas. Which of the following is the best way to mitigate this issue?",
        "options": [
            "Trusted sources",
            "Valid certificates",
            "User training",
            "Password manager"
        ],
        "correct_answer": 3,
        "description": "The correct answer is user training, which educates users on secure practices.\n\n- Trusted sources and valid certificates ensure secure communication but don’t address user behavior.\n- A password manager helps secure passwords but relies on user understanding of secure storage."
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
        "description": "The correct answer is System, where display settings are configured for multi-monitor setups.\n\n- Color Management adjusts color settings, not screen extensions.\n- Troubleshooting identifies issues but does not configure displays.\n- Device Manager manages hardware but not display extensions.\n- Administrative Tools are for system management, not display configuration."
    },
    {
        "question": "Which of the following commands can a technician use to get the MAC address of a Linux distribution?",
        "options": [
            "net use",
            "ifconfig",
            "netstat",
            "ping"
        ],
        "correct_answer": 2,
        "description": "The correct answer is ifconfig, which displays network interface details, including MAC addresses on Linux.\n\n- net use connects network resources in Windows.\n- netstat shows network connections and traffic but not MAC addresses.\n- ping tests connectivity but does not retrieve MAC addresses."
    },
{
    "question": "A user reports that an Android mobile device takes a long time to boot, and all applications crash when launched. The user installed the applications from a third-party website. Which of the following steps should the technician complete to diagnose the issue?",
    "options": [
        "Scan the system for malware.",
        "Clear the web browser cache.",
        "Enroll the device in an MDM system.",
        "Confirm the compatibility of the applications with the OS."
    ],
    "correct_answer": [1],
    "description": "The correct answer is Scan the system for malware. Since the applications were installed from a third-party website, they may contain malicious software that is causing the system issues. Scanning for malware will help identify and remove any harmful software. \n\n- Clearing the web browser cache may help with browser-related issues but is unlikely to resolve problems caused by third-party apps. \n- Enrolling the device in an MDM system is not necessary at this point; MDM is more suited for managing corporate devices, not diagnosing individual app issues. \n- Confirming compatibility is a good practice, but since the apps were installed from an untrusted source, malware is a more immediate concern."
},





#451-480


    {
        "question": "A technician is hardening a company file server and needs to prevent unauthorized LAN devices from accessing stored files. Which of the following should the technician use?",
        "options": [
            "Software firewall",
            "Password complexity",
            "Antivirus application",
            "Anti-malware scans"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Software firewall. A firewall can block unauthorized devices from accessing resources by filtering network traffic.\n\n- Password complexity does not address unauthorized LAN devices, as it only strengthens individual accounts.\n- Antivirus application focuses on preventing malicious software but does not control device access.\n- Anti-malware scans detect and remove malware but do not prevent unauthorized device access."
    },
    {
        "question": "A technician is installing software on a user’s workstation. The installation fails due to incompliance with the HCL. Which of the following components is most likely causing the installation to fail? (Choose two.)",
        "options": [
            "NIC",
            "CPU",
            "PSU",
            "KVM",
            "RAM",
            "DVI"
        ],
        "correct_answer": [2, 5],
        "description": "The correct answers are CPU and RAM. Compatibility issues with these components are common causes of HCL (Hardware Compatibility List) installation failures.\n\n- NIC, PSU, and DVI are less likely to cause HCL incompatibility as they do not directly impact the system’s ability to support software.\n- KVM switches are used for managing multiple systems and do not typically affect installation compatibility."
    },
    {
        "question": "Which of the following items require special e-waste recycling? (Choose two.)",
        "options": [
            "Solid-state drive",
            "A/C adapter",
            "Surge protector",
            "Laptop battery",
            "CRT monitor",
            "Power supply"
        ],
        "correct_answer": [4, 5],
        "description": "The correct answers are Laptop battery and CRT monitor. Batteries and CRT monitors contain hazardous materials that require special handling in e-waste recycling.\n\n- Solid-state drives and power supplies, while recyclable, do not require special recycling due to hazardous materials.\n- A/C adapters and surge protectors can be recycled in standard electronics recycling programs."
    },
    {
        "question": "A user reports that the hard drive activity light on a Windows 10 desktop computer has been steadily lit for more than an hour and performance is severely degraded. Which of the following tabs in Task Manager contains the information a technician should use to identify the cause of this issue?",
        "options": [
            "Services",
            "Processes",
            "Performance",
            "Startup"
        ],
        "correct_answer": 2,
        "description": "The correct answer is Processes. The Processes tab shows resource utilization by active applications, helping identify which one might be causing the high disk activity.\n\n- The Services tab lists system services but does not provide resource usage.\n- The Performance tab provides an overview of overall system resource usage but lacks process-specific details.\n- Startup manages startup items but does not offer information on active processes."
    },
    {
        "question": "A technician downloaded a software program to a network share. When the technician attempts to copy the program to the Windows tablet for installation, the technician receives an error. Which of the following is the best procedure for the technician to use to complete the assignment?",
        "options": [
            "Copy the program file to a USB drive and install.",
            "Burn the program file to a CD and install.",
            "Format the HDD and then do the installation.",
            "Replace the HDD and then do the installation."
        ],
        "correct_answer": 1,
        "description": "The correct answer is to copy the program file to a USB drive and install. Transferring via USB is a reliable method when direct network transfer encounters errors.\n\n- Burning to a CD is less efficient and not commonly supported on tablets.\n- Formatting or replacing the HDD is unnecessary and excessive for resolving a file transfer error."
    },
    {
        "question": "Which of the following features can be used to ensure a user can access multiple versions of files?",
        "options": [
            "Multiple desktops",
            "Remote Disc",
            "Time Machine",
            "FileVault"
        ],
        "correct_answer": 3,
        "description": "The correct answer is Time Machine. This feature on macOS allows users to back up and restore multiple versions of files over time.\n\n- Multiple desktops organize active windows but do not store file versions.\n- Remote Disc facilitates file access from other devices but does not offer version history.\n- FileVault encrypts files for security but does not manage file versions."
    },
    {
        "question": "Users report that a network printer intermittently goes offline during the day. Which of the following commands should the technician use to confirm whether the printer has connectivity issues?",
        "options": [
            "ping",
            "netstat",
            "net",
            "nslookup"
        ],
        "correct_answer": 1,
        "description": "The correct answer is ping. This command checks the connectivity status of the printer by sending a request and measuring the response.\n\n- netstat monitors network connections but does not specifically check device connectivity.\n- net is a command suite but not specific to connectivity testing.\n- nslookup resolves domain names to IP addresses and is unrelated to network connectivity testing."
    },
    {
        "question": "A technician wants to enable BitLocker on a Windows 10 laptop and is unable to find the BitLocker Drive Encryption menu item in Control Panel. Which of the following explains why the technician is unable to find this menu item?",
        "options": [
            "The hardware does not meet BitLocker’s minimum system requirements.",
            "BitLocker was renamed for Windows 10.",
            "BitLocker is not included on Windows 10 Home.",
            "BitLocker was disabled in the registry of the laptop."
        ],
        "correct_answer": 3,
        "description": "The correct answer is BitLocker is not included on Windows 10 Home. BitLocker is only available on Windows 10 Pro and Enterprise editions.\n\n- Minimum system requirements affect BitLocker’s functionality, not its visibility.\n- BitLocker was not renamed for Windows 10.\n- Registry settings may impact functionality but typically would not remove the option from the Control Panel."
    },
   {
    "question": "A user’s Windows 10 workstation with an HDD is running really slowly. The user has opened, closed, and saved many large files over the past week. Which of the following tools should a technician use to remediate the issue?",
    "options": [
        "Disk Defragment",
        "Registry Editor",
        "System Information",
        "Disk Cleanup"
    ],
    "correct_answer": 4,
    "description": "The correct answer is Disk Cleanup. This tool clears temporary files and frees up disk space, which can improve the performance of an HDD after extensive file operations.\n\n- Disk Defragment helps optimize data layout on an HDD but is typically used to organize fragmented data rather than directly free up space.\n- Registry Editor manages system configurations, but it is not used for cleaning or optimizing disk space.\n- System Information provides data about the computer but does not contribute to improving HDD performance."
},




    {
        "question": "A branch office suspects a machine contains ransomware. Which of the following mitigation steps should a technician take first?",
        "options": [
            "Disable System Restore.",
            "Remediate the system.",
            "Educate the system user.",
            "Quarantine the system."
        ],
        "correct_answer": 4,
        "description": "The correct answer is Quarantine the system. Isolating the affected machine prevents ransomware from spreading to other networked devices. \n\n- Disabling System Restore could prevent potential data recovery points but does not isolate the threat. \n- Remediating the system is critical but only after containment to prevent wider impact. \n- Educating the user is valuable post-remediation but is not a first-line defense during an active ransomware incident."
    },
    {
        "question": "A Linux technician needs a filesystem type that meets the following requirements:\n• All changes are tracked.\n• The possibility of file corruption is reduced.\n• Data recovery is easy.\n\nWhich of the following filesystem types best meets these requirements?",
        "options": [
            "ext3",
            "FAT32",
            "exFAT",
            "NTFS"
        ],
        "correct_answer": 1,
        "description": "The correct answer is ext3. Ext3 supports journaling, which logs changes and reduces file corruption risk, making data recovery more reliable.\n\n- FAT32 lacks journaling, making it more prone to corruption.\n- exFAT is optimized for external storage but doesn’t track changes.\n- NTFS supports journaling but is primarily used in Windows environments, while ext3 is more Linux-native."
    },
    {
        "question": "A user’s laptop has been performing slowly and redirecting to unfamiliar websites. The user has also noticed random pop-up windows. Which of the following is the first step a technician should take to resolve the issue?",
        "options": [
            "Scan for malware and ransomware.",
            "Perform a system restore.",
            "Check the network utilization.",
            "Update the antivirus software."
        ],
        "correct_answer": 1,
        "description": "The correct answer is Scan for malware and ransomware. These symptoms indicate malware infection, and a scan can identify and potentially remove it.\n\n- Performing a system restore might help but does not identify the root cause.\n- Checking network utilization could help in performance diagnosis but not in malware detection.\n- Updating antivirus software strengthens security but won’t immediately address current infections."
    },
    {
        "question": "A user reports being unable to access a sports team’s website on an office computer. The administrator tells the user this blocked access is intentional and based on company guidelines. Which of the following is the administrator referring to?",
        "options": [
            "NDA",
            "AUP",
            "VPN",
            "SOP"
        ],
        "correct_answer": 2,
        "description": "The correct answer is AUP. An Acceptable Use Policy (AUP) dictates appropriate internet usage and may restrict access to certain sites.\n\n- NDA (Non-Disclosure Agreement) is related to confidential information, not internet restrictions.\n- VPN provides secure remote access but doesn’t control website access.\n- SOP (Standard Operating Procedure) outlines company workflows but does not regulate internet use."
    },
    {
        "question": "Which of the following authentication types is the most secure?",
        "options": [
            "WPA3",
            "WEP",
            "RADIUS",
            "TACACS+",
            "WPS"
        ],
        "correct_answer": 1,
        "description": "The correct answer is WPA3. WPA3 is a wireless security protocol that provides robust protection for Wi-Fi networks.\n\n- WEP is outdated and easily compromised.\n- RADIUS and TACACS+ are network protocols for remote authentication but don’t inherently secure Wi-Fi.\n- WPS simplifies Wi-Fi setup but is vulnerable to brute-force attacks."
    },
    {
        "question": "A technician is manually updating Windows workstations. Each workstation is currently running Windows Pro in a workgroup environment. Which of the following changes can the technician make to create a more manageable environment?",
        "options": [
            "Downgrade all workstations from the Pro version to the Home version of the OS.",
            "Upgrade all workstations from the Pro version to Pro for Workstations.",
            "Create a domain and join the workstations to the domain for management purposes.",
            "Make sure all workstations are operating under the same workgroup name."
        ],
        "correct_answer": 3,
        "description": "The correct answer is Create a domain and join the workstations to the domain for management purposes. A domain simplifies centralized management of multiple devices.\n\n- Downgrading to Home reduces functionality and management tools.\n- Upgrading to Pro for Workstations increases power but doesn’t add centralized management.\n- Operating under the same workgroup name only organizes devices but lacks centralized management capabilities."
    },
    {
        "question": "A user is unable to start a computer following a failed Windows 10 update. When trying to start the computer, the user sees a blue screen of death. Which of the following steps should a technician take to diagnose the issue?",
        "options": [
            "Perform a safe mode boot.",
            "Run the System Restore wizard.",
            "Start the computer in the last known-good configuration.",
            "Reset the BIOS settings."
        ],
        "correct_answer": 1,
        "description": "The correct answer is Perform a safe mode boot. Safe mode allows troubleshooting by starting Windows with minimal drivers, bypassing recent changes that may have caused issues.\n\n- System Restore could help, but safe mode allows broader diagnosis.\n- Starting with the last known-good configuration helps with driver issues but may not fix update-related failures.\n- Resetting the BIOS settings typically won’t resolve OS issues caused by updates."
    },
    {
        "question": "Applications on a computer are not updating, which is preventing the user from opening certain files. Which of the following MAC snap-ins should the technician launch next to continue troubleshooting the issue?",
        "options": [
            "gpedit.msc",
            "perfmon.msc",
            "devmgmt.msc",
            "eventvwr.msc"
        ],
        "correct_answer": 4,
        "description": "The correct answer is eventvwr.msc. Event Viewer (eventvwr.msc) provides logs that can reveal update-related errors and help identify underlying issues.\n\n- gpedit.msc is for configuring Group Policies, not troubleshooting application updates.\n- perfmon.msc monitors system performance but doesn’t track update issues.\n- devmgmt.msc manages hardware but doesn’t provide software update information."
    },
    {
        "question": "A technician needs to back up a small business’s entire network that includes ten workstations. Which of the following methods should the technician use to safely and securely back up the business’s network?",
        "options": [
            "Cloud storage",
            "RAID",
            "Tape drive",
            "Local backups"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Cloud storage. Cloud storage offers scalability and security for storing network backups offsite.\n\n- RAID is mainly for local disk redundancy, not full network backups.\n- Tape drives offer physical backups but lack the security and accessibility of cloud solutions.\n- Local backups provide redundancy but can be compromised in on-site disasters."
    },
    {
        "question": "A technician wants to update the local security policies on a Windows machine but is unable to launch the expected snap-in. Which of the following is the most likely reason?",
        "options": [
            "The computer is running Windows Home.",
            "The user did not sign the end user license agreement.",
            "The user disabled the User Account Control.",
            "An antivirus application is blocking access."
        ],
        "correct_answer": 1,
        "description": "The correct answer is The computer is running Windows Home. Windows Home lacks the Group Policy Editor, restricting local security policy changes.\n\n- Not signing the EULA doesn’t affect access to security policies.\n- Disabling UAC affects user permissions but doesn’t limit snap-ins.\n- Antivirus applications might interfere with certain tools but rarely restrict system policies."
    },
    {
        "question": "Which of the following is also known as something you know, something you have, and something you are?",
        "options": [
            "ACL",
            "MFA",
            "SMS",
            "NFC"
        ],
        "correct_answer": 2,
        "description": "The correct answer is MFA. Multi-Factor Authentication (MFA) combines knowledge (password), possession (token), and inherence (biometric) for secure verification.\n\n- ACL controls access but doesn’t involve multifactor checks.\n- SMS is a communication method and can be a factor but doesn’t imply multifactor.\n- NFC is a technology but not a multifactor system."
    },




    {
    "question": "An organization is creating guidelines for the incorporation of generative AI solutions. In which of the following would these guidelines be published?",
    "options": [
        "Standard operating procedure.",
        "Acceptable use policy.",
        "Security protocols.",
        "Data flow diagram."
    ],
    "correct_answer": 2,
    "description": "The correct answer is acceptable use policy. This document outlines the permissible use of resources and technologies, including generative AI, ensuring users understand the organization's stance and guidelines. \n\n- A standard operating procedure provides detailed processes but is not specific to AI. \n- Security protocols focus on measures to protect assets, while a data flow diagram illustrates how data moves within the system, rather than guidelines for use."
},
{
    "question": "When visiting a particular website, a user receives a message stating, “Your connection is not private.” Which of the following describes this issue?",
    "options": [
        "Certificate warning.",
        "Malware.",
        "JavaScript error.",
        "Missing OS update."
    ],
    "correct_answer": 1,
    "description": "The correct answer is certificate warning. This message typically indicates a problem with the website's SSL certificate, which secures the connection, potentially exposing user data. \n\n- Malware could cause security issues but is not specifically indicated by this message. \n- A JavaScript error would not usually affect the connection security, and a missing OS update is unrelated to SSL certificate validation."
},
{
    "question": "Malware is installed on a device after a user clicks on a link in a suspicious email. Which of the following is the best way to remove the malware?",
    "options": [
        "Run System Restore.",
        "Place in recovery mode.",
        "Schedule a scan.",
        "Restart the PC."
    ],
    "correct_answer": 3,
    "description": "The correct answer is schedule a scan. This action allows the antivirus software to detect and remove the malware thoroughly. \n\n- Running System Restore may revert the device to a previous state but does not guarantee malware removal. \n- Recovery mode can be useful, but scheduling a scan is a proactive step in malware removal. \n- Restarting the PC alone is not sufficient to eliminate malware."
},
{
    "question": "A technician needs to perform after-hours service starting at 10:00 p.m. The technician is currently 20 minutes late. The customer will also be late. Which of the following should the technician do considering proper communication techniques and professionalism?",
    "options": [
        "Do not notify the customer if arriving before the customer.",
        "Dismiss the customer and proceed with the after-hours work.",
        "Contact the customer if the technician is arriving late.",
        "Disclose the experience via social media."
    ],
    "correct_answer": 3,
    "description": "The correct answer is to contact the customer if the technician is arriving late. This shows professionalism and respect for the customer's time, ensuring they are informed. \n\n- Not notifying the customer could lead to misunderstandings. \n- Dismissing the customer is unprofessional, and disclosing the experience on social media is inappropriate and could damage the technician's reputation."
},
{
    "question": "A client wants a technician to set up a proxy server in a branch office to manage internet access. This involves configuring the workstations to use the new proxy server. Which of the following Internet Options tabs in Control Panel would be most appropriate for the technician to use to configure the settings?",
    "options": [
        "Privacy.",
        "Advanced.",
        "Content.",
        "Connections.",
        "Security."
    ],
    "correct_answer": 4,
    "description": "The correct answer is Connections. This tab allows the technician to configure proxy settings for internet access on workstations effectively. \n\n- The Privacy tab pertains to user privacy settings, while Advanced deals with advanced browser settings. \n- The Content tab is for managing content settings, and Security focuses on security settings, not proxy configuration."
},


{
    "question": "A customer installed a new web browser from an unsolicited USB drive that the customer received in the mail. The browser is not working as expected, and internet searches are redirected to another site. Which of the following should the user do next after uninstalling the browser?",
    "options": [
        "Delete the browser cookies and history.",
        "Reset all browser settings.",
        "Change the browser default search engine.",
        "Install a trusted browser."
    ],
    "correct_answer": 4,
    "description": "The correct answer is to install a trusted browser. After uninstalling the potentially harmful browser, installing a trusted browser ensures that the user has a secure and functional browser for internet access. \n\n- Deleting cookies and history may help remove traces, but it doesn't fix potential system-level issues caused by the malicious browser. \n- Resetting browser settings is a good step but may not address underlying issues caused by malware. \n- Changing the default search engine is not enough to eliminate malicious changes."
},


{
    "question": "A company is creating an access control system that uses something you have and something you are. Which of the following will be required for user authentication? (Choose two.)",
    "options": [
        "Password manager.",
        "Encryption keys.",
        "Biometric scanner.",
        "Smartcard reader.",
        "Host-based IDS.",
        "PIN code."
    ],
    "correct_answer": [3, 4],
    "description": "The correct answers are biometric scanner and smartcard reader. These elements represent 'something you are' (biometric) and 'something you have' (smartcard), which are essential for multifactor authentication. \n\n- A password manager is for storing passwords, not directly used in access control. \n- Encryption keys are not typically used for user authentication in this context. \n- Host-based IDS monitors for intrusions rather than authentication, and a PIN code is not as secure as biometric measures."
},
{
    "question": "An administrator configured security features on company-owned mobile devices to help protect against data loss. Which of the following is the best way to protect data on a misplaced device?",
    "options": [
        "Remote wipe.",
        "Device encryption.",
        "PIN codes.",
        "Locator applications."
    ],
    "correct_answer": 2,
    "description": "The correct answer is device encryption. This feature ensures that the data on the device is protected, making it unreadable to unauthorized users if the device is lost or stolen. \n\n- Remote wipe is effective for data protection, but device encryption offers ongoing protection for all data, including when the device is in use. \n- PIN codes provide a basic level of security but are not as effective as encryption in protecting data if the device is compromised. \n- Locator applications can help find the device but do not provide data protection."
},
{
    "question": "A technician cannot uninstall a system driver because the driver is currently in use. Which of the following tools should the technician use to help uninstall the driver?",
    "options": [
        "msinfo32.exe.",
        "dxdiag.exe.",
        "msconfig.exe.",
        "regedit.exe."
    ],
    "correct_answer": 3,
    "description": "The correct answer is msconfig.exe. This tool allows the technician to manage startup processes and services, potentially disabling the driver to facilitate uninstallation. \n\n- msinfo32.exe provides system information but does not assist in uninstallation. \n- dxdiag.exe is for diagnostic purposes and does not affect driver management. \n- regedit.exe is for editing the registry, which is risky and not directly related to uninstalling drivers."
},
{
    "question": "Which of the following operating systems is most commonly used in embedded systems?",
    "options": [
        "Chrome OS.",
        "macOS.",
        "Windows.",
        "Linux."
    ],
    "correct_answer": 4,
    "description": "The correct answer is Linux. This operating system is widely used in embedded systems due to its open-source nature, flexibility, and customization capabilities. \n\n- Chrome OS is primarily designed for web-based applications and is not suitable for embedded systems. \n- macOS is designed for Apple hardware and not used in embedded environments. \n- Windows has embedded versions, but Linux is more commonly used in various embedded applications due to its adaptability."
},

#481-500


    {
        "question": "A user identified that a program installed in a workstation does not have optional features enabled. Which of the following must the technician do to install the optional features?",
        "options": [
            "Go to Programs and Features, uninstall the program, and reinstall it.",
            "Go to Administrative Tools and edit System Configuration.",
            "Go to Administrative Tools and run Disk Cleanup.",
            "Go to Programs and Features, select the program, and click on Change."
        ],
        "correct_answer": 4,
        "description": "The correct answer is to go to Programs and Features, select the program, and click on Change. This option allows the technician to modify the installation, including adding optional features.\n\n- Uninstalling and reinstalling the program is unnecessary unless the program is corrupted.\n- Editing System Configuration or running Disk Cleanup would not address the need to install optional features."
    },
    {
        "question": "A technician needs to strengthen security controls against brute-force attacks. Which of the following options best meets this requirement?",
        "options": [
            "Multifactor authentication",
            "Encryption",
            "Increased password complexity",
            "Secure password vault"
        ],
        "correct_answer": 1,
        "description": "The correct answer is multifactor authentication. This adds an additional layer of security, requiring more than just a password, making it more difficult for attackers to succeed with brute-force attacks.\n\n- Encryption protects data but doesn't address login security directly.\n- Increased password complexity helps, but it is not as effective without multifactor authentication.\n- Secure password vaults help manage passwords but do not directly prevent brute-force attacks."
    },
  {
    "question": "A user is experiencing the following issues with Bluetooth on a smartphone:\n\n• The user cannot hear any sound from a speaker paired with the smartphone.\n• The user is having issues synchronizing data from their smartwatch, which is also connected via Bluetooth.\n\nA technician checked the Bluetooth settings, confirmed it is successfully paired with a speaker, and adjusted the volume levels, but still could not hear anything. Which of the following steps should the technician take next to troubleshoot the Bluetooth issues?",
    "options": [
        "Restart the smartphone.",
        "Reset the network settings.",
        "Unpair the Bluetooth speaker.",
        "Check for system updates."
    ],
    "correct_answer": 1,
    "description": "The correct answer is to restart the smartphone. Restarting can help clear temporary issues affecting Bluetooth functionality.\n\n- Unpairing the Bluetooth speaker may be helpful if the issue persists, but restarting the device is a good first step.\n- Resetting the network settings could help, but it's more drastic and might not be necessary.\n- Checking for system updates is always good practice, but this issue seems related to the immediate Bluetooth functionality."
    },
    {
        "question": "A technician is building a new desktop machine for a user who will be using the workstation to render 3-D promotional movies. Which of the following is the most important component?",
        "options": [
            "Dedicated GPU",
            "DDR5 SODIMM",
            "NVMe disk",
            "64-bit CPU"
        ],
        "correct_answer": 1,
        "description": "The correct answer is dedicated GPU. Rendering 3D movies requires substantial graphical processing power, making a dedicated GPU the most crucial component for performance.\n\n- DDR5 SODIMM is important for memory, but the GPU is far more critical in rendering tasks.\n- NVMe disk speeds up data access but is not as important as a dedicated GPU for rendering.\n- A 64-bit CPU is needed for modern systems, but the GPU will have a more significant impact on rendering."
    },
    {
    "question": "A technician is troubleshooting a PC that is unable to perform DNS lookups. Utilizing the following firewall output:\n\nProtocol/Port  |  Action  |  Direction\n--------------------------------------------\n1               |  Allow   |  Out\n445             |  Block   |  Out\n53              |  Block   |  Out\n123             |  Block   |  Out\n80              |  Block   |  Out\n\nWhich of the following ports should be opened to allow for DNS recursion?",
    "options": [
        "1",
        "53",
        "80",
        "123",
        "445"
    ],
    "correct_answer": 2,
    "description": "The correct answer is port 53. DNS uses port 53 for both UDP and TCP traffic to perform lookups and recursion.\n\n- Port 1 is typically reserved for system processes and is not used for DNS.\n- Port 80 is used for HTTP traffic, not DNS.\n- Port 123 is used by NTP (Network Time Protocol), not DNS.\n- Port 445 is used by SMB (Server Message Block), unrelated to DNS."
    },
    {
        "question": "When a user attempts to open an email using a company-issued smartphone, the user receives a message stating the email is encrypted and cannot be opened. The user forwards the email to a personal account and receives the same message. The user then contacts the IT department for assistance. The technician instructs the user to contact the sender to exchange information in order to decode the message. Which of the following will the user receive from the sender?",
        "options": [
            "Keys",
            "Token",
            "Password",
            "Root CA"
        ],
        "correct_answer": 1,
        "description": "The correct answer is keys. When an email is encrypted, the recipient needs the decryption keys from the sender to open the message.\n\n- A token is used for authentication, not for decrypting an email.\n- A password may be required for accessing encrypted data, but decryption keys are what are needed for emails.\n- Root CA refers to certificate authorities used for secure connections, not for decrypting emails."
    },
    {
        "question": "Which of the following statements describes the purpose of scripting languages?",
        "options": [
            "To access the hardware of the computer it is running on",
            "To automate tasks and reduce the amount of manual labor",
            "To abstract the complexity of the computer system",
            "To compile the program into an executable file"
        ],
        "correct_answer": 2,
        "description": "The correct answer is to automate tasks and reduce the amount of manual labor. Scripting languages are primarily used to automate repetitive tasks, saving time and effort.\n\n- Accessing hardware is not the primary purpose of scripting languages; that’s typically done with lower-level programming languages.\n- Scripting languages can simplify the system, but their core purpose is automation.\n- Compiling into an executable file is related to compiled programming languages, not scripting languages."
    },
    {
        "question": "A technician is setting up a printer on a Linux workstation. Which of the following commands should the technician use to set the default printer?",
        "options": [
            "lpr",
            "lspool",
            "lpstat",
            "lpoptions"
        ],
        "correct_answer": 4,
        "description": "The correct answer is lpoptions. This command allows the technician to configure options for the printer, including setting the default printer.\n\n- lpr is used to send a job to the printer, not to configure it.\n- lspool lists print jobs in the print queue, but does not manage printer settings.\n- lpstat displays printer status but doesn't change configuration."
    },
    {
        "question": "A user's work PC has been the target of multiple phishing attacks. Which of the following is a way for the user to prevent further attacks?",
        "options": [
            "Enabling Windows Firewall",
            "Activating the email spam filter",
            "Using a secure VPN connection",
            "Running vulnerability scans on a schedule"
        ],
        "correct_answer": 2,
        "description": "The correct answer is activating the email spam filter. Phishing attacks often come through email, so filtering out spam is a direct way to reduce the risk of these attacks.\n\n- Enabling the firewall is important for network security but doesn't directly address phishing via email.\n- A secure VPN connection protects data in transit, but it doesn't prevent phishing attacks.\n- Running vulnerability scans is useful for detecting system weaknesses, but it does not directly prevent phishing attacks."
    },
    {
        "question": "A technician is troubleshooting a Windows system that is having issues with the OS loading at startup. Which of the following should the technician do to diagnose the issue?",
        "options": [
            "Enable boot logging on the system.",
            "Launch the last known-good configuration.",
            "Check the system resource usage in Task Manager.",
            "Run the sfc /scannow command.",
            "Use the Event Viewer to open the application log."
        ],
        "correct_answer": 1,
        "description": "The correct answer is to enable boot logging on the system. This will create a log of the boot process, which can help identify what is preventing the system from starting properly.\n\n- Launching the last known-good configuration may resolve the issue but doesn't provide diagnostic details.\n- Checking system resource usage and running sfc /scannow are more general troubleshooting steps, not specifically for boot issues.\n- The Event Viewer can be helpful for diagnosing issues after the OS loads, but boot logging is more directly related to startup problems."
    },


#491 - 500


    {
        "question": "A payroll server has data on it that needs to be readily available and can be recovered quickly if something is accidentally removed. Which of the following backup methods should be used to provide the fastest data recovery in this situation?",
        "options": [
            "Full",
            "Differential",
            "Synthetic",
            "Incremental"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Full backup. Full backups provide a complete copy of all data, which allows for the fastest recovery as no other backups need to be restored first. \n\n- Differential backups store changes made since the last full backup, requiring more time to restore. \n- Synthetic backups combine full and incremental backups but are more complex. \n- Incremental backups only store changes since the last backup, which may result in slower recovery times."
    },
    {
    "question": "A company recently experienced a security incident in which a USB drive containing malicious software was able to covertly install malware on a workstation. Which of the following actions should be taken to prevent this incident from happening again? (Choose two.)",
    "options": [
        "Install a host-based IDS.",
        "Restrict log-In times.",
        "Enable a BIOS password.",
        "Update the password complexity.",
        "Disable AutoRun.",
        "Restrict user permissions."
    ],
    "correct_answer": [4, 5],
    "description": "The correct answers are Install a host-based IDS and Disable AutoRun. A host-based IDS will help detect suspicious activity, while disabling AutoRun prevents malicious software from executing automatically when a USB is inserted. \n\n- Restricting log-in times and updating password complexity are security measures but do not directly address the USB malware risk. \n- A BIOS password does not stop the execution of malicious software from external devices. \n- Restricting user permissions can help but is not as effective as disabling AutoRun."
    },

    {
        "question": "A user is trying to limit the amount of time their children spend on the internet. Which of the following Windows 10 settings should be enabled to accomplish this objective?",
        "options": [
            "Family Options",
            "Update & Security",
            "Ease of Access",
            "Network & Internet",
            "Privacy"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Family Options. This setting allows parents to set time limits on their children's device usage and monitor their activity. \n\n- Update & Security focuses on system updates and security, not time management. \n- Ease of Access is meant for users with disabilities, not for managing internet usage. \n- Network & Internet settings are for configuring network connections, not usage limits. \n- Privacy settings control data sharing, not internet time limits."
    },
    {
        "question": "A user reports that a new, personally owned tablet will not connect to the corporate Wi-Fi network. The user is able to connect to the Wi-Fi network with other devices, and the tablet is running the latest software. Which of the following is the most likely cause of the issue?",
        "options": [
            "Incorrect encryption settings",
            "Blocked MAC address",
            "Outdated drivers",
            "Disabled location services"
        ],
        "correct_answer": 2,
        "description": "The correct answer is Blocked MAC address. Corporate networks often use MAC address filtering to restrict access, and the tablet's MAC address might be blocked. \n\n- Incorrect encryption settings would prevent all devices from connecting, not just this tablet. \n- Outdated drivers could be an issue, but the tablet is running the latest software, making this less likely. \n- Disabled location services would not affect Wi-Fi connectivity."
    },


        {
        "question": "A technician is on site dealing with an angry customer. The customer thinks the issues have not been addressed, while the technician thinks that the issue has been correctly resolved. Which of the following should the technician do to best handle the situation?",
        "options": [
            "Insist that the customer is correct and document the concern.",
            "Listen to the customer and do not speak at all.",
            "Escalate the issue to the next tier.",
            "Apologize and ask what would help resolve the issue."
        ],
        "correct_answer": 4,
        "description": "The correct answer is Apologize and ask what would help resolve the issue. This approach shows empathy and focuses on finding a solution to the customer’s concerns. \n\n- Insisting the customer is correct without understanding their issue does not resolve the situation. \n- Listening without speaking may leave the customer feeling ignored. \n- Escalating the issue might be necessary, but addressing the concern directly first is better."
    },




    {
        "question": "Which of the following should be documented to ensure that the change management plan is followed?",
        "options": [
            "Scope of the change",
            "Purpose of the change",
            "Change rollback plan",
            "Change risk analysis"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Scope of the change. Documenting the scope ensures that the change management plan is followed and that the change is within defined limits. \n\n- The purpose of the change is useful but does not define the boundaries of what is being changed. \n- A change rollback plan is critical but is a part of risk management, not scope. \n- Change risk analysis helps assess potential impacts but does not ensure the change itself is controlled."
    },
    {
        "question": "A technician needs to upgrade a legacy system running on a 32-bit OS with new applications that can work both on a 32-bit and a 64-bit system. The legacy system is critically important to the organization. The IT manager cautions that the new applications must not have a detrimental effect on company finances. Which of the following impacts is the IT manager most concerned with?",
        "options": [
            "Device",
            "Business",
            "Network",
            "Operation"
        ],
        "correct_answer": 2,
        "description": "The correct answer is Business. The IT manager is concerned about the financial impact of introducing new applications, which could affect the company's operations and revenue. \n\n- Device impact concerns hardware compatibility. \n- Network impact focuses on communication systems and connectivity. \n- Operational impact would be more focused on performance or functionality rather than financial risks."
    },
    {
    "question": "A technician is modifying the default home page of all the workstations in a company. Which of the following will help to implement this change?",
    "options": [
        "Insist that the customer is correct and document the concern.",
        "Listen to the customer and do not speak at all.",
        "Escalate the issue to the next tier.",
        "Apologize and ask what would help resolve the issue."
    ],
    "correct_answer": [4],
    "description": "The correct answer is Apologize and ask what would help resolve the issue. This approach demonstrates empathy, helping the technician to better understand the customer's concerns and find a solution to the problem. \n\n- Insisting that the customer is correct and documenting the concern is not the most effective way to handle the situation and does not directly address the customer's needs. \n- Listening to the customer without responding may create confusion and lead to a lack of resolution. \n- Escalating the issue to the next tier may not be necessary if the technician can handle the issue directly by resolving the problem and addressing the customer's concerns."
    },


    {
        "question": "A technician is troubleshooting a Windows 10 PC that is unable to start the GUI. A new SSD and a new copy of Windows were recently installed on the PC. Which of the following is the most appropriate command to use to fix the issue?",
        "options": [
            "msconfig",
            "chkdsk",
            "sfc",
            "diskpart",
            "mstsc"
        ],
        "correct_answer": 3,
        "description": "The correct answer is sfc (System File Checker). sfc scans and repairs system files that could be causing the GUI startup issue. \n\n- msconfig is used for startup settings but does not fix file issues. \n- chkdsk checks and repairs disk errors, but the issue is more likely related to system files. \n- diskpart is used for disk management, not file repairs. \n- mstsc is for remote desktop connections, not troubleshooting local issues."
    },
    {
        "question": "A technician is troubleshooting a PC because the user has reported strange pop-up windows and computer performance issues. Which of the following actions should the technician take next?",
        "options": [
            "Isolate the machine from the network.",
            "Scan the system for hidden files.",
            "Disable unused ports.",
            "Install antivirus software.",
            "Reconfigure the firewall."
        ],
        "correct_answer": 1,
        "description": "The correct answer is Isolate the machine from the network. Isolating the machine prevents potential spreading of malware or further harm while troubleshooting. \n\n- Scanning for hidden files is useful but may not address the root cause. \n- Disabling unused ports might not solve the immediate issue. \n- Installing antivirus software is important but should follow isolation. \n- Reconfiguring the firewall may not prevent the existing malware from causing further issues."
    },



#501-530


{
    "question": "A technician has been unable to remediate a persistent malware infection on a user's workstation. After the technician reinstalled the OS, the malware infection returned later that day. Which of the following is the most likely source?",
    "options": [
        "Trojan",
        "Boot sector virus",
        "Spyware",
        "Rootkit"
    ],
    "correct_answer": 4,
    "description": "The correct answer is Rootkit. Rootkits are known for deeply embedding themselves within a system, often evading typical detection and removal processes. \n\n- Trojans may replicate but generally don't survive a full OS reinstall. \n- Boot sector viruses can persist through reinstallation but are typically detected in the initial troubleshooting. \n- Spyware generally does not possess the same resilience to OS reinstalls as a rootkit. Rootkits, however, can remain on a system by hiding in system files and may need specialized tools or procedures to fully remove."
},
    {
        "question": "A technician is doing a bare-metal installation of the Windows 10 operating system. Which of the following prerequisites must be in place before the technician can start the installation process?",
        "options": [
            "Internet connection",
            "Product key",
            "Sufficient storage space",
            "UEFI firmware",
            "Legacy BIOS"
        ],
        "correct_answer": 3,
        "description": "The correct answer is Sufficient storage space. Windows 10 requires a minimum amount of storage space for installation, so the technician must ensure this is available. \n\n- An Internet connection is not required for initial OS installation, though it may be useful for updates. \n- A product key is necessary for activation but not installation. \n- UEFI firmware and Legacy BIOS are boot options but not requirements for a Windows installation on bare metal."
    },
    {
        "question": "Which of the following operating systems would most likely be used to run the inventory management system at a factory?",
        "options": [
            "Windows",
            "Chrome OS",
            "Android",
            "iOS"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Windows. It is commonly used in factories for running inventory and management software due to its compatibility with enterprise applications and hardware support. \n\n- Chrome OS is mostly used for personal devices and limited software. \n- Android and iOS are designed for mobile use and lack the capabilities for complex inventory management systems."
    },
    {
        "question": "A company using Active Directory wants to change the location of all users' \"Documents\" to a file server on the network. Which of the following should the company set up to accomplish this task?",
        "options": [
            "Security groups",
            "Folder redirection",
            "Organizational unit structure",
            "Access control list"
        ],
        "correct_answer": 2,
        "description": "The correct answer is Folder redirection. It allows administrators to redirect the path of a folder to a network location, ensuring users' files are saved to the file server. \n\n- Security groups are used for managing permissions but do not change file storage locations. \n- Organizational unit structures help manage users and computers but don’t control file paths. \n- Access control lists define permissions but don’t affect file locations."
    },
    {
        "question": "A technician is creating a location on a Windows workstation for a customer to store meeting minutes. Which of the following commands should the technician use?",
        "options": [
            "c:\\minutes",
            "dir",
            "rmdir",
            "md"
        ],
        "correct_answer": 4,
        "description": "The correct answer is md. This command creates a new directory, allowing the technician to set up a designated folder for meeting minutes. \n\n- 'c:\\minutes' is a file path but not a command. \n- 'dir' lists files and directories, not create them. \n- 'rmdir' removes directories, so it would not be used to create a new one."
    },
    {
        "question": "Which of the following is the most likely reason a filtration system is critical for data centers?",
        "options": [
            "Plastics degrade over time.",
            "High humidity levels can rust metal.",
            "Insects can invade the data center.",
            "Dust particles can clog the machines."
        ],
        "correct_answer": 4,
        "description": "The correct answer is Dust particles can clog the machines. Dust can accumulate inside hardware, leading to overheating and performance issues, so data centers require filtration to maintain equipment. \n\n- Plastic degradation and rust are issues, but a clean environment addresses dust. \n- Insects are possible but are less controlled by filtration systems."
    },
    {
        "question": "Which of the following Linux commands would help to identify which directory the user is currently operating in?",
        "options": [
            "pwd",
            "dig",
            "find",
            "cat"
        ],
        "correct_answer": 1,
        "description": "The correct answer is pwd (print working directory). This command displays the current directory path. \n\n- 'dig' is a DNS lookup utility unrelated to directory paths. \n- 'find' searches files but does not show the current directory. \n- 'cat' is for viewing file contents and does not display directory locations."
    },
    {
        "question": "Which of the following authentication methods should be used for BYOD wireless devices?",
        "options": [
            "Local certificates",
            "TACACS+",
            "RADIUS",
            "Captive portal"
        ],
        "correct_answer": 3,
        "description": "The correct answer is RADIUS. This centralized authentication protocol is commonly used for network access control, including BYOD wireless. \n\n- Local certificates may require complex setup. \n- TACACS+ is typically used for network equipment authentication rather than user device access. \n- A captive portal does not provide full authentication security."
    },
{
    "question": "A user recently downloaded a free game application on an Android device. The device then began crashing frequently and quickly losing its battery charge. Which of the following should the technician recommend be done first to remediate these issues? (Choose two.)",
    "options": [
        "Uninstall the game application.",
        "Perform a factory reset of the device.",
        "Connect the device to an external charger.",
        "Install the latest security patches.",
        "Clear the application's cache.",
        "Enable the device's built-in anti-malware protection."
    ],
    "correct_answer": [1, 4],
    "description": "The correct answers are to Uninstall the game application and Install the latest security patches. Uninstalling the game removes the suspected source of the issues, likely addressing the crashes and rapid battery drain. Installing security patches ensures the device has the latest protections against vulnerabilities. \n\n- Performing a factory reset could resolve the issue but may result in unnecessary data loss. \n- Connecting to an external charger would not address the underlying software problem. \n- Clearing the application's cache may improve performance slightly but will not fix potential malware."
},







    {
        "question": "A user is setting up a new Windows 10 laptop. Which of the following Windows settings should be used to input the SSID and password?",
        "options": [
            "Network & Internet",
            "System",
            "Personalization",
            "Accounts"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Network & Internet. This setting allows users to manage network connections and input the SSID and password. \n\n- 'System' manages hardware and system properties. \n- 'Personalization' customizes the user interface. \n- 'Accounts' manages user profiles, not network connections."
    },

    
    {
        "question": "A customer is configuring on an old desktop an inexpensive file server to share photos and videos and wants to avoid complicated licensing. Which of the following operating systems should the technician most likely recommend?",
        "options": [
            "Chrome OS",
            "Linux",
            "macOS",
            "Windows"
        ],
        "correct_answer": 2,
        "description": "The correct answer is Linux. Linux offers a variety of free, open-source server options suitable for file sharing and has fewer licensing restrictions, making it an ideal choice for a low-cost file server.\n\n- Chrome OS is limited to Chrome's ecosystem and lacks server functionalities.\n- macOS has licensing and cost constraints, especially for server use.\n- Windows often requires licenses, which can increase costs for basic file-sharing needs."
    },
    {
        "question": "A technician is following the ticketing system's best practices when handling user support requests. Which of the following should the technician do first when responding to a user support request that contains insufficient information?",
        "options": [
            "Ask the user for clarification.",
            "Keep the user updated on the progress.",
            "Document the root cause.",
            "Follow the system's escalation process."
        ],
        "correct_answer": 1,
        "description": "The correct answer is to ask the user for clarification. Obtaining all necessary information at the beginning enables accurate troubleshooting.\n\n- Updating the user on progress is important but should follow after understanding the issue fully.\n- Documenting the root cause is premature until the problem is identified.\n- Escalation should only occur if the technician cannot resolve the issue."
    },
    {
        "question": "Which of the following is used to prevent automobiles from crashing into a building?",
        "options": [
            "Cameras",
            "Bollard",
            "Lighting",
            "Biometrics"
        ],
        "correct_answer": 2,
        "description": "The correct answer is bollard. Bollards are physical barriers designed to block or slow down vehicles, protecting buildings and pedestrians.\n\n- Cameras and lighting help with surveillance but do not physically prevent vehicle access.\n- Biometrics control personnel access but are not relevant to vehicle barriers."
    },
    {
        "question": "Which of the following operating systems uses the ext4 filesystem type?",
        "options": [
            "macOS",
            "iOS",
            "Linux",
            "Windows"
        ],
        "correct_answer": 3,
        "description": "The correct answer is Linux. The ext4 filesystem is commonly used by Linux systems due to its compatibility and reliability for storage.\n\n- macOS and iOS typically use APFS, while Windows uses NTFS or FAT32."
    },
    {
        "question": "A user wants to acquire antivirus software for a SOHO PC. A technician recommends a licensed software product, but the user does not want to pay for a license. Which of the following license types should the technician recommend?",
        "options": [
            "Corporate",
            "Open-source",
            "Personal",
            "Enterprise"
        ],
        "correct_answer": 2,
        "description": "The correct answer is open-source. Open-source antivirus software can be used without purchasing a license, meeting the user's requirement for cost-free protection.\n\n- Corporate, personal, and enterprise licenses generally imply paid or restricted access."
    },
    {
        "question": "A technician needs to track evidence for a forensic investigation on a Windows computer. Which of the following describes this process?",
        "options": [
            "Valid license",
            "Data retention requirements",
            "Material safety data sheet",
            "Chain of custody"
        ],
        "correct_answer": 4,
        "description": "The correct answer is chain of custody. In forensic investigations, maintaining a clear chain of custody ensures evidence is documented and secure from tampering.\n\n- Other options do not relate directly to evidence handling in forensic contexts."
    },
    {
        "question": "Which of the following describes a concept that requires using a combination of an ID, a password, and a biometric?",
        "options": [
            "Types of security",
            "Access control",
            "Principle of least privilege",
            "Multifactor authentication"
        ],
        "correct_answer": 4,
        "description": "The correct answer is multifactor authentication. Multifactor authentication enhances security by requiring multiple forms of identification.\n\n- Other options are related to security but do not specify the requirement for multiple identification types."
    },
    {
        "question": "A technician is troubleshooting a smartphone that is unable to download and install the latest OS update. The technician notices the device operates more slowly than expected, even after rebooting and closing all applications. Which of the following should the technician check next?",
        "options": [
            "Application permissions",
            "Available storage space",
            "Battery charge level",
            "Wi-Fi connection speed"
        ],
        "correct_answer": 2,
        "description": "The correct answer is available storage space. Limited storage can prevent updates and impact performance.\n\n- Checking permissions, battery, and Wi-Fi is useful but less directly related to OS updates and performance slowdowns."
    },
    {
        "question": "A SOHO wireless router needs to be configured so incoming traffic is only allowed on specified ports. Which of the following is the best way for the technician to accomplish this task?",
        "options": [
            "Physically secure access to the router.",
            "Implement AES encryption.",
            "Install the latest firmware.",
            "Disable Universal Plug and Play."
        ],
        "correct_answer": 4,
        "description": "The correct answer is disabling Universal Plug and Play (UPnP). Disabling UPnP limits access to specific ports and helps prevent unauthorized access.\n\n- Other options do not directly restrict incoming traffic or provide targeted security."
    },
    {
        "question": "The calendar application on an employee's smartphone is experiencing frequent crashes, and the smartphone has become unresponsive. Which of the following should a technician do first to resolve the issue?",
        "options": [
            "Reinstall the application on the smartphone.",
            "Update the smartphone's OS.",
            "Reset the smartphone to factory settings.",
            "Reboot the smartphone."
        ],
        "correct_answer": 4,
        "description": "The correct answer is reboot the smartphone. Rebooting is a simple initial troubleshooting step that can resolve many performance issues.\n\n- Other options are more invasive and should be tried if rebooting does not work."
    },
    {
        "question": "Which of the following is the Windows OS that only recognizes 4GB of RAM?",
        "options": [
            "The Home version OS",
            "The 32-bit OS",
            "The 64-bit OS",
            "The trial version OS"
        ],
        "correct_answer": 2,
        "description": "The correct answer is the 32-bit OS. 32-bit versions of Windows have a maximum memory limit of 4GB.\n\n- Other versions (Home, 64-bit) do not have the same restriction on RAM recognition."
    },

#522




    {
        "question": "A company is requiring its staff to work remotely and needs to ensure remote access to servers and fileshares is secure. Which of the following should the company implement? (Choose two.)",
        "options": [
            "RDP",
            "VPN",
            "FTP",
            "VLAN",
            "Telnet",
            "HTTPS",
            "DHCP"
        ],
        "correct_answers": [2, 6],
        "description": "The correct answers are VPN and HTTPS. A VPN (Virtual Private Network) secures the remote connection by encrypting the data, making it safer for employees to access company servers remotely. HTTPS (HyperText Transfer Protocol Secure) ensures that any web-based access to fileshares or servers is encrypted, adding an extra layer of security.\n\n- RDP is useful for remote desktop access but lacks encryption by itself.\n- FTP is unsecure as it transmits data in plain text.\n- VLAN is for segmenting network traffic internally, not for securing remote access.\n- Telnet is outdated and insecure, transmitting data unencrypted.\n- DHCP assigns IP addresses but doesn’t secure remote access."
    },
{
    "question": "A user receives an error message on a Windows 10 device when trying to access a mapped drive from a Windows XP machine in the office. Other Windows XP devices in the office can access the drive. Which of the following Control Panel utilities should the user select to enable connectivity to the device?",
    "options": [
        "Devices and Printers",
        "Administrative Tools",
        "Network and Sharing Center",
        "Programs and Features"
    ],
    "correct_answer": 2,
    "description": "The correct answer is Administrative Tools. Administrative Tools provides various system utilities that can help with advanced configurations and troubleshooting, which may be necessary to enable connectivity with legacy systems like Windows XP.\n\n- Devices and Printers is for managing peripherals, not network connections.\n- Network and Sharing Center is primarily for managing active connections and settings but may not address compatibility with legacy systems.\n- Programs and Features is used for managing installed applications, not network connectivity."
},
    {
        "question": "An administrator received a new shipment of mobile devices. Per company policy, all enterprise-issued devices must have two authentication methods, and the organization has already enforced the use of PIN codes as one method. Which of the following device features should the administrator enable?",
        "options": [
            "Smart card",
            "Biometrics",
            "Hard token",
            "One-time password"
        ],
        "correct_answer": 2,
        "description": "The correct answer is Biometrics. Biometrics provides a secondary form of authentication, such as fingerprint or facial recognition, which enhances security by adding another layer beyond the PIN.\n\n- Smart cards and hard tokens require separate devices, which may not be suitable for mobile.\n- One-time passwords are valid temporarily and do not offer persistent authentication as biometrics does."
    },
    {
        "question": "Which of the following is the best way to limit the loss of confidential data if an employee's company smartphone is lost or stolen?",
        "options": [
            "Installing a VPN",
            "Implementing location tracking",
            "Configuring remote wipe",
            "Enabling backups"
        ],
        "correct_answer": 3,
        "description": "The correct answer is configuring remote wipe. Remote wipe allows data to be erased from a lost or stolen device, protecting confidential information.\n\n- A VPN secures data in transit but does not protect stored data on the device.\n- Location tracking helps locate the device but does not secure or erase data.\n- Backups help recover data but do not prevent data loss from the device."
    },
    {
        "question": "A customer, whose smartphone's screen was recently repaired, reports that the device has no internet access through Wi-Fi. The device shows that it is connected to Wi-Fi, has an address of 192.168.1.42, and has no subnet mask. Which of the following should the technician check next?",
        "options": [
            "Internal antenna connections",
            "Static IP settings",
            "Airplane mode",
            "Digitizer calibration"
        ],
        "correct_answer": 2,
        "description": "The correct answer is static IP settings. Since the device has an IP address but lacks a subnet mask, checking and configuring static IP settings may resolve connectivity issues.\n\n- Internal antenna connections are likely unrelated if the device connects to Wi-Fi.\n- Airplane mode would disable all wireless connections, but Wi-Fi is active.\n- Digitizer calibration affects touch functionality, not network settings."
    },
    {
        "question": "A computer is restarting automatically and displaying the following error message:\n\nYour PC ran into a problem and needs to restart. We’re just collecting some error info, and then we’ll restart for you. (0% complete).\n\nWhich of the following should the technician do first to diagnose the issue?",
        "options": [
            "Check the system event logs.",
            "Verify the hardware driver versions.",
            "Install Windows updates.",
            "Perform a RAM diagnostic."
        ],
        "correct_answer": 1,
        "description": "The correct answer is to check the system event logs. Event logs provide detailed error information, helping identify the cause of the restart.\n\n- Verifying hardware drivers, installing updates, and running diagnostics are helpful but should follow log analysis to determine specific causes."
    },
    {
        "question": "An IT technician is attempting to access a user’s workstation on the corporate network but needs more information from the user before an invitation can be sent. Which of the following command-line tools should the technician instruct the user to run?",
        "options": [
            "nslookup",
            "tracert",
            "hostname",
            "gpresult"
        ],
        "correct_answer": 3,
        "description": "The correct answer is hostname. This command shows the workstation’s name, which the technician needs for remote access.\n\n- nslookup and tracert are network diagnostics unrelated to system names.\n- gpresult provides group policy results, which are not necessary for remote access."
    },
    {
        "question": "A technician needs to upgrade the operating system on 200 lab computers to the latest version of Linux. Which of the following is the fastest upgrade method?",
        "options": [
            "Starting up from the USB flash drive",
            "Cloning each computer’s hard drive",
            "Installing from a network share",
            "Using the Windows Subsystem for Linux"
        ],
        "correct_answer": 3,
        "description": "The correct answer is installing from a network share. This method allows multiple computers to access the installation files simultaneously, making it the fastest for large-scale upgrades.\n\n- USB flash drives require individual handling.\n- Cloning is time-intensive and requires setup for each device.\n- Windows Subsystem for Linux is not a full Linux installation solution."
    },
    {
        "question": "A user’s antivirus software reports an infection that it is unable to remove. Which of the following is the most appropriate way to remediate the issue?",
        "options": [
            "Disable System Restore.",
            "Utilize a Linux live disc.",
            "Quarantine the infected system.",
            "Update the anti-malware."
        ],
        "correct_answer": 3,
        "description": "The correct answer is to quarantine the infected system. Quarantining isolates the infection, preventing it from spreading and protecting other systems until further remediation.\n\n- Disabling System Restore may help remove certain malware but does not contain the threat.\n- A Linux live disc may help detect the infection but does not contain it initially.\n- Updating anti-malware is useful but may not address immediate containment needs."
    },

#531


    {
        "question": "Which of the following is the best reason for sandbox testing in change management?",
        "options": [
            "To evaluate the change before deployment",
            "To obtain end-user acceptance",
            "To determine the affected systems",
            "To select a change owner"
        ],
        "correct_answer": 1,
        "description": "The correct answer is to evaluate the change before deployment. Sandbox testing allows IT teams to simulate the effects of a change in a controlled environment, helping to identify potential issues without affecting production. \n\n- Obtaining end-user acceptance is a later step, typically part of the deployment or post-deployment review. \n- Determining affected systems is part of the planning phase and can be completed before sandbox testing. \n- Selecting a change owner is part of the change management process but is unrelated to testing."
    },
    {
        "question": "A customer calls desktop support and begins yelling at a technician. The customer claims to have submitted a support ticket two hours ago and complains that the issue still has not been resolved. Which of the following describes how the technician should respond?",
        "options": [
            "Place the customer on hold until the customer calms down.",
            "Disconnect the call to avoid a confrontation.",
            "Wait until the customer is done speaking and offer assistance.",
            "Escalate the issue to a supervisor."
        ],
        "correct_answer": 3,
        "description": "The correct answer is to wait until the customer is done speaking and offer assistance. This approach shows empathy and professionalism, allowing the technician to address the issue once the customer has been heard. \n\n- Placing the customer on hold may increase frustration, as it can be seen as dismissive. \n- Disconnecting the call is generally inappropriate and may escalate the situation. \n- Escalating to a supervisor may be necessary later, but initially, allowing the customer to speak often helps in de-escalation."
    },
    {
        "question": "Which of the following operating systems was the .app file type designed to run under as an application file bundle?",
        "options": [
            "macOS",
            "Chrome",
            "Windows",
            "Linux"
        ],
        "correct_answer": 1,
        "description": "The correct answer is macOS. The .app file type is used on macOS as an application bundle format, containing the resources and binaries required to run the application. \n\n- Chrome OS does not natively support .app bundles. \n- Windows uses .exe files for applications, not .app bundles. \n- Linux has various package formats but does not natively recognize .app as a standard application format."
    },

#535


    {
        "question": "A healthcare organization wants to provide iPads to the nursing staff. Which of the following accounts would provide the least privilege to the users?",
        "options": [
            "Guest",
            "Root",
            "Superuser",
            "Administrator"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Guest. A Guest account provides minimal access, granting only the basic functionality necessary for temporary use without modifying system settings. \n\n- Root and Superuser accounts have full administrative control over the system, which exceeds the minimum required privileges for nursing staff. \n- The Administrator account also provides elevated privileges that would not align with the principle of least privilege."
    },
    {
        "question": "A user clicked on a link in an email and was redirected to a web page. Now, some commonly used websites are not accessible. A technician confirms that other users are not experiencing the same issue. Which of the following steps should the technician take next to properly identify the issue?",
        "options": [
            "Check the hosts file.",
            "Review the laptop’s IP settings",
            "Enable the Windows Firewall.",
            "Verify if the wireless router is functioning."
        ],
        "correct_answer": 1,
        "description": "The correct answer is to check the hosts file. The hosts file may have been modified during the user's browsing session, redirecting the user to malicious or incorrect websites. \n\n- Reviewing the IP settings may help if there are network configuration issues, but this seems less likely given that other users are unaffected. \n- Enabling the Windows Firewall is unlikely to resolve this specific issue, as the firewall does not affect DNS or redirection. \n- Verifying the wireless router is functioning is also unnecessary because other users are not experiencing the same issue."
    },
    {
    "question": "A technician is installing a new copy of Windows on all computers in the enterprise. Given the following requirements:\n\n• The install phase must be scripted to run over the network.\n• Each computer requires a new SSD as the system drive.\n• The existing HDD should remain as a backup drive\n\nWhich of the following command-line tools should the technician use to install the drive and transfer the installation files from the network share? (Choose three.)",
    "options": [
        "net use",
        "robocopy",
        "winver",
        "diskpart",
        "sfc",
        "netstat",
        "ping",
        "chkdsk"
    ],
    "correct_answer": [1, 3, 4],
    "description": "The correct answers are 'net use', 'winver', and 'diskpart'. \n\n- 'net use' allows the technician to map a network drive, facilitating access to the network share for installation files. \n- 'winver' checks the Windows version, which can ensure compatibility with the installation. \n- 'diskpart' is used to partition the new SSDs and configure them for installation. \n\n- 'robocopy' is useful for copying files but not necessary for the installation itself. \n- 'sfc' checks for system file integrity, which is not relevant during installation. \n- 'netstat' and 'ping' are for network troubleshooting, which is unnecessary for the installation process."
},
    {
        "question": "A newly hired employee is trying to enroll a personal mobile device in the company's mobile device management system. After the initial attempt, the employee receives a notification stating, \"not compliant - call support.\" Which of the following is the reason why the employee is receiving this message?",
        "options": [
            "More RAM is needed.",
            "AirDrop is not enabled.",
            "The device has been jailbroken.",
            "The account has no profile picture."
        ],
        "correct_answer": 3,
        "description": "The correct answer is 'The device has been jailbroken'. Jailbreaking removes restrictions placed on the device by the manufacturer, which can create security risks and cause non-compliance with the organization's MDM system. \n\n- More RAM would not affect compliance with the MDM system. \n- AirDrop not being enabled is unrelated to device compliance with MDM systems. \n- The lack of a profile picture does not typically cause non-compliance issues."
    },
    {
        "question": "A technician is modifying the default home page of all the workstations in a company. Which of the following will help to implement this change?",
        "options": [
            "Group Policy",
            "Browser extension",
            "System Configuration",
            "Task Scheduler"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Group Policy. Group Policy allows administrators to centrally manage and enforce settings across multiple workstations, including setting a default homepage for browsers. \n\n- A browser extension would require manual installation on each workstation, which is inefficient for managing large numbers of computers. \n- System Configuration is typically used for configuring system startup options, not browser settings. \n- Task Scheduler is used for automating tasks but is not suitable for enforcing browser settings."
    },
    {
        "question": "A technician is implementing the latest application security updates for endpoints on an enterprise network. Which of the following solutions should the technician use to ensure device security on the network while adhering to industry best practices?",
        "options": [
            "Automate the patching process",
            "Monitor the firewall configuration",
            "Implement access control lists.",
            "Document all changes."
        ],
        "correct_answer": 1,
        "description": "The correct answer is to automate the patching process. Automation ensures that devices are consistently updated with the latest security patches, reducing the risk of vulnerabilities. \n\n- Monitoring the firewall configuration is important for network security but does not directly address application security updates. \n- Implementing access control lists is useful for controlling network access but does not address the patching process. \n- Documenting changes is important for tracking but is not a proactive security measure."
    },
{
    "question": "A user's File Explorer keeps crashing. The technician is troubleshooting and tries the following:\n\n• Runs Windows Update\n• Runs CHKDSK and SFC /scannow\n• Clears File Explorer history\n\nWhich of the following actions should the technician take next?",
    "options": [
        "Roll back the most recent set of Windows updates.",
        "Reimage the computer and ask the user to test.",
        "Test the computer's memory.",
        "Repartition the boot drive."
    ],
    "correct_answer": 3,
    "description": "The correct answer is to test the computer's memory. If the memory is faulty, it can cause application crashes, including File Explorer. \n\n- Rolling back the most recent set of Windows updates may not address potential hardware-related issues that could cause the crashes. \n- Reimaging the computer could be a drastic solution, but it may not be necessary unless other solutions fail. \n- Repartitioning the boot drive is unlikely to resolve issues related to application crashes caused by memory problems."
},
{
        "question": "A company installed WAPs and deployed new laptops and docking stations to all employees. The docking stations are connected via LAN cables. Users are now reporting degraded network service. The IT department has determined that the WAP mesh network is experiencing a higher than anticipated amount of traffic. Which of the following would be the most efficient way to ensure the wireless network can support the expected number of wireless users?",
        "options": [
            "Replacing non-mobile users' laptops with wired desktop systems",
            "Increasing the wireless network adapter metric",
            "Adding wireless repeaters throughout the building",
            "Upgrading the current mesh network to support the 802.11n specification"
        ],
        "correct_answer": 4,
        "description": "The correct answer is to upgrade the current mesh network to support the 802.11n specification. This upgrade would increase the wireless network's bandwidth and efficiency, allowing it to handle more traffic. \n\n- Replacing laptops with desktops would not address the issue of high wireless network traffic. \n- Increasing the wireless network adapter metric has limited impact on improving overall network performance. \n- Adding wireless repeaters would increase coverage but could also degrade network performance due to additional traffic on the mesh network."
    },
    {
        "question": "A customer needs to verify an executable file that the customer downloaded from a website. Which of the following should the customer use to verify the file?",
        "options": [
            "Password manager",
            "BitLocker",
            "File Vault",
            "Checksum",
            "Secure site"
        ],
        "correct_answer": 4,
        "description": "The correct answer is Checksum. A checksum is used to verify the integrity of a file by comparing the hash value of the downloaded file to the expected hash value. \n\n- Password manager stores and generates credentials, not for file verification. \n- BitLocker and File Vault are used for encryption, not file verification. \n- A secure site ensures secure browsing but does not verify file integrity after download."
    },

#544
{
    "question": "A technician needs to implement a backup and recovery solution that will ensure executives’ laptops can be restored if needed. The plan should include the capability to perform granular and whole-disk recovery. Which of the following are the best options for the technician to successfully implement the plan? (Choose two.)",
    "options": [
        "RAID",
        "Volume shadow copy",
        "Incremental backup",
        "System restore",
        "Grandfather-father-son backup",
        "Disk imaging"
    ],
    "correct_answer": [2, 6],
    "description": "The correct answers are 'Volume shadow copy' and 'Disk imaging'. \n\n- 'Volume shadow copy' allows for creating backup copies or snapshots of data while the system is running, providing the ability for granular recovery of files and whole-disk recovery. \n- 'Disk imaging' creates an exact copy of the entire disk, allowing for full restoration of the system, including the operating system, applications, and user data. \n\n- 'RAID' is primarily used for data redundancy and fault tolerance, not specifically for backup and recovery. \n- 'Incremental backup' only backs up changes made since the last backup, which might not meet the requirement for whole-disk recovery. \n- 'System restore' is used for rolling back the operating system to a previous state but may not fully restore the laptop as needed. \n- 'Grandfather-father-son backup' is a backup rotation scheme, not a method for performing granular or whole-disk recovery."
},
{
    "question": "A technician is configuring a SOHO router and wants to only allow specific computers on the network. Which of the following should the technician do?",
    "options": [
        "Configure MAC filtering.",
        "Disable DHCP.",
        "Configure port forwarding.",
        "Disable guest access."
    ],
    "correct_answer": 1,
    "description": "The correct answer is 'Configure MAC filtering'. \n\n- 'MAC filtering' allows the technician to specify which devices are allowed to connect to the network by filtering based on their MAC addresses, ensuring only specific devices can access the network. \n\n- 'Disabling DHCP' would stop the router from assigning IP addresses automatically, which could disrupt the network, especially for devices that rely on dynamic addressing. \n- 'Configuring port forwarding' is used to direct traffic to specific devices or services on the network but does not limit access to the network itself. \n- 'Disabling guest access' would block unauthorized users from connecting to a guest network, but does not restrict specific computers on the primary network."
},
{
    "question": "A technician is adding some Windows 10 workstations to the corporate domain. A script was able to add the majority of the workstations, but failed on a couple. Which of the following menus should the technician check in order to complete the task manually?",
    "options": [
        "User Accounts",
        "System Properties",
        "Windows Firewall",
        "Network and Sharing"
    ],
    "correct_answer": 2,
    "description": "The correct answer is 'System Properties'. \n\n- 'System Properties' contains the option to join a computer to a domain, which is necessary to complete the task manually. \n\n- 'User Accounts' manages local and domain user accounts but does not handle domain joining. \n- 'Windows Firewall' may block domain-joining attempts, but it is not the first place to check for domain configuration. \n- 'Network and Sharing' deals with network connections and sharing settings but does not directly handle domain-joining."
},
{
    "question": "A technician is troubleshooting a user's PC that is running slowly and displaying frequent pop-ups. The technician thinks malware may be causing the issues, but before the issues began the user installed anti-malware software in response to a pop-up window. Which of the following is the most likely cause of these issues?",
    "options": [
        "Expired certificate",
        "False alert",
        "Missing system files",
        "OS update failure"
    ],
    "correct_answer": 2,
    "description": "The correct answer is 'False alert'. \n\n- A 'False alert' is often triggered by malware disguised as legitimate security software, which can create pop-ups to encourage the installation of more malicious software. \n\n- 'Expired certificates' typically affect secure connections and are unlikely to cause frequent pop-ups or performance issues. \n- 'Missing system files' can cause stability problems but are less likely to be related to pop-ups. \n- 'OS update failure' might affect system performance but would not typically cause pop-ups related to malware."
},
{
    "question": "A customer called the help desk to report that a new USB CD drive is not working. Which of the following tools should the technician use to diagnose the issue?",
    "options": [
        "lusrmgr.msc",
        "devmgmt.msc",
        "certmgr.msc",
        "perfmon.msc"
    ],
    "correct_answer": 2,
    "description": "The correct answer is 'devmgmt.msc'. \n\n- 'devmgmt.msc' opens Device Manager, where the technician can check if the USB CD drive is recognized by the system and troubleshoot hardware-related issues. \n\n- 'lusrmgr.msc' is used to manage user accounts and groups, not hardware devices. \n- 'certmgr.msc' is for managing certificates and would not help with diagnosing a USB drive issue. \n- 'perfmon.msc' is used to monitor system performance and resource usage, which is unrelated to diagnosing hardware issues."
},
{
    "question": "Which of the following is used to generate passcodes necessary to access applications or systems that require an extra layer of security?",
    "options": [
        "Authenticator application",
        "Access control lists",
        "Biometrics",
        "Smart card readers"
    ],
    "correct_answer": 1,
    "description": "The correct answer is 'Authenticator application'. \n\n- 'Authenticator application' generates time-based one-time passcodes that provide an additional layer of security for accessing applications or systems. \n\n- 'Access control lists' manage permissions and access control but are not used to generate passcodes. \n- 'Biometrics' uses physical characteristics like fingerprints or facial recognition but is not a passcode generator. \n- 'Smart card readers' are used for authentication but do not generate passcodes themselves; they rely on smart cards with embedded credentials."
},
{
    "question": "A user reports receiving constant, unwanted pop-ups and being unable to close the browser window. These issues have impacted the user's productivity and may have caused the user's files to be altered. Which of the following should a technician do to address these issues with minimal impact to the user?",
    "options": [
        "Use System Restore to recover the OS files.",
        "Wipe the computer and install a new copy of the OS.",
        "Identify whether the disk partition table has been reduced in size.",
        "Perform a full-system, antivirus scan and check browser notifications."
    ],
    "correct_answer": 4,
    "description": "The correct answer is 'Perform a full-system, antivirus scan and check browser notifications'. \n\n- A full-system antivirus scan is the most effective way to identify and remove malware that may be causing the pop-ups and file alterations. Checking browser notifications can also reveal if the issue is browser-based. \n\n- 'System Restore' can be helpful if the issue is related to a recent change but may not address ongoing malware infections. \n- 'Wiping the computer and installing a new copy of the OS' would have a large impact on the user and should only be considered as a last resort. \n- 'Identifying whether the disk partition table has been reduced in size' is unrelated to resolving pop-ups or browser issues."
},

#551


    {
        "question": "A customer wants to make sure the data is protected and secure on a Windows laptop's hard drive. Which of the following is the best solution?",
        "options": [
            "Windows Backup",
            "BitLocker",
            "Shadow Copy",
            "Trusted Platform Module"
        ],
        "correct_answer": 2,
        "description": "The correct answer is BitLocker. BitLocker provides full disk encryption, ensuring data is encrypted and only accessible with the proper authentication, significantly enhancing data security.\n\n- Windows Backup only saves data to another location but doesn't secure it on the device.\n- Shadow Copy allows for backup versions but does not secure the data itself.\n- Trusted Platform Module supports encryption but doesn’t directly secure the drive like BitLocker does."
    },
    {
        "question": "Employees at comptia.org are reporting getting a usual amount of emails from a coworker. A technician discovers the emails were sent from the following address: john@cOmptia.org. Which of the following social engineering attacks is this an example of?",
        "options": [
            "Whaling",
            "Insider threat",
            "Phishing",
            "Vishing",
            "Evil twin"
        ],
        "correct_answer": 3,
        "description": "The correct answer is Phishing. Phishing involves impersonating a trusted source (in this case, a coworker) to deceive recipients and potentially gather sensitive information.\n\n- Whaling targets high-profile individuals specifically.\n- Insider threat refers to an internal staff member acting maliciously.\n- Vishing involves voice calls, not emails.\n- Evil twin relates to fake Wi-Fi networks, not email spoofing."
    },
    {
        "question": "A web developer installs and launches a new external web server. Immediately following the launch, the performance of all traffic traversing the firewall degrades substantially. Which of the following considerations was overlooked?",
        "options": [
            "OS compatibility",
            "Quality of service",
            "32- vs. 64-bit architecture",
            "Storage requirements"
        ],
        "correct_answer": 2,
        "description": "The correct answer is Quality of Service (QoS). QoS allows prioritization of network traffic, which helps prevent performance degradation when new services, like an external web server, increase network demand.\n\n- OS compatibility is unlikely to cause network-wide slowdowns.\n- 32- vs. 64-bit architecture affects processing capability but not network traffic.\n- Storage requirements affect data storage, not network performance."
    },
    {
        "question": "A technician is setting up a network printer for a customer who has a SOHO router. The technician wants to make sure the printer stays connected in the future and is available on all the computers in the house. Which of the following should the technician configure on the printer?",
        "options": [
            "DNS settings",
            "Static IP",
            "WWAN",
            "Metered connection"
        ],
        "correct_answer": 2,
        "description": "The correct answer is Static IP. Assigning a static IP ensures the printer’s IP address remains constant, so it remains accessible to other devices in the network.\n\n- DNS settings control name resolution but won’t keep the IP static.\n- WWAN is for cellular connectivity, not needed here.\n- Metered connection limits data but doesn’t ensure consistent connectivity."
    },
    {
        "question": "A web server is configured to only allow secure connections. Which of the following will a user most likely use to connect to the web server?",
        "options": [
            "TFTP",
            "HTTP",
            "FTP",
            "TLS"
        ],
        "correct_answer": 4,
        "description": "The correct answer is TLS. Transport Layer Security (TLS) ensures a secure connection, which is essential for web servers that only allow secure traffic.\n\n- TFTP and FTP are insecure protocols, not suitable here.\n- HTTP is also unencrypted, unlike HTTPS, which would use TLS."
    },
    {
        "question": "Which of the following is protected by government policy for end user information?",
        "options": [
            "DRM",
            "EULA",
            "PCI",
            "PII"
        ],
        "correct_answer": 4,
        "description": "The correct answer is PII. Personally Identifiable Information (PII) is protected by policies to ensure privacy and security of personal data.\n\n- DRM protects digital media rights.\n- EULA covers software usage terms.\n- PCI protects payment card information, not personal user data broadly."
    },
    {
        "question": "Which of the following allows users to access connected system features through account federation?",
        "options": [
            "MFA",
            "NAC",
            "SSO",
            "UAC"
        ],
        "correct_answer": 3,
        "description": "The correct answer is SSO (Single Sign-On). SSO enables users to access multiple applications with a single login, using federated identity management.\n\n- MFA enhances security but doesn’t provide account federation.\n- NAC controls network access, unrelated to login federation.\n- UAC manages permissions on a single system, not across federated accounts."
    },
    {
        "question": "A technician has identified malicious traffic originating from a user's computer. Which of the following is the best way to identify the source of the attack?",
        "options": [
            "Investigate the firewall logs.",
            "Isolate the machine from the network.",
            "Inspect the Windows Event Viewer.",
            "Take a physical inventory of the device."
        ],
        "correct_answer": 1,
        "description": "The correct answer is to Investigate the firewall logs. Firewall logs can provide detailed information on network traffic, helping identify the source of malicious activity.\n\n- Isolating the machine is a containment step but doesn’t identify the source.\n- Windows Event Viewer logs system events, but may not track network-level threats.\n- Physical inventory doesn’t relate to identifying a cyber attack source."
    },
    {
        "question": "A company was recently attacked by ransomware. The IT department has remediated the threat and determined that the attack method used was email. Which of the following is the most effective way to prevent this issue from reoccurring?",
        "options": [
            "Spam filtering",
            "Malware prevention software",
            "End user education",
            "Stateful firewall inspection"
        ],
        "correct_answer": 3,
        "description": "The correct answer is End user education. Educating users on phishing and safe email practices helps prevent future ransomware attacks.\n\n- Spam filtering reduces unwanted emails but doesn’t address user behavior.\n- Malware prevention software is helpful but won’t stop all threats if users don’t recognize risky behavior.\n- Stateful firewall inspection aids in network security but won’t prevent user-targeted email attacks."
    },
    {
        "question": "Which of the following ensures data is unrecoverable on a lost or stolen mobile device?",
        "options": [
            "Device encryption",
            "Remote wipe",
            "Data backup",
            "Fingerprint reader"
        ],
        "correct_answer": 2,
        "description": "The correct answer is Remote wipe. Remote wipe removes all data from the device if lost or stolen, ensuring it is unrecoverable.\n\n- Device encryption protects data but doesn’t actively delete it.\n- Data backup preserves data but doesn’t secure it from unauthorized access.\n- Fingerprint readers add security but don’t prevent data recovery if compromised."
    },
    {
        "question": "Remote employees need access to information that is hosted on local servers at the company. The IT department needs to find a solution that gives employees secure access to the company's resources as if the employees were on premises. Which of the following remote connection services should the IT team implement?",
        "options": [
            "SSH",
            "VNC",
            "VPN",
            "RDP"
        ],
        "correct_answer": 3,
        "description": "The correct answer is VPN (Virtual Private Network). VPNs provide secure, encrypted connections, enabling remote access to internal resources as though on-site.\n\n- SSH is used for secure command-line access but doesn’t mimic local network presence.\n- VNC and RDP allow screen sharing, not secure network-wide access."
    },

#562
 {
        "question": "A user's corporate iPhone had issues and was repaired while the user was on vacation. The mobile phone has applications on it that are unavailable to be downloaded from the application store when compared to an identical phone. Which of the following best describes what is happening to the phone?",
        "options": [
            "APK Source",
            "Connectivity issues",
            "Developer Mode",
            "Jailbreak"
        ],
        "correct_answer": 4,
        "description": "The correct answer is Jailbreak. Jailbreaking allows installation of apps outside the official app store, potentially enabling unauthorized applications to be installed, as in this case. \n\n- APK Source refers to Android app packages, not iOS. \n- Connectivity issues wouldn't affect app availability. \n- Developer Mode is mainly for app development and testing, not for bypassing app store restrictions."
    },



{
    "question": "A technician is upgrading the Microsoft Windows 10 OS. Which of the following are required for the technician to safely upgrade the OS? (Choose two.)",
    "options": [
        "Release notes",
        "Antivirus software",
        "Backup of critical data",
        "Device drivers",
        "Word processing software",
        "Safe boot mode"
    ],
    "correct_answer": [3, 4],
    "description": "The correct answers are Backup of critical data and Device drivers. Backing up critical data ensures no important information is lost if any issues arise during the OS upgrade. \n\n- Device drivers should be up-to-date and compatible with the new OS version to avoid compatibility issues post-upgrade. \n- Release notes are informative but not required for the upgrade. \n- Antivirus software, Word processing software, and Safe boot mode are not essential for the OS upgrade process."
},




    {
        "question": "A user received an alert from a Windows computer indicating low storage space. Which of the following will best resolve this issue?",
        "options": [
            "Reviewing System information",
            "Running Disk Cleanup",
            "Editing the Registry",
            "Checking the Performance Monitor",
            "Increasing the memory"
        ],
        "correct_answer": 2,
        "description": "The correct answer is Running Disk Cleanup. Disk Cleanup can quickly free up storage space by removing unnecessary files such as temporary files and system cache. \n\n- Reviewing System information only provides details on system configuration. \n- Editing the Registry is risky and should not be used for storage issues. \n- Performance Monitor is primarily for monitoring system performance, not managing storage. \n- Increasing memory (RAM) will not address storage space issues on the hard drive."
    },
    {
        "question": "An employee has been using the same password for multiple applications and websites for the past several years. Which of the following would be best to prevent security issues?",
        "options": [
            "Configuring firewall settings",
            "Implementing expiration policies",
            "Defining complexity requirements",
            "Updating antivirus definitions"
        ],
        "correct_answer": 2,
        "description": "The correct answer is Implementing expiration policies. Expiration policies force users to regularly update their passwords, reducing the risk associated with using the same password over long periods. \n\n- Firewall settings control network access, not password security. \n- Complexity requirements are helpful but do not encourage password changes. \n- Updating antivirus definitions is essential for malware protection but does not address password management."
    },
    {
        "question": "A technician is deploying a new Wi-Fi solution for the office and wants to ensure users can log in to the Wi-Fi with their existing network log-in and password. Which of the following methods should the technician use?",
        "options": [
            "AES",
            "RADIUS",
            "TKIP",
            "WPA3"
        ],
        "correct_answer": 2,
        "description": "The correct answer is RADIUS. RADIUS enables network authentication, allowing users to use their existing credentials to access the Wi-Fi network securely. \n\n- AES is an encryption standard, not a login protocol. \n- TKIP is an older encryption protocol and does not handle authentication. \n- WPA3 improves security but does not directly support using network credentials for login."
    },
    {
        "question": "A technician is troubleshooting a Windows 10 PC that has experienced a BSOD. The user recently installed optional Windows updates. Which of the following is best way to resolve the issue?",
        "options": [
            "Enable System Restore",
            "Roll back the device drivers",
            "Reinstall the OS",
            "Update the BIOS"
        ],
        "correct_answer": 2,
        "description": "The correct answer is Roll back the device drivers. If the BSOD occurred after a recent update, reverting to previous drivers can resolve compatibility issues. \n\n- System Restore might help but would revert other recent changes as well. \n- Reinstalling the OS is a drastic solution and should only be a last resort. \n- Updating the BIOS is unrelated to Windows updates and driver issues."
    },
    {
        "question": "A user clicked a link in an email, and now the cursor is moving around on its own. A technician notices that File Explorer is open and data is being copied from the local drive to an unknown cloud storage location. Which of the following should the technician do first?",
        "options": [
            "Investigate the reported symptoms",
            "Run anti-malware software",
            "Educate the user about dangerous links",
            "Quarantine the workstation"
        ],
        "correct_answer": 4,
        "description": "The correct answer is Quarantine the workstation. Quarantining prevents further data loss and stops the malware from spreading to other systems. \n\n- Investigating symptoms may take time and delay containment. \n- Running anti-malware software is important but should follow isolation steps. \n- Educating the user can happen afterward to prevent future incidents."
    },
    {
        "question": "An administrator needs to back up the following components of a single workstation: \n\n• The installation of the operating system \n• Applications \n• User profiles \n• System settings \n\nWhich of the following backup methods can the administrator use to ensure the workstation is properly backed up?",
        "options": [
            "Differential",
            "Image",
            "Synthetic",
            "Archive"
        ],
        "correct_answer": 2,
        "description": "The correct answer is Image. An image backup creates a complete snapshot of the system, including the OS, applications, user profiles, and settings, allowing for full system restoration if needed. \n\n- Differential backups only save changes made since the last backup. \n- Synthetic and archive backups serve different purposes and do not capture the entire system."
    },
    {
        "question": "A technician was assigned a help desk ticket and resolved the issue. Which of the following should the technician update to assist other technicians in resolving similar issues?",
        "options": [
            "End user training",
            "Progress notes",
            "Knowledge base",
            "Acceptable use policy document"
        ],
        "correct_answer": 3,
        "description": "The correct answer is Knowledge base. Updating the knowledge base allows other technicians to reference the solution in future cases. \n\n- End user training and acceptable use policy documents are for user awareness and compliance. \n- Progress notes are specific to the ticket and not intended for general reference."
    },
    {
        "question": "Which of the following would typically require the most computing resources from the host computer?",
        "options": [
            "Chrome OS",
            "Windows",
            "Android",
            "macOS",
            "Linux"
        ],
        "correct_answer": 2,
        "description": "The correct answer is Windows. Windows often requires more CPU, memory, and storage compared to other operating systems due to its extensive features and background processes. \n\n- Chrome OS and Android are optimized for lower resources. \n- macOS and Linux are generally less resource-intensive than Windows."
    },
    {
        "question": "A user's Windows computer seems to work well at the beginning of the day. However, its performance degrades throughout the day, and the system freezes when several applications are open. Which of the following should a technician do to resolve the issue? (Choose two.)",
        "options": [
            "Install the latest GPU drivers",
            "Reinstall the OS",
            "Increase the RAM",
            "Increase the hard drive space",
            "Uninstall unnecessary software",
            "Disable scheduled tasks"
        ],
        "correct_answer": [3, 5],
        "description": "The correct answers are Increase the RAM and Uninstall unnecessary software. Adding RAM helps the computer handle more applications simultaneously, while removing unneeded software reduces system load. \n\n- Updating GPU drivers may not address memory-related slowdowns. \n- Reinstalling the OS is a drastic step. \n- Increasing hard drive space and disabling tasks won’t directly solve memory limitations."
    },

#572


    {
        "question": "A user's Windows computer seems to work well at the beginning of the day. However, its performance degrades throughout the day, and the system freezes when several applications are open. Which of the following should a technician do to resolve the issue? (Choose two.)",
        "options": [
            "Install the latest GPU drivers.",
            "Reinstall the OS.",
            "Increase the RAM.",
            "Increase the hard drive space.",
            "Uninstall unnecessary software.",
            "Disable scheduled tasks."
        ],
        "correct_answer": [3, 5],
        "description": "The correct answers are Increase the RAM and Uninstall unnecessary software. Increasing RAM can enhance system performance by providing more memory for running applications, reducing lag and crashes. \n\n- Uninstalling unnecessary software frees up system resources, helping to improve performance. \n- Installing GPU drivers is unlikely to resolve the main issue as it pertains to overall system memory. \n- Reinstalling the OS is a drastic measure and may not address the underlying resource constraints."
    },
    {
        "question": "Which of the following languages is used for scripting the creation of Active Directory accounts?",
        "options": [
            "Bash",
            "Structured Query Language",
            "Hypertext Preprocessor",
            "PowerShell"
        ],
        "correct_answer": 4,
        "description": "The correct answer is PowerShell. PowerShell is a powerful scripting language commonly used for Windows administration, including automating tasks like Active Directory account creation. \n\n- Bash is more commonly used in Unix-based systems. \n- Structured Query Language (SQL) is primarily for database management. \n- Hypertext Preprocessor (PHP) is for web development and is not related to system administration tasks."
    },
    {
        "question": "A customer reports that an Android phone will not allow the use of contactless electronic payment. Which of the following needs to be enabled to resolve the issue?",
        "options": [
            "Wi-Fi",
            "Nearby share",
            "NFC",
            "Bluetooth"
        ],
        "correct_answer": 3,
        "description": "The correct answer is NFC. Near Field Communication (NFC) is required for contactless payments, allowing secure and quick data exchange for transactions. \n\n- Wi-Fi, Nearby Share, and Bluetooth are unrelated to payment functionality."
    },
    {
        "question": "A technician is creating a Windows splash screen that details log-in expectations. Which of the following should the technician most likely use?",
        "options": [
            "End user license agreement",
            "Non-disclosure agreement",
            "Regulatory compliance",
            "Acceptable use policy"
        ],
        "correct_answer": 4,
        "description": "The correct answer is Acceptable use policy. The Acceptable Use Policy outlines rules and expectations for system use, which is appropriate for a log-in splash screen. \n\n- End User License Agreements, NDAs, and Regulatory Compliance are less relevant to daily user expectations."
    },
    {
        "question": "A user is troubleshooting an issue with a mobile phone that will no longer connect to a smart watch. The user has tried the following:\n\n• Reinstalling the smart watch application on the mobile phone\n• Enabling synchronization\n• Rebooting the phone\n\nWhich of the following should the user do next?",
        "options": [
            "Verify Bluetooth settings on the mobile phone.",
            "Connect the smart watch to Wi-Fi.",
            "Enable NFC on the smart watch.",
            "Turn on the mobile hotspot on the phone."
        ],
        "correct_answer": 1,
        "description": "The correct answer is Verify Bluetooth settings on the mobile phone. Bluetooth connectivity is required to pair the smart watch with the mobile phone. \n\n- Wi-Fi and NFC are unrelated to pairing with most smart watches. \n- Turning on a mobile hotspot is also unrelated to Bluetooth pairing."
    },
    {
        "question": "A user receives an email from what appears to be a trusted, known insider who is requesting confidential banking information. After the user further inspects the email, the user notices that one character in the email address is incorrect. Which of the following is being attempted?",
        "options": [
            "Evil twin",
            "Insider threat",
            "Zero-day attack",
            "Impersonation"
        ],
        "correct_answer": 4,
        "description": "The correct answer is Impersonation. Impersonation attacks involve pretending to be a trusted source to deceive the target, often by using a similar email address. \n\n- Evil twin attacks involve fake Wi-Fi networks. \n- Insider threats come from within the organization, while zero-day attacks exploit unknown vulnerabilities."
    },
    {
        "question": "A management team at a small office wants to block access to inappropriate websites and create a log of these access attempts. Which of the following is a way to meet these requirements?",
        "options": [
            "Content filter",
            "Screened subnet",
            "Port forwarding",
            "Access control list"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Content filter. A content filter blocks access to certain websites and can log access attempts, providing control over web usage. \n\n- Screened subnets, port forwarding, and access control lists do not directly manage web access or filtering."
    },
    {
        "question": "A network administrator is setting up the security for a SOHO wireless network. Which of the following options should the administrator enable to secure the network?",
        "options": [
            "NAT",
            "WPA3",
            "802.1X",
            "Static IP"
        ],
        "correct_answer": 2,
        "description": "The correct answer is WPA3. WPA3 is the latest Wi-Fi security standard, providing strong protection for wireless networks. \n\n- NAT and Static IPs do not directly secure wireless connections. \n- 802.1X is more suitable for enterprise environments."
    },
    {
        "question": "Which of the following environmental factors are most important to consider when planning the configuration of a data center? (Choose two.)",
        "options": [
            "Temperature levels",
            "Location of the servers",
            "Humidity levels",
            "Noise levels",
            "Lighting levels",
            "Cable management"
        ],
        "correct_answer": [1, 3],
        "description": "The correct answers are Temperature levels and Humidity levels. Maintaining optimal temperature and humidity is crucial to prevent overheating and component failure. \n\n- Noise, lighting, and cable management are less critical for data center operation and performance."
    },
    {
        "question": "A user's company phone has several pending software updates. A technician completes the following steps:\n\n• Rebooted the phone\n• Connected to Wi-Fi\n• Disabled metered data\n\nWhich of the following should the technician do next?",
        "options": [
            "Restore the factory settings.",
            "Clean the browser history.",
            "Uninstall and reinstall the applications.",
            "Clear the cache."
        ],
        "correct_answer": 4,
        "description": "The correct answer is Clear the cache. Clearing the cache can resolve update issues by freeing up storage or removing conflicting temporary files. \n\n- Factory reset and reinstalling applications are unnecessary and may cause data loss."
    },
    {
        "question": "A technician would like to repurpose hard drives that contain PII. Which of the following would be the best solution to securely remove the data?",
        "options": [
            "Drilling",
            "Degaussing",
            "Low-level formatting",
            "Incinerating"
        ],
        "correct_answer": 3,
        "description": "The correct answer is Low-level formatting. This method securely erases data by writing over each sector, making data recovery difficult. \n\n- Drilling and incinerating destroy the drive, while degaussing may not be as effective on modern drives."
    },
    {
        "question": "Which of the following documents in criminal proceedings must be updated every time a piece of evidence is touched or transferred in order for the evidence to be considered valid?",
        "options": [
            "Licensing agreement",
            "Regulatory compliance",
            "Incident documentation",
            "Chain of custody"
        ],
        "correct_answer": 4,
        "description": "The correct answer is Chain of custody. This document tracks evidence handling, ensuring that it remains unaltered and properly documented for court proceedings."
    },
    {
        "question": "An organization is updating the monitors on kiosk machines. While performing the upgrade, the organization would like to remove physical input devices. Which of the following utilities in the Control Panel can be used to turn on the on-screen keyboard to replace the physical input devices?",
        "options": [
            "Devices and Printers",
            "Ease of Access",
            "Programs and Features",
            "Device Manager"
        ],
        "correct_answer": 2,
        "description": "The correct answer is Ease of Access. This option provides accessibility tools, including an on-screen keyboard, useful when physical input devices are removed."
    },
    {
        "question": "A large organization is researching proprietary software with vendor support for a multiuser environment. Which of the following EULA types should be selected?",
        "options": [
            "Corporate",
            "Perpetual",
            "Open-source",
            "Personal"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Corporate. Corporate licenses are intended for multiuser environments with support options from vendors. \n\n- Perpetual licenses do not specify support, while open-source and personal licenses are unsuitable for organizational needs."
    },

    {
    "question": "A hotel’s Wi-Fi was used to steal information on a corporate laptop. A technician notes the following security log: \n\nSRC: 192.168.1.1/secrets.zip Protocol SMB >> DST: 192.268.1.50/capture \n\nThe technician analyzes the following Windows firewall information:\n\n| Port | Status | Direction |\n|------|--------|-----------|\n| 1    | Open   | In/Out    |\n| 445  | Open   | In/Out    |\n| 25   | Open   | Out       |\n| 110  | Open   | In/Out    |\n| 53   | Open   | In/Out    |\n\nWhich of the following protocols most likely allowed the data theft to occur?",
    "options": [
        "Port 1",
        "Port 53",
        "Port 110",
        "Port 445"
    ],
    "correct_answer": 4,
    "description": "The correct answer is Port 445. This port is commonly used by the Server Message Block (SMB) protocol, which enables file sharing over a network. The log shows 'Protocol SMB,' indicating that SMB was used to transfer sensitive files from the laptop. \n\n- Port 1 is not typically used for such data transfers and does not align with SMB.\n- Port 53 is generally used for DNS, handling name resolution rather than file transfers.\n- Port 110 is for POP3, which is associated with retrieving emails, not file sharing or SMB connections."
 },

 #588

 
    {
        "question": "A technician needs to configure a computer for a user to work from home so the user can still securely access the user's shared files and corporate email. Which of the following tools would best accomplish this task?",
        "options": [
            "MSRA",
            "FTP",
            "RMM",
            "VPN"
        ],
        "correct_answer": 4,
        "description": "The correct answer is VPN. VPNs provide a secure connection over the internet, allowing users to access corporate resources remotely. \n\n- MSRA is for remote assistance but does not provide secure access to corporate files. \n- FTP is used for file transfer but lacks security for accessing shared files and email. \n- RMM is for managing remote devices but doesn’t provide secure file and email access."
    },
{
    "question": "A technician received a notification about encrypted production data files and thinks active ransomware is on the network. The technician isolated and removed the suspicious system from the network. Which of the following steps should the technician take next?",
    "options": [
        "Schedule and perform an antivirus scan and system update.",
        "Educate the end user on internet usage.",
        "Perform a system scan to remove the malware.",
        "Create a system restore point."
    ],
    "correct_answer": 3,
    "description": "The correct answer is to perform a system scan to remove the malware. This step addresses the immediate need to remove the ransomware and prevent it from spreading further on the network. \n\n- Scheduling an antivirus scan and update is useful but is best done after removing the ransomware to ensure immediate threats are dealt with. \n- Educating the end user is beneficial for long-term prevention but does not resolve the current infection. \n- Creating a system restore point is helpful for recovery but should not be done while malware is potentially active."
},
    {
        "question": "A technician wants to improve password security after several users admitted to using very simple passwords. Which of the following is the best way to resolve this issue?",
        "options": [
            "Requiring four character types",
            "Decreasing the password expiration times",
            "Enabling an automatic lock timer",
            "Adding two characters to the minimum password length"
        ],
        "correct_answer": 1,
        "description": "The correct answer is requiring four character types. This approach strengthens passwords by ensuring a mix of uppercase, lowercase, numbers, and special characters. \n\n- Decreasing expiration times could prompt weak passwords. \n- Lock timers improve security but don’t impact password strength. \n- Increasing minimum length helps but isn’t as effective as enforcing character variety."
    },
    {
        "question": "A technician is working at a client office site and the technician’s family member repeatedly calls and texts about a non-emergency situation. Which of the following should the technician do?",
        "options": [
            "Step aside and answer.",
            "Put the phone on silent.",
            "Text a reply.",
            "Ignore the phone and continue working."
        ],
        "correct_answer": 2,
        "description": "The correct answer is to put the phone on silent. This maintains focus on work while preventing further interruptions. \n\n- Stepping aside might impact productivity unnecessarily. \n- Texting may encourage further messages. \n- Ignoring without silencing could still be distracting."
    },
    {
        "question": "A technician needs to ensure that USB devices are not suspended by the operating system. Which of the following Control Panel utilities should the technician use to configure the setting?",
        "options": [
            "System",
            "Power Options",
            "Recovery",
            "Ease of Access"
        ],
        "correct_answer": 2,
        "description": "The correct answer is Power Options. This utility includes settings for USB selective suspend, allowing USB devices to remain active. \n\n- System does not control USB power settings. \n- Recovery focuses on system restoration. \n- Ease of Access adjusts accessibility settings."
    },
    {
        "question": "A technician is an administrator on a messaging application for a private work group of mixed departments. One of the technician’s colleagues discloses to the group that their employer recently suffered a major security breach and shared details about the breach to the group. Which of the following should the technician do first?",
        "options": [
            "Ignore the messages as all of the group members work for the same employer.",
            "Remove the colleague from the group and ask members to delete the messages.",
            "Message the colleague privately and ask the colleague to delete the messages immediately.",
            "Contact the supervisor and report the colleague with screenshots of the messages."
        ],
        "correct_answer": 4,
        "description": "The correct answer is to contact the supervisor and report the colleague. Reporting ensures proper handling of sensitive information and prevents further exposure. \n\n- Ignoring the message can lead to potential security issues. \n- Removing the colleague without reporting may lack accountability. \n- A private message doesn’t fully address the disclosure issue."
    },
    {
        "question": "An enterprise user cannot authenticate to the office Wi-Fi. Which of the following steps should most likely be taken to resolve the issue?",
        "options": [
            "Reinstall the OS.",
            "Check the machine’s certificates.",
            "Resync the Group Policy.",
            "Power cycle the switch."
        ],
        "correct_answer": 2,
        "description": "The correct answer is checking the machine’s certificates. Wi-Fi authentication often relies on certificates, especially in enterprise environments. \n\n- Reinstalling the OS is excessive and may not address authentication. \n- Group Policy resync may not resolve certificate-related issues. \n- Power cycling the switch is unlikely to affect authentication."
    },
    {
        "question": "A user reported that Windows has crashed several times during the day. A technician needs to check error messages to determine whether the issue pertains to the hardware or an application. Which of the following tools the technician use?",
        "options": [
            "Event Viewer",
            "Resource Monitor",
            "Performance Monitor",
            "Device Manager"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Event Viewer. This tool logs system events, providing details on crashes and errors to help identify the cause. \n\n- Resource Monitor shows current system resource usage, not crash logs. \n- Performance Monitor tracks performance but lacks specific error logging. \n- Device Manager manages hardware drivers but doesn’t log crashes."
    },
    {
        "question": "While browsing the Internet, a customer sees a window stating antivirus protection is no longer functioning. Which of the following steps should a technician take next? (Choose two.)",
        "options": [
            "Isolate the computer from the network.",
            "Enable the firewall service.",
            "Update the endpoint protection software.",
            "Use System Restore to undo changes.",
            "Delete the browser cookies.",
            "Run sfc /scannow."
        ],
        "correct_answers": [1, 3],
        "description": "The correct answers are isolating the computer and updating the endpoint protection software. Isolation prevents potential malware spread, and updating endpoint protection ensures security is restored. \n\n- Enabling the firewall does not address antivirus issues directly. \n- System Restore may help, but it is not the primary solution. \n- Deleting cookies and running sfc are unrelated to antivirus function."
    },
    {
        "question": "During a routine check, a systems administrator discovers that a user’s PC is running slowly and CPU utilization is at 100%. Further investigation shows a large amount of resource usage. Which of the following is the most likely cause of the high resource usage?",
        "options": [
            "Firewall activities",
            "Botnet attack",
            "DDoS attack",
            "Keylogger attack"
        ],
        "correct_answer": 2,
        "description": "The correct answer is Botnet attack. Botnets can take over system resources, often leading to high CPU usage as they perform tasks like spamming or DDoS attacks. \n\n- Firewall activities would not cause such high CPU usage. \n- DDoS attacks target networks, not individual CPU resources. \n- Keyloggers don’t typically consume excessive resources."
    },
    {
        "question": "A technician needs to recommend a way to keep company devices for field and home-based staff up to date. The users live in various places across the country and the company has several national offices that staff can go to for technical support. Which of the following methods is most appropriate for the users?",
        "options": [
            "Make office attendance mandatory for one day per week so that updates can be installed.",
            "Ask users to ensure that they run updates on devices and reboot computers on a regular basis.",
            "Push updates out via VPN on a weekly basis in a staggered manner so that the network is not affected.",
            "Configure cloud-based endpoint management software to automatically manage computer updates."
        ],
        "correct_answer": 4,
        "description": "The correct answer is configuring cloud-based endpoint management software. This allows automatic, remote updates for users across various locations. \n\n- Mandatory office attendance is inconvenient and costly. \n- Relying on users to run updates may lead to inconsistent compliance. \n- VPN-based updates may affect network performance and user access."
    },


  {
    "question": "A user's Windows desktop has low disk space. A technician thinks some upgrade files were never removed. Which of the following tools should the technician use to correct the issue?",
    "options": [
      "devmgmt.msc",
      "cleanmgr.exe",
      "dfrgui.exe",
      "diskmgmt.msc"
    ],
    "correct_answer": 2,
    "description": "The correct answer is cleanmgr.exe. This tool is used to launch the Disk Cleanup utility, which allows the technician to remove unnecessary files, including upgrade files that may have been left behind. \n\n- devmgmt.msc is used to manage device drivers, not disk space. \n- dfrgui.exe is used for defragmenting disks, not for removing upgrade files. \n- diskmgmt.msc is used for managing disks and partitions, not for cleaning up unnecessary files."
  },
  {
    "question": "A user is unable to access the internet but can still print to network printers. Other users are not experiencing this issue. Which of the following steps should the technician take first to diagnose the issue?",
    "options": [
      "Validate physical connectivity.",
      "Reboot the router.",
      "Disable IPv6.",
      "Check the DNS settings."
    ],
    "correct_answer": 1,
    "description": "The correct answer is to validate physical connectivity. Since the user can print to network printers, the local network connection is likely working. The technician should first check the physical connection (e.g., cables, network port) to ensure that the computer is properly connected to the network. \n\n- Rebooting the router may be a solution but should not be the first step since it affects the entire network. \n- Disabling IPv6 is unlikely to solve the issue since it’s not typically the cause of limited internet access. \n- Checking DNS settings is a useful troubleshooting step, but physical connectivity issues should be ruled out first."
  }




]
