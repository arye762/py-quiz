questions_set_B = [

#201-215

    {
      "question": "A user reports a workstation has been performing strangely after a suspicious email was opened on it earlier in the week. Which of the following should the technician perform FIRST?",
      "options": [
        "Escalate the ticket to Tier 2.",
        "Run a virus scan.",
        "Utilize a Windows restore point.",
        "Reimage the computer."
      ],
      "correct_answer": 2,
      "description": "The correct answer is Run a virus scan. The FIRST step when a suspicious email is opened and the computer behaves abnormally is to check for malware. Running a virus scan helps detect and remove any malicious software before further damage is done. \n\n- Escalating the ticket would be premature before taking basic troubleshooting steps. \n- Utilizing a restore point is a later option if the virus scan does not resolve the issue. \n- Reimaging the computer is the last resort after all other methods fail."
    },
    {
      "question": "Which of the following wireless security features can be enabled to allow a user to use login credentials to attach to available corporate SSIDs?",
      "options": [
        "TACACS+",
        "Kerberos",
        "Preshared key",
        "WPA2/AES"
      ],
      "correct_answer": 4,
      "description": "The correct answer is WPA2/AES. WPA2 (Wi-Fi Protected Access 2) with AES encryption provides strong wireless security by requiring login credentials for authentication, making it suitable for corporate environments. \n\n- TACACS+ and Kerberos are authentication protocols but are not typically used for connecting to wireless networks. \n- A preshared key is less secure as it is typically used in home networks rather than corporate SSIDs."
    },
    {
      "question": "Which of the following would MOST likely be used to change the security settings on a user's device in a domain environment?",
      "options": [
        "Security groups",
        "Access control list",
        "Group Policy",
        "Login script"
      ],
      "correct_answer": 3,
      "description": "The correct answer is Group Policy. In a domain environment, Group Policy is commonly used to enforce security settings and configurations across multiple devices. \n\n- Security groups are used for managing access to resources but not for changing device settings. \n- Access control lists define permissions for users and groups but don’t directly change device settings. \n- Login scripts can run at user login but are not specifically designed for security configuration."
    },
    {
      "question": "Which of the following often uses an SMS or third-party application as a secondary method to access a system?",
      "options": [
        "MFA",
        "WPA2",
        "AES",
        "RADIUS"
      ],
      "correct_answer": 1,
      "description": "The correct answer is MFA (Multi-Factor Authentication). MFA uses a combination of something the user knows (e.g., password) and something they have (e.g., an SMS code or an app-generated code) to authenticate access to a system. \n\n- WPA2 and AES are encryption standards for securing wireless communication, not authentication methods. \n- RADIUS is an authentication and accounting system but doesn't inherently provide multi-factor authentication."
    },
    {
      "question": "A technician needs to ensure that USB devices are not suspended by the operating system. Which of the following Control Panel utilities should the technician use to configure the setting?",
      "options": [
        "System",
        "Power Options",
        "Devices and Printers",
        "Device Manager"
      ],
      "correct_answer": 2,
      "description": "The correct answer is Power Options. The technician should configure the Power Options to prevent USB selective suspend, which can cause USB devices to stop functioning temporarily when not in use. \n\n- System and Devices and Printers provide general system information but are not used to manage power settings. \n- Device Manager can troubleshoot hardware issues but doesn't control USB suspension settings."
    },
    {
      "question": "A technician needs to manually set an IP address on a computer that is running macOS. Which of the following commands should the technician use?",
      "options": [
        "ipconfig",
        "ifconfig",
        "arpa",
        "ping"
      ],
      "correct_answer": 2,
      "description": "The correct answer is ifconfig. On macOS and other Unix-based systems, the `ifconfig` command is used to manually configure network interface settings, including IP addresses. \n\n- `ipconfig` is used on Windows systems. \n- `arpa` and `ping` are network utilities but not for configuring IP settings."
    },
    {
      "question": "A user receives a call from someone who claims to be from the user's bank and requests information to ensure the user's account is safe. Which of the following social-engineering attacks is the user experiencing?",
      "options": [
        "Phishing",
        "Smishing",
        "Whaling",
        "Vishing"
      ],
      "correct_answer": 4,
      "description": "The correct answer is Vishing. Vishing (voice phishing) occurs when attackers use phone calls to deceive individuals into revealing sensitive information. \n\n- Phishing generally refers to email-based attacks. \n- Smishing is phishing through SMS messages. \n- Whaling targets high-level individuals like executives."
    },
    {
      "question": "A user called the help desk to report an issue with the internet connection speed on a laptop. The technician thinks that background services may be using extra bandwidth. Which of the following tools should the technician use to investigate connections on the laptop?",
      "options": [
        "nslookup",
        "net use",
        "netstat",
        "net user"
      ],
      "correct_answer": 3,
      "description": "The correct answer is netstat. `netstat` is a command-line tool used to display active connections and network statistics, helping the technician identify any services or processes consuming bandwidth. \n\n- `nslookup` is used for DNS queries. \n- `net use` manages network shares, and `net user` handles user accounts but neither is related to connection troubleshooting."
    },
    {
      "question": "Which of the following operating systems is considered closed source?",
      "options": [
        "Ubuntu",
        "Android",
        "CentOS",
        "OSX"
      ],
      "correct_answer": 4,
      "description": "The correct answer is OSX. Apple's macOS is a closed-source operating system, meaning its source code is not publicly available. \n\n- Ubuntu, Android, and CentOS are open-source operating systems, where the source code is accessible to the public."
    },

 {
      "question": "An internet café has several computers available for public use. Recently, users have reported the computers are much slower than they were the previous week. A technician finds the CPU is at 100% utilization, and antivirus scans report no current infection. Which of the following is MOST likely causing the issue?",
      "options": [
        "Spyware is redirecting browser searches.",
        "A cryptominer is verifying transactions.",
        "Files were damaged from a cleaned virus infection.",
        "A keylogger is capturing user passwords."
      ],
      "correct_answer": 2,
      "description": "The correct answer is A cryptominer is verifying transactions. Cryptominers use system resources to mine cryptocurrency, causing high CPU usage without obvious symptoms of infection. \n\n- Spyware typically affects browser behavior but may not cause such high CPU utilization. \n- Files damaged from a virus would likely show other signs of system failure. \n- A keylogger may capture inputs but does not usually max out CPU resources."
    },
    {
      "question": "Which of the following should be used to secure a device from known exploits?",
      "options": [
        "Encryption",
        "Remote wipe",
        "Operating system updates",
        "Cross-site scripting"
      ],
      "correct_answer": 3,
      "description": "The correct answer is Operating system updates. Keeping the operating system up-to-date is critical to patch vulnerabilities and protect against known exploits. \n\n- Encryption protects data but does not address software vulnerabilities. \n- Remote wipe is used to remove data from a lost or stolen device, not to prevent exploits. \n- Cross-site scripting (XSS) is a vulnerability, not a method for securing a device."
    },
    {
      "question": "A technician is securing a new Windows 10 workstation and wants to enable a screensaver lock. Which of the following options in the Windows settings should the technician use?",
      "options": [
        "Ease of Access",
        "Privacy",
        "Personalization",
        "Update and Security"
      ],
      "correct_answer": 3,
      "description": "The correct answer is Personalization. The screensaver settings, including lock screen configurations, are found under the Personalization option in Windows settings. \n\n- Ease of Access contains accessibility settings. \n- Privacy manages permissions and data collection. \n- Update and Security deals with system updates and security settings but not the screensaver."
    },
    {
      "question": "Sensitive data was leaked from a user's smartphone. A technician discovered an unapproved application was installed, and the user has full access to the device's command shell. Which of the following is the NEXT step the technician should take to find the cause of the leaked data?",
      "options": [
        "Restore the device to factory settings.",
        "Uninstall the unapproved application.",
        "Disable the ability to install applications from unknown sources.",
        "Ensure the device is connected to the corporate WiFi network."
      ],
      "correct_answer": 2,
      "description": "The correct answer is Uninstall the unapproved application. The first step is to remove the suspicious application to prevent further data leaks. \n\n- Restoring the device to factory settings may be necessary later but is not the next immediate step. \n- Disabling unknown sources is a preventive measure but will not address the current issue. \n- Connecting to corporate WiFi has no relevance to solving this problem."
    },
    {
      "question": "A technician is creating a full inventory of the company’s IT hardware. Which of the following should the technician use for documentation management?",
      "options": [
        "Checklist for new user setup",
        "User information",
        "Asset tags and IDs",
        "Procurement life cycle"
      ],
      "correct_answer": 3,
      "description": "The correct answer is Asset tags and IDs. Hardware inventory typically includes asset tags and IDs to track and manage IT equipment. \n\n- A checklist for new user setup deals with onboarding and is not relevant here. \n- User information pertains to user accounts and personal data, not hardware. \n- The procurement life cycle involves purchasing and managing resources, but it's not the documentation needed for an inventory."
    },
    {
      "question": "A systems administrator is creating periodic backups of a folder on a Microsoft Windows machine. The source data is very dynamic, and files are either added or deleted regularly. Which of the following utilities can be used to mirror the source data for the backup?",
      "options": [
        "copy",
        "xcopy",
        "robocopy",
        "Copy-Item"
      ],
      "correct_answer": 3,
      "description": "The correct answer is robocopy. `robocopy` is a robust command-line utility in Windows that allows for mirroring source data, copying files, and even deleting files in the destination if they no longer exist in the source. \n\n- `copy` and `xcopy` can copy files, but they lack the advanced features needed for mirroring dynamic data. \n- `Copy-Item` is a PowerShell cmdlet, but it doesn’t have the mirroring capabilities that `robocopy` offers."
    },
#216-230

    {
      "question": "Each time a user tries to go to the selected web search provider, a different website opens. Which of the following should the technician check FIRST?",
      "options": [
        "System time",
        "IP address",
        "DNS servers",
        "Windows updates"
      ],
      "correct_answer": 3,
      "description": "The correct answer is DNS servers. If a different website opens, it is likely due to incorrect DNS settings or DNS hijacking. \n\n- System time is unlikely to affect web searches directly. \n- IP address issues would typically prevent access to the internet altogether. \n- Windows updates are unrelated to website redirection issues."
    },
    {
      "question": "A technician is troubleshooting a mobile device that was dropped. The technician finds that the screen fails to rotate, even though the settings are correctly applied. Which of the following pieces of hardware should the technician replace to resolve the issue?",
      "options": [
        "LCD",
        "Battery",
        "Accelerometer",
        "Digitizer"
      ],
      "correct_answer": 3,
      "description": "The correct answer is Accelerometer. The accelerometer detects the device's orientation and is responsible for screen rotation. If settings are correct but rotation fails, the accelerometer may be damaged. \n\n- The LCD is the display; it wouldn’t affect rotation functionality. \n- The battery supplies power but does not influence screen rotation. \n- The digitizer is responsible for touch input, not orientation detection."
    },
    {
      "question": "A technician is troubleshooting an issue with a computer that contains sensitive information. The technician determines the computer needs to be taken off site for repair. Which of the following should the technician do NEXT?",
      "options": [
        "Remove the HDD and then send the computer for repair.",
        "Check corporate policies for guidance.",
        "Delete the sensitive information before the computer leaves the building.",
        "Get authorization from the manager."
      ],
      "correct_answer": 2,
      "description": "The correct answer is Check corporate policies for guidance. Corporate policies will provide the necessary steps to handle sensitive information during repair. \n\n- Removing the HDD may not be necessary if policies dictate otherwise. \n- Deleting sensitive information could be against data retention policies. \n- Getting authorization is important, but following policy is the first step."
    },
    {
      "question": "Which of the following macOS features provides the user with a high-level view of all open windows?",
      "options": [
        "Mission Control",
        "Finder",
        "Multiple Desktops",
        "Spotlight"
      ],
      "correct_answer": 1,
      "description": "The correct answer is Mission Control. Mission Control provides an overview of all open windows and spaces, allowing easy navigation. \n\n- Finder is used for file management, not window overview. \n- Multiple Desktops allows for organizing windows but doesn't provide an overview of all. \n- Spotlight is a search feature, not a window manager."
    },
    {
      "question": "A technician is creating a tunnel that hides IP addresses and secures all network traffic. Which of the following protocols is capable of enduring enhanced security?",
      "options": [
        "DNS",
        "IPS",
        "VPN",
        "SSH"
      ],
      "correct_answer": 3,
      "description": "The correct answer is VPN. A Virtual Private Network (VPN) creates a secure tunnel for internet traffic, hiding IP addresses and encrypting data. \n\n- DNS is for resolving domain names and does not secure traffic. \n- IPS (Intrusion Prevention System) monitors traffic but does not create a secure tunnel. \n- SSH (Secure Shell) is used for secure remote access but does not function as a VPN."
    },
    {
      "question": "A technician receives a call from a user who is having issues with an application. To best understand the issue, the technician simultaneously views the user's screen with the user. Which of the following would BEST accomplish this task?",
      "options": [
        "SSH",
        "VPN",
        "VNC",
        "RDP"
      ],
      "correct_answer": 3,
      "description": "The correct answer is VNC. Virtual Network Computing (VNC) allows the technician to view and control the user's screen remotely, making it ideal for troubleshooting. \n\n- SSH is for command-line access, not graphical sessions. \n- VPN secures network traffic but does not facilitate screen sharing. \n- RDP (Remote Desktop Protocol) is also for remote access but may not be as easily used in a direct user-assisted scenario."
    },
    {
      "question": "After a failed update, an application no longer launches and generates the following error message: Application needs to be repaired. Which of the following Windows 10 utilities should a technician use to address this concern?",
      "options": [
        "Device Manager",
        "Administrator Tools",
        "Programs and Features",
        "Recovery"
      ],
      "correct_answer": 3,
      "description": "The correct answer is Programs and Features. This utility allows technicians to repair or uninstall applications in Windows 10. \n\n- Device Manager is for managing hardware devices, not applications. \n- Administrator Tools contains system tools but doesn't directly manage applications. \n- Recovery is used for system restore points and repair but not specifically for applications."
    },
    {
      "question": "A technician needs to access a Windows 10 desktop on the network in a SOHO using RDP. Although the connection is unsuccessful, the technician is able to ping the computer successfully. Which of the following is MOST likely preventing the connection?",
      "options": [
        "The Windows 10 desktop has Windows 10 Home installed.",
        "The Windows 10 desktop does not have DHCP configured.",
        "The Windows 10 desktop is connected via Wi-Fi.",
        "The Windows 10 desktop is hibernating."
      ],
      "correct_answer": 1,
      "description": "The correct answer is The Windows 10 desktop has Windows 10 Home installed. Windows 10 Home does not support RDP server functionality, which would prevent a successful connection. \n\n- DHCP configuration does not affect RDP connectivity directly if the IP is known. \n- Wi-Fi connectivity should not inherently prevent RDP access. \n- Hibernating may cause the system to be unresponsive, but in this case, the ping indicates it's still active."
    },
    {
      "question": "A new employee was hired recently. Which of the following documents will the new employee need to sign before being granted login access to the network?",
      "options": [
        "MSDS",
        "EULA",
        "UAC",
        "AUP"
      ],
      "correct_answer": 4,
      "description": "The correct answer is AUP (Acceptable Use Policy). This document outlines acceptable behavior for using the company's network and resources. \n\n- MSDS (Material Safety Data Sheet) relates to chemical safety, not IT access. \n- EULA (End User License Agreement) pertains to software usage, not network access. \n- UAC (User Account Control) is a Windows feature and not a document."
    },
    {
      "question": "An organization implemented a method of wireless security that requires both a user and the user's computer to be in specific managed groups on the server in order to connect to Wi-Fi. Which of the following wireless security methods BEST describes what this organization implemented?",
      "options": [
        "TKIP",
        "RADIUS",
        "WPA2",
        "AES"
      ],
      "correct_answer": 2,
      "description": "The correct answer is RADIUS (Remote Authentication Dial-In User Service). RADIUS is used for managing authentication and access control based on group membership. \n\n- TKIP (Temporal Key Integrity Protocol) is an encryption protocol, not an access control method. \n- WPA2 is a security protocol that may utilize RADIUS but does not describe the access method itself. \n- AES (Advanced Encryption Standard) is an encryption standard used in WPA2 but is not related to user authentication."
    },
    {
      "question": "Which of the following is used to integrate Linux servers and desktops into Windows Active Directory environments?",
      "options": [
        "apt-get",
        "CIFS",
        "Samba",
        "grep"
      ],
      "correct_answer": 3,
      "description": "The correct answer is Samba. Samba is a software suite that allows Linux and Unix systems to communicate with Windows systems and share files and printers. \n\n- apt-get is a package management command used in Debian-based Linux distributions. \n- CIFS (Common Internet File System) is a network file sharing protocol, not an integration tool. \n- grep is a command-line utility for searching plain-text data, not related to Active Directory."
    },
    {
      "question": "A technician is setting up a newly built computer. Which of the following is the FASTEST way for the technician to install Windows 10?",
      "options": [
        "Factory reset",
        "System Restore",
        "In-place upgrade",
        "Unattended installation"
      ],
      "correct_answer": 4,
      "description": "The correct answer is Unattended installation. This method automates the installation process, allowing Windows 10 to be installed quickly without manual input. \n\n- Factory reset is used to restore an existing installation, not to install a new one. \n- System Restore returns a system to a previous state and does not install Windows. \n- In-place upgrade involves installing a new version over an existing one, which takes more time."
    },
    {
      "question": "A network technician installed a SOHO router for a home office user. The user has read reports about home routers being targeted by malicious actors and then used in DDoS attacks. Which of the following can the technician MOST likely do to defend against this threat?",
      "options": [
        "Add network content filtering.",
        "Disable the SSID broadcast.",
        "Configure port forwarding.",
        "Change the default credentials."
      ],
      "correct_answer": 4,
      "description": "The correct answer is Change the default credentials. Changing the default username and password for the router helps secure it from unauthorized access, reducing the risk of DDoS attacks. \n\n- Adding network content filtering is good for managing web traffic but does not secure the router. \n- Disabling SSID broadcast makes the network less visible but does not enhance security. \n- Configuring port forwarding is necessary for specific services but can also expose the network if not done securely."
    },
    {
      "question": "A kiosk, which is running Microsoft Windows 10, relies exclusively on a numeric keypad to allow customers to enter their ticket numbers but no other information. If the kiosk is idle for four hours, the login screen locks. Which of the following sign-on options would allow any employee the ability to unlock the kiosk?",
      "options": [
        "Requiring employees to enter their usernames and passwords",
        "Setting up facial recognition for each employee",
        "Using a PIN and providing it to employees",
        "Requiring employees to use their fingerprints"
      ],
      "correct_answer": 3,
      "description": "The correct answer is Using a PIN and providing it to employees. A shared PIN allows easy access for multiple employees without needing individual credentials. \n\n- Requiring usernames and passwords complicates access for multiple users. \n- Facial recognition requires setup for each employee, which can be cumbersome. \n- Fingerprint scanning requires specific hardware and enrollment for each employee, making it less practical for easy access."
    },
    {
      "question": "A data center is required to destroy SSDs that contain sensitive information. Which of the following is the BEST method to use for the physical destruction of SSDs?",
      "options": [
        "Wiping",
        "Low-level formatting",
        "Shredding",
        "Erasing"
      ],
      "correct_answer": 3,
      "description": "The correct answer is Shredding. Physically shredding SSDs is the most effective method for ensuring that data cannot be recovered, providing physical destruction of the storage medium. \n\n- Wiping and erasing only prepare the data for deletion but do not physically destroy the hardware. \n- Low-level formatting may not be effective for SSDs and does not guarantee data destruction."
    },

#231-245

    {
    "question": "A user reports that the pages flash on the screen two or three times before finally staying open when attempting to access banking web pages. Which of the following troubleshooting steps should the technician perform NEXT to resolve the issue?",
    "options": [
        "Examine the antivirus logs.",
        "Verify the address bar URL.",
        "Test the internet connection speed.",
        "Check the web service status."
    ],
    "correct_answer": 2,
    "description": "The correct answer is to verify the address bar URL. This step is crucial to ensure that the user is accessing the correct banking website and that they are not being redirected to a malicious site. \n\n- Examining the antivirus logs can help identify potential malware, but verifying the URL addresses the immediate concern of the flashing issue. \n- Testing internet connection speed may assist in diagnosing bandwidth problems, but it might not be relevant to the flashing behavior. \n- Checking the web service status is useful for determining if the bank's website is down, but the first step should be confirming the URL."
},
    {
        "question": "Which of the following script types is used with the Python language by default?",
        "options": [
            ".ps1",
            ".vbs",
            ".bat",
            ".py"
        ],
        "correct_answer": 4,
        "description": "The correct answer is .py. This is the default file extension for Python scripts, indicating that the file contains Python code. \n\n- .ps1 files are for PowerShell scripts and are unrelated to Python. \n- .vbs files indicate Visual Basic Script, which is also not used for Python. \n- .bat files are batch files for Windows command-line scripts, not for Python."
    },
    {
        "question": "Which of the following only has a web browser interface?",
        "options": [
            "Linux",
            "Microsoft Windows",
            "iOS",
            "Chromium"
        ],
        "correct_answer": 4,
        "description": "The correct answer is Chromium. This is an open-source web browser project that has a web-only interface. \n\n- Linux is an operating system that can have various interfaces, including graphical and command-line. \n- Microsoft Windows is a full operating system with many features beyond just a web browser. \n- iOS is an operating system for mobile devices that includes a web browser but is not exclusively web-based."
    },
    {
        "question": "A user has been unable to receive emails or browse the internet from a smartphone while traveling. However, text messages and phone calls are working without issue. Which of the following should a support technician check FIRST?",
        "options": [
            "User account status",
            "Mobile OS version",
            "Data plan coverage",
            "Network traffic outages"
        ],
        "correct_answer": 3,
        "description": "The correct answer is to check data plan coverage. Since the user can make calls and send texts, it's likely that the voice plan is active, but data connectivity issues may stem from insufficient data coverage. \n\n- User account status might be relevant if all services were down, but the user is able to make calls. \n- Mobile OS version could cause app issues but is less likely to affect basic connectivity. \n- Network traffic outages could be a factor but should be checked after verifying the data plan."
    },
    {
        "question": "The web browsing speed on a customer's mobile phone slows down every few weeks and then returns to normal after three or four days. Restarting the device does not usually restore performance. Which of the following should a technician check FIRST to troubleshoot this issue?",
        "options": [
            "Data usage limits",
            "Wi-Fi connection speed",
            "Status of airplane mode",
            "System uptime"
        ],
        "correct_answer": 1,
        "description": "The correct answer is to check data usage limits. If the web browsing speed slows down periodically, the customer may be hitting their data limit or throttling threshold. \n\n- Checking Wi-Fi connection speed is useful but may not be the primary issue if it’s a recurring pattern with mobile data. \n- The status of airplane mode is unlikely to be relevant if the user can still use the phone for calls and texts. \n- System uptime is less relevant since the issue seems tied to data usage rather than device performance."
    },
    {
        "question": "A user calls the help desk to report that mapped drives are no longer accessible. The technician verifies that clicking on any of the drives on the user's machine results in an error message. Other users in the office are not having any issues. As a first step, the technician would like to remove and attempt to reconnect the drives. Which of the following command-line tools should the technician use?",
        "options": [
            "net use",
            "set",
            "mkdir",
            "rename"
        ],
        "correct_answer": 1,
        "description": "The correct answer is net use. This command is specifically designed to manage network connections and allows users to disconnect or reconnect mapped drives. \n\n- The set command is used to display or set environment variables, not for managing network drives. \n- The mkdir command is for creating directories and is not relevant in this context. \n- The rename command is used to rename files or directories, which does not address the mapped drive issue."
    },
    {
        "question": "A technician is editing the hosts file on a few PCs in order to block certain domains. Which of the following would the technician need to execute after editing the hosts file?",
        "options": [
            "Enable promiscuous mode.",
            "Clear the browser cache.",
            "Add a new network adapter.",
            "Reset the network adapter."
        ],
        "correct_answer": 2,
        "description": "The correct answer is to clear the browser cache. After editing the hosts file, clearing the cache ensures that the browser does not use any old DNS data that could bypass the changes made. \n\n- Enabling promiscuous mode is a network setting that is not related to modifying the hosts file. \n- Adding a new network adapter is unnecessary for this task. \n- Resetting the network adapter might refresh the connection, but it does not address the immediate need to clear cached data."
    },
    {
        "question": "A technician is finalizing a new workstation for a user. The user's PC will be connected to the internet but will not require the same private address each time. Which of the following protocols will the technician MOST likely utilize?",
        "options": [
            "DHCP",
            "SMTP",
            "DNS",
            "RDP"
        ],
        "correct_answer": 1,
        "description": "The correct answer is DHCP. This protocol automatically assigns IP addresses to devices on a network, allowing them to change each time they connect. \n\n- SMTP is used for sending emails and is not relevant for IP address assignment. \n- DNS translates domain names to IP addresses and does not manage addressing directly. \n- RDP is used for remote desktop connections and is unrelated to IP address management."
    },
    {
        "question": "A company acquired a local office, and a technician is attempting to join the machines at the office to the local domain. The technician notes that the domain join option appears to be missing. Which of the following editions of Windows is MOST likely installed on the machines?",
        "options": [
            "Windows Professional",
            "Windows Education",
            "Windows Enterprise",
            "Windows Home"
        ],
        "correct_answer": 4,
        "description": "The correct answer is Windows Home. This edition does not support joining a domain, which explains the missing option. \n\n- Windows Professional does allow domain joins and is typically used in business environments. \n- Windows Education is designed for academic institutions and supports domain joining. \n- Windows Enterprise also supports domain functionality and is used in larger organizations."
    },
    {
        "question": "A technician discovers user input has been captured by a malicious actor. Which of the following malware types is MOST likely being used?",
        "options": [
            "Cryptominers",
            "Rootkit",
            "Spear phishing",
            "Keylogger"
        ],
        "correct_answer": 4,
        "description": "The correct answer is keylogger. This type of malware is designed to capture user input, such as keystrokes, to steal sensitive information like passwords. \n\n- Cryptominers are used to generate cryptocurrency but do not capture user input. \n- Rootkits allow unauthorized access but typically do not capture keystrokes directly. \n- Spear phishing is a social engineering tactic to deceive users into revealing information, rather than malware that captures input."
    },
    {
        "question": "A user is trying to use a third-party USB adapter but is experiencing connection issues. Which of the following tools should the technician use to resolve this issue?",
        "options": [
            "taskschd.msc",
            "eventvwr.msc",
            "devmgmt.msc",
            "diskmgmt.msc"
        ],
        "correct_answer": 3,
        "description": "The correct answer is devmgmt.msc. This command opens Device Manager, where the technician can troubleshoot hardware issues, including USB adapter problems. \n\n- taskschd.msc is for managing scheduled tasks and does not pertain to device management. \n- eventvwr.msc opens the Event Viewer, which is useful for viewing logs but not for resolving hardware issues. \n- diskmgmt.msc is for managing disks and partitions, which is not relevant for USB adapter connection issues."
    },
    {
        "question": "Which of the following defines the extent of a change?",
        "options": [
            "Scope",
            "Purpose",
            "Analysis",
            "Impact"
        ],
        "correct_answer": 1,
        "description": "The correct answer is scope. This term refers to the boundaries and extent of a project or change, defining what is included and excluded. \n\n- Purpose refers to the reason for the change, not its extent. \n- Analysis involves examining data but does not define change boundaries. \n- Impact assesses the effects of a change, which is different from defining its scope."
    },
    {
        "question": "All the desktop icons on a user's newly issued PC are very large. The user reports that the PC was working fine until a recent software patch was deployed. Which of the following would BEST resolve the issue?",
        "options": [
            "Rolling back video card drivers",
            "Restoring the PC to factory settings",
            "Repairing the Windows profile",
            "Reinstalling the Windows OS"
        ],
        "correct_answer": 1,
        "description": "The correct answer is rolling back video card drivers. A recent software patch may have caused compatibility issues with the video drivers, resulting in large icons. Rolling back the driver can restore the previous settings. \n\n- Restoring the PC to factory settings is a drastic step and not necessary if the driver rollback can resolve the issue. \n- Repairing the Windows profile might help but does not directly address driver-related icon size problems. \n- Reinstalling the Windows OS is also too extreme given the context of the issue."
    },
   {
    "question": "A computer on a corporate network has a malware infection. Which of the following would be the BEST method for returning the computer to service?",
    "options": [
        "Scanning the system with a Linux live disc, flashing the BIOS, and then returning the computer to service",
        "Flashing the BIOS, reformatting the drive, and then reinstalling the OS",
        "Degaussing the hard drive, flashing the BIOS, and then reinstalling the OS",
        "Reinstalling the OS, flashing the BIOS, and then scanning with on-premises antivirus"
    ],
    "correct_answer": 2,
    "description": "The correct answer is flashing the BIOS, reformatting the drive, and then reinstalling the OS. This method ensures that the system is completely cleansed of malware, starting with a fresh operating environment. \n\n- Scanning the system with a Linux live disc is effective for malware removal but may not guarantee complete protection if the BIOS is compromised. \n- Degaussing the hard drive is extreme and unnecessary unless dealing with highly sensitive data destruction. \n- Reinstalling the OS and scanning with on-premises antivirus may miss deep-rooted infections that could persist after the OS is reinstalled."
    },
    {
        "question": "A technician is installing a program from an ISO file. Which of the following steps should the technician take?",
        "options": [
            "Mount the ISO and run the installation file.",
            "Copy the ISO and execute on the server.",
            "Copy the ISO file to a backup location and run the ISO file.",
            "Unzip the ISO and execute the setup.exe file."
        ],
        "correct_answer": 1,
        "description": "The correct answer is to mount the ISO and run the installation file. This allows for proper access to the files contained within the ISO, enabling installation. \n\n- Copying the ISO to execute on a server is not a standard method for installation and could lead to errors. \n- Copying to a backup location does not assist in installation. \n- Unzipping the ISO is unnecessary, as mounting it provides direct access to the contents."
    },

#246-260


    {
        "question": "A technician installed Windows 10 on a workstation. The workstation only has 3.5GB of usable RAM, even though the technician installed 8GB. Which of the following is the MOST likely reason this system is not utilizing all the available RAM?",
        "options": [
            "The system is missing updates.",
            "The system is utilizing a 32-bit OS.",
            "The system's memory is failing.",
            "The system requires BIOS updates."
        ],
        "correct_answer": 2,
        "description": "The correct answer is that the system is utilizing a 32-bit OS. A 32-bit operating system can only address up to 4GB of RAM, and typically, the usable RAM is less than that due to system overhead. \n\n- Missing updates could affect system performance but would not limit RAM usage to this extent. \n- Failing memory might cause crashes or errors but is unlikely to limit RAM visibility. \n- BIOS updates can enhance compatibility but wouldn't change the addressable memory limit imposed by a 32-bit OS."
    },
    {
        "question": "While staying at a hotel, a user attempts to connect to the hotel Wi-Fi but notices that multiple SSIDs have very similar names. Which of the following social-engineering attacks is being attempted?",
        "options": [
            "Evil twin",
            "Impersonation",
            "Insider threat",
            "Whaling"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Evil twin. This attack involves creating a rogue Wi-Fi hotspot that mimics a legitimate network, tricking users into connecting. \n\n- Impersonation refers to pretending to be someone else, but it does not specifically relate to Wi-Fi attacks. \n- Insider threat involves risks from within the organization, not typically associated with hotel Wi-Fi. \n- Whaling is a form of phishing aimed at high-profile individuals and does not directly involve network connections."
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
        "description": "The correct answer is drive failure. The S.M.A.R.T. error indicates potential hard drive issues, which are likely to result in the OS not being found. \n\n- Boot order problems might prevent booting but typically would not cause a S.M.A.R.T. error. \n- Malware could interfere with booting, but the S.M.A.R.T. error suggests a physical issue with the drive. \n- Windows updates are unlikely to cause this specific problem unless they were interrupted, but they wouldn't result in a S.M.A.R.T. error."
    },
    {
    "question": "The battery life on an employee's new phone seems to be drastically less than expected, and the screen stays on for a very long time after the employee sets the phone down. Which of the following should the technician check FIRST to troubleshoot this issue? (Choose two.)",
    "options": [
        "Screen resolution",
        "Screen zoom",
        "Screen timeout",
        "Screen brightness",
        "Screen damage",
        "Screen motion smoothness"
    ],
    "correct_answer": [3, 4],
    "description": "The correct answers are screen timeout and screen brightness. Checking these settings is essential as a shorter screen timeout can ensure the display turns off when not in use, and reducing brightness can significantly conserve battery power. \n\n- Screen resolution typically impacts performance rather than battery life. \n- Screen zoom does not directly affect battery consumption. \n- Screen damage may lead to functional issues but wouldn't inherently cause excessive battery usage. \n- Screen motion smoothness enhances user experience but is less critical for optimizing battery performance."
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
        "description": "The correct answer is risk analysis. This process identifies potential problems and impacts related to change implementation, ensuring preparedness for any adverse effects. \n\n- Scope change refers to adjustments in project parameters, not specifically to potential issues. \n- End-user acceptance measures user satisfaction but does not address problems that may arise. \n- Rollback plans detail steps to revert changes but do not provide an analysis of risks."
    },
    {
        "question": "Which of the following is an advantage of using WPA2 instead of WPA3?",
        "options": [
            "Connection security",
            "Encryption key length",
            "Device compatibility",
            "Offline decryption resistance"
        ],
        "correct_answer": 3,
        "description": "The correct answer is device compatibility. WPA2 is supported by a wider range of devices compared to WPA3, making it more versatile for various environments. \n\n- Connection security is improved in WPA3. \n- Encryption key length is generally longer in WPA3. \n- Offline decryption resistance is also better in WPA3 due to enhanced security protocols."
    },
    {
        "question": "A technician needs to remotely connect to a Linux desktop to assist a user with troubleshooting. The technician needs to make use of a tool natively designed for Linux. Which of the following tools will the technician MOST likely use?",
        "options": [
            "VNC",
            "MFA",
            "MSRA",
            "RDP"
        ],
        "correct_answer": 1,
        "description": "The correct answer is VNC. This tool is widely used for remote desktop access on Linux systems and is natively compatible. \n\n- MFA (Multi-Factor Authentication) is a security measure, not a remote access tool. \n- MSRA (Microsoft Remote Assistance) is for Windows systems, not Linux. \n- RDP (Remote Desktop Protocol) is primarily a Windows protocol and is not natively designed for Linux."
    },
    {
        "question": "A technician is preparing to remediate a Trojan virus that was found on a workstation. Which of the following steps should the technician complete BEFORE removing the virus?",
        "options": [
            "Disable System Restore.",
            "Schedule a malware scan.",
            "Educate the end user.",
            "Run Windows Update."
        ],
        "correct_answer": 1,
        "description": "The correct answer is to disable System Restore. This step is crucial to prevent the Trojan from being reintroduced from a restore point after removal. \n\n- Scheduling a malware scan can help find threats but is not necessary before removal. \n- Educating the end user is important for future prevention but does not impact the immediate threat. \n- Running Windows Update is good practice but does not directly affect the malware removal process."
    },
  {
    "question": "Which of the following options should MOST likely be considered when preserving data from a hard drive for forensic analysis? (Choose two.)",
    "options": [
        "Licensing agreements",
        "Chain of custody",
        "Incident management documentation",
        "Data integrity",
        "Material safety data sheet",
        "Retention requirements"
    ],
    "correct_answer": [2, 4],
    "description": "The correct answers are chain of custody and data integrity. Chain of custody ensures that the data is handled properly and maintains its authenticity, while data integrity verifies that the information has not been altered. \n\n- Licensing agreements do not relate directly to data preservation. \n- Incident management documentation is important but secondary to the preservation itself. \n- Material safety data sheets and retention requirements are less relevant in forensic contexts."
},
{
    "question": "Which of the following would MOST likely be deployed to enhance physical security for a building? (Choose two.)",
    "options": [
        "Multifactor authentication",
        "Badge reader",
        "Personal identification number",
        "Firewall",
        "Motion sensor",
        "Soft token"
    ],
    "correct_answer": [2, 5],
    "description": "The correct answers are badge reader and motion sensor. Badge readers control access to the building, ensuring only authorized individuals can enter, while motion sensors enhance security by detecting unauthorized movement and alerting personnel to potential intrusions. \n\n- Multifactor authentication primarily applies to digital security, not physical access. \n- Personal identification numbers often work in conjunction with physical access tools but do not function as standalone solutions. \n- Firewalls are devices used for network security, not physical security measures. \n- Soft tokens are designed for digital authentication rather than physical access."
},

    {
        "question": "A technician, who is working at a local office, has found multiple copies of home edition software installed on computers. Which of the following does this MOST likely violate?",
        "options": [
            "EULA",
            "PII",
            "DRM",
            "Open-source agreement"
        ],
        "correct_answer": 1,
        "description": "The correct answer is EULA (End User License Agreement). Installing multiple copies of home edition software typically violates the licensing terms set forth in the EULA. \n\n- PII (Personally Identifiable Information) concerns data privacy but is not relevant in this context. \n- DRM (Digital Rights Management) is related to protecting copyrighted material but does not directly address software installation issues. \n- Open-source agreements apply to software that is freely available for use and modification, not commercial software."
    },
    {
        "question": "A user tries to access commonly used web pages but is redirected to unexpected websites. Clearing the web browser cache does not resolve the issue. Which of the following should a technician investigate NEXT to resolve the issue?",
        "options": [
            "Enable firewall ACLs.",
            "Examine the localhost file entries.",
            "Verify the routing tables.",
            "Update the antivirus definitions."
        ],
        "correct_answer": 2,
        "description": "The correct answer is to examine the localhost file entries. These entries can be modified by malware to redirect traffic, which could explain the user's redirection to unexpected sites. \n\n- Enabling firewall ACLs may enhance security but will not address the redirection issue. \n- Verifying routing tables is more complex and less likely the cause. \n- Updating antivirus definitions is good practice, but the redirection problem should be investigated first."
    },
    {
        "question": "Which of the following features must be configured on a Windows OS desktop in order to encrypt files in a laptop?",
        "options": [
            "HDD drivers",
            "BitLocker",
            "Boot settings",
            "RAID"
        ],
        "correct_answer": 2,
        "description": "The correct answer is BitLocker. This feature is specifically designed to encrypt files and protect data on Windows devices. \n\n- HDD drivers are necessary for disk operation but are not directly related to encryption. \n- Boot settings may affect startup but do not influence file encryption. \n- RAID is a storage configuration method that does not provide encryption."
    },
    {
        "question": "A manager called the help desk to ask for assistance with creating a more secure environment for the finance department, which resides in a non-domain environment. Which of the following would be the BEST method to protect against unauthorized use?",
        "options": [
            "Implementing password expiration",
            "Restricting user permissions",
            "Using screen locks",
            "Disabling unnecessary services"
        ],
        "correct_answer": 2,
        "description": "The correct answer is restricting user permissions. This approach minimizes the risk of unauthorized access by limiting what users can do within the system. \n\n- Implementing password expiration is good practice but does not address all unauthorized access risks. \n- Using screen locks is a helpful security measure but is more of a first line of defense. \n- Disabling unnecessary services enhances security but does not directly restrict access based on user roles."
    },
    {
        "question": "A Windows workstation that was recently updated with approved system patches shut down instead of restarting. Upon reboot, the technician notices an alert stating the workstation has malware in the root OS folder. The technician promptly performs a System Restore and reboots the workstation, but the malware is still detected. Which of the following BEST describes why the system still has malware?",
        "options": [
            "A system patch disabled the antivirus protection and host firewall.",
            "The system updates did not include the latest anti-malware definitions.",
            "The system restore process was compromised by the malware.",
            "The malware was installed before the system restore point was created."
        ],
        "correct_answer": 4,
        "description": "The correct answer is that the malware was installed before the system restore point was created. This means that the malware would still be present even after restoring to a previous state. \n\n- A system patch disabling antivirus protection is possible but unlikely to be the sole reason for persistent malware. \n- Updates may not have included the latest anti-malware definitions, but the presence of malware indicates a prior infection. \n- A compromised restore process is possible but less likely than the malware being present before the restore."
    },
#261-280


        {
            "question": "Which of the following filesystem formats would be the BEST choice to ensure read and write compatibility of USB flash drives across several generations of Microsoft operating systems?",
            "options": [
                "APFS",
                "ext4",
                "CDFS",
                "FAT32"
            ],
            "correct_answer": 4,
            "description": "The correct answer is FAT32. FAT32 is widely compatible with various versions of Microsoft Windows, making it the best choice for ensuring read and write functionality across different operating systems. \n\n- APFS is primarily used by macOS and iOS, limiting compatibility with Windows. \n- ext4 is a Linux filesystem format, not natively supported by Windows. \n- CDFS is used for CD-ROMs and is not suitable for flash drives."
        },
        {
            "question": "Which of the following would cause a corporate-owned iOS device to have an Activation Lock issue?",
            "options": [
                "A forgotten keychain password",
                "An employee's Apple ID used on the device",
                "An operating system that has been jailbroken",
                "An expired screen unlock code"
            ],
            "correct_answer": 2,
            "description": "The correct answer is an employee's Apple ID used on the device. Activation Lock is tied to the Apple ID and prevents unauthorized access if the device is lost or stolen. \n\n- A forgotten keychain password would not trigger Activation Lock. \n- Jailbreaking can bypass restrictions, but it does not directly cause Activation Lock. \n- An expired screen unlock code affects access but does not impact Activation Lock."
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
            "description": "The correct answer is Finder. Finder serves as the default file manager and GUI for macOS, allowing users to navigate files and applications easily. \n\n- Disk Utility is used for disk management tasks. \n- The Dock is a UI element for launching applications, not a file manager. \n- FileVault is a disk encryption program."
        },
        {
            "question": "A technician is attempting to mitigate micro power outages, which occur frequently within the area of operation. The outages are usually short, with the longest occurrence lasting five minutes. Which of the following should the technician use to mitigate this issue?",
            "options": [
                "Surge suppressor",
                "Battery backup",
                "CMOS battery",
                "Generator backup"
            ],
            "correct_answer": 2,
            "description": "The correct answer is a battery backup. A battery backup (UPS) provides temporary power during short outages, allowing systems to continue operating without interruption. \n\n- A surge suppressor protects against voltage spikes but does not provide backup power. \n- A CMOS battery is for maintaining BIOS settings, not for power outages. \n- Generator backup is more suited for extended outages."
        },
        {
            "question": "A user contacts a technician about an issue with a laptop. The user states applications open without being launched and the browser redirects when trying to go to certain websites. Which of the following is MOST likely the cause of the user's issue?",
            "options": [
                "Keylogger",
                "Cryptominers",
                "Virus",
                "Malware"
            ],
            "correct_answer": 4,
            "description": "The correct answer is malware. The symptoms of applications launching unexpectedly and browser redirections indicate malicious software that affects system behavior. \n\n- A keylogger records keystrokes but wouldn’t cause these symptoms directly. \n- Cryptominers utilize system resources but typically don't alter application behavior. \n- While a virus is a type of malware, the broader term 'malware' encompasses various malicious software types."
        },
        {
            "question": "Which of the following security methods supports the majority of current Wi-Fi-capable devices without sacrificing security?",
            "options": [
                "WPA3",
                "MAC filtering",
                "RADIUS",
                "TACACS+"
            ],
            "correct_answer": 1,
            "description": "The correct answer is WPA3. WPA3 provides robust security features for modern Wi-Fi networks while maintaining compatibility with most Wi-Fi-capable devices. \n\n- MAC filtering provides minimal security as MAC addresses can be spoofed. \n- RADIUS and TACACS+ are authentication protocols more suited for enterprise networks rather than individual device security."
        },
        {
            "question": "Which of the following threats will the use of a privacy screen on a computer help prevent?",
            "options": [
                "Impersonation",
                "Shoulder surfing",
                "Whaling",
                "Tailgating"
            ],
            "correct_answer": 2,
            "description": "The correct answer is shoulder surfing. A privacy screen restricts the viewing angle of the display, helping prevent unauthorized individuals from seeing sensitive information. \n\n- Impersonation involves pretending to be someone else, which a privacy screen cannot mitigate. \n- Whaling is a type of phishing targeting high-profile individuals and is unrelated to physical viewing of screens. \n- Tailgating refers to physical security breaches rather than visual ones."
        },
        {
            "question": "A technician needs to override DNS and redirect IP addresses and URLs to different locations. Which of the following should the technician do?",
            "options": [
                "Install signal repeaters.",
                "Edit the hosts file.",
                "Configure the firewall.",
                "Enable port forwarding."
            ],
            "correct_answer": 2,
            "description": "The correct answer is to edit the hosts file. Modifying the hosts file allows the technician to manually redirect URLs and IP addresses on the local machine. \n\n- Signal repeaters extend wireless range but do not affect DNS resolution. \n- Configuring the firewall typically involves controlling incoming/outgoing traffic, not DNS overrides. \n- Port forwarding is used for directing external traffic to specific internal devices, not for DNS modification."
        },
        {
            "question": "A company needs employees who work remotely to have secure access to the corporate intranet. Which of the following should the company implement?",
            "options": [
                "Password-protected Wi-Fi",
                "Port forwarding",
                "Virtual private network",
                "Perimeter network"
            ],
            "correct_answer": 3,
            "description": "The correct answer is a virtual private network (VPN). A VPN provides secure encrypted connections for remote employees accessing the corporate intranet, protecting sensitive data from interception. \n\n- Password-protected Wi-Fi secures the network but does not provide encryption for remote access. \n- Port forwarding is used for directing specific traffic and is not a secure solution for remote access. \n- A perimeter network is used for additional security layers but does not provide direct secure access for remote users."
        },
        {
            "question": "Which of the following operating systems can allow users to have access to the source code, can host various server applications, and can be command line only?",
            "options": [
                "Windows",
                "macOS",
                "Linux",
                "Chrome OS"
            ],
            "correct_answer": 3,
            "description": "The correct answer is Linux. Linux is an open-source operating system that allows users full access to its source code, supports various server applications, and can be operated entirely from the command line. \n\n- Windows and macOS are proprietary and do not provide source code access. \n- Chrome OS is a lightweight OS primarily designed for web applications and does not support extensive server functionalities."
        },
        {
            "question": "A technician is investigating options to secure a small office wireless network. One requirement is to allow automatic logins to the network using certificates instead of passwords. Which of the following should the wireless solution have in order to support this feature?",
            "options": [
                "RADIUS",
                "AES",
                "EAP-EKE",
                "MFA"
            ],
            "correct_answer": 1,
            "description": "The correct answer is RADIUS. RADIUS (Remote Authentication Dial-In User Service) allows for authentication and authorization of users via certificates, enabling secure automatic logins. \n\n- AES is an encryption standard but does not handle authentication directly. \n- EAP-EKE is an authentication method but is not typically used for certificate-based logins. \n- MFA (Multi-Factor Authentication) enhances security but is not specifically related to certificate-based logins."
        },
        {
            "question": "A SOHO client is having trouble navigating to a corporate website. Which of the following should a technician do to allow access?",
            "options": [
                "Adjust the content filtering.",
                "Unmap port forwarding.",
                "Disable unused ports.",
                "Reduce the encryption strength."
            ],
            "correct_answer": 1,
            "description": "The correct answer is to adjust the content filtering. Content filtering may be blocking access to the corporate website, and adjusting the settings can resolve the issue. \n\n- Unmapping port forwarding is typically related to incoming connections, not directly affecting web browsing. \n- Disabling unused ports may improve security but would not necessarily resolve access issues to specific websites. \n- Reducing encryption strength could pose a security risk and is not advisable for improving website access."
        },
        {
            "question": "A technician needs a way to test software without placing company systems at risk. Which of the following features should the technician use to completely isolate the testing environment from the host machine?",
            "options": [
                "Virtual machine",
                "Cloud service",
                "Snapshot",
                "Dual-boot"
            ],
            "correct_answer": 1,
            "description": "The correct answer is a virtual machine (VM). A VM allows the technician to run software in an isolated environment, preventing any potential harm to the host system. \n\n- Cloud services may offer isolated environments but depend on external resources. \n- A snapshot captures the state of a VM but does not create isolation. \n- Dual-booting runs two operating systems on the same hardware, which could still pose a risk to the host system."
        },
        {
            "question": "A technician needs a way to test software without placing company systems at risk. Which of the following features should the technician use to completely achieve this objective?",
            "options": [
                "Cryptography",
                "Sandbox",
                "Perimeter network",
                "Firewall"
            ],
            "correct_answer": 2,
            "description": "The correct answer is a sandbox. A sandbox allows for the testing of software in a controlled environment, isolating it from the rest of the system to prevent potential harm. \n\n- Cryptography secures data but does not create a testing environment. \n- A perimeter network adds security to a network's boundaries but does not isolate software testing. \n- A firewall protects systems but does not provide an isolated environment for testing."
        },
        {
            "question": "A systems administrator notices that a server on the company network has extremely high CPU utilization. Upon further inspection, the administrator sees that the server is consistently communicating with an IP address that is traced back to a company that awards digital currency for solving hash algorithms. Which of the following was MOST likely used to compromise the server?",
            "options": [
                "Keylogger",
                "Ransomware",
                "Boot sector virus",
                "Cryptomining malware"
            ],
            "correct_answer": 4,
            "description": "The correct answer is cryptomining malware. This type of malware utilizes system resources to mine cryptocurrency, which would explain the high CPU utilization observed. \n\n- A keylogger records user activity but does not cause high CPU usage. \n- Ransomware typically encrypts files rather than directly using CPU resources for mining. \n- A boot sector virus affects system startup but is not associated with continuous high CPU communication."
        },
        {
            "question": "A system dives nearly full, and a technician needs to free up some space. Which of the following tools should the technician use?",
            "options": [
                "Disk Cleanup",
                "Resource Monitor",
                "Disk Defragment",
                "Disk Management"
            ],
            "correct_answer": 1,
            "description": "The correct answer is Disk Cleanup. This tool helps remove unnecessary files, freeing up disk space efficiently. \n\n- Resource Monitor provides insights into system performance but does not directly free up space. \n- Disk Defragment reorganizes fragmented data but does not delete files to create space. \n- Disk Management is used for partitioning and formatting drives, not for cleaning up files."
        },
        {
            "question": "A technician is partitioning a hard disk. The five primary partitions should contain 4TB of free space. Which of the following partition styles should the technician use to partition the device?",
            "options": [
                "EFS",
                "GPT",
                "MBR",
                "FAT32"
            ],
            "correct_answer": 2,
            "description": "The correct answer is GPT (GUID Partition Table). GPT supports large disks over 2TB and allows for more than four primary partitions, making it suitable for the specified requirements. \n\n- EFS (Encrypting File System) is for file encryption, not partitioning. \n- MBR (Master Boot Record) is limited to 2TB and four primary partitions. \n- FAT32 is a file system, not a partition style."
        },
        {
            "question": "A developer receives the following error while trying to install virtualization software on a workstation: VTx not supported by system - Which of the following upgrades will MOST likely fix the issue?",
            "options": [
                "Processor",
                "Hard drive",
                "Memory",
                "Video card"
            ],
            "correct_answer": 1,
            "description": "The correct answer is the processor. The error indicates that the virtualization technology (VTx) is not enabled or supported by the current CPU, and upgrading to a compatible processor should resolve the issue. \n\n- A hard drive upgrade would not impact virtualization capabilities. \n- Memory is important for performance but does not affect VTx support. \n- A video card upgrade is unrelated to virtualization support."
        },
        {
            "question": "The screen on a user's mobile device is not autorotating even after the feature has been enabled and the device has been restarted. Which of the following should the technician do NEXT to troubleshoot the issue?",
            "options": [
                "Calibrate the phone sensors.",
                "Enable the touchscreen.",
                "Reinstall the operating system.",
                "Replace the screen."
            ],
            "correct_answer": 1,
            "description": "The correct answer is to calibrate the phone sensors. Sensor calibration can resolve issues with autorotation if the sensors are misreading orientation. \n\n- Enabling the touchscreen does not relate to autorotation functionality. \n- Reinstalling the operating system is a more drastic step and unlikely to be necessary. \n- Replacing the screen is unnecessary unless there is physical damage affecting sensor functionality."
        },
        {
            "question": "A technician received a call from a user who clicked on a web advertisement. Now, every time the user moves the mouse, a pop-up displays across the monitor. Which of the following procedures should the technician perform?",
            "options": [
                "Boot into safe mode.",
                "Perform a malware scan.",
                "Restart the machine.",
                "Reinstall the browser."
            ],
            "correct_answer": 2,
            "description": "The correct answer is to perform a malware scan. The pop-ups indicate potential malware infection, and a scan will help identify and remove it. \n\n- Booting into safe mode could be a troubleshooting step but is not the first action. \n- Restarting the machine might temporarily stop the pop-ups but will not address the root cause. \n- Reinstalling the browser may not be effective if malware is present on the system."
        },
        {
            "question": "A user’s permissions are limited to read on a shared network folder using NTFS security settings. Which of the following describes this type of security control?",
            "options": [
                "SMS",
                "MFA",
                "ACL",
                "MDM"
            ],
            "correct_answer": 3,
            "description": "The correct answer is ACL (Access Control List). ACLs define the permissions for users on files and folders, indicating that the user has read-only access to the shared network folder. \n\n- SMS (Short Message Service) is unrelated to security controls. \n- MFA (Multi-Factor Authentication) enhances security but does not specifically pertain to folder permissions. \n- MDM (Mobile Device Management) pertains to managing mobile devices rather than file permissions."
        },

#281-300


       {
        "question": "A user attempts to install additional software and receives a UAC prompt. Which of the following is the BEST way to resolve this issue?",
        "options": [
            "Add a user account to the local administrator's group.",
            "Configure Windows Defender Firewall to allow access to all networks.",
            "Create a Microsoft account.",
            "Disable the guest account."
        ],
        "correct_answer": 1,
        "description": "The correct answer is to add a user account to the local administrator's group. This will provide the necessary permissions for the user to install software without being prompted by UAC. \n\n- Configuring the firewall to allow access to all networks does not directly relate to installation permissions. \n- Creating a Microsoft account does not resolve UAC prompts and may not be necessary for local installations. \n- Disabling the guest account improves security but does not aid in software installation."
    },
    {
        "question": "A user is unable to access a web-based application. A technician verifies the computer cannot access any web pages at all. The computer obtains an IP address from the DHCP server. Then, the technician verifies the user can ping localhost, the gateway, and known IP addresses on the internet and receive a response. Which of the following is the MOST likely reason for the issue?",
        "options": [
            "A firewall is blocking the application.",
            "The wrong VLAN was assigned.",
            "The incorrect DNS address was assigned.",
            "The browser cache needs to be cleared."
        ],
        "correct_answer": 3,
        "description": "The correct answer is the incorrect DNS address was assigned. Since the user can ping known IP addresses but cannot access web pages, it's likely a DNS resolution issue. \n\n- A firewall blocking the application would prevent access to specific applications but not affect all web pages. \n- The wrong VLAN being assigned may limit network access but isn't a likely reason here since the user can ping local and external addresses. \n- Clearing the browser cache is a good troubleshooting step but unlikely to solve connectivity issues."
    },
    {
        "question": "A user is unable to access a website, which is widely used across the organization, and receives the following error message: The security certificate presented by this website has expired or is not yet valid. The technician confirms the website works when accessing it from another computer but not from the user's computer. Which of the following should the technician perform NEXT to troubleshoot the issue?",
        "options": [
            "Reboot the computer.",
            "Reinstall the OS.",
            "Configure a static IP.",
            "Check the computer's date and time."
        ],
        "correct_answer": 4,
        "description": "The correct answer is to check the computer's date and time. An incorrect system date or time can cause SSL certificate validation failures, resulting in the error message. \n\n- Rebooting the computer may help but is not a targeted solution to the problem. \n- Reinstalling the OS is unnecessary and too drastic. \n- Configuring a static IP does not relate to certificate errors and would not solve the issue."
    },
    {
        "question": "Every time a user tries to open the organization's proprietary application on an Android tablet, the application immediately closes. Other applications are operating normally. Which of the following troubleshooting actions would MOST likely resolve the issue? (Choose two.)",
        "options": [
            "Uninstalling the application.",
            "Gaining root access to the tablet.",
            "Resetting the web browser cache.",
            "Deleting the application cache.",
            "Clearing the application storage.",
            "Disabling mobile device management."
        ],
        "correct_answer": [4, 5],
        "description": "The correct answers are deleting the application cache and clearing the application storage. These actions can resolve issues caused by corrupted data or settings, which may be causing the app to crash. \n\n- Uninstalling the application would work but is not always necessary if data can be cleared. \n- Gaining root access can expose the device to risks and is not required for troubleshooting this issue. \n- Resetting the web browser cache does not affect the proprietary app, and disabling mobile device management could violate company policy."
    },
    {
        "question": "A technician needs to add an individual as a local administrator on a Windows home PC. Which of the following utilities would the technician MOST likely use?",
        "options": [
            "Settings > Personalization.",
            "Control Panel > Credential Manager.",
            "Settings > Accounts > Family and Other Users.",
            "Control Panel > Network and Sharing Center."
        ],
        "correct_answer": 3,
        "description": "The correct answer is Settings > Accounts > Family and Other Users. This section allows the technician to add or modify user accounts and assign administrative privileges. \n\n- Settings > Personalization focuses on display and theme settings, not user management. \n- Control Panel > Credential Manager is for managing credentials, not user accounts. \n- Control Panel > Network and Sharing Center is related to network settings and does not deal with user administration."
    },
    {
        "question": "A Windows administrator is creating user profiles that will include home directories and network printers for several new users. Which of the following is the MOST efficient way for the technician to complete this task?",
        "options": [
            "Access control.",
            "Authentication application.",
            "Group Policy.",
            "Folder redirection."
        ],
        "correct_answer": 3,
        "description": "The correct answer is Group Policy. This allows administrators to efficiently configure user profiles, including settings for home directories and network printers across multiple users. \n\n- Access control refers to permissions but does not manage profiles. \n- Authentication applications are not directly related to user profile creation. \n- Folder redirection is useful but typically operates within a Group Policy framework for broader management."
    },
    {
        "question": "A user's corporate laptop with proprietary work information was stolen from a coffee shop. The user logged in to the laptop with a simple password, and no other security mechanisms were in place. Which of the following would MOST likely prevent the stored data from being recovered?",
        "options": [
            "Biometrics.",
            "Full disk encryption.",
            "Enforced strong system password.",
            "Two-factor authentication."
        ],
        "correct_answer": 2,
        "description": "The correct answer is full disk encryption. This ensures that all data on the laptop is encrypted and inaccessible without the correct credentials, thus preventing recovery. \n\n- Biometrics would enhance security but is not a complete solution without encryption. \n- Enforced strong system passwords improve security but do not protect data at rest. \n- Two-factor authentication secures login access but does not protect stored data if the device is stolen."
    },
    {
        "question": "A technician is troubleshooting boot times for a user. The technician attempts to use MSConfig to see which programs are starting with the OS but receives a message that it can no longer be used to view startup items. Which of the following programs can the technician use to view startup items?",
        "options": [
            "msinfo32.",
            "perfmon.",
            "regedit.",
            "taskmgr."
        ],
        "correct_answer": 4,
        "description": "The correct answer is taskmgr. The Task Manager allows the technician to view and manage startup programs in the 'Startup' tab. \n\n- msinfo32 provides system information but does not show startup items. \n- perfmon is for performance monitoring and does not relate to startup management. \n- regedit allows access to the registry but is not a user-friendly method for managing startup items."
    },
    {
        "question": "A systems administrator is experiencing issues connecting from a laptop to the corporate network using PKI. Which of the following tools can the systems administrator use to help remediate the issue?",
        "options": [
            "certmgr.msc.",
            "mscontig.exe.",
            "lusrmgr.msc.",
            "perfmon.msc."
        ],
        "correct_answer": 1,
        "description": "The correct answer is certmgr.msc. This tool manages certificates and allows the administrator to check for issues with the PKI infrastructure. \n\n- mscontig.exe is for defragmentation and not relevant to PKI issues. \n- lusrmgr.msc manages user accounts and groups, which is not applicable here. \n- perfmon.msc monitors system performance and does not assist with certificate management."
    },
    {
        "question": "A large company is selecting a new Windows operating system and needs to ensure it has built-in encryption and endpoint protection. Which of the following Windows versions will MOST likely be selected?",
        "options": [
            "Home.",
            "Pro.",
            "Pro for Workstations.",
            "Enterprise."
        ],
        "correct_answer": 4,
        "description": "The correct answer is Enterprise. This version includes built-in encryption and advanced security features necessary for large organizations. \n\n- Home lacks many security features required for business environments. \n- Pro includes some security features but may not meet all enterprise-level requirements. \n- Pro for Workstations is optimized for high-performance tasks but may not include all necessary security capabilities."
    },




   
    {
        "question": "A technician is reimaging a desktop PC. The technician connects the PC to the network and powers it on. The technician attempts to boot the computer via the NIC to image the computer, but this method does not work. Which of the following is the MOST likely reason the computer is unable to boot into the imaging system via the network?",
        "options": [
            "The computer's CMOS battery failed.",
            "The computer's NIC is faulty.",
            "The PXE boot option has not been enabled.",
            "The Ethernet cable the technician is using to connect the desktop to the network is faulty."
        ],
        "correct_answer": 3,
        "description": "The correct answer is that the PXE boot option has not been enabled. Without enabling this option in the BIOS, the computer will not attempt to boot from the network. \n\n- A failed CMOS battery would typically lead to incorrect date/time settings rather than a failure to boot via NIC. \n- A faulty NIC would prevent any network connectivity, not just PXE booting. \n- A faulty Ethernet cable would likely result in no connection at all, not specifically in the PXE boot failure."
    },
    {
        "question": "Which of the following features allows a technician to configure policies in a Windows 10 Professional desktop?",
        "options": [
            "gpedit.",
            "gpmc.",
            "gpresult.",
            "gpupdate."
        ],
        "correct_answer": 1,
        "description": "The correct answer is gpedit. The Group Policy Editor allows technicians to configure local policies on a Windows 10 Professional desktop. \n\n- gpmc (Group Policy Management Console) is used in domain environments to manage policies across multiple machines. \n- gpresult provides information about the applied policies but does not allow for policy configuration. \n- gpupdate is used to refresh the applied policies but does not itself configure them."
    },
    {
        "question": "A technician is trying to encrypt a single folder on a PC. Which of the following should the technician use to accomplish this task?",
        "options": [
            "FAT32.",
            "exFAT.",
            "BitLocker.",
            "EFS."
        ],
        "correct_answer": 4,
        "description": "The correct answer is EFS (Encrypting File System). EFS allows users to encrypt individual files and folders on NTFS file systems. \n\n- FAT32 and exFAT do not support file encryption. \n- BitLocker is used for full disk encryption and cannot selectively encrypt individual folders."
    },
    {
        "question": "A small-office customer needs three PCs to be configured in a network with no server. Which of the following network types is the customer's BEST choice for this environment?",
        "options": [
            "Workgroup network.",
            "Public network.",
            "Wide area network.",
            "Domain network."
        ],
        "correct_answer": 1,
        "description": "The correct answer is a workgroup network. This allows multiple PCs to connect and share resources without the need for a central server, ideal for small offices. \n\n- A public network is not suitable for internal office use. \n- A wide area network typically refers to larger geographic connections and is not applicable here. \n- A domain network requires a server to manage user accounts and resources, which is not present in this scenario."
    },
    {
        "question": "Which of the following common security vulnerabilities can be mitigated by using input validation?",
        "options": [
            "Brute-force attack.",
            "Cross-site scripting.",
            "SQL injection.",
            "Cross-site request forgery."
        ],
        "correct_answer": 3,
        "description": "The correct answer is SQL injection. Input validation helps ensure that only expected data is processed, preventing SQL injection attacks. \n\n- Brute-force attacks exploit weak passwords, not input validation. \n- Cross-site scripting vulnerabilities arise from improper output handling rather than input validation. \n- Cross-site request forgery also relies on user actions rather than inputs to the application."
    },
    {
        "question": "A company is looking for a solution that provides a backup for all data on the system while providing the lowest impact to the network. Which of the following backup types will the company MOST likely select?",
        "options": [
            "Off-site.",
            "Synthetic.",
            "Full.",
            "Differential."
        ],
        "correct_answer": 2,
        "description": "The correct answer is synthetic backup. This type of backup integrates changes to backups without requiring extensive network resources during the backup process. \n\n- Off-site backups refer to the storage location rather than the impact on the network. \n- Full backups consume significant network bandwidth and time. \n- Differential backups require more resources than synthetic backups since they rely on the last full backup."
    },
    {
        "question": "A technician needs to establish a remote access session with a user who has a Windows workstation. The session must allow for simultaneous viewing of the workstation by both the user and technician. Which of the following remote access technologies should be used?",
        "options": [
            "RDP.",
            "VPN.",
            "SSH.",
            "MSRA."
        ],
        "correct_answer": 4,
        "description": "The correct answer is MSRA (Microsoft Remote Assistance). This allows both the technician and user to view and control the desktop simultaneously, enabling effective troubleshooting. \n\n- RDP (Remote Desktop Protocol) also supports simultaneous access but is typically used for remote control without user involvement. \n- VPN (Virtual Private Network) provides secure access to the network but does not facilitate desktop sharing. \n- SSH (Secure Shell) is primarily used for secure command-line access, not graphical interfaces."
    },
    {
        "question": "A user's iPhone was permanently locked after several failed login attempts. Which of the following will restore access to the device?",
        "options": [
            "Fingerprint and pattern.",
            "Facial recognition and PIN code.",
            "Primary account and password.",
            "Secondary account and recovery code."
        ],
        "correct_answer": 4,
        "description": "The correct answer is the secondary account and recovery code. This is often the method to regain access after being locked out due to failed attempts. \n\n- Fingerprint and pattern or facial recognition and PIN code would not work if the device is locked. \n- The primary account and password are not typically used to unlock the device after it is permanently locked."
    },
    {
        "question": "A remote user is having issues accessing an online share. Which of the following tools would MOST likely be used to troubleshoot the issue?",
        "options": [
            "Screen-sharing software.",
            "Secure shell.",
            "Virtual private network.",
            "File transfer software."
        ],
        "correct_answer": 1,
        "description": "The correct answer is screen-sharing software. This allows the technician to view the user's screen and understand the issue with accessing the online share. \n\n- Secure shell is primarily for command-line access and not for screen sharing. \n- Virtual private network is for secure connections but does not provide direct troubleshooting capabilities. \n- File transfer software is unrelated to troubleshooting access issues."
    },

#301-315


{
    "question": "A customer calls a service support center and begins yelling at a technician about a feature for a product that is not working to the customer's satisfaction. This feature is not supported by the service support center and requires a field technician to troubleshoot. The customer continues to demand service. Which of the following is the BEST course of action for the support center representative to take?",
    "options": [
        "Inform the customer that the issue is not within the scope of this department.",
        "Apologize to the customer and escalate the issue to a manager.",
        "Ask the customer to explain the issue and then try to fix it independently.",
        "Respond that the issue is something the customer should be able to fix."
    ],
    "correct_answer": 2,
    "description": "The correct answer is to apologize to the customer and escalate the issue to a manager. This approach shows empathy and acknowledges the customer's frustration while directing them to the appropriate resource for resolution. \n\n- Informing the customer that the issue is not within the scope of this department may seem dismissive and could further frustrate them. \n- Asking the customer to explain the issue and trying to fix it independently may lead to wasted time and resources since a field technician is needed. \n- Responding that the customer should be able to fix it does not address their concern and could escalate the situation."
},
    {
        "question": "A user reported that a laptop's screen turns off very quickly after sitting for a few moments and is also very dim when not plugged in to an outlet. Everything else seems to be functioning normally. Which of the following Windows settings should be configured?",
        "options": [
            "Power Plans",
            "Hibernate",
            "Sleep/Suspend",
            "Screensaver"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Power Plans. Adjusting power plans allows the user to modify settings related to screen timeout and brightness when unplugged. \n\n- Hibernate is for saving the current session to disk, which does not directly affect screen dimming. \n- Sleep/Suspend settings control whether the computer enters low power mode but do not specifically address screen brightness. \n- Screensaver settings are unrelated to the functionality of screen timeout or brightness adjustment."
    },
    {
        "question": "A user is receiving repeated pop-up advertising messages while browsing the internet. A malware scan is unable to locate the source of an infection. Which of the following should the technician check NEXT?",
        "options": [
            "Windows updates",
            "DNS settings",
            "Certificate store",
            "Browser plug-ins"
        ],
        "correct_answer": 4,
        "description": "The correct answer is browser plug-ins. Unwanted advertising pop-ups are often caused by malicious browser plug-ins that can evade standard malware scans. \n\n- Windows updates are important for security but are unlikely to resolve this specific issue. \n- DNS settings may affect web access but are not typically linked to pop-up ads. \n- The certificate store is related to secure connections and is not relevant to advertising pop-ups."
    },
    {
        "question": "The courts determined that a cybercrimes case could no longer be prosecuted due to the agency’s handling of evidence. Which of the following was MOST likely violated during the investigation?",
        "options": [
            "Open-source software",
            "EULA",
            "Chain of custody",
            "AUP"
        ],
        "correct_answer": 3,
        "description": "The correct answer is chain of custody. Proper handling of evidence is crucial in legal cases, and a breach in the chain of custody can compromise the case. \n\n- Open-source software and EULA relate to software licensing but not evidence handling. \n- AUP (Acceptable Use Policy) deals with acceptable use of organizational resources but does not directly impact legal proceedings."
    },
    {
        "question": "A user reports a virus is on a PC. The user installs additional real-time protection antivirus software, and the PC begins performing extremely slow. Which of the following steps should the technician take to resolve the issue?",
        "options": [
            "Uninstall one antivirus software program and install a different one.",
            "Launch Windows Update, and then download and install OS updates.",
            "Activate real-time protection on both antivirus software programs.",
            "Enable the quarantine feature on both antivirus software programs.",
            "Remove the user-installed antivirus software program."
        ],
        "correct_answer": 5,
        "description": "The correct answer is to remove the user-installed antivirus software program. Running multiple real-time protection programs can cause performance issues and conflicts. \n\n- Uninstalling and installing a different program won't solve the problem if two are running simultaneously. \n- Launching Windows Update may improve performance but is not the direct cause of the slow response. \n- Activating real-time protection on both programs will only worsen the performance issue. \n- Enabling the quarantine feature on both programs doesn't address the underlying conflict."
    },
    {
        "question": "A technician removed a virus from a user's device. The user returned the device a week later with the same virus on it. Which of the following should the technician do to prevent future infections?",
        "options": [
            "Disable System Restore.",
            "Educate the end user.",
            "Install the latest OS patches.",
            "Clean the environment preinstallation."
        ],
        "correct_answer": 2,
        "description": "The correct answer is to educate the end user. Educating users about safe browsing habits and recognizing phishing attempts can help prevent future infections. \n\n- Disabling System Restore is not advisable, as it may prevent recovery options in case of future issues. \n- Installing OS patches is important for security, but user behavior is a significant factor in preventing infections. \n- Cleaning the environment preinstallation may help but is not a direct solution to user behavior issues."
    },
    {
        "question": "A technician is concerned about a large increase in the number of whaling attacks happening in the industry. The technician wants to limit the company’s risk to avoid any issues. Which of the following items should the technician implement?",
        "options": [
            "Screened subnet",
            "Firewall",
            "Anti-phishing training",
            "Antivirus"
        ],
        "correct_answer": 3,
        "description": "The correct answer is anti-phishing training. Educating employees about whaling attacks can help them recognize and avoid these targeted scams. \n\n- A screened subnet and firewall can provide some protection but do not address user awareness. \n- Antivirus software is useful for detecting known threats but is not effective against sophisticated whaling attempts that often rely on social engineering."
    },
    {
        "question": "A customer calls the help desk asking for instructions on how to modify desktop wallpaper. Which of the following Windows 10 settings should the technician recommend?",
        "options": [
            "Personalization",
            "Apps",
            "Updates",
            "Display"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Personalization. This setting allows users to change the desktop wallpaper and other appearance settings. \n\n- Apps relate to software management, not personalization settings. \n- Updates manage system updates and do not pertain to wallpaper changes. \n- Display settings may affect screen resolution but do not specifically provide options for wallpaper."
    },
{
    "question": "A user calls the help desk and reports a workstation is infected with malicious software. Which of the following tools should the help desk technician use to remove the malicious software? (Choose two.)",
    "options": [
        "Local Network Connection",
        "User Account Control",
        "Windows Backup and Restore",
        "Windows Firewall",
        "Windows Defender",
        "Network Packet Analyzer"
    ],
    "correct_answer": [5, 6],
    "description": "The correct answers are Windows Defender and Network Packet Analyzer. Windows Defender is built-in antivirus software that can effectively remove malware. \n\n- Local Network Connection, User Account Control, and Windows Firewall do not directly address malware removal. \n- Windows Backup and Restore are for data recovery, not malware removal. A Network Packet Analyzer can help identify malicious traffic or behavior, aiding in further investigation."
},
    {
        "question": "A systems administrator is monitoring an unusual amount of network traffic from a kiosk machine and needs to investigate to determine the source of the traffic. Which of the following tools can the administrator use to view which processes on the kiosk machine are connecting to the internet?",
        "options": [
            "Resource Monitor",
            "Performance Monitor",
            "Command Prompt",
            "System Information"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Resource Monitor. This tool allows the administrator to view active network connections and which processes are using the network. \n\n- Performance Monitor is used for tracking system performance metrics but does not provide detailed information on network connections. \n- Command Prompt can be used for some network commands, but Resource Monitor provides a more user-friendly interface. \n- System Information gives an overview of system specs but does not monitor active processes."
    },
    {
        "question": "Which of the following protects a mobile device against unwanted access when it is left unattended?",
        "options": [
            "PIN code",
            "OS updates",
            "Antivirus software",
            "BYOD policy"
        ],
        "correct_answer": 1,
        "description": "The correct answer is PIN code. A PIN code secures the device and prevents unauthorized access when the device is unattended. \n\n- OS updates are crucial for security but do not directly prevent access when the device is left alone. \n- Antivirus software helps protect against malicious software but does not secure the device when unattended. \n- A BYOD policy outlines acceptable use but does not provide direct protection against unauthorized access."
    },
    {
        "question": "A systems administrator installed the latest Windows security patch and received numerous tickets reporting slow performance the next day. Which of the following should the administrator do to resolve this issue?",
        "options": [
            "Rebuild user profiles.",
            "Roll back the updates.",
            "Restart the services.",
            "Perform a system file check."
        ],
        "correct_answer": 2,
        "description": "The correct answer is to roll back the updates. If a security patch is causing performance issues, rolling it back can restore normal functionality. \n\n- Rebuilding user profiles may address user-specific issues but does not tackle the patch's impact. \n- Restarting services may help but is unlikely to resolve issues caused by the update. \n- Performing a system file check can identify corrupted files but may not directly relate to the slow performance."
    },
    {
        "question": "A corporation purchased new computers for a school. The computers are the same make and model and need to have the standard image loaded. Which of the following orchestration tools should a desktop administrator use for wide-scale deployment?",
        "options": [
            "USB drive",
            "DVD installation media",
            "PXE boot",
            "Recovery partition"
        ],
        "correct_answer": 3,
        "description": "The correct answer is PXE boot. PXE boot allows for network-based deployment of images, making it efficient for deploying to multiple computers simultaneously. \n\n- USB drives and DVD installation media are limited to one computer at a time and require manual intervention. \n- A recovery partition is useful for restoring individual computers but is not practical for wide-scale deployment."
    },
{
    "question": "A Windows user recently replaced a computer. The user can access the public internet on the computer; however, an internal site at https://companyintranet.com:8888 is no longer loading. Which of the following should a technician adjust to resolve the issue?",
    "options": [
        "Default gateway settings",
        "DHCP settings",
        "IP address settings",
        "Firewall settings",
        "Antivirus settings"
    ],
    "correct_answer": 4,
    "description": "The correct answer is firewall settings. The inability to access an internal site may indicate that the firewall is blocking the connection to the specific internal resource. \n\n- Default gateway settings are important for routing traffic, but since the public internet is accessible, the gateway is likely not the issue. \n- DHCP settings manage IP address allocation but do not typically affect access to specific sites. \n- IP address settings may impact connectivity, but the firewall is the most probable cause in this scenario. \n- Antivirus settings could interfere with connections, but the firewall is a more common issue when internal sites are inaccessible."
},
    {
        "question": "Which of the following refers to the steps to be taken if an issue occurs during a change implementation?",
        "options": [
            "Testing",
            "Rollback",
            "Risk",
            "Acceptance"
        ],
        "correct_answer": 2,
        "description": "The correct answer is rollback. Rollback procedures define how to revert changes if an implementation fails or causes issues. \n\n- Testing refers to the process of evaluating changes before implementation. \n- Risk involves assessing potential problems but does not provide a direct action plan for dealing with issues. \n- Acceptance is about agreeing to changes but does not specify actions to take if problems arise."
    },

#316-330

    {
        "question": "A company would like to implement multifactor authentication for all employees at a minimal cost. Which of the following best meets the company's requirements?",
        "options": [
            "Biometrics",
            "Soft token",
            "Access control lists",
            "Smart card"
        ],
        "correct_answer": 2,
        "description": "The correct answer is soft token. Soft tokens are cost-effective solutions that generate time-based one-time passwords (TOTPs) for multifactor authentication without the need for expensive hardware. \n\n- Biometrics can be costly due to the need for specialized hardware. \n- Access control lists manage permissions but do not provide multifactor authentication. \n- Smart cards require physical cards and card readers, making them more expensive than soft tokens."
    },
    {
        "question": "A help desk technician determines a motherboard has failed. Which of the following is the most logical next step in the remediation process?",
        "options": [
            "Escalating the issue to Tier 2",
            "Verifying warranty status with the vendor",
            "Replacing the motherboard",
            "Purchasing another PC"
        ],
        "correct_answer": 2,
        "description": "The correct answer is verifying warranty status with the vendor. Before proceeding with repairs or replacements, it is crucial to determine if the motherboard is still under warranty to avoid unnecessary costs. \n\n- Escalating to Tier 2 may not be necessary if the technician has already diagnosed the issue. \n- Replacing the motherboard without checking warranty status can lead to added expenses. \n- Purchasing another PC is an extreme measure when warranty support may be available."
    },
    {
        "question": "A user added a second monitor and wants to extend the display to it. In which of the following Windows settings will the user most likely be able to make this change?",
        "options": [
            "System",
            "Devices",
            "Personalization",
            "Accessibility"
        ],
        "correct_answer": 3,
        "description": "The correct answer is Personalization. This section in Windows allows users to manage display settings, including extending displays across multiple monitors. \n\n- The System settings are more general and do not focus on display configurations. \n- Devices settings pertain to adding and managing hardware but not display settings. \n- Accessibility options focus on features for users with disabilities rather than monitor configurations."
    },
    {
        "question": "A systems administrator is configuring centralized desktop management for computers on a domain. The management team has decided that all users' workstations should have the same network drives, printers, and configurations. Which of the following should the administrator use to accomplish this task?",
        "options": [
            "Network and Sharing Center",
            "net use",
            "User Accounts",
            "regedit",
            "Group Policy"
        ],
        "correct_answer": 5,
        "description": "The correct answer is Group Policy. This tool allows administrators to enforce settings across multiple computers on a domain, ensuring consistency in network drives, printers, and configurations. \n\n- Network and Sharing Center is used for managing network connections but lacks centralized control features. \n- net use is a command-line utility for mapping network drives, not for centralized management. \n- User Accounts manage user settings but do not configure network resources. \n- regedit allows changes to the Windows Registry but is not suitable for managing multiple machines effectively."
    },
    {
        "question": "A user connected an external hard drive but is unable to see it as a destination to save files. Which of the following tools will allow the drive to be formatted?",
        "options": [
            "Disk Management",
            "Device Manager",
            "Disk Cleanup",
            "Disk Defragmenter"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Disk Management. This tool is used to manage disk drives and partitions, including formatting unrecognized drives. \n\n- Device Manager is for managing hardware devices but does not format disks. \n- Disk Cleanup removes unnecessary files but does not format disks. \n- Disk Defragmenter reorganizes data on existing drives but does not perform formatting operations."
    },
    {
        "question": "Which of the following best describes when to use the YUM command in Linux?",
        "options": [
            "To add functionality",
            "To change folder permissions",
            "To show documentation",
            "To list file contents"
        ],
        "correct_answer": 1,
        "description": "The correct answer is to add functionality. YUM (Yellowdog Updater Modified) is a package manager for Linux that simplifies the installation, updating, and removal of software packages. \n\n- Changing folder permissions is done with the chmod command, not YUM. \n- Showing documentation can be accomplished with the man command. \n- Listing file contents is done using commands like ls, not YUM."
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
        "description": "The correct answer is proper ventilation. Adequate airflow helps prevent overheating, which can significantly extend the life of electronic devices. \n\n- Battery backup protects against power surges but does not directly extend device lifespan. \n- Electrostatic discharge mats help prevent damage during handling, but they are not a maintenance solution. \n- Green disposal pertains to environmentally responsible methods of disposing of electronic waste."
    },
    {
        "question": "While trying to repair a Windows 10 OS, a technician receives a prompt asking for a key. The technician tries the administrator password, but it is rejected. Which of the following does the technician need in order to continue the OS repair?",
        "options": [
            "SSL key",
            "Preshared key",
            "WPA2 key",
            "Recovery key"
        ],
        "correct_answer": 4,
        "description": "The correct answer is recovery key. This key is required to access encrypted drives or to continue repair processes if a prompt specifically requests it. \n\n- An SSL key is used for secure web communications, not OS repair. \n- Preshared keys are used in network security, not for OS repairs. \n- WPA2 keys are related to wireless network security."
    },
    {
        "question": "Which of the following allows access to the command line in macOS?",
        "options": [
            "PsExec",
            "command.com",
            "Terminal",
            "CMD"
        ],
        "correct_answer": 3,
        "description": "The correct answer is Terminal. Terminal is the macOS application that provides a command-line interface for users to interact with the system. \n\n- PsExec is a Windows tool for executing processes on remote systems, not available on macOS. \n- command.com is a command-line interpreter for DOS, not used in macOS. \n- CMD is the command prompt in Windows, not applicable to macOS."
    },
    {
        "question": "A technician sees a file that is requesting payment to a cryptocurrency address. Which of the following should the technician do first?",
        "options": [
            "Quarantine the computer.",
            "Disable System Restore.",
            "Update the antivirus software definitions.",
            "Boot to safe mode."
        ],
        "correct_answer": 1,
        "description": "The correct answer is to quarantine the computer. This step isolates the affected system to prevent further spread of potential malware. \n\n- Disabling System Restore may not be necessary initially and could hinder recovery options. \n- Updating antivirus definitions is important but should follow isolation to prevent further harm. \n- Booting to safe mode is a potential step, but isolation should be prioritized first."
    },
    {
        "question": "A user contacts the help desk to request assistance with a program feature. The user is in a different building but on the same network as the help desk technician. Which of the following should the technician use to assist the user?",
        "options": [
            "AAA",
            "SSH",
            "RDP",
            "VPN"
        ],
        "correct_answer": 3,
        "description": "The correct answer is RDP (Remote Desktop Protocol). This allows the technician to remotely access the user's desktop to assist with the program feature. \n\n- AAA refers to authentication, authorization, and accounting and is not a tool for remote support. \n- SSH is a secure shell for command-line access but not suitable for graphical user interface support. \n- VPN provides secure remote access to the network but does not allow direct assistance with a user's desktop."
    },
    {
        "question": "An engineer is configuring a new server that requires a bare-metal installation. Which of the following installation methods should the engineer use if installation media is not available on site?",
        "options": [
            "Image deployment",
            "Recovery partition Installation",
            "Remote network installation",
            "Repair installation"
        ],
        "correct_answer": 3,
        "description": "The correct answer is remote network installation. This method allows the installation of an operating system over the network without local media. \n\n- Image deployment requires pre-made installation images, which are not available in this scenario. \n- Recovery partition installation is contingent on having access to recovery media on the server itself. \n- Repair installation is intended for fixing existing installations, not for new setups."
    },
    {
        "question": "A company is experiencing a DDoS attack. Several internal workstations are the source of the traffic. Which of the following types of infections are the workstations most likely experiencing? (Choose two.)",
        "options": [
            "Zombies",
            "Keylogger",
            "Adware",
            "Botnet",
            "Ransomware",
            "Spyware"
        ],
        "correct_answer": [1, 4],
        "description": "The correct answers are zombies and botnet. Zombie computers are part of a botnet and are often used to carry out DDoS attacks by overwhelming targeted services with traffic. \n\n- Keyloggers and spyware focus on capturing user data and activity rather than participating in attacks. \n- Adware typically shows ads and does not contribute to DDoS activities. \n- Ransomware encrypts files for ransom and is unrelated to DDoS attacks."
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
        "description": "The correct answer is Disk Defragment. Defragmenting the hard drive can improve access times and overall performance for older HDDs, especially if files are fragmented. \n\n- Disk Management is used for partition management but does not improve performance. \n- Disk Cleanup removes temporary files but may not address the underlying performance issues. \n- Device Manager manages hardware but does not affect disk performance directly."
    },
    {
        "question": "An employee calls the help desk regarding an issue with a laptop PC. After a Windows update, the user can no longer use certain locally attached devices, and a reboot has not fixed the issue. Which of the following should the technician perform to fix the issue?",
        "options": [
            "Disable the Windows Update service.",
            "Check for updates.",
            "Restore hidden updates.",
            "Roll back updates."
        ],
        "correct_answer": 4,
        "description": "The correct answer is roll back updates. This step restores the system to a previous state before the problematic update, potentially fixing the issue with locally attached devices. \n\n- Disabling the Windows Update service is not a viable solution for resolving issues caused by specific updates. \n- Checking for updates may not address the current issue. \n- Restoring hidden updates does not resolve the problem if the current update is already causing issues."
    },

#331-350

 {
        "question": "A technician needs to transfer a file to a user's workstation. Which of the following would best accomplish this task utilizing the workstation's built-in protocols?",
        "options": [
            "VPN",
            "SMB",
            "RMM",
            "MSRA"
        ],
        "correct_answer": 2,
        "description": "The correct answer is SMB (Server Message Block). SMB is a network protocol used for file sharing and allows for easy transfer of files between devices on the same network. \n\n- VPN (Virtual Private Network) is primarily used for secure remote access, not direct file transfer. \n- RMM (Remote Monitoring and Management) tools typically manage devices remotely rather than transferring files. \n- MSRA (Microsoft Remote Assistance) allows users to share their screen but is not designed specifically for file transfers."
    },
    {
        "question": "Which of the following is most likely used to run .vbs files on Windows devices?",
        "options": [
            "winmgmt.exe",
            "powershell.exe",
            "cscript.exe",
            "explorer.exe"
        ],
        "correct_answer": 3,
        "description": "The correct answer is cscript.exe. This command-line utility is specifically designed to execute VBScript files (.vbs) in Windows. \n\n- winmgmt.exe is related to Windows Management Instrumentation (WMI), not for running scripts. \n- powershell.exe is a more advanced scripting environment but is not specifically for .vbs files. \n- explorer.exe is the Windows file explorer and does not execute scripts."
    },
    {
        "question": "A technician wants to install Developer Mode on a Windows laptop but is receiving a “failed to install package” message. Which of the following should the technician do first?",
        "options": [
            "Ensure internet connectivity.",
            "Check for Windows updates.",
            "Enable SSH.",
            "Reboot computer."
        ],
        "correct_answer": 1,
        "description": "The correct answer is ensure internet connectivity. Internet access is crucial for downloading packages and updates, and a lack of connectivity can lead to installation failures. \n\n- Checking for Windows updates can be important, but it may not address immediate connectivity issues. \n- Enabling SSH is irrelevant in this context as it is not related to installing Developer Mode. \n- Rebooting the computer may help but does not address the core issue of connectivity."
    },
    {
        "question": "A PC is taking a long time to boot. Which of the following operations would be best to do to resolve the issue at a minimal expense? (Choose two.)",
        "options": [
            "Installing additional RAM",
            "Removing the applications from startup",
            "Installing a faster SSD",
            "Running the Disk Cleanup utility",
            "Defragmenting the hard drive",
            "Ending the processes in the Task Manager"
        ],
        "correct_answer": [2, 5],
        "description": "The correct answers are removing the applications from startup and defragmenting the hard drive. \n\n- Removing startup applications can significantly decrease boot time by limiting the number of programs that load at startup. \n- Defragmenting the hard drive can improve file access speeds, especially for older HDDs. \n\n- Installing additional RAM and a faster SSD would improve performance but involve higher costs. \n- Running Disk Cleanup can help but is less effective for boot times than the other two options. \n- Ending processes in the Task Manager is a temporary fix and may not resolve boot issues."
    },
    {
        "question": "A technician installs specialized software on a workstation. The technician then attempts to run the software. The workstation displays a message indicating the software is not authorized to run. Which of the following should the technician do to most likely resolve the issue?",
        "options": [
            "Install the software in safe mode.",
            "Attach the external hardware token.",
            "Install OS updates.",
            "Restart the workstation after installation"
        ],
        "correct_answer": 2,
        "description": "The correct answer is to attach the external hardware token. Some specialized software requires hardware authentication to function properly, which could lead to the authorization error if not present. \n\n- Installing in safe mode may bypass certain restrictions but is not a guaranteed fix for authorization issues. \n- Installing OS updates could improve compatibility but is not directly related to the authorization problem. \n- Restarting the workstation may help, but it is unlikely to resolve the authorization issue without the proper token."
    },
    {
        "question": "Which of the following would most likely be used in a small office environment?",
        "options": [
            "Print server",
            "Virtualization",
            "Domain access",
            "Workgroup"
        ],
        "correct_answer": 4,
        "description": "The correct answer is workgroup. Workgroups are simpler and easier to manage in small office environments, allowing devices to connect and share resources without the complexity of a server-based domain. \n\n- Print servers can be used but typically in larger setups where multiple printers are centralized. \n- Virtualization is more common in larger or enterprise environments due to resource demands. \n- Domain access is suitable for larger organizations needing centralized control and management."
    },
    {
        "question": "When trying to access a secure internal network, the user receives an error messaging stating, \"There is a problem with this website's security certificate.\" The user reboots the desktop and tries to access the website again, but the issue persists. Which of the following should the user do to prevent this error from reoccurring?",
        "options": [
            "Reimage the system and install SSL.",
            "Install Trusted Root Certificate",
            "Select View Certificates and then Install Certificate.",
            "Continue to access the website."
        ],
        "correct_answer": 2,
        "description": "The correct answer is to install Trusted Root Certificate. This action ensures that the system recognizes the certificate authority and can validate the security certificates used by the website, preventing future errors. \n\n- Reimaging the system is unnecessary and overly drastic for this issue. \n- Selecting View Certificates may provide insights but does not directly resolve the problem. \n- Continuing to access the website may expose the user to security risks."
    },
  {
    "question": "A department manager submits a help desk ticket to request the migration of a printer's port utilization from USB to Ethernet so multiple users can access the printer. This will be a new network printer; thus, a new IP address allocation is required. Which of the following should happen immediately before network use is authorized?",
    "options": [
        "Document the date and time of the change.",
        "Submit a change request form.",
        "Determine the risk level of this change.",
        "Request an unused IP address."
    ],
    "correct_answer": 3,
    "description": "The correct answer is to determine the risk level of this change. Understanding the risk associated with migrating the printer's port utilization is crucial to ensure that potential issues are identified and mitigated before the change is authorized. \n\n- Submitting a change request form is also necessary, but assessing the risk should come first to guide the decision-making process. \n- Documenting the date and time is important for record-keeping but is not the priority before authorization. \n- Requesting an unused IP address will follow after the risk assessment and change approval."
  },
    {
        "question": "An IT security team is implementing a new Group Policy that will return a computer to the log-in after three minutes. Which of the following best describes the change in policy?",
        "options": [
            "Log-in times",
            "Screen lock",
            "User permission",
            "Log-in lockout attempts"
        ],
        "correct_answer": 2,
        "description": "The correct answer is screen lock. This policy configuration is designed to automatically lock the computer after a period of inactivity, requiring the user to log back in. \n\n- Log-in times refer to the duration of user sessions, not inactivity. \n- User permission deals with access rights and not session management. \n- Log-in lockout attempts relate to failed log-in attempts rather than inactivity."
    },
  {
    "question": "A company recently experienced a security incident in which a USB drive containing malicious software was able to covertly install malware on a workstation. Which of the following actions should be taken to prevent this incident from happening again? (Choose two.)",
    "options": [
        "Install a host-based IDS.",
        "Restrict log-in times.",
        "Enable a BIOS password.",
        "Update the password complexity.",
        "Disable AutoRun.",
        "Update the antivirus definitions.",
        "Restrict user permissions."
    ],
    "correct_answer": [5, 7],
    "description": "The correct answers are disable AutoRun and restrict user permissions. \n\n- Disabling AutoRun prevents USB drives from executing files automatically, significantly reducing the risk of malware installation. \n- Restricting user permissions limits access to potentially harmful actions and resources, providing an additional layer of security against unauthorized software execution. \n\n- While installing a host-based IDS can enhance security, it is not as immediate a preventive measure against USB threats as the other two options. \n- Other options, such as updating antivirus definitions and enabling a BIOS password, also contribute to security but do not directly prevent USB malware execution."
  },
  {
    "question": "A hard drive that previously contained PII needs to be repurposed for a public access workstation. Which of the following data destruction methods should a technician use to ensure data is completely removed from the hard drive?",
    "options": [
        "Shredding",
        "Degaussing",
        "Low-level formatting",
        "Recycling"
    ],
    "correct_answer": 2,
    "description": "The correct answer is degaussing. This method effectively destroys all data on the hard drive by disrupting the magnetic fields used to store information, ensuring that any PII is irretrievable. \n\n- Shredding refers to physically destroying the drive, which is effective but may not always be feasible for repurposing. \n- Low-level formatting can make data harder to recover but does not guarantee complete destruction. \n- Recycling does not destroy data and poses a risk of data exposure."
},

{
    "question": "A technician receives a help desk ticket from a user who is unable to update a phone. The technician investigates the issue and notices the following error message: Insufficient storage space. While analyzing the phone, the technician does not discover any third-party applications or photos. Which of the following is the best way to resolve the issue?",
    "options": [
        "Exchange the device for a newer one.",
        "Upgrade the onboard storage.",
        "Allocate more space by removing factory applications.",
        "Move factory applications to external memory."
    ],
    "correct_answer": 3,
    "description": "The correct answer is to allocate more space by removing factory applications. Many phones come with pre-installed applications that can be safely removed to free up space. \n\n- Upgrading onboard storage may not be possible for all devices, especially if they are not designed for expansion. \n- Moving factory applications to external memory might not be supported by all operating systems. \n- Exchanging the device is unnecessary if the issue can be resolved by managing storage."
},

{
    "question": "During an enterprise rollout of a new application, a technician needs to validate compliance with an application’s EULA while also reducing the number of licenses to manage. Which of the following licenses would best accomplish this goal?",
    "options": [
        "Personal use license",
        "Corporate use license",
        "Open-source license",
        "Non-expiring license"
    ],
    "correct_answer": 2,
    "description": "The correct answer is corporate use license. This license allows for multiple users within an organization to utilize the software while ensuring compliance with the EULA, simplifying license management. \n\n- Personal use licenses are typically restrictive and do not cover corporate use. \n- Open-source licenses allow free use but may not provide the same support or compliance assurances. \n- Non-expiring licenses do not necessarily reduce the number of licenses needed to manage."
},

{
    "question": "An administrator is designing and implementing a server backup system that minimizes the capacity of storage used. Which of the following is the best backup approach to use in conjunction with synthetic full backups?",
    "options": [
        "Differential",
        "Open file",
        "Archive",
        "Incremental"
    ],
    "correct_answer": 4,
    "description": "The correct answer is incremental. Incremental backups only save changes made since the last backup, minimizing storage usage when used alongside synthetic full backups. \n\n- Differential backups save changes since the last full backup, which can use more space over time. \n- Open file backups refer to files that are currently in use, not a specific strategy for storage management. \n- Archive backups typically retain data longer but do not focus on minimizing capacity."
},

{
    "question": "A developer's Type 2 hypervisor is performing inadequately when compiling new source code. Which of the following components should the developer upgrade to improve the hypervisor's performance?",
    "options": [
        "Amount of system RAM",
        "NIC performance",
        "Storage IOPS",
        "Dedicated GPU"
    ],
    "correct_answer": 1,
    "description": "The correct answer is amount of system RAM. Increasing RAM can enhance the performance of a Type 2 hypervisor by allowing more memory for the virtual machines, which is crucial for resource-intensive tasks like compiling source code. \n\n- While NIC performance and storage IOPS are important, they have less impact on the overall performance of the hypervisor compared to RAM. \n- A dedicated GPU may not significantly affect the performance of a Type 2 hypervisor unless graphical processing is a bottleneck, which is less common in source code compilation."
},

{
    "question": "A change advisory board authorized a setting change so a technician is permitted to implement the change. The technician successfully implemented the change. Which of the following should be done next?",
    "options": [
        "Document the date and time of change.",
        "Document the purpose of the change.",
        "Document the risk level.",
        "Document the findings of the sandbox test."
    ],
    "correct_answer": 1,
    "description": "The correct answer is to document the date and time of change. This documentation is essential for tracking changes and their effects, helping in future audits and troubleshooting. \n\n- While documenting the purpose and risk level is important, the immediate priority is to establish when the change occurred. \n- Documenting findings from the sandbox test is useful but typically happens before implementation."
},

{
    "question": "A user's corporate phone was stolen, and the device contains company trade secrets. Which of the following technologies should be implemented to mitigate this risk? (Choose two.)",
    "options": [
        "Remote wipe",
        "Firewall",
        "Device encryption",
        "Remote backup",
        "Antivirus",
        "Global Positioning System"
    ],
    "correct_answer": [1, 3],
    "description": "The correct answers are remote wipe and device encryption. Remote wipe allows for the erasure of sensitive data from a stolen device, while device encryption protects data at rest, making it unreadable without proper authorization. \n\n- A firewall is more effective for network security than device-specific data protection. \n- Remote backup and antivirus software are important for overall security but do not directly address the risk of stolen devices."
},

{
    "question": "A user visits a game vendor's website to view the latest patch notes, but this information is not available on the page. Which of the following should the user perform before reloading the page?",
    "options": [
        "Synchronize the browser data.",
        "Enable private browsing mode.",
        "Mark the site as trusted.",
        "Clear the cached file."
    ],
    "correct_answer": 4,
    "description": "The correct answer is to clear the cached file. This action can resolve issues with outdated or corrupted data being displayed on the webpage. \n\n- Synchronizing browser data does not affect the current page view. \n- Enabling private browsing mode will not help with loading the latest content. \n- Marking the site as trusted is a security measure but irrelevant to retrieving the patch notes."
},

{
    "question": "A user receives the following error while attempting to boot a computer: BOOTMGR is missing - Press Ctrl+Alt+Del to restart - Which of the following should a desktop engineer attempt first to address this issue?",
    "options": [
        "Repair Windows.",
        "Partition the hard disk.",
        "Reimage the workstation.",
        "Roll back the updates."
    ],
    "correct_answer": 1,
    "description": "The correct answer is to repair Windows. This option focuses on addressing the boot manager error directly, allowing the user to boot into the operating system without losing data. \n\n- Partitioning the hard disk may be necessary if there are underlying issues, but it's not the first step. \n- Reimaging the workstation is a more drastic measure that could result in data loss. \n- Rolling back updates may not be effective if the boot manager issue is unrelated to recent changes."
},

{
    "question": "A technician is working on a way to register all employee badges and associated computer IDs. Which of the following options should the technician use in order to achieve this objective?",
    "options": [
        "Database system",
        "Software management",
        "Active Directory description",
        "Infrastructure as a Service"
    ],
    "correct_answer": 1,
    "description": "The correct answer is a database system. A database is well-suited for storing, organizing, and managing employee badges and associated computer IDs, providing easy access and retrieval. \n\n- Software management focuses on managing applications and systems rather than specific data records. \n- Active Directory is used for managing user permissions and authentication, not specifically for tracking badges. \n- Infrastructure as a Service is a cloud computing model and does not directly apply to the task of registration."
},

#350-360


    {
    "question": "A technician successfully removed malicious software from an infected computer after running updates and scheduled scans to mitigate future risks. Which of the following should the technician do next?",
    "options": [
        "Educate the end user on best practices for security.",
        "Quarantine the host in the antivirus system.",
        "Investigate how the system was infected with malware.",
        "Create a system restore point."
    ],
    "correct_answer": 4,
    "description": "The correct answer is to create a system restore point. This action allows the technician to capture the current state of the system, ensuring that a stable version is available for recovery in case of future issues. \n\n- Educating the end user on best practices is important for long-term security, but creating a restore point addresses immediate system stability. \n- Quarantining the host is unnecessary since the malware has already been removed. \n- Investigating how the system was infected is relevant for understanding security weaknesses but does not provide immediate protection."
  },
    {
        "question": "An administrator responded to an incident where an employee copied financial data to a portable hard drive and then left the company with the data. The administrator documented the movement of the evidence. Which of the following concepts did the administrator demonstrate?",
        "options": [
            "Preserving chain of custody",
            "Implementing data protection policies",
            "Informing law enforcement",
            "Creating a summary of the incident"
        ],
        "correct_answer": 1,
        "description": "The correct answer is preserving chain of custody. This concept involves documenting the handling of evidence to ensure it is admissible in legal situations. \n\n- Implementing data protection policies is relevant but not specific to the handling of evidence. \n- Informing law enforcement may be necessary but is not directly related to documenting the evidence movement. \n- Creating a summary of the incident is useful but does not address the legal implications of evidence handling."
    },
    {
        "question": "A user requires a drive to be mapped through a Windows command line. Which of the following command-line tools can be utilized to map the drive?",
        "options": [
            "gpupdate",
            "net use",
            "hostname",
            "dir"
        ],
        "correct_answer": 2,
        "description": "The correct answer is net use. This command is specifically designed for mapping network drives in Windows. \n\n- gpupdate is used for updating Group Policy settings, not for mapping drives. \n- hostname displays the name of the computer and does not relate to drive mapping. \n- dir lists the contents of a directory, which is not relevant to mapping a drive."
    },
    {
        "question": "Users access files in the department share. When a user creates a new subfolder, only that user can access the folder and its files. Which of the following will MOST likely allow all users to access the new folders?",
        "options": [
            "Assigning share permissions",
            "Enabling inheritance",
            "Requiring multifactor authentication",
            "Removing archive attribute"
        ],
        "correct_answer": 2,
        "description": "The correct answer is enabling inheritance. This allows new subfolders to inherit the permissions of the parent folder, making them accessible to all users. \n\n- Assigning share permissions alone may not automatically apply to new folders. \n- Requiring multifactor authentication enhances security but does not affect folder access permissions. \n- Removing the archive attribute does not influence access rights."
    },
    {
        "question": "A computer technician is investigating a computer that is not booting. The user reports that the computer was working prior to shutting it down last night. The technician notices a removable USB device is inserted, and the user explains the device is a prize the user received in the mail yesterday. Which of the following types of attacks does this describe?",
        "options": [
            "Phishing",
            "Dumpster diving",
            "Tailgating",
            "Evil twin"
        ],
        "correct_answer": 1,
        "description": "The correct answer is phishing. The scenario suggests that the USB device may have been maliciously designed to compromise the system, potentially leading to data theft or malware installation. \n\n- Dumpster diving involves searching through trash for confidential information, not related to USB devices. \n- Tailgating refers to unauthorized access to a facility, and evil twin involves rogue Wi-Fi hotspots, neither of which are applicable here."
    },
    {
        "question": "A macOS user is installing a new application. Which of the following system directories is the software most likely to install by default?",
        "options": [
            "/etc/services",
            "/Applications",
            "/usr/bin",
            "C:\\Program Files"
        ],
        "correct_answer": 2,
        "description": "The correct answer is /Applications. This is the default directory for installed applications on macOS systems. \n\n- /etc/services is a configuration file directory, not for applications. \n- /usr/bin is for executable binaries but not where applications are installed. \n- C:\\Program Files is a Windows directory, not relevant for macOS."
    },
    {
        "question": "A customer is requesting help with a technical issue. Which of the following techniques should the technician use to properly evaluate and correct the customer concern?",
        "options": [
            "Have a videoconference using the customer’s personal phone so the customer can share the screen.",
            "Ask yes or no questions so that the answers are clear.",
            "Use open-ended questions to get additional information.",
            "Ask for the customer’s password so the issue can be resolved quickly and directly by the technician."
        ],
        "correct_answer": 3,
        "description": "The correct answer is to use open-ended questions to get additional information. This technique encourages the customer to provide more details, helping the technician understand the issue better. \n\n- Videoconferencing can be helpful but may not always be possible or practical. \n- Yes or no questions limit the responses and may not provide enough context. \n- Asking for passwords poses a security risk and is unnecessary for resolving most issues."
    },
    {
        "question": "A user is setting up backups on a workstation. The user wants to ensure that the restore process is as simple as possible. Which of the following backup types should the user select?",
        "options": [
            "Full",
            "Incremental",
            "Differential",
            "Synthetic"
        ],
        "correct_answer": 1,
        "description": "The correct answer is full. A full backup contains all the data and simplifies the restore process because the entire dataset is available in one backup. \n\n- Incremental backups require the last full backup plus all subsequent increments to restore, complicating the process. \n- Differential backups need the last full backup and the latest differential backup but can still be more complex than a full backup. \n- Synthetic backups involve multiple sources and can complicate the restore process."
    },
    {
        "question": "A user notices a small USB drive is attached to the user’s computer after a new vendor visited the office. The technician notices two files named grabber.exe and output.txt. Which of the following attacks is most likely occurring?",
        "options": [
            "Trojan",
            "Rootkit",
            "Cryptominer",
            "Keylogger"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Trojan. The file name grabber.exe suggests that it may be designed to extract data from the system, characteristic of a Trojan horse. \n\n- A rootkit is used to gain unauthorized access and remain undetected, but the context here suggests active data extraction. \n- A cryptominer is used to mine cryptocurrency and would typically be named differently. \n- A keylogger captures keystrokes and would not be indicated by these file names."
    },
    {
        "question": "Which of the following ls command options is used to display hidden files and directories?",
        "options": [
            "-a",
            "-s",
            "-lh",
            "-t"
        ],
        "correct_answer": 1,
        "description": "The correct answer is -a. This option displays all files, including hidden files and directories, which are typically prefixed with a dot (.). \n\n- -s shows the size of files, but not hidden files. \n- -lh lists files with details but does not include hidden ones unless -a is also specified. \n- -t sorts files by modification time, not related to visibility."
    },
#361-375

    {
        "question": "Which of the following social engineering tactics is best avoided by shredding sensitive documents?",
        "options": [
            "Dumpster diving",
            "Phishing",
            "Whaling",
            "Shoulder surfing"
        ],
        "correct_answer": 1,
        "description": "The correct answer is dumpster diving. Shredding sensitive documents helps prevent unauthorized individuals from retrieving confidential information discarded in the trash. \n\n- Phishing involves tricking users into giving away personal information and is not related to physical document disposal. \n- Whaling is a form of phishing targeting high-profile individuals and also does not relate to document handling. \n- Shoulder surfing is the act of watching someone enter confidential information and is not prevented by shredding documents."
    },
    {
        "question": "A user receives an error message from an online banking site that states the following: Your connection is not private. Authority invalid. Which of the following actions should the user take next?",
        "options": [
            "Proceed to the site.",
            "Use a different browser.",
            "Report the error to the bank.",
            "Reinstall the browser."
        ],
        "correct_answer": 3,
        "description": "The correct answer is to report the error to the bank. Reporting helps ensure the bank can investigate potential security issues with their website. \n\n- Proceeding to the site could expose the user to security risks. \n- Using a different browser might bypass the error but does not address the underlying security concern. \n- Reinstalling the browser is unnecessary and does not solve the issue of a potentially compromised connection."
    },
    {
        "question": "Which of the following filesystems replaced FAT as the preferred filesystem for Microsoft Windows OS?",
        "options": [
            "APFS",
            "FAT32",
            "NTFS",
            "ext4"
        ],
        "correct_answer": 3,
        "description": "The correct answer is NTFS. NTFS (New Technology File System) is the modern filesystem used by Windows, providing improved features such as better security and support for larger files. \n\n- APFS is primarily used by macOS and is not applicable to Windows. \n- FAT32 is an older filesystem that has limitations, particularly with file size and security features. \n- ext4 is commonly used in Linux environments and not for Windows."
    },
    {
        "question": "A user requires local administrative access to a workstation. Which of the following Control Panel utilities allows the technician to grant access to the user?",
        "options": [
            "System",
            "Network and Sharing Center",
            "User Accounts",
            "Security and Maintenance"
        ],
        "correct_answer": 3,
        "description": "The correct answer is User Accounts. This utility allows the technician to manage user accounts and assign administrative privileges. \n\n- The System utility deals with system settings and does not manage user permissions. \n- Network and Sharing Center is focused on network settings and does not provide user access controls. \n- Security and Maintenance is for system security settings but does not directly manage user account permissions."
    },
    {
        "question": "A systems administrator received a request to limit the amount of cellular data a user's Windows 10 tablet can utilize when traveling. Which of the following can the administrator do to best solve the user's issue?",
        "options": [
            "Turn on airplane mode.",
            "Set the connection to be metered.",
            "Configure the device to use a static IP address.",
            "Enable the Windows Defender Firewall."
        ],
        "correct_answer": 2,
        "description": "The correct answer is to set the connection to be metered. This setting limits data usage on Windows devices, helping to control cellular data consumption. \n\n- Turning on airplane mode would disable all wireless communications, not just limit data usage. \n- Configuring a static IP address does not impact data usage and is related to network configuration. \n- Enabling the Windows Defender Firewall enhances security but does not directly address data usage."
    },
    {
        "question": "Which of the following is used to ensure users have the appropriate level of access to perform their job functions?",
        "options": [
            "Access control list",
            "Multifactor authentication",
            "Least privilege",
            "Mobile device management"
        ],
        "correct_answer": 3,
        "description": "The correct answer is least privilege. The principle of least privilege ensures users have only the access necessary to perform their job functions, reducing security risks. \n\n- Access control lists (ACLs) define permissions but do not inherently enforce the principle of least privilege. \n- Multifactor authentication enhances security but does not dictate access levels. \n- Mobile device management pertains to managing devices rather than access permissions."
    },
    {
        "question": "A company implemented a BYOD policy and would like to reduce data disclosure caused by malware that may infect these devices. Which of the following should the company deploy to address these concerns?",
        "options": [
            "UAC",
            "MDM",
            "LDAP",
            "SSO"
        ],
        "correct_answer": 2,
        "description": "The correct answer is MDM (Mobile Device Management). MDM solutions help manage and secure mobile devices, ensuring compliance with company policies and minimizing risks from malware. \n\n- UAC (User Account Control) is a Windows security feature that manages user privileges but does not protect mobile devices. \n- LDAP (Lightweight Directory Access Protocol) is used for directory services and does not address malware concerns. \n- SSO (Single Sign-On) simplifies user authentication but does not provide malware protection."
    },
{
    "question": "Which of the following would allow physical access to a restricted area while maintaining a record of events?",
    "options": [
        "Hard token",
        "Access control vestibule",
        "Key fob",
        "Door Lock"
    ],
    "correct_answer": 3,
    "description": "The correct answer is key fob. Key fobs can be integrated with access control systems to grant entry while also maintaining logs of who accessed the restricted area, including timestamps for each entry and exit. \n\n- A hard token provides secure access but does not maintain a physical entry log. \n- An access control vestibule can log entries, but it typically requires additional hardware like key fobs or cards to function effectively. \n- A door lock secures access but does not inherently track entry."
},
    {
        "question": "Maintaining the chain of custody is an important part of the incident response process. Which of the following reasons explains why this is important?",
        "options": [
            "To maintain an information security policy",
            "To properly identify the issue",
            "To control evidence and maintain integrity",
            "To gather as much information as possible"
        ],
        "correct_answer": 3,
        "description": "The correct answer is to control evidence and maintain integrity. Proper chain of custody ensures that evidence is preserved in its original state, which is vital for legal and investigative purposes. \n\n- Maintaining an information security policy is a broader concept and not specifically related to incident response evidence. \n- Properly identifying the issue is important, but it does not directly relate to the chain of custody. \n- Gathering information is a goal of investigations, but maintaining the integrity of evidence is more critical."
    },
    {
        "question": "A remote user is experiencing issues connecting to a corporate email account on a laptop. The user clicks the internet connection icon and does not recognize the connected Wi-Fi. The help desk technician, who is troubleshooting the issue, assumes this is a rogue access point. Which of the following is the first action the technician should take?",
        "options": [
            "Restart the wireless adapter.",
            "Launch the browser to see if it redirects to an unknown site.",
            "Instruct the user to disconnect the Wi-Fi.",
            "Instruct the user to run the installed antivirus software."
        ],
        "correct_answer": 3,
        "description": "The correct answer is to instruct the user to disconnect the Wi-Fi. This action prevents potential data interception and secures the user's connection until the issue is resolved. \n\n- Restarting the wireless adapter may not address the underlying issue of a rogue access point. \n- Launching the browser does not directly resolve the connection issue and could expose the user to risks. \n- Running antivirus software is a good security measure but not the immediate action needed to disconnect from a potentially dangerous network."
    },
    {
        "question": "A systems administrator is troubleshooting network performance issues in a large corporate office. The end users report that traffic to certain internal environments is not stable and often drops. Which of the following command-line tools can provide the most detailed information for investigating the issue further?",
        "options": [
            "ipconfig",
            "arp",
            "nslookup",
            "pathping"
        ],
        "correct_answer": 4,
        "description": "The correct answer is pathping. This tool combines the functions of ping and tracert, providing detailed information about network latency and packet loss across multiple hops. \n\n- ipconfig displays network configuration details but does not analyze performance. \n- arp is used for address resolution and does not provide performance data. \n- nslookup resolves DNS queries but does not assess network performance."
    },
    {
        "question": "A user's workstation is failing to load. An analyst inspects the workstation and sees a message that states there is no bootable device. Which of the following should the analyst do first?",
        "options": [
            "Reimage the machine back to factory defaults.",
            "Verify drive readability in the BIOS.",
            "Select safe mode when the machine begins booting.",
            "Boot to a Linux live image."
        ],
        "correct_answer": 2,
        "description": "The correct answer is to verify drive readability in the BIOS. This step checks whether the BIOS recognizes the hard drive, which is essential for troubleshooting boot issues. \n\n- Reimaging the machine is a last resort and should only be done after confirming hardware issues. \n- Selecting safe mode assumes the device is recognized by the BIOS, which is not the case here. \n- Booting to a Linux live image can help diagnose issues but requires the drive to be readable first."
    },
    {
        "question": "A large university wants to equip all classrooms with high-definition IP videoconferencing equipment. Which of the following would most likely be impacted in this situation?",
        "options": [
            "SAN",
            "LAN",
            "GPU",
            "PAN"
        ],
        "correct_answer": 2,
        "description": "The correct answer is LAN (Local Area Network). Implementing high-definition videoconferencing requires sufficient bandwidth and network resources, which directly affects the LAN infrastructure. \n\n- SAN (Storage Area Network) pertains to storage solutions and is not directly involved in videoconferencing. \n- GPU (Graphics Processing Unit) affects video rendering but is not impacted by the network deployment. \n- PAN (Personal Area Network) typically involves devices within a small area and is less relevant for classroom videoconferencing."
    },
    {
        "question": "A technician needs administrator access on a Windows workstation to facilitate system changes without elevating permissions. Which of the following would best accomplish this task?",
        "options": [
            "Group Policy Editor",
            "Local Users and Groups",
            "Device Manager",
            "System Configuration"
        ],
        "correct_answer": 2,
        "description": "The correct answer is Local Users and Groups. This utility allows the technician to modify user permissions and grant administrative rights. \n\n- Group Policy Editor manages policies across users and devices but does not directly provide individual access control. \n- Device Manager deals with hardware devices and drivers, not user permissions. \n- System Configuration is for configuring system startup options and does not handle user access."
    },
    {
        "question": "Which of the following default system tools can be used in macOS to allow the technician to view the screen simultaneously with the user?",
        "options": [
            "Remote Assistance",
            "Remote Desktop Protocol",
            "Screen Sharing",
            "Virtual Network Computing"
        ],
        "correct_answer": 3,
        "description": "The correct answer is Screen Sharing. This built-in feature in macOS enables technicians to view and interact with a user's screen in real-time, facilitating troubleshooting. \n\n- Remote Assistance is primarily a Windows feature and not applicable to macOS. \n- Remote Desktop Protocol (RDP) is used for remote access but is not native to macOS. \n- Virtual Network Computing (VNC) can be used but is less integrated than the built-in Screen Sharing feature."
    },

#376-400

    {
        "question": "Windows updates need to be performed on a department's servers. Which of the following methods should be used to connect to the server?",
        "options": [
            "FTP",
            "MSRA",
            "RDP",
            "VPN"
        ],
        "correct_answer": 3,
        "description": "The correct answer is RDP (Remote Desktop Protocol). RDP allows remote access to a server's graphical interface, making it ideal for performing updates. \n\n- FTP (File Transfer Protocol) is primarily used for transferring files and does not provide remote desktop access. \n- MSRA (Microsoft Remote Assistance) is useful for providing help but is not typically used for server management tasks like updates. \n- VPN (Virtual Private Network) provides a secure connection but does not facilitate remote desktop access on its own."
    },
    {
        "question": "A technician is working on a Windows 10 PC that has unwanted applications starting on boot. Which of the following tools should the technician use to disable applications on startup?",
        "options": [
            "System Configuration",
            "Task Manager",
            "Performance Monitor",
            "Group Policy Editor"
        ],
        "correct_answer": 2,
        "description": "The correct answer is Task Manager. It includes a Startup tab that allows users to enable or disable applications that run at boot. \n\n- System Configuration (msconfig) is also an option but is more complex for this task. \n- Performance Monitor is used to track system performance and does not manage startup applications. \n- Group Policy Editor is used for enforcing policies on multiple machines rather than individual startup configurations."
    },
    {
        "question": "A technician receives an invalid certificate error when visiting a website. Other workstations on the same local network are unable to replicate this issue. Which of the following is most likely causing the issue?",
        "options": [
            "Date and time",
            "User access control",
            "UEFI boot mode",
            "Log-on times"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Date and time. An incorrect date or time can cause certificate validation errors since certificates are time-sensitive. \n\n- User access control typically manages permissions rather than affecting certificate validation. \n- UEFI boot mode relates to the system's startup method and does not impact certificates. \n- Log-on times are not directly related to certificate issues."
    },
    {
        "question": "A company is recycling old hard drives and wants to quickly reprovision the drives for reuse. Which of the following data destruction methods should the company use?",
        "options": [
            "Degaussing",
            "Standard formatting",
            "Low-level wiping",
            "Deleting"
        ],
        "correct_answer": 1,
        "description": "The correct answer is degaussing. This method erases data by disrupting the magnetic field of the drive, making data recovery virtually impossible. \n\n- Standard formatting may not remove all data and can be reversed with recovery software. \n- Low-level wiping is effective but can take longer than degaussing. \n- Deleting files does not ensure they are unrecoverable."
    },
    {
        "question": "Which of the following is used as a password manager in the macOS?",
        "options": [
            "Terminal",
            "FileVault",
            "Privacy",
            "Keychain"
        ],
        "correct_answer": 4,
        "description": "The correct answer is Keychain. Keychain securely stores passwords and other sensitive information on macOS. \n\n- Terminal is a command-line interface and does not manage passwords. \n- FileVault is used for disk encryption, not password management. \n- Privacy settings control application access to user data but do not function as a password manager."
    },
    {
        "question": "A company's assets are scanned annually. Which of the following will most likely help the company gain a holistic view of asset cost?",
        "options": [
            "Creating a database",
            "Assigning users to assets",
            "Inventorying asset tags",
            "Updating the procurement account owners"
        ],
        "correct_answer": 1,
        "description": "The correct answer is creating a database. A comprehensive database allows for better tracking and analysis of asset costs over time. \n\n- Assigning users to assets provides accountability but does not address cost analysis directly. \n- Inventorying asset tags helps in asset tracking but lacks a complete view of costs. \n- Updating procurement account owners ensures proper management but does not directly relate to cost overview."
    },
    {
        "question": "Which of the following types of malicious software is most likely to demand payments in cryptocurrency?",
        "options": [
            "Ransomware",
            "Keylogger",
            "Cryptomining",
            "Rootkit"
        ],
        "correct_answer": 1,
        "description": "The correct answer is ransomware. Ransomware encrypts files and demands payment, often in cryptocurrency, to restore access. \n\n- Keyloggers capture keystrokes for data theft but do not typically demand payment. \n- Cryptomining uses system resources to mine cryptocurrency but does not directly demand payment from users. \n- Rootkits are used to gain unauthorized access but do not usually involve financial demands."
    },
    {
        "question": "A systems administrator is creating a new document with a list of the websites that users are allowed to access. Which of the following types of documents is the administrator most likely creating?",
        "options": [
            "Access control list",
            "Acceptable use policy",
            "Incident report",
            "Standard operating procedure"
        ],
        "correct_answer": 1,
        "description": "The correct answer is access control list. This document specifies which websites users can access, enforcing security policies. \n\n- An acceptable use policy outlines general rules for system use but may not list specific websites. \n- An incident report documents security breaches or policy violations, not access permissions. \n- A standard operating procedure details processes but does not specify access permissions."
    },
    {
        "question": "Which of the following file types would be used in the Windows Startup folder to automate copying a personal storage table (.pst file) to a network drive at log-in?",
        "options": [
            ".bat",
            ".dll",
            ".ps1",
            ".txt"
        ],
        "correct_answer": 1,
        "description": "The correct answer is .bat (batch file). A .bat file can execute commands to automate tasks like copying files during startup. \n\n- .dll files are dynamic link libraries used by applications but are not executable scripts. \n- .ps1 files are PowerShell scripts, which can be used but are less common for startup tasks. \n- .txt files are plain text files and cannot execute commands."
    },
    {
        "question": "Which of the following macOS features can help a user close an application that has stopped responding?",
        "options": [
            "Finder",
            "Mission Control",
            "System Preferences",
            "Force Quit"
        ],
        "correct_answer": 4,
        "description": "The correct answer is Force Quit. This feature allows users to terminate unresponsive applications quickly. \n\n- Finder is the file management system and does not manage application states. \n- Mission Control provides an overview of open applications but does not close them. \n- System Preferences is used for system configuration, not for closing applications."
    },
    {
        "question": "Which of the following filesystem types does macOS use?",
        "options": [
            "ext4",
            "exFAT",
            "NTFS",
            "APFS"
        ],
        "correct_answer": 4,
        "description": "The correct answer is APFS (Apple File System). APFS is optimized for flash storage and is the default filesystem for macOS. \n\n- ext4 is a Linux filesystem and not compatible with macOS. \n- exFAT is used for external drives across different operating systems but is not the native filesystem for macOS. \n- NTFS is a Windows filesystem that macOS can read but not write to natively."
    },
    {
        "question": "A company recently outsourced its night-shift cleaning service. A technician is concerned about having unsupervised contractors in the building. Which of the following security measures can be used to prevent the computers from being accessed? (Choose two.)",
        "options": [
            "Implementing data-at-rest encryption",
            "Disabling AutoRun",
            "Restricting user permissions",
            "Restricting log-in times",
            "Enabling a screen lock",
            "Disabling local administrator accounts"
        ],
        "correct_answer": 1,
        "description": "The correct answers are implementing data-at-rest encryption and enabling a screen lock. \n\n- Implementing data-at-rest encryption ensures that even if contractors access computers, the data remains secure. \n- Enabling a screen lock prevents unauthorized access when users are away. \n- Disabling AutoRun does not prevent physical access to computers. \n- Restricting user permissions helps, but encryption adds an extra layer of security. \n- Restricting log-in times limits access hours but does not secure data itself. \n- Disabling local administrator accounts can restrict access but is not as effective as the first two measures."
    },
    {
        "question": "A user requested that the file permissions on a Linux device be changed to only allow access to a certain group of users. Which of the following commands should be used to modify file permissions?",
        "options": [
            "chmod",
            "setfacl",
            "chown",
            "passwd"
        ],
        "correct_answer": 2,
        "description": "The correct answer is setfacl. This command allows the administrator to set access control lists for files and directories, modifying permissions for specific users or groups. \n\n- chmod changes file permissions, but setfacl is specifically for ACLs. \n- chown changes the ownership of files, not permissions. \n- passwd is used for changing user passwords, not for modifying file permissions."
    },

    {
        "question": "A user installed a new computer game. Upon starting the game, the user notices the frame rates are low. Which of the following should the user upgrade to resolve the issue?",
        "options": [
            "Hard drive",
            "Graphics card",
            "Random-access memory",
            "Monitor"
        ],
        "correct_answer": 2,
        "description": "The correct answer is graphics card. Upgrading the graphics card can significantly improve frame rates in games, as it handles the rendering of images and video. \n\n- A hard drive upgrade won't enhance graphics performance; faster load times might occur, but frame rates won't improve. \n- Random-access memory (RAM) can help with overall system performance but won't specifically address low frame rates unless the current RAM is critically low. \n- A monitor upgrade will improve display quality but won't resolve the underlying issue with frame rates."
    },
    {
        "question": "A technician is troubleshooting application crashes on a Windows workstation. Each time the workstation user tries to open a website in a browser, the following message is displayed: crypt32.dll is missing or not found. Which of the following should the technician attempt first?",
        "options": [
            "Rebuild Windows profiles",
            "Reimage the workstation",
            "Roll back updates",
            "Perform a system file check"
        ],
        "correct_answer": 4,
        "description": "The correct answer is perform a system file check. This tool scans for and repairs corrupted system files, which is likely causing the missing crypt32.dll error. \n\n- Rebuilding Windows profiles is unnecessary unless the user-specific settings are corrupted. \n- Reimaging the workstation is a drastic measure that may not address the specific file issue. \n- Rolling back updates might help if a recent update caused the problem, but it's better to check for system file integrity first."
    },
    {
        "question": "A technician is setting up a new laptop. The company's security policy states that users cannot install virtual machines. Which of the following should the technician implement to prevent users from enabling virtual technology on their laptops?",
        "options": [
            "UEFI password",
            "Secure boot",
            "Account lockout",
            "Disable network drivers"
        ],
        "correct_answer": 1,
        "description": "The correct answer is UEFI password. Setting a UEFI password can prevent unauthorized changes to firmware settings, including enabling virtualization features. \n\n- Secure boot helps protect against unauthorized firmware but does not control virtualization settings. \n- Account lockout policies manage user access but won’t affect hardware capabilities. \n- Disabling network drivers won't prevent users from installing virtual machines; it only impacts network connectivity."
    },
    {
        "question": "Which of the following involves sending arbitrary characters in a web page request?",
        "options": [
            "SMS",
            "SSL",
            "XSS",
            "VPN"
        ],
        "correct_answer": 3,
        "description": "The correct answer is XSS (Cross-Site Scripting). XSS is a security vulnerability that allows an attacker to inject arbitrary code into web pages viewed by other users. \n\n- SMS (Short Message Service) is for sending text messages and not related to web requests. \n- SSL (Secure Sockets Layer) is a protocol for secure communication over a computer network and does not involve sending arbitrary characters. \n- VPN (Virtual Private Network) is used for secure remote access but does not relate to web page requests."
    },
    {
        "question": "A user is trying to use proprietary software, but it crashes intermittently. The user notices that the desktop is displaying a 'low memory' warning message. Upon restarting the desktop, the issue persists. Which of the following should a technician do next to troubleshoot the issue?",
        "options": [
            "Reimage the computer.",
            "Replace the system RAM.",
            "Reinstall and update the failing software.",
            "Decrease the page file size."
        ],
        "correct_answer": 3,
        "description": "The correct answer is reinstall and update the failing software. This step can resolve issues caused by corrupted installation files or outdated versions that may not manage memory efficiently. \n\n- Reimaging the computer is excessive at this point and may not directly address the software issue. \n- Replacing the system RAM may be necessary, but first confirming that the software is the cause is more efficient. \n- Decreasing the page file size can exacerbate memory issues, as it reduces virtual memory available for applications."
    },
    {
        "question": "An office is experiencing constant connection attempts to the corporate Wi-Fi. Which of the following should be disabled to mitigate connection attempts?",
        "options": [
            "SSID",
            "DHCP",
            "Firewall",
            "SSD"
        ],
        "correct_answer": 1,
        "description": "The correct answer is SSID. Disabling the SSID broadcast makes the network less visible to unauthorized users, reducing connection attempts. \n\n- Disabling DHCP would make it harder for legitimate users to connect since they wouldn't automatically receive an IP address. \n- A firewall should be enabled to protect the network; disabling it would increase vulnerabilities. \n- SSD (Solid State Drive) is unrelated to network connections."
    },
    {
        "question": "A customer is accessing a public kiosk in a company’s lobby. Which of the following should be enforced to mitigate the risk of customer data being accidentally saved to the kiosk?",
        "options": [
            "Manually clearing browsing data",
            "Private-browsing mode",
            "Browser data synchronization",
            "Password manager"
        ],
        "correct_answer": 2,
        "description": "The correct answer is private-browsing mode. This mode prevents the browser from saving any history or data from the session, reducing the risk of personal information being stored. \n\n- Manually clearing browsing data is less secure, as users may forget to do it. \n- Browser data synchronization could inadvertently save user data to a cloud service. \n- A password manager is not applicable in this context and does not protect against data saving during a kiosk session."
    },
    {
        "question": "A technician receives a personal text message while troubleshooting a customer's PC. The technician does not reply to the message and continues troubleshooting. Which of the following best describes the technician's actions?",
        "options": [
            "Avoiding distractions",
            "Presenting a professional appearance",
            "Setting and meeting timelines",
            "Projecting confidence"
        ],
        "correct_answer": 1,
        "description": "The correct answer is avoiding distractions. By not responding to the text message, the technician remains focused on resolving the customer's issue without interruptions. \n\n- Presenting a professional appearance relates more to demeanor and attire than distractions. \n- Setting and meeting timelines is important but doesn't apply to the technician's choice here. \n- Projecting confidence is beneficial but not directly related to the technician's decision to ignore the text."
    },
    {
        "question": "A new employee is having difficulties using a laptop with a docking station. The laptop is connected to the docking station, and the laptop is closed. The external monitor works for a few seconds, but then the laptop goes to sleep. Which of the following options should the technician configure in order to fix the issue?",
        "options": [
            "Hibernate",
            "Sleep/suspend",
            "Choose what closing the lid does",
            "Turn on fast startup"
        ],
        "correct_answer": 3,
        "description": "The correct answer is choose what closing the lid does. Configuring this setting allows the technician to prevent the laptop from sleeping when the lid is closed, ensuring continuous operation with the docking station. \n\n- Hibernate is a power-saving state but doesn't resolve the issue of sleep mode activation. \n- Sleep/suspend settings are the cause of the problem, not the solution. \n- Turning on fast startup improves boot times but does not address the immediate issue with the docking station."
    },
    {
        "question": "A technician is unable to access the internet or named network resources. The technician receives a valid IP address from the DHCP server and can ping the default gateway. Which of the following should the technician check next to resolve the issue?",
        "options": [
            "Verify the DNS server settings",
            "Turn off the Windows firewall",
            "Confirm the subnet mask is correct",
            "Configure a static IP address"
        ],
        "correct_answer": 1,
        "description": "The correct answer is verify the DNS server settings. If the IP address is valid and the default gateway is reachable, DNS settings could be the reason for the inability to access the internet. \n\n- Turning off the Windows firewall could expose the system to vulnerabilities and should only be a last resort. \n- Confirming the subnet mask is correct is important, but since the DHCP server provided a valid address, it's likely correct. \n- Configuring a static IP address is unnecessary and may complicate network management."
    },
    {
        "question": "A technician needs to ensure that USB devices are not suspended by the operating system. Which of the following Control Panel utilities should the technician use to configure the setting?",
        "options": [
            "System",
            "Power Options",
            "Devices and Printers",
            "Ease of Access"
        ],
        "correct_answer": 2,
        "description": "The correct answer is Power Options. This utility allows the technician to modify settings related to power management, including USB selective suspend settings. \n\n- The System utility primarily deals with system properties and performance settings, not power management. \n- Devices and Printers show connected devices but do not provide options for power settings. \n- Ease of Access is for accessibility options and does not relate to USB device management."
    },
    {
        "question": "During a network outage, a technician discovers a new network switch that was not listed in the support documentation. The switch was installed during a recent change window when a new office was added to the environment. Which of the following would most likely prevent this type of mismatch after next month's change window?",
        "options": [
            "Performing annual network topology reviews",
            "Requiring all network changes include updating the network diagrams",
            "Allowing network changes once per year",
            "Routinely backing up switch configuration files"
        ],
        "correct_answer": 2,
        "description": "The correct answer is requiring all network changes include updating the network diagrams. This ensures that any new equipment or changes are documented, preventing mismatches in future reviews. \n\n- Performing annual network topology reviews is useful but may not catch changes made during the year. \n- Allowing network changes only once per year can delay necessary updates and responses. \n- Routinely backing up switch configuration files is important for recovery but doesn't prevent undocumented changes from being made."
    }


]
