questions_701_A = [
    {
        "question": "Which of the following threat actors is the most likely to be hired by a foreign government to attack critical systems located in other countries?",
        "options": [
            "Hacktivist",
            "Whistleblower",
            "Organized crime",
            "Unskilled attacker"
        ],
        "correct_answer": 3,
        "description": "Organized crime groups are often well-resourced and capable of executing sophisticated attacks, potentially under the employment of foreign governments.\n\n- Hacktivist: Individuals or groups that use hacking to promote political ends.\n- Whistleblower: Individuals who expose information or activities within a private or public organization.\n- Organized crime: Criminal organizations that are often involved in sophisticated, large-scale illegal activities.\n- Unskilled attacker: Individuals with limited technical skills and resources.\n\n**Domain 1: Attacks, Threats, and Vulnerabilities**"
    },
    {
        "question": "Which of the following is used to add extra complexity before using a one-way data transformation algorithm?",
        "options": [
            "Key stretching",
            "Data masking",
            "Steganography",
            "Salting"
        ],
        "correct_answer": 4,
        "description": "Salting is a technique used to add randomness to passwords before hashing, increasing security against attacks like rainbow tables.\n\n- Key stretching: Techniques used to make keys harder to crack by increasing the time it takes to derive the key.\n- Data masking: The process of hiding original data with modified content.\n- Steganography: The technique of hiding secret data within an ordinary, non-secret file or message.\n- Salting: Adding random data to inputs of a hash function to ensure that the output is unique.\n\n**Domain 3: Implementation**"
    },
    {
        "question": "An employee clicked a link in an email from a payment website that asked the employee to update contact information. The employee entered the log-in information but received a 'page not found' error message. Which of the following types of social engineering attacks occurred?",
        "options": [
            "Brand impersonation",
            "Pretexting",
            "Typosquatting",
            "Phishing"
        ],
        "correct_answer": 4,
        "description": "Phishing attacks trick users into providing sensitive information by posing as a legitimate entity, often using fake websites.\n\n- Brand impersonation: Fraudulent use of a company's brand to deceive users.\n- Pretexting: A form of social engineering where an attacker creates a fabricated scenario to steal information.\n- Typosquatting: Registering domains with misspellings of popular websites to trick users.\n- Phishing: A technique used to trick individuals into providing sensitive information by pretending to be a trustworthy entity.\n\n**Domain 1: Attacks, Threats, and Vulnerabilities**"
    },
    {
        "question": "An enterprise is trying to limit outbound DNS traffic originating from its internal network. Outbound DNS requests will only be allowed from one device with the IP address 10.50.10.25. Which of the following firewall ACLs will accomplish this goal?",
        "options": [
            "Access list outbound permit 0.0.0.0/0 0.0.0.0/0 port 53 Access list outbound deny 10.50.10.25/32 0.0.0.0/0 port 53",
            "Access list outbound permit 0.0.0.0/0 10.50.10.25/32 port 53 Access list outbound deny 0.0.0.0/0 0.0.0.0/0 port 53",
            "Access list outbound permit 0.0.0.0/0 0.0.0.0/0 port 53 Access list outbound deny 0.0.0.0/0 10.50.10.25/32 port 53",
            "Access list outbound permit 10.50.10.25/32 0.0.0.0/0 port 53 Access list outbound deny 0.0.0.0/0 0.0.0.0/0 port 53"
        ],
        "correct_answer": 4,
        "description": "Allowing outbound DNS traffic only from a specific IP address, in this case, 10.50.10.25, and denying it for all others is the correct approach.\n\n- Incorrect because it permits all traffic and denies from the specific IP.\n- Incorrect because it denies all traffic except for one IP, which does not match the requirement.\n- Incorrect because the deny rule is not structured properly.\n- Correct because it correctly permits traffic from 10.50.10.25 and denies all other traffic.\n\n**Domain 2: Architecture and Design**"
    },
    {
        "question": "A data administrator is configuring authentication for a SaaS application and would like to reduce the number of credentials employees need to maintain. The company prefers to use domain credentials to access new SaaS applications. Which of the following methods would allow this functionality?",
        "options": [
            "SSO",
            "LEAP",
            "MFA",
            "PEAP"
        ],
        "correct_answer": 1,
        "description": "Single Sign-On (SSO) allows employees to use a single set of credentials to access multiple applications, simplifying the authentication process.\n\n- SSO (Single Sign-On): Allows users to log in with a single ID and password across multiple systems.\n- LEAP (Lightweight Extensible Authentication Protocol): An authentication protocol for wireless networks.\n- MFA (Multi-Factor Authentication): Requires multiple forms of verification before granting access.\n- PEAP (Protected Extensible Authentication Protocol): A version of EAP used in wireless networks.\n\n**Domain 3: Implementation**"
    },
    {
        "question": "Which of the following scenarios describes a possible business email compromise attack?",
        "options": [
            "An employee receives a gift card request in an email that has an executive’s name in the display field of the email.",
            "Employees who open an email attachment receive messages demanding payment in order to access files.",
            "A service desk employee receives an email from the HR director asking for log-in credentials to a cloud administrator account.",
            "An employee receives an email with a link to a phishing site that is designed to look like the company’s email portal."
        ],
        "correct_answer": 3,
        "description": "Business Email Compromise (BEC) often involves emails that appear to come from high-level executives, requesting actions like wire transfers or gift card purchases.\n\n- This describes a BEC attack, where attackers impersonate executives to make fraudulent requests.\n- This describes a ransomware attack, which encrypts files and demands payment to unlock them.\n- Correct because it involves a BEC attack where attackers impersonate high-level personnel.\n- This is a phishing attack, which aims to steal credentials by directing users to fake sites.\n\n**Domain 1: Attacks, Threats, and Vulnerabilities**"
    },
    {
        "question": "A company prevented direct access from the database administrators’ workstations to the network segment that contains database servers. Which of the following should a database administrator use to access the database servers?",
        "options": [
            "Jump server",
            "RADIUS",
            "HSM",
            "Load balancer"
        ],
        "correct_answer": 1,
        "description": "A jump server, also known as a jump box, provides a controlled access point for managing devices in a different security zone.\n\n- Jump server: Provides controlled access to devices in a different security zone.\n- RADIUS (Remote Authentication Dial-In User Service): Used for network access control.\n- HSM (Hardware Security Module): Used for cryptographic key management.\n- Load balancer: Distributes traffic across multiple servers.\n\n**Domain 2: Architecture and Design**"
    },
    {
        "question": "An organization’s internet-facing website was compromised when an attacker exploited a buffer overflow. Which of the following should the organization deploy to best protect against similar attacks in the future?",
        "options": [
            "NGFW",
            "WAF",
            "TLS",
            "SD-WAN"
        ],
        "correct_answer": 2,
        "description": "A Web Application Firewall (WAF) can help protect against vulnerabilities like buffer overflows by filtering and monitoring HTTP traffic.\n\n- NGFW (Next-Generation Firewall): Provides advanced network security features.\n- WAF (Web Application Firewall): Filters and monitors HTTP traffic to protect web applications.\n- TLS (Transport Layer Security): Secures communications.\n- SD-WAN (Software-Defined Wide Area Network): Optimizes network performance.\n\n**Domain 3: Implementation**"
    },
    {
        "question": "An administrator notices that several users are logging in from suspicious IP addresses. After speaking with the users, the administrator determines that the employees were not logging in from those IP addresses and resets the affected users’ passwords. Which of the following should the administrator implement to prevent this type of attack from succeeding in the future?",
        "options": [
            "Multifactor authentication",
            "Permissions assignment",
            "Access management",
            "Password complexity"
        ],
        "correct_answer": 1,
        "description": "Implementing multifactor authentication (MFA) adds an additional layer of security, making it harder for attackers to gain unauthorized access.\n\n- Multifactor authentication (MFA): Adds an extra layer of security by requiring multiple forms of verification.\n- Permissions assignment: Refers to setting access controls.\n- Access management: The process of managing user access to resources.\n- Password complexity: Involves requiring strong passwords.\n\n**Domain 4: Operations and Incident Response**"
    },
    {
        "question": "An employee receives a text message that appears to have been sent by the payroll department and is asking for credential verification. Which of the following social engineering techniques are being attempted? (Choose two.)",
        "options": [
            "Typosquatting",
            "Phishing",
            "Impersonation",
            "Vishing",
            "Smishing",
            "Misinformation"
        ],
        "correct_answer": [3, 5],
        "description": "This scenario describes an attempt at impersonation and smishing. \nSmishing is phishing conducted via SMS, and impersonation involves pretending to be a trusted entity.\n\n- Typosquatting: Using misspelled domain names to trick users.\n- Phishing: Tricking individuals into providing sensitive information.\n- Impersonation: Pretending to be a trusted entity to deceive others.\n- Vishing: Phishing conducted via voice calls.\n- Smishing: Phishing conducted via SMS (text messages).\n- Misinformation: Spreading false information.\n\n**Domain 1: Attacks, Threats, and Vulnerabilities**"
    },
    {
        "question": "Several employees received a fraudulent text message from someone claiming to be the Chief Executive Officer (CEO). The message stated: 'I’m in an airport right now with no access to email. I need you to buy gift cards for employee recognition awards. Please send the gift cards to following email address.' Which of the following are the best responses to this situation? (Choose two).",
        "options": [
            "Cancel current employee recognition gift cards.",
            "Add a smishing exercise to the annual company training.",
            "Issue a general email warning to the company.",
            "Have the CEO change phone numbers.",
            "Conduct a forensic investigation on the CEO’s phone.",
            "Implement mobile device management."
        ],
        "correct_answer": [2, 3],
        "description": "The best responses include adding a smishing exercise to the training and issuing a warning to the company about this specific threat.\n\n- Cancel current employee recognition gift cards: Unnecessary without a direct threat.\n- Add a smishing exercise to the annual company training: Helps raise awareness and train employees.\n- Issue a general email warning to the company: Informs all employees of the potential threat.\n- Have the CEO change phone numbers: Not directly addressing the root of the issue.\n- Conduct a forensic investigation on the CEO’s phone: Excessive without evidence of compromise.\n- Implement mobile device management: A broader measure that doesn't address the immediate issue.\n\n**Domain 4: Operations and Incident Response**"
    },
    {
        "question": "A company is required to use certified hardware when building networks. Which of the following best addresses the risks associated with procuring counterfeit hardware?",
        "options": [
            "A thorough analysis of the supply chain",
            "A legally enforceable corporate acquisition policy",
            "A right to audit clause in vendor contracts and SOWs",
            "An in-depth penetration test of all suppliers and vendors"
        ],
        "correct_answer": 1,
        "description": "Conducting a thorough analysis of the supply chain helps to mitigate risks associated with counterfeit hardware by ensuring authenticity and reliability.\n\n- Thorough analysis of the supply chain: Ensures that all hardware components are authentic and reliable.\n- Legally enforceable corporate acquisition policy: Sets legal parameters but doesn't necessarily prevent counterfeit hardware.\n- Right to audit clause in vendor contracts and SOWs: Provides the ability to review vendor practices.\n- In-depth penetration test of all suppliers and vendors: Excessive and not specifically targeted to hardware authenticity.\n\n**Domain 5: Governance, Risk, and Compliance**"
    },







  {
        "question": "Which of the following provides the details about the terms of a test with a third-party penetration tester?",
        "options": [
            "Rules of engagement",
            "Supply chain analysis",
            "Right to audit clause",
            "Due diligence"
        ],
        "correct_answer": 1,
        "description": "Rules of engagement outline the scope, boundaries, and expectations for a penetration test, ensuring both parties understand the terms of the engagement.\n\n- Rules of engagement: Defines the scope and boundaries of the penetration test.\n- Supply chain analysis: Assesses suppliers' security.\n- Right to audit clause: Allows for inspections of vendors.\n- Due diligence: Involves careful evaluation of risks.\n\n**Domain 5: Governance, Risk, and Compliance**"
    },
    {
        "question": "A penetration tester begins an engagement by performing port and service scans against the client environment according to the rules of engagement. Which of the following reconnaissance types is the tester performing?",
        "options": [
            "Active",
            "Passive",
            "Defensive",
            "Offensive"
        ],
        "correct_answer": 1,
        "description": "Active reconnaissance involves directly interacting with the target system to gather information, such as through port and service scanning.\n\n- Active reconnaissance: Direct interaction with the target to gather information.\n- Passive reconnaissance: Gathering information without interacting directly with the target.\n- Defensive: Refers to security strategies to protect assets.\n- Offensive: Involves taking actions to breach or compromise a target.\n\n**Domain 1: Attacks, Threats, and Vulnerabilities**"
    },
    {
        "question": "Which of the following is required for an organization to properly manage its restore process in the event of system failure?",
        "options": [
            "IRP",
            "DRP",
            "RPO",
            "SDLC"
        ],
        "correct_answer": 2,
        "description": "A Disaster Recovery Plan (DRP) is essential for managing the restore process after a system failure, ensuring business continuity.\n\n- IRP (Incident Response Plan): Focuses on handling security incidents.\n- DRP (Disaster Recovery Plan): Ensures business continuity by restoring systems after a failure.\n- RPO (Recovery Point Objective): Defines the maximum acceptable data loss.\n- SDLC (Software Development Life Cycle): Involves the stages of software development.\n\n**Domain 5: Governance, Risk, and Compliance**"
    },
    {
        "question": "Which of the following vulnerabilities is associated with installing software outside of a manufacturer’s approved software repository?",
        "options": [
            "Jailbreaking",
            "Memory injection",
            "Resource reuse",
            "Side loading"
        ],
        "correct_answer": 4,
        "description": "Side loading refers to installing applications from unauthorized sources, which can introduce security vulnerabilities.\n\n- Jailbreaking: Removes software restrictions on devices.\n- Memory injection: Involves injecting malicious code into memory.\n- Resource reuse: Refers to insecurely reusing system resources.\n- Side loading: Installing applications from unauthorized sources.\n\n**Domain 1: Attacks, Threats, and Vulnerabilities**"
    },
    {
        "question": "A security analyst is reviewing the following logs:\n\n[10:00:00 AM] Login rejected - username administrator - password Spring2023\n[10:00:01 AM] Login rejected - username jsmith - password Spring2023\n[10:00:01 AM] Login rejected - username guest - password Spring2023\n[10:00:02 AM] Login rejected - username cpolk - password Spring2023\n[10:00:03 AM] Login rejected - username fmartin - password Spring2023\n\nWhich of the following attacks is most likely occurring?",
        "options": [
            "Password spraying",
            "Account forgery",
            "Pass-the-hash",
            "Brute-force"
        ],
        "correct_answer": 1,
        "description": "Password spraying is an attack method where the attacker tries a common password across multiple accounts before moving on to another password, as indicated by the logs showing multiple login attempts with the same password.\n\n- Password spraying: An attack method involving trying a common password across multiple accounts.\n- Account forgery: Involves creating unauthorized accounts.\n- Pass-the-hash: Uses a hashed password to authenticate.\n- Brute-force: Involves systematically trying all possible passwords.\n\n**Domain 1: Attacks, Threats, and Vulnerabilities**"
    },
    {
        "question": "An analyst is evaluating the implementation of Zero Trust principles within the data plane. Which of the following would be most relevant for the analyst to evaluate?",
        "options": [
            "Secured zones",
            "Subject role",
            "Adaptive identity",
            "Threat scope reduction"
        ],
        "correct_answer": 1,
        "description": "Zero Trust principles focus on securing data by segmenting the network into secured zones to minimize potential attack surfaces.\n\n- Secured zones: Segments of the network designed to minimize potential attack surfaces.\n- Subject role: Involves assigning permissions based on roles.\n- Adaptive identity: Refers to dynamically adjusting access controls.\n- Threat scope reduction: Focuses on limiting the impact of potential threats.\n\n**Domain 2: Architecture and Design**"
    },
    {
        "question": "An engineer needs to find a solution that creates an added layer of security by preventing unauthorized access to internal company resources. Which of the following would be the best solution?",
        "options": [
            "RDP server",
            "Jump server",
            "Proxy server",
            "Hypervisor"
        ],
        "correct_answer": 2,
        "description": "A jump server acts as an intermediary and controlled access point, adding a layer of security for accessing internal resources.\n\n- RDP (Remote Desktop Protocol) server: Allows remote access to a system.\n- Jump server: Provides controlled access to internal resources.\n- Proxy server: Acts as an intermediary for requests from clients.\n- Hypervisor: Manages virtual machines.\n\n**Domain 2: Architecture and Design**"
    },
    {
        "question": "A company’s web filter is configured to scan the URL for strings and deny access when matches are found. Which of the following search strings should an analyst employ to prohibit access to non-encrypted websites?",
        "options": [
            "encryption=off",
            "http://",
            "www.*.com",
            ":443"
        ],
        "correct_answer": 2,
        "description": "Blocking access to non-encrypted (HTTP) websites can be done by filtering for URLs that start with 'http://'.\n\n- encryption=off: Indicates a site disabling encryption, but not specifically HTTP.\n- http://: Represents non-encrypted websites.\n- www.*.com: A general domain pattern that doesn't necessarily indicate encryption status.\n- :443: Represents HTTPS, which is encrypted.\n\n**Domain 3: Implementation**"
    },
    {
        "question": "During a security incident, the security operations team identified sustained network traffic from a malicious IP address: 10.1.4.9. A security analyst is creating an inbound firewall rule to block the IP address from accessing the organization’s network. Which of the following fulfills this request?",
        "options": [
            "access-list inbound deny ip source 0.0.0.0/0 destination 10.1.4.9/32",
            "access-list inbound deny ip source 10.1.4.9/32 destination 0.0.0.0/0",
            "access-list inbound permit ip source 10.1.4.9/32 destination 0.0.0.0/0",
            "access-list inbound permit ip source 0.0.0.0/0 destination 10.1.4.9/32"
        ],
        "correct_answer": 2,
        "description": "Blocking traffic from a specific IP address (10.1.4.9) can be achieved by denying all inbound traffic from that source.\n\n- access-list inbound deny ip source 0.0.0.0/0 destination 10.1.4.9/32: Incorrect, denies all traffic to the IP.\n- access-list inbound deny ip source 10.1.4.9/32 destination 0.0.0.0/0: Correct, denies traffic from the specific IP address.\n- access-list inbound permit ip source 10.1.4.9/32 destination 0.0.0.0/0: Incorrect, permits traffic from the IP.\n- access-list inbound permit ip source 0.0.0.0/0 destination 10.1.4.9/32: Incorrect, permits traffic to the IP.\n\n**Domain 3: Implementation**"
    },
    {
        "question": "A company needs to provide administrative access to internal resources while minimizing the traffic allowed through the security boundary. Which of the following methods is most secure?",
        "options": [
            "Implementing a bastion host",
            "Deploying a perimeter network",
            "Installing a WAF",
            "Utilizing single sign-on"
        ],
        "correct_answer": 1,
        "description": "A bastion host is a secure computer used to manage access to internal resources while minimizing security risks.\n\n- Implementing a bastion host: Provides secure access to internal resources.\n- Deploying a perimeter network: Separates internal and external networks but doesn't provide secure access control.\n- Installing a WAF (Web Application Firewall): Protects web applications but doesn't control internal access.\n- Utilizing single sign-on (SSO): Simplifies access across systems but doesn't specifically secure internal resources.\n\n**Domain 2: Architecture and Design**"
    },
    {
        "question": "A security analyst is reviewing alerts in the SIEM related to potential malicious network traffic coming from an employee’s corporate laptop. The security analyst has determined that additional data about the executable running on the machine is necessary to continue the investigation. Which of the following logs should the analyst use as a data source?",
        "options": [
            "Application",
            "IPS/IDS",
            "Network",
            "Endpoint"
        ],
        "correct_answer": 4,
        "description": "Endpoint logs provide detailed information about the software and processes running on a device, crucial for investigating suspicious activities.\n\n- Application: Logs track activities of applications.\n- IPS/IDS (Intrusion Prevention/Detection Systems): Monitor network traffic for suspicious activity.\n- Network: Logs capture data about network traffic.\n- Endpoint: Logs provide detailed information about software and processes on devices.\n\n**Domain 4: Operations and Incident Response**"
    },
    {
        "question": "A cyber operations team informs a security analyst about a new tactic malicious actors are using to compromise networks. SIEM alerts have not yet been configured. Which of the following best describes what the security analyst should do to identify this behavior?",
        "options": [
            "Digital forensics",
            "E-discovery",
            "Incident response",
            "Threat hunting"
        ],
        "correct_answer": 4,
        "description": "Threat hunting involves proactively searching for indicators of compromise and malicious activity before they trigger any alerts.\n\n- Digital forensics: Involves analyzing digital evidence.\n- E-discovery: Refers to the process of identifying and producing digital information for legal purposes.\n- Incident response: The process of managing and addressing security incidents.\n- Threat hunting: Proactively searching for indicators of compromise and malicious activity.\n\n**Domain 4: Operations and Incident Response**"
    },
    {
        "question": "A company purchased cyber insurance to address items listed on the risk register. Which of the following strategies does this represent?",
        "options": [
            "Accept",
            "Transfer",
            "Mitigate",
            "Avoid"
        ],
        "correct_answer": 2,
        "description": "By purchasing cyber insurance, the company is transferring the financial risk associated with potential security incidents.\n\n- Accept: Acknowledging the risk without taking action.\n- Transfer: Shifting the risk to another party (e.g., through insurance).\n- Mitigate: Taking steps to reduce the risk.\n- Avoid: Taking actions to eliminate the risk.\n\n**Domain 5: Governance, Risk, and Compliance**"
    },
    {
        "question": "A security administrator would like to protect data on employees’ laptops. Which of the following encryption techniques should the security administrator use?",
        "options": [
            "Partition",
            "Asymmetric",
            "Full disk",
            "Database"
        ],
        "correct_answer": 3,
        "description": "Full disk encryption (FDE) protects all data on the laptop's hard drive, ensuring that unauthorized users cannot access sensitive information.\n\n- Partition: Dividing storage into separate sections.\n- Asymmetric: Uses a pair of public and private keys for encryption.\n- Full disk: Encrypts all data on the hard drive.\n- Database: Protects data within databases.\n\n**Domain 3: Implementation**"
    },
    {
        "question": "Which of the following security control types does an acceptable use policy best represent?",
        "options": [
            "Detective",
            "Compensating",
            "Corrective",
            "Preventive"
        ],
        "correct_answer": 4,
        "description": "An acceptable use policy is a preventive control designed to ensure that employees use company resources responsibly and securely.\n\n- Detective: Identifies and records incidents.\n- Compensating: Alternative measures when primary controls are not feasible.\n- Corrective: Aims to fix issues after they occur.\n- Preventive: Designed to stop incidents before they happen.\n\n**Domain 5: Governance, Risk, and Compliance**"
    },
    {
        "question": "An IT manager informs the entire help desk staff that only the IT manager and the help desk lead will have access to the administrator console of the help desk software. Which of the following security techniques is the IT manager setting up?",
        "options": [
            "Hardening",
            "Employee monitoring",
            "Configuration enforcement",
            "Least privilege"
        ],
        "correct_answer": 4,
        "description": "The principle of least privilege ensures that employees only have the access necessary to perform their job functions, minimizing security risks.\n\n- Hardening: Securing systems by reducing vulnerabilities.\n- Employee monitoring: Tracks employee activities.\n- Configuration enforcement: Ensures that system settings adhere to security policies.\n- Least privilege: Ensures that employees only have the access necessary for their roles.\n\n**Domain 5: Governance, Risk, and Compliance**"
    },
    {
        "question": "Which of the following is the most likely to be used to document risks, responsible parties, and thresholds?",
        "options": [
            "Risk tolerance",
            "Risk transfer",
            "Risk register",
            "Risk analysis"
        ],
        "correct_answer": 3,
        "description": "A risk register is a tool used to document all identified risks, including their likelihood, impact, and the parties responsible for managing them.\n\n- Risk tolerance: Defines the level of risk an organization is willing to accept.\n- Risk transfer: Involves shifting the risk to another party.\n- Risk register: Documents identified risks and management strategies.\n- Risk analysis: The process of evaluating potential risks.\n\n**Domain 5: Governance, Risk, and Compliance**"
    },
    {
        "question": "Which of the following should a security administrator adhere to when setting up a new set of firewall rules?",
        "options": [
            "Disaster recovery plan",
            "Incident response procedure",
            "Business continuity plan",
            "Change management procedure"
        ],
        "correct_answer": 4,
        "description": "Change management procedures ensure that all changes, including new firewall rules, are documented, reviewed, and approved before implementation.\n\n- Disaster recovery plan: Focuses on restoring systems after a failure.\n- Incident response procedure: Manages security incidents.\n- Business continuity plan: Ensures operations continue during disruptions.\n- Change management procedure: Ensures that all changes are documented, reviewed, and approved.\n\n**Domain 5: Governance, Risk, and Compliance**"
    },
    {
        "question": "A company is expanding its threat surface program and allowing individuals to security test the company’s internet-facing application. The company will compensate researchers based on the vulnerabilities discovered. Which of the following best describes the program the company is setting up?",
        "options": [
            "Open-source intelligence",
            "Bug bounty",
            "Red team",
            "Penetration testing"
        ],
        "correct_answer": 2,
        "description": "A bug bounty program rewards individuals who find and report security vulnerabilities in a company's applications.\n\n- Open-source intelligence: Gathering publicly available information.\n- Bug bounty: Rewards individuals for finding and reporting vulnerabilities.\n- Red team: Simulates real-world attacks to test security.\n- Penetration testing: Authorized attempts to exploit system vulnerabilities.\n\n**Domain 1: Attacks, Threats, and Vulnerabilities**"
    },
    {
        "question": "Which of the following threat actors is the most likely to use large financial resources to attack critical systems located in other countries?",
        "options": [
            "Insider",
            "Unskilled attacker",
            "Nation-state",
            "Hacktivist"
        ],
        "correct_answer": 3,
        "description": "Nation-state actors typically have significant resources and capabilities, allowing them to carry out sophisticated attacks on critical infrastructure in other countries.\n\n- Insider: An individual within the organization.\n- Unskilled attacker: Lacks advanced capabilities.\n- Nation-state: Well-resourced and capable of sophisticated attacks.\n- Hacktivist: Uses hacking to promote political or social agendas.\n\n**Domain 1: Attacks, Threats, and Vulnerabilities**"
    },
    {
        "question": "Which of the following enables the use of an input field to run commands that can view or manipulate data?",
        "options": [
            "Cross-site scripting",
            "Side loading",
            "Buffer overflow",
            "SQL injection"
        ],
        "correct_answer": 4,
        "description": "SQL injection is a common attack method that exploits vulnerabilities in an application's input fields to run arbitrary SQL commands.\n\n- Cross-site scripting (XSS): Involves injecting malicious scripts into web pages.\n- Side loading: Refers to installing unauthorized software.\n- Buffer overflow: Involves overrunning a buffer's boundary and overwriting adjacent memory.\n- SQL injection: Exploits vulnerabilities in input fields to run SQL commands.\n\n**Domain 1: Attacks, Threats, and Vulnerabilities**"
    },
    {
        "question": "Employees in the research and development business unit receive extensive training to ensure they understand how to best protect company data. Which of the following is the type of data these employees are most likely to use in day-to-day work activities?",
        "options": [
            "Encrypted",
            "Intellectual property",
            "Critical",
            "Data in transit"
        ],
        "correct_answer": 2,
        "description": "Intellectual property (IP) is a key asset in research and development, often representing proprietary technology or designs that require protection.\n\n- Encrypted: Data secured through encryption.\n- Intellectual property: Proprietary technology or designs requiring protection.\n- Critical: Essential data for business operations.\n- Data in transit: Data being transferred across networks.\n\n**Domain 5: Governance, Risk, and Compliance**"
    },
    {
        "question": "A company has begun labeling all laptops with asset inventory stickers and associating them with employee IDs. Which of the following security benefits do these actions provide? (Choose two.)",
        "options": [
            "If a security incident occurs on the device, the correct employee can be notified.",
            "The security team will be able to send user awareness training to the appropriate device.",
            "Users can be mapped to their devices when configuring software MFA tokens.",
            "User-based firewall policies can be correctly targeted to the appropriate laptops.",
            "When conducting penetration testing, the security team will be able to target the desired laptops.",
            "Company data can be accounted for when the employee leaves the organization."
        ],
        "correct_answer": [1, 6],
        "description": "Labeling laptops with asset inventory stickers helps in incident response by identifying the responsible employee and ensuring data is accounted for when employees leave the organization.\n\n- If a security incident occurs on the device, the correct employee can be notified: Correct, helps in incident response.\n- The security team will be able to send user awareness training to the appropriate device: Incorrect, not related to labeling laptops.\n- Users can be mapped to their devices when configuring software MFA tokens: Incorrect, not a primary benefit of labeling laptops.\n- User-based firewall policies can be correctly targeted to the appropriate laptops: Incorrect, more related to network configuration.\n- When conducting penetration testing, the security team will be able to target the desired laptops: Incorrect, labeling laptops doesn't directly relate to penetration testing.\n- Company data can be accounted for when the employee leaves the organization: Correct, helps in data management during employee exit.\n\n**Domain 5: Governance, Risk, and Compliance**"
    },
    {
        "question": "A technician wants to improve the situational and environmental awareness of existing users as they transition from remote to in-office work. Which of the following is the best option?",
        "options": [
            "Send out periodic security reminders.",
            "Update the content of new hire documentation.",
            "Modify the content of recurring training.",
            "Implement a phishing campaign."
        ],
        "correct_answer": 3,
        "description": "Updating the content of recurring training sessions ensures that users are informed about the latest security threats and best practices, particularly during transitions like returning to the office.\n\n- Send out periodic security reminders: Useful, but updating training content has a more significant impact.\n- Update the content of new hire documentation: Focuses on new employees, not existing users.\n- Modify the content of recurring training: Correct, keeps users informed about current threats and best practices.\n- Implement a phishing campaign: Helps in phishing awareness but doesn't address situational and environmental awareness comprehensively.\n\n**Domain 5: Governance, Risk, and Compliance**"
    },
    {
        "question": "A newly appointed board member with cybersecurity knowledge wants the board of directors to receive a quarterly report detailing the number of incidents that impacted the organization. The systems administrator is creating a way to present the data to the board of directors. Which of the following should the systems administrator use?",
        "options": [
            "Packet captures",
            "Vulnerability scans",
            "Metadata",
            "Dashboard"
        ],
        "correct_answer": 4,
        "description": "Dashboards provide a visual representation of data, making it easier to present and understand key metrics, such as the number of security incidents, to stakeholders like the board of directors.\n\n- Packet captures: Analyze network traffic, not suitable for presenting to the board.\n- Vulnerability scans: Identify weaknesses, but not for summarizing incidents.\n- Metadata: Provides information about data attributes, but not for incident reporting.\n- Dashboard: Correct, visual representation of data for easier understanding by the board.\n\n**Domain 5: Governance, Risk, and Compliance**"
    },
    {
        "question": "A systems administrator receives the following alert from a file integrity monitoring tool: The hash of the cmd.exe file has changed. The systems administrator checks the OS logs and notices that no patches were applied in the last two months. Which of the following most likely occurred?",
        "options": [
            "The end user changed the file permissions.",
            "A cryptographic collision was detected.",
            "A snapshot of the file system was taken.",
            "A rootkit was deployed."
        ],
        "correct_answer": 4,
        "description": "A rootkit modifies system files, including critical executables like cmd.exe, to hide its presence and maintain control over a compromised system.\n\n- The end user changed the file permissions: Unlikely, doesn't explain the hash change.\n- A cryptographic collision was detected: Unlikely, as hash collisions are rare and usually not associated with rootkit activity.\n- A snapshot of the file system was taken: Doesn't change file hashes.\n- A rootkit was deployed: Correct, modifies system files and explains the hash change.\n\n**Domain 1: Attacks, Threats, and Vulnerabilities**"
    },
    {
        "question": "Which of the following roles, according to the shared responsibility model, is responsible for securing the company’s database in an IaaS model for a cloud environment?",
        "options": [
            "Client",
            "Third-party vendor",
            "Cloud provider",
            "DBA"
        ],
        "correct_answer": 1,
        "description": "In the IaaS (Infrastructure as a Service) model, the client is responsible for securing their data and applications, including databases.\n\n- Client: Correct, responsible for securing data and applications in IaaS.\n- Third-party vendor: May provide services, but not responsible for database security in this context.\n- Cloud provider: Secures the underlying infrastructure but not the client's databases.\n- DBA (Database Administrator): Manages the database but security responsibility lies with the client.\n\n**Domain 5: Governance, Risk, and Compliance**"
    },
    {
        "question": "A client asked a security company to provide a document outlining the project, the cost, and the completion time frame. Which of the following documents should the company provide to the client?",
        "options": [
            "MSA",
            "SLA",
            "BPA",
            "SOW"
        ],
        "correct_answer": 4,
        "description": "A Statement of Work (SOW) outlines the project's scope, deliverables, timeline, and costs, serving as a formal agreement between the client and service provider.\n\n- MSA (Master Service Agreement): Defines general terms, not project-specific.\n- SLA (Service Level Agreement): Specifies performance expectations, not the overall project.\n- BPA (Business Partnership Agreement): Governs business relationships, not specific projects.\n- SOW (Statement of Work): Correct, outlines the project, cost, and completion time frame.\n\n**Domain 5: Governance, Risk, and Compliance**"
    },
    {
        "question": "A security team is reviewing the findings in a report that was delivered after a third party performed a penetration test. One of the findings indicated that a web application form field is vulnerable to cross-site scripting. Which of the following application security techniques should the security analyst recommend the developer implement to prevent this vulnerability?",
        "options": [
            "Secure cookies",
            "Version control",
            "Input validation",
            "Code signing"
        ],
        "correct_answer": 3,
        "description": "Input validation ensures that only properly formatted data is accepted by the application, preventing cross-site scripting (XSS) attacks.\n\n- Secure cookies: Enhance session security but do not prevent XSS.\n- Version control: Manages code changes, not directly related to preventing XSS.\n- Input validation: Correct, ensures only properly formatted data is accepted, preventing XSS.\n- Code signing: Ensures the integrity and authenticity of code, not related to XSS prevention.\n\n**Domain 3: Implementation**"
    },
    {
        "question": "Which of the following must be considered when designing a high-availability network? (Choose two).",
        "options": [
            "Ease of recovery",
            "Ability to patch",
            "Physical isolation",
            "Responsiveness",
            "Attack surface",
            "Extensible authentication"
        ],
        "correct_answer": [1, 4],
        "description": "High-availability networks should be designed for ease of recovery and responsiveness to ensure that they can quickly recover from failures and maintain performance.\n\n- Ease of recovery: Correct, ensures the network can quickly recover from failures.\n- Ability to patch: Important but not directly related to high availability.\n- Physical isolation: Reduces the risk of security breaches, but not specifically about availability.\n- Responsiveness: Correct, ensures the network can maintain performance during failures.\n- Attack surface: Important for security but not directly related to high availability.\n- Extensible authentication: Supports scalable access control but not specifically related to availability.\n\n**Domain 2: Architecture and Design**"
    },
    {
        "question": "A technician recently performed a remote installation of new software on multiple servers. The software has a known vulnerability, and the vendor has provided a hotfix to address the issue. Which of the following deployment techniques should be used to deploy the hotfix?",
        "options": [
            "Phased deployment",
            "Vulnerability assessment",
            "Patch management",
            "Change control"
        ],
        "correct_answer": 3,
        "description": "Patch management is the process of managing updates and fixes for software vulnerabilities, including deploying hotfixes to address known issues.\n\n- Phased deployment: Introduces changes gradually.\n- Vulnerability assessment: Identifies vulnerabilities but doesn't fix them.\n- Patch management: Correct, involves deploying updates and fixes for software vulnerabilities.\n- Change control: Manages changes in an IT environment but doesn't specifically address hotfix deployment.\n\n**Domain 3: Implementation**"
    },
    {
        "question": "A security analyst needs to configure encryption for company devices and wants to avoid a single point of failure. Which of the following should the analyst implement?",
        "options": [
            "SSH key",
            "TPM",
            "BitLocker",
            "RAID"
        ],
        "correct_answer": 2,
        "description": "A TPM (Trusted Platform Module) is a hardware-based encryption technology that stores cryptographic keys securely, reducing the risk of a single point of failure in encryption.\n\n- SSH key: Used for secure access but not related to avoiding single points of failure.\n- TPM: Correct, stores cryptographic keys securely, reducing the risk of a single point of failure.\n- BitLocker: Encrypts data on Windows devices, but depends on TPM for secure key storage.\n- RAID: Provides data redundancy but not related to encryption.\n\n**Domain 3: Implementation**"
    },





        {
            "question": "A technician needs to apply a high-priority patch to a production system. Which of the following steps should be taken first?",
            "options": [
                "Air gap the system.",
                "Move the system to a different network segment.",
                "Create a change control request.",
                "Apply the patch to the system."
            ],
            "correct_answer": 3,
            "description": "Before making significant changes to a production system, such as applying a high-priority patch, a change control request should be submitted to ensure that the change is documented and approved. \n- Air gapping isolates the system from the network. \n- Moving to a different segment separates the system for security. \n- Applying the patch addresses vulnerabilities.\n\n**Domain 5: Governance, Risk, and Compliance**"
        },
        {
            "question": "Which of the following describes the reason root cause analysis should be conducted as part of incident response?",
            "options": [
                "To gather IoCs for the investigation",
                "To discover which systems have been affected",
                "To eradicate any trace of malware on the network",
                "To prevent future incidents of the same nature"
            ],
            "correct_answer": 4,
            "description": "Root cause analysis helps identify the underlying cause of an incident, enabling organizations to implement measures that prevent similar incidents in the future. \n- IoCs (Indicators of Compromise) help detect threats. \n- Discovering affected systems identifies the scope of impact. \n- Eradicating malware ensures the network is clean.\n\n**Domain 4: Operations and Incident Response**"
        },
        {
            "question": "Which of the following is the most likely outcome if a large bank fails an internal PCI DSS compliance assessment?",
            "options": [
                "Fines",
                "Audit findings",
                "Sanctions",
                "Reputation damage"
            ],
            "correct_answer": 2,
            "description": "Audit findings (Company mistakes will stay inside the company) As an example, you work in a company and you made a mistakes that will lose your job. Are you going to tell them or are you just going to keep it to yourself? Its kinda same scenario as the question. \n- Audit findings document non-compliance. \n- Sanctions may be imposed for violations. \n- Reputation damage results from public disclosure of non-compliance.\n\n**Domain 5: Governance, Risk, and Compliance**"
        },
        {
            "question": "A company is developing a business continuity strategy and needs to determine how many staff members would be required to sustain the business in the case of a disruption. Which of the following best describes this step?",
            "options": [
                "Capacity planning",
                "Redundancy",
                "Geographic dispersion",
                "Tabletop exercise"
            ],
            "correct_answer": 1,
            "description": "Capacity planning involves determining the resources, including staff, needed to maintain operations during a disruption, ensuring business continuity. \n- Redundancy provides backup resources. \n- Geographic dispersion reduces risk by spreading resources across locations. \n- Tabletop exercises simulate disaster scenarios.\n\n**Domain 5: Governance, Risk, and Compliance**"
        },
        {
            "question": "A company’s legal department drafted sensitive documents in a SaaS application and wants to ensure the documents cannot be accessed by individuals in high-risk countries. Which of the following is the most effective way to limit this access?",
            "options": [
                "Data masking",
                "Encryption",
                "Geolocation policy",
                "Data sovereignty regulation"
            ],
            "correct_answer": 3,
            "description": "Implementing a geolocation policy can restrict access to sensitive documents based on the user's geographic location, protecting them from high-risk countries. \n- Data masking obscures sensitive information. \n- Encryption secures data in transit and at rest. \n- Data sovereignty regulation ensures compliance with local laws.\n\n**Domain 5: Governance, Risk, and Compliance**"
        },




        {
            "question": "Which of the following is a hardware-specific vulnerability?",
            "options": [
                "Firmware version",
                "Buffer overflow",
                "SQL injection",
                "Cross-site scripting"
            ],
            "correct_answer": 1,
            "description": "Hardware-specific vulnerabilities often stem from outdated or compromised firmware versions, which can expose devices to security risks. \n- Buffer overflow and SQL injection are software vulnerabilities. \n- Cross-site scripting (XSS) involves injecting malicious scripts into web pages.\n\n**Domain 1: Attacks, Threats, and Vulnerabilities**"
        },
        {
            "question": "While troubleshooting a firewall configuration, a technician determines that a 'deny any' policy should be added to the bottom of the ACL. The technician updates the policy, but the new policy causes several company servers to become unreachable. Which of the following actions would prevent this issue?",
            "options": [
                "Documenting the new policy in a change request and submitting the request to change management",
                "Testing the policy in a non-production environment before enabling the policy in the production network",
                "Disabling any intrusion prevention signatures on the 'deny any' policy prior to enabling the new policy",
                "Including an 'allow any' policy above the 'deny any' policy"
            ],
            "correct_answer": 2,
            "description": "Testing the policy in a non-production environment ensures that any issues, such as making company servers unreachable, are identified and resolved before deploying the policy in the production network. \n- Change management documents changes. \n- Disabling signatures on 'deny any' could bypass important security measures. \n- Including an 'allow any' policy could create security risks.\n\n**Domain 4: Operations and Incident Response**"
        },
        {
            "question": "An organization is building a new backup data center with cost-benefit as the primary requirement and RTO and RPO values around two days. Which of the following types of sites is the best for this scenario?",
            "options": [
                "Real-time recovery",
                "Hot",
                "Cold",
                "Warm"
            ],
            "correct_answer": 3,
            "description": "A cold site is a cost-effective solution for backup data centers when the RTO (Recovery Time Objective) and RPO (Recovery Point Objective) are around two days, as it does not have active IT infrastructure. \n- Hot sites are fully equipped and ready for immediate use. \n- Warm sites have partial infrastructure. \n- Real-time recovery involves immediate recovery of services.\n\n**Domain 5: Governance, Risk, and Compliance**"
        },
        {
            "question": "A company requires hard drives to be securely wiped before sending decommissioned systems to recycling. Which of the following best describes this policy?",
            "options": [
                "Enumeration",
                "Sanitization",
                "Destruction",
                "Inventory"
            ],
            "correct_answer": 2,
            "description": "Sanitization is the process of securely wiping data from hard drives and other media to ensure that the data cannot be recovered before the systems are sent for recycling. \n- Destruction involves physically destroying media. \n- Enumeration refers to identifying systems. \n- Inventory tracks assets.\n\n**Domain 3: Implementation**"
        },
        {
            "question": "A systems administrator works for a local hospital and needs to ensure patient data is protected and secure. Which of the following data classifications should be used to secure patient data?",
            "options": [
                "Private",
                "Critical",
                "Sensitive",
                "Public"
            ],
            "correct_answer": 3,
            "description": "Sensitive data classifications should be used to protect and secure patient data in compliance with regulations like HIPAA. \n- Private data is personal information. \n- Critical data is essential for business operations. \n- Public data is information that can be shared openly.\n\n**Domain 5: Governance, Risk, and Compliance**"
        },
        {
            "question": "A U.S.-based cloud-hosting provider wants to expand its data centers to new international locations. Which of the following should the hosting provider consider first?",
            "options": [
                "Local data protection regulations",
                "Risks from hackers residing in other countries",
                "Impacts to existing contractual obligations",
                "Time zone differences in log correlation"
            ],
            "correct_answer": 1,
            "description": "The hosting provider should first consider local data protection regulations in the new international locations to ensure compliance. \n- Risks from hackers and Impacts to contractual obligations are important but secondary considerations. \n- Time zone differences affect log correlation and monitoring.\n\n**Domain 5: Governance, Risk, and Compliance**"
        },
        {
            "question": "Which of the following would be the best way to block unknown programs from executing?",
            "options": [
                "Access control list",
                "Application allow list",
                "Host-based firewall",
                "DLP solution"
            ],
            "correct_answer": 2,
            "description": "An application allow list restricts the execution of unknown or unauthorized programs, ensuring only approved software can run. \n- An Access control list (ACL) controls network traffic. \n- A Host-based firewall monitors and controls traffic to and from a computer. \n- A DLP (Data Loss Prevention) solution prevents data leakage.\n\n**Domain 3: Implementation**"
        },
        {
            "question": "A company hired a consultant to perform an offensive security assessment covering penetration testing and social engineering. Which of the following teams will conduct this assessment activity?",
            "options": [
                "White",
                "Purple",
                "Blue",
                "Red"
            ],
            "correct_answer": 4,
            "description": "The Red Team conducts offensive security assessments, including penetration testing and social engineering. \n- The Blue Team focuses on defending against attacks. \n- The White Team monitors exercises. \n- The Purple Team integrates Red and Blue team activities.\n\n**Domain 1: Attacks, Threats, and Vulnerabilities**"
        },
        {
            "question": "A software development manager wants to ensure the authenticity of the code created by the company. Which of the following options is the most appropriate?",
            "options": [
                "Testing input validation on the user input fields",
                "Performing code signing on company-developed software",
                "Performing static code analysis on the software",
                "Ensuring secure cookies are used"
            ],
            "correct_answer": 2,
            "description": "Code signing ensures the authenticity and integrity of the code by using a digital signature. \n- Input validation ensures data is correctly formatted. \n- Static code analysis detects vulnerabilities in code without executing it. \n- Secure cookies protect session data.\n\n**Domain 3: Implementation**"
        },
        {
            "question": "Which of the following can be used to identify potential attacker activities without affecting production servers?",
            "options": [
                "Honeypot",
                "Video surveillance",
                "Zero Trust",
                "Geofencing"
            ],
            "correct_answer": 1,
            "description": "A honeypot is used to lure potential attackers and observe their activities without affecting production servers. \n- Video surveillance monitors physical premises. \n- Zero Trust is a security model that assumes no trust within the network. \n- Geofencing restricts access based on geographic location.\n\n**Domain 2: Architecture and Design**"
        },
        {
            "question": "During an investigation, an incident response team attempts to understand the source of an incident. Which of the following incident response activities describes this process?",
            "options": [
                "Analysis",
                "Lessons learned",
                "Detection",
                "Containment"
            ],
            "correct_answer": 1,
            "description": "Analysis is the process of understanding the source, cause, and impact of an incident during an investigation. \n- Detection involves identifying incidents. \n- Containment focuses on limiting the damage. \n- Lessons learned involve reviewing the response to improve future actions.\n\n**Domain 4: Operations and Incident Response**"
        },
        {
            "question": "A security practitioner completes a vulnerability assessment on a company’s network and finds several vulnerabilities, which the operations team remediates. Which of the following should be done next?",
            "options": [
                "Conduct an audit.",
                "Initiate a penetration test.",
                "Rescan the network.",
                "Submit a report."
            ],
            "correct_answer": 3,
            "description": "After remediation, the network should be rescanned to verify that the vulnerabilities have been successfully addressed. \n- Audits assess the effectiveness of security measures. \n- Penetration tests identify vulnerabilities by simulating attacks. \n- Reports document findings.\n\n**Domain 4: Operations and Incident Response**"
        },











        {
            "question": "An administrator was notified that a user logged in remotely after hours and copied large amounts of data to a personal device. Which of the following best describes the user’s activity?",
            "options": [
                "Penetration testing",
                "Phishing campaign",
                "External audit",
                "Insider threat"
            ],
            "correct_answer": 4,
            "description": "The user's activity is best described as an insider threat, where an authorized individual misuses access to data. \n- Penetration testing involves authorized attempts to exploit system vulnerabilities. \n- Phishing campaigns trick users into revealing information. \n- External audits review compliance and security practices.\n\n**Domain 1: Attacks, Threats, and Vulnerabilities**"
        },
        {
            "question": "Which of the following allows for the attribution of messages to individuals?",
            "options": [
                "Adaptive identity",
                "Non-repudiation",
                "Authentication",
                "Access logs"
            ],
            "correct_answer": 2,
            "description": "Non-repudiation ensures that a message or action cannot be denied by the individual who sent or performed it, allowing for attribution. \n- Authentication verifies the identity of a user. \n- Adaptive identity dynamically adjusts access controls. \n- Access logs record user activities.\n\n**Domain 3: Implementation**"
        },
        {
            "question": "Which of the following is the best way to consistently determine on a daily basis whether security settings on servers have been modified?",
            "options": [
                "Automation",
                "Compliance checklist",
                "Attestation",
                "Manual audit"
            ],
            "correct_answer": 1,
            "description": "Automation provides a consistent and reliable method to check whether security settings on servers have been modified daily. \n- Compliance checklists ensure adherence to policies. \n- Attestation confirms that security controls are in place. \n- Manual audits involve human review.\n\n**Domain 4: Operations and Incident Response**"
        },
        {
            "question": "Which of the following tools can assist with detecting an employee who has accidentally emailed a file containing a customer’s PII?",
            "options": [
                "SCAP",
                "NetFlow",
                "Antivirus",
                "DLP"
            ],
            "correct_answer": 4,
            "description": "A Data Loss Prevention (DLP) solution can help detect and prevent the unauthorized sharing of sensitive data such as PII (Personally Identifiable Information). \n- SCAP (Security Content Automation Protocol) automates vulnerability management. \n- NetFlow monitors network traffic. \n- Antivirus protects against malware.\n\n**Domain 4: Operations and Incident Response**"
        },
        {
            "question": "An organization recently updated its security policy to include the following statement: Regular expressions are included in source code to remove special characters such as $, |, ;. &, `, and ? from variables set by forms in a web application. Which of the following best explains the security technique the organization adopted by making this addition to the policy?",
            "options": [
                "Identify embedded keys",
                "Code debugging",
                "Input validation",
                "Static code analysis"
            ],
            "correct_answer": 3,
            "description": "Input validation ensures that user input is sanitized to prevent malicious data from being processed by the application. \n- Identifying embedded keys refers to securing hard-coded credentials. \n- Code debugging finds and fixes software bugs. \n- Static code analysis identifies vulnerabilities without executing code.\n\n**Domain 3: Implementation**"
        },
        {
            "question": "A security analyst and the management team are reviewing the organizational performance of a recent phishing campaign. The user click-through rate exceeded the acceptable risk threshold, and the management team wants to reduce the impact when a user clicks on a link in a phishing message. Which of the following should the analyst do?",
            "options": [
                "Place posters around the office to raise awareness of common phishing activities.",
                "Implement email security filters to prevent phishing emails from being delivered.",
                "Update the EDR policies to block automatic execution of downloaded programs.",
                "Create additional training for users to recognize the signs of phishing attempts."
            ],
            "correct_answer": 3,
            "description": "Updating EDR (Endpoint Detection and Response) policies to block the automatic execution of downloaded programs reduces the impact of users clicking on phishing links. \n- Email security filters prevent phishing emails from reaching users. \n- Training educates users on phishing. \n- Posters raise awareness.\n\n**Domain 4: Operations and Incident Response**"
        },
        {
            "question": "Which of the following has been implemented when a host-based firewall on a legacy Linux system allows connections from only specific internal IP addresses?",
            "options": [
                "Compensating control",
                "Network segmentation",
                "Transfer of risk",
                "SNMP traps"
            ],
            "correct_answer": 1,
            "description": "A compensating control is implemented to mitigate risks, such as allowing only specific internal IP addresses through a host-based firewall. \n- Network segmentation separates network traffic. \n- Transfer of risk involves shifting risk to another party. \n- SNMP traps alert on specific events in network management.\n\n**Domain 5: Governance, Risk, and Compliance**"
        },
        {
            "question": "The management team notices that new accounts that are set up manually do not always have correct access or permissions. Which of the following automation techniques should a systems administrator use to streamline account creation?",
            "options": [
                "Guard rail script",
                "Ticketing workflow",
                "Escalation script",
                "User provisioning script"
            ],
            "correct_answer": 4,
            "description": "A user provisioning script automates the process of account creation, ensuring that correct access and permissions are assigned. \n- Guard rail scripts enforce security boundaries. \n- Ticketing workflows manage support requests. \n- Escalation scripts trigger actions when certain conditions are met.\n\n**Domain 5: Governance, Risk, and Compliance**"
        },
        {
            "question": "A company is planning to set up a SIEM system and assign an analyst to review the logs on a weekly basis. Which of the following types of controls is the company setting up?",
            "options": [
                "Corrective",
                "Preventive",
                "Detective",
                "Deterrent"
            ],
            "correct_answer": 3,
            "description": "A detective control is set up to identify and alert on potential security incidents, such as the weekly review of SIEM (Security Information and Event Management) logs. \n- Corrective controls fix issues after they occur. \n- Preventive controls aim to stop incidents before they happen. \n- Deterrent controls discourage malicious activity.\n\n**Domain 5: Governance, Risk, and Compliance**"
        },
        {
            "question": "A systems administrator is looking for a low-cost application-hosting solution that is cloud-based. Which of the following meets these requirements?",
            "options": [
                "Serverless framework",
                "Type 1 hypervisor",
                "SD-WAN",
                "SDN"
            ],
            "correct_answer": 1,
            "description": "A serverless framework provides a low-cost, cloud-based solution for hosting applications without the need for managing server infrastructure. \n- A Type 1 hypervisor runs directly on hardware to manage virtual machines. \n- SD-WAN (Software-Defined Wide Area Network) optimizes network connections. \n- SDN (Software-Defined Networking) centralizes network management.\n\n**Domain 3: Implementation**"
        },
        {
            "question": "A security operations center determines that the malicious activity detected on a server is normal. Which of the following activities describes the act of ignoring detected activity in the future?",
            "options": [
                "Tuning",
                "Aggregating",
                "Quarantining",
                "Archiving"
            ],
            "correct_answer": 1,
            "description": "Tuning involves adjusting the security monitoring system to ignore or reduce alerts for known and acceptable activity. \n- Aggregating collects and consolidates data. \n- Quarantining isolates suspicious files or devices. \n- Archiving stores data for long-term retention.\n\n**Domain 4: Operations and Incident Response**"
        },
        {
            "question": "A security analyst reviews domain activity logs and notices the following:\n\nUserID jsmith, password authentication: succeeded, MFA: failed (invalid code)\nUserID jsmith, password authentication: succeeded, MFA: failed (invalid code)\nUserID jsmith, password authentication: succeeded, MFA: failed (invalid code)\nUserID jsmith, password authentication: succeeded, MFA: failed (invalid code)\n\nWhich of the following is the best explanation for what the security analyst has discovered?",
            "options": [
                "The user jsmith’s account has been locked out.",
                "A keylogger is installed on jsmith’s workstation.",
                "An attacker is attempting to brute force jsmith’s account.",
                "Ransomware has been deployed in the domain."
            ],
            "correct_answer": 3,
            "description": "The repeated successful password authentications followed by failed MFA attempts suggest that an attacker may be trying to brute-force jsmith's account. \n- A keylogger captures keystrokes. \n- Locking out an account prevents further access attempts. \n- Ransomware encrypts files for ransom.\n\n**Domain 1: Attacks, Threats, and Vulnerabilities**"
        },
        {
            "question": "A company is concerned about weather events causing damage to the server room and downtime. Which of the following should the company consider?",
            "options": [
                "Clustering servers",
                "Geographic dispersion",
                "Load balancers",
                "Off-site backups"
            ],
            "correct_answer": 2,
            "description": "Geographic dispersion of data centers helps mitigate the risk of weather-related damage by distributing resources across multiple locations. \n- Clustering servers groups them together for redundancy. \n- Load balancers distribute traffic across servers. \n- Off-site backups protect data in case of local disasters.\n\n**Domain 5: Governance, Risk, and Compliance**"
        },
        {
            "question": "Which of the following is a primary security concern for a company setting up a BYOD program?",
            "options": [
                "End of life",
                "Buffer overflow",
                "VM escape",
                "Jailbreaking"
            ],
            "correct_answer": 4,
            "description": "Jailbreaking is a primary security concern in a BYOD (Bring Your Own Device) program as it removes security controls and allows unauthorized apps to run on devices. \n- End of life refers to products no longer supported. \n- Buffer overflow involves memory vulnerabilities. \n- VM escape is a hypervisor vulnerability.\n\n**Domain 1: Attacks, Threats, and Vulnerabilities**"
        },
        {
            "question": "A company decided to reduce the cost of its annual cyber insurance policy by removing the coverage for ransomware attacks. Which of the following analysis elements did the company most likely use in making this decision?",
            "options": [
                "MTTR",
                "RTO",
                "ARO",
                "MTBF"
            ],
            "correct_answer": 3,
            "description": "ARO (Annualized Rate of Occurrence) likely influenced the company's decision to remove ransomware coverage to reduce insurance costs. \n- MTTR (Mean Time to Repair) measures recovery time. \n- RTO (Recovery Time Objective) defines acceptable downtime. \n- MTBF (Mean Time Between Failures) predicts the time between failures.\n\n**Domain 5: Governance, Risk, and Compliance**"
        },
        {
            "question": "Which of the following is the most likely to be included as an element of communication in a security awareness program?",
            "options": [
                "Reporting phishing attempts or other suspicious activities",
                "Detecting insider threats using anomalous behavior recognition",
                "Verifying information when modifying wire transfer data",
                "Performing social engineering as part of third-party penetration testing"
            ],
            "correct_answer": 1,
            "description": "Reporting phishing attempts and other suspicious activities is a key communication element in a security awareness program. \n- Detecting insider threats involves monitoring for unusual behavior. \n- Verifying information protects against fraud. \n- Social engineering tests employees' security awareness.\n\n**Domain 5: Governance, Risk, and Compliance**"
        },
        {
            "question": "Which of the following is the phase in the incident response process when a security analyst reviews roles and responsibilities?",
            "options": [
                "Preparation",
                "Recovery",
                "Lessons learned",
                "Analysis"
            ],
            "correct_answer": 1,
            "description": "The Preparation phase involves defining roles and responsibilities to ensure an effective incident response. \n- Recovery focuses on restoring systems. \n- Lessons learned involve reviewing the response to improve future actions. \n- Analysis investigates the cause and impact of an incident.\n\n**Domain 4: Operations and Incident Response**"
        },
        {
            "question": "After a recent vulnerability scan, a security engineer needs to harden the routers within the corporate network. Which of the following is the most appropriate to disable?",
            "options": [
                "Console access",
                "Routing protocols",
                "VLANs",
                "Web-based administration"
            ],
            "correct_answer": 4,
            "description": "Disabling web-based administration on routers helps reduce the attack surface and improve security. \n- Console access allows direct interaction with the router. \n- Routing protocols manage network routes. \n- VLANs (Virtual Local Area Networks) separate network traffic.\n\n**Domain 3: Implementation**"
        },
        {
            "question": "A security administrator needs a method to secure data in an environment that includes some form of checks to track any changes. Which of the following should the administrator set up to achieve this goal?",
            "options": [
                "SPF",
                "GPO",
                "NAC",
                "FIM"
            ],
            "correct_answer": 4,
            "description": "File Integrity Monitoring (FIM) tracks changes to files and provides a way to detect unauthorized modifications to data. \n- SPF (Sender Policy Framework) helps prevent email spoofing. \n- GPO (Group Policy Object) manages Windows environment configurations. \n- NAC (Network Access Control) controls network access.\n\n**Domain 3: Implementation**"
        },
        {
            "question": "An administrator is reviewing a single server's security logs and discovers the following:\n\nKeywords           Date and Time             Source                     Event ID     Task Category\n---------------------------------------------------------------------------------------------------\nAudit Failure      09/16/2022 11:13:05 AM    Microsoft Windows security 4625           Logon\nAudit Failure      09/16/2022 11:13:07 AM    Microsoft Windows security 4625           Logon\nAudit Failure      09/16/2022 11:13:09 AM    Microsoft Windows security 4625           Logon\nAudit Failure      09/16/2022 11:13:11 AM    Microsoft Windows security 4625           Logon\nAudit Failure      09/16/2022 11:13:13 AM    Microsoft Windows security 4625           Logon\nAudit Failure      09/16/2022 11:13:15 AM    Microsoft Windows security 4625           Logon\nAudit Failure      09/16/2022 11:13:17 AM    Microsoft Windows security 4625           Logon\nAudit Failure      09/16/2022 11:13:19 AM    Microsoft Windows security 4625           Logon\nAudit Failure      09/16/2022 11:13:21 AM    Microsoft Windows security 4625           Logon\nAudit Failure      09/16/2022 11:13:23 AM    Microsoft Windows security 4625           Logon\nAudit Failure      09/16/2022 11:13:25 AM    Microsoft Windows security 4625           Logon\nAudit Failure      09/16/2022 11:13:27 AM    Microsoft Windows security 4625           Logon\n\nWhich of the following best describes the action captured in this log file?",
            "options": [
                "Brute-force attack",
                "Privilege escalation",
                "Failed password audit",
                "Forgotten password by the user"
            ],
            "correct_answer": 1,
            "description": "The repeated failed logon attempts indicated by the 'Failure' keyword and Event ID 4625 suggest that a brute-force attack is occurring. \n- Privilege escalation involves gaining unauthorized access to higher-level permissions. \n- A Failed password audit refers to a review of password policies. \n- Forgotten password by the user is self-explanatory.\n\n**Domain 1: Attacks, Threats, and Vulnerabilities**"
        },
        {
            "question": "A security engineer is implementing FDE for all laptops in an organization. Which of the following are the most important for the engineer to consider as part of the planning process? (Choose two.)",
            "options": [
                "Key escrow",
                "TPM presence",
                "Digital signatures",
                "Data tokenization",
                "Public key management",
                "Certificate authority linking"
            ],
            "correct_answer": [1, 2],
            "description": "Key escrow and TPM (Trusted Platform Module) presence are critical considerations when planning to implement Full Disk Encryption (FDE) on laptops. \n- Key escrow involves securely storing encryption keys. \n- Digital signatures ensure data integrity. \n- Data tokenization replaces sensitive data with tokens. \n- Public key management handles encryption keys. \n- Certificate authority linking ties identities to encryption keys.\n\n**Domain 3: Implementation**"
        },
        {
            "question": "A security analyst scans a company's public network and discovers a host is running a remote desktop that can be used to access the production network. Which of the following changes should the security analyst recommend?",
            "options": [
                "Changing the remote desktop port to a non-standard number",
                "Setting up a VPN and placing the jump server inside the firewall",
                "Using a proxy for web connections from the remote desktop server",
                "Connecting the remote server to the domain and increasing the password length"
            ],
            "correct_answer": 2,
            "description": "Setting up a VPN (Virtual Private Network) and placing the jump server inside the firewall improves security by requiring secure, authenticated access to the network. \n- Changing the remote desktop port to a non-standard number may help avoid automated attacks. \n- A Proxy server controls web traffic. \n- Increasing password length enhances security.\n\n**Domain 2: Architecture and Design**"
        },
        {
            "question": "An enterprise has been experiencing attacks focused on exploiting vulnerabilities in older browser versions with well-known exploits. Which of the following security solutions should be configured to best provide the ability to monitor and block these known signature-based attacks?",
            "options": [
                "ACL",
                "DLP",
                "IDS",
                "IPS"
            ],
            "correct_answer": 4,
            "description": "An Intrusion Prevention System (IPS) can monitor network traffic and block signature-based attacks, such as those exploiting known vulnerabilities in browsers. \n- An Access Control List (ACL) controls network traffic. \n- Data Loss Prevention (DLP) prevents unauthorized data sharing. \n- Intrusion Detection Systems (IDS) detect but do not block attacks.\n\n**Domain 3: Implementation**"
        },
        {
            "question": "Security controls in a data center are being reviewed to ensure data is properly protected and that human life considerations are included. Which of the following best describes how the controls should be set up?",
            "options": [
                "Remote access points should fail closed.",
                "Logging controls should fail open.",
                "Safety controls should fail open.",
                "Logical security controls should fail closed."
            ],
            "correct_answer": 3,
            "description": "Safety controls in a data center should fail open to ensure that human life is not endangered in the event of a failure. Failing open means that in the case of a failure, the system defaults to an open state to allow for human safety, even if it compromises security temporarily.\n\n**Domain 5: Governance, Risk, and Compliance**"
        },
        {
            "question": "Which of the following would be best suited for constantly changing environments?",
            "options": [
                "RTOS",
                "Containers",
                "Embedded systems",
                "SCADA"
            ],
            "correct_answer": 2,
            "description": "Containers are well-suited for environments that are constantly changing because they allow for quick deployment and scalability. \n- RTOS (Real-Time Operating System) is designed for time-sensitive tasks. \n- Embedded systems are designed for specific functions. \n- SCADA (Supervisory Control and Data Acquisition) systems manage industrial processes.\n\n**Domain 2: Architecture and Design**"
        },
        {
            "question": "Which of the following incident response activities ensures evidence is properly handled?",
            "options": [
                "E-discovery",
                "Chain of custody",
                "Legal hold",
                "Preservation"
            ],
            "correct_answer": 2,
            "description": "Chain of custody ensures that evidence is properly documented and handled to maintain its integrity throughout the incident response process. \n- E-discovery involves identifying and collecting digital information for legal purposes. \n- Legal hold preserves relevant information for litigation. \n- Preservation involves maintaining the integrity of evidence.\n\n**Domain 4: Operations and Incident Response**"
        },
        {
            "question": "An accounting clerk sent money to an attacker's bank account after receiving fraudulent instructions to use a new account. Which of the following would most likely prevent this activity in the future?",
            "options": [
                "Standardizing security incident reporting",
                "Executing regular phishing campaigns",
                "Implementing insider threat detection measures",
                "Updating processes for sending wire transfers"
            ],
            "correct_answer": 4,
            "description": "Updating processes for sending wire transfers, such as implementing verification steps, can help prevent fraudulent transactions. \n- Standardizing incident reporting ensures consistent responses. \n- Phishing campaigns educate employees on recognizing fraud. \n- Insider threat detection monitors for suspicious activities.\n\n**Domain 5: Governance, Risk, and Compliance**"
        },
        {
            "question": "A systems administrator is creating a script that would save time and prevent human error when performing account creation for a large number of end users. Which of the following would be a good use case for this task?",
            "options": [
                "Off-the-shelf software",
                "Orchestration",
                "Baseline",
                "Policy enforcement"
            ],
            "correct_answer": 2,
            "description": "Orchestration involves automating complex IT tasks, such as account creation, to save time and reduce the risk of human error. \n- Off-the-shelf software refers to ready-made applications. \n- Baselines establish standards for system configuration. \n- Policy enforcement ensures compliance with security policies.\n\n**Domain 5: Governance, Risk, and Compliance**"
        },
        {
            "question": "A company's marketing department collects, modifies, and stores sensitive customer data. The infrastructure team is responsible for securing the data while in transit and at rest. Which of the following data roles describes the customer?",
            "options": [
                "Processor",
                "Custodian",
                "Subject",
                "Owner"
            ],
            "correct_answer": 3,
            "description": "The customer is the data subject, as they are the individuals to whom the sensitive data relates. The data subject is the person whose personal data is being collected, stored, or processed.\n\n**Domain 5: Governance, Risk, and Compliance**"
        },
        {
            "question": "Which of the following describes the maximum allowance of accepted risk?",
            "options": [
                "Risk indicator",
                "Risk level",
                "Risk score",
                "Risk threshold"
            ],
            "correct_answer": 4,
            "description": "Risk threshold refers to the maximum level of risk that an organization is willing to accept before it must take action to reduce it. It defines the point at which a risk becomes unacceptable and triggers risk mitigation strategies.\n\n**Domain 5: Governance, Risk, and Compliance**"
        },
        {
            "question": "A security analyst receives alerts about an internal system sending a large amount of unusual DNS queries to systems on the internet over short periods of time during non-business hours. Which of the following is most likely occurring?",
            "options": [
                "A worm is propagating across the network.",
                "Data is being exfiltrated.",
                "A logic bomb is deleting data.",
                "Ransomware is encrypting files."
            ],
            "correct_answer": 2,
            "description": "Unusual DNS queries during non-business hours could indicate that data is being exfiltrated from the network. Attackers may use DNS to covertly transmit data out of the network to avoid detection by traditional security controls.\n\n**Domain 1: Attacks, Threats, and Vulnerabilities**"
        },
        {
            "question": "A technician is opening ports on a firewall for a new system being deployed and supported by a SaaS provider. Which of the following is a risk in the new system?",
            "options": [
                "Default credentials",
                "Non-segmented network",
                "Supply chain vendor",
                "Vulnerable software"
            ],
            "correct_answer": 3,
            "description": "Supply chain risks arise when a third-party vendor is involved in the deployment and maintenance of a system, potentially introducing vulnerabilities. Ensuring that the vendor follows security best practices is essential to mitigating these risks.\n\n**Domain 2: Architecture and Design**"
        },
        {
            "question": "A systems administrator is working on a solution with the following requirements:\n• Provide a secure zone.\n• Enforce a company-wide access control policy.\n• Reduce the scope of threats.\nWhich of the following is the systems administrator setting up?",
            "options": [
                "Zero Trust",
                "AAA",
                "Non-repudiation",
                "CIA"
            ],
            "correct_answer": 1,
            "description": "Zero Trust is a security model that ensures strict access control and reduces the scope of threats by assuming no trust within the network. Every access request is treated as though it originates from an open network, regardless of its origin.\n\n**Domain 2: Architecture and Design**"
        },
        {
            "question": "Which of the following involves an attempt to take advantage of database misconfigurations?",
            "options": [
                "Buffer overflow",
                "SQL injection",
                "VM escape",
                "Memory injection"
            ],
            "correct_answer": 2,
            "description": "SQL injection attacks exploit vulnerabilities in database configurations to execute malicious SQL code. These attacks can lead to unauthorized access to or manipulation of the database.\n\n**Domain 1: Attacks, Threats, and Vulnerabilities**"
        },
        {
            "question": "Which of the following is used to validate a certificate when it is presented to a user?",
            "options": [
                "OCSP",
                "CSR",
                "CA",
                "CRC"
            ],
            "correct_answer": 1,
            "description": "OCSP (Online Certificate Status Protocol) is used to validate the status of a digital certificate when it is presented. It ensures that the certificate is still valid and has not been revoked.\n\n**Domain 3: Implementation**"
        },
        {
            "question": "One of a company's vendors sent an analyst a security bulletin that recommends a BIOS update. Which of the following vulnerability types is being addressed by the patch?",
            "options": [
                "Virtualization",
                "Firmware",
                "Application",
                "Operating system"
            ],
            "correct_answer": 2,
            "description": "The BIOS is firmware, so a patch that updates the BIOS addresses vulnerabilities at the firmware level. Firmware vulnerabilities can compromise the underlying hardware's security.\n\n**Domain 3: Implementation**"
        },
        {
            "question": "Which of the following is used to quantitatively measure the criticality of a vulnerability?",
            "options": [
                "CVE",
                "CVSS",
                "CIA",
                "CERT"
            ],
            "correct_answer": 2,
            "description": "CVSS (Common Vulnerability Scoring System) is used to measure and score the criticality of vulnerabilities. It provides a way to prioritize vulnerabilities based on their potential impact.\n\n**Domain 1: Attacks, Threats, and Vulnerabilities**"
        },
        {
            "question": "Which of the following actions could a security engineer take to ensure workstations and servers are properly monitored for unauthorized changes and software?",
            "options": [
                "Configure all systems to log scheduled tasks.",
                "Collect and monitor all traffic exiting the network.",
                "Block traffic based on known malicious signatures.",
                "Install endpoint management software on all systems"
            ],
            "correct_answer": 4,
            "description": "Installing endpoint management software helps ensure that workstations and servers are monitored for unauthorized changes and software. This software can detect and alert administrators to any unauthorized modifications.\n\n**Domain 4: Operations and Incident Response**"
        },
        {
            "question": "An organization is leveraging a VPN between its headquarters and a branch location. Which of the following is the VPN protecting?",
            "options": [
                "Data in use",
                "Data in transit",
                "Geographic restrictions",
                "Data sovereignty"
            ],
            "correct_answer": 2,
            "description": "A VPN protects data in transit by encrypting it as it travels between the headquarters and branch location. This ensures that the data cannot be intercepted and read by unauthorized parties during transmission.\n\n**Domain 2: Architecture and Design**"
        }

]

