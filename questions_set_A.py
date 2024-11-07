questions_set_A = [

#2 - 10
{
    "question": "A help desk team lead contacts a systems administrator because the technicians are unable to log in to a Linux server that is used to access tools. When the administrator tries to use remote desktop to log in to the server, the administrator sees the GUI is crashing. Which of the following methods can the administrator use to troubleshoot the server effectively?",
    "options": [
        "SFTP",
        "SSH",
        "VNC",
        "MSRA"
    ],
    "correct_answer": 2,
    "description": "The correct answer is 'SSH.' SSH (Secure Shell) provides a secure command-line interface for accessing Linux servers, allowing the administrator to troubleshoot the server without relying on the graphical user interface (GUI), which is crashing. \n\n- SFTP (Secure File Transfer Protocol) is used for transferring files, not for remote administration. \n- VNC (Virtual Network Computing) provides a graphical interface, which is not suitable if the GUI is crashing. \n- MSRA (Microsoft Remote Assistance) is for Windows environments and won't work with Linux servers."
},

{
    "question": "A company wants to remove information from past users' hard drives in order to reuse the hard drives. Which of the following is the MOST secure method?",
    "options": [
        "Reinstalling Windows",
        "Performing a quick format",
        "Using disk-wiping software",
        "Deleting all files from command-line interface"
    ],
    "correct_answer": 3,
    "description": "The correct answer is 'Using disk-wiping software.' Disk-wiping software securely erases all data from the hard drive by overwriting it multiple times, ensuring that the data cannot be recovered. \n\n- Reinstalling Windows may remove the operating system but does not securely erase user data. \n- Performing a quick format only removes file system references to data, leaving the data itself recoverable. \n- Deleting files via command-line interface only removes references to the files, but data recovery is still possible."
},

{
    "question": "A user is having phone issues after installing a new application that claims to optimize performance. The user downloaded the application directly from the vendor's website and is now experiencing high network utilization and is receiving repeated security warnings. Which of the following should the technician perform FIRST to mitigate the issue?",
    "options": [
        "Reset the phone to factory settings.",
        "Uninstall the fraudulent application.",
        "Increase the data plan limits.",
        "Disable the mobile hotspot."
    ],
    "correct_answer": 2,
    "description": "The correct answer is 'Uninstall the fraudulent application.' The high network utilization and security warnings are likely caused by the newly installed app, which is potentially harmful. Uninstalling it removes the root cause of the issue. \n\n- Resetting the phone to factory settings may be an option but should be done only if uninstalling the app does not resolve the issue. \n- Increasing the data plan limits does not address the root cause of the issue, which is the fraudulent app. \n- Disabling the mobile hotspot does not directly resolve the issue related to the application."
},

{
    "question": "A change advisory board just approved a change request. Which of the following is the MOST likely next step in the change process?",
    "options": [
        "End user acceptance",
        "Perform risk analysis",
        "Communicate to stakeholders",
        "Sandbox testing"
    ],
    "correct_answer": 3,
    "description": "The correct answer is 'Communicate to stakeholders.' Once a change request is approved, it is important to inform stakeholders about the upcoming changes so they can prepare accordingly. \n\n- End user acceptance comes later in the process, after the change is implemented. \n- Risk analysis should have already been performed during the planning phase of the change process. \n- Sandbox testing occurs earlier in the process to test the change in a controlled environment."
},

{
    "question": "A user calls the help desk to report that none of the files on a PC will open. The user also indicates a program on the desktop is requesting payment in exchange for file access. A technician verifies the user's PC is infected with ransomware. Which of the following should the technician do FIRST?",
    "options": [
        "Scan and remove the malware.",
        "Schedule automated malware scans.",
        "Quarantine the system.",
        "Disable System Restore."
    ],
    "correct_answer": 3,
    "description": "The correct answer is 'Quarantine the system.' The first step in responding to a ransomware infection is to isolate the system to prevent the ransomware from spreading to other devices. \n\n- Scanning and removing the malware can only happen after the system is isolated. \n- Scheduling automated malware scans is a proactive measure but not an immediate step in response to an active ransomware attack. \n- Disabling System Restore might prevent the malware from being restored but does not prevent its spread."
},

{
    "question": "A company is issuing smartphone to employees and needs to ensure data is secure if the devices are lost or stolen. Which of the following provides the BEST solution?",
    "options": [
        "Anti-malware",
        "Remote wipe",
        "Locator applications",
        "Screen lock"
    ],
    "correct_answer": 2,
    "description": "The correct answer is 'Remote wipe.' Remote wipe allows the company to erase data from the device remotely in the event it is lost or stolen, ensuring sensitive data is not compromised. \n\n- Anti-malware protects the device from malicious software but does not address the issue of lost or stolen devices. \n- Locator applications help track the device's location but do not provide a way to secure the data. \n- Screen lock secures access to the device but does not protect the data if the device is stolen."
},

{
    "question": "A user reports seeing random, seemingly non-malicious advertisement notifications in the Windows 10 Action Center. The notifications indicate the advertisements are coming from a web browser. Which of the following is the BEST solution for a technician to implement?",
    "options": [
        "Disable the browser from sending notifications to the Action Center.",
        "Run a full antivirus scan on the computer.",
        "Disable all Action Center notifications.",
        "Move specific site notifications from Allowed to Block."
    ],
    "correct_answer": 4,
    "description": "The correct answer is 'Move specific site notifications from Allowed to Block.' Blocking notifications from the specific websites that are sending the ads helps stop the unwanted ads while allowing legitimate notifications. \n\n- Disabling the browser from sending notifications may stop all notifications, but it is better to block only the specific sites causing issues. \n- Running a full antivirus scan is useful for detecting malware but is unlikely to address legitimate, non-malicious advertisements. \n- Disabling all Action Center notifications will prevent all notifications, including those that are important."
},


{
    "question": "A help desk technician is troubleshooting a workstation in a SOHO environment that is running above normal system baselines. The technician discovers an unknown executable with a random string name running on the system. The technician terminates the process, and the system returns to normal operation. The technician thinks the issue was an infected file, but the antivirus is not detecting a threat. The technician is concerned other machines may be infected with this unknown virus. Which of the following is the MOST effective way to check other machines on the network for this unknown threat?",
    "options": [
        "Run a startup script that removes files by name.",
        "Provide a sample to the antivirus vendor.",
        "Manually check each machine.",
        "Monitor outbound network traffic."
    ],
    "correct_answer": [3],
    "description": "The correct answer is Manually check each machine. Manually inspecting each machine allows the technician to identify any unknown executables or unusual behavior similar to what was found on the original workstation. \n\n- Running a startup script that removes files by name could inadvertently remove important files or may not catch all instances of the virus if the file names are not known.\n- Providing a sample to the antivirus vendor is useful for future virus definitions but does not immediately help in detecting threats across the network.\n- Monitoring outbound network traffic can help identify suspicious activity, but without knowledge of the specific threat, manual checks provide a direct method to find infected machines."
},

#19-20

    {
        "question": "A laptop user is visually impaired and requires a different cursor color. Which of the following OS utilities is used to change the color of the cursor?",
        "options": [
            "Keyboard",
            "Touch pad",
            "Ease of Access Center",
            "Display settings"
        ],
        "correct_answer": [3],
        "description": "The correct answer is Ease of Access Center. This utility in the OS allows users to customize accessibility settings, including the size and color of the cursor to assist users with visual impairments.\n\n- Keyboard and Touch pad settings are unrelated to cursor customization.\n- Display settings change screen resolution and brightness, not cursor colors."
    },
    {
        "question": "A manager reports that staff members often forget the passwords to their mobile devices and applications. Which of the following should the systems administrator do to reduce the number of help desk tickets submitted?",
        "options": [
            "Enable multifactor authentication.",
            "Increase the failed log-in threshold.",
            "Remove complex password requirements.",
            "Implement a single sign-on with biometrics."
        ],
        "correct_answer": [4],
        "description": "The correct answer is Implement a single sign-on with biometrics. This method allows users to log in once and use biometric authentication, such as a fingerprint or face scan, to access all apps without remembering multiple passwords.\n\n- Multifactor authentication improves security but doesn't address forgotten passwords.\n- Increasing the failed login threshold only delays lockouts, not solving the problem.\n- Removing complex password requirements reduces security."
    },
    {
        "question": "A technician suspects a rootkit has been installed and needs to be removed. Which of the following would BEST resolve the issue?",
        "options": [
            "Application updates",
            "Anti-malware software",
            "OS reinstallation",
            "File restore"
        ],
        "correct_answer": [3],
        "description": "The correct answer is OS reinstallation. Rootkits are sophisticated threats that can compromise system integrity, and the most effective way to remove them is by reinstalling the operating system to ensure the malware is completely eradicated.\n\n- Application updates and anti-malware software may not detect or remove rootkits due to their deep integration in the OS.\n- File restore only recovers files and doesn’t remove malware."
    },
    {
        "question": "A technician is setting up a SOHO wireless router. The router is about ten years old. The customer would like the most secure wireless network possible. Which of the following should the technician configure?",
        "options": [
            "WPA2 with TKIP",
            "WPA2 with AES",
            "WPA3 with AES-256",
            "WPA3 with AES-128"
        ],
        "correct_answer": [2],
        "description": "The correct answer is WPA2 with AES. Given the router's age, WPA2 with AES provides a good balance of security and compatibility, as WPA3 may not be supported on older hardware.\n\n- WPA3 with AES-128 and AES-256 are newer and more secure but may not work on a 10-year-old router.\n- WPA2 with TKIP is outdated and less secure compared to WPA2 with AES."
    },
    {
        "question": "A technician is troubleshooting an issue involving programs on a Windows 10 machine that are loading on startup but causing excessive boot times. Which of the following should the technician do to selectively prevent programs from loading?",
        "options": [
            "Right-click the Windows button, then select Run... entering shell:startup and clicking OK, and then move items one by one to the Recycle Bin.",
            "Remark out entries listed HKEY_LOCAL_MACHINE>SOFTWARE>Microsoft>Windows>CurrentVersion>Run.",
            "Manually disable all startup tasks currently listed as enabled and reboot, checking for issue resolution at startup.",
            "Open the Startup tab and methodically disable items currently listed as enabled and reboot, checking for issue resolution at each startup."
        ],
        "correct_answer": [4],
        "description": "The correct answer is Open the Startup tab and methodically disable items currently listed as enabled and reboot, checking for issue resolution at each startup. This ensures a methodical approach to isolating which startup program is causing excessive boot times.\n\n- Editing the registry directly can be risky without knowing exactly which entries to modify.\n- Moving files to the Recycle Bin or disabling all startup tasks might solve the problem but isn't the most efficient or precise method."
    },
    {
        "question": "A call center technician receives a call from a user asking how to update Windows. Which of the following describes what the technician should do?",
        "options": [
            "Have the user consider using an iPad if the user is unable to complete updates.",
            "Have the user text the user's password to the technician.",
            "Ask the user to click in the Search field, type Check for Updates, and then press the Enter key.",
            "Advise the user to wait for an upcoming, automatic patch."
        ],
        "correct_answer": [3],
        "description": "The correct answer is Ask the user to click in the Search field, type Check for Updates, and then press the Enter key. This provides clear and direct instructions on how to perform a Windows update.\n\n- Telling the user to wait for an automatic patch may not solve the issue in a timely manner.\n- Asking for a password via text is insecure and inappropriate."
    },
    {
        "question": "When a user calls in to report an issue, a technician submits a ticket on the user's behalf. Which of the following practices should the technician use to make sure the ticket is associated with the correct user?",
        "options": [
            "Have the user provide a callback phone number to be added to the ticket.",
            "Assign the ticket to the department's power user.",
            "Register the ticket with a unique user identifier.",
            "Provide the user with a unique ticket number that can be referenced on subsequent calls."
        ],
        "correct_answer": [3],
        "description": "The correct answer is Register the ticket with a unique user identifier. This ensures that the ticket is correctly associated with the user and prevents confusion in tracking the issue.\n\n- Assigning the ticket to a department power user does not ensure the ticket is linked to the correct user.\n- A callback number is useful for follow-up but does not ensure correct ticket association."
    },
    {
        "question": "Which of the following is the MOST important environmental concern inside a data center?",
        "options": [
            "Battery disposal",
            "Electrostatic discharge mats",
            "Toner disposal",
            "Humidity levels"
        ],
        "correct_answer": [4],
        "description": "The correct answer is Humidity levels. Maintaining optimal humidity levels is crucial in a data center to prevent electrostatic discharge or condensation, both of which can damage sensitive equipment.\n\n- Battery and toner disposal are environmental concerns but less critical to daily operations than humidity control.\n- ESD mats help with static discharge but aren't as important as monitoring overall humidity."
    },
    {
        "question": "A user is unable to log in to the network. The network uses 802.1X with EAP-TLS to authenticate on the wired network. The user has been on an extended leave and has not logged in to the computer in several months. Which of the following is causing the log-in issue?",
        "options": [
            "Expired certificate",
            "OS update failure",
            "Service not started",
            "Application crash",
            "Profile rebuild needed"
        ],
        "correct_answer": [1],
        "description": "The correct answer is Expired certificate. EAP-TLS relies on certificates for authentication, and an expired certificate will prevent the user from logging in.\n\n- An OS update failure or application crash would not typically cause an authentication failure in an 802.1X environment."
    },
    {
        "question": "A technician needs to format a USB drive to transfer 20GB of data from a Linux computer to a Windows computer. Which of the following filesystems will the technician MOST likely use?",
        "options": [
            "FAT32",
            "ext4",
            "NTFS",
            "exFAT"
        ],
        "correct_answer": [4],
        "description": "The correct answer is exFAT. exFAT supports large file sizes and is compatible with both Linux and Windows, making it ideal for transferring 20GB of data.\n\n- FAT32 does not support files larger than 4GB.\n- ext4 is a Linux file system and not natively supported by Windows.\n- NTFS is supported by Windows, but writing to NTFS on Linux may require additional drivers."
    },

#21-30


    {
        "question": "Following the latest Windows update, PDF files are opening in Microsoft Edge instead of Adobe Reader. Which of the following utilities should be used to ensure all PDF files open in Adobe Reader?",
        "options": [
            "Network and Sharing Center",
            "Programs and Features",
            "Default Apps",
            "Add or Remove Programs"
        ],
        "correct_answer": [3],
        "description": "The correct answer is Default Apps. This utility allows users to set the default application for different file types, including PDFs, ensuring that Adobe Reader is used for all PDF files.\n\n- Network and Sharing Center is for managing network connections and does not affect file associations. \n- Programs and Features, and Add or Remove Programs are used for installing or uninstalling software but not for managing default applications."
    },
    {
        "question": "A technician needs to exclude an application folder from being cataloged by a Windows 10 search. Which of the following utilities should be used?",
        "options": [
            "Privacy",
            "Indexing Options",
            "System",
            "Device Manager"
        ],
        "correct_answer": [2],
        "description": "The correct answer is Indexing Options. This utility allows you to customize which folders and files are indexed by Windows Search, ensuring the application folder is excluded.\n\n- Privacy settings manage data collection preferences but do not impact search indexing.\n- System manages performance settings and hardware but does not affect search results.\n- Device Manager is used for managing hardware devices, not for search indexing."
    },
    {
        "question": "As part of a CYOD policy, a systems administrator needs to configure each user's Windows device to require a password when resuming from a period of sleep or inactivity. Which of the following paths will lead the administrator to the correct settings?",
        "options": [
            "Use Settings to access Screensaver settings.",
            "Use Settings to access Screen Timeout settings.",
            "Use Settings to access General.",
            "Use Settings to access Display."
        ],
        "correct_answer": [1],
        "description": "The correct answer is Use Settings to access Screensaver settings. Screensaver settings include the option to require a password on resume.\n\n- Screen Timeout settings relate to power management but do not include password settings. \n- General and Display settings do not manage security policies related to sleep or inactivity."
    },
    {
        "question": "A technician is working with a company to determine the best way to transfer sensitive personal information between offices when conducting business. The company currently uses USB drives and is resistant to change. The company's compliance officer states that all media at rest must be encrypted. Which of the following would be the BEST way to secure the current workflow?",
        "options": [
            "Deploy a secondary hard drive with encryption on the appropriate workstation.",
            "Configure a hardened SFTP portal for file transfers between file servers.",
            "Require files to be individually password protected with unique passwords.",
            "Enable BitLocker To Go with a password that meets corporate requirements."
        ],
        "correct_answer": [4],
        "description": "The correct answer is Enable BitLocker To Go with a password that meets corporate requirements. BitLocker To Go provides encryption for removable drives such as USB drives, which fits the company's current workflow and security needs.\n\n- Deploying a secondary encrypted hard drive may help but would require more changes to the current process.\n- SFTP portals secure file transfers over networks but do not apply to USB drives.\n- Individual password protection is less secure and harder to manage than drive-level encryption."
    },
    {
        "question": "The command cat comptia.txt was issued on a Linux terminal. Which of the following results should be expected?",
        "options": [
            "The contents of the text comptia.txt will be replaced with a new blank document.",
            "The contents of the text comptia.txt would be displayed.",
            "The contents of the text comptia.txt would be categorized in alphabetical order.",
            "The contents of the text comptia.txt would be copied to another comptia.txt file."
        ],
        "correct_answer": [2],
        "description": "The correct answer is The contents of the text comptia.txt would be displayed. The 'cat' command in Linux is used to display the contents of a file.\n\n- The command does not replace the contents of the file or sort it alphabetically.\n- Copying content is handled by other commands like 'cp'."
    },
    {
        "question": "An incident handler needs to preserve evidence for possible litigation. Which of the following will the incident handler MOST likely do to preserve the evidence?",
        "options": [
            "Encrypt the files.",
            "Clone any impacted hard drives.",
            "Contact the cyber insurance company.",
            "Inform law enforcement."
        ],
        "correct_answer": [2],
        "description": "The correct answer is Clone any impacted hard drives. Cloning ensures an exact copy of the drive is made, preserving the evidence in a forensically sound manner for investigation or legal proceedings.\n\n- Encrypting the files could alter the evidence and complicate investigation.\n- Contacting cyber insurance or law enforcement is important but not the first step in preserving evidence."
    },
    {
        "question": "A technician needs to recommend the best backup method that will mitigate ransomware attacks. Only a few files are regularly modified; however, storage space is a concern. Which of the following backup methods would BEST address these concerns?",
        "options": [
            "Full",
            "Differential",
            "Off-site",
            "Grandfather-father-son"
        ],
        "correct_answer": [2],
        "description": "The correct answer is Differential. Differential backups only copy files that have changed since the last full backup, reducing storage space while ensuring important files are protected.\n\n- Full backups take up more storage space. \n- Off-site backups can add security but don't specifically mitigate storage space concerns.\n- Grandfather-father-son is a backup rotation scheme but does not address the space issue."
    },
    {
        "question": "A technician is troubleshooting a customer's PC and receives a phone call. The technician does not take the call and sets the phone to silent. Which of the following BEST describes the technician's actions?",
        "options": [
            "Avoid distractions",
            "Deal appropriately with customer's confidential material",
            "Adhere to user privacy policy",
            "Set and meet timelines"
        ],
        "correct_answer": [1],
        "description": "The correct answer is Avoid distractions. By silencing the phone, the technician ensures they remain focused on the current task, leading to better concentration and quality work.\n\n- Dealing with confidential material and adhering to privacy policies are important but not directly related to this action.\n- Setting timelines is also not applicable in this scenario."
    },
    {
        "question": "A technician needs to transfer a large number of files over an unreliable connection. The technician should be able to resume the process if the connection is interrupted. Which of the following tools can be used?",
        "options": [
            "sfc",
            "chkdsk",
            "git clone",
            "robocopy"
        ],
        "correct_answer": [4],
        "description": "The correct answer is robocopy. Robocopy is a Windows command-line tool designed for file replication, and it can resume transfers if interrupted, making it ideal for large file transfers over unreliable connections.\n\n- sfc (System File Checker) is for scanning and repairing system files.\n- chkdsk checks for disk errors, and git clone is for cloning repositories, not file transfer."
    },
    {
        "question": "A company installed a new backup and recovery system. Which of the following types of backups should be completed FIRST?",
        "options": [
            "Full",
            "Non-parity",
            "Differential",
            "Incremental"
        ],
        "correct_answer": [1],
        "description": "The correct answer is Full. A full backup is the initial step in any backup strategy as it captures all data on the system, forming the foundation for future differential or incremental backups.\n\n- Non-parity is not a standard backup type.\n- Differential and incremental backups are subsequent backups that rely on a full backup to be in place first."
    },

#31-40


    {
        "question": "A user's smartphone data usage is well above average. The user suspects an installed application is transmitting data in the background. The user would like to be alerted when an application attempts to communicate with the internet. Which of the following BEST addresses the user's concern?",
        "options": [
            "Operating system updates",
            "Remote wipe",
            "Antivirus",
            "Firewall"
        ],
        "correct_answer": [4],
        "description": "The correct answer is Firewall. A firewall can monitor and control network traffic, allowing the user to block or allow applications from communicating with the internet. This would alert the user when an app tries to transmit data.\n\n- Operating system updates keep the device secure but do not directly monitor network traffic.\n- Remote wipe is used to erase data on a lost or stolen device.\n- Antivirus helps detect malicious software but is not designed to alert the user when an application accesses the internet."
    },
    {
        "question": "A technician has been tasked with installing a workstation that will be used for point-of-sale transactions. The point-of-sale system will process credit cards and loyalty cards. Which of the following encryption technologies should be used to secure the workstation in case of theft?",
        "options": [
            "Data-in-transit encryption",
            "File encryption",
            "USB drive encryption",
            "Disk encryption"
        ],
        "correct_answer": [4],
        "description": "The correct answer is Disk encryption. Disk encryption ensures that all data on the hard drive is encrypted and inaccessible in the event the workstation is stolen.\n\n- Data-in-transit encryption protects data being transmitted over networks, not data stored on the workstation.\n- File encryption only encrypts specific files and is less comprehensive than full disk encryption.\n- USB drive encryption protects removable storage devices, not the entire workstation."
    },
    {
        "question": "A user contacted the help desk to report pop-ups on a company workstation, indicating the computer has been infected with 137 viruses and payment is needed to remove them. The user thought the company-provided antivirus software would prevent this issue. The help desk ticket states that the user only receives these messages when first opening the web browser. Which of the following steps would MOST likely resolve the issue? (Choose two.)",
        "options": [
            "Scan the computer with the company-provided antivirus software.",
            "Install a new hard drive and clone the user's drive to it.",
            "Deploy an ad-blocking extension to the browser.",
            "Uninstall the company-provided antivirus software.",
            "Click the link in the messages to pay for virus removal.",
            "Perform a reset on the user's web browser."
        ],
        "correct_answer": [1, 6],
        "description": "The correct answers are Scan the computer with the company-provided antivirus software and Perform a reset on the user's web browser. Scanning the system will help detect any malware, while resetting the browser can remove malicious extensions or settings causing the pop-ups.\n\n- Installing a new hard drive is not necessary at this stage and would be an extreme measure.\n- Deploying an ad-blocking extension might reduce pop-ups but would not address the underlying issue.\n- Uninstalling the antivirus software would leave the system vulnerable, and clicking the link in the messages could lead to further malware infection."
    },
    {
        "question": "A technician is installing new software on a macOS computer. Which of the following file types will the technician MOST likely use?",
        "options": [
            ".deb",
            ".vbs",
            ".exe",
            ".app"
        ],
        "correct_answer": [4],
        "description": "The correct answer is .app. This is the file format for applications on macOS, and it is what users install when adding new software.\n\n- .deb is used for Linux-based distributions, particularly Debian.\n- .vbs is a Visual Basic Script used on Windows for automation.\n- .exe is the executable file format for Windows programs."
    },
    {
        "question": "A technician is investigating an employee's smartphone that has the following symptoms: \n✑ The device is hot, even when it is not in use. \n✑ Applications crash, especially when others are launched. \n✑ Certain applications, such as GPS, are in portrait mode when they should be in landscape mode. \nWhich of the following can the technician do to MOST likely resolve these issues with minimal impact? (Choose two.)",
        "options": [
            "Turn on autorotation.",
            "Activate airplane mode.",
            "Close unnecessary applications.",
            "Perform a factory reset.",
            "Update the device's operating system.",
            "Reinstall the applications that have crashed."
        ],
        "correct_answer": [3, 5],
        "description": "The correct answers are Close unnecessary applications and Update the device's operating system. Closing background applications will help prevent overheating and crashes, while updating the OS can fix bugs that cause apps to malfunction.\n\n- Autorotation might address screen orientation issues but would not fix overheating or app crashes.\n- Airplane mode would stop background data but is not a long-term solution.\n- Factory reset is a drastic measure that may not be necessary if the issues can be solved with simpler steps."
    },
    {
        "question": "A customer reported that a home PC with Windows 10 installed in the default configuration is having issues loading applications after a reboot occurred in the middle of the night. Which of the following is the FIRST step in troubleshooting?",
        "options": [
            "Install alternate open-source software in place of the applications with issues.",
            "Run both CPU and memory tests to ensure that all hardware functionality is normal.",
            "Check for any installed patches and roll them back one at a time until the issue is resolved.",
            "Reformat the hard drive, and then reinstall the newest Windows 10 release and all applications."
        ],
        "correct_answer": [3],
        "description": "The correct answer is Check for any installed patches and roll them back one at a time until the issue is resolved. A recent patch may have caused the issue, and rolling back the update is the least intrusive way to fix the problem.\n\n- Installing alternative software is not necessary, as it does not address the root cause.\n- CPU and memory tests are useful but should be performed after checking for software-related issues.\n- Reformatting the hard drive and reinstalling Windows is a last resort and not the first step."
    },
    {
        "question": "Which of the following could be used to implement secure physical access to a data center?",
        "options": [
            "Geofence",
            "Alarm system",
            "Badge reader",
            "Motion sensor"
        ],
        "correct_answer": [3],
        "description": "The correct answer is Badge reader. Badge readers allow only authorized personnel to enter secured areas, ensuring that access is restricted.\n\n- Geofencing sets virtual boundaries and is more commonly used for mobile devices.\n- Alarm systems detect breaches but do not control access.\n- Motion sensors detect movement but do not verify identity."
    },
    {
        "question": "The Chief Executive Officer at a bank recently saw a news report about a high-profile cybercrime where a remote-access tool that the bank uses for support was also used in this crime. The report stated that attackers were able to brute force passwords to access systems. Which of the following would BEST limit the bank's risk? (Choose two.)",
        "options": [
            "Enable multifactor authentication for each support account.",
            "Limit remote access to destinations inside the corporate network.",
            "Block all support accounts from logging in from foreign countries.",
            "Configure a replacement remote-access tool for support cases.",
            "Purchase a password manager for remote-access tool users.",
            "Enforce account lockouts after five bad password attempts."
        ],
        "correct_answer": [1, 6],
        "description": "The correct answers are Enable multifactor authentication for each support account and Enforce account lockouts after five bad password attempts. Multifactor authentication makes it harder for attackers to access accounts, and account lockouts help prevent brute force attacks.\n\n- Limiting remote access to the corporate network does not stop attackers who have valid credentials.\n- Blocking logins from foreign countries adds some protection but is not as effective as multifactor authentication.\n- Changing the remote-access tool might not address the underlying issue of weak password security.\n- A password manager helps users manage passwords but does not directly prevent brute force attacks."
    },
    {
        "question": "A user reports a computer is running slow. Which of the following tools will help a technician identify the issue?",
        "options": [
            "Disk Cleanup",
            "Group Policy Editor",
            "Disk Management",
            "Resource Monitor"
        ],
        "correct_answer": [4],
        "description": "The correct answer is Resource Monitor. Resource Monitor provides detailed information on how the computer's resources, such as CPU and memory, are being used and helps pinpoint performance bottlenecks.\n\n- Disk Cleanup removes temporary files but does not help diagnose performance issues.\n- Group Policy Editor manages system policies but does not assist in troubleshooting slowness.\n- Disk Management is used for partitioning and managing storage drives."
    },
    {
        "question": "Upon downloading a new ISO, an administrator is presented with the following string: \n59d15a16ce90c8ee97fa7c211b7673a8 \nWhich of the following BEST describes the purpose of this string?",
        "options": [
            "XSS verification",
            "AES-256 verification",
            "Hash verification",
            "Digital signature verification"
        ],
        "correct_answer": [3],
        "description": "The correct answer is Hash verification. The string presented is a hash, which is used to verify that the downloaded ISO file has not been altered or corrupted.\n\n- XSS (Cross-Site Scripting) verification is related to web security, not file integrity.\n- AES-256 is an encryption standard and not used for file verification.\n- Digital signature verification also ensures file integrity but typically uses certificates, not hash strings."
    },
    
#41-50

    {
        "question": "A user's mobile phone has become sluggish. A systems administrator discovered several malicious applications on the device and reset the phone. The administrator installed MDM software. Which of the following should the administrator do to help secure the device against this threat in the future? (Choose two.)",
        "options": [
            "Prevent a device root.",
            "Disable biometric authentication.",
            "Require a PIN on the unlock screen.",
            "Enable developer mode.",
            "Block a third-party application installation.",
            "Prevent GPS spoofing."
        ],
        "correct_answer": [1, 5],
        "description": "The correct answers are Prevent a device root and Block a third-party application installation. Preventing device rooting helps protect the integrity of the OS by stopping users from bypassing built-in security features, and blocking third-party app installations reduces the risk of installing malicious software. \n\n- Disabling biometric authentication would reduce security by removing an extra layer of protection. \n- Requiring a PIN is beneficial, but the question asks for actions that target malicious app threats. \n- Enabling developer mode could increase security risks by allowing access to system settings and debugging features. \n- GPS spoofing is unrelated to app threats and securing the device from malicious applications."
    },
    {
        "question": "A technician is unable to join a Windows 10 laptop to a domain. Which of the following is the MOST likely reason?",
        "options": [
            "The domain's processor compatibility is not met.",
            "The laptop has Windows 10 Home installed.",
            "The laptop does not have an onboard Ethernet adapter.",
            "The laptop does not have all current Windows updates installed."
        ],
        "correct_answer": [2],
        "description": "The correct answer is The laptop has Windows 10 Home installed. Windows 10 Home edition does not include the necessary features to join a domain, which is only available in Windows 10 Pro and higher versions. \n\n- Processor compatibility is unrelated to domain joining. \n- The lack of an Ethernet adapter can be overcome with Wi-Fi, and this would not prevent domain joining. \n- Missing updates may cause issues, but they are unlikely to prevent domain joining entirely."
    },
    {
        "question": "Which of the following OS types provides a lightweight option for workstations that need an easy-to-use, browser-based interface?",
        "options": [
            "FreeBSD",
            "Chrome OS",
            "macOS",
            "Windows"
        ],
        "correct_answer": [2],
        "description": "The correct answer is Chrome OS. Chrome OS is designed to be lightweight and optimized for web-based tasks, making it an ideal option for users who primarily use web applications. \n\n- FreeBSD is a UNIX-like OS, not typically known for its ease of use or lightweight nature. \n- macOS is a full-featured OS, not specifically designed for lightweight or browser-based usage. \n- Windows is also a full-featured OS and not lightweight when compared to Chrome OS."
    },
    {
        "question": "A user has requested help setting up the fingerprint reader on a Windows 10 laptop. The laptop is equipped with a fingerprint reader and is joined to a domain. Group Policy enables Windows Hello on all computers in the environment. Which of the following options describes how to set up Windows Hello Fingerprint for the user?",
        "options": [
            "Navigate to the Control Panel utility, select the Security and Maintenance submenu, select Change Security and Maintenance settings, select Windows Hello Fingerprint, and have the user place a fingerprint on the fingerprint reader repeatedly until Windows indicates setup is complete.",
            "Navigate to the Windows 10 Settings menu, select the Accounts submenu, select Sign-in options, select Windows Hello Fingerprint, and have the user place a fingerprint on the fingerprint reader repeatedly until Windows indicates setup is complete.",
            "Navigate to the Windows 10 Settings menu, select the Update & Security submenu, select Windows Security, select Windows Hello Fingerprint, and have the user place a fingerprint on the fingerprint reader repeatedly until Windows indicates setup is complete.",
            "Navigate to the Control Panel utility, select the Administrative Tools submenu, select the user account in the list, select Windows Hello Fingerprint, and have the user place a fingerprint on the fingerprint reader repeatedly until Windows indicates setup is complete."
        ],
        "correct_answer": [2],
        "description": "The correct answer is Navigate to the Windows 10 Settings menu, select the Accounts submenu, select Sign-in options, select Windows Hello Fingerprint, and have the user place a fingerprint on the fingerprint reader repeatedly until Windows indicates setup is complete. This is the correct procedure for setting up Windows Hello Fingerprint in a Windows 10 environment. \n\n- The Control Panel and Administrative Tools options are not used for setting up fingerprint readers on Windows 10. \n- Update & Security in Windows Settings does not provide access to Windows Hello Fingerprint setup."
    },
    {
        "question": "An architecture firm is considering upgrading its computer-aided design (CAD) software to the newest version that forces storage of backups of all CAD files on the software's cloud server. Which of the following is MOST likely to be of concern to the IT manager?",
        "options": [
            "All updated software must be tested with all system types and accessories.",
            "Extra technician hours must be budgeted during installation of updates.",
            "Network utilization will be significantly increased due to the size of CAD files.",
            "Large update and installation files will overload the local hard drives."
        ],
        "correct_answer": [3],
        "description": "The correct answer is Network utilization will be significantly increased due to the size of CAD files. CAD files are typically large, and constantly uploading them to the cloud will increase network bandwidth usage significantly, which is a major concern for IT managers. \n\n- Testing software updates is a standard practice but is not specific to cloud storage concerns. \n- Extra technician hours may be required, but the biggest issue is the ongoing network strain. \n- Overloading local hard drives is irrelevant since the files are stored in the cloud, not locally."
    },
    {
        "question": "Someone who is fraudulently claiming to be from a reputable bank calls a company employee. Which of the following describes this incident?",
        "options": [
            "Pretexting",
            "Spoofing",
            "Vishing",
            "Scareware"
        ],
        "correct_answer": [3],
        "description": "The correct answer is Vishing. Vishing is a form of social engineering in which attackers use voice communication (like phone calls) to deceive individuals into giving away sensitive information. \n\n- Pretexting refers to creating a fabricated scenario to steal information but can occur over various communication methods, not just voice. \n- Spoofing typically refers to faking caller IDs or email addresses, not the entire conversation. \n- Scareware uses fear tactics, usually in the form of pop-up messages or emails, not phone calls."
    },
    {
        "question": "The network was breached over the weekend. System logs indicate that a single user's account was successfully breached after 500 attempts with a dictionary attack. Which of the following would BEST mitigate this threat?",
        "options": [
            "Encryption at rest",
            "Account lockout",
            "Automatic screen lock",
            "Antivirus"
        ],
        "correct_answer": [2],
        "description": "The correct answer is Account lockout. Enforcing an account lockout policy after a certain number of failed login attempts would prevent the attacker from using a dictionary attack to guess the password. \n\n- Encryption at rest protects stored data but does not prevent account login attempts. \n- Automatic screen lock helps secure unattended devices but is not directly related to login security. \n- Antivirus software protects against malware but does not stop password guessing attacks."
    },
    {
        "question": "A user reports a PC is running slowly. The technician suspects it has a badly fragmented hard drive. Which of the following tools should the technician use?",
        "options": [
            "resmon.exe",
            "msconfig.exe",
            "dfrgui.exe",
            "msinfo32.exe"
        ],
        "correct_answer": [3],
        "description": "The correct answer is dfrgui.exe. This is the Disk Defragmenter utility in Windows, which is used to analyze and defragment the hard drive, improving performance by reorganizing fragmented data. \n\n- resmon.exe is used to monitor system resource usage but does not fix fragmentation. \n- msconfig.exe is used to configure startup programs, not disk defragmentation. \n- msinfo32.exe provides system information but does not address performance issues directly."
    },
    {
        "question": "A company has just refreshed several desktop PCs. The hard drives contain PII. Which of the following is the BEST method to dispose of the drives?",
        "options": [
            "Drilling",
            "Degaussing",
            "Low-level formatting",
            "Erasing/wiping"
        ],
        "correct_answer": [2],
        "description": "The correct answer is Degaussing. Degaussing uses strong magnetic fields to permanently erase all data from the hard drive, ensuring that sensitive PII cannot be recovered. \n\n- Drilling physically destroys the drive but does not guarantee all data is unrecoverable. \n- Low-level formatting is less secure and can sometimes be undone. \n- Erasing/wiping can be effective but may still leave traces of data."
    },
    {
        "question": "Which of the following is the MOST cost-effective version of Windows 10 that allows remote access through Remote Desktop?",
        "options": [
            "Home",
            "Pro for Workstations",
            "Enterprise",
            "Pro"
        ],
        "correct_answer": [4],
        "description": "The correct answer is Pro. Windows 10 Pro includes the necessary features for Remote Desktop at a lower cost than Enterprise or Pro for Workstations. \n\n- Windows 10 Home does not support Remote Desktop hosting. \n- Pro for Workstations and Enterprise are both more expensive and include additional features unnecessary for most users."
    },
#51-60


    {
        "question": "A user created a file on a shared drive and wants to prevent its data from being accidentally deleted by others. Which of the following applications should the technician use to assist the user with hiding the file?",
        "options": [
            "Device Manager",
            "Indexing Options",
            "File Explorer",
            "Administrative Tools"
        ],
        "correct_answer": [3],
        "description": "The correct answer is File Explorer. File Explorer is used to manage files and folders on Windows, and it allows users to hide files by changing their properties, offering an easy way to protect the file from being accessed or deleted by others. \n\n- Device Manager is used to manage hardware devices, not files or folders. \n- Indexing Options manage search indexing for files, but do not directly help in hiding or protecting them. \n- Administrative Tools offer system management utilities, which are not relevant to file-level permissions or hiding."
    },
    {
        "question": "A user is configuring a new SOHO Wi-Fi router for the first time. Which of the following settings should the user change FIRST?",
        "options": [
            "Encryption",
            "Wi-Fi channel",
            "Default passwords",
            "Service set identifier"
        ],
        "correct_answer": [3],
        "description": "The correct answer is Default passwords. Changing default passwords is the first step to securing the router and preventing unauthorized access, as default credentials are widely known and exploited by attackers. \n\n- Encryption settings are important for securing data, but without changing the default password, the router remains vulnerable. \n- Changing the Wi-Fi channel helps avoid interference, but it doesn't improve security. \n- The Service Set Identifier (SSID) helps identify the network, but changing it first has no impact on security."
    },
    {
        "question": "A technician has spent hours trying to resolve a computer issue for the company's Chief Executive Officer (CEO). The CEO needs the device returned as soon as possible. Which of the following step should the technician take NEXT?",
        "options": [
            "Continue researching the issue.",
            "Repeat the iterative processes.",
            "Inform the CEO the repair will take a couple of weeks.",
            "Escalate the ticket."
        ],
        "correct_answer": [4],
        "description": "The correct answer is Escalate the ticket. When a high-priority user like the CEO needs a rapid resolution and the technician is unable to fix the issue promptly, the best step is to escalate the ticket to a higher-level technician or specialist. \n\n- Continuing research or repeating the same processes will delay the resolution further, which is not ideal in this situation. \n- Informing the CEO of a long delay would be inappropriate without trying other escalation options."
    },
    {
        "question": "Which of the following must be maintained throughout the forensic evidence life cycle when dealing with a piece of evidence?",
        "options": [
            "Acceptable use",
            "Chain of custody",
            "Security policy",
            "Information management"
        ],
        "correct_answer": [2],
        "description": "The correct answer is Chain of custody. The chain of custody ensures that evidence is properly handled and tracked from collection to presentation, protecting its integrity and ensuring it can be used in legal proceedings. \n\n- Acceptable use policies govern the proper use of resources, but they do not address evidence handling. \n- Security policies protect information systems but are not specific to managing physical or digital evidence. \n- Information management focuses on the storage and organization of data, not specifically the handling of evidence."
    },
    {
        "question": "A technician is configuring a SOHO device. Company policy dictates that static IP addresses cannot be used. The company wants the server to maintain the same IP address at all times. Which of the following should the technician use?",
        "options": [
            "DHCP reservation",
            "Port forwarding",
            "DNS A record",
            "NAT"
        ],
        "correct_answer": [1],
        "description": "The correct answer is DHCP reservation. DHCP reservations ensure that a device, such as a server, always receives the same IP address from the DHCP server without requiring static IP configurations, meeting the company's policy requirements. \n\n- Port forwarding is used to direct traffic to specific devices, not to assign IP addresses. \n- A DNS A record is used for domain name resolution, not for maintaining a specific IP address. \n- NAT translates IP addresses between networks but does not ensure a consistent IP for a specific device."
    },
    {
        "question": "Security software was accidentally uninstalled from all servers in the environment. After requesting the same version of the software be reinstalled, the security analyst learns that a change request will need to be filled out. Which of the following is the BEST reason to follow the change management process in this scenario?",
        "options": [
            "Owners can be notified a change is being made and can monitor it for performance impact.",
            "A risk assessment can be performed to determine if the software is needed.",
            "End users can be aware of the scope of the change.",
            "A rollback plan can be implemented in case the software breaks an application."
        ],
        "correct_answer": [4],
        "description": "The correct answer is A rollback plan can be implemented in case the software breaks an application. Following the change management process ensures that, if the reinstallation of the security software causes problems, there is a structured plan to roll back the changes and restore the previous state. \n\n- Notifying owners is important but is not the primary concern in preventing operational disruptions. \n- A risk assessment is unlikely to question the need for critical security software. \n- Informing end users of the change is useful, but it does not directly address the risk of software failure."
    },
    {
        "question": "Once weekly, a user needs Linux to run a specific open-source application that is not available for the currently installed Windows platform. The user has limited bandwidth throughout the day. Which of the following solutions would be the MOST efficient, allowing for parallel execution of the Linux application and Windows applications?",
        "options": [
            "Install and run Linux and the required application in a PaaS cloud environment.",
            "Install and run Linux and the required application as a virtual machine installed under the Windows OS.",
            "Use a swappable drive bay for the boot drive and install each OS with applications on its own drive. Swap the drives as needed.",
            "Set up a dual boot system by selecting the option to install Linux alongside Windows."
        ],
        "correct_answer": [2],
        "description": "The correct answer is Install and run Linux and the required application as a virtual machine installed under the Windows OS. Running Linux as a virtual machine allows the user to run both Linux and Windows applications in parallel, without the need to restart the computer or swap out hardware, making it efficient for occasional use. \n\n- Running Linux in a PaaS cloud environment would consume bandwidth, which the user has limited access to. \n- A swappable drive bay would require hardware swaps and reboots, which is inconvenient. \n- A dual boot system would also require restarting the computer each time Linux is needed."
    },
    {
        "question": "A user connects a laptop that is running Windows 10 to a docking station with external monitors when working at a desk. The user would like to close the laptop when it is docked, but the user reports it goes to sleep when it is closed. Which of the following is the BEST solution to prevent the laptop from going to sleep when it is closed and on the docking station?",
        "options": [
            "Within the Power Options of the Control Panel utility, click the Change Plan Settings button for the enabled power plan and select Put the Computer to Sleep under the Plugged In category to Never.",
            "Within the Power Options of the Control Panel utility, click the Change Plan Settings button for the enabled power plan and select Put the Computer to Sleep under the On Battery category to Never.",
            "Within the Power Options of the Control Panel utility, select the option Choose When to Turn Off the Display and select Turn Off the Display under the Plugged In category to Never.",
            "Within the Power Options of the Control Panel utility, select the option Choose What Closing the Lid Does and select When I Close the Lid under the Plugged In category to Do Nothing."
        ],
        "correct_answer": [4],
        "description": "The correct answer is Within the Power Options of the Control Panel utility, select the option Choose What Closing the Lid Does and select When I Close the Lid under the Plugged In category to Do Nothing. This setting allows the user to close the laptop lid without putting it to sleep, ensuring it continues to function while docked. \n\n- Changing sleep settings for the entire power plan or display settings won't specifically prevent the laptop from sleeping when closed."
    },
    {
        "question": "A user attempts to open some files, but a message appears stating that the files are encrypted. The user was able to access these files before without receiving this message, and no changes have been made within the company. Which of the following has infected the computer?",
        "options": [
            "Cryptominer",
            "Phishing",
            "Ransomware",
            "Keylogger"
        ],
        "correct_answer": [3],
        "description": "The correct answer is Ransomware. Ransomware encrypts files and demands a ransom to decrypt them, which aligns with the user's experience of suddenly finding their files inaccessible. \n\n- A cryptominer would use system resources to mine cryptocurrency but would not encrypt files. \n- Phishing is a social engineering attack and typically does not involve file encryption. \n- A keylogger tracks keystrokes, but it does not encrypt files."
    },
{
    "question": "A technician is replacing the processor in a desktop computer. Prior to opening the computer, the technician wants to ensure the internal components are protected. Which of the following safety procedures would BEST protect the components in the PC? (Choose two.)",
    "options": [
        "Utilizing an ESD strap",
        "Disconnecting the computer from the power source",
        "Placing the PSU in an antistatic bag",
        "Ensuring proper ventilation",
        "Removing dust from the ventilation fans",
        "Ensuring equipment is grounded"
    ],
    "correct_answer": [1, 2],
    "description": "The correct answers are Utilizing an ESD strap and Disconnecting the computer from the power source. Using an ESD strap prevents electrostatic discharge from damaging sensitive components during handling, and disconnecting the power source ensures that no electrical current is flowing, which is critical for safety. \n\n- Ensuring equipment is grounded is important but secondary to directly disconnecting the power source. \n- Placing the PSU in an antistatic bag is unnecessary during the processor replacement. \n- Proper ventilation and removing dust are general maintenance practices but not directly related to component protection during the replacement."
},


#61-70


{
  "question": "A user wants to set up speech recognition on a PC. In which of the following Windows Settings tools can the user enable this option?",
  "options": [
    "Language",
    "System",
    "Personalization",
    "Ease of Access"
  ],
  "correct_answer": [4],
  "description": "The correct answer is Ease of Access. The 'Ease of Access' settings in Windows are specifically designed for accessibility options, including speech recognition. This is where users can enable and configure features that help interact with the computer more easily, including speech-to-text and voice commands.\n\n- 'Language' settings are used to manage the system’s language packs, input methods, and other regional formats but do not directly control accessibility features like speech recognition.\n- 'System' settings control hardware and power configurations, not speech recognition.\n- 'Personalization' settings relate to the appearance of the desktop, such as wallpaper and theme customization."
},
{
  "question": "A user reports that antivirus software indicates a computer is infected with viruses. The user thinks this happened while browsing the internet. The technician does not recognize the interface with which the antivirus message is presented. Which of the following is the NEXT step the technician should take?",
  "options": [
    "Shut down the infected computer and swap it with another computer.",
    "Investigate what the interface is and what triggered it to pop up.",
    "Proceed with initiating a full scan and removal of the viruses using the presented interface.",
    "Call the phone number displayed in the interface of the antivirus removal tool."
  ],
  "correct_answer": [2],
  "description": "The correct answer is to investigate what the interface is and what triggered it to pop up. The unfamiliar antivirus interface suggests that it could be a form of scareware or rogue software. It’s important to identify whether the message is legitimate or part of a scam before taking further action.\n\n- Shutting down the computer and swapping it is premature as it doesn't resolve the issue or verify the nature of the threat.\n- Proceeding with a scan from an unverified interface could potentially cause more harm if it’s not a legitimate antivirus tool.\n- Calling the phone number in the interface could lead to a phishing scam or other fraudulent activity."
},

{
  "question": "A technician found that an employee is mining cryptocurrency on a work desktop. The company has decided that this action violates its guidelines. Which of the following should be updated to reflect this new requirement?",
  "options": [
    "MDM",
    "EULA",
    "IRP",
    "AUP"
  ],
  "correct_answer": [4],
  "description": "The correct answer is AUP (Acceptable Use Policy). The AUP outlines acceptable and unacceptable activities for company resources. If cryptocurrency mining is now prohibited, this policy must be updated to reflect the new guidelines.\n\n- MDM (Mobile Device Management) is used for managing and securing mobile devices but wouldn’t directly address unauthorized use of desktops.\n- EULA (End User License Agreement) governs software licensing terms and is not relevant here.\n- IRP (Incident Response Plan) deals with how to respond to security incidents, not usage violations."
},

{
  "question": "An organization is centralizing support functions and requires the ability to support a remote user's desktop. Which of the following technologies will allow a technician to see the issue along with the user?",
  "options": [
    "RDP",
    "VNC",
    "SSH",
    "VPN"
  ],
  "correct_answer": [2],
  "description": "The correct answer is VNC (Virtual Network Computing). VNC allows the technician to remotely view and control the user’s desktop, making it ideal for remote support, where both the user and the technician can see the issue.\n\n- RDP (Remote Desktop Protocol) is also a remote desktop solution but typically locks out the user's session while the technician is controlling it.\n- SSH (Secure Shell) is used for secure command-line access and is not suitable for desktop support.\n- VPN (Virtual Private Network) provides secure access to a network but doesn’t facilitate remote control or desktop sharing."
},

{
  "question": "Which of the following provide the BEST way to secure physical access to a data center server room? (Choose two.)",
  "options": [
    "Biometric lock",
    "Badge reader",
    "USB token",
    "Video surveillance",
    "Locking rack",
    "Access control vestibule"
  ],
  "correct_answer": [1, 2],
  "description": "The correct answers are Biometric lock and Badge reader. A biometric lock ensures that only authorized individuals can enter by using unique physical characteristics like fingerprints or retinal scans, making it highly secure against unauthorized access. A badge reader adds another layer of access control by requiring personnel to swipe their security badges, logging entries and preventing unauthorized access.\n\n- USB tokens provide logical access to computers or networks, not physical security to rooms. \n- Video surveillance monitors activity but does not actively prevent unauthorized access. \n- Locking racks secure individual servers but do not control access to the entire server room. \n- An access control vestibule, while secure, is not as commonly deployed as biometric locks and badge readers in standard data center environments."
},

{
  "question": "Which of the following Wi-Fi protocols is the MOST secure?",
  "options": [
    "WPA3",
    "WPA-AES",
    "WEP",
    "WPA-TKIP"
  ],
  "correct_answer": [1],
  "description": "The correct answer is WPA3. WPA3 is the latest Wi-Fi security protocol, offering stronger encryption and more secure key exchanges, making it the most secure option available.\n\n- WPA-AES is more secure than WPA-TKIP but less advanced than WPA3.\n- WEP is an outdated and easily compromised protocol.\n- WPA-TKIP is also less secure compared to WPA3, as it uses older encryption standards."
},


{
  "question": "A department has the following technical requirements for a new application: Quad-core processor, 250GB hard drive space, 6GB of RAM, and touch screens. The company plans to upgrade from a 32-bit Windows OS to a 64-bit OS. Which of the following will the company be able to fully take advantage of after the upgrade?",
  "options": [
    "CPU",
    "Hard drive",
    "RAM",
    "Touch screen"
  ],
  "correct_answer": [3],
  "description": "The correct answer is RAM. A 64-bit OS can fully utilize more than 4GB of RAM, which is the maximum limit for a 32-bit system. After the upgrade, the company will be able to take full advantage of the 6GB of RAM.\n\n- The CPU is already fully utilized regardless of the operating system's architecture. \n- The hard drive capacity is not affected by switching from 32-bit to 64-bit. \n- Touch screens do not require a 64-bit OS to function."
},
{
  "question": "A user is unable to log in to the domain with a desktop PC, but a laptop PC is working properly on the same network. A technician logs in to the desktop PC with a local account but is unable to browse to the secure intranet site to get troubleshooting tools. Which of the following is the MOST likely cause of the issue?",
  "options": [
    "Time drift",
    "Dual in-line memory module failure",
    "Application crash",
    "Filesystem errors"
  ],
  "correct_answer": [1],
  "description": "The correct answer is Time drift. If the time on the desktop PC is not synchronized with the domain, it could cause authentication issues and prevent access to the network and intranet resources. \n\n- A memory failure would likely cause crashes or performance issues but wouldn’t explain the inability to log in to the domain. \n- An application crash might affect a specific program, but not network login or intranet access. \n- Filesystem errors could cause some system instability but are less likely to prevent domain logins specifically."
},
{
  "question": "A user reports that a workstation is operating sluggishly. Several other users operate on the same workstation and have reported that the workstation is operating normally. The systems administrator has validated that the workstation functions normally. Which of the following steps should the systems administrator most likely attempt NEXT?",
  "options": [
    "Increase the paging file size.",
    "Run the chkdsk command.",
    "Rebuild the user's profile.",
    "Add more system memory.",
    "Defragment the hard drive."
  ],
  "correct_answer": [3],
  "description": "The correct answer is Rebuild the user's profile. If the workstation operates normally for other users, the issue may be with the specific user profile. Rebuilding the profile can resolve any profile corruption or settings misconfigurations that are causing the slowdown.\n\n- Increasing the paging file size or adding more memory might help with performance issues, but these would affect all users, not just one. \n- Running chkdsk and defragmenting the hard drive could help with disk-related issues, but they are less likely to explain why only one user is experiencing problems."
},
{
  "question": "A technician is setting up a desktop computer in a small office. The user will need to access files on a drive shared from another desktop on the network. Which of the following configurations should the technician employ to achieve this goal?",
  "options": [
    "Configure the network as private.",
    "Enable a proxy server.",
    "Grant the network administrator role to the user.",
    "Create a shortcut to public documents."
  ],
  "correct_answer": [1],
  "description": "The correct answer is Configure the network as private. A private network allows for file sharing and communication between devices on the same network, ensuring that the shared drive can be accessed securely.\n\n- Enabling a proxy server is unrelated to file sharing; it is used for routing traffic through an intermediary server. \n- Granting network administrator privileges is unnecessary for accessing a shared drive. \n- Creating a shortcut to public documents won’t allow the user to access shared drives on other computers."
},


#71-80



  {
    "question": "Which of the following is a proprietary Cisco AAA protocol?",
    "options": [
      "TKIP",
      "AES",
      "RADIUS",
      "TACACS+"
    ],
    "correct_answer": [4],
    "description": "The correct answer is TACACS+. TACACS+ (Terminal Access Controller Access-Control System Plus) is a proprietary Cisco protocol used for AAA (Authentication, Authorization, and Accounting) services. \n\n- RADIUS (Remote Authentication Dial-In User Service) is an open standard and not proprietary to Cisco. \n- TKIP (Temporal Key Integrity Protocol) and AES (Advanced Encryption Standard) are encryption protocols, not AAA protocols."
  },
  {
    "question": "A technician is asked to resize a partition on the internal storage drive of a computer running macOS. Which of the following tools should the technician use to accomplish this task?",
    "options": [
      "Console",
      "Disk Utility",
      "Time Machine",
      "FileVault"
    ],
    "correct_answer": [2],
    "description": "The correct answer is Disk Utility. Disk Utility is a built-in macOS application that allows users to manage disks and partitions, including resizing them. \n\n- Console is used for viewing system logs, not for managing partitions. \n- Time Machine is a backup tool, while FileVault is for disk encryption, neither of which can resize partitions."
  },
  {
    "question": "A desktop specialist needs to prepare a laptop running Windows 10 for a newly hired employee. Which of the following methods should the technician use to refresh the laptop?",
    "options": [
      "Internet-based upgrade",
      "Repair installation",
      "Clean install",
      "USB repair",
      "In-place upgrade"
    ],
    "correct_answer": [3],
    "description": "The correct answer is Clean install. A clean install refreshes the system by completely removing existing data and installing a fresh copy of Windows 10, ensuring that the new employee starts with a clean slate. \n\n- An Internet-based upgrade or in-place upgrade retains existing data, which is not ideal for preparing a new device. \n- Repair installation and USB repair are meant for fixing issues, not preparing a laptop for a new user."
  },
  {
    "question": "A user reports that a PC seems to be running more slowly than usual. A technician checks system resources, but disk, CPU, and memory usage seem to be fine. The technician sees that GPU temperature is extremely high. Which of the following types of malware is MOST likely to blame?",
    "options": [
      "Spyware",
      "Cryptominer",
      "Ransomware",
      "Boot sector virus"
    ],
    "correct_answer": [2],
    "description": "The correct answer is Cryptominer. Cryptominers use excessive GPU resources to mine cryptocurrency, which can cause the GPU temperature to spike and the system to slow down. \n\n- Spyware typically gathers information without causing significant resource usage. \n- Ransomware encrypts files and is not primarily resource-intensive. \n- Boot sector viruses affect startup processes rather than GPU performance."
  },
  {
    "question": "A user is experiencing frequent malware symptoms on a Windows workstation. The user has tried several times to roll back the state, but the malware persists. Which of the following would MOST likely resolve the issue?",
    "options": [
      "Quarantining system files",
      "Reimaging the workstation",
      "Encrypting the hard drive",
      "Disabling TLS 1.0 support"
    ],
    "correct_answer": [2],
    "description": "The correct answer is Reimaging the workstation. Reimaging restores the workstation to a clean state, removing all malware and returning the system to a functioning condition. \n\n- Quarantining files may not eliminate persistent malware. \n- Encrypting the hard drive is a security measure but does not remove malware. \n- Disabling TLS 1.0 support pertains to network security, not malware removal."
  },
  {
    "question": "A change advisory board did not approve a requested change due to the lack of alternative actions if implementation failed. Which of the following should be updated before requesting approval again?",
    "options": [
      "Scope of change",
      "Risk level",
      "Rollback plan",
      "End user acceptance"
    ],
    "correct_answer": [3],
    "description": "The correct answer is Rollback plan. A rollback plan outlines how to revert to the previous state in case the change fails, which is crucial for gaining approval. \n\n- The scope of change and risk level are important but do not specifically address the board's concerns about failure management. \n- End user acceptance is necessary but not directly related to the change's implementation risks."
  },
  {
  "question": "A technician is setting up a new laptop. The company's security policy states that users cannot install virtual machines. Which of the following should the technician implement to prevent users from enabling virtual technology on their laptops?",
  "options": [
    "UEFI password",
    "Secure boot",
    "Account lockout",
    "Restricted user permissions"
  ],
  "correct_answer": [1],
  "description": "The correct answer is UEFI password. By implementing a UEFI password, the technician can prevent users from changing the BIOS settings, including enabling virtualization technology, thus enforcing the company's security policy. \n\n- Secure boot is a feature that helps ensure that the device boots using only trusted software but does not specifically prevent virtual machine installations. \n- Account lockout is related to login security and does not control software installation. \n- Restricted user permissions can limit software installation but may not completely prevent enabling virtualization features."
    },
  {
    "question": "During a recent flight, an executive unexpectedly received several dog and cat pictures while trying to watch a movie via in-flight Wi-Fi on an iPhone. The executive has no records of any contacts sending pictures like these and has not seen these pictures before. To BEST resolve this issue, the executive should:",
    "options": [
      "set AirDrop so that transfers are only accepted from known contacts.",
      "completely disable all wireless systems during the flight.",
      "discontinue using iMessage and only use secure communication applications.",
      "only allow messages and calls from saved contacts."
    ],
    "correct_answer": [1],
    "description": "The correct answer is set AirDrop so that transfers are only accepted from known contacts. This setting prevents unsolicited file transfers from strangers, protecting the executive's device from unwanted content. \n\n- Completely disabling all wireless systems is excessive and would prevent any communication. \n- Discontinuing iMessage does not address the issue of random file transfers. \n- Allowing messages and calls only from saved contacts does not prevent file transfers via AirDrop."
  },
  {
    "question": "A technician receives a call from a user who is unable to open Outlook. The user states that Outlook worked fine yesterday, but the computer may have restarted sometime overnight. Which of the following is the MOST likely reason Outlook has stopped functioning?",
    "options": [
      "Spam filter installation",
      "Invalid registry settings",
      "Malware infection",
      "Operating system update"
    ],
    "correct_answer": [4],
    "description": "The correct answer is Operating system update. If the computer restarted due to an OS update, it may have affected the functionality of Outlook, leading to the reported issue. \n\n- A spam filter installation typically does not prevent Outlook from opening. \n- Invalid registry settings are possible but less likely to occur spontaneously. \n- While malware infection is a possibility, it is less common compared to issues arising from OS updates."
  },
  {
    "question": "A bank would like to enhance building security in order to prevent vehicles from driving into the building while also maintaining easy access for customers. Which of the following BEST addresses this need?",
    "options": [
      "Guards",
      "Bollards",
      "Motion sensors",
      "Access control vestibule"
    ],
    "correct_answer": [2],
    "description": "The correct answer is Bollards. Bollards are short, sturdy posts that can effectively prevent vehicles from entering specific areas while allowing pedestrians to access the building easily. \n\n- Guards provide security but do not physically prevent vehicle access. \n- Motion sensors can alert to unauthorized access but do not stop vehicles. \n- An access control vestibule is more suitable for managing foot traffic than vehicle access."
  },

#81-90

    {
      "question": "After a company installed a new SOHO router, customers were unable to access the company-hosted public website. Which of the following will MOST likely allow customers to access the website?",
      "options": [
        "Port forwarding",
        "Firmware updates",
        "IP filtering",
        "Content filtering"
      ],
      "correct_answer": [1],
      "description": "The correct answer is Port forwarding. By configuring port forwarding on the router, incoming traffic to specific ports can be redirected to the correct internal servers, allowing customers to access the website. \n\n- **Firmware updates** might improve router functionality but won't resolve access issues unless specifically related to bugs. \n- **IP filtering** could block legitimate traffic if not set up correctly, while **content filtering** is more about controlling access to specific types of content rather than allowing access to the website."
    },
    {
      "question": "Which of the following is the proper way for a technician to dispose of used printer consumables?",
      "options": [
        "Proceed with the custom manufacturer's procedure.",
        "Proceed with the disposal of consumables in standard trash receptacles.",
        "Empty any residual Ink or toner from consumables before disposing of them in a standard recycling bin.",
        "Proceed with the disposal of consumables in standard recycling bins."
      ],
      "correct_answer": [1],
      "description": "The correct answer is to proceed with the custom manufacturer's procedure. Manufacturers often have specific guidelines for disposing of their products to ensure environmental safety and compliance with regulations. \n\n- Disposing of consumables in standard trash receptacles can be harmful to the environment. \n- Emptying residual ink or toner before disposal may not be sufficient if the materials are not properly recycled. \n- Using standard recycling bins without knowing if they are suitable for these materials could also lead to environmental issues."
    },
    {
      "question": "An Android user reports that when attempting to open the company's proprietary mobile application, it immediately closes. The user states that the issue persists, even after rebooting the phone. The application contains critical information that cannot be lost. Which of the following steps should a systems administrator attempt FIRST?",
      "options": [
        "Uninstall and reinstall the application.",
        "Reset the phone to factory settings.",
        "Install an alternative application with similar functionality.",
        "Clear the application cache."
      ],
      "correct_answer": [4],
      "description": "The correct answer is Clear the application cache. This step is often the quickest and least disruptive method to resolve application issues, as it removes temporary data that may be causing the app to malfunction. \n\n- Uninstalling and reinstalling the application could result in data loss if not backed up. \n- Resetting the phone to factory settings is too drastic and may lead to data loss. \n- Installing an alternative application may not address the issue with the original app."
    },
    {
      "question": "A wireless network is set up, but it is experiencing some interference from other nearby SSIDs. Which of the following can BEST resolve the interference?",
      "options": [
        "Changing channels",
        "Modifying the wireless security",
        "Disabling the SSID broadcast",
        "Changing the access point name"
      ],
      "correct_answer": [1],
      "description": "The correct answer is Changing channels. By selecting a less crowded channel, the wireless network can minimize interference from nearby SSIDs, leading to a more stable connection. \n\n- Modifying wireless security settings does not address interference directly. \n- Disabling SSID broadcast may enhance privacy but does not reduce interference. \n- Changing the access point name does not affect performance."
    },
    {
      "question": "A user rotates a cell phone horizontally to read emails, but the display remains vertical, even though the settings indicate autorotate is on. Which of the following will MOST likely resolve the issue?",
      "options": [
        "Recalibrating the magnetometer",
        "Recalibrating the compass",
        "Recalibrating the digitizer",
        "Recalibrating the accelerometer"
      ],
      "correct_answer": [4],
      "description": "The correct answer is Recalibrating the accelerometer. The accelerometer detects the orientation of the device, and recalibrating it can resolve issues with autorotation not functioning properly. \n\n- Recalibrating the magnetometer and compass relates to location services rather than screen orientation. \n- Recalibrating the digitizer affects touch input rather than display rotation."
    },
    {
      "question": "A Microsoft Windows PC needs to be set up for a user at a large corporation. The user will need access to the corporate domain to access email and shared drives. Which of the following versions of Windows would a technician MOST likely deploy for the user?",
      "options": [
        "Windows Enterprise Edition",
        "Windows Professional Edition",
        "Windows Server Standard Edition",
        "Windows Home Edition"
      ],
      "correct_answer": [2],
      "description": "The correct answer is Windows Professional Edition. This version supports joining a domain, allowing the user access to corporate resources like email and shared drives. \n\n- Windows Enterprise Edition is often used for larger organizations but is typically available through volume licensing. \n- Windows Server Standard Edition is designed for server environments, not individual workstations. \n- Windows Home Edition does not support domain joining."
    },
    {
      "question": "An Android user contacts the help desk because a company smartphone failed to complete a tethered OS update. A technician determines there are no error messages on the device. Which of the following should the technician do NEXT?",
      "options": [
        "Verify all third-party applications are disabled.",
        "Determine if the device has adequate storage available.",
        "Check if the battery is sufficiently charged.",
        "Confirm a strong internet connection is available using Wi-Fi or cellular data."
      ],
      "correct_answer": [2],
      "description": "The correct answer is Determine if the device has adequate storage available. Insufficient storage can prevent OS updates from completing, so checking this is crucial. \n\n- Verifying that third-party applications are disabled may not be necessary, as they may not directly impact the update. \n- Checking the battery level is important, but if there are no error messages, storage is more likely the issue. \n- Confirming a strong internet connection is helpful but does not address the potential storage limitation."
    },
    {
      "question": "A technician just completed a Windows 10 installation on a PC that has a total of 16GB of RAM. The technician notices the Windows OS has only 4GB of RAM available for use. Which of the following explains why the OS can only access 4GB of RAM?",
      "options": [
        "The UEFI settings need to be changed.",
        "The RAM has compatibility issues with Windows 10.",
        "Some of the RAM is defective.",
        "The newly installed OS is x86."
      ],
      "correct_answer": [4],
      "description": "The correct answer is The newly installed OS is x86. An x86 version of Windows can only address up to 4GB of RAM, while a 64-bit version can utilize the full 16GB. \n\n- Changing UEFI settings might not be necessary if the OS itself is limiting access due to its architecture. \n- Compatibility issues with Windows 10 are unlikely if the RAM is supported. \n- Defective RAM would typically result in no available RAM rather than a specific limitation."
    },
    {
      "question": "A call center handles inquiries into billing issues for multiple medical facilities. A security analyst notices that call center agents often walk away from their workstations, leaving patient data visible for anyone to see. Which of the following should a network administrator do to BEST prevent data theft within the call center?",
      "options": [
        "Encrypt the workstation hard drives.",
        "Lock the workstations after five minutes of inactivity.",
        "Install privacy screens.",
        "Log off the users when their workstations are not in use."
      ],
      "correct_answer": [2],
      "description": "The correct answer is Lock the workstations after five minutes of inactivity. This measure automatically secures the workstation and prevents unauthorized access to sensitive patient data when agents step away. \n\n- Encrypting hard drives protects data at rest but does not prevent unauthorized viewing when the workstation is active. \n- Privacy screens can deter prying eyes but do not secure the workstation. \n- Logging off users may be disruptive and reduce productivity."
    },
    {
      "question": "An organization's Chief Financial Officer (CFO) is concerned about losing access to very sensitive, legacy, unmaintained PII on a workstation if a ransomware outbreak occurs. The CFO has a regulatory requirement to retain this data for many years. Which of the following backup methods would BEST meet the requirements?",
      "options": [
        "A daily, incremental backup that is saved to the corporate file server",
        "An additional, secondary hard drive in a mirrored RAID configuration",
        "A full backup of the data that is stored off site in cold storage",
        "Weekly, differential backups that are stored in a cloud-hosting provider"
      ],
      "correct_answer": [3],
      "description": "The correct answer is A full backup of the data that is stored off site in cold storage. This method provides a secure and long-term solution for retaining sensitive data while protecting it from ransomware attacks. \n\n- Daily incremental backups may not be sufficient if the primary data is compromised before the backup. \n- Mirrored RAID configurations offer redundancy but do not protect against ransomware if the primary data is attacked. \n- Weekly differential backups stored in the cloud may not provide the longevity or security required for very sensitive data."
    },

#90-100

    {
      "question": "A police officer often leaves a workstation for several minutes at a time. Which of the following is the BEST way the officer can secure the workstation quickly when walking away?",
      "options": [
        "Use a key combination to lock the computer when leaving.",
        "Ensure no unauthorized personnel are in the area.",
        "Configure a screensaver to lock the computer automatically after approximately 30 minutes of inactivity.",
        "Turn off the monitor to prevent unauthorized visibility of information."
      ],
      "correct_answer": [1],
      "description": "The correct answer is Use a key combination to lock the computer when leaving. This is the quickest way to secure the workstation, ensuring that unauthorized users cannot access the system immediately. \n\n- Ensuring no unauthorized personnel are in the area does not actively prevent access. \n- Configuring a screensaver to lock the computer after 30 minutes provides a delayed response and may not address immediate concerns. \n- Turning off the monitor does not prevent access to the workstation itself."
    },
    {
  "question": "While browsing a website, a staff member received a message that the website could not be trusted. Shortly afterward, several other colleagues reported the same issue across numerous other websites. Remote users who were not connected to corporate resources did not have any issues. Which of the following is MOST likely the cause of this issue?",
  "options": [
    "A bad antivirus signature update was installed.",
    "A router was misconfigured and was blocking traffic.",
    "An upstream internet service provider was flapping.",
    "The time or date was not in sync with the website."
  ],
  "correct_answer": [4],
  "description": "The correct answer is The time or date was not in sync with the website. If the local time or date on the users' devices is incorrect, it can cause SSL/TLS certificates to appear invalid, leading to the warning messages about untrusted websites. \n\n- A bad antivirus signature update would typically not cause widespread issues across multiple sites. \n- A misconfigured router usually affects all users and not just specific segments. \n- An upstream ISP issue would likely affect all users and not differentiate based on connection type."
     },
    {
      "question": "While browsing a website, a staff member received a message that the website could not be trusted. Shortly afterward, several other colleagues reported the same issue across numerous other websites. Remote users who were not connected to corporate resources did not have any issues. Which of the following is MOST likely the cause of this issue?",
      "options": [
        "A bad antivirus signature update was installed.",
        "A router was misconfigured and was blocking traffic.",
        "An upstream internet service provider was flapping.",
        "The time or date was not in sync with the website."
      ],
      "correct_answer": [1],
      "description": "The correct answer is A bad antivirus signature update was installed. This can cause legitimate websites to be flagged as untrusted due to incorrect signatures. \n\n- A misconfigured router typically affects all users, not just those connected to corporate resources. \n- An upstream ISP issue would likely affect all users, while time/date sync problems would typically only affect HTTPS connections."
    },
    {
      "question": "Which of the following data is MOST likely to be regulated?",
      "options": [
        "Name in a phone book",
        "Name on a medical diagnosis",
        "Name on a job application",
        "Name on an employer's website"
      ],
      "correct_answer": [2],
      "description": "The correct answer is Name on a medical diagnosis. This data is protected under regulations such as HIPAA, which safeguard personal health information. \n\n- A name in a phone book and on a job application does not have the same level of protection. \n- Information on an employer's website is generally public and less likely to be regulated."
    },
    {
      "question": "A company is deploying mobile phones on a one-to-one basis, but the IT manager is concerned that users will root/jailbreak their phones. Which of the following technologies can be implemented to prevent this issue?",
      "options": [
        "Signed system images",
        "Antivirus",
        "SSO",
        "MDM"
      ],
      "correct_answer": [4],
      "description": "The correct answer is MDM (Mobile Device Management). MDM solutions can enforce security policies and prevent users from rooting or jailbreaking their devices. \n\n- Signed system images help verify software integrity but do not prevent rooting. \n- Antivirus can protect against malware but does not specifically address jailbreaking. \n- SSO (Single Sign-On) is more about authentication than device security."
    },
    {
      "question": "A technician is setting up a conference room computer with a script that boots the application on log-in. Which of the following would the technician use to accomplish this task? (Choose two.)",
      "options": [
        "File Explorer",
        "Startup Folder",
        "System Information",
        "Programs and Features",
        "Task Scheduler",
        "Device Manager"
      ],
      "correct_answer": [2, 5],
      "description": "The correct answers are Startup Folder and Task Scheduler. The Startup Folder allows applications to launch automatically upon login, while Task Scheduler can be configured to run scripts at specific events, including user log-in. \n\n- File Explorer is a file management tool and does not directly facilitate application startup. \n- System Information, Programs and Features, and Device Manager do not relate to application launch on startup."
    },
    {
      "question": "A systems administrator needs to reset a user's password because the user forgot it. The systems administrator creates the new password and wants to further protect the user's account. Which of the following should the systems administrator do?",
      "options": [
        "Require the user to change the password at the next log-in",
        "Disallow the user from changing the password.",
        "Disable the account.",
        "Choose a password that never expires."
      ],
      "correct_answer": [1],
      "description": "The correct answer is Require the user to change the password at the next log-in. This ensures that the user has control over their password and that it is kept secure. \n\n- Disallowing the user from changing the password undermines security. \n- Disabling the account prevents access entirely, which is not a solution. \n- Choosing a password that never expires could lead to security risks."
    },
    {
      "question": "A technician downloaded software from the Internet that required the technician to scroll through a text box and at the end of the text box, click a button labeled Accept. Which of the following agreements is MOST likely in use?",
      "options": [
        "DRM",
        "NDA",
        "EULA",
        "MOU"
      ],
      "correct_answer": [3],
      "description": "The correct answer is EULA (End User License Agreement). This agreement outlines the terms under which the user is allowed to use the software. \n\n- DRM (Digital Rights Management) relates to copyright protection, not user agreement. \n- NDA (Non-Disclosure Agreement) is about confidentiality, and MOU (Memorandum of Understanding) is a less formal agreement between parties."
    },
    {
      "question": "Which of the following command-line tools will delete a directory?",
      "options": [
        "md",
        "del",
        "dir",
        "rd",
        "cd"
      ],
      "correct_answer": [4],
      "description": "The correct answer is rd (remove directory). This command is used in command-line interfaces to delete a directory. \n\n- md (make directory) creates a new directory. \n- del is used to delete files, not directories. \n- dir lists the contents of a directory, and cd changes the current directory."
    },
    {
      "question": "A technician is troubleshooting a computer with a suspected short in the power supply. Which of the following is the FIRST step the technician should take?",
      "options": [
        "Put on an ESD strap.",
        "Disconnect the power before servicing the PC.",
        "Place the PC on a grounded work bench.",
        "Place components on an ESD mat."
      ],
      "correct_answer": [2],
      "description": "The correct answer is Disconnect the power before servicing the PC. This is the safest first step to prevent electrical shock or further damage. \n\n- While wearing an ESD strap, placing the PC on a grounded workbench, and using an ESD mat are all good practices, they should occur after ensuring the power is disconnected."
    },

#101-110

  {
    "question": "A systems administrator is tasked with configuring desktop systems to use a new proxy server that the organization has added to provide content filtering. Which of the following Windows utilities is the BEST choice for accessing the necessary configuration to complete this goal?",
    "options": [
      "Security and Maintenance",
      "Network and Sharing Center",
      "Windows Defender Firewall",
      "Internet Options"
    ],
    "correct_answer": [4],
    "description": "The correct answer is Internet Options. Internet Options allows users to configure proxy settings under the Connections tab. \n\n- Security and Maintenance is used for general security and system health monitoring. \n- Network and Sharing Center is for managing network connections and settings, not proxy configurations. \n- Windows Defender Firewall manages firewall rules and security settings, but it doesn’t control proxy configurations."
  },
  {
    "question": "An analyst needs GUI access to server software running on a macOS server. Which of the following options provides the BEST way for the analyst to access the macOS server from the Windows workstation?",
    "options": [
      "RDP through RD Gateway",
      "Apple Remote Desktop",
      "SSH access with SSH keys",
      "VNC with username and password"
    ],
    "correct_answer": [4],
    "description": "The correct answer is VNC with username and password. VNC (Virtual Network Computing) provides a cross-platform way to remotely access a GUI on the macOS server from Windows. \n\n- RDP through RD Gateway works for Windows-to-Windows connections. \n- Apple Remote Desktop is a macOS-to-macOS tool, not compatible with Windows. \n- SSH access with SSH keys is for terminal-based access, not GUI access."
  },
  {
    "question": "Which of the following is an example of MFA?",
    "options": [
      "Fingerprint scan and retina scan",
      "Password and PIN",
      "Username and password",
      "Smart card and password"
    ],
    "correct_answer": [4],
    "description": "The correct answer is Smart card and password. MFA (Multi-Factor Authentication) requires two or more factors of different types. Smart cards are a possession-based factor, while passwords are knowledge-based, making this a valid MFA. \n\n- Fingerprint scan and retina scan are both biometric, and therefore the same type of factor. \n- Password and PIN are both knowledge-based, so this is not considered MFA. \n- Username and password are also both knowledge-based and do not satisfy MFA requirements."
  },
  {
    "question": "A user turns on a new laptop and attempts to log in to specialized software, but receives a message stating that the address is already in use. The user logs on to the old desktop and receives the same message. A technician checks the account and sees a comment that the user requires a specifically allocated address before connecting to the software. Which of the following should the technician do to MOST likely resolve the issue?",
    "options": [
      "Bridge the LAN connection between the laptop and the desktop.",
      "Set the laptop configuration to DHCP to prevent conflicts.",
      "Remove the static IP configuration from the desktop.",
      "Replace the network card in the laptop, as it may be defective."
    ],
    "correct_answer": [3],
    "description": "The correct answer is Remove the static IP configuration from the desktop. A static IP address assigned to both devices is likely causing a conflict, leading to connection issues. \n\n- Bridging the LAN connection between devices would not resolve the IP conflict issue. \n- Setting the laptop to DHCP could help, but it's better to address the static IP configuration causing the issue. \n- Replacing the network card is unnecessary unless there’s hardware failure, which isn't indicated here."
  },
  {
    "question": "A user is having issues with document-processing software on a Windows workstation. Other users that log in to the same device do not have the same issue. Which of the following should a technician do to remediate the issue?",
    "options": [
      "Roll back the updates.",
      "Increase the page file.",
      "Update the drivers.",
      "Rebuild the profile."
    ],
    "correct_answer": [4],
    "description": "The correct answer is Rebuild the profile. Since the issue is isolated to one user's profile, rebuilding it can resolve any corruption or misconfigurations within that profile. \n\n- Rolling back updates is unnecessary since the issue is not system-wide. \n- Increasing the page file won’t fix a profile-specific issue. \n- Updating drivers is unrelated to this problem since it’s profile-specific."
  },
  {
    "question": "Which of the following is the MOST basic version of Windows that includes BitLocker?",
    "options": [
      "Home",
      "Pro",
      "Enterprise",
      "Pro for Workstations"
    ],
    "correct_answer": [2],
    "description": "The correct answer is Pro. Windows Pro is the most basic version of Windows that supports BitLocker encryption. \n\n- Windows Home does not include BitLocker. \n- Enterprise and Pro for Workstations both include BitLocker, but they are more advanced and expensive than Pro."
  },
  {
    "question": "A Windows user reported that a pop-up indicated a security issue. During inspection, an antivirus system identified malware from a recent download, but it was unable to remove the malware. Which of the following actions would be BEST to remove the malware while also preserving the user's files?",
    "options": [
      "Run the virus scanner in an administrative mode.",
      "Reinstall the operating system.",
      "Reboot the system in safe mode and rescan.",
      "Manually delete the infected files."
    ],
    "correct_answer": [3],
    "description": "The correct answer is Reboot the system in safe mode and rescan. Safe mode starts the system with minimal services, allowing the antivirus to scan and remove malware that may be protected during normal operation. \n\n- Running the virus scanner in administrative mode may not bypass active malware protections. \n- Reinstalling the OS is drastic and would not preserve the user’s files. \n- Manually deleting files is risky and may not remove all malware components."
  },
  {
    "question": "A technician is installing a new business application on a user's desktop computer. The machine is running Windows 10 Enterprise 32-bit operating system. Which of the following files should the technician execute in order to complete the installation?",
    "options": [
      "Installer_x64.exe",
      "Installer_Files.zip",
      "Installer_32.msi",
      "Installer_x86.exe",
      "Installer_Win10Enterprise.dmg"
    ],
    "correct_answer": [4],
    "description": "The correct answer is Installer_x86.exe. Since the machine is running a 32-bit operating system, an x86 installer is compatible. \n\n- Installer_x64.exe is designed for 64-bit operating systems and won’t work on a 32-bit system. \n- Installer_Files.zip is a compressed archive and not an executable. \n- Installer_32.msi might be an installer, but .exe files are more commonly used for Windows software installations. \n- Installer_Win10Enterprise.dmg is a macOS installation file, not for Windows."
  },
  {
    "question": "A user calls the help desk to report potential malware on a computer. The anomalous activity began after the user clicked a link to a free gift card in a recent email. The technician asks the user to describe any unusual activity, such as slow performance, excessive pop-ups, and browser redirections. Which of the following should the technician do NEXT?",
    "options": [
      "Advise the user to run a complete system scan using the OS anti-malware application.",
      "Guide the user to reboot the machine into safe mode and verify whether the anomalous activities are still present.",
      "Have the user check for recently installed applications and outline those installed since the link in the email was clicked.",
      "Instruct the user to disconnect the Ethernet connection to the corporate network."
    ],
    "correct_answer": [4],
    "description": "The correct answer is Instruct the user to disconnect the Ethernet connection to the corporate network. Disconnecting the computer from the network helps prevent any malware from spreading to other devices in the network. \n\n- Running a scan can help identify the issue, but it is important to first isolate the infected machine from the network. \n- Rebooting in safe mode can be helpful, but isolation is the immediate priority. \n- Checking for recently installed applications is part of identifying the issue but should come after disconnecting the network."
  },
  {
    "question": "A technician is setting up a new laptop for an employee who travels. Which of the following is the BEST security practice for this scenario?",
    "options": [
      "PIN-based login",
      "Quarterly password changes",
      "Hard drive encryption",
      "A physical laptop lock"
    ],
    "correct_answer": [3],
    "description": "The correct answer is Hard drive encryption. For a traveling employee, encryption ensures that sensitive data on the laptop is protected even if the device is lost or stolen. \n\n- A PIN-based login offers minimal security compared to encryption. \n- Quarterly password changes are important but do not offer immediate protection in the case of theft. \n- A physical laptop lock can deter theft but does not protect the data if the laptop is compromised."
  },

#111-120


  {
    "question": "A technician is troubleshooting a lack of outgoing audio on a third-party Windows 10 VoIP application. The PC uses a USB microphone connected to a powered hub. The technician verifies the microphone works on the PC using Voice Recorder. Which of the following should the technician do to solve the issue?",
    "options": [
      "Remove the microphone from the USB hub and plug it directly into a USB port on the PC.",
      "Enable the microphone under Windows Privacy settings to allow desktop applications to access it.",
      "Delete the microphone from Device Manager and scan for new hardware.",
      "Replace the USB microphone with one that uses a traditional 3.5mm plug."
    ],
    "correct_answer": [2],
    "description": "The correct answer is Enable the microphone under Windows Privacy settings to allow desktop applications to access it. This solution is appropriate because Windows privacy settings often block certain applications from using devices like microphones, especially when dealing with third-party software. \n\n- Removing the microphone from the USB hub and plugging it directly into the PC is unlikely to resolve a software permissions issue, although it could be worth trying if hardware issues were suspected. \n- Deleting the microphone from Device Manager may solve issues related to driver conflicts but doesn't address privacy settings. \n- Replacing the USB microphone with one that uses a 3.5mm plug would only be necessary if hardware issues were at fault, which isn’t indicated here."
  },
  {
    "question": "A user who is unable to connect to the network submits a help desk ticket. The assigned help desk technician inquires about whether any recent changes have been made. The user reports there is construction activity in the surrounding offices. The help desk technician proceeds to ping the user's desktop, which does not respond. Which of the following is the MOST likely cause of this issue?",
    "options": [
      "A duplicate IP address has been issued to the user's desktop.",
      "The HDD of the OS is failing.",
      "The network cable has become disconnected.",
      "Malware has infected the system."
    ],
    "correct_answer": [3],
    "description": "The correct answer is The network cable has become disconnected. Given the construction activity, it's likely that physical network infrastructure has been affected, causing the cable to disconnect. \n\n- A duplicate IP address could cause network issues, but it wouldn’t typically prevent ping responses entirely. \n- HDD failure would impact the system as a whole, but wouldn’t be directly tied to the network connectivity. \n- Malware could be a cause, but there’s no indication of suspicious behavior related to infections."
  },
  {
    "question": "A user has been unable to access a website and has submitted a help desk ticket. The website has been verified to be online. Which of the following troubleshooting steps will MOST likely resolve the issue?",
    "options": [
      "Deleting the browser history",
      "Clearing the cache",
      "Enabling private mode browsing",
      "Enabling ad blocking"
    ],
    "correct_answer": [2],
    "description": "The correct answer is Clearing the cache. When a website isn’t loading properly, it’s often due to outdated or corrupt cache data stored by the browser. Clearing the cache forces the browser to retrieve fresh data. \n\n- Deleting browser history is unnecessary and would not resolve a caching issue. \n- Enabling private mode would bypass the cache but doesn’t address the underlying problem, which might persist in future sessions. \n- Ad blocking could potentially prevent some websites from loading correctly but isn’t the cause here."
  },
  {
    "question": "A desktop support technician is tasked with migrating several PCs from Windows 7 Pro to Windows 10 Pro. The technician must ensure files and user preferences are retained, must perform the operation locally, and should migrate one station at a time. Which of the following methods would be MOST efficient?",
    "options": [
      "Golden image",
      "Remote network install",
      "In-place upgrade",
      "Clean install"
    ],
    "correct_answer": [3],
    "description": "The correct answer is In-place upgrade. This method allows the operating system to be upgraded while keeping the user’s files and settings intact, meeting the technician’s requirements for local execution and preservation of preferences. \n\n- A golden image is ideal for large-scale deployments but overwrites existing settings and files. \n- A remote network install would require more infrastructure setup and doesn’t guarantee that individual settings are preserved. \n- A clean install would remove user preferences and files, which contradicts the requirements."
  },
  {
    "question": "The findings from a security audit indicate the risk of data loss from lost or stolen laptops is high. The company wants to reduce this risk with minimal impact to users who want to use their laptops when not on the network. Which of the following would BEST reduce this risk for Windows laptop users?",
    "options": [
      "Requiring strong passwords",
      "Disabling cached credentials",
      "Requiring MFA to sign on",
      "Enabling BitLocker on all hard drives"
    ],
    "correct_answer": [4],
    "description": "The correct answer is Enabling BitLocker on all hard drives. BitLocker encrypts the hard drive, protecting data even if the laptop is lost or stolen, with minimal impact on the user’s daily workflow. \n\n- Requiring strong passwords improves security, but does not protect data if the laptop is lost or stolen. \n- Disabling cached credentials can be inconvenient for users who frequently work offline. \n- MFA adds a layer of security but doesn’t protect local data if the laptop is compromised."
  },
  {
    "question": "A technician has been asked to set up a new wireless router with the best possible security. Which of the following should the technician implement?",
    "options": [
      "WPS",
      "TKIP",
      "WPA3",
      "WEP"
    ],
    "correct_answer": [3],
    "description": "The correct answer is WPA3. WPA3 is the latest and most secure wireless encryption protocol, offering improved security over previous standards. \n\n- WPS is a convenience feature that can be easily exploited, compromising network security. \n- TKIP is an outdated encryption method that is less secure than modern standards. \n- WEP is highly vulnerable to attacks and should not be used."
  },
  {
    "question": "After returning from vacation, a user is unable to connect to the network at the corporate office. Windows allows the user to log in; however, no internal or external websites are accessible when running a browser. The user's expected network shares are unreachable, and all websites attempted return the message, 'Hmm, we can't reach this page.' Which of the following is the MOST likely cause of this issue?",
    "options": [
      "The user's password expired while on vacation.",
      "The user clicked on a malicious email.",
      "The user connected to a captive portal while traveling.",
      "The user enabled airplane mode."
    ],
    "correct_answer": [4],
    "description": "The correct answer is The user enabled airplane mode. Airplane mode disables network connectivity, which would explain why the user can’t access internal or external websites or network shares. \n\n- Expired passwords would prevent the user from logging into Windows. \n- A malicious email could cause network issues, but there's no evidence of suspicious activity. \n- A captive portal would typically only affect the user while they were traveling and not in the office."
  },
  {
    "question": "Which of the following file extensions are commonly used to install applications on a macOS machine? (Choose three.)",
    "options": [
      ".mac",
      ".pkg",
      ".deb",
      ".dmg",
      ".msi",
      ".appx",
      ".app",
      ".apk"
    ],
    "correct_answer": [2, 4, 7],
    "description": "The correct answers are .pkg, .dmg, and .app. These file types are native to macOS. \n\n- .pkg is a macOS package file for installing software. \n- .dmg is a disk image file used to distribute macOS applications. \n- .app files are executable application files in macOS. \n\n- .mac is not a valid file extension. \n- .deb is a package format for Debian-based Linux systems. \n- .msi is used for Windows installations. \n- .appx is a Windows application package format. \n- .apk is for Android applications."
  },
  {
    "question": "A suite of security applications was installed a few days ago on a user's home computer. The user reports that the computer has been running slowly since the installation. The user notices the hard drive activity light is constantly solid. Which of the following should be checked FIRST?",
    "options": [
      "Services in Control Panel to check for overutilization",
      "Performance Monitor to check for resource utilization",
      "System File Checker to check for modified Windows files",
      "Event Viewer to identify errors"
    ],
    "correct_answer": [2],
    "description": "The correct answer is Performance Monitor to check for resource utilization. Performance Monitor allows the technician to identify which processes or applications are consuming system resources, potentially related to the new security software. \n\n- Checking services in Control Panel might help, but Performance Monitor offers a more detailed view of the issue. \n- System File Checker is for identifying system file issues, which is not indicated here. \n- Event Viewer is useful for checking errors, but won’t directly identify overutilization of resources."
  },
  {
    "question": "A field technician applied a Group Policy setting to all the workstations in the network. This setting forced the workstations to use a specific SNTP server. Users are unable to log in now. Which of the following is the MOST likely cause of this issue?",
    "options": [
      "The SNTP server is offline.",
      "A user changed the time zone on a local machine.",
      "The Group Policy setting has disrupted domain authentication on the system.",
      "The workstations and the authentication server have a system clock difference."
    ],
    "correct_answer": [4],
    "description": "The correct answer is The workstations and the authentication server have a system clock difference. A significant clock difference can cause authentication failures, as domain controllers rely on time synchronization. \n\n- The SNTP server being offline would cause time synchronization issues, but it’s the system clock difference that directly impacts domain authentication. \n- A user changing the time zone would only affect that individual system, not the entire network. \n- Group Policy disruptions could cause other issues but are less likely to affect login across all users."
  },

#121-130
    
  {
    "question": "A technician is setting up a backup method on a workstation that only requires two sets of tapes to restore. Which of the following would BEST accomplish this task?",
    "options": [
      "Differential backup",
      "Off-site backup",
      "Incremental backup",
      "Full backup"
    ],
    "correct_answer": [1],
    "description": "The correct answer is Differential backup. A differential backup stores the changes made since the last full backup, requiring only two sets of tapes: one for the last full backup and one for the latest differential. \n\n- An incremental backup would require more than two sets, as it stores only the changes since the last incremental backup. \n- Off-site backup refers to where the data is stored rather than the method used, so it doesn’t address the issue of using two tape sets. \n- A full backup stores everything, but restoring would only require one set of tapes, not two."
  },
  {
    "question": "A technician receives a call from a user who is on vacation. The user provides the necessary credentials and asks the technician to log in to the user's account and read a critical email that the user has been expecting. The technician refuses because this is a violation of the:",
    "options": [
      "acceptable use policy",
      "regulatory compliance requirements",
      "non-disclosure agreement",
      "incident response procedures"
    ],
    "correct_answer": [1],
    "description": "The correct answer is acceptable use policy. Most companies have policies in place that prohibit accessing another user's account, even with consent. Logging in on behalf of the user could compromise security and violate internal IT policies. \n\n- Regulatory compliance requirements focus on broader legal obligations but are not specific to internal login credentials in this context. \n- A non-disclosure agreement protects sensitive information but doesn’t govern account access. \n- Incident response procedures are for handling security incidents, not routine account access requests."
  },
  {
    "question": "A technician received a call stating that all files in a user's documents folder appear to be changed, and each of the files now has a .lock file extension. Which of the following actions is the FIRST step the technician should take?",
    "options": [
      "Run a live disk clone",
      "Run a full antivirus scan",
      "Use a batch file to rename the files",
      "Disconnect the machine from the network"
    ],
    "correct_answer": [4],
    "description": "The correct answer is Disconnect the machine from the network. This step helps to isolate the system from potentially spreading the ransomware or malware across the network. \n\n- Running a live disk clone is useful for preserving data but won’t stop the active threat. \n- Running a full antivirus scan can identify the malware, but the system should be isolated first to prevent further damage. \n- Using a batch file to rename the files won’t resolve the underlying infection and may complicate further analysis."
  },
  {
    "question": "A user is attempting to browse the internet using Internet Explorer. When trying to load a familiar web page, the user is unexpectedly redirected to an unfamiliar website. Which of the following would MOST likely solve the issue?",
    "options": [
      "Updating the operating system",
      "Changing proxy settings",
      "Reinstalling the browser",
      "Enabling port forwarding"
    ],
    "correct_answer": [2],
    "description": "The correct answer is Changing proxy settings. Unfamiliar website redirects are often caused by altered proxy settings, potentially due to malware. Changing these settings back to default should resolve the issue. \n\n- Updating the operating system might fix other security issues but won’t directly address a proxy setting problem. \n- Reinstalling the browser might work, but adjusting the proxy settings is more efficient in this case. \n- Port forwarding is related to network configurations and wouldn’t solve browser redirect issues."
  },
  {
    "question": "An administrator has submitted a change request for an upcoming server deployment. Which of the following must be completed before the change can be approved?",
    "options": [
      "Risk analysis",
      "Sandbox testing",
      "End user acceptance",
      "Lessons learned"
    ],
    "correct_answer": [1],
    "description": "The correct answer is Risk analysis. Before any significant changes, especially server deployments, assessing potential risks is critical to ensure the deployment doesn't negatively impact the business. \n\n- Sandbox testing is useful for validating the deployment but is not always required before approval. \n- End user acceptance typically comes after the deployment, during the testing phase. \n- Lessons learned are gathered after a change is implemented, not before."
  },
  {
    "question": "Which of the following is a consequence of end-of-life operating systems?",
    "options": [
      "Operating systems void the hardware warranty",
      "Operating systems cease to function",
      "Operating systems no longer receive updates",
      "Operating systems are unable to migrate data to the new operating system"
    ],
    "correct_answer": [3],
    "description": "The correct answer is Operating systems no longer receive updates. When an OS reaches end-of-life, it no longer gets security patches or updates, making it vulnerable to security risks. \n\n- End-of-life OSs don’t void hardware warranties, which are tied to physical components, not software. \n- End-of-life OSs will still function but become riskier to use. \n- Data migration between OSs is typically possible with proper tools and planning."
  },
  {
    "question": "A macOS user reports seeing a spinning round cursor on a program that appears to be frozen. Which of the following methods does the technician use to force the program to close in macOS?",
    "options": [
      "The technician presses the Ctrl+Alt+Del keys to open the Force Quit menu, selects the frozen application in the list, and clicks Force Quit",
      "The technician clicks on the frozen application and presses and holds the Esc key on the keyboard for 10 seconds which causes the application to force quit",
      "The technician opens Finder, navigates to the Applications folder, locates the application that is frozen in the list, right-clicks on the application, and selects the Force Quit option",
      "The technician opens the Apple icon menu, selects Force Quit, selects the frozen application in the list, and clicks Force Quit"
    ],
    "correct_answer": [4],
    "description": "The correct answer is The technician opens the Apple icon menu, selects Force Quit, selects the frozen application in the list, and clicks Force Quit. This is the proper procedure for forcing an unresponsive application to close on macOS. \n\n- Ctrl+Alt+Del is a Windows shortcut and does not apply to macOS. \n- Holding the Esc key is not a macOS method for closing applications. \n- Using Finder does not offer an option to directly force quit an application, though you can access Force Quit via the Apple menu."
  },
  {
    "question": "A technician is tasked with configuring a computer for a visually impaired user. Which of the following utilities should the technician use?",
    "options": [
      "Device Manager",
      "System",
      "Ease of Access Center",
      "Programs and Features"
    ],
    "correct_answer": [3],
    "description": "The correct answer is Ease of Access Center. This tool provides various accessibility options such as magnifiers, screen readers, and high contrast modes to assist users with visual impairments. \n\n- Device Manager is used for managing hardware devices but not accessibility settings. \n- System settings manage overall system information and performance but do not specifically cater to accessibility. \n- Programs and Features is for managing installed applications and does not provide accessibility options."
  },
  {
    "question": "A user received the following error upon visiting a banking website: The security certificate presented by this website was issued for a different website's address. A technician should instruct the user to:",
    "options": [
      "clear the browser cache and contact the bank",
      "close out of the site and contact the bank",
      "continue to the site and contact the bank",
      "update the browser and contact the bank"
    ],
    "correct_answer": [2],
    "description": "The correct answer is close out of the site and contact the bank. A mismatched security certificate could indicate a phishing attempt or an improperly configured website. It's safer to close the site and report it to the bank to ensure it's not a security risk. \n\n- Clearing the cache won’t resolve the issue of a mismatched certificate. \n- Continuing to the site could expose the user to security risks. \n- Updating the browser is a good practice, but it won’t resolve a certificate issue tied to the website."
  },
  {
    "question": "A technician connects an additional monitor to a PC using a USB port. The original HDMI monitor is mounted to the left of the new monitor. When moving the mouse to the right from the original monitor to the new monitor, the mouse stops at the end of the screen on the original monitor. Which of the following will allow the mouse to correctly move to the new monitor?",
    "options": [
      "Rearranging the monitor's position in display settings",
      "Swapping the cables for the monitors",
      "Using the Ctrl+Alt+=> to correct the display orientation",
      "Updating the display drivers for the video card"
    ],
    "correct_answer": [1],
    "description": "The correct answer is Rearranging the monitor's position in display settings. The operating system needs to know the physical arrangement of the monitors to align cursor movement correctly. \n\n- Swapping cables won’t affect how the system interprets the monitor layout. \n- Ctrl+Alt+=> is not a valid method for adjusting display orientation. \n- Updating the display drivers is a good practice, but it won’t resolve this specific issue of screen alignment."
  },

  #131-140

  {
    "question": "A user is unable to use any internet-related functions on a smartphone when it is not connected to Wi-Fi. When the smartphone is connected to Wi-Fi, the user can browse the internet and send and receive email. The user is also able to send and receive text messages and phone calls when the smartphone is not connected to Wi-Fi. Which of the following is the MOST likely reason the user is unable to use the internet on the smartphone when it is not connected to Wi-Fi?",
    "options": [
      "The smartphone's line was not provisioned with a data plan",
      "The smartphone's SIM card has failed.",
      "The smartphone's Bluetooth radio is disabled",
      "The smartphone has too many applications open"
    ],
    "correct_answer": [1],
    "description": "The correct answer is The smartphone's line was not provisioned with a data plan. This means the user can make calls and send texts but does not have cellular data access for internet functions. \n\n- If the SIM card had failed, the user would likely be unable to make calls or send texts as well. \n- A disabled Bluetooth radio would not affect internet connectivity; it only impacts wireless device connections. \n- Having too many applications open may slow down the phone, but it wouldn’t prevent internet access if the data plan is active."
  },
  {
    "question": "A help desk technician runs the following script: Inventory.py. The technician receives the following error message: How do you want to open this file? Which of the following is the MOST likely reason this script is unable to run?",
    "options": [
      "Scripts are not permitted to run.",
      "The script was not built for Windows.",
      "The script requires administrator privileges.",
      "The runtime environment is not installed."
    ],
    "correct_answer": [4],
    "description": "The correct answer is The runtime environment is not installed. The message suggests that the system does not know how to execute the Python script, indicating a missing Python runtime. \n\n- If scripts were not permitted to run, the user would likely see a different error message or warning. \n- If the script was not built for Windows, it would typically specify compatibility issues rather than simply asking how to open the file. \n- While some scripts require admin privileges, the presented error indicates a lack of an execution environment rather than permissions."
  },
  {
    "question": "A company discovered that numerous computers from multiple geographic locations are sending a very high number of connection requests which is causing the company’s web server to become unavailable to the general public. Which of the following attacks is occurring?",
    "options": [
      "Zero day",
      "SQL injection",
      "Cross-site scripting",
      "Distributed denial of service"
    ],
    "correct_answer": [4],
    "description": "The correct answer is Distributed denial of service. This type of attack overwhelms a server with traffic, making it unavailable to legitimate users. \n\n- A zero-day attack exploits a previously unknown vulnerability but doesn’t specifically describe high-volume connection requests. \n- SQL injection and cross-site scripting are attacks targeting web application vulnerabilities, not necessarily aimed at overwhelming a server with requests."
  },
  {
    "question": "A technician suspects the boot disk of a user’s computer contains bad sectors. Which of the following should the technician verify in the command prompt to address the issue without making any changes?",
    "options": [
      "Run sfc /scannow on the drive as the administrator",
      "Run cleanmgr on the drive as the administrator",
      "Run chkdsk on the drive as the administrator",
      "Run dfrgui on the drive as the administrator"
    ],
    "correct_answer": [3],
    "description": "The correct answer is Run chkdsk on the drive as the administrator. This command checks the file system integrity and can identify bad sectors without altering the disk's contents. \n\n- sfc /scannow is used for scanning and repairing system files, not specifically for checking disk sectors. \n- cleanmgr is a disk cleanup tool that removes unnecessary files, and does not check for bad sectors. \n- dfrgui is used for defragmenting disks, which is not applicable for diagnosing bad sectors."
  },
  {
    "question": "A BSOD appears on a user’s workstation monitor. The user immediately presses the power button to shut down the PC, hoping to repair the issue. The user then restarts the PC, and the BSOD reappears, so the user contacts the help desk. Which of the following should the technician use to determine the cause?",
    "options": [
      "Stop code",
      "Event Viewer",
      "Services",
      "System Configuration"
    ],
    "correct_answer": [1],
    "description": "The correct answer is Stop code. The stop code displayed on the BSOD provides specific information about the error that caused the system crash, guiding the technician in troubleshooting. \n\n- Event Viewer logs provide historical data and might include errors leading up to the BSOD, but it won’t directly indicate the cause of the crash. \n- Services show the status of system services but won’t help diagnose a BSOD. \n- System Configuration is used for troubleshooting startup issues, but it does not provide immediate details about a BSOD."
  },
  {
    "question": "Which of the following is the STRONGEST wireless configuration?",
    "options": [
      "WPS",
      "WPA3",
      "WEP",
      "WMN"
    ],
    "correct_answer": [2],
    "description": "The correct answer is WPA3. This is the latest Wi-Fi security protocol, providing enhanced protection against brute-force attacks and improved encryption. \n\n- WPS (Wi-Fi Protected Setup) is convenient but has known vulnerabilities. \n- WEP (Wired Equivalent Privacy) is outdated and easily compromised. \n- WMN (Wireless Mesh Network) is a network topology rather than a security protocol."
  },
  {
    "question": "A technician is installing new network equipment in a SOHO and wants to ensure the equipment is secured against external threats on the Internet. Which of the following actions should the technician do FIRST?",
    "options": [
      "Lock all devices in a closet.",
      "Ensure all devices are from the same manufacturer.",
      "Change the default administrative password.",
      "Install the latest operating system and patches."
    ],
    "correct_answer": [3],
    "description": "The correct answer is Change the default administrative password. This is a crucial step in securing network devices as default passwords are often well-known and can be easily exploited. \n\n- Locking devices in a closet does not address the fundamental security vulnerabilities present in the default configurations. \n- Ensuring devices are from the same manufacturer may simplify management but does not enhance security. \n- Installing the latest operating system and patches is important but should follow changing default passwords to minimize immediate risks."
  },
  {
    "question": "While assisting a customer with an issue, a support representative realizes the appointment is taking longer than expected and will cause the next customer meeting to be delayed by five minutes. Which of the following should the support representative do NEXT?",
    "options": [
      "Send a quick message regarding the delay to the next customer.",
      "Cut the current customer's time short and rush to the next customer.",
      "Apologize to the next customer when arriving late.",
      "Arrive late to the next meeting without acknowledging the time."
    ],
    "correct_answer": [1],
    "description": "The correct answer is Send a quick message regarding the delay to the next customer. This proactive communication demonstrates respect for the next customer's time and helps manage expectations. \n\n- Cutting the current appointment short may lead to unresolved issues and dissatisfaction for the customer currently being helped. \n- Apologizing after arriving late is reactive rather than proactive. \n- Arriving late without acknowledgment is unprofessional and can damage customer relationships."
  },
  {
    "question": "A user connected a laptop to a wireless network and was tricked into providing log-in credentials for a website. Which of the following threats was used to carry out the attack?",
    "options": [
      "Zero day",
      "Vishing",
      "DDoS",
      "Evil twin"
    ],
    "correct_answer": [4],
    "description": "The correct answer is Evil twin. This threat involves setting up a rogue Wi-Fi network that appears legitimate, tricking users into connecting and providing sensitive information. \n\n- A zero-day attack refers to exploiting a software vulnerability that is unknown to the developer but does not apply here. \n- Vishing (voice phishing) involves phone calls, not wireless networks. \n- DDoS (Distributed Denial of Service) targets service availability, not credential theft."
  },
  {
    "question": "A new service desk is having a difficult time managing the volume of requests. Which of the following is the BEST solution for the department?",
    "options": [
      "Implementing a support portal",
      "Creating a ticketing system",
      "Commissioning an automated callback system",
      "Submitting tickets through email"
    ],
    "correct_answer": [1],
    "description": "The correct answer is Implementing a support portal. A support portal centralizes requests, provides self-service options, and improves tracking and management of user requests. \n\n- A ticketing system is part of a support portal, but alone may not address volume management effectively. \n- An automated callback system can help but does not resolve the initial request management issue. \n- Submitting tickets through email can lead to disorganization and can overwhelm support staff without proper tracking."
  },

  #141-150

  
  {
    "question": "Which of the following Linux commands would be used to install an application?",
    "options": [
      "yum",
      "grep",
      "ls",
      "sudo"
    ],
    "correct_answer": [1],
    "description": "The correct answer is yum. This command is used in Linux distributions that use the RPM package manager, allowing users to install applications and manage software packages easily. \n\n- grep is a command for searching text in files and is not used for installation. \n- ls is used to list directory contents and does not perform installations. \n- sudo is a command that allows a permitted user to run commands with elevated privileges, but it does not itself install applications."
  },
  {
    "question": "A network administrator is deploying a client certificate to be used for Wi-Fi access for all devices in an organization. The certificate will be used in conjunction with the user's existing username and password. Which of the following BEST describes the security benefits realized after this deployment?",
    "options": [
      "Multifactor authentication will be forced for Wi-Fi.",
      "All Wi-Fi traffic will be encrypted in transit.",
      "Eavesdropping attempts will be prevented.",
      "Rogue access points will not connect."
    ],
    "correct_answer": [1],
    "description": "The correct answer is Multifactor authentication will be forced for Wi-Fi. By requiring both a certificate and user credentials, the deployment enhances security by ensuring that both something the user knows (username/password) and something the user has (the certificate) are required for access. \n\n- While Wi-Fi traffic encryption is important, it is the combination of factors that provides multifactor authentication. \n- Eavesdropping attempts can be mitigated with encryption but not entirely prevented. \n- Rogue access points can still connect unless additional security measures are taken."
  },
    {
      "question": "A user in a corporate office reports the inability to connect to any network drives. No other users have reported this issue. Which of the following is the MOST likely reason the user is having this issue?",
      "options": [
        "The user is not connected to the VPN.",
        "The file server is offline.",
        "A low battery is preventing the connection.",
        "The log-in script failed."
      ],
      "correct_answer": [4],
      "description": "The correct answer is 4. The log-in script failed. A failed log-in script can prevent the user from properly authenticating to the network drives, which would explain why they are unable to connect. \n\n- If the user were not connected to the VPN, they would still be able to access local resources but not network drives. \n- If the file server were offline, multiple users would likely report connectivity issues. \n- A low battery would not directly impact the ability to connect to network drives unless it caused the device to shut down."
    },
  {
    "question": "A user reports a PC is running slowly. The technician suspects high disk I/O. Which of the following should the technician perform NEXT?",
    "options": [
      "resmon.exe",
      "msconfig.exe",
      "dfrgui.exe",
      "msinfo32.exe"
    ],
    "correct_answer": [1],
    "description": "The correct answer is resmon.exe. This command opens the Resource Monitor, which provides detailed information about disk activity, allowing the technician to assess high disk I/O in real-time. \n\n- msconfig.exe is used for managing startup configurations and services, not for monitoring disk I/O. \n- dfrgui.exe is for disk defragmentation and optimization, which may not directly address slow performance due to high disk I/O. \n- msinfo32.exe provides a system information overview but lacks specific real-time disk I/O monitoring."
  },
    {
  "question": "A user enabled a mobile device's screen lock function with pattern unlock. The user is concerned someone could access the mobile device by repeatedly attempting random patterns to unlock the device. Which of the following features BEST addresses the user's concern?",
  "options": [
    "Remote wipe",
    "Anti-malware",
    "Device encryption",
    "Failed login restrictions"
  ],
  "correct_answer": [4],
  "description": "The correct answer is 4. Failed login restrictions. This feature limits the number of unsuccessful unlock attempts, thereby protecting the device from unauthorized access through brute-force attacks. \n\n- Remote wipe is useful for data security but does not prevent access attempts. \n- Anti-malware protects against malicious software but not against unauthorized access attempts. \n- Device encryption secures data but does not address the concern of repeated pattern attempts."
    },
    {
  "question": "Which of the following is MOST likely contained in an EULA?",
  "options": [
    "Chain of custody",
    "Backup of software code",
    "Personally identifiable information",
    "Restrictions of use"
  ],
  "correct_answer": [4],
  "description": "The correct answer is 4. Restrictions of use. An End User License Agreement (EULA) outlines how software can and cannot be used, specifying limitations and rights granted to the user. \n\n- Chain of custody is related to legal procedures and evidence management, not typical in EULAs. \n- A backup of software code is not relevant to end users; EULAs pertain to usage rights. \n- Personally identifiable information is protected under privacy laws and is not usually detailed in an EULA."
    },
  {
    "question": "A junior administrator is responsible for deploying software to a large group of computers in an organization. The administrator finds a script on a popular coding website to automate this distribution but does not understand the scripting language. Which of the following BEST describes the risks in running this script?",
    "options": [
      "The instructions from the software company are not being followed.",
      "Security controls will treat automated deployments as malware.",
      "The deployment script is performing unknown actions.",
      "Copying scripts off the internet is considered plagiarism."
    ],
    "correct_answer": [3],
    "description": "The correct answer is The deployment script is performing unknown actions. Running a script without understanding it can lead to unintended consequences, including security vulnerabilities or system instability. \n\n- Not following instructions from the software company could be a concern, but the immediate risk is executing unknown code. \n- Security controls may flag the script, but this is secondary to the risk of unknown actions. \n- While copying scripts may raise ethical concerns, it does not directly affect operational security."
  },
  {
    "question": "A user opened a ticket regarding a corporate-managed mobile device. The assigned technician notices the OS is several versions out of date. The user is unaware the OS version is not current because auto-update is turned on. Which of the following is MOST likely the cause of the issue?",
    "options": [
      "The device does not have enough free space to download the OS updates.",
      "The device needs user confirmation to update to a major release.",
      "The device is not compatible with the newest version of the OS.",
      "The device is restricted from updating due to a corporate security policy."
    ],
    "correct_answer": [1],
    "description": "The correct answer is The device does not have enough free space to download the OS updates. Insufficient storage can prevent updates from being downloaded and installed, despite auto-update being enabled. \n\n- User confirmation for major releases is a common requirement, but it wouldn’t explain why the OS remains out of date if auto-updates were functioning. \n- If the device were incompatible, it would usually display an error message. \n- Corporate policies may restrict updates, but this would require explicit communication or settings."
  },
  {
    "question": "A technician receives a ticket indicating the user cannot resolve external web pages. However, specific IP addresses are working. Which of the following does the technician MOST likely need to change on the workstation to resolve the issue?",
    "options": [
      "Default gateway",
      "Host address",
      "Name server",
      "Subnet mask"
    ],
    "correct_answer": [3],
    "description": "The correct answer is Name server. If specific IP addresses work but domain names do not, it suggests an issue with the DNS resolution, which the name server handles. \n\n- The default gateway is necessary for routing traffic to external networks, but the scenario indicates that IPs are functional. \n- Host address refers to the computer’s own IP configuration, not external page access. \n- Subnet mask defines the network range and does not directly impact web page resolution."
  },
 {
  "question": "An administrator has received approval for a change request for an upcoming server deployment. Which of the following steps should be completed NEXT?",
  "options": [
    "Perform a risk analysis.",
    "Implement the deployment.",
    "Verify end user acceptance.",
    "Document the lessons learned."
  ],
  "correct_answer": [1],
  "description": "The correct answer is. Perform a risk analysis. Before implementing any changes, it’s essential to assess potential risks associated with the deployment to ensure it does not adversely affect existing systems or services. \n\n- Implementing the deployment should only occur after risk analysis and planning have been completed. \n- Verifying end user acceptance is important but comes after ensuring the deployment is safe. \n- Documenting lessons learned is part of the post-implementation review, not a pre-deployment step."
 },

#151-160

    {
      "question": "A user calls the help desk to report that Windows installed updates on a laptop and rebooted overnight. When the laptop started up again, the touchpad was no longer working. The technician thinks the software that controls the touchpad might be the issue. Which of the following tools should the technician use to make adjustments?",
      "options": [
        "eventvwr.msc",
        "perfmon.msc",
        "gpedit.msc",
        "devmgmt.msc"
      ],
      "correct_answer": [4],
      "description": "The correct answer is devmgmt.msc. This tool, also known as Device Manager, allows the technician to manage hardware devices and their drivers, which is essential for troubleshooting issues related to the touchpad. \n\n- eventvwr.msc is used to view Windows event logs and would not provide direct control over hardware settings. \n- perfmon.msc monitors system performance and resource usage but does not manage device drivers. \n- gpedit.msc is used to configure group policies and does not directly address hardware-related issues."
    },

    {
      "question": "Antivirus software indicates that a workstation is infected with ransomware that cannot be quarantined. Which of the following should be performed FIRST to prevent further damage to the host and other systems?",
      "options": [
        "Power off the machine.",
        "Run a full antivirus scan.",
        "Remove the LAN card.",
        "Install a different endpoint solution."
      ],
      "correct_answer": [1],
      "description": "The correct answer is Power off the machine. This action immediately halts any ongoing encryption processes and prevents the ransomware from spreading to other devices on the network. \n\n- Running a full antivirus scan may help later but won't stop the ransomware from causing further damage while the machine is still operational. \n- Removing the LAN card might be a necessary step, but it is more effective to power down the machine first to avoid data loss. \n- Installing a different endpoint solution should occur after the machine is safely powered off and assessed for further action."
    },

    {
      "question": "A technician has been tasked with troubleshooting audiovisual issues in a conference room. The meeting presenters are unable to play a video with sound. The following error is received: The Audio Driver is not running. Which of the following will MOST likely resolve the issue?",
      "options": [
        "compmgmt.msc",
        "regedit.exe",
        "explorer.exe",
        "taskmgr.exe",
        "gpmc.msc",
        "services.msc"
      ],
      "correct_answer": [6],
      "description": "The correct answer is services.msc. This tool allows the technician to manage Windows services, enabling them to start the audio driver service that is currently not running. \n\n- compmgmt.msc provides access to various management tools but is less direct for service management. \n- regedit.exe is used for editing the Windows Registry, which is not necessary for resolving this issue. \n- explorer.exe is the file manager and does not pertain to audio drivers. \n- taskmgr.exe can help monitor resource usage but is not designed for managing services. \n- gpmc.msc is related to Group Policy management and is not relevant to this troubleshooting scenario."
    },

    {
      "question": "A technician installed a new application on a workstation. For the program to function properly, it needs to be listed in the Path Environment Variable. Which of the following Control Panel utilities should the technician use?",
      "options": [
        "System",
        "Indexing Options",
        "Device Manager",
        "Programs and Features"
      ],
      "correct_answer": [1],
      "description": "The correct answer is System. This utility allows the technician to access the Environment Variables settings, where the Path variable can be modified to include the newly installed application's directory. \n\n- Indexing Options is used for configuring the Windows search indexing settings, not for modifying environment variables. \n- Device Manager manages hardware devices but does not relate to application path settings. \n- Programs and Features allows users to uninstall or change installed software but does not manage environment variables."
    },

    {
      "question": "A systems administrator is setting up a Windows computer for a new user. Corporate policy requires a least privilege environment. The user will need to access advanced features and configuration settings for several applications. Which of the following BEST describes the account access level the user will need?",
      "options": [
        "Power user account",
        "Standard account",
        "Guest account",
        "Administrator account"
      ],
      "correct_answer": [1],
      "description": "The correct answer is Power user account. This account type provides the necessary permissions to perform advanced tasks without granting full administrative rights, aligning with the least privilege policy. \n\n- A Standard account offers basic user permissions and would restrict access to advanced features. \n- A Guest account has very limited permissions, making it unsuitable for a user requiring access to advanced settings. \n- An Administrator account grants full access, which is contrary to the least privilege principle."
    },

    {
      "question": "A technician downloads a validated security tool and notes the vendor hash of a11e11a1. When the download is complete, the technician again validates the hash, but the value returns as 2a222a2b2. Which of the following is the MOST likely cause of the issue?",
      "options": [
        "Private-browsing mode",
        "Invalid certificate",
        "Modified file",
        "Browser cache"
      ],
      "correct_answer": [3],
      "description": "The correct answer is Modified file. The hash mismatch indicates that the file has been altered in some way, potentially indicating a security risk. \n\n- Private-browsing mode affects how browsing data is stored but does not alter the file's hash value. \n- An invalid certificate would prevent the download or indicate a warning but would not cause a hash change after the download. \n- Browser cache may affect loading times or access to older versions but does not alter file integrity."
    },

    {
      "question": "A company needs to securely dispose of data stored on optical discs. Which of the following is the MOST effective method to accomplish this task?",
      "options": [
        "Degaussing",
        "Low-level formatting",
        "Recycling",
        "Shredding"
      ],
      "correct_answer": [4],
      "description": "The correct answer is Shredding. Physically shredding the optical discs ensures that the data cannot be recovered, making it the most secure disposal method. \n\n- Degaussing is effective for magnetic media but does not apply to optical discs. \n- Low-level formatting is not applicable to optical discs and is more relevant to hard drives. \n- Recycling may dispose of the disc but does not guarantee data destruction."
    },

    {
      "question": "A mobile phone user has downloaded a new payment application that allows payments to be made with a mobile device. The user attempts to use the device at a payment terminal but is unable to do so successfully. The user contacts a help desk technician to report the issue. Which of the following should the technician confirm NEXT as part of the troubleshooting process?",
      "options": [
        "If airplane mode is enabled",
        "If Bluetooth is disabled",
        "If NFC is enabled",
        "If Wi-Fi is enabled",
        "If location services are disabled"
      ],
      "correct_answer": [3],
      "description": "The correct answer is If NFC is enabled. Near Field Communication (NFC) must be enabled for mobile payments to work at payment terminals, so confirming this setting is critical. \n\n- Airplane mode would prevent all communication but is a more general check and may not directly address the payment issue. \n- Bluetooth is not typically required for most payment applications unless they specifically use Bluetooth connectivity. \n- Wi-Fi being enabled is usually not necessary for contactless payments, and location services may not affect the payment process directly."
    },

    {
      "question": "A Chief Executive Officer has learned that an exploit has been identified on the web server software, and a patch is not available yet. Which of the following attacks MOST likely occurred?",
      "options": [
        "Brute force",
        "Zero day",
        "Denial of service",
        "On-path"
      ],
      "correct_answer": [2],
      "description": "The correct answer is Zero day. A zero-day exploit refers to vulnerabilities that are exploited before a patch is available, meaning the software is at risk until a fix is released. \n\n- A brute force attack typically involves attempting multiple passwords to gain access, which is different from exploiting a vulnerability. \n- A denial of service attack aims to make services unavailable but does not necessarily exploit software vulnerabilities. \n- An on-path attack (also known as man-in-the-middle) intercepts communications but does not directly relate to unpatched software vulnerabilities."
    },

    {
      "question": "A user has a license for an application that is in use on a personal home laptop. The user approaches a systems administrator about using the same license on multiple computers on the corporate network. Which of the following BEST describes what the systems administrator should tell the user?",
      "options": [
        "Use the application only on the home laptop because it contains the initial license.",
        "Use the application at home and contact the vendor regarding a corporate license.",
        "Use the application on any computer since the user has a license.",
        "Use the application only on corporate computers."
      ],
      "correct_answer": [2],
      "description": "The correct answer is Use the application at home and contact the vendor regarding a corporate license. This response clarifies that while the user may use the application on their personal device, they should seek permission for corporate usage, as licensing agreements often restrict installation to a single device or require separate licenses for multiple installations. \n\n- Using the application only on the home laptop is limiting and does not address the potential for a corporate license. \n- Using the application on any computer could violate licensing terms, leading to compliance issues. \n- Using the application only on corporate computers is incorrect since the license is specific to the home laptop."
    },

#161-170

    {
      "question": "A technician needs to interconnect two offices to the main branch while complying with good practices and security standards. Which of the following should the technician implement?",
      "options": [
        "MSRA",
        "VNC",
        "VPN",
        "SSH"
      ],
      "correct_answer": [3],
      "description": "The correct answer is VPN. A Virtual Private Network (VPN) provides a secure connection over the internet, allowing remote offices to connect to the main branch while maintaining privacy and data integrity. \n\n- MSRA (Microsoft Remote Assistance) is designed for troubleshooting rather than secure inter-office connections. \n- VNC (Virtual Network Computing) allows remote desktop sharing but lacks built-in encryption, making it less secure. \n- SSH (Secure Shell) is primarily used for secure command-line access rather than establishing a network connection between offices."
    },

    {
      "question": "A user receives a notification indicating the data plan on the user's corporate phone has reached its limit. The user has also noted the performance of the phone is abnormally slow. A technician discovers a third-party GPS application was installed on the phone. Which of the following is the MOST likely cause?",
      "options": [
        "The GPS application is installing software updates.",
        "The GPS application contains malware.",
        "The GPS application is updating its geospatial map data.",
        "The GPS application is conflicting with the built-in GPS."
      ],
      "correct_answer": [2],
      "description": "The correct answer is The GPS application contains malware. Malicious applications can consume excessive data and system resources, leading to performance issues and reaching data limits. \n\n- The GPS application installing software updates could consume data but wouldn't typically cause significant performance degradation. \n- Updating geospatial map data is a normal function and would not usually lead to performance problems. \n- Conflicts with the built-in GPS could cause issues, but the excessive data usage suggests a more serious problem, such as malware."
    },

    {
      "question": "A technician needs to document who had possession of evidence at every step of the process. Which of the following does this process describe?",
      "options": [
        "Rights management",
        "Audit trail",
        "Chain of custody",
        "Data integrity"
      ],
      "correct_answer": [3],
      "description": "The correct answer is Chain of custody. This term refers to the process of maintaining and documenting the handling of evidence to ensure it is secure and valid for legal proceedings. \n\n- Rights management involves controlling access to data but does not focus on the handling of physical evidence. \n- An audit trail records actions taken on data but is not specifically about the possession of evidence. \n- Data integrity ensures data accuracy and consistency but does not relate to the handling process."
    },

    {
      "question": "A malicious file was executed automatically when a flash drive was plugged in. Which of the following features would prevent this type of incident?",
      "options": [
        "Disabling UAC",
        "Restricting local administrators",
        "Enabling UPnP",
        "Turning off AutoPlay"
      ],
      "correct_answer": [4],
      "description": "The correct answer is Turning off AutoPlay. Disabling AutoPlay prevents automatic execution of files on removable media, which helps protect against malware infections from flash drives. \n\n- Disabling User Account Control (UAC) can actually increase vulnerability by allowing unauthorized changes without user consent. \n- Restricting local administrators may improve security but does not specifically prevent file execution from flash drives. \n- Enabling UPnP (Universal Plug and Play) can pose security risks and is unrelated to protecting against malicious files on USB drives."
    },

    {
      "question": "Which of the following is used to identify potential issues with a proposed change prior to implementation?",
      "options": [
        "Request form",
        "Rollback plan",
        "End-user acceptance",
        "Sandbox testing"
      ],
      "correct_answer": [4],
      "description": "The correct answer is Sandbox testing. This method involves testing changes in an isolated environment to identify any potential issues before implementation in a live environment. \n\n- A request form is used to document proposed changes but does not test their impact. \n- A rollback plan outlines steps to revert changes if necessary but does not identify issues beforehand. \n- End-user acceptance involves validating changes with users after implementation, rather than assessing potential issues in advance."
    },

    {
      "question": "A user needs assistance changing the desktop wallpaper on a Windows 10 computer. Which of the following methods will enable the user to change the wallpaper using a Windows 10 Settings tool?",
      "options": [
        "Open Settings, select Accounts, select Your info, click Browse, and then locate and open the image the user wants to use as the wallpaper.",
        "Open Settings, select Personalization, click Browse, and then locate and open the image the user wants to use as the wallpaper.",
        "Open Settings, select System, select Display, click Browse, and then locate and open the image the user wants to use as the wallpaper.",
        "Open Settings, select Apps, select Apps & features, click Browse, and then locate and open the image the user wants to use as the wallpaper."
      ],
      "correct_answer": [2],
      "description": "The correct answer is Open Settings, select Personalization, click Browse, and then locate and open the image the user wants to use as the wallpaper. The Personalization section specifically deals with customizing the desktop appearance, including wallpaper changes. \n\n- The Accounts section is for user account settings, not wallpaper changes. \n- The System section and Display settings primarily handle screen resolution and orientation but do not provide direct access to wallpaper settings. \n- The Apps section manages installed applications, not desktop customization."
    },

    {
      "question": "A macOS user needs to create another virtual desktop space. Which of the following applications will allow the user to accomplish this task?",
      "options": [
        "Dock",
        "Spotlight",
        "Mission Control",
        "Launchpad"
      ],
      "correct_answer": [3],
      "description": "The correct answer is Mission Control. This application in macOS provides an overview of all open windows and allows users to create new virtual desktops easily. \n\n- The Dock is a launcher for applications and does not manage desktop spaces. \n- Spotlight is used for searching files and applications but does not create virtual desktops. \n- Launchpad is primarily for accessing applications and does not facilitate desktop management."
    },

    {
      "question": "A user lost a company tablet that was used for customer intake at a doctor's office. Which of the following actions would BEST protect against unauthorized access of the data?",
      "options": [
        "Changing the office's Wi-Fi SSID and password",
        "Performing a remote wipe on the device",
        "Changing the user's password",
        "Enabling remote drive encryption"
      ],
      "correct_answer": [2],
      "description": "The correct answer is Performing a remote wipe on the device. This action ensures that all data on the lost tablet is deleted, preventing unauthorized access to sensitive information. \n\n- Changing the Wi-Fi SSID and password protects the network but does not safeguard the lost tablet's data. \n- Changing the user's password can enhance account security but does not address the data on the device itself. \n- Enabling remote drive encryption is a preventive measure, but it does not help recover the data after the device is lost."
    },

    {
      "question": "A desktop engineer is deploying a master image. Which of the following should the desktop engineer consider when building the master image? (Choose two.)",
      "options": [
        "Device drivers",
        "Keyboard backlight settings",
        "Installed application license keys",
        "Display orientation",
        "Target device power supply",
        "Disabling express charging"
      ],
      "correct_answer": [1, 3],
      "description": "The correct answers are Device drivers and Installed application license keys. Including the correct drivers ensures hardware compatibility and functionality, while license keys are essential for legal compliance and proper software operation. \n\n- Keyboard backlight settings and display orientation are more personalized preferences and do not impact the master image's core functionality. \n- Target device power supply and disabling express charging may relate to hardware but are not critical considerations when building a master image."
    },

    {
      "question": "A technician installed an application on a user's desktop and received an error message. Which of the following tools can the technician use to research the error?",
      "options": [
        "Resource Monitor > CPU > Services",
        "Task Manager > Processes > Apps",
        "Event Viewer > Windows Logs > Application",
        "Device Manager > Computer"
      ],
      "correct_answer": [3],
      "description": "The correct answer is Event Viewer > Windows Logs > Application. This tool logs application errors and events, allowing the technician to find detailed information about the error message encountered. \n\n- Resource Monitor primarily monitors system resources, which may not provide details about specific application errors. \n- Task Manager helps manage running processes but does not offer extensive information on application issues. \n- Device Manager is for managing hardware devices and does not pertain to application error diagnostics."
    },

#171-180

    {
      "question": "A technician is configuring a new Windows laptop. Corporate policy requires that mobile devices make use of full disk encryption at all times. Which of the following encryption solutions should the technician choose?",
      "options": [
        "Encrypting File System",
        "File Vault",
        "BitLocker",
        "Encrypted LVM"
      ],
      "correct_answer": [3],
      "description": "The correct answer is BitLocker. BitLocker is a full disk encryption feature included with Windows that protects data by encrypting the entire disk. \n\n- Encrypting File System (EFS) encrypts files but not the entire disk, making it less suitable for the requirement. \n- File Vault is specific to macOS and not applicable for Windows environments. \n- Encrypted LVM is a Linux solution, not relevant in this context."

    },
    {
      "question": "A small business owner wants to install newly purchased software on all networked PCs. The network is not configured as a domain, and the owner wants to use the easiest method possible. Which of the following is the MOST efficient way for the owner to install the application?",
      "options": [
        "Use a network share to share the installation files.",
        "Save software to an external hard drive to install.",
        "Create an imaging USB for each PC.",
        "Install the software from the vendor's website."
      ],
      "correct_answer": [1],
      "description": "The correct answer is Use a network share to share the installation files. This method allows all PCs to access the shared installation files easily and efficiently without the need for physical media or individual installations. \n\n- Saving to an external hard drive requires physically moving the drive between PCs. \n- Creating an imaging USB for each PC is time-consuming and inefficient for multiple machines. \n- Installing from the vendor's website requires an internet connection on each PC and may not be practical for all devices."

    },
    {
      "question": "A user reports that text on the screen is too small. The user would like to make the text larger and easier to see. Which of the following is the BEST way for the user to increase the size of text, applications, and other items using the Windows 10 Settings tool?",
      "options": [
        "Open Settings, select Devices, select Display, and change the display resolution to a lower resolution option.",
        "Open Settings, select System, select Display, and change the display resolution to a lower resolution option.",
        "Open Settings, select System, select Display, and change the Scale and layout setting to a higher percentage.",
        "Open Settings, select Personalization, select Display, and change the Scale and layout setting to a higher percentage."
      ],
      "correct_answer": [3],
      "description": "The correct answer is Open Settings, select System, select Display, and change the Scale and layout setting to a higher percentage. This directly increases the size of text and other UI elements without compromising screen clarity. \n\n- Changing the display resolution to a lower setting may distort the display and not effectively enlarge the text. \n- The Personalization settings primarily focus on background and themes, not scaling text effectively."

    },
    {
      "question": "A user is being directed by the help desk to look up a Windows PC's network name so the help desk can use a remote administration tool to assist the user. Which of the following commands would allow the user to give the technician the correct information? (Choose two.)",
      "options": [
        "ipconfig /all",
        "hostname",
        "netstat /?",
        "nslookup localhost",
        "arp -a",
        "ping ::1"
      ],
      "correct_answer": [1, 2],
      "description": "The correct answers are ipconfig /all and hostname. Both commands will provide the user with the network name of the PC. \n\n- ipconfig /all shows detailed information about all network interfaces, including the computer's hostname. \n- The hostname command directly displays the name of the computer on the network. \n- The other commands provide networking information but do not directly show the PC's name."

    },
    {
      "question": "Which of the following is a data security standard for protecting credit cards?",
      "options": [
        "PHI",
        "NIST",
        "PCI",
        "GDPR"
      ],
      "correct_answer": [3],
      "description": "The correct answer is PCI (Payment Card Industry Data Security Standard). PCI DSS provides a framework for securing credit card transactions and protecting cardholder data. \n\n- PHI (Protected Health Information) pertains to healthcare data, not credit cards. \n- NIST (National Institute of Standards and Technology) develops guidelines and standards but is not specific to credit card protection. \n- GDPR (General Data Protection Regulation) focuses on personal data protection in the EU, not specifically on credit card information."

    },
    {
      "question": "A technician has verified that a user's computer has a virus, and the antivirus software is out of date. Which of the following steps should the technician take NEXT?",
      "options": [
        "Quarantine the computer.",
        "Use a previous restore point.",
        "Educate the end user about viruses.",
        "Download the latest virus definitions."
      ],
      "correct_answer": [1],
      "description": "The correct answer is Quarantine the computer. Quarantining the computer is crucial to prevent the virus from spreading or causing further damage while the technician resolves the issue. \n\n- Downloading the latest virus definitions should follow quarantining, as this ensures that the antivirus software can effectively identify and remove threats. \n- Using a previous restore point may not eliminate the virus, especially if it was introduced after the restore point was created. \n- Educating the end user is important but should occur after immediate actions to secure the system."
    },
    {
      "question": "A technician installs specialized software on a workstation. The technician then attempts to run the software. The workstation displays a message indicating the software is not authorized to run. Which of the following should the technician do to MOST likely resolve the issue?",
      "options": [
        "Grant permissions to the installation directory.",
        "Attach the external hardware token.",
        "Install OS updates.",
        "Restart the workstation after installation."
      ],
      "correct_answer": [2],
      "description": "The correct answer is Attach the external hardware token. Many specialized software applications require an external hardware token for authorization, which ensures the software can run without restrictions. \n\n- Granting permissions to the installation directory may resolve some authorization issues, but if the software specifically requires a hardware token, this step is crucial. \n- Installing OS updates could improve compatibility, but it won't resolve issues related to hardware authorization. \n- Restarting the workstation may help clear temporary issues but does not directly address the authorization requirement."
    },
    {
      "question": "A team of support agents will be using their workstations to store credit card data. Which of the following should the IT department enable on the workstations in order to remain compliant with common regulatory controls? (Choose two.)",
      "options": [
        "Encryption",
        "Antivirus",
        "AutoRun",
        "Guest accounts",
        "Default passwords",
        "Backups"
      ],
      "correct_answer": [1, 2],
      "description": "The correct answers are Encryption and Antivirus. Enabling encryption protects sensitive data, while antivirus software helps defend against malware that could compromise that data. \n\n- AutoRun can pose a security risk and should generally be disabled. \n- Guest accounts should not be enabled for workstations that handle sensitive data. \n- Default passwords should always be changed to enhance security. \n- While backups are essential for data recovery, they do not directly enhance compliance with regulatory controls."

    },
    {
      "question": "Which of the following editions of Windows 10 requires reactivation every 180 days?",
      "options": [
        "Enterprise",
        "Pro for Workstation",
        "Home",
        "Pro"
      ],
      "correct_answer": [1],
      "description": "The correct answer is Enterprise. This edition is typically used in corporate environments and requires reactivation every 180 days to ensure compliance with licensing agreements. \n\n- Pro for Workstation, Home, and Pro editions do not have this specific reactivation requirement."

    },
    {
      "question": "A technician has an external SSD. The technician needs to read and write to an external SSD on both Macs and Windows PCs. Which of the following filesystems is supported by both OS types?",
      "options": [
        "NTFS",
        "APFS",
        "ext4",
        "exFAT"
      ],
      "correct_answer": [4],
      "description": "The correct answer is exFAT. This filesystem is compatible with both macOS and Windows, making it ideal for external drives that need to be used interchangeably. \n\n- NTFS is a Windows-specific format and is read-only on macOS by default. \n- APFS is designed for macOS and not natively supported by Windows. \n- ext4 is a Linux filesystem and also not supported by Windows or macOS."
    },


#181-200

    {
      "question": "A user's system is infected with malware. A technician updates the anti-malware software and runs a scan that removes the malware. After the user reboots the system, it once again becomes infected with malware. Which of the following will MOST likely help to permanently remove the malware?",
      "options": [
        "Enabling System Restore.",
        "Educating the user.",
        "Booting into safe mode.",
        "Scheduling a scan."
      ],
      "correct_answer": [3],
      "description": "The correct answer is Booting into safe mode. Safe mode loads the operating system with minimal drivers and processes, which can prevent the malware from running and allow for a more thorough removal. \n\n- Enabling System Restore might help recover a previous state, but if malware is present, it could also restore the infection. \n- Educating the user is crucial for prevention, but it won't resolve the current infection. \n- Scheduling a scan may identify the malware later, but immediate action in safe mode is necessary for thorough removal."
    },
    {
      "question": "A technician is upgrading the backup system for documents at a high-volume law firm. The current backup system can retain no more than three versions of full backups before failing. The law firm is not concerned about restore times but asks the technician to retain more versions when possible. Which of the following backup methods should the technician MOST likely implement?",
      "options": [
        "Full.",
        "Mirror.",
        "Incremental.",
        "Differential."
      ],
      "correct_answer": [3],
      "description": "The correct answer is Incremental. Incremental backups save only the changes made since the last backup, allowing for efficient storage and retention of multiple versions without duplicating the entire dataset. \n\n- Full backups consume significant storage space and will become impractical for retaining many versions. \n- Mirror backups create an exact copy of the data, which may not allow for retaining multiple versions over time as older versions get overwritten. \n- Differential backups save changes since the last full backup, which can grow in size and may still require substantial storage for version retention."
    },
    {
      "question": "A user receives a notification indicating the antivirus protection on a company laptop is out of date. A technician is able to ping the user's laptop. The technician checks the antivirus parent servers and sees the latest signatures have been installed. The technician then checks the user's laptop and finds the antivirus engine and definitions are current. Which of the following has MOST likely occurred?",
      "options": [
        "Ransomware.",
        "Failed OS updates.",
        "Adware.",
        "Missing system files."
      ],
      "correct_answer": [3],
      "description": "The correct answer is Adware. Since the antivirus engine is current but the user receives a notification about out-of-date protection, it's likely that adware has installed itself on the system, causing the antivirus to malfunction or display incorrect notifications. \n\n- Ransomware typically encrypts files and would more likely prevent access to data rather than merely cause an antivirus notification. \n- Failed OS updates could lead to system issues, but they wouldn't directly trigger an antivirus protection notification. \n- Missing system files might cause instability or performance issues but are less likely to be the reason for the antivirus alert."
    },
    {
      "question": "A user is unable to access files on a work PC after opening a text document. The text document was labeled “URGENT PLEASE READ.txt - In active folder, .txt file titled urgent please read”. Which of the following should a support technician do FIRST?",
      "options": [
        "Quarantine the host in the antivirus system.",
        "Run antivirus scan for malicious software.",
        "Investigate how malicious software was installed.",
        "Reimage the computer."
      ],
      "correct_answer": [2],
      "description": "The correct answer is Run antivirus scan for malicious software. Running an antivirus scan is essential to detect and remove any malicious software that may have been introduced through the suspicious document. \n\n- Quarantining the host is a response to an identified threat but should occur after confirming the presence of malware. \n- Investigating how malware was installed is important but should follow immediate action to protect the system. \n- Reimaging the computer is a drastic step that may not be necessary if the malware can be removed effectively."
    },
    {
      "question": "A user has a computer with Windows 10 Home installed and purchased a Windows 10 Pro license. The user is not sure how to upgrade the OS. Which of the following should the technician do to apply this license?",
      "options": [
        "Copy the c:\\Windows\\windows.1ic file over to the machine and restart.",
        "Redeem the included activation key card for a product key.",
        "Insert a Windows USB hardware dongle and initiate activation.",
        "Activate with the digital license included with the device hardware."
      ],
      "correct_answer": [2],
      "description": "The correct answer is Redeem the included activation key card for a product key. This method allows the user to upgrade to Windows 10 Pro using the activation key provided. \n\n- Copying a system file is not a recognized method for upgrading Windows. \n- Inserting a USB dongle may not be applicable unless it specifically contains the Windows installation media. \n- Activating with a digital license requires that the license is already linked to the device, which is not applicable in this scenario."
    },
    {
      "question": "Which of the following is a package management utility for PCs that are running the Linux operating system?",
      "options": [
        "chmod.",
        "yum.",
        "man.",
        "grep."
      ],
      "correct_answer": [2],
      "description": "The correct answer is yum. Yum (Yellowdog Updater Modified) is a package management utility used in many Linux distributions to install, update, and manage software packages. \n\n- Chmod is a command used to change file permissions and is not a package manager. \n- Man is a command used to view documentation about commands but does not manage packages. \n- Grep is a command-line utility for searching plain-text data and is not related to package management."
    },
    {
      "question": "A technician is investigating unauthorized Wi-Fi access on a customer's home network. Individuals are able to access the customer's Wi-Fi network without a password. Which of the following is the MOST likely reason this situation is occurring?",
      "options": [
        "Channel utilization is oversubscribed.",
        "WPA2 exploits are being leveraged.",
        "The Wi-Fi password is posted on the router.",
        "The customer has a guest network enabled."
      ],
      "correct_answer": [4],
      "description": "The correct answer is The customer has a guest network enabled. Guest networks are often configured to allow access without a password or with a simpler one, making them vulnerable to unauthorized access. \n\n- Channel utilization oversubscription can affect performance but would not allow unauthorized access. \n- WPA2 exploits could allow unauthorized access if the network is not properly secured, but guest networks are specifically designed to be less secure for convenience. \n- Posting the password on the router is poor practice and could lead to unauthorized access, but it's less likely than having an open or easily accessible guest network."
    },
    {
      "question": "A technician is troubleshooting an issue that requires a user profile to be rebuilt. The technician is unable to locate Local Users and Groups in the MMC console. Which of the following is the NEXT step the technician should take to resolve the issue?",
      "options": [
        "Run the antivirus scan.",
        "Add the required snap-in.",
        "Restore the system backup.",
        "Use the administrator console."
      ],
      "correct_answer": [2],
      "description": "The correct answer is Add the required snap-in. Adding the Local Users and Groups snap-in to the MMC console will allow the technician to manage user profiles effectively. \n\n- Running an antivirus scan is a good practice but not relevant to the issue of missing user management tools. \n- Restoring a system backup is unnecessary at this stage and doesn't directly address the missing feature. \n- Using the administrator console may be a step, but without the proper snap-in, the technician won't be able to access user settings."
    },
    {
      "question": "A user updates a mobile device's OS. A frequently used application becomes consistently unresponsive immediately after the device is launched. Which of the following troubleshooting steps should the user perform FIRST?",
      "options": [
        "Delete the application's cache.",
        "Check for application updates.",
        "Roll back the OS update.",
        "Uninstall and reinstall the application."
      ],
      "correct_answer": [2],
      "description": "The correct answer is Check for application updates. The application may have a version compatible with the latest OS update, which could resolve the unresponsiveness. \n\n- Deleting the application's cache is a good troubleshooting step but should come after checking for updates. \n- Rolling back the OS update is a significant action that may not be necessary. \n- Uninstalling and reinstalling the application can resolve issues but may not be the most efficient first step."
    },
    {
      "question": "Which of the following physical security controls can prevent laptops from being stolen?",
      "options": [
        "Encryption.",
        "LoJack.",
        "Multifactor authentication.",
        "Equipment lock.",
        "Bollards."
      ],
      "correct_answer": [4],
      "description": "The correct answer is Equipment lock. Using physical locks prevents theft by securing laptops to immovable objects, thereby deterring opportunistic theft. \n\n- Encryption protects data but does not physically prevent theft. \n- LoJack is a tracking software solution for stolen devices but is not a physical prevention method. \n- Multifactor authentication secures user access but does not protect the device physically. \n- Bollards protect physical areas but are not practical for individual laptops."
    }



]

