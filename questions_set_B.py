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
    }




]
