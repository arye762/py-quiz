questions_set_D = [
# 601

    {
        "question": "A user’s computer is running slower than usual and takes a long time to start up. Which of the following tools should the technician use first to investigate the issue?",
        "options": [
            "Action Center",
            "Task Manager",
            "Resource Monitor",
            "Security Configuration Wizard",
            "Event Viewer"
        ],
        "correct_answer": 2,
        "description": "The correct answer is Task Manager. Task Manager allows the technician to see processes using high CPU or memory resources, which can cause slowdowns. \n\n- Action Center provides security alerts but does not show real-time resource usage. \n- Resource Monitor shows detailed usage but is typically secondary to Task Manager. \n- Security Configuration Wizard is for setting up security configurations, not troubleshooting performance. \n- Event Viewer is used to review logs, not to identify real-time resource use."
    },
    {
        "question": "An organization’s critical database files were attacked with ransomware. The company refuses to pay the ransom for a decryption key. All traces of the infection have been removed from the underlying servers. Which of the following should the company do next?",
        "options": [
            "Scan all of the infected files with up-to-date anti-malware cleaning software.",
            "Fully patch the server operating systems hosting the fileshares.",
            "Change the files to be read-only.",
            "Restore critical data from backup."
        ],
        "correct_answer": 4,
        "description": "The correct answer is to restore critical data from backup. Backups allow the organization to retrieve unencrypted data without paying the ransom. \n\n- Anti-malware scanning is important but does not recover encrypted data. \n- Patching servers is preventive, not corrective, in this scenario. \n- Changing files to read-only will not decrypt them or restore lost data."
    },
    {
        "question": "A technician wants to securely dispose of storage drives. Which of the following is the best way to eliminate data on SSDs?",
        "options": [
            "Degaussing",
            "Shredding",
            "Erasing",
            "Drilling"
        ],
        "correct_answer": 2,
        "description": "The correct answer is shredding. Shredding physically destroys the SSD, ensuring data cannot be recovered. \n\n- Degaussing does not work on SSDs since they use flash memory. \n- Erasing may leave recoverable data. \n- Drilling may leave parts intact, allowing partial data recovery."
    },
    {
        "question": "A user submits a request to have a graphics application installed on a desktop. When the technician attempts to install the application, the installation fails and the error message 'Not compatible with OS' is displayed. Which of the following is the most likely reason for this error message?",
        "options": [
            "The graphics card driver needs to be updated.",
            "The application installer is 64-bit.",
            "The installation requires administrative rights.",
            "The disk space is inadequate."
        ],
        "correct_answer": 2,
        "description": "The correct answer is that the application installer is 64-bit. This error usually means the OS is incompatible with the application’s architecture. \n\n- Updating the graphics card driver is unrelated to compatibility. \n- Admin rights may be needed but don’t cause compatibility errors. \n- Disk space issues would prompt a different error."
    },
    {
        "question": "A technician is helping a customer connect to a shared drive. The technician notices some unused drives that have already been mapped and wants to disconnect those drives first. Which of the following commands should the technician use?",
        "options": [
            "format",
            "netstat",
            "diskpart",
            "net use",
            "rmdir"
        ],
        "correct_answer": 4,
        "description": "The correct answer is net use. This command shows and manages network drive mappings. \n\n- format is for preparing storage drives, not network mappings. \n- netstat checks network connections but not drive mappings. \n- diskpart manages local disks and partitions. \n- rmdir removes directories, not network drives."
    },
    {
        "question": "Which of the following language types enables the automation of tasks?",
        "options": [
            "Compiled",
            "Scripting",
            "Web",
            "Database"
        ],
        "correct_answer": 2,
        "description": "The correct answer is scripting. Scripting languages are often used for automating tasks in operating systems and applications. \n\n- Compiled languages are generally used for complete applications rather than automation. \n- Web languages focus on front-end development. \n- Database languages are for managing and querying databases."
    },
    {
        "question": "A company wants to take advantage of modern technology and transition away from face-to-face meetings. Which of the following types of software would benefit the company the most? (Choose two.)",
        "options": [
            "Videoconferencing",
            "File transfer",
            "Screen-sharing",
            "Financial",
            "Remote access",
            "Record-keeping"
        ],
        "correct_answer": [1, 3],
        "description": "The correct answers are videoconferencing and screen-sharing. Videoconferencing enables remote meetings, and screen-sharing allows collaboration in real time. \n\n- File transfer is not specifically for meetings. \n- Financial software is for accounting purposes. \n- Remote access is mainly for support, not meetings. \n- Record-keeping is unrelated to meetings."
    },
    {
        "question": "A user authenticates to Windows with a complex password. The user frequently makes errors when entering the password and gets locked out. Which of the following can ensure security while reducing user error? (Choose two.)",
        "options": [
            "Single sign-on",
            "Personal identification number",
            "Fingerprint",
            "Facial recognition",
            "Hardware token",
            "Multifactor authentication"
        ],
        "correct_answer": [3, 4],
        "description": "The correct answers are fingerprint and facial recognition. These biometrics offer secure, error-free access methods. \n\n- Single sign-on only reduces the number of passwords, not errors. \n- A PIN could still be mistyped. \n- Hardware tokens require additional setup. \n- Multifactor authentication can still involve complex passwords."
    },
    {
        "question": "A workstation does not recognize a printer. However, the previous day, the printer successfully received a job from the workstation. Which of the following tools should a technician use to see what happened before the failure?",
        "options": [
            "Performance Monitor",
            "Devices and Printers",
            "Task Scheduler",
            "Event Viewer"
        ],
        "correct_answer": 4,
        "description": "The correct answer is Event Viewer. Event Viewer logs system and application events, which can show if a failure or error affected the printer connection. \n\n- Performance Monitor tracks system resource usage, not peripheral status. \n- Devices and Printers displays connected devices but lacks event history. \n- Task Scheduler is for scheduled tasks, unrelated to diagnosing printer issues."
    },
    {
        "question": "Which of the following attacks can a hacker use to execute code on a user's computer when the user visits a specially prepared, malicious website?",
        "options": [
            "DoS",
            "Spoofing",
            "XSS",
            "SQL injection"
        ],
        "correct_answer": 3,
        "description": "The correct answer is XSS (Cross-Site Scripting). XSS attacks can inject malicious code into a user's browser when they visit a compromised website. \n\n- DoS attacks are for overloading a network or server, not code execution. \n- Spoofing is used to impersonate identities but does not involve code execution. \n- SQL injection targets databases, not browsers."
    },

#611


    {
        "question": "A user reports the following issues:\n\n• Their computer is constantly running slowly.\n• The default home page of the web browser has changed to a suspicious search engine.\n• They have been receiving pop-up ads on the screen.\n\nWhich of the following should a technician do first to address these issues?",
        "options": [
            "Update the antivirus program and run a full system scan",
            "Uninstall the suspicious search engine and reset the home page",
            "Install the latest updates for the operating system",
            "Block the pop-up ads using the web browser settings"
        ],
        "correct_answer": 1,
        "description": "The correct answer is to update the antivirus program and run a full system scan. This approach allows the technician to detect and remove any malware or adware causing the issues before making other adjustments.\n\n- Uninstalling the search engine and resetting the home page would address only part of the problem.\n- Installing OS updates would improve security but likely won’t resolve existing malware.\n- Blocking pop-ups in the browser settings would not eliminate malware causing the ads."
    },
    {
        "question": "Which of the following macOS file types requires mounting before installation?",
        "options": [
            ".pkg",
            ".zip",
            ".app",
            ".dmg"
        ],
        "correct_answer": 4,
        "description": "The correct answer is .dmg. A .dmg file is a disk image file commonly used in macOS. It needs to be mounted to access its contents before installation.\n\n- .pkg files are installer packages and do not require mounting.\n- .zip files are compressed files and do not need mounting to access.\n- .app files represent applications and do not require mounting."
    },
    {
    "question": "A smartphone user is experiencing issues getting an application to launch. When the user taps on the application name, nothing happens. The user recently updated the smartphone's OS. Which of the following steps should the technician take next to troubleshoot the issue?",
    "options": [
        "Roll back the OS update",
        "Uninstall the application",
        "Restart the smartphone",
        "Check for application updates"
    ],
    "correct_answer": 3,
    "description": "The correct answer is to restart the smartphone. A simple restart often resolves minor issues, especially after an OS update, by reloading the operating system and applications.\n\n- Rolling back the OS update could be an unnecessary step and is more complex.\n- Uninstalling the application might work but could cause the loss of user data or settings.\n- Checking for application updates might help but can be done after attempting a quick restart, which is generally faster and easier."
	},
    {
        "question": "A technician thinks that a computer on the network has been infected with malware. The technician attempts several times to use a malware removal tool, but the issue persists. Which of the following should the technician do next?",
        "options": [
            "Restore the computer from the last known-good backup",
            "Reboot the computer into safe mode",
            "Purchase a new endpoint protection tool",
            "Use system recovery to prevent further infection"
        ],
        "correct_answer": 2,
        "description": "The correct answer is to reboot the computer into safe mode. Safe mode restricts startup processes, potentially isolating the malware and allowing for more effective removal.\n\n- Restoring from backup might be an option if other steps fail.\n- Purchasing new protection software doesn’t address the immediate issue.\n- System recovery prevents re-infection but doesn’t resolve active malware."
    },
    {
        "question": "A technician receives a high-priority ticket about sensitive information collected from an end user's workstation. Which of the following steps should a technician take to preserve the chain of custody for a forensic investigation?",
        "options": [
            "Reimage the workstation",
            "Inform the user of the investigation",
            "Recover and secure the workstation",
            "Back up the workstation"
        ],
        "correct_answer": 3,
        "description": "The correct answer is to recover and secure the workstation. This step preserves evidence for investigation and maintains the integrity of data.\n\n- Reimaging would overwrite potential evidence.\n- Informing the user isn’t relevant to maintaining chain of custody.\n- Backing up may be useful but doesn’t ensure evidence integrity."
    },
    {
        "question": "A technician receives a migration audit stating that a desktop needs to be removed from the network and reimaged with a current OS. Which of the following is the most likely reason for the notification?",
        "options": [
            "MTBF exceeded",
            "Incompatible drivers",
            "End-of-life",
            "NTFS corruption"
        ],
        "correct_answer": 3,
        "description": "The correct answer is end-of-life. The desktop's OS may no longer be supported, making it a security risk.\n\n- MTBF (Mean Time Between Failures) relates to hardware, not OS lifecycle.\n- Incompatible drivers usually don’t require reimaging.\n- NTFS corruption may require repair but not OS replacement."
    },
    {
        "question": "A customer service representative is unable to send jobs to a printer at a remote branch office. However, the representative can print successfully to a local network printer. Which of the following commands should a technician use to view the path of the network traffic from the PC?",
        "options": [
            "netstat",
            "ping",
            "format",
            "tracert"
        ],
        "correct_answer": 4,
        "description": "The correct answer is tracert. This command maps the route to the remote printer, helping identify connectivity issues.\n\n- netstat shows active network connections but doesn’t map routes.\n- ping checks connectivity but doesn’t display the path.\n- format is irrelevant for network troubleshooting."
    },
    {
        "question": "A home office user wants to ensure a PC is backed up and protected against local natural disasters and hardware failures. Which of the following would meet the user's requirements?",
        "options": [
            "Using an agent-based cloud backup solution",
            "Implementing a grandfather-father-son backup rotation",
            "Automating backups to a local network share",
            "Saving files manually to an external drive"
        ],
        "correct_answer": 1,
        "description": "The correct answer is using an agent-based cloud backup solution. Cloud storage provides off-site backup, protecting against local disasters.\n\n- Grandfather-father-son backup lacks off-site storage.\n- Backups to local network share are also vulnerable to local disasters.\n- Manually saving to an external drive is prone to human error and lacks automation."
    },
    {
        "question": "A customer reports high data usage on a smartphone that reaches its monthly data limit within the first week of each billing cycle. The customer uses the phone primarily for calls and SMS messages with minimal content streaming. A technician troubleshoots the phone and notices that both developer mode and installs from unknown sources are enabled. Which of the following should the technician check next?",
        "options": [
            "Storage cache",
            "Malicious applications",
            "Privacy settings",
            "Permissions"
        ],
        "correct_answer": 2,
        "description": "The correct answer is malicious applications. High data usage suggests hidden processes possibly due to malware.\n\n- The storage cache wouldn't account for high data use.\n- Privacy settings don’t impact data usage.\n- Permissions could be checked later but wouldn’t cause data usage directly."
    },
    {
        "question": "A developer installed a new software package that has stopped all file server access. Which of the following change management practices should have been followed?",
        "options": [
            "End-user acceptance",
            "Staff delegation",
            "Appropriate scoping",
            "Sandbox testing"
        ],
        "correct_answer": 4,
        "description": "The correct answer is sandbox testing. Testing new software in an isolated environment ensures it won’t disrupt existing services.\n\n- End-user acceptance doesn’t apply to system testing.\n- Staff delegation refers to roles, not testing.\n- Appropriate scoping is important but wouldn’t prevent server access issues."
    },
    {
        "question": "A user takes a work-issued laptop home for the first time. When the user attempts to browse any website on the home internet, the user receives the following error:\n\n\"This site cannot be reached.\"\n\nA technician from work confirms that the static IP that was set up on the machine was changed back to DHCP. Which of the following needs to be corrected?",
        "options": [
            "HTTPS",
            "VLAN",
            "DNS",
            "SMTP"
        ],
        "correct_answer": 3,
        "description": "The correct answer is DNS. If the DNS settings are incorrect, the laptop won’t resolve URLs to IP addresses.\n\n- HTTPS is related to secure browsing but doesn’t resolve IP conflicts.\n- VLANs apply to network segmentation but not home access.\n- SMTP is for email, unrelated to this browsing issue."
    },

#622


    {
        "question": "After a local company office was destroyed by a hurricane, the company files an insurance claim for equipment replacement. The company maintained current, off-site backups. Which of the following is the most important information to provide to the insurance company?",
        "options": [
            "Inventory list",
            "Software licensing",
            "Warranty information",
            "Topology diagram"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Inventory list. Providing an inventory list helps the insurance company determine the equipment lost and the claim's validity. \n\n- Software licensing is important for compliance but not for hardware replacement. \n- Warranty information covers repairs, not replacements after a disaster. \n- A topology diagram shows network layout but does not verify equipment specifics."
    },
    {
        "question": "An organization wants to deploy a customizable operating system. Which of the following should the organization choose?",
        "options": [
            "Windows 10",
            "macOS",
            "Linux",
            "Chrome OS",
            "iOS"
        ],
        "correct_answer": 3,
        "description": "The correct answer is Linux. Linux is highly customizable, making it suitable for specialized configurations. \n\n- Windows 10 and macOS are customizable but with limitations compared to Linux. \n- Chrome OS is cloud-centric with limited customization. \n- iOS is a closed system with minimal customization options."
    },
    {
        "question": "Which of the following types of malware is designed to enable administrative access to a computer?",
        "options": [
            "Rootkit",
            "Trojan",
            "Worm",
            "Ransomware"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Rootkit. Rootkits are designed to hide within a system and provide administrative access to attackers. \n\n- Trojans disguise themselves as legitimate software but do not specifically grant administrative access. \n- Worms spread independently but do not grant administrative access. \n- Ransomware encrypts files but does not typically enable admin-level access."
    },
    {
        "question": "Which of the following applications allows a user to create backups in macOS?",
        "options": [
            "Time Machine",
            "FileVault",
            "Keychain",
            "Mission Control"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Time Machine. Time Machine is the default backup application in macOS, designed specifically for creating backups. \n\n- FileVault provides disk encryption, not backup. \n- Keychain manages passwords but does not handle backups. \n- Mission Control is a task management feature, not a backup tool."
    },
    {
        "question": "A location is experiencing under-voltage events during peak periods. Which of the following should be deployed at this location?",
        "options": [
            "Proper ventilation",
            "UPS",
            "Surge protector",
            "PDU"
        ],
        "correct_answer": 2,
        "description": "The correct answer is UPS. A UPS provides temporary power and voltage regulation, protecting against under-voltage. \n\n- Proper ventilation helps with temperature control, not power issues. \n- A surge protector guards against surges, not under-voltage. \n- A PDU distributes power but does not address under-voltage."
    },
    {
        "question": "A user's workstation was infected with a newly discovered virus that the AV system detected. After a full virus scan and a workstation reboot, the virus is still present in the OS. Which of the following actions should the user take to remove the virus?",
        "options": [
            "Enable the system firewall.",
            "Use bootable antivirus media to scan the system.",
            "Download software designed to specifically target the virus.",
            "Run the operating system update process."
        ],
        "correct_answer": 2,
        "description": "The correct answer is to use bootable antivirus media to scan the system. A bootable antivirus can detect and remove malware outside the infected OS environment. \n\n- Enabling the firewall helps prevent network attacks but does not remove an existing virus. \n- Targeted antivirus software might work but may not be effective for new or resistant viruses. \n- OS updates may help, but do not guarantee virus removal."
    },
    {
        "question": "Which of the following is the weakest wireless security protocol?",
        "options": [
            "WEP",
            "WPA2",
            "TKIP",
            "AES"
        ],
        "correct_answer": 1,
        "description": "The correct answer is WEP. WEP is the least secure of the listed protocols and is considered outdated and vulnerable. \n\n- WPA2 provides stronger encryption than WEP. \n- TKIP improves security over WEP but is still less secure than WPA2. \n- AES is a robust encryption standard used in modern protocols."
    },
    {
        "question": "A user is unable to see transaction details on a website, and nothing happens when the user clicks the details button. Which of the following should the user do to fix this issue?",
        "options": [
            "Clear the browser cache.",
            "Disable the pop-up blocker.",
            "Configure private browsing.",
            "Verify valid certificates."
        ],
        "correct_answer": 2,
        "description": "The correct answer is to disable the pop-up blocker. Pop-up blockers can prevent website elements from loading correctly. \n\n- Clearing the browser cache may help, but it's not specific to button issues. \n- Private browsing has no effect on pop-up settings. \n- Certificate verification is related to security, not functionality."
    },
    {
    "question": "A systems administrator plans to upgrade a server to the latest operating system. Which of the following should the administrator do before placing a change request?",
    "options": [
        "Establish a scope",
        "Get change board approval",
        "Create a test environment",
        "Roll back any previous changes"
    ],
    "correct_answer": 1,
    "description": "The correct answer is to establish a scope. Defining the scope helps outline the specific components, resources, and objectives of the upgrade, providing clarity before submitting a change request.\n\n- Change board approval is obtained after the scope is established and the plan is ready to be reviewed.\n- Creating a test environment is important but typically follows the initial scoping and planning stages.\n- Rolling back previous changes is only necessary if recent modifications caused issues."
	},

	{
    "question": "A systems administrator plans to upgrade a server to the latest operating system. Which of the following should the administrator do before placing a change request?",
    "options": [
        "Establish a scope",
        "Get change board approval",
        "Create a test environment",
        "Roll back any previous changes"
    ],
    "correct_answer": 1,
    "description": "The correct answer is to establish a scope. Defining the scope helps outline the specific components, resources, and objectives of the upgrade, providing clarity before submitting a change request.\n\n- Change board approval is obtained after the scope is established and the plan is ready to be reviewed.\n- Creating a test environment is important but typically follows the initial scoping and planning stages.\n- Rolling back previous changes is only necessary if recent modifications caused issues."
	},
    {
        "question": "Which of the following provides disk encryption on computers running a Windows OS?",
        "options": [
            "FileVault",
            "BitLocker",
            "Private Key",
            "PowerShell"
        ],
        "correct_answer": 2,
        "description": "The correct answer is BitLocker. BitLocker is the built-in disk encryption solution for Windows OS. \n\n- FileVault is Apple's disk encryption solution for macOS. \n- Private Key is a component of cryptographic systems, not a disk encryption tool. \n- PowerShell is a command-line interface, not an encryption feature."
    },
    {
        "question": "A Windows user wants a filesystem that protects confidential data from attackers who have physical access to the system. Which of the following should the user choose?",
        "options": [
            "ext",
            "APFS",
            "FAT",
            "EFS"
        ],
        "correct_answer": 4,
        "description": "The correct answer is EFS. EFS (Encrypting File System) is a Windows feature that allows encryption at the file system level, offering protection for stored data. \n\n- ext is commonly used in Linux but does not provide encryption. \n- APFS is used in macOS, not Windows. \n- FAT is a basic file system without encryption capabilities."
    },
    {
        "question": "A user's PC is performing slowly after the user clicked on a suspicious email attachment. The technician notices that a single process is taking 100% of RAM, CPU, and network resources. Which of the following should the technician do first?",
        "options": [
            "Disconnect the computer from the network",
            "Run an antivirus scan",
            "Reboot the computer",
            "Educate the user about cybersecurity best practices"
        ],
        "correct_answer": 1,
        "description": "The correct answer is to disconnect the computer from the network. Disconnecting prevents the malware from spreading to other systems. \n\n- Running an antivirus scan is helpful but could be delayed if malware is currently spreading. \n- Rebooting could end malicious processes temporarily but does not eliminate them. \n- Educating the user is important for prevention but not part of immediate response."
    },
    {
        "question": "A company wants to reduce the negative ecological impacts of its business and has decided to hire an e-waste company to dispose of equipment. Which of the following should the e-waste company provide the business?",
        "options": [
            "Non-disclosure agreement",
            "Certification of destruction",
            "Low-level formatting",
            "Shredding/drilling"
        ],
        "correct_answer": 2,
        "description": "The correct answer is Certification of destruction. This document confirms the secure and ecological disposal of equipment. \n\n- A non-disclosure agreement ensures data privacy but does not cover disposal. \n- Low-level formatting wipes data but is not the same as certified disposal. \n- Shredding/drilling destroys hardware but does not provide certification."
    },
    {
        "question": "Which of the following commands lists running processes in Linux?",
        "options": [
            "top",
            "apt-get",
            "ls",
            "cat"
        ],
        "correct_answer": 1,
        "description": "The correct answer is top. The 'top' command displays active processes and their resource usage. \n\n- 'apt-get' manages packages, not processes. \n- 'ls' lists directory contents. \n- 'cat' displays file contents."
    },


    #636


    {
        "question": "A technician is setting up a wireless network in a small, crowded office and wants to minimize Wi-Fi access. Which of the following security settings should the technician enable?",
        "options": [
            "Port forwarding",
            "Unused ports",
            "SSID broadcast",
            "Allow list"
        ],
        "correct_answer": 4,
        "description": "The correct answer is to enable an Allow list. An Allow list restricts network access only to approved devices, providing a secure way to control access in a crowded area. \n\n- Port forwarding is for directing incoming connections to specific devices but does not limit Wi-Fi access. \n- Unused ports should be disabled, but this applies to physical network ports, not wireless access. \n- Disabling SSID broadcast hides the network but does not restrict access to unauthorized devices."
    },
    {
        "question": "A technician needs to implement password requirements that apply to all domain-joined computers. Which of the following commands should the technician most likely run?",
        "options": [
            "gpupdate",
            "devmgmt",
            "regedit",
            "resmon"
        ],
        "correct_answer": 1,
        "description": "The correct answer is gpupdate. Running 'gpupdate' enforces Group Policy updates across domain-joined systems, applying password and other security settings as defined by the administrator.\n\n- 'devmgmt' opens the Device Manager, which is unrelated to password policies. \n- 'regedit' accesses the Registry Editor, which is not ideal for enterprise-wide policies. \n- 'resmon' opens Resource Monitor, not related to Group Policy enforcement."
    },
    {
        "question": "A technician is configuring a workstation's security settings, and the following options are available: Account lockout policy, Group policy, Two-factor authentication, Password complexity requirements, Firewalls, User accounts, Access control lists, Antivirus software. Which of the following settings should the technician configure to deploy strong password enforcement across the enterprise?",
        "options": [
            "Account lockout policy",
            "Group policy",
            "Two-factor authentication",
            "Access control lists"
        ],
        "correct_answer": 2,
        "description": "The correct answer is Group policy. Group policies are used to enforce password requirements across an organization, ensuring strong security practices.\n\n- Account lockout policy helps limit login attempts but does not manage password complexity. \n- Two-factor authentication enhances security but does not enforce password rules. \n- Access control lists regulate resource access but are not used for password enforcement."
    },
    {
        "question": "A technician downloaded an OS installation file but is unable to run it. When the technician tries to open the file, a message indicates no software is installed to run this file. Which of the following should the technician do next to attempt to access the OS file?",
        "options": [
            "Request physical media",
            "Mount the ISO file",
            "Install a third-party software",
            "Download an appropriate 32-bit/64-bit OS file"
        ],
        "correct_answer": 2,
        "description": "The correct answer is to mount the ISO file. Mounting the ISO allows the technician to access its contents as a virtual drive, making the OS installation files accessible.\n\n- Requesting physical media is unnecessary if the ISO file is available. \n- Installing third-party software is not needed for mounting ISO files on modern OSes. \n- Downloading a 32-bit/64-bit OS file may help in compatibility but is not required for mounting."
    },
    {
        "question": "A technician is installing an operating system on a new computer. Which of the following is the first step of the process?",
        "options": [
            "Setting the boot order",
            "Formatting the hard drive",
            "Entering the product key",
            "Selecting the filesystem"
        ],
        "correct_answer": 1,
        "description": "The correct answer is setting the boot order. Setting the boot order ensures that the computer boots from the OS installation media first, allowing the OS installation process to begin.\n\n- Formatting the hard drive is part of the installation process but occurs later. \n- Entering the product key is necessary for activation but comes after setup begins. \n- Selecting the filesystem occurs during installation but is not the first step."
    },
    {
        "question": "A technician needs to troubleshoot a user's computer while the user is connected to the system. The technician must also connect to the user's system using remote access tools built in to Windows. Which of the following is the best option to troubleshoot the user's computer?",
        "options": [
            "Screen share",
            "MSRA",
            "Virtual network computer",
            "RDP"
        ],
        "correct_answer": 2,
        "description": "The correct answer is MSRA. MSRA (Microsoft Remote Assistance) allows technicians to connect and troubleshoot a user's computer with the user’s interaction.\n\n- Screen share does not provide control over the user’s system. \n- VNC (Virtual Network Computing) is a remote tool but requires additional setup and is not built-in to Windows. \n- RDP (Remote Desktop Protocol) does not allow for shared sessions with the user."
    },
    {
        "question": "A technician is troubleshooting a desktop PC's recent slow performance and notes the following information. The PC has the standard amount of RAM, a recently defragmented hard drive, a newly installed application, and high CPU utilization. Which of the following actions should the technician take to most likely resolve the performance issue?",
        "options": [
            "Install more RAM",
            "Reboot the PC",
            "Uninstall the new program",
            "Replace the hard drive"
        ],
        "correct_answer": 3,
        "description": "The correct answer is to uninstall the new program. The high CPU usage is likely caused by the newly installed application, which could be resource-intensive or malfunctioning.\n\n- Installing more RAM could help with performance but is unnecessary if CPU is the primary issue. \n- Rebooting the PC may temporarily resolve issues but does not address the root cause. \n- Replacing the hard drive is unnecessary if the drive is functioning properly."
    },

#643

	{
    "question": "A project manager reports severely degraded OS performance after the installation of a recent system patch. Which of the following should the technician most likely do to correct the issue?",
    "options": [
        "Reinstall the OS",
        "Initiate Windows System Restore",
        "Uninstall security update",
        "Run an antivirus scan"
    ],
    "correct_answer": 3,
    "description": "The correct answer is 'Uninstall security update.' When OS performance degrades after a patch installation, it is often caused by a specific update. Uninstalling the update helps determine whether it is the root cause of the performance issue. \n\n- Reinstalling the OS would be a drastic step and should only be considered if other solutions fail. \n- Initiating Windows System Restore might work, but it is more time-consuming and does not specifically target the update. \n- Running an antivirus scan is unrelated to performance issues caused by an OS patch."
	},

	{
    "question": "Which of the following ensures proprietary information on a lost or stolen mobile device cannot be accessed while the device is offline?",
    "options": [
        "Remote wipe",
        "Mandatory screen locks",
        "Location applications",
        "Device data encryption"
    ],
    "correct_answer": 4,
    "description": "The correct answer is 'Device data encryption.' Data encryption ensures that the information stored on the device is protected with strong encryption algorithms, preventing unauthorized access even when the device is offline. \n\n- Remote wipe only works when the device is connected to the network. \n- Mandatory screen locks prevent unauthorized access but are less effective if the device is stolen while unlocked. \n- Location applications only help track the device but do not secure data."
	},

	{
    "question": "A user's enterprise-issued smartphone does not respond to touch after starting up the operating system. Which of the following should a technician try next?",
    "options": [
        "Contact the vendor for assistance.",
        "Replace the screen assembly.",
        "Confirm the touch screen functionality.",
        "Restore to factory settings."
    ],
    "correct_answer": 3,
    "description": "The correct answer is 'Confirm the touch screen functionality.' The technician should first check if the touch screen itself is functioning properly before moving to more complex solutions. \n\n- Contacting the vendor is an unnecessary step at this point. \n- Replacing the screen assembly is premature unless the touch screen is confirmed to be defective. \n- Restoring to factory settings may be a valid option, but it should be considered after confirming whether the touch screen is functioning."
	},

	{
    "question": "Due to special job responsibilities, an end user needs the ability to edit the properties of Windows system files. The user has already been granted local administrator privileges. Which of the following Control Panel utilities should be used to provide easy access to the files?",
    "options": [
        "File Explorer Options",
        "Ease of Access",
        "Indexing Options",
        "Administrative Tools"
    ],
    "correct_answer": 1,
    "description": "The correct answer is 'File Explorer Options.' This utility allows users to modify how system files are displayed and accessed in File Explorer. \n\n- Ease of Access is designed to help users with disabilities, not for editing system file properties. \n- Indexing Options relates to file search indexing, not file property editing. \n- Administrative Tools provide access to advanced management features, but not to directly modify file properties."
	},

	{
    "question": "Which of the following features can a technician use to ensure users are following password length requirements?",
    "options": [
        "Group Policy",
        "Log-on script",
        "Access control list",
        "Security groups"
    ],
    "correct_answer": 1,
    "description": "The correct answer is 'Group Policy.' Group Policy allows administrators to enforce password policies, including minimum length requirements, across the entire domain. \n\n- Log-on scripts are typically used for automation tasks, not for enforcing password policies. \n- Access control lists manage permissions but do not enforce password requirements. \n- Security groups are used to organize users and assign permissions, but they do not directly control password policies."
	},

	{
    "question": "A user with a disability needs to be able to press the Ctrl+Alt+Del keyboard sequence one key at a time. Which of the following turns on this Ease of Access feature?",
    "options": [
        "Press the Shift key five times in a row",
        "Press Ctrl+Alt+Esc simultaneously",
        "Press Ctrl+Alt+Tab simultaneously",
        "Press the Windows key+Tab"
    ],
    "correct_answer": 1,
    "description": "The correct answer is 'Press the Shift key five times in a row.' This activates the Sticky Keys feature, which allows users to press one key at a time for key combinations like Ctrl+Alt+Del. \n\n- Pressing Ctrl+Alt+Esc or Ctrl+Alt+Tab are not related to activating this accessibility feature. \n- Pressing the Windows key+Tab opens Task View, which is not relevant to this task."
	},

	{
    "question": "A technician assigns the equivalent of root-level permissions to a user to perform a task. Which of the following user roles within the Windows OS should the technician choose?",
    "options": [
        "Power",
        "Default",
        "Administrator",
        "Superuser"
    ],
    "correct_answer": 3,
    "description": "The correct answer is 'Administrator.' The Administrator role grants full access to all system files and settings, similar to root-level permissions in other operating systems. \n\n- Power users have some elevated privileges, but they do not have full system access like an Administrator. \n- Default users have standard permissions with limited access. \n- Superuser is a Unix/Linux term equivalent to Administrator in Windows."
	},

	{
    "question": "A user receives a message on a PC stating it has been infected by malware. A technician runs a full scan on the user's machine and detects no malware. Later that day, the same message reappears. Which of the following steps should the technician take to restore the system to regular functionality?",
    "options": [
        "The graphics card driver needs to be updated.",
        "The application installer is 64-bit.",
        "The installation requires administrative rights.",
        "The disk space is inadequate."
    ],
    "correct_answer": 3,
    "description": "The correct answer is 'The installation requires administrative rights.' The repeated malware message could be caused by an application that requires elevated privileges to install or run. \n\n- Updating the graphics card driver is unlikely to resolve a malware-related message. \n- The installer being 64-bit does not affect malware detection. \n- Inadequate disk space may cause installation issues but is unlikely to cause repeated malware warnings."
	},

#651

    {
        "question": "A user's laptop is shutting down every time the laptop lid is closed, which is leading to frequent work interruptions. Which of the following should a help desk specialist do to remediate the issue?",
        "options": [
            "Configure the sleep settings.",
            "Disable hibernation.",
            "Edit the power plan.",
            "Turn on fast startup."
        ],
        "correct_answer": 3,
        "description": "The correct answer is 'Edit the power plan.' This option allows the user to configure the laptop's behavior when the lid is closed, ensuring the laptop doesn't shut down unexpectedly. \n\n- Configuring sleep settings might cause the laptop to enter sleep mode instead of staying active. \n- Disabling hibernation will prevent the laptop from saving the current state but does not directly address the shutdown issue. \n- Turning on fast startup could speed up boot times but is unrelated to the lid's action when closed."
    },
    {
        "question": "A user in a SOHO asks an off-site, remote technician to connect securely to the user's laptop. The technician is able to connect to the VPN but is unable to connect to the user's laptop. Which of the following settings should the technician review?",
        "options": [
            "Wireless protocol",
            "DHCP pool",
            "Content filtering",
            "Firewall"
        ],
        "correct_answer": 4,
        "description": "The correct answer is 'Firewall.' The firewall may be blocking the technician's access to the laptop, even after establishing a VPN connection. \n\n- The wireless protocol controls network access but is less likely to be the issue since the VPN is already connected. \n- DHCP pool settings control IP address assignment, but the VPN connection is already established. \n- Content filtering typically controls internet access or restricts specific types of content but isn't related to direct laptop access."
    },
   {
    "question": "A technician is troubleshooting an issue on a PC that has low disk space. Which of the following Control Panel utilities should the technician most likely use to investigate and remediate the issue?",
    "options": [
        "Indexing Options",
        "Internet Options",
        "System",
        "Programs and Features",
        "Device Manager"
    ],
    "correct_answer": 4,
    "description": "The correct answer is 'Programs and Features.' This utility allows the technician to uninstall unnecessary software, which can free up space on the disk. \n\n- 'Indexing Options' relates to search functionality and won't provide direct information about disk space. \n- 'Internet Options' is focused on browser settings, not disk space. \n- 'System' provides an overview of system settings but does not specifically focus on disk usage. \n- 'Device Manager' is used for hardware management, not disk space issues."
    },
    {
        "question": "A user wants to back up a device's OS and data. Which of the following is the best way to accomplish this task?",
        "options": [
            "Incremental backup",
            "System image",
            "System restore point",
            "Differential backup"
        ],
        "correct_answer": 2,
        "description": "The correct answer is 'System image.' A system image provides a complete copy of the operating system, applications, and data, allowing for full recovery. \n\n- Incremental and differential backups only capture changes to data, not the entire system. \n- A system restore point allows for restoring system settings but does not back up the entire OS and data."
    },
    {
        "question": "Which of the following will automatically map network drives based on Group Policy configuration?",
        "options": [
            "Log-in scripts",
            "Access control lists",
            "Organizational units",
            "Folder redirection"
        ],
        "correct_answer": 1,
        "description": "The correct answer is 'Log-in scripts.' Group Policy can be used to configure log-in scripts that automatically map network drives when users log into their computers. \n\n- Access control lists are used for permissions, not mapping network drives. \n- Organizational units control group memberships and policies but are not directly used for drive mapping. \n- Folder redirection is used to redirect folders like Documents to another location, not for mapping drives."
    },
    {
        "question": "A user is unable to access the company's internal network on a separate subnet. A help desk technician verifies the user’s credentials, and the user has the appropriate permissions to access the network. The technician checks the network and finds the connection is stable. No other users are having this issue. Which of the following should the technician do next?",
        "options": [
            "Consult with the firewall team to see if the user's IP address is blocked.",
            "Delete the user's credentials and create new ones.",
            "Run a virus scan on the user's workstation.",
            "Update the network drivers on the user’s workstation."
        ],
        "correct_answer": 1,
        "description": "The correct answer is 'Consult with the firewall team to see if the user's IP address is blocked.' A firewall might be blocking access to the internal network based on the user's IP. \n\n- Deleting and recreating the user's credentials may not resolve an issue with network access. \n- A virus scan might be helpful but is less likely to address the specific network access issue. \n- Updating network drivers could help with general connectivity issues but won't resolve a blocked IP address."
    },
    {
        "question": "A customer needs to purchase a desktop capable of rendering video. Which of the following should the customer prioritize?",
        "options": [
            "NIC",
            "USB",
            "GPU",
            "HDMI"
        ],
        "correct_answer": 3,
        "description": "The correct answer is 'GPU.' A powerful GPU (Graphics Processing Unit) is essential for rendering video efficiently. \n\n- NIC and USB are important for network and peripheral connectivity but do not affect video rendering performance. \n- HDMI is used for display connections but does not impact the rendering capability of the desktop."
    },
    {
        "question": "A technician is setting up a new PC in a SOHO. Which of the following should the technician most likely configure on the PC?",
        "options": [
            "VDI",
            "Mapped drives",
            "Wireless WAN",
            "Domain"
        ],
        "correct_answer": 2,
        "description": "The correct answer is 'Mapped drives.' In a SOHO, the technician is most likely to map network drives to allow for easy file sharing and access. \n\n- VDI is a virtual desktop infrastructure solution that is not typical for a SOHO setup. \n- Wireless WAN would be used for wide-area networking, but it's not a common setup for individual PCs. \n- Domain configuration is more suitable for larger networks rather than a small office/home office."
    },
    {
        "question": "A client’s device was recently used by multiple other users. The client reports their device is now running slower than usual. Which of the following steps should a technician take first? (Choose two.)",
        "options": [
            "Perform a virus scan.",
            "Check the startup programs.",
            "Back up the data.",
            "Disable the guest account.",
            "Update the firmware.",
            "Reinstall the operating system."
        ],
        "correct_answer": [1, 2],
        "description": "The correct answers are 'Perform a virus scan' and 'Check the startup programs.' A virus scan will ensure that malware isn't slowing down the system, while checking the startup programs will identify any unnecessary applications consuming resources. \n\n- Backing up the data is a good practice but is not the first step in troubleshooting performance. \n- Disabling the guest account might help but is unlikely to directly resolve the slowness issue. \n- Updating the firmware and reinstalling the OS are more drastic measures and should be considered later."
    },
    {
        "question": "A malicious user was able to export an entire website's user database by entering specific commands into a field on the company's website. Which of the following did the malicious user most likely exploit to extract the data?",
        "options": [
            "Cross-site scripting",
            "SQL injection",
            "Brute-force attack",
            "DDoS attack"
        ],
        "correct_answer": 2,
        "description": "The correct answer is 'SQL injection.' SQL injection allows attackers to input malicious commands into web forms that interact with the database, enabling unauthorized data extraction. \n\n- Cross-site scripting (XSS) targets client-side vulnerabilities and doesn't typically involve database extraction. \n- Brute-force attacks involve guessing credentials and are unrelated to SQL injection. \n- DDoS attacks are used to overwhelm servers with traffic but don't involve data extraction."
    },
    {
        "question": "A customer who uses a Linux OS called the help desk to request assistance in locating a missing file. The customer does not know the exact name of the file but can provide a partial file name. Which of the following tools should the technician use? (Choose two.)",
        "options": [
            "cat",
            "df",
            "grep",
            "ps",
            "dig",
            "find",
            "top"
        ],
        "correct_answer": [3, 6],
        "description": "The correct answers are 'grep' and 'find.' The 'find' command can search for files based on a partial name, while 'grep' can be used to search within files for matching content. \n\n- 'cat' displays file contents but isn't used for searching. \n- 'df' shows disk space, but it's not relevant for locating files. \n- 'ps' and 'top' are used for managing processes, not for locating files. 'dig' is used for DNS queries."
    },
#662


    {
        "question": "A user is attempting to access a shared drive from a company-issued laptop while working from home. The user is unable to access any files and notices a red X next to each shared drive. Which of the following needs to be configured in order to restore the user's access to the shared drives?",
        "options": [
            "IPv6",
            "VPN",
            "IPS",
            "DNS"
        ],
        "correct_answer": 2,
        "description": "The correct answer is VPN. A VPN (Virtual Private Network) is used to securely connect remote users to the company’s internal network, allowing them to access resources such as shared drives. \n\n- IPv6 is a network protocol and is not directly related to accessing shared drives. \n- IPS is an intrusion prevention system, not a tool for accessing network shares. \n- DNS is important for domain name resolution but does not specifically address remote access to shared drives."
    },
    {
        "question": "A technician needs to update the software on several hundred Mac laptops. Which of the following is the best method to complete the task?",
        "options": [
            "SSH",
            "MDM",
            "RDP",
            "SFTP"
        ],
        "correct_answer": 2,
        "description": "The correct answer is MDM (Mobile Device Management). MDM solutions allow administrators to remotely manage and update software on Mac laptops across an organization. \n\n- SSH is a secure shell for remote command-line access and is not ideal for mass software updates. \n- RDP (Remote Desktop Protocol) is used for remote access to a machine’s desktop, but not for mass software updates. \n- SFTP is for secure file transfer and does not facilitate software management."
    },
    {
        "question": "A user's home system has been infected with malware. A technician has isolated the system from the network and disabled System Restore. Which of the following should the technician do next?",
        "options": [
            "Perform an antivirus scan.",
            "Run Windows updates.",
            "Reimage the system.",
            "Enable System Restore."
        ],
        "correct_answer": 1,
        "description": "The correct answer is to perform an antivirus scan. After isolating the infected system, running an antivirus scan is the most appropriate next step to detect and remove any malware. \n\n- Running Windows updates may fix vulnerabilities but does not directly address the current malware infection. \n- Reimaging the system is a more drastic step and may not be necessary if the malware can be removed. \n- Enabling System Restore should only be done after the malware is removed to avoid the restoration of infected files."
    },
    {
        "question": "An employee lost a smartphone and reported the loss to the help desk. The employee is concerned about the possibility of a breach of private data. Which of the following is the best way for a technician to protect the data on the phone?",
        "options": [
            "Remote lock",
            "Remote wipe",
            "Remote access",
            "Remote encrypt"
        ],
        "correct_answer": 2,
        "description": "The correct answer is remote wipe. A remote wipe will erase all the data on the lost phone to prevent unauthorized access. \n\n- Remote lock will prevent access to the device but does not delete any sensitive data. \n- Remote access is not a security measure for lost devices. \n- Remote encryption would protect data but would not address the immediate concern of securing a lost device."
    },
    {
        "question": "A network administrator wants to enforce a company's security policy that prohibits USB drives on user workstations. Which of the following commands should the administrator run on the users' workstations?",
        "options": [
            "diskpart",
            "chown",
            "gpupdate",
            "netstat"
        ],
        "correct_answer": 3,
        "description": "The correct answer is gpupdate. Running gpupdate will enforce Group Policy updates, which can be used to disable USB drive access via Group Policy settings. \n\n- Diskpart is used to manage disk partitions, not for controlling USB access. \n- Chown is a Unix/Linux command used for changing file ownership. \n- Netstat is a networking command used to view active connections and does not affect USB devices."
    },
    {
        "question": "A company uses shared drives as part of a workforce collaboration process. To ensure the correct access permissions, inheritance at the top-level folder is assigned to each department. A manager's team is working on confidential material and wants to ensure only the immediate team can view a specific folder and its subsequent files and subfolders. Which of the following actions should the technician most likely take?",
        "options": [
            "Turn off inheritance on the requested folder only and set the requested permissions to each file manually.",
            "Turn off inheritance at the top-level folder and remove all inherited permissions.",
            "Turn off inheritance at the top-level folder and set permissions to each file and subfolder manually.",
            "Turn off inheritance on the requested folder only, set the requested permissions, and then turn on inheritance under the child folders."
        ],
        "correct_answer": 4,
        "description": "The correct answer is to turn off inheritance on the requested folder only, set the requested permissions, and then turn on inheritance under the child folders. This ensures that the confidential folder has specific access permissions, while the child folders can inherit permissions from the parent. \n\n- Manually setting permissions for each file or folder is time-consuming and inefficient. \n- Removing inheritance entirely would be more restrictive than necessary for managing shared drives."
    },
    {
        "question": "A user's smartphone screen is not rotating. The technician confirms the rotation lock is deactivated. Which of the following steps should the technician perform next?",
        "options": [
            "Remove the screen protector.",
            "Update the smartphone’s software.",
            "Restart the smartphone.",
            "Replace the smartphone."
        ],
        "correct_answer": 3,
        "description": "The correct answer is to restart the smartphone. A restart can resolve many common issues with smartphone functionality, including problems with screen rotation. \n\n- Removing the screen protector is unlikely to resolve software-related issues. \n- Updating the smartphone’s software may help but is not the most immediate step. \n- Replacing the smartphone should be considered a last resort."
    },
    {
        "question": "Users report having difficulty using the Windows Hello facial recognition feature. Which of the following is a secondary feature of Windows Hello that can be used to log in?",
        "options": [
            "Personal identification number",
            "Username/password",
            "One-time-use token",
            "Cryptographic device"
        ],
        "correct_answer": 1,
        "description": "The correct answer is personal identification number (PIN). A PIN can be used as a secondary login method if Windows Hello facial recognition fails. \n\n- Username/password is a traditional login method, but it’s not specific to Windows Hello. \n- One-time-use tokens are used for multi-factor authentication, not for logging in directly. \n- Cryptographic devices are used for secure authentication, but not as a backup for Windows Hello."
    },
    {
        "question": "Which of the following is the most secure method to protect a mobile device from unwanted access?",
        "options": [
            "Remote wipe",
            "Biometrics",
            "Personal identification number",
            "Log-in attempt restrictions"
        ],
        "correct_answer": 2,
        "description": "The correct answer is biometrics. Biometrics, such as fingerprint or facial recognition, provide the highest level of security for mobile devices, ensuring only authorized users can access the device. \n\n- Remote wipe is a security measure for lost or stolen devices but does not protect ongoing access. \n- A PIN is secure, but biometrics offer a more convenient and secure option. \n- Log-in attempt restrictions are useful, but biometrics are generally more secure."
    },
    {
        "question": "An administrator's change was approved by the change management review board. Which of the following should the administrator do next?",
        "options": [
            "Perform risk analysis",
            "Assign a change coordinator",
            "Implement the change",
            "Verify testing results"
        ],
        "correct_answer": 3,
        "description": "The correct answer is to implement the change. After approval from the review board, the next step is to implement the change according to the plan. \n\n- Risk analysis should be done before submitting the change request, not after approval. \n- A change coordinator is important for larger changes but may not be required in all cases. \n- Verifying testing results is part of the change process but happens before implementation."
    },
    {
        "question": "A user is unable to log in to a workstation. The user reports an error message about the date being incorrect. A technician reviews the date and verifies it is correct, but the system clock is an hour behind. The technician also determines this workstation is the only one affected. Which of the following is the most likely issue?",
        "options": [
            "Time drift",
            "NTP failure",
            "Windows Update",
            "CMOS battery"
        ],
        "correct_answer": 4,
        "description": "The correct answer is CMOS battery. A failing CMOS battery can cause the system clock to lose time or not retain correct time when the computer is powered off. \n\n- Time drift refers to gradual time changes but is typically not isolated to one workstation. \n- NTP (Network Time Protocol) failure can affect time synchronization, but in this case, the issue is isolated to one machine. \n- A Windows Update would not cause this specific issue."
    },

#673


   {
    "question": "A technician needs to configure a backup solution that will have the least additional expenses and impact on users. Which of the following steps should the technician complete? (Choose two.)",
    "options": [
        "Configure the backup to run when the user logs in.",
        "Configure the backup to run after peak hours.",
        "Use third-party licensed backup software.",
        "Use the built-in OS backup utility.",
        "Configure the backup job to run every hour.",
        "Use an external storage device for the backup."
    ],
    "correct_answer": [2, 4],
    "description": "The correct answers are 'Configure the backup to run after peak hours' and 'Use the built-in OS backup utility.' \n\n- Configuring the backup to run after peak hours minimizes the impact on system performance during regular working hours, ensuring productivity is not interrupted. \n- The built-in OS backup utility is a low-cost solution that reduces the need for third-party software, keeping expenses minimal while still providing a reliable backup method. \n\n- Configuring the backup to run when the user logs in could disrupt user activities and lead to a longer backup window. \n- Third-party licensed backup software introduces unnecessary costs compared to the free built-in OS solutions. \n- Running backups every hour may put excessive strain on system resources and may not be necessary for most use cases. \n- Using an external storage device adds additional expenses and might not be the most scalable or secure solution for regular backups."
	},
    {
        "question": "A change management review board denied an administrator's request for change. The administrator had provided the purpose and scope of the change, the date and time, and impacted systems with the risk analysis. Which of the following should be included to approve this change?",
        "options": [
            "End-user acceptance",
            "Cost analysis",
            "Rollback plan",
            "Standard maintenance window"
        ],
        "correct_answer": 3,
        "description": "The correct answer is 'Rollback plan.' \n\n- A rollback plan is essential for change management as it provides a method for reverting to a previous state if the change causes issues. \n\n- End-user acceptance is not typically required for approval at this stage, though it may be needed during implementation. \n- Cost analysis might be relevant but is not essential for a basic change approval. \n- A standard maintenance window helps schedule changes but doesn't address the risks associated with the change itself."
    },
    {
        "question": "A technician is preparing a training room, and the workstations must all have the same OS, applications, and settings. Which of the following methods is the best way to accomplish this request?",
        "options": [
            "Recovery partition",
            "Clean install",
            "Image deployment",
            "In-place upgrade"
        ],
        "correct_answer": 3,
        "description": "The correct answer is 'Image deployment.' \n\n- Image deployment allows the technician to apply a consistent setup (OS, applications, settings) to multiple workstations quickly and efficiently. \n\n- A recovery partition is not suitable for mass deployment of settings across multiple machines. \n- Clean installs would require individual setup for each machine, which is time-consuming. \n- An in-place upgrade is used for upgrading existing systems, not for deploying identical configurations to multiple systems."
    },
    {
        "question": "Which of the following environmental controls is most important to maintain the safety of a data center?",
        "options": [
            "Temperature control",
            "Humidity control",
            "Fire suppression control",
            "Power management control"
        ],
        "correct_answer": 1,
        "description": "The correct answer is 'Temperature control.' \n\n- Temperature control is critical to maintaining safe operating conditions for data center equipment. Overheating can cause hardware failure and data loss. \n\n- Humidity control is important but secondary to temperature regulation for preventing damage to equipment. \n- Fire suppression control is essential but typically a secondary consideration after ensuring the environment is stable. \n- Power management control is important, but stable temperature is the highest priority to prevent overheating and hardware malfunctions."
    },
    {
        "question": "An employee utilizes a personal smartphone to work remotely. The employee is unable to reach the portal using the company-provided VPN service. Which of the following describes the cause of the issue?",
        "options": [
            "The application must be purchased by the company.",
            "The smartphone is not on the latest OS version.",
            "The smartphone is not enrolled in MDM service.",
            "The application fails to install and launch."
        ],
        "correct_answer": 3,
        "description": "The correct answer is 'The smartphone is not enrolled in MDM service.' \n\n- Enrolling the smartphone in Mobile Device Management (MDM) ensures it complies with the company's security policies, which may include VPN access. \n\n- The smartphone not being on the latest OS version may cause issues, but it’s less likely to be the primary cause of VPN connection issues. \n- The application failing to install or launch may prevent VPN use, but the root issue is likely the MDM enrollment. \n- While the company may need to approve or provide the VPN app, this is not typically the cause of the connection issue."
    },
#678 is an image question

#679


    {
        "question": "A technician receives a help desk request from a user who reports a software issue. After following the established troubleshooting steps, the technician determines the issue is related to the user's outdated software version. Which of the following should the technician do next?",
        "options": [
            "Escalate the issue to the next level of support.",
            "Update the ticket with the actions taken and proposed solutions.",
            "Advise the user to purchase the latest software version.",
            "Update the knowledge base."
        ],
        "correct_answer": 2,
        "description": "The correct answer is 'Update the ticket with the actions taken and proposed solutions.' \n\n- Updating the ticket ensures proper documentation of the issue and the technician's actions, making it easier to track the resolution process. \n- Escalating the issue may not be necessary if the problem is clearly due to outdated software, and the technician has already identified the cause. \n- Advising the user to purchase the latest software version might not be necessary if the update is available for free or covered by a license. \n- Updating the knowledge base is useful but not an immediate step to resolve the user’s specific issue."
    },
    {
        "question": "A technician is investigating a workstation that has not received the latest policy changes. Which of the following commands should the technician use to apply the latest domain policy changes?",
        "options": [
            "sfc /scannow",
            "gpupdate /force",
            "chkdsk /y",
            "xcopy /p"
        ],
        "correct_answer": 2,
        "description": "The correct answer is 'gpupdate /force.' \n\n- The 'gpupdate /force' command forces an immediate update of Group Policy settings, including domain policy changes. \n- 'sfc /scannow' scans and repairs system files but does not affect Group Policy. \n- 'chkdsk /y' checks disk integrity and does not affect policy changes. \n- 'xcopy /p' is used for file copying and is not related to applying policy updates."
    },
    {
        "question": "Internet speeds on a user's Windows 10 device are slow, but other devices on the same network are running at normal speeds. A technician thinks the issue may be related to the proxy settings. Which of the following should the technician check to verify the proxy configuration?",
        "options": [
            "Network and Sharing Center",
            "Internet Options",
            "Firewall settings",
            "System settings"
        ],
        "correct_answer": 2,
        "description": "The correct answer is 'Internet Options.' \n\n- The 'Internet Options' menu allows the technician to view and modify proxy settings, which can affect internet speed. \n- The 'Network and Sharing Center' is more related to network connections but does not provide direct access to proxy settings. \n- Firewall settings may block network traffic but are unlikely to cause proxy-related issues. \n- System settings may influence system performance but do not directly address proxy settings."
    },
    {
        "question": "A user's Android phone has been randomly restarting. A technician investigates and finds several applications have been installed that are not available within the standard marketplace. Which of the following is most likely the cause of the issue?",
        "options": [
            "The OS update failed.",
            "The user downloaded malware.",
            "The device is in developer mode.",
            "The over-the-air carrier update failed."
        ],
        "correct_answer": 2,
        "description": "The correct answer is 'The user downloaded malware.' \n\n- Downloading unauthorized apps outside the standard marketplace is a common way for malware to infect devices, leading to instability and crashes. \n- An OS update failure could cause issues but is less likely to lead to frequent restarts. \n- Developer mode is used for testing and would not cause random restarts unless there is a misconfiguration. \n- A carrier update failure would typically affect functionality but is unlikely to be the cause of random restarts."
    },
    {
        "question": "A technician is troubleshooting a PC that will not run Windows Defender. Windows Defender has been disabled and no other antivirus is installed on the PC. Which of the following would have caused this issue?",
        "options": [
            "Ransomware",
            "Rootkit",
            "Spyware",
            "Keylogger"
        ],
        "correct_answer": 2,
        "description": "The correct answer is 'Rootkit.' \n\n- A rootkit is a type of malware that hides itself from detection and can disable security software like Windows Defender, making it the most likely cause. \n- Ransomware could also disable antivirus but typically involves demanding payment and locking files, not just disabling security software. \n- Spyware and keyloggers typically steal information rather than disable security features, though they can still interfere with antivirus programs."
    },
    {
        "question": "Which of the following is a technique used by a threat actor to engage and obtain information via a telephone call?",
        "options": [
            "Phishing",
            "Smishing",
            "Tailgating",
            "Vishing"
        ],
        "correct_answer": 4,
        "description": "The correct answer is 'Vishing.' \n\n- 'Vishing' refers to phishing attempts made over the phone to steal sensitive information. \n- 'Phishing' involves email-based scams, not telephone calls. \n- 'Smishing' is phishing via SMS messages. \n- 'Tailgating' is a physical security threat where an unauthorized person follows an authorized individual into a restricted area, not a method of obtaining information via phone."
    },
    {
    "question": "A computer has been infected with malware. Despite several attempts to remove the malware, the issue persists. Which of the following actions should the technician take next? (Choose two.)",
    "options": [
        "Reimage the computer.",
        "Restore the computer using the last known-good backup.",
        "Remove the computer from the network.",
        "Put the computer in safe mode.",
        "Verify the file consistency.",
        "Enable the system firewall."
    ],
    "correct_answer": [1, 3],
    "description": "The correct answers are 'Reimage the computer' and 'Remove the computer from the network.' \n\n- Reimaging the computer ensures a fresh, clean installation of the operating system, eliminating persistent malware. \n- Removing the computer from the network prevents the malware from spreading to other devices, reducing the risk of further infection. \n\n- Restoring the computer using a backup could work, but it may reintroduce the malware if the backup is compromised. \n- Safe mode can help in troubleshooting but may not fully eliminate the malware in this scenario. \n- Verifying file consistency and enabling the firewall are important security measures but not the immediate solution to dealing with persistent malware."
	},
    {
        "question": "A user receives a message on a PC stating it has been infected by malware. A technician runs a full scan on the user's machine and detects no malware. Later that day, the same message reappears. Which of the following steps should the technician take to restore the system to regular functionality?",
        "options": [
            "Check for Windows updates.",
            "Reimage the computer.",
            "Enable Windows Firewall.",
            "Run System File Checker."
        ],
        "correct_answer": 2,
        "description": "The correct answer is 'Reimage the computer.' \n\n- Reimaging the computer ensures a fresh, clean installation of the operating system and software, removing any persistent malware that may not be detected by scans. \n- Checking for updates, enabling the firewall, and running System File Checker are important security steps but won't necessarily remove the underlying malware that is causing the repeated warning message."
    },
    {
        "question": "A technician is trying to perform an in-place upgrade of a Windows OS from a file. When the technician double-clicks the file, the technician receives a prompt to mount a drive. Which of the following file types did the technician download?",
        "options": [
            ".msi",
            ".iso",
            ".zip",
            ".exe"
        ],
        "correct_answer": 2,
        "description": "The correct answer is '.iso.' \n\n- An .iso file is a disk image that often requires mounting to perform an in-place upgrade. It contains the installation files for an operating system upgrade. \n- .msi files are Windows installer packages, typically used for individual program installations, not OS upgrades. \n- .zip is a compressed file format, while .exe files are executable programs but do not typically require mounting for an OS upgrade."
    },
    {
        "question": "A change was introduced in the company's DNS server, but local workstations have not applied it yet. Which of the following commands should the help desk technician use to force the workstations to immediately apply the change?",
        "options": [
            "nslookup",
            "netstat",
            "tracert",
            "ipconfig"
        ],
        "correct_answer": 4,
        "description": "The correct answer is 'ipconfig.' \n\n- The 'ipconfig /flushdns' command clears the local DNS cache, forcing the workstation to fetch the latest DNS information from the server. \n- 'nslookup' helps query DNS records but does not update the workstation’s DNS cache. \n- 'netstat' displays network statistics, and 'tracert' traces network routes, neither of which address DNS cache issues."
    },


#689


    {
        "question": "A technician needs to implement a system to handle both authentication and authorization. Which of the following meets this requirement?",
        "options": [
            "WPA3",
            "MFA",
            "TACACS+",
            "OAuth 2.0"
        ],
        "correct_answer": 3,
        "description": "The correct answer is TACACS+. TACACS+ is a protocol used for both authentication and authorization, allowing control over user access to network devices. \n\n- WPA3 is a security protocol for wireless networks but is not related to handling authentication and authorization. \n- MFA (Multi-Factor Authentication) enhances security but is not designed for both authentication and authorization. \n- OAuth 2.0 is an authorization protocol, but it doesn't handle authentication directly."
    },
    {
        "question": "A user’s mobile phone battery does not last long, and navigation is very slow. Which of the following should the technician do first to resolve the issue?",
        "options": [
            "Uninstall unused programs.",
            "Check running applications.",
            "Update the mobile OS.",
            "Disable network services."
        ],
        "correct_answer": 2,
        "description": "The correct answer is 'Check running applications.' Running applications may drain battery life and slow down performance. \n\n- Uninstalling unused programs can help, but it is not the first step to identify the issue. \n- Updating the mobile OS can help with performance, but checking running apps is a more immediate way to identify the root cause. \n- Disabling network services may save battery but is a drastic measure before identifying which apps are the cause."
    },
    {
        "question": "A customer's PC is performing slowly and displaying unexpected pop-up messages. Which of the following should a technician use to troubleshoot this issue?",
        "options": [
            "Anti-malware",
            "Recovery Console",
            "System Configuration",
            "Disk Cleanup"
        ],
        "correct_answer": 1,
        "description": "The correct answer is 'Anti-malware.' Anti-malware software can scan and remove malicious software that may be causing the pop-ups and performance issues. \n\n- The Recovery Console is used for repairing system files, but it may not directly address malware. \n- System Configuration (msconfig) helps troubleshoot startup issues but isn't designed to remove malware. \n- Disk Cleanup can free up space but does not address malware or performance issues caused by malicious software."
    },
    {
        "question": "A systems administrator needs to access a hypervisor that went offline. After doing a port scan, the administrator notices that company policy is blocking the RDP default port. Which of the following ports should the administrator use to access the machine?",
        "options": [
            "22",
            "23",
            "80",
            "3090"
        ],
        "correct_answer": 4,
        "description": "The correct answer is '3090.' This is a non-standard port often used for remote management of hypervisors like VMware. \n\n- Port 22 is for SSH, used primarily for Linux systems and remote command-line access. \n- Port 23 is for Telnet, an insecure communication protocol that is rarely used. \n- Port 80 is for HTTP traffic and would not typically be used for hypervisor management."
    },
    {
    "question": "A technician is configuring security for a computer that is located in a common area. A sign above the computer indicates only authorized users can use the computer. Guests visiting the office must walk past the computer to enter and leave the office. Which of the following will offer the best protection against physical threats?",
    "options": [
        "Using screen lock",
        "Installing a privacy screen",
        "Implementing password complexity",
        "Locking the computer case",
        "Enabling drive encryption"
    ],
    "correct_answer": 4,
    "description": "The correct answer is 'Locking the computer case.' This helps prevent unauthorized physical access to the computer, which is critical in a common area where guests may walk past or interact with the system. \n\n- Using a screen lock prevents unauthorized access to the system, but doesn't address physical tampering with the machine itself. \n- Installing a privacy screen prevents others from seeing the screen but does not secure the computer physically. \n- Implementing password complexity secures the system but does not protect against physical access. \n- Enabling drive encryption secures the data on the drive but doesn't prevent physical access to the computer."
	},
    {
        "question": "A technician is reusing several hard drives to increase local storage on company workstations. The drives contain PII that is no longer needed. Which of the following should the technician do to prevent unauthorized access of the data?",
        "options": [
            "Degauss the drives.",
            "Drill through the drives.",
            "Wipe the drives.",
            "Reimage the drives."
        ],
        "correct_answer": 3,
        "description": "The correct answer is 'Wipe the drives.' Wiping the drives ensures that all data, including PII, is securely erased, preventing unauthorized access. \n\n- Degaussing the drives can be effective but may not work on solid-state drives. \n- Drilling through the drives physically destroys them but is a more extreme measure. \n- Reimaging the drives would reinstall the operating system but would not remove the existing data effectively."
    },
    {
        "question": "Users access files in the department share. When a user creates a new subfolder, only that user can access the folder and its files. Which of the following will MOST likely allow all users to access the new folders?",
        "options": [
            "Elevating quota limitations",
            "Enabling inheritance",
            "Requiring multifactor authentication",
            "Removing archive attribute"
        ],
        "correct_answer": 2,
        "description": "The correct answer is 'Enabling inheritance.' Enabling inheritance allows the new subfolder to inherit the permissions of its parent folder, allowing all users to access it. \n\n- Elevating quota limitations doesn't affect folder permissions. \n- Requiring multifactor authentication secures user access but doesn't resolve the permission issue. \n- Removing the archive attribute is unrelated to access control and affects file backup processes."
    },
    {
        "question": "The following error is displayed on a user's computer screen:\n\nNo operating system found -\n\nWhich of the following is the first troubleshooting step a technician should complete?",
        "options": [
            "Disconnect external storage.",
            "Flash the BIOS.",
            "Replace the SATA cable.",
            "Turn on the device in safe mode."
        ],
        "correct_answer": 1,
        "description": "The correct answer is 'Disconnect external storage.' External storage devices might be misconfigured as the boot device, causing the system to fail to find the operating system. \n\n- Flashing the BIOS is unlikely to resolve the issue, as the BIOS is working. \n- Replacing the SATA cable is a hardware fix that should be considered only after checking the external devices. \n- Turning the device on in safe mode is unnecessary if the system can't even detect an operating system."
    },
    {
        "question": "An MDM report shows that a user's company cell phone has unauthorized applications installed. The device has recently checked into the MDM server, and the company still has access to remote wipe the device. Which of the following describes the action the user has performed?",
        "options": [
            "Obtained root access.",
            "Upgraded the OS.",
            "Installed a VPN.",
            "Uninstalled the MDM software."
        ],
        "correct_answer": 1,
        "description": "The correct answer is 'Obtained root access.' Root access allows the user to install unauthorized applications and modify system settings, which can bypass MDM controls. \n\n- Upgrading the OS is unlikely to cause unauthorized applications to appear, although it could lead to system changes. \n- Installing a VPN would not explain unauthorized apps being installed. \n- Uninstalling the MDM software would prevent remote wipe, but the report indicates the company still has that access."
    },
    {
        "question": "Which of the following languages would a technician most likely use to automate the setup of various services on multiple systems?",
        "options": [
            "SQL",
            "HTML",
            "PowerShell",
            "C#"
        ],
        "correct_answer": 3,
        "description": "The correct answer is 'PowerShell.' PowerShell is a scripting language used to automate administrative tasks, such as configuring services on multiple systems. \n\n- SQL is a database query language and is not used for system automation. \n- HTML is a markup language used for web page structure, not for system administration. \n- C# is a general-purpose programming language, but PowerShell is better suited for system automation tasks."
    },
    {
        "question": "A technician is assisting a customer who is having difficulty accessing the company’s website. Which of the following should the technician do first?",
        "options": [
            "Ask the customer for their log-in credentials.",
            "Check the company’s internal knowledge base for solutions.",
            "Refer the customer to a more experienced technician.",
            "Record the details of the issue in the company's ticketing system."
        ],
        "correct_answer": 2,
        "description": "The correct answer is 'Check the company’s internal knowledge base for solutions.' The knowledge base may have troubleshooting steps or known issues that can help resolve the access problem. \n\n- Asking for log-in credentials should only be done after ruling out other issues. \n- Referring the customer to a more experienced technician can be an option if the issue is complex, but checking the knowledge base is more immediate. \n- Recording the details of the issue is important, but addressing the issue first is more important."
    },
	{
    "question": "A technician is installing a new SOHO wireless router and wants to ensure it is secure and uses the latest network features. Which of the following should the technician do first?",
    "options": [
        "Disable the unused ports.",
        "Enable DHCP reservations.",
        "Update the firmware.",
        "Disable the guest account."
    ],
    "correct_answer": 3,
    "description": "The correct answer is 'Update the firmware.' Ensuring the router has the latest firmware is crucial for security and accessing the latest features and bug fixes. \n\n- Disabling unused ports is important for security but comes after ensuring the router has the latest updates. \n- Enabling DHCP reservations can help with network management but does not address initial security concerns. \n- Disabling the guest account is good for security but should be done after updating firmware to ensure compatibility with the latest security features."
	},
	{
    "question": "A user accidentally installed the incorrect word processing application on an iMac. Which of the following would allow the user to uninstall the incorrect application?",
    "options": [
        "Move the application to the desktop and press delete.",
        "Identify the application in Finder and drag it to the trash can.",
        "Use Spotlight to search for the application, and then run the application.",
        "Use Time Machine to go back to the date before the installation."
    ],
    "correct_answer": 2,
    "description": "The correct answer is 'Identify the application in Finder and drag it to the trash can.' On a Mac, most applications can be uninstalled by simply dragging them to the trash. \n\n- Moving the application to the desktop and pressing delete does not uninstall the application properly. \n- Using Spotlight to search for the application and running it doesn't help with uninstallation. \n- Time Machine can be used to restore the system to a previous state but isn't the most direct method for uninstalling an application."
	}






]
