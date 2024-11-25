questions_set_A = [

#1 - 40

    {
        "question": "A systems administrator needs to improve WiFi performance in a densely populated office tower and use the latest standard. There is a mix of devices that use 2.4 GHz and 5 GHz. Which of the following should the systems administrator select to meet this requirement?",
        "options": [
            "802.11ac",
            "802.11ax",
            "802.11g",
            "802.11n"
        ],
        "correct_answer": 2,
        "description": "The correct answer is 802.11ax. This standard, also known as Wi-Fi 6, offers improved performance, supports both 2.4 GHz and 5 GHz bands, and is designed for dense environments with multiple devices. \n\n- 802.11ac supports only the 5 GHz band, limiting its compatibility. \n- 802.11g is outdated and supports only the 2.4 GHz band. \n- 802.11n supports both bands but lacks the latest performance and efficiency improvements of 802.11ax."
    },
    {
        "question": "Which of the following would be BEST to use to detect a MAC spoofing attack?",
        "options": [
            "Internet Control Message Protocol",
            "Reverse Address Resolution Protocol",
            "Dynamic Host Configuration Protocol",
            "Internet Message Access Protocol"
        ],
        "correct_answer": 2,
        "description": "The correct answer is Reverse Address Resolution Protocol (RARP). This protocol helps map MAC addresses to IP addresses, which can assist in identifying inconsistencies caused by MAC spoofing. \n\n- ICMP is used for network diagnostics, not detecting MAC spoofing. \n- DHCP assigns IP addresses dynamically but does not directly detect spoofing. \n- IMAP is unrelated to network layer security."
    },
    {
        "question": "A technician receives feedback that some users are experiencing high amounts of jitter while using the wireless network. While troubleshooting the network, the technician uses the ping command with the IP address of the default gateway and verifies large variations in latency. The technician thinks the issue may be interference from other networks and non-802.11 devices. Which of the following tools should the technician use to troubleshoot the issue?",
        "options": [
            "NetFlow analyzer",
            "Bandwidth analyzer",
            "Protocol analyzer",
            "Spectrum analyzer"
        ],
        "correct_answer": 4,
        "description": "The correct answer is spectrum analyzer. This tool identifies sources of interference in the wireless spectrum, which can cause jitter and latency issues. \n\n- NetFlow analyzer focuses on network traffic patterns, not wireless interference. \n- Bandwidth analyzers measure data usage but do not detect wireless interference. \n- Protocol analyzers inspect packets but do not identify wireless interference."
    },
    {
        "question": "Wireless users are reporting intermittent internet connectivity. Connectivity is restored when the users disconnect and reconnect, utilizing the web authentication process each time. The network administrator can see the devices connected to the APs at all times. Which of the following steps will MOST likely determine the cause of the issue?",
        "options": [
            "Verify the session time-out configuration on the captive portal settings",
            "Check for encryption protocol mismatch on the client's wireless settings",
            "Confirm that a valid passphrase is being used during the web authentication",
            "Investigate for a client's disassociation caused by an evil twin AP"
        ],
        "correct_answer": 1,
        "description": "The correct answer is to verify the session time-out configuration on the captive portal settings. Misconfigured session timeouts can force users to reauthenticate frequently. \n\n- Encryption protocol mismatches typically prevent connection entirely, not intermittently. \n- A valid passphrase is necessary but unrelated to recurring session drops. \n- Evil twin AP attacks cause disconnections but would also require user action or rogue devices, which is not indicated here."
    },
    {
        "question": "A network administrator walks into a datacenter and notices an unknown person is following closely. The administrator stops and directs the person to the security desk. Which of the following attacks did the network administrator prevent?",
        "options": [
            "Evil twin",
            "Tailgating",
            "Piggybacking",
            "Shoulder surfing"
        ],
        "correct_answer": 2,
        "description": "The correct answer is tailgating. This is when an unauthorized individual gains physical access by closely following someone who is authorized. \n\n- Evil twin refers to creating a rogue access point, not physical access. \n- Piggybacking implies consent from the authorized person, which is not the case here. \n- Shoulder surfing involves spying on screens or documents, unrelated to physical entry."
    },
    {
        "question": "A network is experiencing a number of CRC errors during normal network communication. At which of the following layers of the OSI model will the administrator MOST likely start to troubleshoot?",
        "options": [
            "Layer 1",
            "Layer 2",
            "Layer 3",
            "Layer 4",
            "Layer 5",
            "Layer 6",
            "Layer 7"
        ],
        "correct_answer": 2,
        "description": "The correct answer is Layer 2. Cyclic Redundancy Check (CRC) errors occur at this layer, which involves data link integrity and error detection. \n\n- Layer 1 relates to physical connectivity but does not handle CRC. \n- Higher layers (3-7) are concerned with network, transport, and application-level issues, not low-level error detection."
    },
    {
        "question": "A client recently added 100 users who are using VMs. All users have since reported slow or unresponsive desktops. Reports show minimal network congestion, zero packet loss, and acceptable packet delay. Which of the following metrics will MOST accurately show the underlying performance issues? (Choose two.)",
        "options": [
            "CPU usage",
            "Memory",
            "Temperature",
            "Bandwidth",
            "Latency",
            "Jitter"
        ],
        "correct_answer": [1, 2],
        "description": "The correct answers are CPU usage and memory. These metrics indicate whether the server or host systems have sufficient resources to support the additional VMs. \n\n- Temperature is unrelated to performance unless overheating causes throttling. \n- Bandwidth, latency, and jitter are more relevant to network performance, which is not the reported issue."
    },
    {
        "question": "Client devices cannot enter a network, and the network administrator determines the DHCP scope is exhausted. The administrator wants to avoid creating a new DHCP pool. Which of the following can the administrator perform to resolve the issue?",
        "options": [
            "Install load balancers",
            "Install more switches",
            "Decrease the number of VLANs",
            "Reduce the lease time"
        ],
        "correct_answer": 4,
        "description": "The correct answer is to reduce the lease time. This increases the frequency at which unused IP addresses are reclaimed, freeing them up for new devices. \n\n- Load balancers, switches, and VLAN changes do not address DHCP exhaustion."
    },
    {
        "question": "An administrator is writing a script to periodically log the IPv6 and MAC addresses of all the devices on a network segment. Which of the following switch features will MOST likely be used to assist with this task?",
        "options": [
            "Spanning Tree Protocol",
            "Neighbor Discovery Protocol",
            "Link Aggregation Control Protocol",
            "Address Resolution Protocol"
        ],
        "correct_answer": 2,
        "description": "The correct answer is Neighbor Discovery Protocol (NDP). NDP is part of IPv6 and is used for discovering devices and their MAC addresses on a local network. \n\n- Spanning Tree Protocol prevents loops but does not log addresses. \n- LACP is used for link aggregation, not address discovery. \n- ARP is for IPv4 networks, not IPv6."
    },

    
    {
        "question": "Which of the following DNS records works as an alias to another record?",
        "options": [
            "AAAA",
            "CNAME",
            "MX",
            "SOA"
        ],
        "correct_answer": 2,
        "description": "The correct answer is CNAME. CNAME (Canonical Name) records allow one domain name to alias another, making it easier to redirect or manage domains. \n\n- AAAA records map a domain to an IPv6 address. \n- MX records specify mail servers responsible for receiving emails. \n- SOA records provide administrative information about a DNS zone."
    },
    {
        "question": "A company built a new building at its headquarters location. The new building is connected to the company's LAN via fiber-optic cable. Multiple users in the new building are unable to access the company's intranet site via their web browser, but they are able to access internet sites. Which of the following describes how the network administrator can resolve this issue?",
        "options": [
            "Correct the DNS server entries in the DHCP scope",
            "Correct the external firewall gateway address",
            "Correct the NTP server settings on the clients",
            "Correct a TFTP issue on the company's server"
        ],
        "correct_answer": 1,
        "description": "The correct answer is to correct the DNS server entries in the DHCP scope. Proper DNS configuration is essential for resolving internal domain names. \n\n- An external firewall gateway address would not affect internal site resolution. \n- NTP server settings ensure time synchronization but do not impact domain resolution. \n- TFTP is used for file transfers, unrelated to intranet accessibility."
    },
    {
        "question": "A technician is installing a new fiber connection to a network device in a datacenter. The connection from the device to the switch also traverses a patch panel connection. The chain of connections is in the following order: \nDevice → LC/LC patch cable → Patch panel → Cross-connect fiber cable → Patch panel → LC/LC patch cable → Switch. \nThe connection is not working. The technician has changed both patch cables with known working patch cables. The device had been tested and was working properly before being installed. Which of the following is the MOST likely cause of the issue?",
        "options": [
            "TX/RX is reversed",
            "An incorrect cable was used",
            "The device failed during installation",
            "Attenuation is occurring"
        ],
        "correct_answer": 1,
        "description": "The correct answer is TX/RX is reversed. Fiber connections require correct transmit (TX) and receive (RX) alignment for communication. \n\n- Incorrect cable types would not fit or transmit at all. \n- Device failure during installation is rare if the device was pre-tested. \n- Attenuation typically results in signal degradation, not a complete failure."
    },
    {
        "question": "A technician is searching for a device that is connected to the network and has the device's physical network address. Which of the following should the technician review on the switch to locate the device's network port?",
        "options": [
            "IP route table",
            "VLAN tag",
            "MAC table",
            "QoS tag"
        ],
        "correct_answer": 3,
        "description": "The correct answer is MAC table. The MAC table associates physical addresses with specific switch ports, helping locate the device. \n\n- IP route tables handle logical network paths, not physical locations. \n- VLAN tags identify traffic segmentation, not specific device locations. \n- QoS tags prioritize network traffic but do not help locate devices."
    },
    {
        "question": "Which of the following provides redundancy on a file server to ensure the server is still connected to a LAN even in the event of a port failure on a switch?",
        "options": [
            "NIC teaming",
            "Load balancer",
            "RAID array",
            "PDUs"
        ],
        "correct_answer": 1,
        "description": "The correct answer is NIC teaming. NIC teaming combines multiple network adapters for redundancy and performance. \n\n- Load balancers distribute traffic but do not directly provide LAN redundancy. \n- RAID arrays protect data but do not address network connectivity. \n- PDUs (Power Distribution Units) manage power, not network redundancy."
    },
    {
        "question": "An IT organization needs to optimize speeds for global content distribution and wants to reduce latency in high-density user locations. Which of the following technologies BEST meets the organization's requirements?",
        "options": [
            "Load balancing",
            "Geofencing",
            "Public cloud",
            "Content delivery network",
            "Infrastructure as a service"
        ],
        "correct_answer": 4,
        "description": "The correct answer is Content Delivery Network (CDN). CDNs distribute content across geographically diverse servers to improve speed and reduce latency. \n\n- Load balancing focuses on distributing local traffic. \n- Geofencing restricts access based on location but does not optimize speeds. \n- Public cloud and IaaS provide infrastructure but are not optimized for content distribution."
    },
    {
        "question": "A user reports being unable to access network resources after making some changes in the office. Which of the following should a network technician do FIRST?",
        "options": [
            "Check the system's IP address",
            "Do a ping test against the servers",
            "Reseat the cables into the back of the PC",
            "Ask what changes were made"
        ],
        "correct_answer": 4,
        "description": "The correct answer is to ask what changes were made. Identifying user changes provides critical context to troubleshoot effectively. \n\n- Checking IP addresses or running ping tests should follow understanding the changes. \n- Reseating cables may help but is not the most logical first step."
    },
    {
        "question": "A new cabling certification is being requested every time a network technician rebuilds one end of a Cat 6 (vendor-certified) cable to create a crossover connection that is used to connect switches. Which of the following would address this issue by allowing the use of the original cable?",
        "options": [
            "CSMA/CD",
            "LACP",
            "PoE+",
            "MDIX"
        ],
        "correct_answer": 4,
        "description": "The correct answer is MDIX. MDIX (Medium Dependent Interface Crossover) automatically adjusts for straight-through or crossover cables. \n\n- CSMA/CD handles network collision, unrelated to cables. \n- LACP aggregates links but does not impact cable type. \n- PoE+ delivers power but does not address connection types."
    },
    {
        "question": "A company hired a technician to find all the devices connected within a network. Which of the following software tools would BEST assist the technician in completing this task?",
        "options": [
            "IP scanner",
            "Terminal emulator",
            "NetFlow analyzer",
            "Port scanner"
        ],
        "correct_answer": 1,
        "description": "The correct answer is IP scanner. An IP scanner identifies devices by scanning assigned IP addresses within a range. \n\n- Terminal emulators are for command-line access. \n- NetFlow analyzers monitor traffic flows, not device discovery. \n- Port scanners analyze open ports, not the list of connected devices."
    },
{
    "question": "A technician is installing a high-density wireless network and wants to use an available frequency that supports the maximum number of channels to reduce interference. Which of the following standard 802.11 frequency ranges should the technician look for while reviewing WAP specifications?",
    "options": [
        "2.4GHz",
        "5GHz",
        "6GHz",
        "900MHz"
    ],
    "correct_answer": 2,
    "description": "The correct answer is 5GHz. The 5GHz frequency range offers a significant number of non-overlapping channels compared to 2.4GHz, reducing interference in high-density environments. \n\n- 2.4GHz has limited channels and is prone to interference from other devices. \n- 6GHz is emerging but may not yet be supported by all devices. \n- 900MHz is not used for standard Wi-Fi."
},

    {
        "question": "A technician is configuring a network switch to be used in a publicly accessible location. Which of the following should the technician configure on the switch to prevent unintended connections?",
        "options": [
            "DHCP snooping",
            "Geofencing",
            "Port security",
            "Secure SNMP"
        ],
        "correct_answer": 3,
        "description": "The correct answer is Port security. Port security allows the network administrator to restrict access to switch ports based on MAC addresses, preventing unauthorized devices from connecting. \n\n- DHCP snooping protects against malicious DHCP servers but does not prevent physical connections. \n- Geofencing restricts access based on physical location, not hardware connections. \n- Secure SNMP ensures encrypted management traffic but does not prevent unintended physical connections."
    },
    {
        "question": "Which of the following is used to track and document various types of known vulnerabilities?",
        "options": [
            "CVE",
            "Penetration testing",
            "Zero-day",
            "SIEM",
            "Least privilege"
        ],
        "correct_answer": 1,
        "description": "The correct answer is CVE. The Common Vulnerabilities and Exposures (CVE) database provides a standardized identification system for publicly known vulnerabilities. \n\n- Penetration testing identifies vulnerabilities but does not document them in a global database. \n- Zero-day refers to vulnerabilities without existing fixes. \n- SIEM collects and analyzes security data but does not focus solely on known vulnerabilities. \n- Least privilege is an access control principle, not a documentation tool."
    },
    {
        "question": "The network administrator is informed that a user's email password is frequently hacked by brute-force programs. Which of the following policies should the network administrator implement to BEST mitigate this issue? (Choose two.)",
        "options": [
            "Captive portal",
            "Two-factor authentication",
            "Complex passwords",
            "Geofencing",
            "Role-based access",
            "Explicit deny"
        ],
        "correct_answer": [2, 3],
        "description": "The correct answers are Two-factor authentication and Complex passwords. Two-factor authentication adds an extra layer of security, requiring additional verification beyond just the password. Complex passwords make brute-force attacks significantly more difficult. \n\n- Captive portal provides a web page for network authentication but does not mitigate brute-force attacks. \n- Geofencing restricts access based on location but is not specific to passwords. \n- Role-based access controls permissions, not password strength. \n- Explicit deny prevents access but does not address brute-force protection."
    },
    {
        "question": "A network engineer performs the following tasks to increase server bandwidth:\n✑ Connects two network cables from the server to a switch stack\n✑ Configures LACP on the switchports\n✑ Verifies the correct configurations on the switch interfaces\n\nWhich of the following needs to be configured on the server?",
        "options": [
            "Load balancing",
            "Multipathing",
            "NIC teaming",
            "Clustering"
        ],
        "correct_answer": 3,
        "description": "The correct answer is NIC teaming. NIC teaming combines multiple network interfaces on a server to improve bandwidth and provide redundancy. \n\n- Load balancing distributes traffic across servers, not interfaces. \n- Multipathing is used for storage connections, not network traffic. \n- Clustering involves multiple servers working together, not increasing a single server's bandwidth."
    },
    {
        "question": "A network technician is manually configuring the network settings for a new device and is told the network block is 192.168.0.0/20. Which of the following subnets should the technician use?",
        "options": [
            "255.255.128.0",
            "255.255.192.0",
            "255.255.240.0",
            "255.255.248.0"
        ],
        "correct_answer": 3,
        "description": "The correct answer is 255.255.240.0. A /20 subnet mask corresponds to 255.255.240.0, which provides the correct number of addresses for the given network block. \n\n- 255.255.128.0 and 255.255.192.0 represent smaller subnets than /20. \n- 255.255.248.0 represents a /21 subnet, which is larger than /20."
    },
    {
        "question": "Which of the following is the LARGEST MTU for a standard Ethernet frame?",
        "options": [
            "1452",
            "1492",
            "1500",
            "2304"
        ],
        "correct_answer": 3,
        "description": "The correct answer is 1500. The maximum transmission unit (MTU) for standard Ethernet frames is 1500 bytes. \n\n- 1452 and 1492 are smaller than the standard MTU size. \n- 2304 represents the MTU for certain non-standard Ethernet configurations, such as jumbo frames."
    },
    {
    "question": "Given the following information:\n\nProtocol   Local address         Foreign address        State\nTCP        127.0.0.1:57779      Desktop-Open:57780     Established\nTCP        127.0.0.1:57780      Desktop-Open:57779     Established\n\nWhich of the following command-line tools would generate this output?",
    "options": [
        "netstat",
        "arp",
        "dig",
        "tracert"
    ],
    "correct_answer": 1,
    "description": "The correct answer is netstat. The netstat command displays active TCP connections, listening ports, and the network state, making it ideal for showing established connections like the one in the output. \n\n- arp displays and modifies the ARP table, which shows MAC-to-IP address mappings, not active connections.\n- dig is used for DNS queries to resolve domain names, not network connection states.\n- tracert maps the route packets take to reach a destination but does not show active connections or listening ports."
    },
    {
        "question": "According to troubleshooting methodology, which of the following should the technician do NEXT after determining the most likely probable cause of an issue?",
        "options": [
            "Establish a plan of action to resolve the issue and identify potential effects",
            "Verify full system functionality and, if applicable, implement preventive measures",
            "Implement the solution or escalate as necessary",
            "Test the theory to determine the cause"
        ],
        "correct_answer": 1,
        "description": "The correct answer is to establish a plan of action to resolve the issue and identify potential effects. This step ensures that the solution is well thought out and considers the potential impact of the actions taken. \n\n- Verifying full system functionality is important but occurs later in the process, after implementing the solution.\n- Implementing the solution or escalating it is premature without a plan of action.\n- Testing the theory is already completed by this stage in the methodology."
    },
    {
        "question": "Which of the following BEST describes a network appliance that warns of unapproved devices that are accessing the network?",
        "options": [
            "Firewall",
            "AP",
            "Proxy server",
            "IDS"
        ],
        "correct_answer": 4,
        "description": "The correct answer is IDS (Intrusion Detection System). An IDS monitors network traffic for suspicious activity and alerts administrators about unauthorized devices or access attempts. \n\n- Firewalls block or allow traffic based on predefined rules but do not provide detailed alerts about unapproved devices.\n- AP (Access Point) provides wireless access but does not monitor for unauthorized devices.\n- Proxy servers handle requests between clients and servers for security or performance but do not actively warn about unapproved devices."
    },
    {
        "question": "A technician is installing a cable modem in a SOHO. Which of the following cable types will the technician MOST likely use to connect a modem to the ISP?",
        "options": [
            "Coaxial",
            "Single-mode fiber",
            "Cat 6e",
            "Multimode fiber"
        ],
        "correct_answer": 1,
        "description": "The correct answer is coaxial. Cable modems typically use coaxial cables to connect to the ISP's infrastructure, making it the most likely choice in a SOHO setup. \n\n- Single-mode fiber is used for long-distance, high-speed internet connections but is less common in residential setups.\n- Cat 6e cables are used for Ethernet connections within the local network, not for connecting to the ISP.\n- Multimode fiber is used for short-distance, high-speed connections but is also uncommon in SOHO environments."
    },
    {
    "question": "A network technician is reviewing the interface counters on a router interface. The technician is attempting to confirm a cable issue. Given the following information:\n\nMetric       | Value\nLast cleared | 7 minutes, 34 seconds\n# of packets output | 6915\n# of packets input | 270\nCRCs          | 183\nGiants        | 0\nRunts         | 0\nMulticasts    | 14\n\nWhich of the following metrics confirms there is a cabling issue?",
    "options": [
        "Last cleared",
        "Number of packets output",
        "CRCs",
        "Giants",
        "Multicasts"
    ],
    "correct_answer": 3,
    "description": "The correct answer is CRCs (Cyclic Redundancy Check errors). A high number of CRC errors indicates that frames are being corrupted during transmission, often due to a cabling issue such as interference, poor cable quality, or incorrect cable length.\n\n- Last cleared is unrelated to diagnosing a cabling issue; it only shows when counters were last reset.\n- The number of packets output reflects the traffic volume and does not provide information about errors.\n- Giants refer to frames that are too large, but there are none in this scenario.\n- Multicasts represent normal traffic and are unrelated to cabling problems."
    },
    {
        "question": "Which of the following is the physical topology for an Ethernet LAN?",
        "options": [
            "Bus",
            "Ring",
            "Mesh",
            "Star"
        ],
        "correct_answer": 4,
        "description": "The correct answer is Star. In an Ethernet LAN, the physical topology uses a central switch or hub to connect devices, creating a star-like arrangement. This setup allows for easy troubleshooting and prevents a single cable failure from affecting the entire network.\n\n- Bus topology is outdated and involves a single backbone cable, which is not commonly used in Ethernet LANs.\n- Ring topology is used in older systems like Token Ring but is not applicable to Ethernet networks.\n- Mesh topology involves direct connections between devices and is used for redundancy, not typical Ethernet LANs."
    },
    {
        "question": "An IT director is setting up new disaster and HA policies for a company. Limited downtime is critical to operations. To meet corporate requirements, the director set up two different datacenters across the country that will stay current on data and applications. In the event of an outage, the company can immediately switch from one datacenter to another. Which of the following does this BEST describe?",
        "options": [
            "A warm site",
            "Data mirroring",
            "Multipathing",
            "Load balancing",
            "A hot site"
        ],
        "correct_answer": 5,
        "description": "The correct answer is A hot site. A hot site is a fully functional datacenter that mirrors the primary site in real-time, allowing for an immediate switch during an outage, minimizing downtime.\n\n- Warm sites require manual setup and are not immediately ready for operation.\n- Data mirroring involves replicating data but does not cover the full operational readiness of the site.\n- Multipathing is for redundant data paths, not disaster recovery.\n- Load balancing spreads workload across systems but does not describe datacenter failover capabilities."
    },
    {
        "question": "The management team needs to ensure unnecessary modifications to the corporate network are not permitted and version control is maintained. Which of the following documents would BEST support this?",
        "options": [
            "An incident response plan",
            "A business continuity plan",
            "A change management policy",
            "An acceptable use policy"
        ],
        "correct_answer": 3,
        "description": "The correct answer is A change management policy. This document ensures that changes to the corporate network are planned, reviewed, and approved to prevent unauthorized modifications and maintain version control.\n\n- An incident response plan is for handling security incidents, not network modifications.\n- A business continuity plan focuses on operations during disruptions but does not address network changes.\n- An acceptable use policy defines proper use of IT resources but does not manage changes."
    },
    {
        "question": "Which of the following is MOST likely to generate significant East-West traffic in a datacenter?",
        "options": [
            "A backup of a large video presentation to cloud storage for archival purposes",
            "A duplication of a hosted virtual server to another physical server for redundancy",
            "A download of navigation data to a portable device for offline access",
            "A query from an IoT device to a cloud-hosted server for a firmware update"
        ],
        "correct_answer": 2,
        "description": "The correct answer is A duplication of a hosted virtual server to another physical server for redundancy. East-West traffic refers to data transfer within a datacenter, such as server-to-server communication, which occurs during virtual server duplication.\n\n- Backing up to cloud storage generates North-South traffic (datacenter to external cloud).\n- A download to a portable device involves external communication, not internal.\n- IoT device queries to a cloud-hosted server are also North-South traffic."
    },
    {
        "question": "A technician is troubleshooting a network switch that seems to stop responding to requests intermittently whenever the logging level is set for debugging. Which of the following metrics should the technician check to begin troubleshooting the issue?",
        "options": [
            "Audit logs",
            "CPU utilization",
            "CRC errors",
            "Jitter"
        ],
        "correct_answer": 2,
        "description": "The correct answer is CPU utilization. Debug-level logging generates significant system overhead, which can cause the switch to become unresponsive if the CPU is overburdened.\n\n- Audit logs are for security and compliance, not performance issues.\n- CRC errors are related to data corruption, not system responsiveness.\n- Jitter is a measure of latency variation in network traffic, unrelated to switch CPU performance."
    },
    {
        "question": "A technician wants to deploy a new wireless network that comprises 30 WAPs installed throughout a three-story office building. All the APs will broadcast the same SSID for client access. Which of the following BEST describes this deployment?",
        "options": [
            "Extended service set",
            "Basic service set",
            "Unified service set",
            "Independent basic service set"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Extended service set. An ESS allows multiple WAPs to broadcast the same SSID, enabling seamless roaming for clients within the network.\n\n- A basic service set refers to a single WAP and its associated clients.\n- Unified service set is not a standard Wi-Fi term.\n- Independent basic service set is for ad-hoc networks without WAPs."
    },
    {
        "question": "A user tries to ping 192.168.1.100 from the command prompt on the 192.168.2.101 network but gets the following response: U.U.U.U. Which of the following needs to be configured for these networks to reach each other?",
        "options": [
            "Network address translation",
            "Default gateway",
            "Loopback",
            "Routing protocol"
        ],
        "correct_answer": 2,
        "description": "The correct answer is Default gateway. The lack of communication between different networks indicates that the default gateway is not correctly configured, preventing routing between subnets.\n\n- Network address translation is for address translation, not basic inter-network communication.\n- Loopback is a local address for testing and does not facilitate network communication.\n- A routing protocol establishes routes between routers but is not necessary for a single gateway setup."
    },
{
    "question": "A branch of a company recently switched to a new ISP. The network engineer was given a new IP range to assign. The ISP assigned 196.26.4.0/26, and the branch gateway router now has the following configurations on the interface that peers to the ISP:\n\nIP address: 196.26.4.30\nSubnet mask: 255.255.255.224\nGateway: 196.24.4.1\n\nThe network engineer observes that all users have lost Internet connectivity. Which of the following describes the issue?",
    "options": [
        "The incorrect subnet mask was configured.",
        "The incorrect gateway was configured.",
        "The incorrect IP address was configured.",
        "The incorrect interface was configured."
    ],
    "correct_answer": 2,
    "description": "The correct answer is 'The incorrect gateway was configured.' The gateway address (196.24.4.1) is outside the assigned subnet range of 196.26.4.0/26, which has valid IP addresses from 196.26.4.1 to 196.26.4.62. As a result, devices cannot communicate with the ISP.\n\n- The subnet mask (255.255.255.224) is correct for a /26 network.\n- The IP address (196.26.4.30) is within the correct range and properly configured.\n- The interface is not indicated to be the source of the issue, so this option is not relevant."
},

{
    "question": "Within the realm of network security, Zero Trust:",
    "options": [
        "Prevents attackers from moving laterally through a system.",
        "Allows a server to communicate with outside networks without a firewall.",
        "Blocks malicious software that is too new to be found in virus definitions.",
        "Stops infected files from being downloaded via websites."
    ],
    "correct_answer": 1,
    "description": "The correct answer is 'Prevents attackers from moving laterally through a system.' Zero Trust security models assume that threats exist both inside and outside the network. As a result, Zero Trust limits lateral movement within the system by enforcing strict access controls and verifying every request for access, whether it's inside or outside the network.\n\n- Option B is incorrect because Zero Trust still requires stringent security measures, including firewalls.\n- Option C refers to techniques like heuristic or behavioral detection, but this is not a primary focus of Zero Trust.\n- Option D is also incorrect as Zero Trust focuses on verifying access, not just blocking downloads of infected files."
},





]

