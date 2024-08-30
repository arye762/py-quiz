questions_701_C = [
# Page 5 of 7 
    {
        "question": "Which of the following would best explain why a security analyst is running daily vulnerability scans on all corporate endpoints?",
        "options": [
            "To track the status of patching installations",
            "To find shadow IT cloud deployments",
            "To continuously monitor hardware inventory",
            "To hunt for active attackers in the network"
        ],
        "correct_answer": 1,
        "description": "Running daily vulnerability scans helps to ensure that all systems are consistently up-to-date with the latest security patches, thereby reducing the risk of unpatched vulnerabilities."
    },
    {
        "question": "Which of the following is classified as high availability in a cloud environment?",
        "options": [
            "Access broker",
            "Cloud HSM",
            "WAF",
            "Load balancer"
        ],
        "correct_answer": 4,
        "description": "A load balancer is used to distribute traffic across multiple servers to ensure that services remain available even if one server fails, which is a key component of high availability in cloud environments."
    },
    {
        "question": "Which of the following security measures is required when using a cloud-based platform for IoT management?",
        "options": [
            "Encrypted connection",
            "Federated identity",
            "Firewall",
            "Single sign-on"
        ],
        "correct_answer": 1,
        "description": "An encrypted connection ensures that data transmitted between IoT devices and the cloud platform is secure and protected from interception or tampering."
    },
    {
        "question": "Which of the following threat vectors is most commonly utilized by insider threat actors attempting data exfiltration?",
        "options": [
            "Unidentified removable devices",
            "Default network device credentials",
            "Spear phishing emails",
            "Impersonation of business units through typosquatting"
        ],
        "correct_answer": 1,
        "description": "Insider threat actors often use removable devices like USB drives to easily and covertly transfer sensitive data out of an organization."
    },
    {
        "question": "Which of the following methods to secure credit card data is best to use when a requirement is to see only the last four numbers on a credit card?",
        "options": [
            "Encryption",
            "Hashing",
            "Masking",
            "Tokenization"
        ],
        "correct_answer": 3,
        "description": "Masking is the process of hiding parts of sensitive data, such as displaying only the last four digits of a credit card number, while ensuring that the full data remains secure."
    },
    {
        "question": "The Chief Information Security Officer (CISO) has determined the company is non-compliant with local data privacy regulations. The CISO needs to justify the budget request for more resources. Which of the following should the CISO present to the board as the direct consequence of non-compliance?",
        "options": [
            "Fines",
            "Reputational damage",
            "Sanctions",
            "Contractual implications"
        ],
        "correct_answer": 1,
        "description": "Fines are often the direct and immediate consequence of non-compliance with data privacy regulations, which can be substantial and provide a strong justification for additional resources."
    },
    {
        "question": "Which of the following alert types is the most likely to be ignored over time?",
        "options": [
            "True positive",
            "True negative",
            "False positive",
            "False negative"
        ],
        "correct_answer": 3,
        "description": "False positives, or alerts that incorrectly indicate a threat when none exists, can lead to alert fatigue, where users start ignoring alerts altogether."
    },
    {
        "question": "A security analyst is investigating an application server and discovers that software on the server is behaving abnormally. The software normally runs batch jobs locally and does not generate traffic, but the process is now generating outbound traffic over random high ports. Which of the following vulnerabilities has likely been exploited in this software?",
        "options": [
            "Memory injection",
            "Race condition",
            "Side loading",
            "SQL injection"
        ],
        "correct_answer": 1,
        "description": "Memory injection vulnerabilities can allow attackers to manipulate the memory of a process, potentially leading to unauthorized outbound traffic."
    },
    {
        "question": "An important patch for a critical application has just been released, and a systems administrator is identifying all of the systems requiring the patch. Which of the following must be maintained in order to ensure that all systems requiring the patch are updated?",
        "options": [
            "Asset inventory",
            "Network enumeration",
            "Data certification",
            "Procurement process"
        ],
        "correct_answer": 1,
        "description": "Maintaining an asset inventory is crucial for tracking which systems are in place and ensuring that all relevant systems are patched when necessary."
    },








    {
        "question": "Which of the following should a security operations center use to improve its incident response procedure?",
        "options": [
            "Playbooks",
            "Frameworks",
            "Baselines",
            "Benchmarks"
        ],
        "correct_answer": 1,
        "description": "Playbooks provide step-by-step guidance on how to respond to specific incidents, helping to standardize and improve the incident response process."
    },
    {
        "question": "Which of the following describes an executive team that is meeting in a board room and testing the company's incident response plan?",
        "options": [
            "Continuity of operations",
            "Capacity planning",
            "Tabletop exercise",
            "Parallel processing"
        ],
        "correct_answer": 3,
        "description": "A tabletop exercise is a discussion-based session where team members meet to discuss their roles during an incident and review the incident response plan."
    },
    {
        "question": "A healthcare organization wants to provide a web application that allows individuals to digitally report health emergencies. Which of the following is the most important consideration during development?",
        "options": [
            "Scalability",
            "Availability",
            "Cost",
            "Ease of deployment"
        ],
        "correct_answer": 2,
        "description": "Availability is critical for applications that deal with health emergencies, as they need to be accessible at all times to ensure prompt responses."
    },
    {
        "question": "Which of the following agreement types defines the time frame in which a vendor needs to respond?",
        "options": [
            "SOW",
            "SLA",
            "MOA",
            "MOU"
        ],
        "correct_answer": 2,
        "description": "A Service Level Agreement (SLA) outlines the expected level of service, including response times, that a vendor must adhere to."
    },
    {
        "question": "Which of the following is a feature of a next-generation SIEM system?",
        "options": [
            "Virus signatures",
            "Automated response actions",
            "Security agent deployment",
            "Vulnerability scanning"
        ],
        "correct_answer": 2,
        "description": "Next-generation SIEM systems often include automated response actions, enabling faster and more efficient responses to security incidents."
    },
    {
        "question": "To improve the security at a data center, a security administrator implements a CCTV system and posts several signs about the possibility of being filmed. Which of the following best describe these types of controls? (choose two)",
        "options": [
            "Preventive",
            "Deterrent",
            "Corrective",
            "Directive",
            "Compensating",
            "Detective"
        ],
        "correct_answer": [2, 6],
        "description": "Deterrent controls discourage potential attackers by signaling that security measures are in place, while detective controls help to identify and record unauthorized activities."
    },









    {
        "question": "Which of the following examples would be best mitigated by input sanitization?",
        "options": [
            "<script>alert('Warning!');</script>"
            "nmap - 10.11.1.130",
            "Email message: 'Click this link to get your free gift card.'",
            "Browser message: 'Your connection is not private.'"
        ],
        "correct_answer": 1,
        "description": "Input sanitization helps to prevent malicious input, such as command injection attacks, from being processed by applications."
    },
    {
        "question": "An attacker posing as the Chief Executive Officer calls an employee and instructs the employee to buy gift cards. Which of the following techniques is the attacker using?",
        "options": [
            "Smishing",
            "Disinformation",
            "Impersonating",
            "Whaling"
        ],
        "correct_answer": 3,
        "description": "Impersonating involves pretending to be someone else, in this case, the CEO, to manipulate the employee into taking certain actions."
    },
    {
        "question": "After conducting a vulnerability scan, a systems administrator notices that one of the identified vulnerabilities is not present on the systems that were scanned. Which of the following describes this example?",
        "options": [
            "False positive",
            "False negative",
            "True positive",
            "True negative"
        ],
        "correct_answer": 1,
        "description": "A false positive occurs when a scan incorrectly identifies a vulnerability that does not actually exist on the system."
    },
    {
        "question": "A recent penetration test identified that an attacker could flood the MAC address table of network switches. Which of the following would best mitigate this type of attack?",
        "options": [
            "Load balancer",
            "Port security",
            "IPS",
            "NGFW"
        ],
        "correct_answer": 2,
        "description": "Port security can help prevent MAC address flooding by limiting the number of MAC addresses that can be learned on a port, thereby mitigating this type of attack."
    },
    {
        "question": "A user would like to install software and features that are not available with a smartphone's default software. Which of the following would allow the user to install unauthorized software and enable new features?",
        "options": [
            "SQLi",
            "Cross-site scripting",
            "Jailbreaking",
            "Side loading"
        ],
        "correct_answer": 3,
        "description": "Jailbreaking involves removing software restrictions on a smartphone, allowing the installation of unauthorized software and access to additional features."
    },
    {
        "question": "Which of the following phases of an incident response involves generating reports?",
        "options": [
            "Recovery",
            "Preparation",
            "Lessons learned",
            "Containment"
        ],
        "correct_answer": 3,
        "description": "The 'Lessons learned' phase involves documenting the incident and the response to it, including generating reports to inform future incident responses."
    },
    {
        "question": "Which of the following methods would most likely be used to identify legacy systems?",
        "options": [
            "Bug bounty program",
            "Vulnerability scan",
            "Package monitoring",
            "Dynamic analysis"
        ],
        "correct_answer": 2,
        "description": "Vulnerability scans can help identify outdated software and systems that may not receive regular updates, indicating the presence of legacy systems."
    },
    {
        "question": "Employees located off-site must have access to company resources in order to complete their assigned tasks. These employees utilize a solution that allows remote access without interception concerns. Which of the following best describes this solution?",
        "options": [
            "Proxy server",
            "NGFW",
            "VPN",
            "Security zone"
        ],
        "correct_answer": 3,
        "description": "A Virtual Private Network (VPN) provides secure remote access by encrypting data transmitted between the user's device and the company's network."
    },
    {
        "question": "A company allows customers to upload PDF documents to its public e-commerce website. Which of the following would a security analyst most likely recommend?",
        "options": [
            "Utilizing attack signatures in an IDS",
            "Enabling malware detection through a UTM",
            "Limiting the affected servers with a load balancer",
            "Blocking command injections via a WAF"
        ],
        "correct_answer": 2,
        "description": "Enabling malware detection through a Unified Threat Management (UTM) solution helps to ensure that uploaded files are scanned for malware before being processed."
    },
    {
        "question": "A security analyst developed a script to automate a trivial and repeatable task. Which of the following best describes the benefits of ensuring other team members understand how the script works?",
        "options": [
            "To reduce implementation cost",
            "To identify complexity",
            "To remediate technical debt",
            "To prevent a single point of failure"
        ],
        "correct_answer": 4,
        "description": "Ensuring that multiple team members understand how the script works helps to prevent reliance on a single person, thereby reducing the risk of a single point of failure."
    },
    {
        "question": "A company is decommissioning its physical servers and replacing them with an architecture that will reduce the number of individual operating systems. Which of the following strategies should the company use to achieve this security requirement?",
        "options": [
            "Microservices",
            "Containerization",
            "Virtualization",
            "Infrastructure as code"
        ],
        "correct_answer": 2,
        "description": "Containerization allows multiple applications to run on a single operating system while isolating each application in its own container, reducing the need for multiple OS instances."
    },








    {
        "question": "An administrator needs to perform server hardening before deployment. Which of the following steps should the administrator take? (Choose two.)",
        "options": [
            "Disable default accounts.",
            "Add the server to the asset inventory.",
            "Remove unnecessary services.",
            "Document default passwords.",
            "Send server logs to the SIEM.",
            "Join the server to the corporate domain."
        ],
        "correct_answer": [1, 3],
        "description": "Disabling default accounts and removing unnecessary services are key steps in hardening a server to reduce potential attack surfaces before deployment."
    },
    {
        "question": "A Chief Information Security Officer would like to conduct frequent, detailed reviews of systems and procedures to track compliance objectives. Which of the following will be the best method to achieve this objective?",
        "options": [
            "Third-party attestation",
            "Penetration testing",
            "Internal auditing",
            "Vulnerability scans"
        ],
        "correct_answer": 3,
        "description": "Internal auditing allows for detailed and frequent reviews of systems and procedures to ensure compliance with organizational and regulatory standards."
    },
    {
        "question": "Which of the following security concepts is accomplished with the installation of a RADIUS server?",
        "options": [
            "CIA",
            "AAA",
            "ACL",
            "PEM"
        ],
        "correct_answer": 2,
        "description": "A RADIUS server is used for AAA (Authentication, Authorization, and Accounting) to manage user access and track activities within the network."
    },
    {
        "question": "After creating a contract for IT contractors, the human resources department changed several clauses. The contract has gone through three revisions. Which of the following processes should the human resources department follow to track revisions?",
        "options": [
            "Version validation",
            "Version changes",
            "Version updates",
            "Version control"
        ],
        "correct_answer": 4,
        "description": "Version control involves tracking changes to documents or software, ensuring that each revision is documented and can be referenced."
    },
    {
        "question": "The executive management team is mandating the company develop a disaster recovery plan. The cost must be kept to a minimum, and the money to fund additional internet connections is not available. Which of the following would be the best option?",
        "options": [
            "Hot site",
            "Cold site",
            "Failover site",
            "Warm site"
        ],
        "correct_answer": 2,
        "description": "A cold site is a low-cost disaster recovery option that provides a backup location where the organization can set up operations, but it requires time to be fully operational."
    },
    {
        "question": "An administrator at a small business notices an increase in support calls from employees who receive a blocked page message after trying to navigate to a spoofed website. Which of the following should the administrator do?",
        "options": [
            "Deploy multifactor authentication.",
            "Decrease the level of the web filter settings.",
            "Implement security awareness training.",
            "Update the acceptable use policy."
        ],
        "correct_answer": 3,
        "description": "Security awareness training helps employees recognize and avoid malicious websites, reducing the likelihood of successful phishing and other social engineering attacks."
    },
    {
        "question": "Which of the following teams is best suited to determine whether a company has systems that can be exploited by a potential, identified vulnerability?",
        "options": [
            "Purple team",
            "Blue team",
            "Red team",
            "White team"
        ],
        "correct_answer": 3,
        "description": "The Red team simulates attacks to identify vulnerabilities and test the effectiveness of security measures, helping to identify and mitigate potential exploitation risks."
    },
    {
        "question": "A company is reviewing options to enforce user logins after several account takeovers. The following conditions must be met as part of the solution:\n\n• Allow employees to work remotely or from assigned offices around the world.\n• Provide a seamless login experience.\n• Limit the amount of equipment required.\n\nWhich of the following best meets these conditions?",
        "options": [
            "Trusted devices",
            "Geotagging",
            "Smart cards",
            "Time-based logins"
        ],
        "correct_answer": 1,
        "description": "Trusted devices ensure that only recognized and authorized devices can access the system, providing a secure yet seamless login experience for remote workers."
    },
    {
        "question": "Which of the following methods can be used to detect attackers who have successfully infiltrated a network? (Choose two.)",
        "options": [
            "Tokenization",
            "CI/CD",
            "Honeypots",
            "Threat modeling",
            "DNS sinkhole",
            "Data obfuscation"
        ],
        "correct_answer": [3, 5],
        "description": "Honeypots and DNS sinkholes are effective tools for detecting attackers by either luring them into a controlled environment or redirecting malicious traffic."
    },
    {
        "question": "A company wants to ensure that the software it develops will not be tampered with after the final version is completed. Which of the following should the company most likely use?",
        "options": [
            "Hashing",
            "Encryption",
            "Baselines",
            "Tokenization"
        ],
        "correct_answer": 1,
        "description": "Hashing ensures the integrity of software by creating a unique value based on the contents, allowing any unauthorized changes to be easily detected."
    },
    {
        "question": "An organization completed a project to deploy SSO across all business applications last year. Recently, the finance department selected a new cloud-based accounting software vendor. Which of the following should most likely be configured during the new software deployment?",
        "options": [
            "RADIUS",
            "SAML",
            "EAP",
            "OpenID"
        ],
        "correct_answer": 2,
        "description": "Security Assertion Markup Language (SAML) is commonly used for Single Sign-On (SSO) implementations, allowing users to authenticate across multiple systems with a single set of credentials."
    },
    {
        "question": "A user, who is waiting for a flight at an airport, logs in to the airline website using the public Wi-Fi, ignores a security warning and purchases an upgraded seat. When the flight lands, the user finds unauthorized credit card charges. Which of the following attacks most likely occurred?",
        "options": [
            "Replay attack",
            "Memory leak",
            "Buffer overflow attack",
            "On-path attack"
        ],
        "correct_answer": 4,
        "description": "An on-path attack (formerly known as a man-in-the-middle attack) occurs when an attacker intercepts communication between two parties, such as during a public Wi-Fi session."
    },
    {
        "question": "A network engineer deployed a redundant switch stack to increase system availability. However, the budget can only cover the cost of one ISP connection. Which of the following best describes the potential risk factor?",
        "options": [
            "The equipment MTBF is unknown.",
            "The ISP has no SLA.",
            "An RPO has not been determined.",
            "There is a single point of failure."
        ],
        "correct_answer": 4,
        "description": "Even with redundant internal infrastructure, relying on a single ISP connection introduces a single point of failure, potentially compromising system availability."
    },
    {
        "question": "A network team segmented a critical, end-of-life server to a VLAN that can only be reached by specific devices but cannot be reached by the perimeter network. Which of the following best describe the controls the team implemented? (Choose two.)",
        "options": [
            "Managerial",
            "Physical",
            "Corrective",
            "Detective",
            "Compensating",
            "Technical",
            "Deterrent"
        ],
        "correct_answer": [5, 6],
        "description": "Technical controls like VLAN segmentation and compensating controls such as additional access restrictions help protect critical systems that cannot be updated or replaced."
    },
    {
        "question": "A threat actor was able to use a username and password to log in to a stolen company mobile device. Which of the following provides the best solution to increase mobile data security on all employees' company mobile devices?",
        "options": [
            "Application management",
            "Full disk encryption",
            "Remote wipe",
            "Containerization"
        ],
        "correct_answer": 3,
        "description": "emote wipe ensures that if a company mobile device is lost or stolen, all data can be erased remotely, preventing the threat actor from accessing sensitive company information. This method is highly effective in situations where the device is compromised."
    },
    {
        "question": "Which of the following best describes the risk present after controls and mitigating factors have been applied?",
        "options": [
            "Residual",
            "Avoided",
            "Inherent",
            "Operational"
        ],
        "correct_answer": 1,
        "description": "Residual risk is the remaining risk after controls and mitigations have been applied, representing the risk that still needs to be managed."
    },
    {
        "question": "A software development team asked a security administrator to recommend techniques that should be used to reduce the chances of the software being reverse engineered. Which of the following should the security administrator recommend?",
        "options": [
            "Digitally signing the software",
            "Performing code obfuscation",
            "Limiting the use of third-party libraries",
            "Using compile flags"
        ],
        "correct_answer": 2,
        "description": "Code obfuscation makes it more difficult for attackers to reverse engineer the software by intentionally complicating the code's structure and readability."
    },
    {
        "question": "Which of the following is a possible factor for MFA?",
        "options": [
            "Something you exhibit",
            "Something you have",
            "Somewhere you are",
            "Someone you know"
        ],
        "correct_answer": 2,
        "description": "Something you have, such as a physical token or smart card, is one of the factors used in Multi-Factor Authentication (MFA)."
    },
    {
        "question": "Easy-to-guess passwords led to an account compromise. The current password policy requires at least 12 alphanumeric characters, one uppercase character, one lowercase character, a password history of two passwords, a minimum password age of one day, and a maximum password age of 90 days. Which of the following would reduce the risk of this incident from happening again? (Choose two.)",
        "options": [
            "Increasing the minimum password length to 14 characters.",
            "Upgrading the password hashing algorithm from MD5 to SHA-512.",
            "Increasing the maximum password age to 120 days.",
            "Reducing the minimum password length to ten characters.",
            "Reducing the minimum password age to zero days.",
            "Including a requirement for at least one special character."
        ],
        "correct_answer": [1, 6],
        "description": "Increasing the minimum password length and requiring a special character would make passwords more complex and harder to guess."
    },
    {
        "question": "A user downloaded software from an online forum. After the user installed the software, the security team observed external network traffic connecting to the user's computer on an uncommon port. Which of the following is the most likely explanation of this unauthorized connection?",
        "options": [
            "The software had a hidden keylogger.",
            "The software was ransomware.",
            "The user's computer had a fileless virus.",
            "The software contained a backdoor."
        ],
        "correct_answer": 4,
        "description": "A backdoor allows unauthorized access to a system by bypassing normal authentication mechanisms, which can result in unexpected network connections."
    },
    {
        "question": "A utility company is designing a new platform that will host all the virtual machines used by business applications. The requirements include:\n\n• A starting baseline of 50% memory utilization\n• Storage scalability\n• Single circuit failure resilience\n\nWhich of the following best meets all of these requirements?",
        "options": [
            "Connecting dual PDUs to redundant power supplies",
            "Transitioning the platform to an IaaS provider",
            "Configuring network load balancing for multiple paths",
            "Deploying multiple large NAS devices for each host"
        ],
        "correct_answer": 2,
        "description": "Transitioning to an Infrastructure as a Service (IaaS) provider offers scalability and redundancy while maintaining baseline resource utilization."
    },
    {
        "question": "Which of the following best describes a use case for a DNS sinkhole?",
        "options": [
            "Attackers can see a DNS sinkhole as a highly valuable resource to identify a company's domain structure.",
            "A DNS sinkhole can be used to draw employees away from known-good websites to malicious ones owned by the attacker.",
            "A DNS sinkhole can be used to capture traffic to known-malicious domains used by attackers.",
            "A DNS sinkhole can be set up to attract potential attackers away from a company's network resources."
        ],
        "correct_answer": 3,
        "description": "A DNS sinkhole can redirect traffic from malicious domains to a safe destination, effectively capturing and neutralizing potential threats."
    },
    {
        "question": "An incident analyst finds several image files on a hard disk. The image files may contain geolocation coordinates. Which of the following best describes the type of information the analyst is trying to extract from the image files?",
        "options": [
            "Log data",
            "Metadata",
            "Encrypted data",
            "Sensitive data"
        ],
        "correct_answer": 2,
        "description": "Metadata in image files can contain geolocation coordinates, timestamps, and other data that can provide context and additional information about the file."
    },
    {
        "question": "Which of the following most likely describes why a security engineer would configure all outbound emails to use S/MIME digital signatures?",
        "options": [
            "To meet compliance standards",
            "To increase delivery rates",
            "To block phishing attacks",
            "To ensure non-repudiation"
        ],
        "correct_answer": 4,
        "description": "S/MIME (Secure/Multipurpose Internet Mail Extensions) digital signatures provide non-repudiation by allowing the recipient to verify the sender's identity and ensuring that the email has not been tampered with."
    },


# Page 6 of 7


    {
        "question": "During a recent company safety stand-down, the cyber-awareness team gave a presentation on the importance of cyber hygiene. One topic the team covered was best practices for printing centers. Which of the following describes an attack method that relates to printing centers?",
        "options": [
            "Whaling",
            "Credential harvesting",
            "Prepending",
            "Dumpster diving"
        ],
        "correct_answer": 4,
        "description": "Dumpster diving involves searching through physical waste for confidential information. In the context of printing centers, discarded documents could be exploited this way."
    },
    {
        "question": "Which of the following considerations is the most important regarding cryptography used in an IoT device?",
        "options": [
            "Resource constraints",
            "Available bandwidth",
            "The use of block ciphers",
            "The compatibility of the TLS version"
        ],
        "correct_answer": 1,
        "description": "Resource constraints such as limited processing power and memory are critical considerations when implementing cryptography in IoT devices."
    },
    {
        "question": "A coffee shop owner wants to restrict internet access to only paying customers by prompting them for a receipt number. Which of the following is the best method to use given this requirement?",
        "options": [
            "WPA3",
            "Captive portal",
            "PSK",
            "IEEE 802.1X"
        ],
        "correct_answer": 2,
        "description": "A captive portal prompts users to enter a code or other information (like a receipt number) before granting access to the internet."
    },
    {
        "question": "While performing digital forensics, which of the following is considered the most volatile and should have the contents collected first?",
        "options": [
            "Hard drive",
            "RAM",
            "SSD",
            "Temporary files"
        ],
        "correct_answer": 2,
        "description": "RAM is the most volatile form of data storage, meaning it should be collected first in a forensic investigation to avoid losing crucial information."
    },
    {
        "question": "A hosting provider needs to prove that its security controls have been in place over the last six months and have sufficiently protected customer data. Which of the following would provide the best proof that the hosting provider has met the requirements?",
        "options": [
            "NIST CSF",
            "SOC 2 Type 2 report",
            "CIS Top 20 compliance reports",
            "Vulnerability report"
        ],
        "correct_answer": 2,
        "description": "A SOC 2 Type 2 report verifies that security controls were in place over a period of time and were effective in protecting customer data."
    },
    {
        "question": "A city municipality lost its primary data center when a tornado hit the facility. Which of the following should the city staff use immediately after the disaster to handle essential public services?",
        "options": [
            "BCP",
            "Communication plan",
            "DRP",
            "IRP"
        ],
        "correct_answer": 3,
        "description": "A Disaster Recovery Plan (DRP) outlines the steps to restore essential services following a disaster, such as setting up a backup data center."
    },
{
    "question": "A systems administrator notices that a testing system is down. While investigating, the systems administrator finds that the servers are online and accessible from any device on the server network. The administrator reviews the following information from the monitoring system:\n\n| Server name | IP          | Traffic sent | Traffic received | Status |\n|-------------|-------------|--------------|------------------|--------|\n| File01      | 10.12.14.13 | 2654812      | 23185            | Up     |\n| DC01        | 10.12.15.2  | 168741       | 65481            | Up     |\n| Test01      | 10.25.1.3   | 14872        | 654123168        | Down   |\n| Test02      | 10.25.1.4   | 16941        | 651321685        | Down   |\n| DC02        | 10.12.15.3  | 32145        | 32158            | Up     |\n| Finance01   | 10.18.1.14  | 12374        | 6548             | Up     |\n\nWhich of the following is the most likely cause of the outage?",
    "options": [
        "Denial of service",
        "ARP poisoning",
        "Jamming",
        "Kerberoasting"
    ],
    "correct_answer": 1,
    "description": "The correct answer is Kerberoasting, which is a type of attack that targets service accounts in Active Directory. The large amount of received traffic on the 'Down' systems indicates that they may have been compromised by such an attack."
},
    {
        "question": "A security team has been alerted to a flood of incoming emails that have various subject lines and are addressed to multiple email inboxes. Each email contains a URL shortener link that is redirecting to a dead domain. Which of the following is the best step for the security team to take?",
        "options": [
            "Create a blocklist for all subject lines.",
            "Send the dead domain to a DNS sinkhole.",
            "Quarantine all emails received and notify all employees.",
            "Block the URL shortener domain in the web proxy."
        ],
        "correct_answer": 4,
        "description": "Sending the dead domain to a DNS sinkhole redirects any future traffic to that domain to a safe destination, effectively nullifying the attack."
    },
    {
        "question": "A security administrator is working to secure company data on corporate laptops in case the laptops are stolen. Which of the following solutions should the administrator consider?",
        "options": [
            "Disk encryption",
            "Data loss prevention",
            "Operating system hardening",
            "Boot security"
        ],
        "correct_answer": 1,
        "description": "Disk encryption ensures that even if a laptop is stolen, the data stored on it cannot be accessed without proper decryption credentials."
    },
    {
        "question": "A company needs to keep the fewest records possible, meet compliance needs, and ensure destruction of records that are no longer needed. Which of the following best describes the policy that meets these requirements?",
        "options": [
            "Security policy",
            "Classification policy",
            "Retention policy",
            "Access control policy"
        ],
        "correct_answer": 3,
        "description": "A retention policy specifies how long records should be kept and when they should be destroyed, ensuring compliance while minimizing unnecessary record-keeping."
    },
    {
        "question": "Which of the following is a common source of unintentional corporate credential leakage in cloud environments?",
        "options": [
            "Code repositories",
            "Dark web",
            "Threat feeds",
            "State actors",
            "Vulnerability databases"
        ],
        "correct_answer": 1,
        "description": "Code repositories, especially public ones, can unintentionally expose corporate credentials if they are not properly secured."
    },
    {
        "question": "Which of the following is the best reason an organization should enforce a data classification policy to help protect its most sensitive information?",
        "options": [
            "End users will be required to consider the classification of data that can be used in documents.",
            "The policy will result in the creation of access levels for each level of classification.",
            "The organization will have the ability to create security requirements based on classification levels.",
            "Security analysts will be able to see the classification of data within a document before opening it."
        ],
        "correct_answer": 3,
        "description": "Data classification policies enable organizations to apply appropriate security measures based on the sensitivity of the data, ensuring that critical information is properly protected."
    },
    {
        "question": "An analyst is performing a vulnerability scan against the web servers exposed to the internet without a system account. Which of the following is most likely being performed?",
        "options": [
            "Non-credentialed scan",
            "Packet capture",
            "Privilege escalation",
            "System enumeration",
            "Passive scan"
        ],
        "correct_answer": 1,
        "description": "A non-credentialed scan is performed without access to the internal system credentials, often to simulate an external attacker's perspective."
    },
    {
        "question": "A security administrator is hardening corporate systems and applying appropriate mitigations by consulting a real-world knowledge base for adversary behavior. Which of the following would be best for the administrator to reference?",
        "options": [
            "MITRE ATT&CK",
            "CSIRT",
            "CVSS",
            "SOAR"
        ],
        "correct_answer": 1,
        "description": "The MITRE ATT&CK framework provides detailed information on adversary tactics, techniques, and procedures, making it an ideal resource for system hardening."
    },
    {
        "question": "An architect has a request to increase the speed of data transfer using JSON requests externally. Currently, the organization uses SFTP to transfer data files. Which of the following will most likely meet the requirements?",
        "options": [
            "A website-hosted solution",
            "Cloud shared storage",
            "A secure email solution",
            "Microservices using API"
        ],
        "correct_answer": 4,
        "description": "Microservices using APIs can handle JSON requests efficiently, making them a suitable solution for fast external data transfers."
    },
    {
        "question": "Which of the following addresses individual rights such as the right to be informed, the right of access, and the right to be forgotten?",
        "options": [
            "GDPR",
            "PCI DSS",
            "NIST",
            "ISO"
        ],
        "correct_answer": 1,
        "description": "The General Data Protection Regulation (GDPR) provides individuals with various rights concerning their personal data, including the right to be forgotten."
    },
    {
        "question": "An administrator is installing an LDAP browser tool in order to view objects in the corporate LDAP directory. Secure connections to the LDAP server are required. When the browser connects to the server, certificate errors are being displayed, and then the connection is terminated. Which of the following is the most likely solution?",
        "options": [
            "The administrator should allow SAN certificates in the browser configuration.",
            "The administrator needs to install the server certificate into the local truststore.",
            "The administrator should request that the secure LDAP port be opened to the server.",
            "The administrator needs to increase the TLS version on the organization's RA."
        ],
        "correct_answer": 2,
        "description": "Installing the server certificate into the local truststore resolves the certificate errors by establishing trust between the client and server."
    },




    {
        "question": "Which of the following is the most important security concern when using legacy systems to provide production service?",
        "options": [
            "Instability",
            "Lack of vendor support",
            "Loss of availability",
            "Use of insecure protocols"
        ],
        "correct_answer": 2,
        "description": "Lack of vendor support means that legacy systems may not receive security updates, leaving them vulnerable to exploitation."
    },
    {
        "question": "A security investigation revealed that malicious software was installed on a server using a server administrator's credentials. During the investigation, the server administrator explained that Telnet was regularly used to log in. Which of the following most likely occurred?",
        "options": [
            "A spraying attack was used to determine which credentials to use.",
            "A packet capture tool was used to steal the password.",
            "A remote-access Trojan was used to install the malware.",
            "A dictionary attack was used to log in as the server administrator."
        ],
        "correct_answer": 2,
        "description": "Telnet transmits data in plaintext, making it susceptible to packet capture attacks where credentials can be easily intercepted."
    },
    {
        "question": "A user is requesting Telnet access to manage a remote development web server. Insecure protocols are not allowed for use within any environment. Which of the following should be configured to allow remote access to this server?",
        "options": [
            "HTTPS",
            "SNMPv3",
            "SSH",
            "RDP",
            "SMTP"
        ],
        "correct_answer": 3,
        "description": "SSH is a secure protocol that provides encrypted communication for managing remote servers, unlike Telnet."
    },
    {
        "question": "A security administrator is working to find a cost-effective solution to implement certificates for a large number of domains and subdomains owned by the company. Which of the following types of certificates should the administrator implement?",
        "options": [
            "Wildcard",
            "Client certificate",
            "Self-signed",
            "Code signing"
        ],
        "correct_answer": 1,
        "description": "Wildcard certificates allow an organization to secure an unlimited number of subdomains with a single certificate, making it a cost-effective solution."
    },
    {
        "question": "An auditor discovered multiple insecure ports on some servers. Other servers were found to have legacy protocols enabled. Which of the following tools did the auditor use to discover these issues?",
        "options": [
            "Nessus",
            "curl",
            "Wireshark",
            "netcat"
        ],
        "correct_answer": 1,
        "description": "Nessus is a widely used vulnerability scanner that can identify open ports, insecure services, and legacy protocols on servers."
    },
    {
        "question": "A security analyst received a tip that sensitive proprietary information was leaked to the public. The analyst is reviewing the PCAP and notices traffic between an internal server and an external host that includes the following:\n\n[PCAP data]\n\nWhich of the following was most likely used to exfiltrate the data?",
        "options": [
            "Encapsulation",
            "MAC address spoofing",
            "Steganography",
            "Broken encryption",
            "Sniffing via on-path position"
        ],
        "correct_answer": 1,
        "description": "Encapsulation can be used to disguise data exfiltration by embedding it within legitimate traffic."
    },
    {
        "question": "A company wants to reduce the time and expense associated with code deployment. Which of the following technologies should the company utilize?",
        "options": [
            "Serverless architecture",
            "Thin clients",
            "Private cloud",
            "Virtual machines"
        ],
        "correct_answer": 1,
        "description": "Serverless architecture allows for scalable and cost-effective deployment of code, reducing both the time and expenses involved."
    },
    {
        "question": "A security administrator is performing an audit on a stand-alone UNIX server, and the following message is immediately displayed:\n\n(Error 13): /etc/shadow: Permission denied.\n\nWhich of the following best describes the type of tool that is being used?",
        "options": [
            "Pass-the-hash monitor",
            "File integrity monitor",
            "Forensic analysis",
            "Password cracker"
        ],
        "correct_answer": 4,
        "description": "A file integrity monitor would alert the administrator when unauthorized changes or access attempts occur, as indicated by the permission denied error."
    },
    {
        "question": "A security administrator needs to create firewall rules for the following protocols: RTP, SIP, H.323, and SRTP. Which of the following does this rule set support?",
        "options": [
            "RTOS",
            "VoIP",
            "SoC",
            "HVAC"
        ],
        "correct_answer": 2,
        "description": "RTP, SIP, H.323, and SRTP are protocols commonly used in VoIP (Voice over IP) communications."
    },
    {
        "question": "Which of the following best describes a social engineering attack that uses a targeted electronic messaging campaign aimed at a Chief Executive Officer?",
        "options": [
            "Whaling",
            "Spear phishing",
            "Impersonation",
            "Identity fraud"
        ],
        "correct_answer": 1,
        "description": "Whaling is a form of spear phishing that specifically targets high-profile individuals like CEOs."
    },





    
    {
        "question": "During a penetration test, a flaw in the internal PKI was exploited to gain domain administrator rights using specially crafted certificates. Which of the following remediation tasks should be completed as part of the cleanup phase?",
        "options": [
            "Updating the CRL",
            "Patching the CA",
            "Changing passwords",
            "Implementing SOAR"
        ],
        "correct_answer": 2,
        "description": "Updating the Certificate Revocation List (CRL) ensures that any compromised certificates are invalidated and cannot be used in the future."
    },
    {
        "question": "A company wants to implement MFA. Which of the following enables the additional factor while using a smart card?",
        "options": [
            "PIN",
            "Hardware token",
            "User ID",
            "SMS"
        ],
        "correct_answer": 1,
        "description": "A PIN (Personal Identification Number) provides the second factor of authentication in addition to the smart card."
    },
    {
        "question": "A company hired an external consultant to assist with required system upgrades to a critical business application. A systems administrator needs to secure the consultant's access without sharing passwords to critical systems. Which of the following solutions should most likely be utilized?",
        "options": [
            "TACACS+",
            "SAML",
            "An SSO platform",
            "Role-based access control",
            "PAM software"
        ],
        "correct_answer": 5,
        "description": "Privileged Access Management (PAM) software allows the company to grant secure, temporary access to sensitive systems without sharing passwords."
    },
    {
        "question": "A newly implemented wireless network is designed so that visitors can connect to the wireless network for business activities. The legal department is concerned that visitors might connect to the network and perform illicit activities. Which of me following should the security team implement to address this concern?",
        "options": [
            "Configure a RADIUS server to manage device authentication.",
            "Use 802.1X on all devices connecting to wireless.",
            "Add a guest captive portal requiring visitors to accept terms and conditions.",
            "Allow for new devices to be connected via WPS."
        ],
        "correct_answer": 3,
        "description": "A guest captive portal requiring visitors to accept terms and conditions helps prevent illicit activities by establishing legal boundaries for network use."
    },
    {
        "question": "Which of the following data roles is responsible for identifying risks and appropriate access to data?",
        "options": [
            "Owner",
            "Custodian",
            "Steward",
            "Controller"
        ],
        "correct_answer": 1,
        "description": "The data owner is responsible for defining access controls and identifying potential risks related to the data."
    },
    {
        "question": "Which of the following physical controls can be used to both detect and deter? (Choose two.)",
        "options": [
            "Lighting",
            "Fencing",
            "Signage",
            "Sensor",
            "Bollard",
            "Lock"
        ],
        "correct_answer": [1, 4],
        "description": "Lighting and sensors can both deter unauthorized access and detect intrusions when they occur."
    },
    {
        "question": "A multinational bank hosts several servers in its data center. These servers run a business-critical application used by customers to access their account information. Which of the following should the bank use to ensure accessibility during peak usage times?",
        "options": [
            "Load balancer",
            "Cloud backups",
            "Geographic dispersal",
            "Disk multipathing"
        ],
        "correct_answer": 1,
        "description": "A load balancer distributes traffic across multiple servers to ensure the application remains accessible during peak usage."
    },
    {
        "question": "The author of a software package is concerned about bad actors repackaging and inserting malware into the software. The software download is hosted on a website, and the author exclusively controls the website's contents. Which of the following techniques would best ensure the software's integrity?",
        "options": [
            "Input validation",
            "Code signing",
            "Secure cookies",
            "Fuzzing"
        ],
        "correct_answer": 2,
        "description": "Code signing allows the author to digitally sign the software, providing a way for users to verify that it has not been tampered with."
    },
    {
        "question": "A third-party vendor is moving a particular application to the end-of-life stage at the end of the current year. Which of the following is the most critical risk if the company chooses to continue running the application?",
        "options": [
            "Lack of security updates",
            "Lack of new features",
            "Lack of support",
            "Lack of source code access"
        ],
        "correct_answer": 1,
        "description": "The lack of security updates poses the most critical risk as vulnerabilities in the application will remain unpatched."
    },
    {
        "question": "A security analyst recently read a report about a flaw in several of the organization's printer models that causes credentials to be sent over the network in cleartext, regardless of the encryption settings. Which of the following would be best to use to validate this finding?",
        "options": [
            "Wireshark",
            "netcat",
            "Nessus",
            "Nmap"
        ],
        "correct_answer": 1,
        "description": "Wireshark can capture and analyze network traffic, making it ideal for verifying whether credentials are indeed being sent in cleartext."
    },
    {
        "question": "A development team is launching a new public-facing web product. The Chief Information Security Officer has asked that the product be protected from attackers who use malformed or invalid inputs to destabilize the system. Which of the following practices should the development team implement?",
        "options": [
            "Fuzzing",
            "Continuous deployment",
            "Static code analysis",
            "Manual peer review"
        ],
        "correct_answer": 1,
        "description": "Fuzzing involves testing an application by inputting malformed or unexpected data to identify potential security vulnerabilities."
    },
    {
        "question": "During an annual review of the system design, an engineer identified a few issues with the currently released design. Which of the following should be performed next according to best practices?",
        "options": [
            "Risk management process",
            "Product design process",
            "Design review process",
            "Change control process"
        ],
        "correct_answer": 4,
        "description": "A design review process should be initiated to address and rectify the identified issues with the system design."
    },
    {
        "question": "Which of the following is best to use when determining the severity of a vulnerability?",
        "options": [
            "CVE",
            "OSINT",
            "SOAR",
            "CVSS"
        ],
        "correct_answer": 4,
        "description": "The Common Vulnerability Scoring System (CVSS) is a standardized method for assessing the severity of security vulnerabilities."
    },
    {
        "question": "An organization experienced a security breach that allowed an attacker to send fraudulent wire transfers from a hardened PC exclusively to the attacker's bank through remote connections. A security analyst is creating a timeline of events and has found a different PC on the network containing malware. Upon reviewing the command history, the analyst finds the following:\n\n[Command history]\n\nWhich of the following best describes how the attacker gained access to the hardened PC?",
        "options": [
            "The attacker created fileless malware that was hosted by the banking platform.",
            "The attacker performed a pass-the-hash attack using a shared support account.",
            "The attacker utilized living-off-the-land binaries to evade endpoint detection and response software.",
            "The attacker socially engineered the accountant into performing bad transfers."
        ],
        "correct_answer": 2,
        "description": "A pass-the-hash attack involves capturing and reusing hashed credentials, which likely allowed the attacker to gain access to the hardened PC."
    },
    {
        "question": "Which of the following is the best resource to consult for information on the most common application exploitation methods?",
        "options": [
            "OWASP",
            "STIX",
            "OVAL",
            "Threat intelligence feed",
            "Common Vulnerabilities and Exposures"
        ],
        "correct_answer": 1,
        "description": "The OWASP (Open Web Application Security Project) provides resources and documentation on common application security risks and exploitation methods."
    },
{
    "question": "A security analyst is reviewing the logs on an organization’s DNS server and notices the following unusual snippet: Log from named: post-processed 20230102 0045L ... qry_source: 124.22.158.37 TCP/53 qry_dest: 52.165.16.154 TCP/53 qry_dest: 10.100.50.5 TCP/53 qry_type: AXFR | zone int.comptia.org ------------------------| www A 10.100.50.21 ------------------------| dns A 10.100.5.5 ------------------------| adds A 10.101.10.10 ------------------------| fshare A 10.101.10.20 ------------------------| sip A 10.100.5.11 ... Which of the following attack techniques was most likely used?",
    "options": [
        "Determining the organization’s ISP-assigned address space",
        "Bypassing the organization’s DNS sinkholing",
        "Footprinting the internal network",
        "Attempting to achieve initial access to the DNS server",
        "Exfiltrating data from fshare.int.complia.org"
    ],
    "correct_answer": 3,
    "description": "Footprinting the internal network is the most likely attack technique in this scenario, where the attacker is gathering information about internal DNS records."
},
    {
        "question": "A security analyst at an organization observed several user logins from outside the organization's network. The analyst determined that these logins were not performed by individuals within the organization. Which of the following recommendations would reduce the likelihood of future attacks? (Choose two.)",
        "options": [
            "Disciplinary actions for users",
            "Conditional access policies",
            "More regular account audits",
            "Implementation of additional authentication factors",
            "Enforcement of content filtering policies",
            "A review of user account permissions"
        ],
        "correct_answer": [2, 4],
        "description": "Conditional access policies and implementing additional authentication factors, such as MFA, can reduce the risk of unauthorized logins."
    },
    {
        "question": "A security team is addressing a risk associated with the attack surface of the organization's web application over port 443. Currently, no advanced network security capabilities are in place. Which of the following would be best to set up? (Choose two.)",
        "options": [
            "NIDS",
            "Honeypot",
            "Certificate revocation list",
            "HIPS",
            "WAF",
            "SIEM"
        ],
        "correct_answer": [5, 1],
        "description": "Implementing a Web Application Firewall (WAF) and Security Information and Event Management (SIEM) will help in monitoring and protecting the web application over port 443."
    },
    {
        "question": "A systems administrator would like to create a point-in-time backup of a virtual machine. Which of the following should the administrator use?",
        "options": [
            "Replication",
            "Simulation",
            "Snapshot",
            "Containerization"
        ],
        "correct_answer": 3,
        "description": "A snapshot captures the state of a virtual machine at a specific point in time, allowing for a quick restore if needed."
    },
    {
        "question": "A security administrator notices numerous unused, non-compliant desktops are connected to the network. Which of the following actions would the administrator most likely recommend to the management team?",
        "options": [
            "Monitoring",
            "Decommissioning",
            "Patching",
            "Isolating"
        ],
        "correct_answer": 2,
        "description": "Decommissioning unused and non-compliant desktops reduces the risk they pose to the network."
    },
    {
        "question": "Which of the following is a common data removal option for companies that want to wipe sensitive data from hard drives in a repeatable manner but allow the hard drives to be reused?",
        "options": [
            "Sanitization",
            "Formatting",
            "Degaussing",
            "Defragmentation"
        ],
        "correct_answer": 1,
        "description": "Sanitization involves securely wiping data from storage devices in a way that allows them to be reused."
    },
    {
        "question": "An organization wants to improve the company's security authentication method for remote employees. Given the following requirements:\n\n• Must work across SaaS and internal network applications\n• Must be device manufacturer agnostic\n• Must have offline capabilities\n\nWhich of the following would be the most appropriate authentication method?",
        "options": [
            "Username and password",
            "Biometrics",
            "SMS verification",
            "Time-based tokens"
        ],
        "correct_answer": 4,
        "description": "Time-based tokens provide a robust, device-agnostic method of authentication that works across various platforms and applications, including offline use."
    },


# Page 7 of 7


    {
        "question": "A security officer is implementing a security awareness program and has placed security-themed posters around the building and assigned online user training. Which of the following will the security officer most likely implement?",
        "options": [
            "Password policy",
            "Access badges",
            "Phishing campaign",
            "Risk assessment"
        ],
        "correct_answer": 3,
        "description": "Phishing campaigns are often implemented alongside security awareness programs to educate employees on identifying and avoiding phishing attacks."
    },
    {
        "question": "A malicious update was distributed to a common software platform and disabled services at many organizations. Which of the following best describes this type of vulnerability?",
        "options": [
            "DDoS attack",
            "Rogue employee",
            "Insider threat",
            "Supply chain"
        ],
        "correct_answer": 4,
        "description": "A supply chain attack occurs when attackers compromise a trusted third-party service, software, or hardware to infiltrate a larger organization."
    },
    {
        "question": "A company web server is initiating outbound traffic to a low-reputation, public IP on a non-standard port. The web server is used to present an unauthenticated page to clients who upload images to the company. An analyst notices a suspicious process running on the server that was not created by the company development team. Which of the following is the most likely explanation for this security incident?",
        "options": [
            "A web shell has been deployed to the server through the page.",
            "A vulnerability has been exploited to deploy a worm to the server.",
            "Malicious insiders are using the server to mine cryptocurrency.",
            "Attackers have deployed a rootkit Trojan to the server over an exposed RDP port."
        ],
        "correct_answer": 1,
        "description": "A web shell is a malicious script uploaded to a web server to allow remote command execution, often through file upload vulnerabilities."
    },
    {
        "question": "An organization requests a third-party full-spectrum analysis of its supply chain. Which of the following would the analysis team use to meet this requirement?",
        "options": [
            "Vulnerability scanner",
            "Penetration test",
            "SCAP",
            "Illumination tool"
        ],
        "correct_answer": 4,
        "description": "An illumination tool is used to analyze and map the entire supply chain, identifying potential risks and vulnerabilities throughout the network."
    },
    {
        "question": "A systems administrator deployed a monitoring solution that does not require installation on the endpoints that the solution is monitoring. Which of the following is described in this scenario?",
        "options": [
            "Agentless solution",
            "Client-based solution",
            "Open port",
            "File-based solution"
        ],
        "correct_answer": 1,
        "description": "An agentless solution monitors systems and networks without requiring software agents to be installed on the endpoints, reducing overhead and simplifying deployment."
    },
    {
        "question": "A security analyst is reviewing the source code of an application in order to identify misconfigurations and vulnerabilities. Which of the following kinds of analysis best describes this review?",
        "options": [
            "Dynamic",
            "Static",
            "Gap",
            "Impact"
        ],
        "correct_answer": 2,
        "description": "Static analysis involves reviewing source code to identify potential security vulnerabilities before the application is run or deployed."
    }
]
