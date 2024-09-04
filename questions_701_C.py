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
            "description": "Running daily vulnerability scans helps to ensure that all systems are consistently up-to-date with the latest security patches (status of patching installations), thereby reducing the risk of unpatched vulnerabilities.\n- Tracking the status of patching installations is crucial as unpatched systems can be exploited by attackers, making this the primary reason for daily scans.\n- Finding shadow IT cloud deployments refers to identifying unauthorized cloud services, which are not typically found through standard vulnerability scans.\n- Continuously monitoring hardware inventory involves tracking physical devices, which is not the primary focus of vulnerability scans.\n- Hunting for active attackers requires different tools and methods, such as intrusion detection systems (IDS) and monitoring suspicious activities.\n\n**Domain 5: Governance, Risk, and Compliance**"
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
            "description": "A load balancer is used to distribute traffic across multiple servers to ensure that services remain available even if one server fails, which is a key component of high availability in cloud environments.\n- An access broker manages access permissions but does not directly contribute to high availability.\n- A Cloud HSM (Hardware Security Module) provides key management and encryption but is not specifically related to high availability.\n- A WAF (Web Application Firewall) protects against web attacks but does not manage high availability.\n- A load balancer distributes network traffic to multiple servers to ensure continuous availability and prevent downtime.\n\n**Domain 3: Implementation**"
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
            "description": "An encrypted connection ensures that data transmitted between IoT devices and the cloud platform is secure and protected from interception or tampering.\n- Encrypted connection protects data in transit by ensuring that it cannot be read or modified by unauthorized parties.\n- Federated identity allows users to access multiple systems with a single identity but does not address data security during transmission.\n- A firewall controls network traffic based on rules but does not specifically protect data transmitted over a network.\n- Single sign-on simplifies authentication by allowing users to access multiple applications with one set of credentials but does not encrypt data.\n\n**Domain 1: Attacks, Threats, and Vulnerabilities**"
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
            "description": "Insider threat actors often use removable devices like USB drives to easily and covertly transfer sensitive data out of an organization.\n\n- Unidentified removable devices can be used by insiders to export data without detection.\n- Default network device credentials are more related to initial unauthorized access rather than data exfiltration.\n- Spear phishing emails target individuals to obtain sensitive information but are less directly related to physical data transfer.\n- Impersonation through typosquatting involves creating deceptive websites to steal data but does not involve physical data transfer methods.\n\n**Domain 1: Attacks, Threats, and Vulnerabilities**"
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
            "description": "Masking is the process of hiding parts of sensitive data, such as displaying only the last four digits of a credit card number, while ensuring that the full data remains secure.\n\n- Encryption secures data by converting it into a coded format, but does not specifically limit visibility to only part of the data.\n- Hashing converts data into a fixed-length hash value, which cannot be reversed to reveal the original data, but does not allow partial visibility.\n- Masking hides parts of sensitive data to allow limited visibility, such as showing only the last four digits of a credit card number.\n- Tokenization replaces sensitive data with tokens, but may not meet the requirement of partially viewing the original data.\n\n**Domain 5: Governance, Risk, and Compliance**"
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
            "description": "Fines are often the direct and immediate consequence of non-compliance with data privacy regulations, which can be substantial and provide a strong justification for additional resources.\n\n- Fines are financial penalties imposed for non-compliance and can be significant, making them a direct consequence.\n- Reputational damage affects the company’s public image but is not a direct financial consequence.\n- Sanctions may include various penalties but are typically broader than just financial fines.\n- Contractual implications involve potential breaches of agreements but do not directly quantify the immediate financial impact as fines do.\n\n**Domain 5: Governance, Risk, and Compliance**"
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
            "description": "False positives, or alerts that incorrectly indicate a threat when none exists, can lead to alert fatigue, where users start ignoring alerts altogether.\n\n- True positive alerts correctly identify actual threats and are generally acted upon.\n- True negative alerts correctly identify non-threats and are usually not problematic.\n- False positive alerts incorrectly indicate a threat, causing alert fatigue and potential ignoring of future alerts.\n- False negative alerts fail to identify actual threats, which may lead to unnoticed issues but do not directly cause ignoring of alerts.\n\n**Domain 4: Operations and Incident Response**"
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
            "description": "Memory injection vulnerabilities can allow attackers to manipulate the memory of a process, potentially leading to unauthorized outbound traffic.\n\n- Memory injection involves manipulating application memory to execute unauthorized code or actions, which can result in abnormal behavior like unexpected traffic.\n- Race condition occurs when multiple processes access shared resources in an unpredictable sequence, but it is less likely to cause abnormal outbound traffic.\n- Side loading involves installing unauthorized applications but does not specifically explain unexpected outbound traffic.\n- SQL injection involves inserting malicious SQL queries into a database but is not typically related to outbound traffic issues.\n\n**Domain 1: Attacks, Threats, and Vulnerabilities**"
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
            "description": "Maintaining an asset inventory is crucial for tracking which systems are in place and ensuring that all relevant systems are patched when necessary.\n\n- Asset inventory tracks all hardware and software assets, helping to identify which systems need updates.\n- Network enumeration involves identifying devices and services on a network but does not specifically track system updates.\n- Data certification ensures data quality and accuracy but does not relate to managing system patches.\n- Procurement process involves acquiring assets but does not track existing systems for updates.\n\n**Domain 5: Governance, Risk, and Compliance**"
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
            "description": "Improving incident response requires clear, actionable guidance that can be quickly followed during a security event.\n\n- Playbooks provide step-by-step guidance on responding to specific incidents, helping to standardize and improve the incident response process.\n- Frameworks offer a broad structure for implementing security measures but are not specific to incident response procedures.\n- Baselines establish normal operational behavior, used to detect anomalies but not for guiding incident response.\n- Benchmarks set standards for performance or efficiency but are not directly related to incident response.\n\n**Domain 4: Operations and Incident Response**"
        },
        {
            "question": "Which of the following describes an executive team that is meeting in a boardroom and testing the company's incident response plan?",
            "options": [
                "Continuity of operations",
                "Capacity planning",
                "Tabletop exercise",
                "Parallel processing"
            ],
            "correct_answer": 3,
            "description": "Testing an incident response plan helps ensure that the organization is prepared for potential security incidents.\n\n- A continuity of operations plan focuses on keeping critical functions running during disruptions, not specifically testing incident response.\n- Capacity planning involves ensuring that resources can handle current and future demands, unrelated to incident response testing.\n- A tabletop exercise is a discussion-based session where team members review and discuss their roles during an incident, fitting the scenario.\n- Parallel processing involves simultaneously running multiple tasks, not related to incident response testing.\n\n**Domain 4: Operations and Incident Response**"
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
            "description": "Web applications dealing with health emergencies must be reliable and accessible at all times.\n\n-g Scalability ensures the application can handle growing user demand, but it’s not as critical as availability for emergency reporting.\n- Availability is crucial for applications dealing with health emergencies, as they must be accessible 24/7 to ensure prompt responses.\n- Cost is always a consideration, but in this context, it is secondary to ensuring the application is always available.\n- Ease of deployment makes the application quicker to launch but does not address the need for continuous availability.\n\n**Domain 3: Implementation**"
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
            "description": "Agreements with vendors often specify response times and service expectations.\n\n-g A Statement of Work (SOW) defines project-specific activities, deliverables, and timelines but does not focus on response times.\n- A Service Level Agreement (SLA) outlines the expected level of service, including response times, making it the correct choice.\n- A Memorandum of Agreement (MOA) is a document describing a bilateral agreement, not necessarily including response times.\n- A Memorandum of Understanding (MOU) is a non-binding agreement between parties and typically does not define response times.\n\n**Domain 5: Governance, Risk, and Compliance**"
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
            "description": "Next-generation Security Information and Event Management (SIEM) systems are designed to enhance security monitoring and response.\n\n-g Virus signatures are part of traditional antivirus software, not a core feature of SIEM systems.\n- Automated response actions allow SIEM systems to react quickly to detected threats, a key feature of next-generation systems.\n- Security agent deployment is part of endpoint protection, not a SIEM feature.\n- Vulnerability scanning is typically performed by separate tools, though SIEM systems may ingest the results for analysis.\n\n**Domain 4: Operations and Incident Response**"
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
            "description": "Implementing security measures involves a combination of different control types.\n\n-g Preventive controls aim to stop security incidents before they happen, but CCTV is not primarily preventive.\n- Deterrent controls discourage potential attackers by signaling that security measures are in place, like CCTV signs.\n- Corrective controls restore systems after an incident, unrelated to CCTV.\n- Directive controls dictate what actions should be taken, but do not apply here.\n- Compensating controls provide alternative measures when primary controls are not possible.\n- Detective controls help to identify and record unauthorized activities, which CCTV systems do.\n\n**Domain 3: Implementation**"
        },

       









        {
            "question": "Which of the following examples would be best mitigated by input sanitization?",
            "options": [
                "<script>alert('Warning!');</script>",
                "nmap - 10.11.1.130",
                "Email message: 'Click this link to get your free gift card.'",
                "Browser message: 'Your connection is not private.'"
            ],
            "correct_answer": 1,
            "description": "Input sanitization is a crucial security measure to prevent various types of injection attacks.\n\n-g The script example is a potential cross-site scripting (XSS) attack, which can be mitigated by input sanitization.\n- The nmap command is a network scanning tool, not related to input sanitization.\n- The email message example is related to phishing, not input sanitization.\n- The browser message is a security warning about SSL/TLS, unrelated to input sanitization.\n\n**Domain 1: Attacks, Threats, and Vulnerabilities**"
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
            "description": "Impersonating involves the attacker pretending to be someone else, in this case, the Chief Executive Officer, to deceive the employee into performing actions such as buying gift cards. This technique is part of social engineering attacks, where the attacker uses manipulation rather than technical hacking to achieve their goals.\n\n-g Smishing involves using SMS text messages to deceive individuals, not phone calls.\n- Disinformation is the deliberate spread of false information, unrelated to this scenario.\n- Impersonating involves pretending to be someone else, which is part of the whaling technique but not the specific term used here.\n- Whaling is a type of phishing attack targeted at high-profile individuals, fitting the scenario described.\n\n**Domain 1: Attacks, Threats, and Vulnerabilities**"
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
            "description": "Understanding the accuracy of vulnerability scans is important for effective security management.\n\n-g A false positive occurs when a vulnerability is incorrectly identified, fitting the scenario.\n- A false negative occurs when a vulnerability is not identified by the scan, which is not the case here.\n- A true positive is when a vulnerability is correctly identified, not applicable here.\n- A true negative occurs when the scan correctly identifies no vulnerabilities, which is also not the case.\n\n**Domain 5: Governance, Risk, and Compliance**"
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
            "description": "Mitigating network attacks requires appropriate controls and configurations.\n\n-g A load balancer distributes network traffic but does not prevent MAC address table flooding.\n- Port security limits the number of MAC addresses learned on a port, effectively mitigating the attack described.\n- An Intrusion Prevention System (IPS) detects and prevents network threats, but does not specifically address MAC address table flooding.\n- A Next-Generation Firewall (NGFW) offers advanced security features but is not directly related to this type of attack.\n\n**Domain 3: Implementation**"
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
            "description": "Modifying smartphone software often involves bypassing restrictions set by the device manufacturer.\n\n-g SQL injection (SQLi) is a type of attack against databases, not related to smartphone software.\n- Cross-site scripting (XSS) is a web security vulnerability, unrelated to smartphone software installation.\n- Jailbreaking removes restrictions on a smartphone, allowing the installation of unauthorized software and new features.\n- Side loading involves installing apps from outside the official app store, but jailbreaking is specifically required to enable such features.\n\n**Domain 3: Implementation**"
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
            "description": "Incident response involves several phases, each with specific tasks.\n\n-g The Recovery phase focuses on restoring systems to normal operation, not report generation.\n- The Preparation phase involves planning and readiness activities before an incident occurs.\n- The Lessons learned phase includes reviewing the incident and generating reports to document what happened and how it was handled.\n- The Containment phase is about limiting the spread of the incident, not generating reports.\n\n**Domain 4: Operations and Incident Response**"
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
            "description": "Identifying legacy systems is crucial for maintaining security and compatibility within an organization.\n\n-g A bug bounty program encourages external researchers to find vulnerabilities, not specifically for identifying legacy systems.\n- A vulnerability scan can help identify outdated systems and software that may not receive regular updates, indicating legacy systems.\n- Package monitoring tracks installed software packages, which may help identify legacy software but is not the primary method.\n- Dynamic analysis tests software during execution, not typically used for identifying legacy systems.\n\n**Domain 1: Attacks, Threats, and Vulnerabilities**"
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
            "description": "Ensuring secure remote access is essential for employees working off-site.\n\n-g A proxy server acts as an intermediary for requests from clients seeking resources, but does not inherently provide encryption.\n- A Next-Generation Firewall (NGFW) provides advanced network security features but is not specifically designed for remote access.\n- A Virtual Private Network (VPN) provides secure, encrypted remote access, preventing interception of data in transit.\n- A security zone is a network segment with specific security policies but does not describe a remote access solution.\n\n**Domain 3: Implementation**"
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
            "description": "Ensuring that uploaded files do not pose a security risk is critical for public-facing websites.\n\n- Utilizing attack signatures in an Intrusion Detection System (IDS) helps detect known threats but is not specific to file uploads.\n- Enabling malware detection through a Unified Threat Management (UTM) solution helps ensure that uploaded files are scanned for malware.\n- Limiting servers with a load balancer helps with traffic distribution, not directly with file security.\n- Blocking command injections via a Web Application Firewall (WAF) protects against certain types of attacks but is not specific to file uploads.\n\n**Domain 3: Implementation**"
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
            "description": "Automating tasks can increase efficiency, but it’s important to ensure the team is familiar with the process.\n\n- Reducing implementation costs is a benefit of automation, but not the primary reason for sharing script knowledge.\n- Identifying complexity in the script is important, but does not directly address the issue of shared knowledge.\n- Remediating technical debt is about resolving outdated or poorly maintained code, not directly related to script sharing.\n- Preventing a single point of failure by ensuring multiple team members understand how the script works is crucial for continuity.\n\n**Domain 4: Operations and Incident Response**"
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
            "description": "Modernizing infrastructure often involves reducing the overhead of managing multiple systems.\n\n- Microservices involve breaking down applications into smaller, manageable services, but they do not reduce the number of operating systems.\n- Containerization allows multiple applications to run on a single operating system, reducing the number of individual OS instances.\n- Virtualization allows multiple operating systems to run on a single physical server, but does not reduce the number of operating systems overall.\n- Infrastructure as code is a method of managing and provisioning infrastructure through code, unrelated to reducing operating systems.\n\n**Domain 3: Implementation**"
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
            "description": "Server hardening involves taking steps to reduce security risks before deployment.\n\n- Disabling default accounts prevents unauthorized access using common credentials.\n- Adding the server to the asset inventory is important for tracking but does not directly contribute to hardening.\n- Removing unnecessary services reduces the attack surface by limiting potential entry points for attackers.\n- Documenting default passwords is important for tracking but does not enhance security if those passwords are not changed.\n- Sending server logs to the Security Information and Event Management (SIEM) system is useful for monitoring but not a hardening step.\n- Joining the server to the corporate domain is an administrative task, not directly related to hardening.\n\n**Domain 3: Implementation**"
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
            "description": "Ensuring compliance with security policies and procedures requires regular review.\n\n- Third-party attestation involves external validation, not frequent internal reviews.\n- Penetration testing evaluates security by simulating attacks but is not focused on tracking compliance.\n- Internal auditing allows for detailed, frequent reviews of systems and procedures to ensure they meet compliance objectives.\n- Vulnerability scans identify security weaknesses but do not provide a comprehensive review of compliance with procedures.\n\n**Domain 5: Governance, Risk, and Compliance**"
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
            "description": "RADIUS servers are used to manage network access and track user activities.\n\n- CIA (Confidentiality, Integrity, Availability) is a foundational concept in security, but not directly related to RADIUS.\n- AAA (Authentication, Authorization, and Accounting) is a security framework that RADIUS implements to manage user access and activities.\n- ACL (Access Control List) defines access permissions but is not directly related to RADIUS.\n- PEM (Privacy-Enhanced Mail) is an email security protocol, unrelated to RADIUS.\n\n**Domain 3: Implementation**"
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
            "description": "Tracking document changes is important for maintaining accurate records.\n\n- Version validation is the process of confirming the accuracy of a version but does not track revisions.\n- Version changes occur when a document is modified, but the process of tracking these changes is separate.\n- Version updates refer to the process of updating a document, but not specifically to tracking.\n- Version control is the process of tracking and managing changes to documents, ensuring each revision is documented and traceable.\n\n**Domain 5: Governance, Risk, and Compliance**"
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
            "description": "Disaster recovery planning involves selecting a site that meets both budget and operational needs.\n\n- A hot site is fully operational and ready for immediate use, but it is also the most expensive option.\n- A cold site provides a basic location that requires setup before it can be used, making it a cost-effective solution.\n- A failover site is a location where operations can quickly transfer, but this generally requires more infrastructure than a cold site.\n- A warm site is partially equipped and ready for operation, but more expensive than a cold site.\n\n**Domain 5: Governance, Risk, and Compliance**"
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
            "description": "Educating employees on security practices can reduce the risk of falling victim to threats.\n\n- Deploying multifactor authentication (MFA) enhances login security, but does not directly address this issue.\n- Decreasing the level of web filter settings would make it easier to access potentially harmful sites, not recommended.\n- Implementing security awareness training helps employees recognize and avoid spoofed websites and other threats.\n- Updating the acceptable use policy defines what employees can do, but does not directly prevent them from being tricked.\n\n**Domain 5: Governance, Risk, and Compliance**"
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
    "description": "Identifying vulnerabilities is a critical aspect of security management.\n\n- The Purple team combines defensive and offensive strategies but does not focus solely on identifying vulnerabilities.\n- The Blue team is responsible for defending against attacks, not specifically identifying vulnerabilities.\n- The Red team conducts simulated attacks to discover vulnerabilities, making them the best choice for this task.\n- The White team typically provides oversight and evaluation, rather than direct vulnerability identification.\n\n**Domain 1: Attacks, Threats, and Vulnerabilities**"
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
    "description": "Ensuring secure and convenient login processes is essential for a global workforce.\n\n- Trusted devices allow only recognized and authorized devices to access systems, meeting the seamless login and limited equipment requirements.\n- Geotagging tracks the location of users but does not directly enforce secure logins.\n- Smart cards provide a secure login but require additional hardware, which might not fit the limited equipment requirement.\n- Time-based logins restrict access to specific times, which may not be practical for a globally dispersed workforce.\n\n**Domain 3: Implementation**"
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
    "description": "Detecting network intrusions requires specific strategies:\n\n- Tokenization is a method of protecting sensitive data, not detecting intrusions.\n- CI/CD (Continuous Integration/Continuous Deployment) is a software development practice, not related to intrusion detection.\n- Honeypots are decoy systems designed to attract and monitor attackers, making them effective for intrusion detection.\n- Threat modeling identifies potential threats during the design phase but does not help in real-time detection.\n- A DNS sinkhole redirects malicious traffic to a controlled environment, helping to detect and neutralize threats.\n- Data obfuscation hides sensitive data but does not directly aid in intrusion detection.\n\n**Domain 1: Attacks, Threats, and Vulnerabilities**"
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
    "description": "Protecting software integrity is vital to prevent tampering:\n\n- Hashing creates a unique value (hash) based on the software's contents, enabling detection of any unauthorized changes.\n- Encryption secures data by converting it into an unreadable format but does not ensure that the software remains untampered.\n- Baselines provide a standard for system configuration or performance but do not specifically protect software integrity.\n- Tokenization replaces sensitive data with non-sensitive equivalents, unrelated to software integrity.\n\n**Domain 3: Implementation**"
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
    "description": "Configuring authentication for new software should align with existing systems:\n\n- RADIUS (Remote Authentication Dial-In User Service) is used for network access authentication but is not typically involved in SSO (Single Sign-On).\n- SAML (Security Assertion Markup Language) is a common protocol used for SSO, making it the best choice for integrating the new software.\n- EAP (Extensible Authentication Protocol) is used in wireless networks and point-to-point connections, not SSO.\n- OpenID is another identity protocol but SAML is more commonly used in enterprise SSO solutions.\n\n**Domain 3: Implementation**"
},
{
    "question": "A user, who is waiting for a flight at an airport, logs in to the airline website using the public Wi-Fi, ignores a security warning, and purchases an upgraded seat. When the flight lands, the user finds unauthorized credit card charges. Which of the following attacks most likely occurred?",
    "options": [
        "Replay attack",
        "Memory leak",
        "Buffer overflow attack",
        "On-path attack"
    ],
    "correct_answer": 4,
    "description": "Understanding common attack methods helps in identifying potential risks:\n\n- A Replay attack involves capturing and reusing legitimate data transmissions, which does not fit the scenario.\n- Memory leaks occur when software does not manage memory allocation properly, unrelated to the scenario.\n- A Buffer overflow attack involves overwriting memory with excessive data, also unrelated to the situation.\n- An On-path attack (formerly known as a Man-in-the-Middle attack) occurs when an attacker intercepts communication, which is likely in this scenario where the user ignored a security warning on public Wi-Fi.\n\n**Domain 1: Attacks, Threats, and Vulnerabilities**"
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
    "description": "Understanding risk factors is crucial in network management:\n\n- MTBF (Mean Time Between Failures) is important for understanding equipment reliability, but it does not directly address the redundancy issue.\n- An SLA (Service Level Agreement) defines the service expectations with the ISP, but the primary concern here is redundancy.\n- RPO (Recovery Point Objective) defines the maximum tolerable period in which data might be lost due to an incident, but does not directly address availability.\n- Having only one ISP connection introduces a Single Point of Failure (SPOF), meaning if the ISP fails, the entire system could be impacted, making it the most critical risk.\n\n**Domain 2: Architecture and Design**"
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
    "description": "Implementing the right controls ensures the protection of critical systems:\n\n- Managerial controls are policy-based and administrative, not directly applied in this scenario.\n- Physical controls involve securing the physical environment, not relevant to network segmentation.\n- Corrective controls are actions taken after a security incident to mitigate damage, which does not apply here.\n- Detective controls are used to identify and alert on incidents, but the scenario is about preventing access.\n- Compensating controls provide alternative measures when primary controls are not feasible, fitting the scenario where additional access restrictions are applied.\n- Technical controls involve using technology to enforce security measures, like VLAN segmentation, which is applied here.\n- Deterrent controls discourage security violations but are not the main focus in this scenario.\n\n**Domain 3: Implementation**"
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
    "description": "Securing mobile devices is critical to protecting company data:\n\n- Application management controls which apps can be installed but does not prevent access to data if a device is stolen.\n- Full disk encryption protects data at rest, but if the attacker has login credentials, they can access the device.\n- Remote wipe allows an organization to erase data on a stolen or lost device, preventing unauthorized access to sensitive information, making it the best solution here.\n- Containerization separates personal and company data on a device but does not protect data if the device is compromised.\n\n**Domain 3: Implementation**"
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
    "description": "Understanding different types of risks is essential in risk management:\n\n- Residual risk is the remaining risk after all controls and mitigations have been applied, which still needs to be managed.\n- Avoided risk refers to a risk that has been completely eliminated, not applicable here.\n- Inherent risk is the level of risk before any controls are applied, unrelated to this scenario.\n- Operational risk refers to the risk of loss from inadequate or failed internal processes, which is not the focus here.\n\n**Domain 5: Governance, Risk, and Compliance**"
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
    "description": "Protecting software from reverse engineering is crucial for maintaining security:\n\n- Digitally signing the software verifies the source and integrity but does not prevent reverse engineering.\n- Code obfuscation intentionally complicates the code structure, making it harder for attackers to reverse engineer the software, which is the best recommendation here.\n- Limiting the use of third-party libraries reduces dependency risks but does not protect against reverse engineering.\n- Using compile flags can optimize the build process but is not directly related to preventing reverse engineering.\n\n**Domain 3: Implementation**"
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
    "description": "Multi-Factor Authentication (MFA) relies on multiple forms of verification:\n\n- 'Something you exhibit' is not typically a factor in MFA.\n- 'Something you have,' such as a physical token or smart card, is a common factor in MFA, making it the correct choice.\n- 'Somewhere you are' (location-based factors) can also be used in MFA but is not the correct choice here.\n- 'Someone you know' is not a factor used in MFA.\n\n**Domain 3: Implementation**"
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
    "description": "Strengthening password policies is crucial to prevent compromises:\n\n- Increasing the minimum password length to 14 characters enhances security by making passwords harder to guess.\n- Upgrading the hashing algorithm from MD5 to SHA-512 improves security but is not directly related to password complexity.\n- Increasing the maximum password age to 120 days might make passwords more prone to guessing over time, not recommended.\n- Reducing the minimum password length to ten characters weakens security, not advisable.\n- Reducing the minimum password age to zero days could lead to frequent password changes, weakening overall security.\n- Including a requirement for at least one special character makes passwords more complex, reducing the risk of compromise.\n\n**Domain 3: Implementation**"
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
    "description": "Understanding the risks associated with downloading software from untrusted sources is critical:\n\n- A hidden keylogger records keystrokes but would not typically cause unusual network traffic.\n- Ransomware encrypts files and demands a ransom but does not usually involve external network connections.\n- A fileless virus resides in memory and does not install itself on the system, making it harder to detect but unrelated to this scenario.\n- A backdoor allows unauthorized access to the system, often through unusual network connections, which fits the scenario.\n\n**Domain 1: Attacks, Threats, and Vulnerabilities**"
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
    "description": "Meeting the specified infrastructure requirements is essential for reliable operation:\n\n- Connecting dual PDUs to redundant power supplies addresses power redundancy but does not cover memory utilization or storage scalability.\n- Transitioning to an Infrastructure as a Service (IaaS) provider offers scalability, baseline resource management, and resilience to failures, making it the best option.\n- Configuring network load balancing improves network reliability but does not address memory utilization or storage scalability.\n- Deploying multiple NAS devices improves storage but does not meet the other requirements.\n\n**Domain 2: Architecture and Design**"
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
    "description": "A DNS sinkhole is a tool used in network security to redirect malicious traffic:\n\n- The first option suggests attackers might use a DNS sinkhole to identify domain structures, which is not a correct use case.\n- The second option implies using a DNS sinkhole for malicious purposes, which contradicts its intended defensive use.\n- The correct option is that a DNS sinkhole captures traffic to known-malicious domains, redirecting it to a safe location, thus neutralizing the threat.\n- The fourth option suggests using a DNS sinkhole as a decoy, but its primary function is to capture and neutralize malicious traffic, not attract attackers.\n\n**Domain 4: Operations and Incident Response**"
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
    "description": "Different types of data can be extracted from image files, depending on what the analyst is looking for:\n\n- Log data refers to recorded activities or events, unrelated to image files.\n- Metadata, which is the correct answer, includes information such as geolocation coordinates, timestamps, and device information, embedded within the image file.\n- Encrypted data would involve secure information that has been encoded, which is not typically associated with the standard image file content.\n- Sensitive data could refer to any private or confidential information, but the scenario specifically involves geolocation coordinates, making metadata the correct term.\n\n**Domain 1: Attacks, Threats, and Vulnerabilities**"
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
    "description": "Understanding the benefits of S/MIME digital signatures is essential for email security:\n\n- Meeting compliance standards can be a reason, but it doesn't specifically address the need for digital signatures.\n- Increasing delivery rates is unrelated to the use of S/MIME.\n- Blocking phishing attacks might be a benefit, but it's not the primary purpose of S/MIME digital signatures.\n- The correct answer is ensuring non-repudiation, as S/MIME digital signatures allow the recipient to verify the sender's identity and confirm that the email content has not been altered.\n\n**Domain 2: Architecture and Design**"
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
    "description": "Understanding how different attack methods relate to specific scenarios is key in cybersecurity:\n\n- Whaling targets high-profile individuals with personalized phishing attacks, unrelated to printing centers.\n- Credential harvesting involves stealing login credentials, which is not specific to the context of printing centers.\n- Prepending adds information to the beginning of data, often used in phishing but not related to printing centers.\n- The correct answer is dumpster diving, where attackers search through discarded materials, such as printed documents, to find sensitive information.\n\n**Domain 1: Attacks, Threats, and Vulnerabilities**"
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
    "description": "Choosing the right cryptographic methods for IoT devices involves understanding their limitations:\n\n- Resource constraints, which is the correct answer, refer to the limited processing power and memory of IoT devices, making it a critical consideration when implementing cryptography.\n- Available bandwidth is important for data transmission but less relevant to cryptography.\n- The use of block ciphers is a consideration in cryptographic design but not the most important factor in this context.\n- The compatibility of the TLS version is necessary for secure communications but is secondary to the device's resource constraints.\n\n**Domain 2: Architecture and Design**"
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
    "description": "Restricting internet access to authorized users can be done in several ways:\n\n- WPA3 is a Wi-Fi security protocol but does not provide a way to prompt for a receipt number.\n- A captive portal, which is the correct answer, directs users to a web page where they must enter a receipt number or other credentials before accessing the internet.\n- PSK (Pre-Shared Key) is used for securing Wi-Fi networks but does not meet the requirement of prompting for a receipt number.\n- IEEE 802.1X provides network access control but is more complex and not specifically designed for the scenario described.\n\n**Domain 3: Implementation**"
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
    "description": "Digital forensics requires careful consideration of the order of data collection:\n\n- The hard drive contains persistent data, which is less volatile than other storage types.\n- RAM, which is the correct answer, is the most volatile form of storage, meaning it loses data when the power is turned off, so it should be collected first.\n- SSDs (Solid State Drives) store data persistently, similar to hard drives, and are less volatile than RAM.\n- Temporary files are less volatile than RAM but still more volatile than persistent storage; however, they are not the first priority in data collection.\n\n**Domain 4: Operations and Incident Response**"
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
    "description": "Proving the effectiveness of security controls is important for compliance:\n\n- NIST CSF provides a framework for improving cybersecurity but does not directly prove control effectiveness.\n- A SOC 2 Type 2 report, which is the correct answer, demonstrates that security controls have been effectively in place over a period of time, providing the required proof.\n- CIS Top 20 compliance reports highlight critical security controls but do not provide proof of control effectiveness over time.\n- A vulnerability report shows potential weaknesses but does not demonstrate the effectiveness of controls over a specific period.\n\n**Domain 5: Governance, Risk, and Compliance**"
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
    "description": "Recovering from a disaster requires a well-defined plan:\n\n- A Business Continuity Plan (BCP) focuses on keeping critical functions running during and after a disaster but is broader than what's needed immediately after the event.\n- A Communication plan is essential for coordinating response efforts but does not directly address restoring services.\n- A Disaster Recovery Plan (DRP), which is the correct answer, outlines the specific steps to restore essential services and operations after a disaster, making it the immediate priority.\n- An Incident Response Plan (IRP) deals with handling specific security incidents and is not focused on disaster recovery.\n\n**Domain 4: Operations and Incident Response**"
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
    "description": "The symptoms of a system outage can often be traced back to different types of attacks:\n\n- Denial of Service (DoS) attacks, which is the correct answer, are characterized by overwhelming the target system with traffic, making it unresponsive. The high amount of received traffic on the downed systems suggests a DoS attack.\n- ARP poisoning alters the network traffic flow by linking the attacker’s MAC address with a legitimate IP address, which would not cause the traffic pattern seen here.\n- Jamming is a technique that interferes with wireless networks, not applicable to this scenario.\n- Kerberoasting targets service accounts in Active Directory, unrelated to the current issue.\n\n**Domain 1: Attacks, Threats, and Vulnerabilities**"
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
    "description": "Responding to a phishing campaign or a similar attack involves various methods:\n\n- Creating a blocklist for subject lines is not effective due to the variety of subject lines used.\n- Sending the dead domain to a DNS sinkhole could neutralize the threat, but only after the link has been clicked.\n- Quarantining all emails and notifying employees helps prevent further spread but does not address the root cause.\n- Blocking the URL shortener domain in the web proxy, which is the correct answer, stops users from accessing the malicious links, effectively neutralizing the threat.\n\n**Domain 4: Operations and Incident Response**"
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
    "description": "Securing data on corporate laptops involves protecting it from unauthorized access:\n\n- Disk encryption, which is the correct answer, ensures that data on the laptop cannot be accessed without the proper decryption key, even if the device is stolen.\n- Data loss prevention focuses on preventing data leaks but doesn’t directly protect against physical theft.\n- Operating system hardening improves overall security but doesn't specifically address data protection in the event of theft.\n- Boot security ensures the system starts securely but doesn’t protect the data at rest on the device.\n\n**Domain 2: Architecture and Design**"
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
    "description": "Managing data records within a company requires the implementation of the appropriate policy:\n\n- A Security policy defines the overall security framework but doesn’t specifically address data retention.\n- A Classification policy dictates how data is categorized but does not focus on retention.\n- A Retention policy, which is the correct answer, outlines how long records must be kept and ensures their proper destruction when no longer needed, balancing record-keeping with compliance.\n- An Access control policy governs who can access data but does not address retention or destruction.\n\n**Domain 5: Governance, Risk, and Compliance**"
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
    "description": "Credential leakage in cloud environments can occur through various channels:\n\n- Code repositories, which is the correct answer, can unintentionally expose credentials if they are not properly secured, especially when publicly accessible.\n- The Dark web is where leaked credentials might end up, but it’s not a source of unintentional leakage.\n- Threat feeds provide information on potential threats but are not a source of credential leakage.\n- State actors may exploit leaked credentials but are not a source of leakage.\n- Vulnerability databases track security flaws, not credential leaks.\n\n**Domain 1: Attacks, Threats, and Vulnerabilities**"
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
    "description": "A data classification policy provides several key benefits to an organization:\n\n- Requiring end users to consider data classification improves awareness but is not the primary benefit.\n- Creating access levels for each classification level is important but not the main reason for enforcing a classification policy.\n- The correct answer is that the organization will have the ability to create tailored security requirements based on the sensitivity of the data, ensuring that the most sensitive information is adequately protected.\n- Allowing security analysts to see classification levels helps in processing data securely but is a secondary benefit.\n\n**Domain 5: Governance, Risk, and Compliance**"
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
    "description": "Understanding different types of vulnerability assessments is critical in cybersecurity:\n\n- A non-credentialed scan, which is the correct answer, is performed without system credentials and simulates an external attacker's view of the system.\n- Packet capture collects network traffic data but is not a method for scanning web servers.\n- Privilege escalation is an attack technique, not a vulnerability scanning method.\n- System enumeration involves identifying resources and services but does not describe a vulnerability scan.\n- A passive scan detects vulnerabilities without actively probing the system, but it is different from a non-credentialed scan.\n\n**Domain 4: Operations and Incident Response**"
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
    "description": "Using real-world knowledge bases to understand adversary behavior helps in applying effective security measures:\n\n- The MITRE ATT&CK framework, which is the correct answer, provides detailed information on adversary tactics, techniques, and procedures, making it a valuable resource for system hardening.\n- CSIRT (Computer Security Incident Response Team) manages incidents but does not focus on adversary behavior.\n- CVSS (Common Vulnerability Scoring System) assesses the severity of vulnerabilities but does not detail adversary behavior.\n- SOAR (Security Orchestration, Automation, and Response) automates responses to security threats but is not a knowledge base.\n\n**Domain 1: Attacks, Threats, and Vulnerabilities**"
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
    "description": "Modernizing data transfer methods requires understanding of different technologies:\n\n- A website-hosted solution might allow for JSON requests but is not optimized for speed or external use.\n- Cloud shared storage is useful for data access but not necessarily for speeding up JSON transfers.\n- A secure email solution ensures data security but is not designed for fast JSON data transfer.\n- Microservices using APIs, which is the correct answer, handle JSON requests efficiently and are designed for fast external data transfers.\n\n**Domain 2: Architecture and Design**"
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
    "description": "Understanding different regulations and their focus areas is crucial for compliance:\n\n- GDPR (General Data Protection Regulation), which is the correct answer, addresses individual rights concerning personal data, including the right to be informed, access, and erasure (right to be forgotten).\n- PCI DSS (Payment Card Industry Data Security Standard) focuses on securing credit card transactions, not individual rights.\n- NIST (National Institute of Standards and Technology) provides guidelines for security but does not directly address individual rights.\n- ISO (International Organization for Standardization) develops standards for various industries, not focused specifically on individual rights.\n\n**Domain 5: Governance, Risk, and Compliance**"
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
    "description": "Resolving certificate errors in secure connections requires proper certificate management:\n\n- Allowing SAN (Subject Alternative Name) certificates might be necessary but is not the solution here.\n- Installing the server certificate into the local truststore, which is the correct answer, establishes trust between the LDAP browser and the server, resolving the certificate errors.\n- Requesting the secure LDAP port to be opened is unrelated to certificate errors.\n- Increasing the TLS (Transport Layer Security) version might enhance security but does not address the immediate certificate issue.\n\n**Domain 3: Implementation**"
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
    "description": "Lack of vendor support is critical as it means no security updates or patches, leaving the system vulnerable to exploitation.\n\n- Instability: Concern but not directly a security issue.\n- Loss of availability: Operational issue, not a security concern.\n- Use of insecure protocols: Can be mitigated, unlike lack of support.\n\n**Domain 2: Architecture and Design**"
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
    "description": "Packet capture tools can easily intercept Telnet credentials as Telnet transmits data in plaintext.\n\n- Spraying attack: Unlikely due to Telnet's cleartext vulnerability.\n- Packet capture tool: Correct, it intercepts plaintext credentials.\n- Remote-access Trojan: Possible, but not tied to Telnet use.\n- Dictionary attack: Relates to password guessing, not Telnet vulnerability.\n\n**Domain 3: Implementation**"
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
    "description": "SSH is a secure protocol that provides encrypted communication for managing remote servers, unlike Telnet.\n\n- HTTPS: Secure for web traffic, not remote server management.\n- SNMPv3: Used for network management, not server access.\n- RDP: Secure but mainly for Windows GUI-based access.\n- SMTP: Protocol for email transmission, not server management.\n\n**Domain 3: Implementation**"
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
    "description": "Wildcard certificates allow securing unlimited subdomains under a single certificate, making it cost-effective.\n\n- Client certificate: Used for client authentication, not multiple domains.\n- Self-signed: Not trusted publicly, unsuitable for large-scale use.\n- Code signing: Ensures software integrity, not domain security.\n\n**Domain 2: Architecture and Design**"
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
    "description": "Nessus is a vulnerability scanner that can identify open ports, insecure services, and legacy protocols on servers.\n\n- curl: Used for data transfer, not for scanning ports/protocols.\n- Wireshark: Captures and analyzes network traffic, not scanning.\n- netcat: Used for network communication, not comprehensive scanning.\n\n**Domain 4: Operations and Incident Response**"
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
    "description": "Serverless architecture allows for scalable and cost-effective deployment of code, reducing both time and expenses involved.\n\n- Thin clients: Reduce hardware costs, not deployment complexity.\n- Private cloud: Offers scalability but may still be costly and complex.\n- Virtual machines: Useful but require infrastructure management.\n\n**Domain 2: Architecture and Design**"
},
{
    "question": "A security administrator is performing an audit on a stand-alone UNIX server, and the following message is immediately displayed: (Error 13): /etc/shadow: Permission denied. Which of the following best describes the type of tool that is being used?",
    "options": [
        "Pass-the-hash monitor",
        "File integrity monitor",
        "Forensic analysis",
        "Password cracker"
    ],
    "correct_answer": 4,
    "description": "The error suggests a password cracker is being used as it attempts to access the /etc/shadow file, where passwords are stored.\n\n- Pass-the-hash monitor: Monitors hash-based attacks, not directly involved.\n- File integrity monitor: Checks for changes, does not access /etc/shadow.\n- Forensic analysis: Collects evidence, not used for cracking passwords.\n\n**Domain 1: Attacks, Threats, and Vulnerabilities**"
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
    "description": "RTP, SIP, H.323, and SRTP are protocols commonly used in VoIP (Voice over IP) communications.\n\n- RTOS: Real-Time Operating System, unrelated to these protocols.\n- SoC: System on Chip, unrelated to network communication.\n- HVAC: Heating, Ventilation, and Air Conditioning, not relevant here.\n\n**Domain 3: Implementation**"
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
    "description": "Whaling is a form of spear phishing that specifically targets high-profile individuals like CEOs.\n- Spear phishing: Targets specific individuals, but whaling is more specific to executives.\n- Impersonation: Pretending to be someone else, a broader category.\n- Identity fraud: Stealing identity for fraud, broader than phishing.\n\n**Domain 1: Attacks, Threats, and Vulnerabilities**"
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
    "description": "After exploiting the PKI, the following steps should be considered:\n- Updating the CRL (Certificate Revocation List) is important but only invalidates compromised certificates.\n- Patching the CA (Certificate Authority), which is the correct answer, addresses the root vulnerability in the PKI infrastructure.\n- Changing passwords is important but does not address the certificate flaw.\n- Implementing SOAR (Security Orchestration, Automation, and Response) helps automate responses but is not specific to the PKI issue.\n\n**Domain 4: Operations and Incident Response**"
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
    "description": "For multi-factor authentication (MFA) involving smart cards:\n- A PIN (Personal Identification Number), which is the correct answer, is often required along with a smart card to authenticate the user, serving as the second factor.\n- A hardware token could be used as an alternative second factor, but not specifically with smart cards.\n- A User ID is used for identification, not as an authentication factor.\n- SMS is typically used for sending codes, but not in combination with smart cards.\n\n**Domain 3: Implementation**"
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
    "description": "To secure access for an external consultant:\n TACACS+ is a protocol for network access control but does not manage privileged access.\n- SAML (Security Assertion Markup Language) is used for single sign-on but is not specific to privileged access.\n- An SSO platform helps with centralized authentication but does not manage elevated privileges.\n- Role-based access control (RBAC) defines user roles but does not specifically manage external access.\n- PAM (Privileged Access Management) software, which is the correct answer, allows secure, temporary access to critical systems without sharing passwords.\n\n**Domain 3: Implementation**"
},
{
    "question": "A newly implemented wireless network is designed so that visitors can connect to the wireless network for business activities. The legal department is concerned that visitors might connect to the network and perform illicit activities. Which of the following should the security team implement to address this concern?",
    "options": [
        "Configure a RADIUS server to manage device authentication.",
        "Use 802.1X on all devices connecting to wireless.",
        "Add a guest captive portal requiring visitors to accept terms and conditions.",
        "Allow for new devices to be connected via WPS."
    ],
    "correct_answer": 3,
    "description": "To manage visitor access to a wireless network:\n- Configuring a RADIUS server manages device authentication but does not specifically address visitor activities.\n- Using 802.1X provides port-based network access control but is complex for guest access.\n- A guest captive portal, which is the correct answer, requires visitors to accept terms and conditions before accessing the network, setting legal boundaries for use.\n- WPS (Wi-Fi Protected Setup) is not secure and should not be used for guest access.\n\n**Domain 2: Architecture and Design**"
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
    "description": "In data management, roles have distinct responsibilities:\n- The Owner, which is the correct answer, is responsible for identifying risks, defining access controls, and ensuring proper data management.\n- The Custodian manages data storage and backups but does not define access.\n- The Steward oversees data quality and policy compliance but does not define access or identify risks.\n- The Controller handles data protection laws and regulations but does not define internal access controls.\n\n**Domain 5: Governance, Risk, and Compliance**"
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
    "description": "Physical security controls serve different purposes:\n- Lighting, which is one correct answer, deters unauthorized access by increasing visibility and can also detect intruders when combined with sensors.\n\n- Fencing is primarily a deterrent but does not detect intrusions.\n- Signage deters by warning of consequences but does not detect activities.\n- A Sensor, which is the other correct answer, detects unauthorized access and can act as a deterrent when combined with other measures.\n- A Bollard is a physical barrier but does not detect or deter by itself.\n- A Lock prevents access but does not detect intrusions.\n\n**Domain 3: Implementation**"
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
    "description": "To ensure accessibility during peak times:\n- A Load balancer, which is the correct answer, distributes incoming network traffic across multiple servers, ensuring the application remains responsive during high demand.\n- Cloud backups protect data but do not help with real-time accessibility.\n- Geographic dispersal increases redundancy and disaster recovery capabilities but does not directly address load management.\n- Disk multipathing improves storage reliability but does not manage application traffic.\n\n**Domain 2: Architecture and Design**"
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
    "description": "To ensure software integrity:\n- Input validation protects against malicious inputs but does not prevent tampering with the software itself.\n- Code signing, which is the correct answer, digitally signs the software, allowing users to verify its authenticity and that it has not been altered.\n- Secure cookies protect session data in web applications but are unrelated to software integrity.\n- Fuzzing tests software for vulnerabilities but does not protect against tampering.\n\n**Domain 3: Implementation**"
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
    "description": "When continuing to use end-of-life software:\n- The lack of security updates, which is the correct answer, is the most critical risk, as it leaves the application vulnerable to new threats.\n- The lack of new features is a disadvantage but does not pose a security risk.\n- The lack of support means troubleshooting may be difficult, but it is not as critical as security updates.\n- The lack of source code access limits customization but is not the primary security concern.\n\n**Domain 5: Governance, Risk, and Compliance**"
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
    "description": "To validate if credentials are being sent in cleartext:\n- Wireshark, which is the correct answer, captures and analyzes network traffic, making it ideal for verifying whether credentials are exposed in transit.\n- netcat is a networking tool but does not analyze traffic content.\n- Nessus scans for vulnerabilities but does not capture network traffic.\n- Nmap identifies open ports and services but does not inspect traffic content.\n\n**Domain 4: Operations and Incident Response**"
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
    "description": "To protect against attacks using malformed inputs:\n- Fuzzing, which is the correct answer, tests the product by inputting unexpected or malformed data to uncover potential vulnerabilities.\n- Continuous deployment automates the release of new code but does not specifically protect against malformed inputs.\n- Static code analysis examines the code for security issues but may not catch runtime vulnerabilities like malformed input attacks.\n- Manual peer review helps identify coding errors but may not focus on input handling.\n\n**Domain 3: Implementation**"
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
    "description": "When issues are identified in a design:\n- The Risk management process assesses and mitigates risks but does not address design changes directly.\n- The Product design process involves creating the design, not reviewing it.\n- The Design review process identifies issues but does not implement changes.\n- The Change control process, which is the correct answer, manages how changes are introduced to the design to address identified issues.\n\n**Domain 2: Architecture and Design**"
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
    "description": "To determine the severity of a vulnerability:\n- CVE (Common Vulnerabilities and Exposures) lists known vulnerabilities but does not provide a severity score.\n- OSINT (Open Source Intelligence) gathers publicly available information but does not assess vulnerability severity.\n- SOAR (Security Orchestration, Automation, and Response) automates security operations but does not score vulnerabilities.\n- CVSS (Common Vulnerability Scoring System), which is the correct answer, provides a standardized method for assessing the severity of security vulnerabilities.\n\n**Domain 1: Attacks, Threats, and Vulnerabilities**"

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
    "description": "For information on common application exploitation methods:\n- OWASP (Open Web Application Security Project), which is the correct answer, provides detailed resources on application security, including common vulnerabilities.\n- STIX (Structured Threat Information eXpression) is a language for sharing threat intelligence but not specific to application exploits.\n- OVAL (Open Vulnerability and Assessment Language) standardizes security content but does not focus on application exploits.\n- A Threat intelligence feed provides up-to-date information on threats but is not as focused on application vulnerabilities.\n- CVE lists known vulnerabilities but does not provide detailed exploitation methods.\n\n**Domain 1: Attacks, Threats, and Vulnerabilities**"
},
{
    "question": "A security analyst is reviewing the logs on an organization’s DNS server and notices the following unusual snippet: \n\nLog from named: post-processed 20230102 0045L \n... \nqry_source: 124.22.158.37 TCP/53 \nqry_dest: 52.165.16.154 TCP/53 \nqry_dest: 10.100.50.5 TCP/53 \nqry_type: AXFR \n| zone int.comptia.org \n------------------------| www A 10.100.50.21 \n------------------------| dns A 10.100.5.5 \n------------------------| adds A 10.101.10.10 \n------------------------| fshare A 10.101.10.20 \n------------------------| sip A 10.100.5.11 \n... \n\nWhich of the following attack techniques was most likely used?",
    "options": [
        "Determining the organization’s ISP-assigned address space",
        "Bypassing the organization’s DNS sinkholing",
        "Footprinting the internal network",
        "Attempting to achieve initial access to the DNS server",
        "Exfiltrating data from fshare.int.complia.org"
    ],
    "correct_answer": 3,
    "description": "To analyze the DNS server log activity:\n- Determining the ISP-assigned address space identifies the external network range but does not explain the log details.\n- Bypassing DNS sinkholing avoids redirection but is unrelated to the internal network footprint.\n- Footprinting the internal network, which is the correct answer, involves mapping the internal network, fitting the DNS queries observed.\n- Attempting to achieve initial access to the DNS server would involve exploiting vulnerabilities but is not evident here.\n- Exfiltrating data describes stealing information but does not match the DNS queries in the log.\n\n**Domain 1: Attacks, Threats, and Vulnerabilities**"
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
    "description": "To prevent unauthorized logins:\n- Disciplinary actions are important for policy violations but do not prevent external attacks.\n- Conditional access policies, which are correct, restrict access based on conditions like location or device, reducing the risk of unauthorized logins.\n- Regular account audits help monitor activity but do not prevent unauthorized logins.\n- Additional authentication factors, also correct, such as MFA, make it harder for attackers to gain access.\n- Content filtering prevents access to harmful content but does not directly address unauthorized logins.\n- Reviewing user account permissions ensures proper access but is not a direct preventative measure.\n\n**Domain 4: Operations and Incident Response**"
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
    "description": "To protect a web application on port 443:\n- NIDS (Network Intrusion Detection System) monitors network traffic and can detect attacks, making it one correct answer.\n- A Honeypot attracts attackers but does not directly protect the application.\n- A Certificate revocation list invalidates compromised certificates but does not protect against attacks.\n- HIPS (Host Intrusion Prevention System) protects the host but may not cover the entire web application.\n- WAF (Web Application Firewall), which is the other correct answer, specifically protects web applications by filtering and monitoring HTTP traffic.\n- SIEM (Security Information and Event Management) provides centralized logging and alerts but is not a direct protective measure.\n\n**Domain 3: Implementation**"
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
    "description": "For a point-in-time backup of a virtual machine:\n- Replication creates copies of data but not necessarily a snapshot of a specific moment.\n- Simulation tests scenarios and does not create backups.\n- A Snapshot, which is the correct answer, captures the state of a virtual machine at a specific point in time.\n- Containerization isolates applications but does not relate to virtual machine backups.\n\n**Domain 3: Implementation**"
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
    "description": "To handle unused, non-compliant desktops:\n- Monitoring tracks activity but does not address the non-compliance.\n- Decommissioning, which is the correct answer, removes non-compliant systems from the network, reducing security risks.\n- Patching updates systems but does not resolve the issue of unused or non-compliant desktops.\n- Isolating prevents interaction with other systems but does not fully mitigate the risk.\n\n**Domain 4: Operations and Incident Response**"
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
    "description": "For data removal while allowing reuse of hard drives:\n- Sanitization, which is the correct answer, securely wipes data from storage devices, making the data unrecoverable while preserving the drive for reuse.\n- Formatting erases the file system but may not completely remove data.\n- Degaussing uses magnetic fields to erase data but can render the drive unusable.\n- Defragmentation reorganizes data on a drive but does not remove it.\n\n**Domain 3: Implementation**"
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
    "description": "For secure remote authentication:\n- Username and password are common but do not meet the criteria for enhanced security.\n- Biometrics offer strong security but may not be device-agnostic or work offline.\n- SMS verification adds a second factor but relies on network connectivity.\n- Time-based tokens, which are the correct answer, provide a secure, device-agnostic method of authentication that works across platforms and offline.\n\n**Domain 3: Implementation**"
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
    "description": "In a security awareness program:\n- A Password policy defines password requirements but is not directly related to awareness training.\n- Access badges control physical entry but are not part of a security awareness program.\n- A Phishing campaign, which is the correct answer, educates employees on recognizing and avoiding phishing attacks, fitting the program’s goals.\n- A Risk assessment evaluates potential risks but is not an awareness activity.\n\n**Domain 5: Governance, Risk, and Compliance**"
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
    "description": "To understand the vulnerability caused by a malicious update:\n- A DDoS (Distributed Denial of Service) attack overwhelms a service with traffic but is not caused by a software update.\n- A Rogue employee might introduce threats but does not explain the widespread impact of the update.\n- An Insider threat involves someone within the organization causing harm but does not fit this scenario.\n- A Supply chain attack, which is the correct answer, compromises a trusted third-party service or software, leading to widespread issues.\n\n**Domain 1: Attacks, Threats, and Vulnerabilities**"
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
    "description": "To identify the cause of suspicious server activity:\n- A web shell, which is the correct answer, is a script uploaded to a web server that allows remote command execution, fitting the scenario.\n- A worm spreads across networks but does not explain the specific suspicious process.\n- Malicious insiders may mine cryptocurrency, but this scenario involves external traffic and unauthorized processes.\n- A rootkit Trojan compromises systems at a deeper level but does not match the web shell description.\n\n**Domain 1: Attacks, Threats, and Vulnerabilities**"
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
    "description": "For a comprehensive supply chain analysis:\n- A Vulnerability scanner identifies potential weaknesses but does not provide a full-spectrum analysis.\n- A Penetration test simulates attacks but focuses on security, not the entire supply chain.\n- SCAP (Security Content Automation Protocol) standardizes vulnerability management but is not a full-spectrum tool.\n- An Illumination tool, which is the correct answer, maps and analyzes the supply chain, identifying potential risks and vulnerabilities.\n\n**Domain 4: Operations and Incident Response**"
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
    "description": "An Agentless solution, which is the correct answer, monitors systems and networks without requiring software agents on the endpoints being monitored.\n\n- A Client-based solution requires installation of monitoring software on each endpoint.\n- An Open port refers to a network port that allows communication but does not describe a monitoring solution.\n- A File-based solution involves managing or storing files and is not related to system monitoring.\n\n**Domain 4: Operations and Incident Response**"
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
    "description": "Static analysis involves examining the application's source code without executing it to identify vulnerabilities, coding errors, and misconfigurations early in the development process.\n\n- Dynamic analysis involves evaluating the application while it's running, focusing on its behavior during execution rather than its source code.\n- Static analysis involves reviewing the source code itself without executing the application to uncover potential misconfigurations and vulnerabilities.\n- Gap analysis identifies discrepancies between current processes and desired outcomes, but it doesn't involve examining \n\n**Domain 3: Implementation.**"
}

]
