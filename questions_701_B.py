questions_701_B = [

# Page 3 of 7 {
{
    "question": "After reviewing the following vulnerability scanning report:\n\nServer: 192.168.14.6\nService: Telnet\nPort: 23 Protocol: TCP\nStatus: Open Severity: High\nVulnerability: Use of an insecure network protocol\n\nA security analyst performs the following test:\n\nnmap -p 23 192.168.14.6 --script telnet-encryption\n\nPORT       STATE  SERVICE  REASON\n23/tcp     open   telnet   syn-ack\n|  telnet encryption:\n|_ Telnet server supports encryption\n\nWhich of the following would the security analyst conclude for this reported vulnerability?",
    "options": [
        "It is a false positive.",
        "A rescan is required.",
        "It is considered noise.",
        "Compensating controls exist."
    ],
    "correct_answer": 1,
    "description": "The Telnet server supports encryption, indicating that compensating controls exist, mitigating the risk of using an insecure network protocol."
},

    {
        "question": "An organization disabled unneeded services and placed a firewall in front of a business-critical legacy system. Which of the following best describes the actions taken by the organization?",
        "options": [
            "Exception",
            "Segmentation",
            "Risk transfer",
            "Compensating controls"
        ],
        "correct_answer": 2,
        "description": "Segmentation involves dividing the network into segments to isolate and protect critical systems, which helps to limit the attack surface and mitigate risks."
    },
    {
        "question": "A security consultant needs secure, remote access to a client environment. Which of the following should the security consultant most likely use to gain access?",
        "options": [
            "EAP",
            "DHCP",
            "IPSec",
            "NAT"
        ],
        "correct_answer": 3,
        "description": "IPSec is a secure protocol used to establish encrypted remote access tunnels, providing a secure method for accessing client environments."
    },
    {
        "question": "Which of the following should a systems administrator use to ensure an easy deployment of resources within the cloud provider?",
        "options": [
            "Software as a service",
            "Infrastructure as code",
            "Internet of Things",
            "Software-defined networking"
        ],
        "correct_answer": 2,
        "description": "Infrastructure as code (IaC) allows for the automation and management of cloud resources, ensuring easy deployment and scalability."
    },
    {
        "question": "After a security awareness training session, a user called the IT help desk and reported a suspicious call. The suspicious caller stated that the Chief Financial Officer wanted credit card information in order to close an invoice. Which of the following topics did the user recognize from the training?",
        "options": [
            "Insider threat",
            "Email phishing",
            "Social engineering",
            "Executive whaling"
        ],
        "correct_answer": 3,
        "description": "Social engineering involves manipulating individuals to disclose confidential information, as seen in this scenario with the suspicious caller."
    },
    {
        "question": "A security administrator is deploying a DLP solution to prevent the exfiltration of sensitive customer data. Which of the following should the administrator do first?",
        "options": [
            "Block access to cloud storage websites.",
            "Create a rule to block outgoing email attachments.",
            "Apply classifications to the data.",
            "Remove all user permissions from shares on the file server."
        ],
        "correct_answer": 3,
        "description": "Applying data classifications helps the DLP solution to accurately identify and protect sensitive customer data from exfiltration."
    },
    {
        "question": "An administrator assists the legal and compliance team with ensuring information about customer transactions is archived for the proper time period. Which of the following data policies is the administrator carrying out?",
        "options": [
            "Compromise",
            "Retention",
            "Analysis",
            "Transfer",
            "Inventory"
        ],
        "correct_answer": 2,
        "description": "Retention policies dictate how long data must be kept before it can be archived or deleted, ensuring compliance with legal and regulatory requirements."
    },
    {
        "question": "A company is working with a vendor to perform a penetration test. Which of the following includes an estimate about the number of hours required to complete the engagement?",
        "options": [
            "SOW",
            "BPA",
            "SLA",
            "NDA"
        ],
        "correct_answer": 1,
        "description": "A Statement of Work (SOW) outlines the scope, timelines, and estimated hours for completing a penetration testing engagement."
    },
    {
        "question": "A Chief Information Security Officer (CISO) wants to explicitly raise awareness about the increase of ransomware-as-a-service in a report to the management team. Which of the following best describes the threat actor in the CISO’s report?",
        "options": [
            "Insider threat",
            "Hacktivist",
            "Nation-state",
            "Organized crime"
        ],
        "correct_answer": 4,
        "description": "Ransomware-as-a-service is typically operated by organized crime groups, making it a significant threat that the CISO wants to address."
    },
    {
        "question": "Which of the following practices would be best to prevent an insider from introducing malicious code into a company's development process?",
        "options": [
            "Code scanning for vulnerabilities",
            "Open-source component usage",
            "Quality assurance testing",
            "Peer review and approval"
        ],
        "correct_answer": 4,
        "description": "Peer review and approval processes help detect and prevent the introduction of malicious code into the development pipeline."
    },
    {
        "question": "Which of the following can best protect against an employee inadvertently installing malware on a company system?",
        "options": [
            "Host-based firewall",
            "System isolation",
            "Least privilege",
            "Application allow list"
        ],
        "correct_answer": 4,
        "description": "An application allow list restricts software installations to approved programs only, preventing employees from inadvertently installing malware."
    },
    {
        "question": "A company is adding a clause to its AUP that states employees are not allowed to modify the operating system on mobile devices. Which of the following vulnerabilities is the organization addressing?",
        "options": [
            "Cross-site scripting",
            "Buffer overflow",
            "Jailbreaking",
            "Side loading"
        ],
        "correct_answer": 3,
        "description": "Jailbreaking removes security controls from mobile devices, making them more vulnerable to attacks and unauthorized modifications."
    },
    {
        "question": "Which of the following would be the best ways to ensure only authorized personnel can access a secure facility? (Choose two.)",
        "options": [
            "Fencing",
            "Video surveillance",
            "Badge access",
            "Access control vestibule",
            "Sign-in sheet",
            "Sensor"
        ],
        "correct_answer": [3, 4],
        "description": "Badge access and access control vestibules are effective methods for ensuring only authorized personnel can access secure facilities."
    },
    {
        "question": "An organization would like to store customer data on a separate part of the network that is not accessible to users on the main corporate network. Which of the following should the administrator use to accomplish this goal?",
        "options": [
            "Segmentation",
            "Isolation",
            "Patching",
            "Encryption"
        ],
        "correct_answer": 1,
        "description": "Network segmentation helps to isolate sensitive data from other parts of the network, enhancing security and protecting customer data."
    },
    {
        "question": "Which of the following is the most common data loss path for an air-gapped network?",
        "options": [
            "Bastion host",
            "Unsecured Bluetooth",
            "Unpatched OS",
            "Removable devices"
        ],
        "correct_answer": 4,
        "description": "Removable devices, such as USB drives, are a common data loss path in air-gapped networks, as they can be physically removed and connected to other systems."
    },
    {
        "question": "Malware spread across a company's network after an employee visited a compromised industry blog. Which of the following best describes this type of attack?",
        "options": [
            "Impersonation",
            "Disinformation",
            "Watering-hole",
            "Smishing"
        ],
        "correct_answer": 3,
        "description": "A watering-hole attack targets specific groups by compromising websites they are likely to visit, as seen in this scenario."
    },
    {
        "question": "An organization is struggling with scaling issues on its VPN concentrator and internet circuit due to remote work. The organization is looking for a software solution that will allow it to reduce traffic on the VPN and internet circuit, while still providing encrypted tunnel access to the data center and monitoring of remote employee internet traffic. Which of the following will help achieve these objectives?",
        "options": [
            "Deploying a SASE solution to remote employees",
            "Building a load-balanced VPN solution with redundant internet",
            "Purchasing a low-cost SD-WAN solution for VPN traffic",
            "Using a cloud provider to create additional VPN concentrators"
        ],
        "correct_answer": 1,
        "description": "A Secure Access Service Edge (SASE) solution reduces VPN traffic by offloading some services to the cloud, while still providing secure, encrypted access."
    },
    {
        "question": "Which of the following is the best reason to complete an audit in a banking environment?",
        "options": [
            "Regulatory requirement",
            "Organizational change",
            "Self-assessment requirement",
            "Service-level requirement"
        ],
        "correct_answer": 1,
        "description": "Regulatory requirements often mandate regular audits in banking environments to ensure compliance with financial regulations and standards."
    },
    {
        "question": "Which of the following security concepts is the best reason for permissions on a human resources fileshare to follow the principle of least privilege?",
        "options": [
            "Integrity",
            "Availability",
            "Confidentiality",
            "Non-repudiation"
        ],
        "correct_answer": 3,
        "description": "Confidentiality is a key reason for following the principle of least privilege, ensuring that only authorized individuals have access to sensitive HR data."
    },
    {
        "question": "Which of the following are cases in which an engineer should recommend the decommissioning of a network device? (Choose two.)",
        "options": [
            "The device has been moved from a production environment to a test environment.",
            "The device is configured to use cleartext passwords.",
            "The device is moved to an isolated segment on the enterprise network.",
            "The device is moved to a different location in the enterprise.",
            "The device's encryption level cannot meet organizational standards.",
            "The device is unable to receive authorized updates."
        ],
        "correct_answer": [5, 6],
        "description": "A network device should be decommissioned if it cannot meet organizational encryption standards or if it can no longer receive updates, increasing security risks."
    },
    {
        "question": "A company is required to perform a risk assessment on an annual basis. Which of the following types of risk assessments does this requirement describe?",
        "options": [
            "Continuous",
            "Ad hoc",
            "Recurring",
            "One time"
        ],
        "correct_answer": 3,
        "description": "A recurring risk assessment is conducted on a regular basis, such as annually, to evaluate and manage risks within an organization."
    },
    {
        "question": "After a recent ransomware attack on a company's system, an administrator reviewed the log files. Which of the following control types did the administrator use?",
        "options": [
            "Compensating",
            "Detective",
            "Preventive",
            "Corrective"
        ],
        "correct_answer": 2,
        "description": "Detective controls are used to identify and report security incidents, such as reviewing log files after a ransomware attack."
    },
    {
        "question": "Which of the following exercises should an organization use to improve its incident response process?",
        "options": [
            "Tabletop",
            "Replication",
            "Failover",
            "Recovery"
        ],
        "correct_answer": 1,
        "description": "A tabletop exercise is a discussion-based exercise used to improve an organization's incident response process by simulating a security event."
    },
    {
        "question": "Which of the following best ensures minimal downtime and data loss for organizations with critical computing equipment located in earthquake-prone areas?",
        "options": [
            "Generators and UPS",
            "Off-site replication",
            "Redundant cold sites",
            "High availability networking"
        ],
        "correct_answer": 2,
        "description": "Off-site replication ensures that data is continuously backed up to a remote location, minimizing data loss in the event of an earthquake or other disaster."
    },
    {
        "question": "A newly identified network access vulnerability has been found in the OS of legacy IoT devices. Which of the following would best mitigate this vulnerability quickly?",
        "options": [
            "Insurance",
            "Patching",
            "Segmentation",
            "Replacement"
        ],
        "correct_answer": 3,
        "description": "Segmentation can quickly mitigate network access vulnerabilities by isolating the affected devices from the rest of the network."
    },
    {
        "question": "After an audit, an administrator discovers all users have access to confidential data on a file server. Which of the following should the administrator use to restrict access to the data quickly?",
        "options": [
            "Group Policy",
            "Content filtering",
            "Data loss prevention",
            "Access control lists"
        ],
        "correct_answer": 4,
        "description": "Access control lists (ACLs) are used to quickly and effectively restrict access to data by specifying which users or groups are allowed to access certain resources."
    },
    {
        "question": "A client demands at least 99.99% uptime from a service provider's hosted security services. Which of the following documents includes the information the service provider should return to the client?",
        "options": [
            "MOA",
            "SOW",
            "MOU",
            "SLA"
        ],
        "correct_answer": 4,
        "description": "A Service Level Agreement (SLA) outlines the required uptime, performance metrics, and responsibilities between the service provider and the client."
    },
    {
        "question": "A company is discarding a classified storage array and hires an outside vendor to complete the disposal. Which of the following should the company request from the vendor?",
        "options": [
            "Certification",
            "Inventory list",
            "Classification",
            "Proof of ownership"
        ],
        "correct_answer": 1,
        "description": "The company should request a certification of destruction from the vendor to ensure that the classified data has been securely disposed of."
    },
    {
        "question": "A company is planning a disaster recovery site and needs to ensure that a single natural disaster would not result in the complete loss of regulated backup data. Which of the following should the company consider?",
        "options": [
            "Geographic dispersion",
            "Platform diversity",
            "Hot site",
            "Load balancing"
        ],
        "correct_answer": 1,
        "description": "Geographic dispersion involves placing backup data in physically separate locations to prevent a single disaster from causing total data loss."
    },
    {
        "question": "A security analyst locates a potentially malicious video file on a server and needs to identify both the creation date and the file's creator. Which of the following actions would most likely give the security analyst the information required?",
        "options": [
            "Obtain the file's SHA-256 hash.",
            "Use hexdump on the file's contents.",
            "Check endpoint logs.",
            "Query the file's metadata."
        ],
        "correct_answer": 4,
        "description": "Querying the file's metadata can provide information about the file's creation date, creator, and other properties useful in a forensic investigation."
    },
    {
        "question": "Which of the following teams combines both offensive and defensive testing techniques to protect an organization's critical systems?",
        "options": [
            "Red",
            "Blue",
            "Purple",
            "Yellow"
        ],
        "correct_answer": 3,
        "description": "A Purple Team integrates the skills and techniques of both Red (offensive) and Blue (defensive) Teams to enhance an organization's security posture."
    },
    {
        "question": "A small business uses kiosks on the sales floor to display product information for customers. A security team discovers the kiosks use end-of-life operating systems. Which of the following is the security team most likely to document as a security implication of the current architecture?",
        "options": [
            "Patch availability",
            "Product software compatibility",
            "Ease of recovery",
            "Cost of replacement"
        ],
        "correct_answer": 1,
        "description": "End-of-life operating systems often lack available patches and security updates, increasing the risk of vulnerabilities in the system."
    },
    {
        "question": "Which of the following would help ensure a security analyst is able to accurately measure the overall risk to an organization when a new vulnerability is disclosed?",
        "options": [
            "A full inventory of all hardware and software",
            "Documentation of system classifications",
            "A list of system owners and their departments",
            "Third-party risk assessment documentation"
        ],
        "correct_answer": 1,
        "description": "A full inventory of hardware and software helps a security analyst assess the impact of new vulnerabilities on all affected systems."
    },
    {
        "question": "Which of the following best practices gives administrators a set period to perform changes to an operational system to ensure availability and minimize business impacts?",
        "options": [
            "Impact analysis",
            "Scheduled downtime",
            "Backout plan",
            "Change management boards"
        ],
        "correct_answer": 2,
        "description": "Scheduled downtime allows administrators to perform necessary changes or maintenance on systems during a predefined period to minimize disruptions."
    },
    {
        "question": "A company must ensure sensitive data at rest is rendered unreadable. Which of the following will the company most likely use?",
        "options": [
            "Hashing",
            "Tokenization",
            "Encryption",
            "Segmentation"
        ],
        "correct_answer": 3,
        "description": "Encryption is commonly used to render sensitive data unreadable when it is stored (data at rest) by converting it into an encrypted format."
    },
    {
        "question": "A legacy device is being decommissioned and is no longer receiving updates or patches. Which of the following describes this scenario?",
        "options": [
            "End of business",
            "End of testing",
            "End of support",
            "End of life"
        ],
        "correct_answer": 3,
        "description": "End of life refers to the point at which a product is no longer supported or updated by the manufacturer, requiring decommissioning."
    },
    {
        "question": "A bank insists all of its vendors must prevent data loss on stolen laptops. Which of the following strategies is the bank requiring?",
        "options": [
            "Encryption at rest",
            "Masking",
            "Data classification",
            "Permission restrictions"
        ],
        "correct_answer": 1,
        "description": "Encryption at rest ensures that data on a laptop is encrypted and remains protected even if the laptop is stolen."
    },
    {
        "question": "A company's end users are reporting that they are unable to reach external websites. After reviewing the performance data for the DNS severs, the analyst discovers that the CPU, disk, and memory usage are minimal, but the network interface is flooded with inbound traffic. Network logs show only a small number of DNS queries sent to this server. Which of the following best describes what the security analyst is seeing?",
        "options": [
            "Concurrent session usage",
            "Secure DNS cryptographic downgrade",
            "On-path resource consumption",
            "Reflected denial of service"
        ],
        "correct_answer": 4,
        "description": "A reflected denial of service attack sends a high volume of traffic to a victim's server by exploiting open services, overwhelming the network interface."
    },
    {
        "question": "A systems administrator wants to prevent users from being able to access data based on their responsibilities. The administrator also wants to apply the required access structure via a simplified format. Which of the following should the administrator apply to the site recovery resource group?",
        "options": [
            "RBAC",
            "ACL",
            "SAML",
            "GPO"
        ],
        "correct_answer": 1,
        "description": "Role-Based Access Control (RBAC) allows for the assignment of access permissions based on the user's role, simplifying access management."
    },
    {
        "question": "During the onboarding process, an employee needs to create a password for an intranet account. The password must include ten characters, numbers, and letters, and two special characters. Once the password is created, the company will grant the employee access to other company-owned websites based on the intranet profile. Which of the following access management concepts is the company most likely using to safeguard intranet accounts and grant access to multiple sites based on a user's intranet account? (Choose two.)",
        "options": [
            "Federation",
            "Identity proofing",
            "Password complexity",
            "Default password changes",
            "Password manager",
            "Open authentication"
        ],
        "correct_answer": [1, 3],
        "description": "Federation and password complexity are key components of access management, ensuring secure and consistent access across multiple systems."
    },
    {
        "question": "Which of the following describes a security alerting and monitoring tool that collects system, application, and network logs from multiple sources in a centralized system?",
        "options": [
            "SIEM",
            "DLP",
            "IDS",
            "SNMP"
        ],
        "correct_answer": 1,
        "description": "A Security Information and Event Management (SIEM) system collects and correlates logs from multiple sources to provide centralized monitoring and alerting."
    },
    {
        "question": "A network manager wants to protect the company's VPN by implementing multifactor authentication that uses:\n\nSomething you know -\nSomething you have -\nSomething you are -\n\nWhich of the following would accomplish the manager's goal?",
        "options": [
            "Domain name, PKI, GeoIP lookup",
            "VPN IP address, company ID, facial structure",
            "Password, authentication token, thumbprint",
            "Company URL, TLS certificate, home address"
        ],
        "correct_answer": 3,
        "description": "A password (something you know), an authentication token (something you have), and a thumbprint (something you are) form the basis of multifactor authentication."
    },
    {
        "question": "Which of the following would be the best way to handle a critical business application that is running on a legacy server?",
        "options": [
            "Segmentation",
            "Isolation",
            "Hardening",
            "Decommissioning"
        ],
        "correct_answer": 1,
        "description": "Hardening involves applying security measures to protect a legacy server and the critical applications it hosts, reducing vulnerabilities."
    },
    {
        "question": "Which of the following vulnerabilities is exploited when an attacker overwrites a register with a malicious address?",
        "options": [
            "VM escape",
            "SQL injection",
            "Buffer overflow",
            "Race condition"
        ],
        "correct_answer": 3,
        "description": "Buffer overflow attacks occur when an attacker overwrites a memory register with malicious code, causing unintended behavior in the system."
    },
    {
        "question": "After a company was compromised, customers initiated a lawsuit. The company's attorneys have requested that the security team initiate a legal hold in response to the lawsuit. Which of the following describes the action the security team will most likely be required to take?",
        "options": [
            "Retain the emails between the security team and affected customers for 30 days.",
            "Retain any communications related to the security breach until further notice.",
            "Retain any communications between security members during the breach response.",
            "Retain all emails from the company to affected customers for an indefinite period of time."
        ],
        "correct_answer": 2,
        "description": "A legal hold requires the retention of any communications, documents, or evidence related to a legal case, such as a security breach, until further notice."
    },
    {
        "question": "Which of the following describes the process of concealing code or text inside a graphical image?",
        "options": [
            "Symmetric encryption",
            "Hashing",
            "Data masking",
            "Steganography"
        ],
        "correct_answer": 4,
        "description": "Steganography involves hiding code or text within an image, making the data less likely to be detected by unauthorized users."
    },
    {
        "question": "An employee receives a text message from an unknown number claiming to be the company’s Chief Executive Officer and asking the employee to purchase several gift cards. Which of the following types of attacks does this describe?",
        "options": [
            "Vishing",
            "Smishing",
            "Pretexting",
            "Phishing"
        ],
        "correct_answer": 2,
        "description": "Smishing is a type of phishing attack conducted via SMS or text message, often used to impersonate high-ranking officials to trick employees into taking action."
    },
    {
        "question": "Which of the following risk management strategies should an enterprise adopt first if a legacy application is critical to business operations and there are preventative controls that are not yet implemented?",
        "options": [
            "Mitigate",
            "Accept",
            "Transfer",
            "Avoid"
        ],
        "correct_answer": 1,
        "description": "Mitigation involves implementing controls to reduce the risk associated with a critical legacy application that cannot yet be fully secured."
    },
    {
        "question": "Visitors to a secured facility are required to check in with a photo ID and enter the facility through an access control vestibule. Which of the following best describes this form of security control?",
        "options": [
            "Physical",
            "Managerial",
            "Technical",
            "Operational"
        ],
        "correct_answer": 1,
        "description": "Physical security controls include measures like photo ID checks and access control vestibules to prevent unauthorized entry to secured facilities."
    },
    {
        "question": "The local administrator account for a company's VPN appliance was unexpectedly used to log in to the remote management interface. Which of the following would have most likely prevented this from happening?",
        "options": [
            "Using least privilege",
            "Changing the default password",
            "Assigning individual user IDs",
            "Reviewing logs more frequently"
        ],
        "correct_answer": 2,
        "description": "Changing the default password is a critical security step that could have prevented unauthorized access to the VPN appliance's remote management interface."
    },

# page 4 of 7


    {
        "question": "Which of the following is the best way to secure an on-site data center against intrusion from an insider?",
        "options": [
            "Bollards",
            "Access badge",
            "Motion sensor",
            "Video surveillance"
        ],
        "correct_answer": 2,
        "description": "Access badges restrict entry to authorized personnel, providing a secure way to control who can access the data center."
    },
    {
        "question": "An engineer moved to another team and is unable to access the new team's shared folders while still being able to access the shared folders from the former team. After opening a ticket, the engineer discovers that the account was never moved to the new group. Which of the following access controls is most likely causing the lack of access?",
        "options": [
            "Role-based",
            "Discretionary",
            "Time of day",
            "Least privilege"
        ],
        "correct_answer": 1,
        "description": "Role-based access control assigns permissions based on a user's role, and the engineer's role was not updated to reflect the new team."
    },
    {
        "question": "Which of the following factors are the most important to address when formulating a training curriculum plan for a security awareness program? (Choose two.)",
        "options": [
            "Channels by which the organization communicates with customers",
            "The reporting mechanisms for ethics violations",
            "Threat vectors based on the industry in which the organization operates",
            "Secure software development training for all personnel",
            "Cadence and duration of training events",
            "Retraining requirements for individuals who fail phishing simulations"
        ],
        "correct_answer": [3, 6],
        "description": "Cadence and retraining are critical to ensuring the effectiveness of a security awareness program, especially in addressing industry-specific threats."
    },
    {
        "question": "A network administrator is working on a project to deploy a load balancer in the company's cloud environment. Which of the following fundamental security requirements does this project fulfill?",
        "options": [
            "Privacy",
            "Integrity",
            "Confidentiality",
            "Availability"
        ],
        "correct_answer": 4,
        "description": "Load balancers enhance availability by distributing traffic across multiple servers, ensuring the continuous operation of cloud services."
    },
    {
        "question": "A systems administrator is changing the password policy within an enterprise environment and wants this update implemented on all systems as quickly as possible. Which of the following operating system security measures will the administrator most likely use?",
        "options": [
            "Deploying PowerShell scripts",
            "Pushing GPO update",
            "Enabling PAP",
            "Updating EDR profiles"
        ],
        "correct_answer": 2,
        "description": "Group Policy Objects (GPO) allow for quick and uniform deployment of password policy changes across all systems in the domain."
    },
    {
        "question": "Which of the following would be most useful in determining whether the long-term cost to transfer a risk is less than the impact of the risk?",
        "options": [
            "ARO",
            "RTO",
            "RPO",
            "ALE",
            "SLE"
        ],
        "correct_answer": 4,
        "description": "Annualized Loss Expectancy (ALE) helps organizations compare the cost of transferring risk versus the potential financial impact of that risk."
    },
    {
        "question": "In order to strengthen a password and prevent a hacker from cracking it, a random string of 36 characters was added to the password. Which of the following best describes this technique?",
        "options": [
            "Key stretching",
            "Tokenization",
            "Data masking",
            "Salting"
        ],
        "correct_answer": 4,
        "description": "Salting adds a random string of characters to a password before hashing to make it more resistant to cracking attempts."
    },
    {
        "question": "A technician is deploying a new security camera. Which of the following should the technician do?",
        "options": [
            "Configure the correct VLAN.",
            "Perform a vulnerability scan.",
            "Disable unnecessary ports.",
            "Conduct a site survey."
        ],
        "correct_answer": 4,
        "description": "Disabling unnecessary ports on the security camera reduces the attack surface and helps prevent unauthorized access."
    },
    {
        "question": "A company is experiencing a web services outage on the public network. The services are up and available but inaccessible. The network logs show a sudden increase in network traffic that is causing the outage. Which of the following attacks is the organization experiencing?",
        "options": [
            "ARP poisoning",
            "Brute force",
            "Buffer overflow",
            "DDoS"
        ],
        "correct_answer": 4,
        "description": "A Distributed Denial of Service (DDoS) attack floods the network with excessive traffic, overwhelming resources and causing outages."
    },
    {
        "question": "Which of the following threat actors is the most likely to be motivated by profit?",
        "options": [
            "Hacktivist",
            "Insider threat",
            "Organized crime",
            "Shadow IT"
        ],
        "correct_answer": 3,
        "description": "Organized crime groups are often financially motivated, engaging in activities like ransomware attacks to profit from their exploits."
    },
    {
        "question": "An organization experiences a cybersecurity incident involving a command-and-control server. Which of the following logs should be analyzed to identify the impacted host? (Choose two.)",
        "options": [
            "Application",
            "Authentication",
            "DHCP",
            "Network",
            "Firewall",
            "Database"
        ],
        "correct_answer": [4, 5],
        "description": "Network and firewall logs can provide insights into the communications with the command-and-control server, helping to identify the impacted host."
    },
    {
        "question": "During a penetration test, a vendor attempts to enter an unauthorized area using an access badge. Which of the following types of tests does this represent?",
        "options": [
            "Defensive",
            "Passive",
            "Offensive",
            "Physical"
        ],
        "correct_answer": 4,
        "description": "A physical penetration test assesses the security of physical barriers and access controls, such as entering an unauthorized area using a badge."
    },
    {
        "question": "A systems administrator uses a key to encrypt a message being sent to a peer in a different branch office. The peer then uses the same key to decrypt the message. Which of the following describes this example?",
        "options": [
            "Symmetric",
            "Asymmetric",
            "Hashing",
            "Salting"
        ],
        "correct_answer": 1,
        "description": "Symmetric encryption uses the same key for both encryption and decryption, making it faster and suitable for secure communication between trusted parties."
    },
    {
        "question": "A visitor plugs a laptop into a network jack in the lobby and is able to connect to the company's network. Which of the following should be configured on the existing network infrastructure to best prevent this activity?",
        "options": [
            "Port security",
            "Web application firewall",
            "Transport layer security",
            "Virtual private network"
        ],
        "correct_answer": 1,
        "description": "Port security restricts the devices that can connect to a network port, preventing unauthorized devices from gaining access."
    },
    {
        "question": "A security administrator is reissuing a former employee's laptop. Which of the following is the best combination of data handling activities for the administrator to perform? (Choose two.)",
        "options": [
            "Data retention",
            "Certification",
            "Destruction",
            "Classification",
            "Sanitization",
            "Enumeration"
        ],
        "correct_answer": [2, 5],
        "description": "Sanitization and destruction ensure that all sensitive data is securely removed from the laptop before reissuing it to another user."
    },
    {
        "question": "A systems administrator would like to deploy a change to a production system. Which of the following must the administrator submit to demonstrate that the system can be restored to a working state in the event of a performance issue?",
        "options": [
            "Backout plan",
            "Impact analysis",
            "Test procedure",
            "Approval procedure"
        ],
        "correct_answer": 1,
        "description": "A backout plan outlines the steps to revert the system to its previous state if a change causes issues, ensuring business continuity."
    },
    {
        "question": "A company is redesigning its infrastructure and wants to reduce the number of physical servers in use. Which of the following architectures is best suited for this goal?",
        "options": [
            "Serverless",
            "Segmentation",
            "Virtualization",
            "Microservices"
        ],
        "correct_answer": 3,
        "description": "Virtualization allows multiple virtual servers to run on a single physical server, reducing the number of physical servers required."
    },
    {
        "question": "A bank set up a new server that contains customers' PII. Which of the following should the bank use to make sure the sensitive data is not modified?",
        "options": [
            "Full disk encryption",
            "Network access control",
            "File integrity monitoring",
            "User behavior analytics"
        ],
        "correct_answer": 3,
        "description": "File integrity monitoring (FIM) ensures that files containing sensitive data are not modified without authorization, protecting data integrity."
    },
    {
        "question": "Users at a company are reporting they are unable to access the URL for a new retail website because it is flagged as gambling and is being blocked. Which of the following changes would allow users to access the site?",
        "options": [
            "Creating a firewall rule to allow HTTPS traffic",
            "Configuring the IPS to allow shopping",
            "Tuning the DLP rule that detects credit card data",
            "Updating the categorization in the content filter"
        ],
        "correct_answer": 4,
        "description": "Updating the content filter's categorization to correctly reflect the website as a retail site will allow users to access it without triggering blocks."
    },
    {
        "question": "Which of the following most impacts an administrator's ability to address CVEs discovered on a server?",
        "options": [
            "Rescanning requirements",
            "Patch availability",
            "Organizational impact",
            "Risk tolerance"
        ],
        "correct_answer": 2,
        "description": "Patch availability directly affects whether a CVE can be mitigated, as patches are needed to fix vulnerabilities identified in CVEs."
    },
    {
        "question": "Which of the following describes effective change management procedures?",
        "options": [
            "Approving the change after a successful deployment",
            "Having a backout plan when a patch fails",
            "Using a spreadsheet for tracking changes",
            "Using an automatic change control bypass for security updates"
        ],
        "correct_answer": 2,
        "description": "Having a backout plan is essential for effective change management, ensuring that the system can be restored if a change fails."
    },
    {
        "question": "The CIRT is reviewing an incident that involved a human resources recruiter exfiltrating sensitive company data. The CIRT found that the recruiter was able to use HTTP over port 53 to upload documents to a web server. Which of the following security infrastructure devices could have identified and blocked this activity?",
        "options": [
            "WAF utilizing SSL decryption",
            "NGFW utilizing application inspection",
            "UTM utilizing a threat feed",
            "SD-WAN utilizing IPSec"
        ],
        "correct_answer": 2,
        "description": "A Next-Generation Firewall (NGFW) with application inspection can detect and block unusual traffic patterns, such as using HTTP over port 53."
    },
    {
        "question": "An enterprise is working with a third party and needs to allow access between the internal networks of both parties for a secure file migration. The solution needs to ensure encryption is applied to all traffic that is traversing the networks. Which of the following solutions should most likely be implemented?",
        "options": [
            "EAP",
            "IPSec",
            "SD-WAN",
            "TLS"
        ],
        "correct_answer": 2,
        "description": "IPSec provides end-to-end encryption for data in transit, ensuring that traffic between the enterprise and third-party networks is secure."
    },
    {
        "question": "An administrator has identified and fingerprinted specific files that will generate an alert if an attempt is made to email these files outside of the organization. Which of the following best describes the tool the administrator is using?",
        "options": [
            "DLP",
            "SNMP traps",
            "SCAP",
            "IPS"
        ],
        "correct_answer": 1,
        "description": "Data Loss Prevention (DLP) tools are designed to detect and prevent the unauthorized transfer of sensitive data, such as emailing specific files."
    },
    {
        "question": "A software developer released a new application and is distributing application files via the developer's website. Which of the following should the developer post on the website to allow users to verify the integrity of the downloaded files?",
        "options": [
            "Hashes",
            "Certificates",
            "Algorithms",
            "Salting"
        ],
        "correct_answer": 1,
        "description": "Posting hashes of the files allows users to verify that the files they downloaded have not been altered by comparing the hash values."
    },
    {
        "question": "An organization wants to limit potential impact to its log-in database in the event of a breach. Which of the following options is the security team most likely to recommend?",
        "options": [
            "Tokenization",
            "Hashing",
            "Obfuscation",
            "Segmentation"
        ],
        "correct_answer": 2,
        "description": "Hashing passwords ensures that even if the login database is breached, the actual passwords are not exposed, limiting the impact."
    },
    {
        "question": "An administrator finds that all user workstations and servers are displaying a message that is associated with files containing an extension of .ryk. Which of the following types of infections is present on the systems?",
        "options": [
            "Virus",
            "Trojan",
            "Spyware",
            "Ransomware"
        ],
        "correct_answer": 4,
        "description": "Ransomware is a type of malware that encrypts files and displays a message demanding payment, often changing file extensions like .ryk."
    },
{
    "question": "A systems administrator is advised that an external web server is not functioning properly. The administrator reviews the following firewall logs containing traffic going to the web server: Date         | Time        | SourceIP       | SPort | Flag | DestIP     | DPort 2023-01-25   | 01:45:09.102 | 98.123.45.100  | 4560  | SYN  | 100.50.20.7 | 443 2023-01-25   | 01:45:09.102 | 95.123.45.101  | 3361  | SYN  | 100.50.20.7 | 443 2023-01-25   | 01:45:09.102 | 99.123.45.102  | 3662  | SYN  | 100.50.20.7 | 443 2023-01-25   | 01:45:09.104 | 99.123.45.103  | 5663  | SYN  | 100.50.20.7 | 443 2023-01-25   | 01:45:09.104 | 80.123.45.105  | 4064  | SYN  | 100.50.20.7 | 443 2023-01-25   | 01:45:09.102 | 80.123.45.106  | 4365  | SYN  | 100.50.20.7 | 443 Which of the following attacks is likely occurring?",
    "options": [
        "DDoS",
        "Directory traversal",
        "Brute-force",
        "HTTPS downgrade"
    ],
    "correct_answer": 1,
    "description": "A Distributed Denial of Service (DDoS) attack is likely occurring, as indicated by the large number of SYN packets targeting the same destination IP and port."
},

    {
        "question": "An organization would like to calculate the time needed to resolve a hardware issue with a server. Which of the following risk management processes describes this example?",
        "options": [
            "Recovery point objective",
            "Mean time between failures",
            "Recovery time objective",
            "Mean time to repair"
        ],
        "correct_answer": 4,
        "description": "Mean Time to Repair (MTTR) is a metric used to determine the average time required to fix a hardware issue and restore functionality."
    },
    {
        "question": "A security engineer is installing an IPS to block signature-based attacks in the environment. Which of the following modes will best accomplish this task?",
        "options": [
            "Monitor",
            "Sensor",
            "Audit",
            "Active"
        ],
        "correct_answer": 4,
        "description": "Active mode in an Intrusion Prevention System (IPS) allows the system to block detected signature-based attacks in real-time."
    },
    {
        "question": "An IT manager is increasing the security capabilities of an organization after a data classification initiative determined that sensitive data could be exfiltrated from the environment. Which of the following solutions would mitigate the risk?",
        "options": [
            "XDR",
            "SPF",
            "DLP",
            "DMARC"
        ],
        "correct_answer": 3,
        "description": "Data Loss Prevention (DLP) solutions are designed to detect and prevent unauthorized exfiltration of sensitive data from the organization."
    },
    {
        "question": "Which of the following is used to protect a computer from viruses, malware, and Trojans being installed and moving laterally across the network?",
        "options": [
            "IDS",
            "ACL",
            "EDR",
            "NAC"
        ],
        "correct_answer": 3,
        "description": "Endpoint Detection and Response (EDR) solutions provide comprehensive protection against threats like viruses and malware, including lateral movement across networks."
    },
    {
        "question": "Client files can only be accessed by employees who need to know the information and have specified roles in the company. Which of the following best describes this security concept?",
        "options": [
            "Availability",
            "Confidentiality",
            "Integrity",
            "Non-repudiation"
        ],
        "correct_answer": 2,
        "description": "Confidentiality ensures that sensitive information is only accessible to those who are authorized and need to know."
    },
    {
        "question": "Which of the following describes the category of data that is most impacted when it is lost?",
        "options": [
            "Confidential",
            "Public",
            "Private",
            "Critical"
        ],
        "correct_answer": 4,
        "description": "Critical data is essential to an organization's operations and its loss can have significant impacts, including financial and reputational damage."
    },
    {
        "question": "A new employee logs in to the email system for the first time and notices a message from human resources about onboarding. The employee hovers over a few of the links within the email and discovers that the links do not correspond to links associated with the company. Which of the following attack vectors is most likely being used?",
        "options": [
            "Business email",
            "Social engineering",
            "Unsecured network",
            "Default credentials"
        ],
        "correct_answer": 1,
        "description": "Social engineering involves tricking individuals into revealing confidential information or taking certain actions, often through deceptive emails."
    },
    {
        "question": "Which of the following describes the understanding between a company and a client about what will be provided and the accepted time needed to provide the company with the resources?",
        "options": [
            "SLA",
            "MOU",
            "MOA",
            "BPA"
        ],
        "correct_answer": 1,
        "description": "A Service Level Agreement (SLA) outlines the expected level of service, including timeframes, between a service provider and a client."
    },
    {
        "question": "A company that is located in an area prone to hurricanes is developing a disaster recovery plan and looking at site considerations that allow the company to immediately continue operations. Which of the following is the best type of site for this company?",
        "options": [
            "Cold",
            "Tertiary",
            "Warm",
            "Hot"
        ],
        "correct_answer": 4,
        "description": "A hot site is fully equipped with the necessary infrastructure and is ready to take over operations immediately in the event of a disaster."
    },
    {
        "question": "Which of the following security controls is most likely being used when a critical legacy server is segmented into a private network?",
        "options": [
            "Deterrent",
            "Corrective",
            "Compensating",
            "Preventive"
        ],
        "correct_answer": 3,
        "description": "Compensating controls, like network segmentation, are used to mitigate the risks associated with legacy systems that cannot be fully secured."
    },
    {
        "question": "Which of the following best describes the practice of researching laws and regulations related to information security operations within a specific industry?",
        "options": [
            "Compliance reporting",
            "GDPR",
            "Due diligence",
            "Attestation"
        ],
        "correct_answer": 3,
        "description": "Due diligence involves researching and understanding legal and regulatory requirements to ensure that security practices are compliant."
    },
    {
        "question": "Which of the following considerations is the most important for an organization to evaluate as it establishes and maintains a data privacy program?",
        "options": [
            "Reporting structure for the data privacy officer",
            "Request process for data subject access",
            "Role as controller or processor",
            "Physical location of the company"
        ],
        "correct_answer": 3,
        "description": "Understanding whether the organization acts as a data controller or processor is crucial for establishing and maintaining a data privacy program."
    },
    {
        "question": "A security analyst is investigating a workstation that is suspected of outbound communication to a command-and-control server. During the investigation, the analyst discovered that logs on the endpoint were deleted. Which of the following logs would the analyst most likely look at next?",
        "options": [
            "IPS",
            "Firewall",
            "ACL",
            "Windows security"
        ],
        "correct_answer": 2,
        "description": "Firewall logs can provide information about network traffic, including any communications between the workstation and a command-and-control server."
    },
    {
        "question": "An IT manager is putting together a documented plan describing how the organization will keep operating in the event of a global incident. Which of the following plans is the IT manager creating?",
        "options": [
            "Business continuity",
            "Physical security",
            "Change management",
            "Disaster recovery"
        ],
        "correct_answer": 1,
        "description": "A business continuity plan outlines the steps an organization will take to ensure it can continue operating during and after a disruptive event."
    },
    {
        "question": "A business needs a recovery site but does not require immediate failover. The business also wants to reduce the workload required to recover from an outage. Which of the following recovery sites is the best option?",
        "options": [
            "Hot",
            "Cold",
            "Warm",
            "Geographically dispersed"
        ],
        "correct_answer": 3,
        "description": "A warm site offers a compromise between hot and cold sites, providing some pre-installed infrastructure to speed up recovery without the cost of a fully operational hot site."
    },
    {
        "question": "A security team is setting up a new environment for hosting the organization's on-premises software application as a cloud-based service. Which of the following should the team ensure is in place in order for the organization to follow security best practices?",
        "options": [
            "Virtualization and isolation of resources",
            "Network segmentation",
            "Data encryption",
            "Strong authentication policies"
        ],
        "correct_answer": 1,
        "description": "Virtualization and resource isolation are critical in a cloud environment to ensure that different applications and data sets are securely separated."
    },
    {
        "question": "A manager receives an email that contains a link to receive a refund. After hovering over the link, the manager notices that the domain's URL points to a suspicious link. Which of the following security practices helped the manager to identify the attack?",
        "options": [
            "End user training",
            "Policy review",
            "URL scanning",
            "Plain text email"
        ],
        "correct_answer": 1,
        "description": "End user training helps employees recognize signs of phishing and other malicious activities, such as suspicious URLs in emails."
    },
    {
        "question": "A company wants to verify that the software the company is deploying came from the vendor the company purchased the software from. Which of the following is the best way for the company to confirm this information?",
        "options": [
            "Validate the code signature.",
            "Execute the code in a sandbox.",
            "Search the executable for ASCII strings.",
            "Generate a hash of the files."
        ],
        "correct_answer": 1,
        "description": "Validating the code signature ensures that the software has not been tampered with and confirms its authenticity as coming from the vendor."
    },
    {
        "question": "A systems administrator notices that one of the systems critical for processing customer transactions is running an end-of-life operating system. Which of the following techniques would increase enterprise security?",
        "options": [
            "Installing HIDS on the system",
            "Placing the system in an isolated VLAN",
            "Decommissioning the system",
            "Encrypting the system's hard drive"
        ],
        "correct_answer": 2,
        "description": "Placing the system in an isolated VLAN helps protect it from potential threats by limiting its network exposure, which is crucial for end-of-life systems."
    },
    {
        "question": "The Chief Information Security Officer (CISO) at a large company would like to gain an understanding of how the company's security policies compare to the requirements imposed by external regulators. Which of the following should the CISO use?",
        "options": [
            "Penetration test",
            "Internal audit",
            "Attestation",
            "External examination"
        ],
        "correct_answer": 4,
        "description": "An internal audit allows the CISO to assess the organization's security policies against regulatory requirements and identify any gaps."
    },
    {
        "question": "A systems administrator notices that the research and development department is not using the company VPN when accessing various company-related services and systems. Which of the following scenarios describes this activity?",
        "options": [
            "Espionage",
            "Data exfiltration",
            "Nation-state attack",
            "Shadow IT"
        ],
        "correct_answer": 4,
        "description": "Shadow IT refers to the use of IT systems, software, and services without the knowledge or approval of the IT department, such as bypassing the company VPN."
    },
    {
        "question": "The marketing department set up its own project management software without telling the appropriate departments. Which of the following describes this scenario?",
        "options": [
            "Shadow IT",
            "Insider threat",
            "Data exfiltration",
            "Service disruption"
        ],
        "correct_answer": 1,
        "description": "Shadow IT occurs when departments or individuals use unauthorized software or services without the knowledge of the IT department."
    }


]