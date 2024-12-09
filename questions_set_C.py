questions_set_C = [
# 401-450



  {
    "question": "A switch is connected to another switch. Incompatible hardware causes a surge in traffic on both switches. Which of the following configurations will cause traffic to pause, allowing the switches to drain buffers?",
    "options": [
      "Speed",
      "Flow control",
      "802.1Q",
      "Duplex"
    ],
    "correct_answer": 2,
    "description": "The correct answer is Flow control. Flow control helps manage the rate of data transmission between devices to prevent packet loss and congestion. It pauses traffic to allow switches to drain buffers. \n\n- Speed and Duplex configurations may impact connectivity but do not directly manage congestion. \n- 802.1Q is a standard for VLAN tagging and does not address traffic flow management."
  },
  {
    "question": "Which of the following records can be used to track the number of changes on a DNS zone?",
    "options": [
      "SOA",
      "SRV",
      "PTR",
      "NS"
    ],
    "correct_answer": 1,
    "description": "The correct answer is SOA (Start of Authority). The SOA record contains information about the DNS zone, including the serial number, which can be used to track changes. \n\n- SRV, PTR, and NS records are used for specific network services and domain name resolutions but do not track DNS zone changes."
  },
  {
    "question": "A network administrator is investigating a performance issue on a dual-link connection — VPN and MPLS — to a partner network. The MPLS is the primary path, and the VPN is used as a backup. While communicating, the delay is measured at 18ms, which is higher than the 6ms expected when the MPLS link is operational but lower than the 30ms expected for the VPN connection. Which of the following will MOST likely point to the root cause of the issue?",
    "options": [
      "Checking the routing tables on both sides to ensure there is no asymmetric routing",
      "Checking on the partner network for a missing route pointing to the VPN connection",
      "Running iPerf on both sides to confirm the delay that is measured is accurate",
      "Checking for an incorrect VLAN assignment affecting the MPLS traffic"
    ],
    "correct_answer": 1,
    "description": "The correct answer is checking the routing tables to ensure there is no asymmetric routing. Asymmetric routing occurs when traffic takes different paths in each direction, which could cause delays or performance issues. \n\n- A missing route to the VPN connection may cause delays, but it's less likely than routing issues. \n- Running iPerf can be useful for measuring delay but may not directly identify the cause of the delay. \n- VLAN misconfigurations usually cause other issues but are less likely to explain the performance drop in this case."
  },
  {
    "question": "Which of the following is a requirement when certifying a network cabling as Cat 7?",
    "options": [
      "Ensure the patch panel is certified for the same category.",
      "Limit 10Gb transmissions to 180ft (55m).",
      "Use F-type connectors on the network terminations.",
      "Ensure the termination standard is TIA/EIA-568-A."
    ],
    "correct_answer": 1,
    "description": "The correct answer is ensuring the patch panel is certified for the same category. To maintain Cat 7 standards, both the cables and the associated hardware (like patch panels) must meet the same specifications. \n\n- 10Gb transmissions are typically supported by Cat 6a or higher cables, and distance limitations may vary. \n- F-type connectors are not used for Cat 7 cables; they use RJ45 connectors. \n- TIA/EIA-568-A is a standard for wiring but not specifically tied to Cat 7 certification."
  },
  {
    "question": "Which of the following architectures is used for FTP?",
    "options": [
      "Client-server",
      "Service-oriented",
      "Connection-oriented",
      "Data-centric"
    ],
    "correct_answer": 1,
    "description": "The correct answer is client-server. FTP (File Transfer Protocol) operates on a client-server architecture, where the client requests files from the server. \n\n- Service-oriented architecture (SOA) is used for building software systems with reusable services, which is not relevant to FTP. \n- Connection-oriented refers to protocols like TCP, but it doesn't describe FTP architecture. \n- Data-centric focuses on data management systems and doesn't relate to FTP architecture."
  },
  {
    "question": "Which of the following bandwidth management techniques uses buffers at the client side to prevent TCP retransmissions from occurring when the ISP starts to drop packets of specific types that exceed the agreed traffic rate?",
    "options": [
      "Traffic shaping",
      "Traffic policing",
      "Traffic marking",
      "Traffic prioritization"
    ],
    "correct_answer": 1,
    "description": "The correct answer is traffic shaping. Traffic shaping controls the flow of traffic to prevent network congestion by using buffers to delay excess traffic and avoid retransmissions. \n\n- Traffic policing is about enforcing limits on traffic, but it doesn't buffer packets like shaping does. \n- Traffic marking refers to tagging packets for quality of service (QoS), not managing traffic flow. \n- Traffic prioritization ensures important traffic gets through but doesn't prevent retransmissions caused by congestion."
  },
  {
    "question": "An engineer needs to verify the external record for SMTP traffic. The engineer logged in to the server and entered the nslookup command. Which of the following commands should the engineer send before entering the DNS name?",
    "options": [
      "set type=A",
      "ls -d company.mail.com",
      "set domain=company.mail.com",
      "set querytype=MX"
    ],
    "correct_answer": 4,
    "description": "The correct answer is 'set querytype=MX'. To verify the external record for SMTP traffic, the engineer needs to check the MX (Mail Exchange) record, which handles email routing. \n\n- 'set type=A' looks up A records (IP addresses), not MX records. \n- 'ls -d' lists domain information but is not relevant to checking MX records. \n- 'set domain' sets the domain but doesn't directly query for MX records."
  },
  {
    "question": "A security engineer is trying to determine whether an internal server was accessed by hosts on the internet. The internal server was shut down during the investigation. Which of the following will the engineer review to determine whether the internal server had an unauthorized access attempt?",
    "options": [
      "The ARP table",
      "The NetFlow statistics",
      "The firewall logs",
      "The audit logs on the core switch"
    ],
    "correct_answer": 3,
    "description": "The correct answer is the firewall logs. Firewall logs can provide detailed records of traffic entering and leaving the network, including any unauthorized access attempts to the internal server. \n\n- The ARP table shows IP-to-MAC address mappings and is less likely to provide information about unauthorized access attempts. \n- NetFlow statistics track flow data but may not give a clear picture of unauthorized access. \n- Audit logs on the core switch may provide some information, but firewall logs are more directly related to access attempts."
  },
  {
    "question": "A company is reviewing ways to cut the overall cost of its IT budget. A network technician suggests removing various computer programs from the IT budget and only providing these programs on an as-needed basis. Which of the following models would meet this requirement?",
    "options": [
      "Multitenancy",
      "IaaS",
      "SaaS",
      "VPN"
    ],
    "correct_answer": 3,
    "description": "The correct answer is SaaS (Software as a Service). SaaS allows businesses to provide software on a subscription or on-demand basis, reducing the need for large upfront investments and only paying for what is needed. \n\n- Multitenancy refers to an architecture where a single instance of software serves multiple customers, but it doesn't directly address on-demand provisioning of software. \n- IaaS (Infrastructure as a Service) provides virtualized computing resources, not software applications. \n- VPN is a secure network connection, not a software delivery model."
  },
  {
    "question": "An IP address is maintained despite a failing UPS that causes a workstation to restart several times. Which of the following would allow this to occur?",
    "options": [
      "DHCP reservation",
      "DHCP scope",
      "Name server",
      "Root DNS server"
    ],
    "correct_answer": 1,
    "description": "The correct answer is DHCP reservation. DHCP reservations ensure that a specific IP address is always assigned to a particular device, even if the workstation restarts or experiences other issues. \n\n- DHCP scope defines the range of IP addresses that can be assigned but does not guarantee a specific IP address to a device. \n- Name servers and root DNS servers are related to domain name resolution, not IP address assignment."
  },



    {
        "question": "A network administrator wants to control new router deployments via the use of application programming interfaces (APIs). This would be an example of:",
        "options": [
            "Software-defined networking.",
            "A three-tiered architecture.",
            "Collapsed backbone.",
            "Top-of-rack switching."
        ],
        "correct_answer": 1,
        "description": "The correct answer is software-defined networking. APIs enable network administrators to programmatically manage and control networking devices, which is a hallmark of SDN. \n\n- A three-tiered architecture describes a logical network structure, not API control. \n- Collapsed backbone refers to a network topology, not automation. \n- Top-of-rack switching pertains to physical switch placement in a data center."
    },
    {
        "question": "A technician is equipped with a tablet, a smartphone, and a laptop to troubleshoot a switch with the help of support over the phone. However, the technician is having issues interconnecting all these tools in troubleshooting the switch. Which of the following should the technician use to gain connectivity?",
        "options": [
            "PAN",
            "WAN",
            "LAN",
            "MAN"
        ],
        "correct_answer": 1,
        "description": "The correct answer is PAN (Personal Area Network). This allows devices in close proximity to interconnect wirelessly, enabling seamless troubleshooting. \n\n- WAN (Wide Area Network) is for long-distance networking, not personal device connections. \n- LAN (Local Area Network) connects devices within a single location but requires infrastructure. \n- MAN (Metropolitan Area Network) covers citywide networks and is not relevant to this scenario."
    },
    {
        "question": "Users within a corporate network need to connect to the internet, but corporate network policy does not allow direct connections. Which of the following is MOST likely to be used?",
        "options": [
            "Proxy server.",
            "VPN client.",
            "Bridge.",
            "VLAN."
        ],
        "correct_answer": 1,
        "description": "The correct answer is proxy server. This acts as an intermediary between users and the internet, enforcing corporate policies. \n\n- VPN client secures communication but does not mediate internet access. \n- A bridge connects network segments and is unrelated to internet access policies. \n- VLAN organizes networks but does not provide controlled internet access."
    },
    {
        "question": "A network is secured and is only accessible via TLS and IPSec VPNs. Which of the following would need to be present to allow a user to access network resources on a laptop without logging in to the VPN application?",
        "options": [
            "Site-to-site.",
            "Secure Shell.",
            "In-band management.",
            "Remote desktop connection."
        ],
        "correct_answer": 1,
        "description": "The correct answer is site-to-site. This configuration connects networks directly and securely without requiring a user to log in to a VPN. \n\n- Secure Shell provides command-line access but does not enable seamless resource access. \n- In-band management refers to managing devices over the same network, not user access. \n- Remote desktop connection enables control of a device but is not a network access solution."
    },
    {
        "question": "A technician is checking network devices to look for opportunities to improve security. Which of the following tools would BEST accomplish this task?",
        "options": [
            "Wi-Fi analyzer.",
            "Protocol analyzer.",
            "Nmap.",
            "IP scanner."
        ],
        "correct_answer": 3,
        "description": "The correct answer is Nmap. It identifies open ports and services, highlighting potential vulnerabilities. \n\n- Wi-Fi analyzer focuses on wireless networks and signal optimization. \n- Protocol analyzer monitors and decodes network traffic but does not scan devices. \n- IP scanner identifies connected devices but lacks in-depth vulnerability analysis."
    },
    {
        "question": "Which of the following describes when an active exploit is used to gain access to a network?",
        "options": [
            "Penetration testing.",
            "Vulnerability testing.",
            "Risk assessment.",
            "Posture assessment.",
            "Baseline testing."
        ],
        "correct_answer": 1,
        "description": "The correct answer is penetration testing. This involves simulating attacks using active exploits to identify weaknesses. \n\n- Vulnerability testing identifies vulnerabilities without exploiting them. \n- Risk assessment evaluates potential risks, not active exploits. \n- Posture assessment reviews the overall security state but does not simulate attacks. \n- Baseline testing compares current systems to a standard, unrelated to exploits."
    },
    {
        "question": "A homeowner frequently has guests visit and would like to install a wireless router for their personal devices. The homeowner wants to ensure that the wireless router is compatible with the widest range of devices possible. Which of the following standards should a technician suggest?",
        "options": [
            "802.11ac.",
            "802.11b.",
            "802.11g.",
            "802.11n."
        ],
        "correct_answer": 4,
        "description": "The correct answer is 802.11n. This standard supports backward compatibility with 802.11a/b/g devices and provides decent speeds for modern use. \n\n- 802.11ac offers faster speeds but lacks broad backward compatibility. \n- 802.11b and 802.11g are outdated and do not support modern devices effectively."
    },
    {
        "question": "A GRE tunnel has been configured between two remote sites. Which of the following features, when configured, ensures the GRE overhead does not affect payload?",
        "options": [
            "Jumbo frames.",
            "Auto medium-dependent interface.",
            "Interface crossover.",
            "Collision detection."
        ],
        "correct_answer": 1,
        "description": "The correct answer is jumbo frames. These allow larger packets to be transmitted, minimizing the impact of GRE overhead on payload. \n\n- Auto medium-dependent interface simplifies cable requirements but does not address payload size. \n- Interface crossover refers to physical cabling and is irrelevant to GRE tunnels. \n- Collision detection prevents data collisions but is unrelated to GRE payload handling."
    },
    {
        "question": "Which of the following attacks MOST likely utilizes a botnet to disrupt traffic?",
        "options": [
            "DDoS.",
            "Deauthentication.",
            "Social engineering.",
            "Ransomware.",
            "DNS poisoning."
        ],
        "correct_answer": 1,
        "description": "The correct answer is DDoS. Distributed Denial-of-Service attacks use botnets to flood a network, disrupting traffic. \n\n- Deauthentication attacks target Wi-Fi clients but do not require botnets. \n- Social engineering manipulates individuals and does not involve network traffic disruption. \n- Ransomware encrypts files and is unrelated to traffic disruption. \n- DNS poisoning redirects traffic but does not disrupt it using botnets."
    },
    {
        "question": "A network administrator is looking at switch features and is unsure whether to purchase a model with PoE. Which of the following devices that commonly utilize PoE should the administrator consider? (Choose two.)",
        "options": [
            "VoIP phones.",
            "Cameras.",
            "Printers.",
            "Cable modems.",
            "Laptops.",
            "UPSs."
        ],
        "correct_answer": [1, 2],
        "description": "The correct answers are VoIP phones and cameras. These devices commonly utilize Power over Ethernet (PoE) to receive both data and power through a single cable. \n\n- Printers, laptops, and UPSs do not typically use PoE. \n- Cable modems require a direct power source."
    },



    {
        "question": "All packets arriving at an interface need to be fully analyzed. Which of the following features should be used to enable monitoring of the packets?",
        "options": [
            "LACP",
            "Flow control",
            "Port mirroring",
            "NetFlow exporter"
        ],
        "correct_answer": 3,
        "description": "The correct answer is Port mirroring. Port mirroring duplicates traffic from one or more ports on a switch to another port where it can be analyzed by a monitoring tool. \n\n- LACP is used for link aggregation and does not provide packet monitoring capabilities. \n- Flow control manages the rate of data transfer to prevent congestion but does not monitor packets. \n- NetFlow exporter collects and exports flow data, but it is not intended for real-time packet analysis."
    },
    {
        "question": "Which of the following record types would be used to define where SIP is found?",
        "options": [
            "SRV",
            "CNAME",
            "A",
            "MX"
        ],
        "correct_answer": 1,
        "description": "The correct answer is SRV. SRV records specify services and their locations, such as SIP servers, to enable clients to connect to the appropriate resources. \n\n- CNAME is used to create an alias for another DNS record, not for locating services. \n- A records map domain names to IP addresses, which is unrelated to SIP services. \n- MX records are specific to email routing and do not relate to SIP."
    },
    {
        "question": "Which of the following is an advanced distance vector routing protocol that automates routing tables and also uses some features of link-state routing protocols?",
        "options": [
            "OSPF",
            "RIP",
            "EIGRP",
            "BGP"
        ],
        "correct_answer": 3,
        "description": "The correct answer is EIGRP. EIGRP is a hybrid protocol that combines features of distance vector and link-state protocols, offering fast convergence and efficient routing table management. \n\n- OSPF is a pure link-state protocol. \n- RIP is a basic distance vector protocol with limited scalability. \n- BGP is used for inter-domain routing and is neither distance vector nor link-state."
    },
    {
        "question": "A network resource was accessed by an outsider as a result of a successful phishing campaign. Which of the following strategies should be employed to mitigate the effects of phishing?",
        "options": [
            "Multifactor authentication",
            "Single sign-on",
            "RADIUS",
            "VPN"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Multifactor authentication. By requiring multiple forms of verification, MFA makes it significantly harder for attackers to gain unauthorized access even with stolen credentials. \n\n- Single sign-on simplifies user authentication but does not enhance security against phishing. \n- RADIUS provides centralized authentication but is not a strategy for phishing mitigation. \n- VPN secures connections but does not prevent unauthorized access from phishing attacks."
    },
    {
        "question": "A PC user who is on a local network reports very slow speeds when accessing files on the network server. The user's PC is connecting, but file downloads are very slow when compared to other users' download speeds. The PC's NIC should be capable of Gigabit Ethernet. Which of the following will MOST likely fix the issue?",
        "options": [
            "Releasing and renewing the PC's IP address",
            "Replacing the patch cable",
            "Reseating the NIC inside the PC",
            "Flushing the DNS cache"
        ],
        "correct_answer": 2,
        "description": "The correct answer is Replacing the patch cable. A faulty or lower-quality cable can degrade network performance, even if the NIC supports higher speeds. \n\n- Releasing and renewing the IP address does not address physical layer issues. \n- Reseating the NIC is unlikely to fix cable-related problems. \n- Flushing the DNS cache does not resolve slow file transfers."
    },
    {
        "question": "A network administrator is configuring logging on an edge switch. The requirements are to log each time a switch port goes up or down. Which of the following logging levels will provide this information?",
        "options": [
            "Warnings",
            "Notifications",
            "Alert",
            "Errors"
        ],
        "correct_answer": 2,
        "description": "The correct answer is Notifications. This logging level includes port status changes, providing detailed information about switch operations. \n\n- Warnings indicate potential issues but may not include port status changes. \n- Alerts are higher-priority events requiring immediate attention. \n- Errors only log critical issues and may not capture routine port changes."
    },
    {
        "question": "Which of the following would be the MOST likely attack used to bypass an access control vestibule?",
        "options": [
            "Tailgating",
            "Phishing",
            "Evil twin",
            "Brute-force"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Tailgating. This occurs when an unauthorized individual follows an authorized person into a secure area without proper authentication. \n\n- Phishing is a social engineering attack unrelated to physical security. \n- Evil twin involves setting up a rogue Wi-Fi network to intercept traffic. \n- Brute-force targets passwords or encryption, not physical access controls."
    },




    {
        "question": "A company is considering shifting its business to the cloud. The management team is concerned about the availability of the third-party cloud service. Which of the following should the management team consult to determine the promised availability of the cloud provider?",
        "options": [
            "Memorandum of understanding.",
            "Business continuity plan.",
            "Disaster recovery plan.",
            "Service-level agreement."
        ],
        "correct_answer": 4,
        "description": "The correct answer is Service-level agreement. This document defines the promised availability and performance guarantees provided by the cloud service provider. \n\n- Memorandum of understanding is typically used for non-binding agreements and does not specify technical details like availability. \n- Business continuity plan focuses on internal strategies for maintaining operations during a disruption. \n- Disaster recovery plan outlines the steps to recover systems after an incident but does not specify service guarantees."
    },
    {
        "question": "A new company recently moved into an empty office space. Within days, users in the next office began noticing increased latency and packet drops with their Wi-Fi-connected devices. Which of the following is the MOST likely reason for this issue?",
        "options": [
            "Channel overlap.",
            "Distance from the AP.",
            "Bandwidth latency.",
            "Disabled WPS.",
            "Network congestion."
        ],
        "correct_answer": 1,
        "description": "The correct answer is Channel overlap. Wi-Fi channels that overlap can cause interference, leading to increased latency and packet loss. \n\n- Distance from the AP would lead to signal degradation but not directly cause interference in neighboring offices. \n- Bandwidth latency refers to the inherent delay in data transfer, not typically caused by physical interference. \n- Disabled WPS affects device pairing but not Wi-Fi performance. \n- Network congestion could contribute but is less likely than channel interference in this scenario."
    },
    {
        "question": "A company is designing a SAN and would like to use STP as its medium for communication. Which of the following protocols would BEST suit the company's needs?",
        "options": [
            "SFTP.",
            "Fibre Channel.",
            "iSCSI.",
            "FTP."
        ],
        "correct_answer": 2,
        "description": "The correct answer is Fibre Channel. It is designed for high-speed data transfers in a SAN environment and supports STP for robust communication. \n\n- SFTP and FTP are file transfer protocols, not suitable for SANs. \n- iSCSI is an alternative SAN protocol but does not use STP as its medium."
    },
    {
        "question": "A technician notices that equipment is being moved around and misplaced in the server room, even though the room has locked doors and cabinets. Which of the following would be the BEST solution to identify who is responsible?",
        "options": [
            "Install motion detection.",
            "Install cameras.",
            "Install tamper detection.",
            "Hire a security guard."
        ],
        "correct_answer": 2,
        "description": "The correct answer is Install cameras. Cameras can monitor activity in the server room and provide visual evidence of unauthorized access. \n\n- Motion detection can alert administrators but does not identify the individual responsible. \n- Tamper detection can signal attempts to access equipment but lacks video evidence. \n- Hiring a security guard can be effective but is a costlier and less precise option than cameras."
    },
    {
        "question": "A computer engineer needs to ensure that only a specific workstation can connect to port 1 on a switch. Which of the following features should the engineer configure on the switch interface?",
        "options": [
            "Port tagging.",
            "Port security.",
            "Port mirroring.",
            "Port aggregation."
        ],
        "correct_answer": 2,
        "description": "The correct answer is Port security. This allows the switch to limit access to a specific MAC address, ensuring only the designated workstation can connect. \n\n- Port tagging is used for VLAN configurations, not access control. \n- Port mirroring is for monitoring traffic, not restricting it. \n- Port aggregation combines multiple connections for increased bandwidth but does not enforce security."
    },
    {
        "question": "A cafeteria is facing lawsuits related to criminal internet access that was made over its guest network. The marketing team, however, insists on keeping the cafeteria's phone number as the wireless passphrase. Which of the following actions would improve wireless security while accommodating the marketing team and accepting the terms of use?",
        "options": [
            "Setting WLAN security to use EAP-TLS.",
            "Deploying a captive portal for user authentication.",
            "Using geofencing to limit the area covered by the WLAN.",
            "Configuring guest network isolation."
        ],
        "correct_answer": 2,
        "description": "The correct answer is Deploying a captive portal for user authentication. A captive portal can require users to agree to terms of use, enhancing security and tracking without changing the passphrase. \n\n- EAP-TLS would require additional infrastructure and is not user-friendly for guests. \n- Geofencing is effective for limiting physical access but does not address authentication. \n- Guest network isolation prevents communication between users but does not mitigate misuse of the network."
    },


    {
        "question": "A computer engineer needs to ensure that only a specific workstation can connect to port 1 on a switch. Which of the following features should the engineer configure on the switch interface?",
        "options": [
            "Port tagging.",
            "Port security.",
            "Port mirroring.",
            "Port aggregation."
        ],
        "correct_answer": 2,
        "description": "The correct answer is Port security. This feature allows the administrator to restrict access to a specific port based on MAC address, ensuring that only the designated workstation can connect. \n\n- Port tagging is used for VLAN assignments and does not enforce physical access restrictions. \n- Port mirroring is for monitoring network traffic and does not control connectivity. \n- Port aggregation is used to combine multiple physical links into a single logical link for increased bandwidth, not for restricting access."
    },
    {
        "question": "A cafeteria is facing lawsuits related to criminal internet access that was made over its guest network. The marketing team, however, insists on keeping the cafeteria's phone number as the wireless passphrase. Which of the following actions would improve wireless security while accommodating the marketing team and accepting the terms of use?",
        "options": [
            "Setting WLAN security to use EAP-TLS.",
            "Deploying a captive portal for user authentication.",
            "Using geofencing to limit the area covered by the WLAN.",
            "Configuring guest network isolation."
        ],
        "correct_answer": 2,
        "description": "The correct answer is Deploying a captive portal for user authentication. Captive portals require users to authenticate before accessing the network, adding a layer of accountability while allowing the passphrase to remain simple. \n\n- EAP-TLS requires certificate-based authentication, which may be overly complex for this scenario. \n- Geofencing limits signal range but does not address user authentication. \n- Guest network isolation prevents access between devices but does not authenticate users."
    },
    {
        "question": "An administrator would like to have two servers at different geographical locations provide fault tolerance and high performance while appearing as one URL to users. Which of the following should the administrator implement?",
        "options": [
            "Load balancing.",
            "Multipathing.",
            "NIC teaming.",
            "Warm site."
        ],
        "correct_answer": 1,
        "description": "The correct answer is Load balancing. This distributes traffic across servers to enhance performance and ensure availability, even during server failures. \n\n- Multipathing is used for storage redundancy, not server traffic. \n- NIC teaming provides network redundancy but does not combine geographically separate servers. \n- A warm site is a disaster recovery solution, not a performance enhancement."
    },
    {
        "question": "An IT technician successfully connects to the corporate wireless network at a bank. While performing some tests, the technician observes that the physical address of the DHCP server has changed even though the network connection has not been lost. Which of the following would BEST explain this change?",
        "options": [
            "Server upgrade.",
            "Duplicate IP address.",
            "Scope exhaustion.",
            "Rogue server."
        ],
        "correct_answer": 4,
        "description": "The correct answer is Rogue server. A rogue DHCP server can assign IP configurations, including its own MAC address, to clients, causing such anomalies. \n\n- A server upgrade would not change the MAC address of the legitimate DHCP server. \n- Duplicate IP addresses cause conflicts but do not explain changes in MAC address. \n- Scope exhaustion results in failure to assign IP addresses, not MAC address changes."
    },
    {
        "question": "An ISP is providing internet to a retail store and has terminated its point of connection using a standard Cat 6 pin-out. Which of the following terminations should the technician use when running a cable from the ISP's port to the front desk?",
        "options": [
            "F-type connector.",
            "TIA/EIA-568-B.",
            "LC.",
            "SC."
        ],
        "correct_answer": 2,
        "description": "The correct answer is TIA/EIA-568-B. This standard defines the wiring pinout for Ethernet cables, ensuring compatibility for a Cat 6 cable. \n\n- F-type connectors are used for coaxial cables, not Ethernet. \n- LC and SC connectors are for fiber-optic cables and are incompatible with Cat 6."
    },
    {
        "question": "A company needs to virtualize a replica of its internal physical network without changing the logical topology and the way that devices behave and are managed. Which of the following technologies meets this requirement?",
        "options": [
            "NVF.",
            "SDWAN.",
            "VIP.",
            "MPLS."
        ],
        "correct_answer": 1,
        "description": "The correct answer is NVF (Network Functions Virtualization). This technology allows replication of network functions in a virtual environment without altering the logical topology. \n\n- SDWAN optimizes wide-area network performance but does not replicate internal networks. \n- VIP (Virtual IP) is an addressing mechanism, not a virtualization technology. \n- MPLS is a routing technique, not a virtualization solution."
    },
    {
        "question": "A network technician needs to ensure the company’s external mail server can pass reverse lookup checks. Which of the following records would the technician MOST likely configure?",
        "options": [
            "PTR.",
            "AAAA.",
            "SPF.",
            "CNAME."
        ],
        "correct_answer": 1,
        "description": "The correct answer is PTR (Pointer) record. PTR records map an IP address to a domain name, enabling reverse DNS lookups for email server validation. \n\n- AAAA records map IPv6 addresses, unrelated to reverse lookup. \n- SPF records define mail server policies but do not handle reverse lookups. \n- CNAME aliases domain names but does not address IP-to-domain mapping."
    },


{
  "question": "A network administrator views a network pcap and sees a packet containing the following:\n\ncommunity: public\nrequest-id: 13438\nget-response 1.3.6.1.2.1.1.3.0 Value: 206801150\n\nWhich of the following are the BEST ways for the administrator to secure this type of traffic? (Choose two.)",
  "options": [
    "A. Migrate the network to IPv6.",
    "B. Implement 802.1 X authentication.",
    "C. Set a private community string.",
    "D. Use SNMPv3.",
    "E. Incorporate SSL encryption.",
    "F. Utilize IPSec tunnelling."
  ],
  "correct_answer": [3, 4],
  "description": "The correct answers are C and D. SNMPv3 provides stronger security with encryption and authentication, which is more secure than the older SNMPv1 and SNMPv2 protocols that use community strings. \n\n- Setting a private community string is an improvement over using 'public', but it doesn't provide the same level of security as SNMPv3. \n- IPv6 migration doesn't directly address SNMP security. \n- 802.1X is a network access control method, not directly related to securing SNMP traffic. \n- SSL encryption is relevant for securing web traffic but not for SNMP."
},
{
  "question": "A network technician is troubleshooting a network issue for employees who have reported issues with speed when accessing a server in another subnet. The server is in another building that is 410ft (125m) away from the employees' building. The 10GBASE-T connection between the two buildings uses Cat 5e. Which of the following BEST explains the speed issue?",
  "options": [
    "A. The connection type is not rated for that distance.",
    "B. A broadcast storm is occurring on the subnet.",
    "C. The cable run has interference on it.",
    "D. The connection should be made using a Cat 6 cable."
  ],
  "correct_answer": 1,
  "description": "The correct answer is A. The 10GBASE-T standard requires a maximum distance of 100 meters (328 feet) for Cat 5e cables. At 410 feet, the connection exceeds the distance limit for optimal performance. \n\n- A broadcast storm could affect network performance, but it wouldn't specifically explain the speed issue caused by cable distance. \n- Interference could impact speed, but the primary issue here is the distance. \n- While upgrading to Cat 6 would improve performance, it’s the distance limitation that causes the problem."
},
{
  "question": "Which of the following is a security flaw in an application or network?",
  "options": [
    "A. A threat",
    "B. A vulnerability",
    "C. An exploit",
    "D. A risk"
  ],
  "correct_answer": 2,
  "description": "The correct answer is B. A vulnerability is a weakness in a system or application that could potentially be exploited. \n\n- A threat refers to anything that has the potential to cause harm but is not necessarily a flaw. \n- An exploit is an attack that takes advantage of a vulnerability. \n- A risk refers to the potential for harm, but it is not specifically a flaw in the system."
},
{
  "question": "An administrator is investigating reports of network slowness in a building. While looking at the uplink interface statistics in the switch's CLI, the administrator discovers the uplink is at 100% utilization. However, the administrator is unsure how to identify what traffic is causing the saturation. Which of the following tools should the administrator utilize to identify the source and destination addresses of the traffic?",
  "options": [
    "A. SNMP",
    "B. Traps",
    "C. Syslog",
    "D. NetFlow"
  ],
  "correct_answer": 4,
  "description": "The correct answer is D. NetFlow provides detailed information about traffic flows, including source and destination addresses, allowing the administrator to pinpoint the cause of network saturation. \n\n- SNMP and Traps provide network statistics but lack the detailed flow data required to track traffic patterns. \n- Syslog is useful for logging system events but does not offer detailed traffic flow analysis."
},
{
  "question": "Two new network switches located in different buildings are connected together with single-mode fiber. However, no link exists between the two switches. Which of the following steps should the technician perform FIRST to troubleshoot the issue?",
  "options": [
    "A. Reverse TX/RX on the fiber patch cord at one building.",
    "B. Replace the fiber patch cords in both buildings.",
    "C. Clean the fiber patch cord connectors in both buildings.",
    "D. Connect the fiber patch cord to an OTDR at one building."
  ],
  "correct_answer": 3,
  "description": "The correct answer is C. Cleaning the fiber patch cord connectors is often the first step in troubleshooting a no-link issue, as dirt and dust can interfere with the signal. \n\n- Reversing the TX/RX could be necessary if the cables were wired incorrectly, but it's typically addressed after confirming the physical condition of the cables. \n- Replacing the cables may not be needed if cleaning resolves the issue. \n- An OTDR is a useful tool for more advanced troubleshooting but is typically used after the basics are ruled out."
},
{
  "question": "Which of the following OSI model layers would allow a user to access and download files from a remote computer?",
  "options": [
    "A. Session",
    "B. Presentation",
    "C. Network",
    "D. Application"
  ],
  "correct_answer": 4,
  "description": "The correct answer is D. The Application layer allows users to interact with network services such as file transfer protocols (FTP) and web browsers for file access and download. \n\n- The Session layer establishes, manages, and terminates connections but does not handle file access. \n- The Presentation layer ensures that data is in a readable format but doesn't handle the actual file transfer. \n- The Network layer is responsible for routing data but not for file access."
},
{
  "question": "A new office space is being designed. The network switches are up, but no services are running yet. A network engineer plugs in a laptop configured as a DHCP client to a switch. Which of the following IP addresses should be assigned to the laptop?",
  "options": [
    "A. 10.1.1.1",
    "B. 169.254.1.128",
    "C. 172.16.128.128",
    "D. 192.168.0.1"
  ],
  "correct_answer": 2,
  "description": "The correct answer is B. When a DHCP client cannot reach a DHCP server, it assigns itself an APIPA (Automatic Private IP Addressing) address from the 169.254.x.x range. \n\n- 10.1.1.1, 172.16.128.128, and 192.168.0.1 are private IP addresses, but they require a DHCP server or manual configuration to be assigned."
},
{
  "question": "An organization requires the ability to send encrypted email messages to a partner from an email server that is hosted on premises. The organization prefers to use the standard default ports when creating firewall rules. Which of the following ports should be open to satisfy the requirements?",
  "options": [
    "A. 110",
    "B. 143",
    "C. 587",
    "D. 636"
  ],
  "correct_answer": 3,
  "description": "The correct answer is C. Port 587 is used for sending email securely via SMTP (Simple Mail Transfer Protocol) with encryption. \n\n- Port 110 is used for POP3 email retrieval, not sending encrypted email. \n- Port 143 is used for IMAP email retrieval, also not for sending encrypted messages. \n- Port 636 is used for LDAPS, which is unrelated to email transmission."
},
{
  "question": "Which of the following BEST describes a split-tunnel client-to-server VPN connection?",
  "options": [
    "A. The client sends all network traffic down the VPN tunnel.",
    "B. The client has two different IP addresses that can be connected to a remote site from two different ISPs to ensure availability.",
    "C. The client sends some network traffic down the VPN tunnel and other traffic to the local gateway.",
    "D. The client connects to multiple remote sites at the same time."
  ],
  "correct_answer": 3,
  "description": "The correct answer is C. In a split-tunnel VPN, some traffic is sent through the encrypted VPN tunnel, while other traffic is sent directly to the local network. \n\n- Full-tunnel VPNs send all traffic through the VPN tunnel, which is different from split-tunnel. \n- Using two different IP addresses or connecting to multiple remote sites is not a feature of split-tunneling."
},
{
  "question": "Which of the following is the MOST secure connection used to inspect and provide controlled internet access when remote employees are connected to the corporate network?",
  "options": [
    "A. Site-to-site VPN",
    "B. Full-tunnel VPN",
    "C. Split-tunnel VPN",
    "D. SSH"
  ],
  "correct_answer": 2,
  "description": "The correct answer is B. A full-tunnel VPN ensures that all internet traffic from remote employees is routed through the corporate network, allowing for inspection and controlled access. \n\n- Site-to-site VPNs connect entire networks, not individual remote employees. \n- Split-tunnel VPNs allow some traffic to bypass the corporate network, which may not provide as much control over internet access. \n- SSH is used for secure command-line access, not for providing internet access."
},
{
  "question": "An engineer is troubleshooting poor performance on the network that occurs during work hours. Which of the following should the engineer do to improve performance?",
  "options": [
    "A. Replace the patch cables.",
    "B. Create link aggregation.",
    "C. Create separation rules on the firewall.",
    "D. Create subinterfaces on the existing port."
  ],
  "correct_answer": 2,
  "description": "The correct answer is B. Link aggregation combines multiple network connections to increase throughput and reduce bottlenecks, improving performance. \n\n- Replacing patch cables may address physical layer issues but not necessarily improve network performance. \n- Separation rules on the firewall could help segment traffic but are not focused on improving throughput. \n- Creating subinterfaces does not directly address performance issues related to network congestion."
},



#451-500

{
  "question": "A customer reports there is no access to resources following the replacement of switches. A technician goes to the site to examine the configuration and discovers redundant links between two switches. Which of the following is the reason the network is not functional?",
  "options": [
    "The ARP cache has become corrupt.",
    "CSMA/CD protocols have failed.",
    "STP is not configured.",
    "The switches are incompatible models."
  ],
  "correct_answer": 3,
  "description": "The correct answer is STP (Spanning Tree Protocol) is not configured. STP is necessary to prevent loops in a network with redundant links. Without STP, loops could occur, causing broadcast storms and network congestion. \n\n- ARP cache corruption usually leads to issues with IP resolution, not network connectivity issues caused by redundant links. \n- CSMA/CD is related to Ethernet media access control and does not directly relate to switch configuration. \n- Switch compatibility is rarely the issue when there is no access to resources due to redundant links."
},
{
  "question": "Users are reporting poor wireless performance in some areas of an industrial plant. The wireless controller is measuring a low EIRP value compared to the recommendations noted on the most recent site survey. Which of the following should be verified or replaced for the EIRP value to meet the site survey's specifications? (Choose two.)",
  "options": [
    "AP transmit power",
    "Channel utilization",
    "Signal loss",
    "Update ARP tables",
    "Antenna gain",
    "AP association time"
  ],
  "correct_answer": [1, 5],
  "description": "The correct answers are AP transmit power and Antenna gain. EIRP (Effective Isotropic Radiated Power) is a measure of the strength of the radio signal from an access point. Increasing the AP transmit power or adjusting antenna gain can help meet the desired EIRP values. \n\n- Channel utilization affects interference, but does not directly influence the EIRP. \n- Signal loss may be a factor, but it is not as directly related to the AP's transmit power or antenna gain in this case. \n- Updating ARP tables and AP association time are unrelated to the EIRP calculation."
},
{
  "question": "A coffee shop owner hired a network consultant to provide recommendations for installing a new wireless network. The coffee shop customers expect high speeds even when the network is congested. Which of the following standards should the consultant recommend?",
  "options": [
    "802.11ac",
    "802.11ax",
    "802.11g",
    "802.11n"
  ],
  "correct_answer": 2,
  "description": "The correct answer is 802.11ax (Wi-Fi 6). 802.11ax is the latest wireless standard, offering improved performance in congested environments by using features like OFDMA and MU-MIMO, enabling faster speeds and better efficiency. \n\n- 802.11ac offers high speeds but does not handle congestion as well as 802.11ax. \n- 802.11g and 802.11n are older standards with lower speeds and less effective performance in congested environments."
},
{
  "question": "A network technician is hired to review all the devices within a network and make recommendations to improve network efficiency. Which of the following should the technician do FIRST before reviewing and making any recommendations?",
  "options": [
    "Capture a network baseline.",
    "Perform an environmental review.",
    "Read the network logs.",
    "Run a bandwidth test."
  ],
  "correct_answer": 1,
  "description": "The correct answer is to capture a network baseline. A network baseline provides a reference point to measure the current network performance, which helps identify areas for improvement. \n\n- An environmental review is important but comes after capturing the baseline. \n- Reading network logs and running a bandwidth test can provide useful data, but a baseline must first be established."
},
{
  "question": "A company has multiple offices around the world. The computer rooms in some office locations are too warm. Dedicated sensors are in each room, but the process of checking each sensor takes a long time. Which of the following options can the company put in place to automate temperature readings with internal resources?",
  "options": [
    "Implement NetFlow.",
    "Hire a programmer to write a script to perform the checks.",
    "Utilize ping to measure the response.",
    "Use SNMP with an existing collector server."
  ],
  "correct_answer": 4,
  "description": "The correct answer is to use SNMP (Simple Network Management Protocol) with an existing collector server. SNMP allows for remote monitoring of devices, including temperature sensors, making it an efficient way to automate temperature readings. \n\n- NetFlow is used for network traffic analysis, not temperature monitoring. \n- Writing a custom script could work but is more resource-intensive. \n- Ping measures network availability, not temperature."
},
{
  "question": "Which of the following architectures reduces network latency by enforcing a limit on the number of switching devices on the frame's path between any internal hosts?",
  "options": [
    "Spine and leaf",
    "Software-defined network",
    "Three-tiered",
    "Collapsed core"
  ],
  "correct_answer": 1,
  "description": "The correct answer is Spine and leaf architecture. The spine and leaf design reduces latency by limiting the number of switching devices a frame passes through in the network. \n\n- Software-defined networks focus on the control plane, not directly on reducing latency. \n- Three-tiered architecture may involve more hops, increasing latency. \n- Collapsed core may reduce latency but is less focused on limiting hops compared to spine and leaf."
},
{
  "question": "A network administrator is decommissioning a server. Which of the following will the network administrator MOST likely consult?",
  "options": [
    "Onboarding and offboarding policies",
    "Business continuity plan",
    "Password requirements",
    "Change management documentation"
  ],
  "correct_answer": 4,
  "description": "The correct answer is change management documentation. Decommissioning a server is a change process and should follow the change management procedure to ensure proper handling. \n\n- Onboarding and offboarding policies are related to employee management, not server decommissioning. \n- Business continuity plans cover operational continuity, not server decommissioning. \n- Password requirements are relevant but not directly related to the decommissioning process."
},
{
  "question": "A technician is investigating an issue with connectivity at a customer's location. The technician confirms that users can access resources locally but not over the internet. The technician theorizes that the local router has failed and investigates further. The technician’s testing results show that the router is functional; however, users still are unable to reach resources on the internet. Which of the following describes what the technician should do NEXT?",
  "options": [
    "Document the lessons learned.",
    "Escalate the issue.",
    "Identify the symptoms.",
    "Question users for additional information."
  ],
  "correct_answer": 3,
  "description": "The correct answer is to question users for additional information. Since the router is functional but users still cannot access resources on the internet, the technician should gather more information from the users to identify other potential issues. \n\n- Documenting lessons learned comes after resolving the issue. \n- Escalating the issue might not be necessary if more information can help troubleshoot. \n- Identifying the symptoms has already been done."
},
{
  "question": "On a network with redundant switches, a network administrator replaced one of the switches but was unable to get a connection with another switch. Which of the following should the administrator check after successfully testing the cable that was wired for TIA/EIA-568A on both ends?",
  "options": [
    "If MDIX is enabled on the new switch",
    "If PoE is enabled",
    "If a plenum cable is being used",
    "If STP is disabled on the switches"
  ],
  "correct_answer": 1,
  "description": "The correct answer is to check if MDIX is enabled on the new switch. MDIX (Medium Dependent Interface Crossover) determines whether a crossover cable is needed for the connection. If MDIX is not enabled, a straight-through cable might not work as expected. \n\n- PoE (Power over Ethernet) and plenum cables are unrelated to this specific issue. \n- STP (Spanning Tree Protocol) should be enabled to prevent loops but is not the most immediate concern here."
},
{
  "question": "The lack of a formal process to grant network permissions to different profiles of employees and contractors is leading to an increasing number of security incidents. Non-uniform and overly permissive network accesses are being granted. Which of the following would be the MOST appropriate method to improve the security of the environment?",
  "options": [
    "Change the default permissions to implicit deny.",
    "Configure uniform ACLs to employees and NAC for contractors.",
    "Deploy an RDP server to centralize the access to the network.",
    "Implement role-based access control."
  ],
  "correct_answer": 4,
  "description": "The correct answer is to implement role-based access control (RBAC). RBAC allows for strict control over network permissions based on the role of the user, ensuring that employees and contractors only have access to what is necessary for their role. \n\n- Implicit deny and ACLs are useful but do not provide the granularity of control that RBAC offers. \n- RDP servers are useful for remote access but do not directly address the issue of network access control."
},


    {
        "question": "Which of the following types of planes propagates routing information in an SDWAN solution?",
        "options": [
            "Orchestration plane",
            "Management plane",
            "Control plane",
            "Data plane"
        ],
        "correct_answer": 3,
        "description": "The correct answer is Control plane. In SD-WAN, the control plane is responsible for propagating routing information and making decisions about how traffic should flow across the network. \n\n- The orchestration plane is responsible for overall management and monitoring of the SD-WAN solution. \n- The management plane is used for controlling and monitoring devices but does not directly propagate routing information. \n- The data plane handles actual data traffic but does not manage routing information."
    },
    {
        "question": "A technician is running new Cat 5e cables to a server room. Which of the following tools should the technician use to terminate the cables at the patch panel?",
        "options": [
            "Multimeter",
            "Cable crimper",
            "Toner probe",
            "Punchdown tool"
        ],
        "correct_answer": 4,
        "description": "The correct answer is Punchdown tool. A punchdown tool is used to insert the individual wires of a network cable into the patch panel, ensuring a solid connection. \n\n- A multimeter is used for measuring electrical properties like voltage and resistance, not for terminating cables. \n- A cable crimper is used for attaching connectors to the ends of cables, not for terminating cables into patch panels. \n- A toner probe helps trace cables and identify cables, but it is not used for termination."
    },
    {
        "question": "A disaster recovery team needs a solution that would best meet the following requirements: \n• The server infrastructure has been pre-installed \n• The fail-over location offers basic life support. \n• The fail-over location provides basic network connectivity. \n• Minimizing cost is preferred over quicker business recovery times \n• The expected time for services to be fully operational is days. \nWhich of the following sites would meet the requirements?",
        "options": [
            "Cold site",
            "Cloud site",
            "Warm site",
            "Hot site"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Cold site. A cold site is a basic disaster recovery site with minimal infrastructure that is ideal for cost-sensitive situations. Services can be restored, but it may take several days. \n\n- A cloud site provides a flexible and scalable solution, but it does not fit the requirement of cost minimization and the expected time for services to be fully operational. \n- A warm site provides some hardware and infrastructure but is not as basic and cost-effective as a cold site. \n- A hot site offers fully operational infrastructure, ensuring quick recovery, but it is more expensive."
    },
    {
        "question": "A technician troubleshoots a computer that has intermittent network connectivity and notices the termination point is loose. The technician also observes that the patch cable has already been replaced. Which of the following should the technician do NEXT?",
        "options": [
            "Use a tone generator to trace the cable",
            "Use a multimeter to determine if PoE is available on the switchport",
            "Use a cable crimper to replace the RJ45 connector on the patch cable",
            "Use a punchdown tool to reseat the copper in the wall jack"
        ],
        "correct_answer": 4,
        "description": "The correct answer is Use a punchdown tool to reseat the copper in the wall jack. Since the termination point is loose, reseating the copper with a punchdown tool is necessary to ensure a secure connection. \n\n- Using a tone generator is more appropriate for identifying a cable’s route, not for fixing a loose connection. \n- A multimeter is used for checking electrical issues, not for fixing loose terminations. \n- A cable crimper is used to attach connectors, but the issue here is with the termination point inside the wall jack."
    },
    {
        "question": "A company wants to invest in new hardware for the core network infrastructure. The management team requires that the infrastructure be capable of being repaired in less than 60 minutes if any major part fails. Which of the following metrics is MOST likely associated with this requirement?",
        "options": [
            "RPO",
            "MTTR",
            "FHRP",
            "MTBF"
        ],
        "correct_answer": 2,
        "description": "The correct answer is MTTR (Mean Time to Repair). MTTR refers to the average time taken to repair a system after a failure, aligning with the company's requirement to have infrastructure repairs completed within 60 minutes. \n\n- RPO (Recovery Point Objective) refers to the maximum acceptable amount of data loss, not repair time. \n- FHRP (First Hop Redundancy Protocol) is used to ensure network availability but does not address repair times. \n- MTBF (Mean Time Between Failures) measures the time between system failures but does not focus on the repair time."
    },
    {
        "question": "Which of the following devices and encapsulations are found at the data link layer? (Choose two.)",
        "options": [
            "Session",
            "Frame",
            "Firewall",
            "Switch",
            "Packet",
            "Router"
        ],
        "correct_answer": [2, 4],
        "description": "The correct answers are Frame and Switch. The data link layer handles frames, which encapsulate data for transmission, and devices like switches operate at the data link layer to forward frames. \n\n- The session layer handles session management, not data link layer functions. \n- A firewall operates at multiple layers, but it is not specifically a data link layer device. \n- A router operates at the network layer, not the data link layer."
    },
    {
        "question": "After rebooting an AP, a user is no longer able to connect to the enterprise LAN. A technician plugs a laptop into the same network jack and receives the IP 169.254.0.200. Which of the following is MOST likely causing the issue?",
        "options": [
            "DHCP scope exhaustion",
            "Signal attenuation",
            "Channel overlap",
            "Improper DNS configuration"
        ],
        "correct_answer": 1,
        "description": "The correct answer is DHCP scope exhaustion. The IP address 169.254.0.200 is an APIPA address, which indicates that the device could not receive a valid IP from the DHCP server, suggesting that the DHCP scope may be exhausted. \n\n- Signal attenuation refers to weakened signal strength and would not directly cause an APIPA address to be assigned. \n- Channel overlap could affect wireless performance but would not result in an APIPA address. \n- Improper DNS configuration would affect name resolution, not the assignment of an IP address."
    },
    {
        "question": "A network administrator is concerned about a rainbow table being used to help access network resources. Which of the following must be addressed to reduce the likelihood of a rainbow table being effective?",
        "options": [
            "Password policy",
            "Remote access policy",
            "Acceptable use policy",
            "Data loss prevention policy"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Password policy. A password policy that enforces strong passwords (e.g., complex characters and longer lengths) makes rainbow table attacks less effective by reducing the effectiveness of pre-computed hashes. \n\n- Remote access policy governs access methods but does not directly affect the effectiveness of rainbow tables. \n- Acceptable use policy dictates how resources can be used but does not affect password security. \n- Data loss prevention policy is focused on protecting data from being leaked but does not address password security."
    },

    {
    "question": "Which of the following describes the ability of a corporate IT department to expand its cloud-hosted VM environment with minimal effort?",
    "options": [
        "Scalability",
        "Load balancing",
        "Multitenancy",
        "Geo-redundancy"
    ],
    "correct_answer": 1,
    "description": "The correct answer is Scalability. Scalability refers to the ability to expand or contract resources efficiently to meet demand. In the context of cloud-hosted VMs, scalability ensures the environment can grow with minimal effort.\n\n- Load balancing is used to distribute traffic across multiple servers to optimize resource usage and improve performance but doesn't directly address expansion.\n- Multitenancy refers to a cloud infrastructure where multiple users share the same resources, but it doesn’t specifically address ease of expansion.\n- Geo-redundancy refers to distributing resources across different geographical locations to provide reliability and continuity, but it doesn't focus on expansion."
},
{
    "question": "A user from a remote office is reporting slow file transfers. Which of the following tools will an engineer MOST likely use to get detailed measurement data?",
    "options": [
        "Packet capture",
        "iPerf",
        "SIEM log review",
        "Internet speed test"
    ],
    "correct_answer": 2,
    "description": "The correct answer is iPerf. iPerf is a network testing tool used to measure the bandwidth between two systems, making it ideal for assessing network performance during slow file transfers.\n\n- Packet capture provides insight into network traffic but does not specifically measure bandwidth.\n- SIEM log review focuses on security event management, not network performance.\n- Internet speed tests measure public internet speed and are not helpful for diagnosing internal network issues."
},
{
    "question": "Which of the following can be used to decrease latency during periods of high utilization of a firewall?",
    "options": [
        "Hot site",
        "Content inspection",
        "HA pair",
        "VRRP"
    ],
    "correct_answer": 3,
    "description": "The correct answer is HA pair. A High Availability (HA) pair allows for the deployment of two firewalls that can take over from each other in case of failure, balancing the load and reducing latency during high utilization periods.\n\n- Hot site is a disaster recovery option, not related to decreasing latency during high utilization.\n- Content inspection increases processing time, which may increase latency, not decrease it.\n- VRRP (Virtual Router Redundancy Protocol) ensures router failover, but doesn’t specifically address firewall latency."
},
{
    "question": "A customer calls the help desk to report that a Windows PC is unable to open any websites or access any server shares. The help desk technician suspects there is an issue with the configuration. Which of the following commands should the technician issue FIRST to troubleshoot the issue?",
    "options": [
        "tracert",
        "netstat",
        "arp",
        "ipconfig",
        "nmap"
    ],
    "correct_answer": 4,
    "description": "The correct answer is ipconfig. The ipconfig command displays the network configuration details of the PC, including IP address, subnet mask, and default gateway, which are essential to diagnosing network connectivity issues.\n\n- tracert is useful for tracing the route packets take to reach their destination but isn’t the first step in troubleshooting configuration issues.\n- netstat shows active network connections but doesn’t address configuration problems.\n- arp displays the IP-to-MAC address mappings, which may be helpful later, but not in the initial troubleshooting phase.\n- nmap is a network scanning tool, not directly related to configuration issues."
},
{
    "question": "A network technician needs to select an AP that will support at least 1.3Gbps and 5GHz only. Which of the following wireless standards must the AP support to meet the requirements?",
    "options": [
        "B",
        "AC",
        "AX",
        "N",
        "G"
    ],
    "correct_answer": 2,
    "description": "The correct answer is AC. The 802.11ac wireless standard supports speeds up to 1.3Gbps on the 5GHz band, making it suitable for the technician’s requirements.\n\n- 802.11b, 802.11g, and 802.11n have slower speeds, with 802.11n capable of up to 600Mbps in optimal conditions but not suitable for 1.3Gbps.\n- 802.11ax (Wi-Fi 6) also supports higher speeds but is overkill for the specific 1.3Gbps requirement and could be a higher-cost option."
},
{
    "question": "Which of the following devices would be used to extend the range of a wireless network?",
    "options": [
        "A repeater",
        "A media converter",
        "A router",
        "A switch"
    ],
    "correct_answer": 1,
    "description": "The correct answer is A repeater. A wireless repeater receives and amplifies the signal, extending the range of the network.\n\n- A media converter changes the type of transmission media but does not extend the range of a wireless network.\n- A router connects networks and routes data between them, but it is not designed to extend a wireless signal.\n- A switch is used to connect devices within a network, but it doesn’t extend wireless range."
},
{
    "question": "Which of the following redundant devices creates broadcast storms when connected together on a high-availability network?",
    "options": [
        "Switches",
        "Routers",
        "Access points",
        "Servers"
    ],
    "correct_answer": 1,
    "description": "The correct answer is Switches. When multiple switches are connected without the proper configurations (such as spanning tree protocol), they can create broadcast storms, which flood the network with broadcast packets.\n\n- Routers are designed to route traffic between different networks and are less likely to cause broadcast storms.\n- Access points provide wireless connectivity but do not create broadcast storms in the same way switches do.\n- Servers are used for storing and processing data and do not inherently cause broadcast storms."
},
{
    "question": "A technician is investigating a misconfiguration on a Layer 3 switch. When the technician logs in and runs a command, the following data is shown:\n\nNetwork                   Gateway              Interface\n------------------------------------------------------------\n10.10.0.2/24             10.10.0.1              FastEthernet1/2\n172.16.10.0/24         172.16.10.1          FastEthernet1/3\n192.168.100.0/24    192.168.100.1     Serial0/0\n192.168.50.0/24      192.168.50.1       Serial0/1\n\nWhich of the following commands generated this output?",
    "options": [
        "show route",
        "show config",
        "show interface",
        "tcpdump",
        "netstat -s"
    ],
    "correct_answer": 1,
    "description": "The correct answer is show route. The 'show route' command displays the routing table, which includes the network, gateway, and interface information as shown in the output.\n\n- 'show config' shows the configuration settings, not the routing table.\n- 'show interface' shows details of specific interfaces but doesn’t display routing table information.\n- 'tcpdump' is a network packet analyzer, not related to routing tables.\n- 'netstat -s' shows statistics about network connections but not routing table information."
},
{
    "question": "An IT technician is working on a support ticket regarding an unreachable website. The technician has utilized the ping command to the website, but the site is still unreachable. Which of the following tools should the technician use NEXT?",
    "options": [
        "ipconfig",
        "tracert",
        "arp",
        "netstat"
    ],
    "correct_answer": 2,
    "description": "The correct answer is tracert. tracert (or traceroute) is used to trace the path packets take to reach the destination, which can help identify where the connectivity issue lies.\n\n- ipconfig provides the network configuration details but doesn’t help trace the path of the connection.\n- arp shows the address resolution protocol table, which maps IP addresses to MAC addresses, not useful for diagnosing routing issues.\n- netstat shows active connections, but it is not useful for tracing the path to an unreachable site."
},
{
    "question": "An ISP configured an internet connection to provide 20Mbps, but actual data rates are occurring at 10Mbps and causing a significant delay in data transmission. Which of the following specifications should the ISP check?",
    "options": [
        "Throughput",
        "Latency",
        "Bandwidth",
        "Jitter"
    ],
    "correct_answer": 3,
    "description": "The correct answer is Bandwidth. Bandwidth is the maximum rate at which data can be transmitted over a network, and the ISP should check if the 20Mbps is being properly delivered.\n\n- Throughput refers to the actual data rate achieved, which is lower than the expected value in this case.\n- Latency refers to the delay in data transmission but does not explain the discrepancy in data rates.\n- Jitter measures variability in packet delay, which is unrelated to the data rate issue."
},


    {
        "question": "An application team is deploying a new application. The application team would like the network team to monitor network performance and create alerts if fluctuations in the round-trip time occur for that traffic. Which of the following should the network team monitor to meet this requirement?",
        "options": [
            "Bandwidth",
            "Latency",
            "Loss",
            "Cyclic redundancy check"
        ],
        "correct_answer": 2,
        "description": "The correct answer is latency. Latency measures the time it takes for a packet of data to travel from the source to the destination and back. Monitoring latency will allow the network team to detect fluctuations in round-trip time for the application. \n\n- Bandwidth refers to the amount of data that can be transferred in a given period but does not directly measure delay. \n- Loss measures the percentage of lost packets, which could impact network performance but does not directly address round-trip time fluctuations. \n- Cyclic redundancy check is used for error checking, not for measuring performance."
    },
    {
        "question": "A network administrator is configuring Neighbor Discovery Protocol in an IPv6 network to ensure an attacker cannot spoof link-layer addresses of network devices. Which of the following should the administrator implement?",
        "options": [
            "MAC filtering",
            "Router Advertisement Guard",
            "Port security",
            "DNSSEC"
        ],
        "correct_answer": 2,
        "description": "The correct answer is Router Advertisement Guard. This feature helps protect against attacks where an attacker spoofs the Router Advertisement messages in an IPv6 network to gain access to network resources. \n\n- MAC filtering only controls which devices can connect to the network based on their MAC addresses and does not address spoofing issues. \n- Port security is used to prevent unauthorized devices from connecting to the network but does not directly address IPv6 Neighbor Discovery Protocol vulnerabilities. \n- DNSSEC is used to protect DNS queries, not link-layer address spoofing."
    },
    {
        "question": "A network architect is developing documentation for an upcoming IPv4/IPv6 dual-stack implementation. The architect wants to shorten the following IPv6 address: ef82:0000:0000:0000:0000:1ab1:1234:1bc2. Which of the following is the MOST appropriate shortened version?",
        "options": [
            "ef82:0:1ab1:1234:1bc2",
            "ef82:0::1ab1:1234:1bc2",
            "ef82:0:0:0:0:1ab1:1234:1bc2",
            "ef82::1ab1:1234:1bc2"
        ],
        "correct_answer": 4,
        "description": "The correct answer is ef82::1ab1:1234:1bc2. In IPv6, leading zeros within each block can be omitted, and consecutive blocks of zeros can be replaced with a double colon (::). \n\n- 'ef82:0:1ab1:1234:1bc2' is not a valid shortened form since it does not compress the zeros properly. \n- 'ef82:0::1ab1:1234:1bc2' would be correct if there were more than one block of zeros to collapse, but it's not the most efficient option. \n- 'ef82:0:0:0:0:1ab1:1234:1bc2' is too long and does not leverage the use of the double colon."
    },
    {
        "question": "Which of the following default ports is MOST likely used to send availability and environmental messages about specific devices across the network?",
        "options": [
            "23",
            "53",
            "389",
            "514",
            "3306"
        ],
        "correct_answer": 4,
        "description": "The correct answer is 514. Port 514 is typically used for Syslog, which is a protocol used for sending log and event messages from network devices to a logging server, often for monitoring device status and environmental alerts. \n\n- Port 23 is used by Telnet, a remote login protocol. \n- Port 53 is used by DNS for resolving domain names. \n- Port 389 is used by LDAP for directory services. \n- Port 3306 is used by MySQL databases."
    },
    {
        "question": "A newly installed multifunction copier needs to be set up so scanned documents can be emailed to recipients. Which of the following ports from the copier’s IP address should be allowed?",
        "options": [
            "22",
            "25",
            "53",
            "80"
        ],
        "correct_answer": 2,
        "description": "The correct answer is port 25. Port 25 is used for SMTP (Simple Mail Transfer Protocol), which is the protocol used to send emails. Allowing this port will enable the copier to send scanned documents via email. \n\n- Port 22 is used for SSH (Secure Shell), a protocol for secure remote access. \n- Port 53 is used for DNS, not email transmission. \n- Port 80 is used for HTTP, which handles web traffic, not email."
    },
    {
        "question": "Which of the following has the capability to centrally manage configuration, logging, and firmware versioning for distributed devices?",
        "options": [
            "WLAN controller",
            "Load balancer",
            "SIEM solution",
            "Syslog server"
        ],
        "correct_answer": 1,
        "description": "The correct answer is a WLAN controller. A WLAN controller can centrally manage wireless access points, including configurations, logging, and firmware updates. \n\n- A load balancer distributes network traffic across multiple servers but does not manage configurations or firmware. \n- A SIEM solution (Security Information and Event Management) handles security logging and monitoring, not configuration management. \n- A syslog server collects log data from network devices but does not manage configurations or firmware."
    },
    {
        "question": "A PC and a network connectivity, and a help desk technician is attempting to resolve the issue. The technician plans to run a constant ping command from a Windows workstation while testing various possible reasons for the connectivity issue. Which of the following should the technician use?",
        "options": [
            "ping -w",
            "ping -i",
            "ping -s",
            "ping -t"
        ],
        "correct_answer": 4,
        "description": "The correct answer is 'ping -t'. The '-t' flag in the ping command instructs Windows to continue sending ping requests indefinitely until manually stopped, which is useful for monitoring connectivity over a period of time. \n\n- 'ping -w' sets the timeout for the ping responses, which does not affect the continuous ping behavior. \n- 'ping -i' sets the Time to Live (TTL) value, which impacts how many hops the packet can make. \n- 'ping -s' sets the packet size, which can impact network performance but does not provide continuous monitoring."
    },
    {
        "question": "Which of the following is the MOST effective security control to keep a company’s physical perimeter protected against intrusions leveraged by social-engineering techniques?",
        "options": [
            "Employee training",
            "Biometric lockers",
            "Access control vestibule",
            "Motion detection"
        ],
        "correct_answer": 1,
        "description": "The correct answer is employee training. Training employees to recognize social engineering attacks is one of the most effective ways to prevent intrusions. \n\n- Biometric lockers and access control vestibules are physical security measures that may help protect against unauthorized access but do not address social engineering threats directly. \n- Motion detection is a surveillance technology but does not prevent social engineering attacks."
    },
    {
        "question": "A customer called the help desk to report a network issue. The customer recently added a hub between the switch and the router in order to duplicate the traffic flow to a logging device. After adding the hub, all the other network components that were connected to the switch slowed more than expected. Which of the following is the MOST likely cause of the issue?",
        "options": [
            "Duplex mismatch",
            "Flow control failure",
            "STP malfunction",
            "802.1Q disabled"
        ],
        "correct_answer": 3,
        "description": "The correct answer is STP malfunction. The addition of a hub could cause a network loop, which can lead to performance degradation due to the lack of loop prevention in hubs. STP (Spanning Tree Protocol) is designed to prevent network loops by blocking redundant paths. \n\n- Duplex mismatch can cause network slowness, but it’s less likely to be the result of adding a hub. \n- Flow control failure would lead to congestion, but it’s not directly related to the use of a hub. \n- 802.1Q is used for VLAN tagging and is unlikely to cause the problem in this case."
    },
    {
        "question": "A fiber patch cable, which was being stored in an unsecure telecommunications closet with janitorial supplies, was damaged and caused an outage. A network technician replaced the broken cable with a new cable from a sealed bag. However, this solution did not resolve the outage. Which of the following is the MOST likely explanation?",
        "options": [
            "Incorrect pinout",
            "Incorrect transceivers",
            "Reversed transmit and receive",
            "Dirty optical cables"
        ],
        "correct_answer": 4,
        "description": "The correct answer is dirty optical cables. Fiber optic cables are sensitive to dirt, dust, and other contaminants. If the fibers are not cleaned properly before installation, it can result in poor signal quality or failure to transmit data. \n\n- Incorrect pinout and transceiver issues are common in copper cables, not fiber optics. \n- Reversed transmit and receive would likely cause communication failure, but the most common issue with fiber cables is contamination."
    },



    {
        "question": "An engineer is gathering data to determine the effectiveness of UPSs in use at remote retail locations. Which of the following statistics can the engineer use to determine the availability of the remote network equipment?",
        "options": [
            "Uptime",
            "NetFlow baseline",
            "Review TTL stats",
            "Interface statistics"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Uptime. Uptime indicates the amount of time the network equipment has been running without interruptions, which helps determine the availability of remote network equipment. \n\n- NetFlow baseline measures network traffic, not directly availability. \n- TTL stats provide information about packet travel time, not availability. \n- Interface statistics can indicate network performance, but uptime is a more direct measure of availability."
    },
    {
        "question": "A technician uses a badge to enter a security checkpoint on a corporate campus. An unknown individual quickly walks in behind the technician without speaking. Which of the following types of attacks did the technician experience?",
        "options": [
            "Tailgating",
            "Evil twin",
            "On-path",
            "Piggybacking"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Tailgating. Tailgating is when an unauthorized person gains access to a secured area by following an authorized person. \n\n- Evil twin refers to a fake Wi-Fi network set up to steal information, not physical access. \n- On-path attacks involve intercepting or modifying communication, which is not applicable in this scenario. \n- Piggybacking is similar to tailgating but usually involves more active cooperation from the authorized person."
    },
    {
        "question": "A company is opening a new building on the other side of its campus. The distance from the closest building to the new building is 1,804ft (550m). The company needs to connect the networking equipment in the new building to the other buildings on the campus without using a repeater. Which of the following transceivers should the company use?",
        "options": [
            "10GBASE-SW",
            "10GBASE-LR",
            "10GBASE-LX4 over multimode fiber",
            "10GBASE-SR"
        ],
        "correct_answer": 2,
        "description": "The correct answer is 10GBASE-LX4 over multimode fiber. This transceiver is designed for long-distance connections (up to 10km) and supports high-speed networking. \n\n- 10GBASE-SW is optimized for shorter distances (around 300m) and is not suitable for the 550m distance. \n- 10GBASE-LR supports long-range connections but typically uses single-mode fiber, not ideal for campus installations requiring multimode fiber. \n- 10GBASE-SR is ideal for short-range connections over multimode fiber, but LX4 offers better range."
    },
    {
        "question": "An AP uses a 98ft (30m) Cat 6 cable to connect to an access switch. The cable is wired through a duct close to a three-phase motor installation. Anytime the three-phase is turned on, all users connected to the switch experience high latency on the network. Which of the following is MOST likely the cause of the issue?",
        "options": [
            "Interference",
            "Attenuation",
            "Open circuit",
            "Short circuit"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Interference. The three-phase motor is likely causing electromagnetic interference (EMI) that affects the performance of the Cat 6 cable, resulting in high latency. \n\n- Attenuation refers to signal degradation over distance and is not the cause of high latency. \n- Open or short circuits would result in a complete loss of connectivity, not intermittent issues like high latency."
    },
    {
        "question": "An IT technician installs five old switches in a network. In addition to the low port rates on these switches, they also have improper network configurations. After three hours, the network becomes overwhelmed by continuous traffic and eventually shuts down. Which of the following is causing the issue?",
        "options": [
            "Broadcast storm",
            "Collisions",
            "IP settings",
            "Routing loops"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Broadcast storm. A broadcast storm occurs when there is an excessive amount of broadcast traffic on the network, causing congestion and potential shutdowns. \n\n- Collisions are less likely with modern switches, which use full-duplex communication. \n- Incorrect IP settings can cause connectivity issues but would not cause continuous traffic that leads to a shutdown. \n- Routing loops can cause network problems but would not result in broadcast storms specifically."
    },
    {
        "question": "An engineer is designing a network topology for a company that maintains a large on-premises private cloud. A design requirement mandates internet-facing hosts to be partitioned off from the internal LAN and internal server IP ranges. Which of the following defense strategies helps meet this requirement?",
        "options": [
            "Implementing a screened subnet",
            "Deploying a honeypot",
            "Utilizing network access control",
            "Enforcing a Zero Trust model"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Implementing a screened subnet. A screened subnet (or DMZ) helps isolate internet-facing hosts from the internal LAN and servers, providing an additional layer of security. \n\n- A honeypot is used to attract and monitor attackers, but it does not directly address partitioning networks. \n- Network access control (NAC) can restrict access but doesn't necessarily provide network isolation. \n- A Zero Trust model focuses on continuous verification of users, not network segmentation."
    },
    {
        "question": "Many IP security cameras use RTSP to control media playback. Which of the following default transport layer port numbers does RTSP use?",
        "options": [
            "445",
            "554",
            "587",
            "5060"
        ],
        "correct_answer": 2,
        "description": "The correct answer is 554. RTSP (Real-Time Streaming Protocol) uses port 554 to manage media streaming for IP cameras and other video applications. \n\n- Port 445 is used for Microsoft-Directory services. \n- Port 587 is for sending email (SMTP with encryption). \n- Port 5060 is used for SIP (Session Initiation Protocol) for voice communication."
    },
    {
        "question": "Which of the following would be increased by adding encryption to data communication across the network?",
        "options": [
            "Availability",
            "Integrity",
            "Accountability",
            "Confidentiality"
        ],
        "correct_answer": 4,
        "description": "The correct answer is Confidentiality. Encryption helps protect data from unauthorized access, ensuring that only authorized parties can view it. \n\n- Availability refers to the availability of services, which is not directly affected by encryption. \n- Integrity ensures that data has not been altered, but encryption specifically secures confidentiality. \n- Accountability relates to tracking actions in a system, but encryption does not directly impact this."
    },
    {
        "question": "A network technician is working at a new office location and needs to connect one laptop to another to transfer files. The laptops are newer models and do not have Ethernet ports. Access points are not available either. Which of the following types of wireless network SSIDs does the network technician need to configure to be able to connect the laptops together?",
        "options": [
            "Independent Basic Service Set",
            "Extended Service Set",
            "Distribution System Service",
            "Basic Service Set"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Independent Basic Service Set (IBSS). IBSS allows laptops to connect directly to each other in an ad-hoc mode without the need for a central access point. \n\n- Extended Service Set (ESS) involves multiple access points and is used for larger networks. \n- Distribution System Service (DSS) is used in infrastructure mode to connect multiple access points. \n- Basic Service Set (BSS) requires a single access point and cannot be used for direct laptop-to-laptop communication."
    },
    {
        "question": "An organization would like to implement a disaster recovery strategy that does not require a facility agreement or idle hardware. Which of the following strategies MOST likely meets the organization’s requirements?",
        "options": [
            "Cloud site",
            "Cold site",
            "Warm site",
            "Hot site"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Cloud site. A cloud site offers flexible, on-demand disaster recovery resources without the need for dedicated physical space or idle hardware. \n\n- A Cold site requires an empty facility and hardware that must be provisioned in the event of a disaster, which involves more upfront preparation. \n- A Warm site has some hardware and software in place but still requires configuration. \n- A Hot site is fully functional with active systems and data replication, but it requires more investment than a cloud site."
    },

#501-550



    {
        "question": "A network administrator is investigating reports about network performance and finds high utilization on a switch uplink. The administrator is unsure whether this is an anomaly or normal behavior that will require an upgrade to resolve. Which of the following should the administrator reference to gain historical perspective?",
        "options": [
            "Device configuration review",
            "ARP table export",
            "Service-level agreement",
            "Network performance baseline"
        ],
        "correct_answer": 4,
        "description": "The correct answer is Network performance baseline. A network performance baseline provides historical data on network utilization and helps the administrator assess whether the current performance is normal or requires an upgrade. \n\n- Device configuration review is useful for verifying settings but does not provide historical performance context. \n- ARP table export does not offer any insights into network performance over time. \n- Service-level agreements are contracts outlining service expectations but do not contain specific historical performance data."
    },
    {
        "question": "A network administrator is troubleshooting a client’s device that cannot connect to the network. A physical inspection of the switch shows the RJ45 is connected. The NIC shows no activity lights. The network administrator moves the device to another location and connects to the network without issues. Which of the following tools would be the BEST option for the network administrator to use to further troubleshoot?",
        "options": [
            "Tone generator",
            "Multimeter",
            "Optical time-domain reflectometer",
            "Cable tester"
        ],
        "correct_answer": 4,
        "description": "The correct answer is Cable tester. A cable tester is the best tool to check if the cable is functioning properly and if there is any wiring or connectivity issue. \n\n- Tone generators are used to trace cables and locate wires but do not diagnose connection issues. \n- Multimeters are used to check electrical components but are not typically used to troubleshoot network cables. \n- An optical time-domain reflectometer is used to test fiber optic cables, not copper network cables."
    },
    {
        "question": "A non-employee was able to enter a server room. Which of the following could have prevented this from happening?",
        "options": [
            "A security camera",
            "A biometric reader",
            "OTP key fob",
            "Employee training"
        ],
        "correct_answer": 2,
        "description": "The correct answer is A biometric reader. A biometric reader is a secure way to restrict physical access to sensitive areas by verifying identity using unique physical traits. \n\n- A security camera can help monitor access but does not prevent unauthorized entry. \n- OTP key fobs provide temporary access codes but do not offer identity verification like biometrics. \n- Employee training is essential for security awareness but does not directly prevent unauthorized access."
    },
    {
        "question": "A large number of PCs are obtaining an APIPA IP address, and a number of new computers were added to the network. Which of the following is MOST likely causing the PCs to obtain an APIPA address?",
        "options": [
            "Rogue DHCP server",
            "Network collision",
            "Incorrect DNS settings",
            "DHCP scope exhaustion"
        ],
        "correct_answer": 4,
        "description": "The correct answer is DHCP scope exhaustion. If the DHCP server runs out of available IP addresses in its scope, clients will default to obtaining an APIPA address. \n\n- A rogue DHCP server may cause IP address conflicts but would not cause APIPA addresses on its own. \n- Network collisions can disrupt communication but are less likely to result in APIPA addresses. \n- Incorrect DNS settings do not affect the ability to obtain an IP address from DHCP."
    },
    {
        "question": "An engineer is using a tool to run an ICMP sweep of a network to find devices that are online. When reviewing the results, the engineer notices a number of workstations that are currently verified as being online are not listed in the report. The tool was configured to scan using the following information: Network address: 172.28.16.0 - CIDR: /22 - The engineer collected the following information from the client workstation: IP address: 172.28.17.206 - Subnet mask: 255.255.252.0 - Which of the following MOST likely explains why the tool is failing to detect some workstations?",
        "options": [
            "The scanned network range is incorrect.",
            "The subnet mask on the client is misconfigured.",
            "The workstation has a firewall enabled.",
            "The tool is unable to scan remote networks."
        ],
        "correct_answer": 1,
        "description": "The correct answer is The scanned network range is incorrect. The CIDR /22 and the subnet mask 255.255.252.0 cover a different range of IPs than what the tool is scanning. \n\n- The subnet mask on the client is correctly set and does not explain the failure. \n- A firewall may block ICMP requests, but the tool specifically scans IP ranges rather than checking firewall settings. \n- The tool can scan local networks, so the issue is most likely due to an incorrect network range."
    },
    {
        "question": "Which of the following can be used to limit the ability of devices to perform only HTTPS connections to an internet update server without exposing the devices to the public internet?",
        "options": [
            "Allow connections only to an internal proxy server.",
            "Deploy an IDS system and place it in line with the traffic.",
            "Create a screened network and move the devices to it.",
            "Use a host-based network firewall on each device."
        ],
        "correct_answer": 3,
        "description": "The correct answer is Create a screened network and move the devices to it. A screened network (also known as a DMZ) can isolate devices and control their internet access, restricting connections to specific servers or protocols. \n\n- Allowing connections only to an internal proxy server may limit internet access but does not directly restrict HTTPS traffic. \n- An IDS system helps detect malicious traffic but does not prevent HTTPS connections. \n- A host-based firewall can control traffic on each device, but it is not as effective in controlling network-wide access."
    },
    {
        "question": "A network administrator notices excessive wireless traffic occurring on an access point after normal business hours. The access point is located on an exterior wall. Which of the following should the administrator do to limit wireless access outside the building?",
        "options": [
            "Set up a private VLAN.",
            "Disable roaming on the WAP.",
            "Change to a directional antenna.",
            "Stop broadcasting of the SSID."
        ],
        "correct_answer": 3,
        "description": "The correct answer is Change to a directional antenna. A directional antenna can focus the wireless signal in a specific direction, limiting coverage outside the building. \n\n- Setting up a private VLAN would control network traffic but not limit wireless access. \n- Disabling roaming on the WAP prevents clients from switching APs but does not affect the wireless range. \n- Stopping the broadcasting of the SSID hides the network name but does not limit the signal range."
    },
    {
        "question": "A technician thinks one of the router ports is flapping. Which of the following available resources should the technician use in order to determine if the router is flapping?",
        "options": [
            "Audit logs",
            "NetFlow",
            "Syslog",
            "Traffic logs"
        ],
        "correct_answer": 3,
        "description": "The correct answer is Syslog. Syslog can capture log messages from the router, including interface status changes, which helps identify if a port is flapping. \n\n- Audit logs are more useful for user activity and access control rather than network device status. \n- NetFlow tracks traffic flow, but does not provide information on port status changes. \n- Traffic logs capture network activity but are not focused on interface status."
    },
    {
        "question": "Which of the following layers is where TCP/IP port numbers identify which network application is receiving the packet and where it is applied?",
        "options": [
            "3",
            "4",
            "5",
            "6",
            "7"
        ],
        "correct_answer": 2,
        "description": "The correct answer is 4. The TCP/IP model uses layer 4 (Transport) to handle port numbers, which direct packets to the correct application on the receiving system. \n\n- Layer 3 (Network) is responsible for routing and IP addressing. \n- Layer 5 (Session) manages communication sessions between applications. \n- Layer 6 (Presentation) deals with data format translation and encryption. \n- Layer 7 (Application) deals with high-level protocols but not port numbers."
    },
    {
        "question": "A user reports that a crucial fileshare is unreachable following a network upgrade that was completed the night before. A network technician confirms the problem exists. Which of the following troubleshooting steps should the network technician perform NEXT?",
        "options": [
            "Establish a theory of probable cause.",
            "Implement a solution to fix the problem.",
            "Create a plan of action to resolve the problem.",
            "Document the problem and the solution."
        ],
        "correct_answer": 1,
        "description": "The correct answer is Establish a theory of probable cause. After confirming the problem, the technician should develop a theory about what is causing the issue before taking corrective action. \n\n- Implementing a solution is premature without identifying the cause. \n- Creating a plan of action is important, but it follows the establishment of the probable cause. \n- Documenting the problem is important, but it comes after solving the issue."
    },


{
    "question": "A network engineer is designing a wireless network that has the following requirements: \n• Network speed must be higher than 100Mbps\n• Must use the 2.4GHz and 5GHz bands\nWhich of the following 802.11 standards should the engineer select?",
    "options": [
        "802.11a",
        "802.11b",
        "802.11g",
        "802.11n"
    ],
    "correct_answer": 4,
    "description": "The correct answer is 802.11n. This standard supports higher speeds (up to 600 Mbps) and can operate on both the 2.4GHz and 5GHz bands. \n\n- 802.11a supports up to 54Mbps and operates only on the 5GHz band. \n- 802.11b supports up to 11Mbps and operates only on the 2.4GHz band. \n- 802.11g also supports up to 54Mbps but only operates on the 2.4GHz band, which doesn’t meet the required speed."
},

{
    "question": "A network engineer is investigating reports of poor performance on a videoconferencing application. Upon reviewing the report, the engineer finds that available bandwidth at the WAN connection is low. Which of the following is the MOST appropriate mechanism to handle this issue?",
    "options": [
        "Traffic shaping",
        "Flow control",
        "NetFlow",
        "Link aggregation"
    ],
    "correct_answer": 1,
    "description": "The correct answer is Traffic shaping. Traffic shaping allows for the prioritization of certain traffic types, such as video conferencing, ensuring that critical applications receive the bandwidth they need. \n\n- Flow control is used to prevent data loss but is not specifically designed for optimizing bandwidth usage. \n- NetFlow is used for monitoring network traffic, not for addressing bandwidth issues. \n- Link aggregation increases the bandwidth between devices but does not prioritize certain types of traffic."
},

{
    "question": "Which of the following protocols can be routed?",
    "options": [
        "FCoE",
        "Fibre Channel",
        "iSCSI",
        "NetBEUI"
    ],
    "correct_answer": 3,
    "description": "The correct answer is iSCSI. iSCSI (Internet Small Computer Systems Interface) is a protocol that allows SCSI commands to be sent over IP networks and can be routed across networks. \n\n- FCoE and Fibre Channel are primarily used for high-speed data transfer in storage area networks and are not routed protocols. \n- NetBEUI is a non-routable protocol primarily used in older Windows networks."
},

{
    "question": "A Fortune 500 company would like to move its on-premises corporate email systems to a multitenant product hosted in the cloud where no maintenance of the underlying server OS or platform is required. Which of the following BEST represents the model the company should choose?",
    "options": [
        "Public",
        "Private",
        "Hybrid",
        "Community"
    ],
    "correct_answer": 1,
    "description": "The correct answer is Public. In a public cloud model, resources are provided by a third-party cloud service provider and the underlying platform and infrastructure are managed by the provider. \n\n- Private cloud involves dedicated resources for a single organization, but the company is looking for a multitenant solution. \n- Hybrid cloud involves a mix of public and private clouds, which isn’t needed here. \n- Community cloud is shared by multiple organizations but is not as commonly used for multitenant applications as public cloud."
},

{
    "question": "Which of the following situations would require an engineer to configure subinterfaces?",
    "options": [
        "In a router-on-a-stick deployment with multiple VLANs",
        "In order to enable inter-VLAN routing on a multilayer switch",
        "When configuring VLAN trunk links between switches",
        "After connecting a router that does not support 802.1Q VLAN tags"
    ],
    "correct_answer": 1,
    "description": "The correct answer is 'In a router-on-a-stick deployment with multiple VLANs.' Subinterfaces are required in this configuration to enable routing between different VLANs using a single physical interface. \n\n- Inter-VLAN routing on a multilayer switch does not require subinterfaces, as multilayer switches handle VLANs differently. \n- VLAN trunk links between switches use a single physical interface, but subinterfaces are not required for basic trunking. \n- A router without 802.1Q support would require additional hardware, not just subinterfaces."
},

{
    "question": "At which of the following OSI model layers does a MAC filter list for a wireless infrastructure operate?",
    "options": [
        "Physical",
        "Network",
        "Session",
        "Data link"
    ],
    "correct_answer": 4,
    "description": "The correct answer is Data link. MAC filtering operates at the Data Link layer (Layer 2) of the OSI model, where MAC addresses are used to identify devices on the network. \n\n- The Physical layer involves the transmission of raw data and does not deal with MAC addresses. \n- The Network layer deals with routing and IP addresses, not MAC addresses. \n- The Session layer handles sessions and connections, which is unrelated to MAC filtering."
},

{
    "question": "The Chief Executive Officer of a company wants to ensure business operations are not disrupted in the event of a disaster. The solution must have fully redundant equipment, real-time synchronization, and zero data loss. Which of the following should be prepared?",
    "options": [
        "Cloud site",
        "Warm site",
        "Hot site",
        "Cold site"
    ],
    "correct_answer": 3,
    "description": "The correct answer is Hot site. A hot site is a fully operational data center with real-time synchronization and redundant equipment to ensure minimal disruption in case of a disaster. \n\n- A cloud site may provide some of these features, but a hot site specifically addresses the requirement for real-time synchronization and zero data loss. \n- A warm site provides some infrastructure but requires more setup and may not meet the zero data loss requirement. \n- A cold site provides basic infrastructure with no active data or systems."
},

{
    "question": "An IT technician needs to increase bandwidth to a server. The server has multiple gigabit ports. Which of the following can be used to accomplish this without replacing hardware?",
    "options": [
        "STP",
        "802.1Q",
        "Duplex",
        "LACP"
    ],
    "correct_answer": 4,
    "description": "The correct answer is LACP (Link Aggregation Control Protocol). LACP allows multiple network connections to be aggregated to increase the overall bandwidth to the server without the need to replace hardware. \n\n- STP (Spanning Tree Protocol) is used to prevent loops in network topologies and does not increase bandwidth. \n- 802.1Q is used for VLAN tagging but does not increase bandwidth by itself. \n- Duplex refers to communication modes (full or half duplex) and does not directly impact bandwidth."
},

{
    "question": "A company wants to mitigate unauthorized physical connectivity after implementing a hybrid work schedule. Which of the following will the company MOST likely configure?",
    "options": [
        "Intrusion prevention system",
        "DHCP snooping",
        "ARP inspection",
        "Port security"
    ],
    "correct_answer": 4,
    "description": "The correct answer is Port security. Port security limits physical access to the network by controlling which devices can connect to specific network ports, helping mitigate unauthorized physical connectivity. \n\n- Intrusion prevention systems protect against unauthorized network traffic but do not control physical access. \n- DHCP snooping and ARP inspection are used to secure network communication, not to control physical device access."
},

{
    "question": "A customer cannot reach a web application on a local server. The network consultant suspects that the server is not accepting the HTTPS connection. Which of the following commands should the consultant run on the server to determine what is occurring?",
    "options": [
        "route",
        "arp",
        "nmap",
        "netstat"
    ],
    "correct_answer": 4,
    "description": "The correct answer is netstat. The netstat command allows the consultant to check the status of network connections, including whether the server is listening for HTTPS connections on port 443. \n\n- The route command is used to display and modify the IP routing table but does not provide details about open ports. \n- arp is used to view the ARP table and resolve MAC addresses, which is unrelated to HTTPS connections. \n- nmap is a network scanning tool that can check open ports, but netstat is more appropriate for checking local server connections."
},


{
  "question": "A help desk technician is troubleshooting a Windows server named SQL.local and wants to check which port a specific application is running on. Which of the following commands should the technician run?",
  "options": [
    "dig",
    "traceroute",
    "arp",
    "netstat"
  ],
  "correct_answer": 4,
  "description": "The correct answer is netstat. This command shows the active connections and the ports that are currently open on the server. \n\n- dig is used for querying DNS records, not for viewing open ports. \n- traceroute is used for determining the path packets take to a destination, not for checking ports. \n- arp is used to view the MAC addresses of devices on the network, not for checking open ports."
},
{
  "question": "A network administrator is configuring a static DSL connection on the perimeter router to use a backup route to the fiber connection using OSPF routing. The administrator notices all traffic is going over the DSL connection and both links are working. Which of the following should the administrator do to adjust the routing settings for the fiber connection to be used by the router?",
  "options": [
    "Add the DSL connection to the neighbor table for OSPF protocol",
    "Change the routing protocol to EIGRP for the fiber connection",
    "Increase the administrative distance of the DSL connection",
    "Create a separate VLAN for the DSL connection"
  ],
  "correct_answer": 3,
  "description": "The correct answer is increase the administrative distance of the DSL connection. Administrative distance is used to determine the preferred route when multiple routes exist. By increasing the distance for the DSL connection, the fiber connection will be preferred. \n\n- Adding the DSL connection to the OSPF neighbor table is unnecessary if it is already functional. \n- Changing the routing protocol to EIGRP is not needed since OSPF can handle the routing properly. \n- Creating a separate VLAN does not affect the routing preference between connections."
},
{
  "question": "A Chief Information Officer wants to monitor network breaching in a passive, controlled manner. Which of the following would be BEST to implement?",
  "options": [
    "Honeypot",
    "Perimeter network",
    "Intrusion prevention system",
    "Port security"
  ],
  "correct_answer": 1,
  "description": "The correct answer is honeypot. A honeypot is a decoy system designed to attract and detect potential attackers in a controlled manner, allowing security teams to monitor breaches without risking critical infrastructure. \n\n- A perimeter network is useful for securing the network but does not specifically monitor for breaches. \n- An intrusion prevention system is an active defense tool, rather than a passive monitoring solution. \n- Port security is important for securing physical access to the network but does not directly address passive monitoring."
},
{
  "question": "A technician monitors a switch interface and notices it is not forwarding frames on a trunked port. However, the cable and interfaces are in working order. Which of the following is MOST likely the cause of the issue?",
  "options": [
    "STP policy",
    "Flow control",
    "802.1Q configuration",
    "Frame size"
  ],
  "correct_answer": 3,
  "description": "The correct answer is 802.1Q configuration. If the 802.1Q VLAN tagging is misconfigured on a trunked port, it can prevent frames from being forwarded correctly. \n\n- STP policy (Spanning Tree Protocol) can block ports to prevent loops but would not prevent frames from being forwarded entirely. \n- Flow control controls data transmission speed but does not stop frames from being forwarded. \n- Frame size issues would typically cause packet drops, but not the complete lack of forwarding on a trunked port."
},
{
  "question": "A wireless network technician is receiving reports from some users who are unable to see both of the corporate SSIDs on their mobile devices. A site survey was recently commissioned, and the results verified acceptable RSSI from both APs in all user areas. The APs support modern wireless standards and are all broadcasting their SSIDs. The following table shows some of the current AP settings:\n\nName\tPower\tDirectionality\tWireless standard\tAuthentication standard\tSSID\nAP1\tMedium\tOmnidirectional\t802.11b\tWPA2-PSK\tCORP01\nAP2\tHigh\tDirectional\t802.11a\tWPA2-PSK\tCORP02\n\nWhich of the following changes would result in all of the user devices being capable of seeing both corporate SSIDs?",
  "options": [
    "Implementing the WPA2 Enterprise authentication standard",
    "Implementing omnidirectional antennas for both APs",
    "Configuring the highest power settings for both APs",
    "Configuring both APs to use the 802.11ac wireless standard"
  ],
  "correct_answer": 2,
  "description": "The correct answer is implementing omnidirectional antennas for both APs. Omnidirectional antennas provide better coverage in all directions, ensuring that users can access both SSIDs. \n\n- WPA2 Enterprise does not address the issue of SSID visibility; it's a more secure method of authentication. \n- Configuring higher power settings might cause interference, especially in areas where the signals overlap. \n- Changing to 802.11ac would improve speed but does not address the visibility issue directly."
},
{
  "question": "An infrastructure company is implementing a cabling solution to connect sites on multiple continents. Which of the following cable types should the company use for this project?",
  "options": [
    "Cat 7",
    "Single-mode",
    "Multimode",
    "Cat 6"
  ],
  "correct_answer": 2,
  "description": "The correct answer is single-mode. Single-mode fiber optics are best suited for long-distance communication, as they can carry signals over greater distances with less signal loss than multimode fiber. \n\n- Cat 7 and Cat 6 cables are copper-based and are typically used for shorter distances. \n- Multimode fiber is suitable for shorter distances compared to single-mode fiber, making it less ideal for a project spanning multiple continents."
},
{
  "question": "A user is required to log in to a main web application, which then grants the user access to all other programs needed to complete job-related tasks. Which of the following authentication methods does this setup describe?",
  "options": [
    "SSO",
    "RADIUS",
    "TACACS+",
    "Multifactor authentication",
    "802.1X"
  ],
  "correct_answer": 1,
  "description": "The correct answer is SSO (Single Sign-On). This allows the user to log in once and gain access to multiple applications without having to log in again. \n\n- RADIUS and TACACS+ are protocols for managing authentication but do not describe the SSO process. \n- Multifactor authentication adds additional layers of security, but it's not the main concept here. \n- 802.1X is an authentication protocol typically used for network access control."
},
{
  "question": "A company has a geographically remote office. In order to connect to the internet, the company has decided to use a satellite WAN link. Which of the following is the GREATEST concern for this type of connection?",
  "options": [
    "Duplex",
    "Collisions",
    "Jitter",
    "Encapsulation"
  ],
  "correct_answer": 3,
  "description": "The correct answer is jitter. Satellite connections have a higher latency, which can lead to jitter, affecting real-time communication like VoIP and video conferencing. \n\n- Duplex and collisions are more commonly concerns for Ethernet-based connections. \n- Encapsulation is a method of packet formatting and is not the primary concern for satellite WAN links."
},
{
  "question": "A network technician is deploying multiple switches for a new office. The switches are separately managed and need to be cabled in to support dual firewalls in a HA setup. Which of the following should the technician enable to support proper stability of the network switches?",
  "options": [
    "NTP",
    "CDMA",
    "STP",
    "LACP",
    "802.1Q"
  ],
  "correct_answer": 3,
  "description": "The correct answer is STP (Spanning Tree Protocol). STP prevents network loops by ensuring that there is only one active path between network switches, which is crucial in high-availability (HA) setups. \n\n- NTP is used for time synchronization, not for network stability. \n- CDMA is a cellular technology, not related to switch stability. \n- LACP (Link Aggregation Control Protocol) and 802.1Q are used for link aggregation and VLAN configuration, respectively, but STP is the key for preventing network loops."
},
{
  "question": "Which of the following would be used to filter web traffic based on content?",
  "options": [
    "Proxy server",
    "Load balancer",
    "Media converter",
    "Access point"
  ],
  "correct_answer": 1,
  "description": "The correct answer is proxy server. A proxy server can filter web traffic, cache data, and block access to certain websites based on content. \n\n- A load balancer distributes traffic between multiple servers and does not filter content. \n- A media converter is used to convert between different types of media (e.g., fiber to copper) and does not filter web traffic. \n- An access point is used for providing wireless network access, not for filtering web traffic."
},


{
  "question": "A bank installed a new smart TV to stream online video services, but the smart TV was not able to connect to the branch Wi-Fi. The next day, a technician was able to connect the TV to the Wi-Fi, but a bank laptop lost network access at the same time. Which of the following is the MOST likely cause?",
  "options": [
    "DHCP scope exhaustion",
    "AP configuration reset",
    "Hidden SSID",
    "Channel overlap"
  ],
  "correct_answer": 1,
  "description": "The correct answer is 'AP configuration reset.' When the AP settings are reset, it can affect network connectivity for devices already connected, such as the laptop in this case. \n\n- DHCP scope exhaustion occurs when the DHCP server runs out of IP addresses, but this typically causes issues for multiple devices and not just the laptop. \n- A hidden SSID would not typically cause issues with connectivity as the device would simply need to be configured to connect to the hidden SSID. \n- Channel overlap can cause interference, but it is less likely to cause such a specific situation where only one device is affected."
},
{
  "question": "Newly crimped 26ft (8m) STP Cat 6 patch cables were recently installed in one room to replace cables that were damaged by a vacuum cleaner. Now, users in that room are unable to connect to the network. A network technician tests the existing cables first. The 177ft (54m) cable that runs from the core switch to the access switch on the floor is working, as is the 115ft (35m) cable run from the access switch to the wall jack in the office. Which of the following is the MOST likely reason the users cannot connect to the network?",
  "options": [
    "Mixed UTP and STP cables are being used.",
    "The patch cables are not plenum rated.",
    "The cable distance is exceeded.",
    "An incorrect pinout on the patch cable is being used."
  ],
  "correct_answer": 3,
  "description": "The correct answer is 'An incorrect pinout on the patch cable is being used.' Incorrect wiring can prevent network connectivity even if the cables appear to be intact. \n\n- Mixed UTP and STP cables typically don’t cause connectivity issues as long as they are wired correctly. \n- The patch cables not being plenum rated does not affect their ability to function, though it may be a concern for fire code compliance in certain environments. \n- The cable distance being exceeded is unlikely as the patch cables are within the acceptable range for Cat 6 cables."
},
{
  "question": "While troubleshooting a network outage, a technician discovers symptoms that indicate a patch cable is connecting the core switch to the router. A network engineer confirms the theory is plausible, and the technician tests the cable. The cable passes the test, and the technician properly plugs the cable back into the correct network ports. However, the network outage continues. Which of the following is the NEXT step the technician should take to troubleshoot the network outage?",
  "options": [
    "Establish a new theory.",
    "Verify full system functionality.",
    "Establish a plan of action.",
    "Continue to work the original theory."
  ],
  "correct_answer": 1,
  "description": "The correct answer is 'Establish a new theory.' Since the original theory (the patch cable issue) has been ruled out, it's time to establish a new theory and explore other potential causes of the network outage. \n\n- Verifying full system functionality might be necessary, but without a new theory, the technician could be troubleshooting the wrong issue. \n- Establishing a plan of action should come after a new theory is confirmed. \n- Continuing with the original theory is not appropriate after the issue with the patch cable has been ruled out."
},
{
  "question": "A help desk supervisor discovers the following ticket excerpt while reviewing notes in a customer’s account: Received report that customer was unable to use the scanner to read barcodes, the internet no longer worked, and the monitor was fuzzy. Arrived on site and began troubleshooting. Confirmed monitor issue. Replaced VGA cable. Confirmed scanner failure. Scanner USB cable was unattached. Reattached cable. Confirmed internet issue. Duplicated on test laptop. Escalated to ISP. Which of the following BEST describes what the technician was doing?",
  "options": [
    "The technician was questioning the obvious.",
    "The technician was implementing preventative measures.",
    "The technician was approaching multiple problems individually.",
    "The technician was determining if anything had changed."
  ],
  "correct_answer": 3,
  "description": "The correct answer is 'The technician was approaching multiple problems individually.' The technician addressed each issue separately, diagnosing and resolving one problem at a time. \n\n- Questioning the obvious would involve re-examining obvious solutions or causes, but this technician was methodical in isolating each problem. \n- Implementing preventative measures is not evident in this scenario, as the technician is only troubleshooting the current issues. \n- Determining if anything had changed is not explicitly mentioned in the ticket; the technician focused on troubleshooting the problems."
},
{
  "question": "Which of the following routing protocols should be implemented to create a route between a local area network and an ISP?",
  "options": [
    "BGP",
    "EIGRP",
    "RIP",
    "OSPF"
  ],
  "correct_answer": 1,
  "description": "The correct answer is 'BGP.' Border Gateway Protocol (BGP) is the most suitable routing protocol for connecting a local area network to an ISP, as it is designed to handle routing between different autonomous systems. \n\n- EIGRP, RIP, and OSPF are interior gateway protocols used within a single organization’s network, but they are not typically used for routing between an ISP and a local network."
},
{
  "question": "A technician would like to implement a low-latency Wi-Fi network. Which of the following standards should the technician deploy for the network if the expected user bandwidth is 450Mbps?",
  "options": [
    "802.11a",
    "802.11b",
    "802.11g",
    "802.11n"
  ],
  "correct_answer": 4,
  "description": "The correct answer is '802.11n.' This Wi-Fi standard supports higher data rates and offers lower latency compared to the older standards. It also supports 450Mbps bandwidth. \n\n- 802.11a, 802.11b, and 802.11g offer lower speeds and higher latencies compared to 802.11n, making them unsuitable for the required bandwidth."
},
{
  "question": "Which of the following attacks, if successful, would provide a malicious user who is connected to an isolated guest network access to the corporate network?",
  "options": [
    "VLAN hopping",
    "On-path attack",
    "IP spoofing",
    "Evil twin"
  ],
  "correct_answer": 1,
  "description": "The correct answer is 'VLAN hopping.' This attack allows a malicious user to bypass network segmentation and access other VLANs, including the corporate network. \n\n- On-path attacks (previously known as man-in-the-middle) require intercepting communication but do not directly lead to unauthorized access to another network. \n- IP spoofing is typically used to impersonate another system but does not inherently allow access to isolated networks. \n- Evil twin attacks involve creating a fake access point, but they don't bypass VLANs to access the corporate network."
},


  {
    "question": "A network administrator implements a group of access points, only changing the SSID, credentials, and IP address. Shortly after, users begin reporting poor quality and video loss while on video calls in the conference room. Which of the following should the administrator do to MOST effectively troubleshoot during business hours?",
    "options": [
      "Remove the current antennas and replace them with directional antennas on each AP.",
      "Disconnect the AP and move it closer to the conference room.",
      "Configure separate channels on APs that are not supporting the conference room.",
      "Reboot the switch and each AP at the same time."
    ],
    "correct_answer": 3,
    "description": "The correct answer is 'Configure separate channels on APs that are not supporting the conference room.' \n\n- Moving the AP closer may improve signal strength but doesn’t address the underlying issue of channel interference, which can be the main cause of video loss. \n- Replacing antennas is a good approach for targeted coverage but doesn't resolve interference from other APs. \n- Rebooting the switch and APs doesn’t directly address the root cause and could lead to temporary downtime without fixing the issue."
  },
  {
    "question": "A desktop support department has observed slow wireless speeds for a new line of laptops using the organization's standard image. No other devices have experienced the same issue. Which of the following should the network administrator recommend troubleshooting FIRST to resolve this issue?",
    "options": [
      "Increasing wireless signal power",
      "Installing a new WAP",
      "Changing the protocol associated to the SSID",
      "Updating the device wireless drivers"
    ],
    "correct_answer": 4,
    "description": "The correct answer is 'Updating the device wireless drivers.' \n\n- The issue is specific to new laptops, suggesting that drivers may be outdated or incompatible with the current network setup. \n- Increasing signal power or installing a new WAP might be unnecessary, as no other devices are having issues. \n- Changing the protocol associated with the SSID may not resolve issues tied to device compatibility."
  },
  {
    "question": "A technician needs to change an incoming fiber line into an RJ45 copper connection for uplinking a new switch. Which of the following would BEST satisfy this requirement?",
    "options": [
      "Media converter",
      "F-type connector",
      "Small form-factor pluggable",
      "Punchdown block"
    ],
    "correct_answer": 1,
    "description": "The correct answer is 'Media converter.' \n\n- A media converter is specifically designed to convert signals between different media types, such as fiber to copper (RJ45). \n- F-type connectors are used for coaxial cables, not for fiber or copper Ethernet connections. \n- Small form-factor pluggable (SFP) modules are used for fiber optic transceivers and would not convert a fiber line to RJ45. \n- Punchdown blocks are used for terminating cables but do not perform signal conversion."
  },
  {
    "question": "A new engineer at a company is working to understand the network. Which of the following diagrams should the engineer review to understand the paths traffic takes?",
    "options": [
      "Physical",
      "Logical",
      "Wiring",
      "Rack"
    ],
    "correct_answer": 2,
    "description": "The correct answer is 'Logical.' \n\n- A logical diagram shows the flow of data and network paths, which is essential for understanding how traffic moves through the network. \n- Physical diagrams show the physical layout, which is helpful for installation but doesn’t focus on traffic flow. \n- Wiring diagrams show cable connections but lack details about data routing. \n- Rack diagrams represent the physical placement of devices but don’t show traffic paths."
  },
  {
    "question": "A network technician is attempting to increase throughput by configuring link port aggregation between a Gigabit Ethernet distribution switch and a Fast Ethernet access switch. Which of the following is the BEST choice concerning speed and duplex for all interfaces that are participating in the link aggregation?",
    "options": [
      "Half duplex and 1GB speed",
      "Full duplex and 1GB speed",
      "Half duplex and 100MB speed",
      "Full duplex and 100MB speed"
    ],
    "correct_answer": 2,
    "description": "The correct answer is 'Full duplex and 1GB speed.' \n\n- For link aggregation, the interfaces should operate at the highest speed and duplex settings to maximize throughput. Full duplex allows simultaneous send and receive, improving performance. \n- Half duplex would limit the effective throughput, while 100MB speed would not provide sufficient bandwidth for link aggregation."
  },
  {
    "question": "A junior network engineer is trying to change the native network ID to a non-default value that can then be applied consistently throughout the network environment. Which of the following issues is the engineer attempting to prevent?",
    "options": [
      "DDoS",
      "ARP spoofing",
      "VLAN hopping",
      "Rogue DHCP"
    ],
    "correct_answer": 3,
    "description": "The correct answer is 'VLAN hopping.' \n\n- Changing the native VLAN ID prevents attackers from exploiting default configurations to perform VLAN hopping, a technique that allows an attacker to gain access to multiple VLANs. \n- DDoS, ARP spoofing, and rogue DHCP attacks do not rely on the native VLAN configuration."
  },
  {
    "question": "Which of the following BEST prevents unauthorized access to spare workstation inventory?",
    "options": [
      "Asset tags",
      "Tamper detection",
      "Security camera",
      "Locking cabinet",
      "Smart lockers"
    ],
    "correct_answer": 4,
    "description": "The correct answer is 'Locking cabinet.' \n\n- A locking cabinet provides physical security and restricts unauthorized access to spare workstations. \n- While asset tags and tamper detection help track and detect theft, they do not prevent access to the inventory itself. \n- Security cameras are useful for monitoring but do not physically secure the inventory. \n- Smart lockers offer good security but are more suitable for individual use rather than securing a large number of workstations."
  },
  {
    "question": "A technician is troubleshooting network connectivity from a wall jack. Readings from a multimeter indicate extremely low ohmic values instead of the rated impedance from the switchport. Which of the following is the MOST likely cause of this issue?",
    "options": [
      "Incorrect transceivers",
      "Faulty LED",
      "Short circuit",
      "Upgraded OS version on switch"
    ],
    "correct_answer": 3,
    "description": "The correct answer is 'Short circuit.' \n\n- A short circuit in the cabling can cause low resistance, leading to abnormal multimeter readings and network connectivity issues. \n- Incorrect transceivers would affect the signal transmission, not impedance readings. \n- Faulty LEDs are indicators for status but do not impact network connectivity. \n- An upgraded OS version on the switch would not cause impedance problems at the wall jack."
  },


  {
    "question": "A user is experimenting with audio transmissions and would like the transmissions to reach several specific devices simultaneously over the IP network. The user requests assistance from a network technician to configure the appropriate features within the SOHO. Which of the following should the technician configure to meet the requirements?",
    "options": [
      "Unicast",
      "Multicast",
      "Anycast",
      "Broadcast"
    ],
    "correct_answer": 2,
    "description": "The correct answer is multicast. Multicast allows audio transmissions to be sent to multiple specific devices at once over the network. \n\n- Unicast transmits data to a single device, which does not meet the requirement. \n- Anycast allows data to be routed to the nearest device but is not intended for simultaneous delivery to multiple devices. \n- Broadcast sends data to all devices on the network, which is inefficient compared to multicast for targeting specific devices."
  },
  {
    "question": "A retail store recently acquired the store next door. The owners would like this store to support Gigabit Ethernet for up to 328ft (100m). Which of the following is the MOST cost-effective solution?",
    "options": [
      "Cat5",
      "Cat 5e",
      "Cat 6",
      "Cat 7"
    ],
    "correct_answer": 2,
    "description": "The correct answer is Cat 5e. Cat 5e is capable of supporting Gigabit Ethernet speeds over a distance of up to 328ft (100m), and it offers a cost-effective solution compared to higher-category cables. \n\n- Cat 5 is outdated and may not provide reliable Gigabit speeds over the full distance. \n- Cat 6 and Cat 7 offer higher performance, but they are more expensive and overkill for the requirements."
  },
  {
    "question": "Which of the following attacks becomes more effective because of global leakages of users’ passwords?",
    "options": [
      "Dictionary",
      "Brute-force",
      "Phishing",
      "Deauthentication"
    ],
    "correct_answer": 1,
    "description": "The correct answer is dictionary. Dictionary attacks involve trying common words and phrases, often sourced from databases of leaked passwords. The more passwords that are leaked globally, the more effective dictionary attacks become. \n\n- Brute-force attacks try all possible combinations and are generally slower but can be effective on weak passwords. \n- Phishing exploits user behavior to gather sensitive information, which is a separate issue from password leaks. \n- Deauthentication is a network attack and is unrelated to password leakage."
  },
  {
    "question": "A network administration team for a medium-sized business has decided to segment the network, logically separating the finance and marketing teams in order to improve performance for both teams. The finance and marketing teams still need to access resources across the subnets, and the router has a single interface. Which of the following should the administrator configure in order to allow the traffic?",
    "options": [
      "Port address translation",
      "Classless masking",
      "IPv6 tunneling",
      "Subinterfaces"
    ],
    "correct_answer": 4,
    "description": "The correct answer is subinterfaces. Subinterfaces allow a single physical interface on the router to be divided into multiple logical interfaces, enabling the communication between the finance and marketing subnets. \n\n- Port address translation (PAT) is used for translating IP addresses and does not facilitate routing between subnets. \n- Classless masking refers to the use of CIDR (Classless Inter-Domain Routing) but does not directly address inter-subnet communication. \n- IPv6 tunneling is used to transmit IPv6 traffic over IPv4 networks and is unrelated to the issue."
  },
  {
    "question": "A network requirement calls for the network traffic of a specific department within a campus network to be monitored. The network has users from each department located in multiple buildings. Which of the following should be configured to meet this requirement? (Choose two.)",
    "options": [
      "MDIX",
      "802.1Q",
      "Jumbo frames",
      "Port mirroring",
      "Flow control",
      "LACP"
    ],
    "correct_answer": [4, 2],
    "description": "The correct answers are port mirroring and 802.1Q. \n\n- Port mirroring allows a copy of network traffic to be sent to a monitoring device for analysis. This is critical for monitoring specific departmental traffic. \n- 802.1Q allows for VLAN tagging, enabling traffic to be segregated by department, even if they are on different physical locations, which is important for isolating the department's traffic. \n\n- MDIX (Media Dependent Interface Crossover) handles cable type (crossover or straight-through) and is unrelated to traffic monitoring. \n- Jumbo frames refer to larger Ethernet frames, which are not related to traffic monitoring. \n- Flow control manages network congestion but does not address monitoring needs. \n- LACP (Link Aggregation Control Protocol) is for combining multiple network links into one, not for monitoring traffic."
  },




    {
        "question": "Link-local IPv6 address    fe80::28e4:a7cc:a55e:4bea\nIPv4 address     192.168.8.105\nSubnet mask      255.255.255.128\nDefault gateway        192.168.8.1\n\nWhich of the following configurations on the PC is incorrect?",
        "options": [
            "Subnet mask",
            "IPv4 address",
            "Default gateway",
            "IPv6 address"
        ],
        "correct_answer": 1,
        "description": "The correct answer is IPv4 address. The IPv4 address is within the range of the subnet mask (255.255.255.128), but it is incorrectly placed outside the valid range for that subnet. \n\n- The subnet mask is correct as it allows for 128 subnets. \n- The default gateway is correct as it falls within the same subnet. \n- The IPv6 address is valid as a link-local address, so it is not the issue."
    },
    {
        "question": "Which of the following layers of the OSI model lies between the transport layer and the network layer?",
        "options": [
            "Application",
            "Data link",
            "Session",
            "Presentation"
        ],
        "correct_answer": 3,
        "description": "The correct answer is Session. The session layer is responsible for managing sessions between devices, while the transport layer manages end-to-end communication, and the network layer handles routing. \n\n- The Application layer is at the top of the OSI model. \n- The Data link layer is beneath the network layer. \n- The Presentation layer deals with data format translation."
    },
    {
        "question": "Which of the following describes a network in which users and devices need to mutually authenticate before any network resource can be accessed?",
        "options": [
            "Least privilege",
            "Local authentication",
            "Zero trust",
            "Need to know"
        ],
        "correct_answer": 3,
        "description": "The correct answer is Zero trust. Zero trust security requires that all users and devices be authenticated, authorized, and continuously validated, regardless of their location. \n\n- Least privilege refers to granting minimal access based on user roles. \n- Local authentication is more about specific authentication methods within a local system. \n- Need to know pertains to restricting access based on necessity rather than authentication."
    },
    {
        "question": "A technician is setting up DNS records on local servers for the company's cloud DNS to enable access by hostname. Which of the following records should be used?",
        "options": [
            "A",
            "MX",
            "CNAME",
            "NS"
        ],
        "correct_answer": 1,
        "description": "The correct answer is A. The A (Address) record maps a hostname to an IPv4 address, allowing access by hostname. \n\n- MX records are used for mail exchange purposes. \n- CNAME is used for aliasing a domain name to another. \n- NS records define authoritative name servers for a domain."
    },
    {
        "question": "A network administrator responds to a support ticket that was submitted by a customer who is having issues connecting to a website inside of the company network. The administrator verifies that the customer could not connect to a website using a URL. Which of the following troubleshooting steps would be BEST for the administrator to take?",
        "options": [
            "Check for certificate issues.",
            "Contact the ISP.",
            "Attempt to connect to the site via IP address.",
            "Check the NTP configuration."
        ],
        "correct_answer": 3,
        "description": "The correct answer is Attempt to connect to the site via IP address. This will help determine if the issue is DNS resolution-related. \n\n- Checking for certificate issues is important for secure connections but unrelated to the URL access problem. \n- Contacting the ISP is only necessary if the issue is external. \n- NTP configuration issues would affect time synchronization, not web access."
    },
    {
        "question": "A network administrator is creating a subnet for a remote office that has 53 network devices. An additional requirement is to use the most efficient subnet. Which of the following CIDR notations indicates the appropriate number of IP addresses with the LEAST amount of unused addresses?",
        "options": [
            "/24",
            "/26",
            "/28",
            "/32"
        ],
        "correct_answer": 2,
        "description": "The correct answer is /26. A /26 subnet provides 64 IP addresses, which is the closest to the required 53 devices without excessive unused IP addresses. \n\n- /24 provides 256 IP addresses, which is overkill for only 53 devices. \n- /28 only provides 16 addresses, which is insufficient. \n- /32 provides only one address, which is inappropriate for subnetting."
    },
    {
        "question": "A Chief Executive Officer (CEO) of a company purchases a new phone that will be used while traveling to different countries. The CEO needs to be able to place outgoing calls and receive incoming calls on the phone using a SIM card. Which of the following cellular technologies does the CEO’s phone need?",
        "options": [
            "WDMA",
            "CDMA",
            "GSM",
            "SLA"
        ],
        "correct_answer": 3,
        "description": "The correct answer is GSM. GSM (Global System for Mobile Communications) is a widely used standard for mobile networks, supporting international roaming with SIM cards. \n\n- WDMA (Wideband Code Division Multiple Access) is a technology used for data transfer, not applicable here. \n- CDMA is a technology used in specific regions but lacks global compatibility. \n- SLA is not a recognized cellular technology."
    },



     {
        "question": "A network technician is troubleshooting a connection to a local server and has verified that the RDP service is running on the server. After running a command, the technician receives the following output:\n\nProto   Local Address      Foreign Address  State\nTCP    10.10.10.42:51421  10.10.10.7:3389  SYN_SENT\n\nWhich of the following MOST likely describes the issue?",
        "options": [
            "A host-based firewall on the server is blocking the connection.",
            "Too many collisions are occurring on the network segment.",
            "A DoS attack is occurring locally.",
            "A routing loop is in the network."
        ],
        "correct_answer": 1,
        "description": "The correct answer is 'A host-based firewall on the server is blocking the connection.' The SYN_SENT state indicates that the client is waiting for a response from the server but hasn't received one, which is likely caused by a firewall blocking the RDP port (3389).\n\n- Collisions typically result in data transmission errors, not a blocked connection.\n- A DoS attack would usually overwhelm the server, affecting all connections, not just one port.\n- A routing loop would cause network issues, but it wouldn't specifically block one connection type."
    },
    {
        "question": "Which of the following would be used to indicate when unauthorized access to physical internal hardware has occurred?",
        "options": [
            "Motion detectors",
            "Radio frequency identification tags",
            "Tamper evident seal",
            "Locking racks"
        ],
        "correct_answer": 3,
        "description": "The correct answer is 'Tamper evident seal.' Tamper-evident seals are designed to show clear signs of unauthorized access to internal hardware, making them useful for security and accountability.\n\n- Motion detectors detect movement but do not specifically indicate tampering with hardware.\n- Radio frequency identification (RFID) tags track items but do not show evidence of tampering.\n- Locking racks prevent unauthorized access but do not provide visible indicators of tampering."
    },
    {
        "question": "A network technician is investigating a trouble ticket for a user who does not have network connectivity. All patch cables between the wall jacks and computers in the building were upgraded over the weekend from Cat 5 to Cat 6. The newly installed cable is crimped with a TIA/EIA 568A on one end and a TIA/EIA 568B on the other end. Which of the following should the technician do to MOST likely fix the issue?",
        "options": [
            "Ensure the switchport has PoE enabled.",
            "Crimp the cable as a straight-through cable.",
            "Ensure the switchport has STP enabled.",
            "Crimp the cable as a rollover cable."
        ],
        "correct_answer": 2,
        "description": "The correct answer is 'Crimp the cable as a straight-through cable.' The issue is most likely caused by mismatched cable wiring standards. A straight-through cable should have the same TIA/EIA standard (either 568A or 568B) on both ends.\n\n- PoE (Power over Ethernet) is not the issue since it deals with power delivery, not connectivity.\n- STP (Shielded Twisted Pair) is used for noise reduction, not for fixing wiring mismatches.\n- A rollover cable is used for console connections, not for standard network connections."
    },
    {
        "question": "Which of the following is a valid alternative to maintain a deployed proxy technology while saving physical space in the data center by moving the network service to the virtualization infrastructure?",
        "options": [
            "NFV",
            "SDWAN",
            "Networking as code",
            "VIP"
        ],
        "correct_answer": 1,
        "description": "The correct answer is 'NFV' (Network Functions Virtualization). NFV allows network services like proxy servers to be virtualized, reducing the need for physical hardware and saving space in the data center.\n\n- SDWAN (Software-Defined Wide Area Network) is used for optimizing network performance across WAN connections, not for virtualization.\n- Networking as code refers to the automation of network configuration, not directly related to proxy deployment.\n- VIP (Virtual IP) is an IP address that is mapped to a set of network resources, not a method for virtualizing network services."
    },
    {
        "question": "A network technician wants to identify which DNS servers a computer is configured to use. Which of the following commands should the technician use?",
        "options": [
            "nbtstat",
            "arp",
            "nslookup",
            "netstat"
        ],
        "correct_answer": 3,
        "description": "The correct answer is 'nslookup.' The nslookup command is used to query DNS servers and can provide information about the configured DNS servers on the system.\n\n- nbtstat shows NetBIOS over TCP/IP information, not DNS server settings.\n- arp displays the Address Resolution Protocol table, which maps IP addresses to MAC addresses, not DNS server information.\n- netstat shows network connections and routing tables, not DNS settings."
    },
    {
        "question": "Which of the following routing protocols has routes that are classified with an administrative distance of 110?",
        "options": [
            "BGP",
            "OSPF",
            "EIGRP",
            "RIP"
        ],
        "correct_answer": 4,
        "description": "The correct answer is 'RIP' (Routing Information Protocol). RIP has an administrative distance of 110, which is used to determine the reliability of routes. A lower distance is more reliable.\n\n- BGP (Border Gateway Protocol) has a much higher administrative distance of 20 or 200.\n- OSPF (Open Shortest Path First) has an administrative distance of 110 but is more specific than RIP.\n- EIGRP (Enhanced Interior Gateway Routing Protocol) has a distance of 90, which is lower than RIP."
    },
    {
        "question": "Which of the following focuses on application delivery?",
        "options": [
            "DaaS",
            "IaaS",
            "SaaS",
            "PaaS"
        ],
        "correct_answer": 3,
        "description": "The correct answer is 'SaaS' (Software as a Service). SaaS delivers software applications over the internet, which is focused on application delivery.\n\n- DaaS (Desktop as a Service) provides virtual desktops, not application delivery.\n- IaaS (Infrastructure as a Service) provides infrastructure resources but not applications.\n- PaaS (Platform as a Service) provides a platform for developers but is not focused on delivering end-user applications."
    },
    {
        "question": "A network engineer is concerned about VLAN hopping happening on the network. Which of the following should the engineer do to address this concern?",
        "options": [
            "Configure private VLANs.",
            "Change the default VLAN.",
            "Implement ACLs on the VLAN.",
            "Enable dynamic ARP inspection."
        ],
        "correct_answer": 1,
        "description": "The correct answer is 'Configure private VLANs.' Private VLANs prevent VLAN hopping by isolating devices within a VLAN, enhancing security.\n\n- Changing the default VLAN does not prevent VLAN hopping.\n- ACLs (Access Control Lists) can control traffic but do not directly prevent VLAN hopping.\n- Dynamic ARP inspection protects against ARP spoofing but does not prevent VLAN hopping."
    },
    {
        "question": "A network technician receives a support ticket concerning multiple users who are unable to access the company's shared drive. The switch interface that the shared drive is connected to is displaying the following:\n\nGigabitEthernet0/9 is down, line protocol is down (notconnect)\nHardware is Gigabit Ethernet, address is c800.84bf.9847 (via c800.84bf.9847)\nMTU 1500 bytes, BW 10000 Kbit/sec, DLY 1000 usec,\nreliability 255/255, txload 1/255, rxload 1/255\nEncapsulation ARPA, loopback not set\n\nWhich of the following is MOST likely the issue?",
        "options": [
            "The switchport is shut down.",
            "The cable is not plugged in.",
            "The loopback is not set.",
            "The bandwidth configuration is incorrect."
        ],
        "correct_answer": 2,
        "description": "The correct answer is 'The cable is not plugged in.' The interface being 'down' and 'line protocol is down' indicates a physical connection issue, most likely due to the cable not being plugged in.\n\n- If the switchport were shut down, it would show 'administratively down' rather than 'line protocol is down.'\n- The loopback setting is not related to physical connectivity.\n- Bandwidth configuration errors would affect performance but would not cause the interface to be down."
    },
    {
        "question": "A customer calls the help desk to report that users are unable to access any network resources. The issue started earlier in the day when an employee rearranged the wiring closet. A technician goes to the site but does not observe any obvious damage. The statistics output on the switch indicates high CPU usage, and all the lights on the switch are blinking rapidly in unison. Which of the following is the MOST likely explanation for these symptoms?",
        "options": [
            "The switch was rebooted and set to run in safe mode.",
            "The line between the switch and the upstream router was removed.",
            "A cable was looped and created a broadcast storm.",
            "A Cat 6 cable from the modem to the router was replaced with Cat 5e."
        ],
        "correct_answer": 3,
        "description": "The correct answer is 'A cable was looped and created a broadcast storm.' A loop in the network can cause broadcast storms, which overwhelm the switch and cause high CPU usage and rapid blinking lights.\n\n- Safe mode would not explain the rapid blinking or CPU usage.\n- Removing the connection to the router would lead to network outages, but not the symptoms described.\n- Replacing the cable would cause a connectivity issue, but not the broadcast storm symptoms."
    },



    {
        "question": "A network administrator is troubleshooting a PC that cannot connect to the LAN. The administrator runs the ipconfig command at the command prompt and gets the following output:\n\nEthernet Adapter:\nPhysical Address: AB-CD-EF-12-34-56\nDHCP Enabled: No\nIPv4 Address: 192.168.1.55\nSubnet Mask: 225.225.225.224\nDefault Gateway: 192.168.1.1\nDHCP Server: 192.168.1.1\nDNS Server: 192.168.1.1\n\nWhich of the following is misconfigured?",
        "options": [
            "Subnet mask",
            "Physical address",
            "DNS server",
            "DHCP server"
        ],
        "correct_answer": 1,
        "description": "The correct answer is 'Subnet mask'. The subnet mask 225.225.225.224 is incorrectly configured for this network. The correct subnet mask for this configuration should be 255.255.255.0 or another appropriate subnet mask for the network. \n\n- The physical address is a unique identifier for the network adapter and does not affect connectivity directly. \n- The DNS server and DHCP server configurations seem correct as per the output."
    },
    {
        "question": "A user stores large graphic files. The time required to transfer the files to the server is excessive due to network congestion. The user's budget does not allow for the current switches to be replaced. Which of the following can be used to provide FASTER transfer times?",
        "options": [
            "Half duplex",
            "Jumbo frames",
            "LACP",
            "802.1Q"
        ],
        "correct_answer": 2,
        "description": "The correct answer is 'Jumbo frames'. Jumbo frames increase the maximum transmission unit (MTU) size, allowing larger packets to be sent over the network, improving the speed of large file transfers. \n\n- Half duplex could reduce the network speed due to collision risks. \n- LACP (Link Aggregation Control Protocol) is used for combining multiple network links, but this may not be a feasible option in this situation. \n- 802.1Q is used for VLAN tagging, which does not directly impact file transfer speed."
    },
    {
        "question": "A sales team at a company uses a SaaS solution primarily for videoconferencing and a CRM application that connects to a database server in the corporate data center. Which of the following VPN solutions would allow secure, remote access for sales staff to the CRM application without impacting videoconferencing traffic?",
        "options": [
            "Clientless",
            "Site-to-site",
            "Split tunnel",
            "Full tunnel"
        ],
        "correct_answer": 3,
        "description": "The correct answer is 'Split tunnel'. A split tunnel VPN allows remote users to access specific resources (like the CRM application) securely while leaving other traffic, such as videoconferencing, unaffected by the VPN. \n\n- Clientless VPN does not require software installation but may not offer granular control over traffic. \n- Site-to-site VPN connects entire networks and would not help in securing individual remote users' access to resources. \n- Full tunnel routes all traffic through the VPN, which could impact videoconferencing performance."
    },
    {
        "question": "Which of the following would a network administrator configure to set NTP settings for a specific subnet within DHCP?",
        "options": [
            "Reservation",
            "Lease time",
            "Scope options",
            "Exclusion range"
        ],
        "correct_answer": 3,
        "description": "The correct answer is 'Scope options'. Scope options in DHCP allow an administrator to configure settings like NTP servers for a specific subnet. \n\n- Reservation is used to allocate a specific IP address to a device. \n- Lease time determines how long an IP address is assigned to a device but does not affect NTP settings. \n- Exclusion range is used to prevent certain IP addresses from being assigned but is unrelated to NTP configuration."
    },
    {
        "question": "A network administrator creates a new network, 10.10.0.0/24, on a DHCP server. The administrator wants to ensure that 10.10.0.10-10.10.0.15 are not allocated to other devices. Which of the following features should the administrator configure?",
        "options": [
            "Exclusion",
            "Reservation",
            "Scope",
            "Relay"
        ],
        "correct_answer": 1,
        "description": "The correct answer is 'Exclusion'. Exclusion prevents certain IP addresses within the scope from being assigned by DHCP, which is what the administrator needs to avoid allocating 10.10.0.10-10.10.0.15 to other devices. \n\n- Reservation is used for assigning specific IP addresses to known devices but is not used for preventing allocation. \n- Scope defines the range of IP addresses available for assignment. \n- Relay is used to forward DHCP requests between clients and servers."
    },
    {
        "question": "Which of the following protocols uses Dijkstra's algorithm to calculate the LOWEST cost between routers?",
        "options": [
            "RIP",
            "OSPF",
            "BGP",
            "EIGRP"
        ],
        "correct_answer": 2,
        "description": "The correct answer is 'OSPF'. OSPF (Open Shortest Path First) uses Dijkstra's algorithm to calculate the shortest path based on the lowest cost between routers. \n\n- RIP (Routing Information Protocol) uses hop count, not Dijkstra's algorithm. \n- BGP (Border Gateway Protocol) is a path vector protocol and does not use Dijkstra's algorithm. \n- EIGRP (Enhanced Interior Gateway Routing Protocol) uses Diffusing Update Algorithm (DUAL), not Dijkstra's."
    },
    {
        "question": "An on-call network technician receives an automated email alert stating that a power supply on a firewall has just powered down. Which of the following protocols would BEST allow for this level of detailed device monitoring?",
        "options": [
            "TFTP",
            "TLS",
            "SSL",
            "SNMP"
        ],
        "correct_answer": 4,
        "description": "The correct answer is 'SNMP'. SNMP (Simple Network Management Protocol) is used for monitoring and managing network devices, including providing detailed information on hardware status like power supplies. \n\n- TFTP (Trivial File Transfer Protocol) is used for transferring files and is not intended for monitoring. \n- TLS and SSL are security protocols used for encrypting communications, not for monitoring devices."
    },
    {
        "question": "A technician is investigating a SAN switch that has a high number of CRC errors. Which of the following is the MOST likely cause of the errors?",
        "options": [
            "Break in the fiber",
            "Bad switch port",
            "Mismatched duplex",
            "Memory errors"
        ],
        "correct_answer": 1,
        "description": "The correct answer is 'Break in the fiber'. CRC errors in a SAN (Storage Area Network) are often caused by physical issues with the fiber connection, such as a break or damage. \n\n- A bad switch port could also cause errors but is less likely compared to fiber issues. \n- Mismatched duplex and memory errors are less likely to cause CRC errors in this context."
    },
    {
        "question": "A customer runs a DNS lookup service and needs a network technician to reconfigure the network to improve performance. The customer wants to ensure that servers are accessed based on whichever one is topographically closest to the destination. If the server does not respond, then the next topographically closest server should respond. Which of the following does the technician need to configure to meet the requirements?",
        "options": [
            "Multicast addressing",
            "Anycast addressing",
            "Broadcast addressing",
            "Unicast addressing"
        ],
        "correct_answer": 2,
        "description": "The correct answer is 'Anycast addressing'. Anycast allows data to be routed to the nearest server based on topology, ensuring that the closest server responds. \n\n- Multicast, broadcast, and unicast addressing are not designed to provide the desired behavior of routing to the nearest server."
    },
    {
        "question": "Which of the following would MOST likely be used to review disaster recovery information for a system?",
        "options": [
            "Business continuity plan",
            "Change management",
            "System life cycle",
            "Standard operating procedures"
        ],
        "correct_answer": 1,
        "description": "The correct answer is 'Business continuity plan'. A business continuity plan outlines how an organization will recover from disasters, including information related to disaster recovery. \n\n- Change management focuses on managing changes in systems, not disaster recovery. \n- The system life cycle involves stages of a system’s existence, while standard operating procedures are focused on routine processes."
    },
    {
        "question": "A network technician is troubleshooting a connection to a web server. The technician is unable to ping the server but is able to verify connectivity to the web service using Telnet. Which of the following protocols is being blocked by the firewall?",
        "options": [
            "UDP",
            "ARP",
            "ICMP",
            "TCP"
        ],
        "correct_answer": 3,
        "description": "The correct answer is 'ICMP'. ICMP (Internet Control Message Protocol) is used for pinging, and if a ping fails but Telnet works, it indicates that ICMP traffic is being blocked by the firewall. \n\n- ARP is used for mapping IP addresses to MAC addresses and does not directly affect ping or Telnet. \n- UDP and TCP protocols are related to transport-layer communication, which is unaffected in this case since Telnet works."
    },





    {
        "question": "A network administrator is configuring a firewall to allow for a new cloud-based email server. The company standard is to use SMTP to route email traffic. Which of the following ports, by default, should be reserved for this purpose?",
        "options": [
            "23",
            "25",
            "53",
            "110"
        ],
        "correct_answer": 2,
        "description": "The correct answer is port 25. SMTP (Simple Mail Transfer Protocol) uses port 25 by default to route email traffic. \n\n- Port 23 is used by Telnet, a protocol for command-line interface access. \n- Port 53 is used by DNS for resolving domain names. \n- Port 110 is used by POP3 for retrieving email, not for sending it."
    },
    {
        "question": "Which of the following demarcation connections would be MOST appropriate to use with a cable modem being installed in a SOHO situation?",
        "options": [
            "RG6",
            "Cat 6",
            "RJ11",
            "Multimode fiber"
        ],
        "correct_answer": 1,
        "description": "The correct answer is RG6. RG6 is a coaxial cable commonly used in cable modem installations, as it is designed to handle higher frequencies and provide better signal quality. \n\n- Cat 6 is used for Ethernet networking, not for cable modem connections. \n- RJ11 is used for telephone lines, not broadband data. \n- Multimode fiber is typically used for high-speed networking over longer distances and is not needed for SOHO cable modem setups."
    },
    {
        "question": "A technician needs to allow a device to maintain the same IP address lease based on the physical address of a network card. Which of the following should the technician use?",
        "options": [
            "MAC address reservation",
            "Static IP address",
            "Custom DNS server entry",
            "IP address exclusion"
        ],
        "correct_answer": 1,
        "description": "The correct answer is MAC address reservation. This allows the device to always receive the same IP address from the DHCP server by associating it with the device's MAC address. \n\n- A static IP address manually configures an IP but does not involve the DHCP process. \n- Custom DNS server entries deal with domain name resolution, not IP address assignment. \n- IP address exclusion prevents certain IPs from being assigned by DHCP, but it doesn't ensure the same IP for a device."
    },
    {
        "question": "A network technician is investigating why a core switch is logging excessive amounts of data to the syslog server. The running configuration of the switch showed the following logging information:\n\nip ssh logging events\nlogging level debugging\nlogging host 192.168.1.100\nlogging synchronous\n\nWhich of the following changes should the technician make to BEST fix the issue?",
        "options": [
            "Update the logging host IP.",
            "Change to asynchronous logging.",
            "Stop logging SSH events.",
            "Adjust the logging level."
        ],
        "correct_answer": 4,
        "description": "The correct answer is to adjust the logging level. The 'debugging' level is very detailed and can produce excessive log data. Changing it to a less verbose level (such as 'informational') would reduce the log volume. \n\n- Updating the logging host IP won't address the excessive logging itself. \n- Asynchronous logging would not solve the problem, as it does not impact the verbosity of the logs. \n- Stopping SSH event logging could reduce the data, but this may not be desirable, as monitoring SSH events is important for security."
    },
    {
        "question": "A network technician wants to find the shortest path from one node to every other node in the network. Which of the following algorithms will provide the FASTEST convergence time?",
        "options": [
            "A static algorithm",
            "A link-state algorithm",
            "A distance-vector algorithm",
            "A path-vector algorithm"
        ],
        "correct_answer": 2,
        "description": "The correct answer is a link-state algorithm. Link-state algorithms, such as OSPF, provide faster convergence times as they exchange detailed information about the network's state and compute the shortest path more quickly. \n\n- A static algorithm is not dynamic and does not adjust to network changes, making it slower to converge. \n- A distance-vector algorithm, such as RIP, converges more slowly compared to link-state algorithms because it relies on periodic updates. \n- A path-vector algorithm, like BGP, is used for inter-domain routing and has slower convergence times compared to link-state algorithms."
    },
    {
        "question": "After upgrading to a SOHO router that supports Wi-Fi 6, the user determines throughput has not increased. Which of the following is the MOST likely cause of the issue?",
        "options": [
            "The wireless router is using an incorrect antenna type.",
            "The user's workstation does not support 802.11ax.",
            "The encryption protocol is mismatched.",
            "The network is experiencing interference."
        ],
        "correct_answer": 2,
        "description": "The correct answer is that the user's workstation does not support 802.11ax. For Wi-Fi 6 (802.11ax) to provide improved throughput, both the router and the connected devices must support this standard. \n\n- The antenna type could affect performance, but it is less likely to be the main issue when Wi-Fi 6 compatibility is not present on the client device. \n- Encryption mismatches might cause connection issues, but they are less likely to result in throughput problems. \n- Network interference can affect speeds, but if the device does not support Wi-Fi 6, it will not benefit from the router's improved throughput capabilities."
    },



    {
        "question": "A network administrator is configuring a firewall to allow for a new cloud-based email server. The company standard is to use SMTP to route email traffic. Which of the following ports, by default, should be reserved for this purpose?",
        "options": [
            "23",
            "25",
            "53",
            "110"
        ],
        "correct_answer": 2,
        "description": "The correct answer is port 25. Port 25 is the default port used for SMTP, which is responsible for sending email messages. \n\n- Port 23 is used for Telnet, a less secure remote access protocol. \n- Port 53 is used for DNS, which handles domain name resolution, not email traffic. \n- Port 110 is used for POP3, a protocol for receiving email, not for sending it."
    },
    {
        "question": "Which of the following demarcation connections would be MOST appropriate to use with a cable modem being installed in a SOHO situation?",
        "options": [
            "RG6",
            "Cat 6",
            "RJ11",
            "Multimode fiber"
        ],
        "correct_answer": 1,
        "description": "The correct answer is RG6. RG6 is the most appropriate coaxial cable for cable modem connections, commonly used in residential and small office environments. \n\n- Cat 6 is used for Ethernet connections, not for cable modem connections. \n- RJ11 is used for telephone lines and would not provide the bandwidth needed for a cable modem. \n- Multimode fiber is typically used for high-speed connections in enterprise environments, not for cable modem setups."
    },
    {
        "question": "A technician needs to allow a device to maintain the same IP address lease based on the physical address of a network card. Which of the following should the technician use?",
        "options": [
            "MAC address reservation",
            "Static IP address",
            "Custom DNS server entry",
            "IP address exclusion"
        ],
        "correct_answer": 1,
        "description": "The correct answer is MAC address reservation. By reserving an IP address for a specific MAC address, the technician ensures that the device always gets the same IP address from the DHCP server. \n\n- A static IP address is manually assigned, but MAC address reservation allows DHCP to automatically assign the same IP. \n- Custom DNS server entries and IP address exclusions are unrelated to maintaining the same IP address lease for a device."
    },
    {
        "question": "A network technician is investigating why a core switch is logging excessive amounts of data to the syslog server. The running configuration of the switch showed the following logging information:\n\nip ssh logging events\nlogging level debugging\nlogging host 192.168.1.100\nlogging synchronous\n\nWhich of the following changes should the technician make to BEST fix the issue?",
        "options": [
            "Update the logging host IP.",
            "Change to asynchronous logging.",
            "Stop logging SSH events.",
            "Adjust the logging level."
        ],
        "correct_answer": 4,
        "description": "The correct answer is to adjust the logging level. The 'debugging' level is very verbose and can generate excessive log data. Changing it to a less detailed level, such as 'informational' or 'warning,' would reduce the volume of logs. \n\n- Updating the logging host IP would not address the issue of excessive logging. \n- Asynchronous logging does not address the verbosity of log data. \n- Stopping logging SSH events would only address one part of the issue, but adjusting the overall logging level is the more effective solution."
    },
    {
        "question": "A network technician wants to find the shortest path from one node to every other node in the network. Which of the following algorithms will provide the FASTEST convergence time?",
        "options": [
            "A static algorithm",
            "A link-state algorithm",
            "A distance-vector algorithm",
            "A path-vector algorithm"
        ],
        "correct_answer": 2,
        "description": "The correct answer is a link-state algorithm. Link-state algorithms, like OSPF, offer fast convergence times because they allow routers to dynamically learn about the entire network and adjust routing tables more efficiently. \n\n- A static algorithm does not adjust dynamically, leading to slower convergence times. \n- Distance-vector algorithms (e.g., RIP) are slower to converge due to periodic updates and less efficient path selection. \n- Path-vector algorithms (used in BGP) are used in different contexts and are not optimized for fast convergence within a single network."
    },
    {
        "question": "After upgrading to a SOHO router that supports Wi-Fi 6, the user determines throughput has not increased. Which of the following is the MOST likely cause of the issue?",
        "options": [
            "The wireless router is using an incorrect antenna type.",
            "The user's workstation does not support 802.11ax.",
            "The encryption protocol is mismatched.",
            "The network is experiencing interference."
        ],
        "correct_answer": 2,
        "description": "The correct answer is that the user's workstation does not support 802.11ax. If the workstation does not support Wi-Fi 6 (802.11ax), it will not be able to take advantage of the increased throughput provided by the router. \n\n- Incorrect antenna types could impact signal strength but would not account for the lack of increased throughput. \n- Mismatched encryption protocols could cause connectivity issues but would not directly affect throughput. \n- Network interference could slow speeds, but the issue here is likely compatibility with Wi-Fi 6 rather than interference."
    },






]
