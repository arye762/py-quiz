questions_set_A = [

#1 - 100

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
    "question": "A network technician is reviewing the interface counters on a router interface. The technician is attempting to confirm a cable issue. Given the following information:\n\nMetric                 | Value\n-----------------------|-----------------\nLast cleared           | 7 minutes, 34 seconds\n# of packets output    | 6915\n# of packets input     | 270\nCRCs                   | 183\nGiants                 | 0\nRunts                  | 0\nMulticasts             | 14\n\nWhich of the following metrics confirms there is a cabling issue?",
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

#41 - 

    {
        "question": "Which of the following service models would MOST likely be used to replace on-premises servers with a cloud solution?",
        "options": [
            "PaaS",
            "IaaS",
            "SaaS",
            "Disaster recovery as a Service (DRaaS)"
        ],
        "correct_answer": 2,
        "description": "The correct answer is IaaS (Infrastructure as a Service). IaaS provides virtualized computing resources over the internet, allowing organizations to replace physical on-premises servers with cloud-hosted servers. \n\n- PaaS (Platform as a Service) is for application development and deployment rather than server replacement. \n- SaaS (Software as a Service) delivers software over the internet but does not replace servers. \n- DRaaS focuses on disaster recovery, not day-to-day server infrastructure."
    },
    {
        "question": "Which of the following factors should be considered when evaluating a firewall to protect a datacenter's east-west traffic?",
        "options": [
            "Replication traffic between an on-premises server and a remote backup facility",
            "Traffic between VMs running on different hosts",
            "Concurrent connections generated by Internet DDoS attacks",
            "VPN traffic from remote offices to the datacenter's VMs"
        ],
        "correct_answer": 2,
        "description": "The correct answer is traffic between VMs running on different hosts. East-west traffic occurs within a datacenter, such as communication between virtual machines (VMs) or servers, making this factor critical when evaluating firewall performance. \n\n- Replication traffic involves north-south traffic and does not represent internal VM-to-VM communication. \n- Concurrent connections from Internet DDoS attacks are typically part of north-south traffic, not east-west. \n- VPN traffic from remote offices also falls under north-south traffic, not internal datacenter communication."
    },
    {
        "question": "Which of the following is used to prioritize Internet usage per application and per user on the network?",
        "options": [
            "Bandwidth management",
            "Load balance routing",
            "Border Gateway Protocol",
            "Administrative distance"
        ],
        "correct_answer": 1,
        "description": "The correct answer is bandwidth management. Bandwidth management allows administrators to allocate and prioritize network resources, ensuring critical applications and users have sufficient bandwidth. \n\n- Load balance routing optimizes the distribution of traffic across multiple paths but does not directly prioritize bandwidth per application or user. \n- Border Gateway Protocol (BGP) manages routing between autonomous systems, unrelated to application-level prioritization. \n- Administrative distance determines route selection based on trustworthiness, not bandwidth prioritization."
    },
    {
        "question": "A network administrator needs to query the NSs for a remote application. Which of the following commands would BEST help the administrator accomplish this task?",
        "options": [
            "dig",
            "arp",
            "show interface",
            "hostname"
        ],
        "correct_answer": 1,
        "description": "The correct answer is dig. The 'dig' command queries Domain Name System (DNS) servers, helping to resolve names or gather DNS-related information about remote applications. \n\n- arp lists IP-to-MAC address mappings, unrelated to querying DNS. \n- show interface displays details about a device's network interfaces but does not involve DNS. \n- hostname shows or sets the system's hostname and is unrelated to querying a remote application."
    },
    {
        "question": "Which of the following would MOST likely be used to review previous upgrades to a system?",
        "options": [
            "Business continuity plan",
            "Change management",
            "System life cycle",
            "Standard operating procedures"
        ],
        "correct_answer": 2,
        "description": "The correct answer is change management. Change management keeps records of changes made to systems, including upgrades, ensuring traceability and proper documentation. \n\n- Business continuity plans focus on disaster recovery and operational resilience, not system changes. \n- System life cycle outlines the development and maintenance stages but does not document upgrades specifically. \n- Standard operating procedures (SOPs) provide general guidelines, not upgrade-specific records."
    },
    {
        "question": "A technician is deploying a new switch model and would like to add it to the existing network monitoring software. The technician wants to know what metrics can be gathered from a given switch. Which of the following should the technician utilize for the switch?",
        "options": [
            "MIB",
            "Trap",
            "Syslog",
            "Audit log"
        ],
        "correct_answer": 1,
        "description": "The correct answer is MIB (Management Information Base). MIB defines the structure of data that network devices can share, enabling the monitoring software to query the switch for specific metrics. \n\n- Traps are SNMP alerts sent by devices but do not provide the list of available metrics. \n- Syslog collects log messages but does not define metric structures. \n- Audit logs record security-related events, not operational metrics."
    },
    {
        "question": "A network device is configured to send critical events to a syslog server; however, the following alerts are not being received: \nSeverity 5 LINK-UPDOWN: Interface 1/1, changed state to down\nSeverity 5 LINK-UPDOWN: Interface 1/3, changed state to down\nWhich of the following describes the reason why the events are not being received?",
        "options": [
            "The network device is not configured to log that level to the syslog server",
            "The network device was down and could not send the event",
            "The syslog server is not compatible with the network device",
            "The syslog server did not have the correct MIB loaded to receive the message"
        ],
        "correct_answer": 1,
        "description": "The correct answer is the network device is not configured to log that level to the syslog server. Syslog servers only receive logs if the device is explicitly configured to send events of the corresponding severity level. \n\n- The device being down would mean no events could be generated at all, which is not the case here. \n- Syslog compatibility issues are rare and unrelated to severity levels. \n- MIBs are unrelated to syslog servers, as syslog does not use SNMP-based MIBs."
    },
    {
        "question": "A network administrator is implementing OSPF on all of a company's network devices. Which of the following will MOST likely replace all the company's hubs?",
        "options": [
            "A Layer 3 switch",
            "A proxy server",
            "A NGFW",
            "A WLAN controller"
        ],
        "correct_answer": 1,
        "description": "The correct answer is a Layer 3 switch. Layer 3 switches can perform routing, making them ideal replacements for hubs, which only function as simple repeaters without any routing capabilities. \n\n- Proxy servers manage web traffic but cannot replace hubs in a network topology. \n- Next-generation firewalls (NGFW) enhance security but are not substitutes for hubs. \n- WLAN controllers manage wireless access points, unrelated to replacing hubs."
    },
    {
        "question": "A network administrator discovers that users in an adjacent building are connecting to the company's guest wireless network to download inappropriate material. Which of the following can the administrator do to MOST easily mitigate this issue?",
        "options": [
            "Reduce the wireless power levels",
            "Adjust the wireless channels",
            "Enable wireless client isolation",
            "Enable wireless port security"
        ],
        "correct_answer": 1,
        "description": "The correct answer is reduce the wireless power levels. By lowering the power output of the access point, the administrator can limit the range of the wireless network, preventing users in the adjacent building from connecting. \n\n- Adjusting wireless channels resolves interference issues but does not reduce network range. \n- Enabling wireless client isolation prevents communication between clients but does not block external users. \n- Wireless port security is used to secure specific ports, not to control range or access."
    },


    {
        "question": "A network administrator is designing a new datacenter in a different region that will need to communicate to the old datacenter with a secure connection. Which of the following access methods would provide the BEST security for this new datacenter?",
        "options": [
            "Virtual network computing.",
            "Secure Socket Shell.",
            "In-band connection.",
            "Site-to-site VPN."
        ],
        "correct_answer": 4,
        "description": "The correct answer is Site-to-site VPN. It provides a secure, encrypted connection between the new and old datacenters, ensuring data confidentiality and integrity. \n\n- Virtual network computing (VNC) is used for remote desktop access but lacks robust security for large-scale datacenter connections. \n- Secure Socket Shell (SSH) is designed for individual connections, not for linking entire datacenters. \n- In-band connections refer to network management over the production network and do not inherently offer security."
    },
    {
        "question": "An attacker is attempting to find the password to a network by inputting common words and phrases in plaintext to the password prompt. Which of the following attack types BEST describes this action?",
        "options": [
            "Pass-the-hash attack.",
            "Rainbow table attack.",
            "Brute-force attack.",
            "Dictionary attack."
        ],
        "correct_answer": 4,
        "description": "The correct answer is Dictionary attack. This method involves systematically testing common words and phrases against a password field. \n\n- Pass-the-hash attacks involve stealing hashed credentials and reusing them, rather than guessing passwords. \n- Rainbow table attacks use precomputed hash values rather than plaintext words. \n- Brute-force attacks involve trying all possible combinations, not just a list of common words."
    },
    {
        "question": "Which of the following technologies provides a failover mechanism for the default gateway?",
        "options": [
            "FHRP.",
            "LACP.",
            "OSPF.",
            "STP."
        ],
        "correct_answer": 1,
        "description": "The correct answer is FHRP (First Hop Redundancy Protocol). It ensures network availability by providing a failover mechanism for the default gateway. \n\n- LACP (Link Aggregation Control Protocol) is used for bundling multiple network connections, not gateway redundancy. \n- OSPF (Open Shortest Path First) is a routing protocol, not directly related to default gateway failover. \n- STP (Spanning Tree Protocol) is used for preventing network loops, not for gateway redundancy."
    },
    {
        "question": "A network engineer is investigating reports of poor network performance. Upon reviewing a device configuration, the engineer finds that duplex settings are mismatched on both ends. Which of the following would be the MOST likely result of this finding?",
        "options": [
            "Increased CRC errors.",
            "Increased giants and runts.",
            "Increased switching loops.",
            "Increased device temperature."
        ],
        "correct_answer": 1,
        "description": "The correct answer is Increased CRC errors. Duplex mismatches can cause excessive collisions and packet retransmissions, leading to CRC errors. \n\n- Giants and runts refer to abnormal packet sizes but are not directly linked to duplex mismatches. \n- Switching loops are caused by incorrect Layer 2 topology configurations, not duplex mismatches. \n- Increased device temperature is unrelated to network configuration issues."
    },
    {
        "question": "Which of the following devices would be used to manage a corporate WLAN?",
        "options": [
            "A wireless NAS.",
            "A wireless bridge.",
            "A wireless router.",
            "A wireless controller."
        ],
        "correct_answer": 4,
        "description": "The correct answer is A wireless controller. It centralizes the management of corporate WLANs, allowing for easy configuration, monitoring, and troubleshooting. \n\n- Wireless NAS (Network Attached Storage) is used for data storage and does not manage WLANs. \n- Wireless bridges connect two network segments but do not manage WLANs. \n- Wireless routers provide local network connectivity but lack advanced WLAN management features."
    },
    {
        "question": "Which of the following types of devices can provide content filtering and threat protection, and manage multiple IPSec site-to-site connections?",
        "options": [
            "Layer 3 switch.",
            "VPN headend.",
            "Next-generation firewall.",
            "Proxy server.",
            "Intrusion prevention."
        ],
        "correct_answer": 3,
        "description": "The correct answer is Next-generation firewall. It combines content filtering, threat protection, and VPN capabilities, making it ideal for managing multiple IPSec connections. \n\n- Layer 3 switches primarily handle routing and switching, not content filtering or threat protection. \n- VPN headends manage VPN connections but lack content filtering and advanced threat protection. \n- Proxy servers provide web filtering but lack IPSec management capabilities. \n- Intrusion prevention focuses on threat detection and response, not site-to-site VPN management."
    },
    {
        "question": "An engineer notices some late collisions on a half-duplex link. The engineer verifies that the devices on both ends of the connection are configured for half duplex. Which of the following is the MOST likely cause of this issue?",
        "options": [
            "The link is improperly terminated.",
            "One of the devices is misconfigured.",
            "The cable length is excessive.",
            "One of the devices has a hardware issue."
        ],
        "correct_answer": 3,
        "description": "The correct answer is The cable length is excessive. Excessive cable length can cause late collisions due to signal degradation and propagation delays. \n\n- Improperly terminated links usually cause signal loss, not late collisions. \n- Misconfigured devices would result in duplex mismatches rather than late collisions. \n- Hardware issues might lead to connectivity problems, not late collisions."
    },
    {
        "question": "A network administrator is configuring a load balancer for two systems. Which of the following must the administrator configure to ensure connectivity during a failover?",
        "options": [
            "VIP.",
            "NAT.",
            "APIPA.",
            "IPv6 tunneling.",
            "Broadcast IP."
        ],
        "correct_answer": 1,
        "description": "The correct answer is VIP (Virtual IP). It enables failover by allowing multiple systems to share a single IP address for seamless connectivity. \n\n- NAT (Network Address Translation) handles IP translation but does not provide failover functionality. \n- APIPA is used for self-assigned IPs when DHCP fails and is unrelated to load balancing. \n- IPv6 tunneling facilitates IPv6 over IPv4 networks but does not ensure failover. \n- Broadcast IP is used for sending messages to all devices on a network, not for failover."
    },


    {
        "question": "The following configuration is applied to a DHCP server connected to a VPN concentrator:\n\nIP address: 10.0.0.1\nSubnet mask: 255.255.255.0\nGateway: 10.0.0.254\n\nThere are 300 non-concurrent sales representatives who log in for one hour a day to upload reports, and 252 of these representatives are able to connect to the VPN without any issues. The remaining sales representatives cannot connect to the VPN over the course of the day. Which of the following can be done to resolve the issue without utilizing additional resources?",
        "options": [
            "Decrease the lease duration",
            "Reboot the DHCP server",
            "Install a new VPN concentrator",
            "Configure a new router"
        ],
        "correct_answer": 1,
        "description": "The correct answer is 'Decrease the lease duration.' By shortening the lease duration, the DHCP server will reallocate IP addresses more frequently, ensuring availability for additional users over time. \n\n- Rebooting the DHCP server may temporarily resolve some issues but does not address the underlying problem of IP address exhaustion. \n- Installing a new VPN concentrator would require additional resources, which the question explicitly states to avoid. \n- Configuring a new router does not resolve DHCP lease issues and is unnecessary."
    },
    {
        "question": "A technician needs to configure a Linux computer for network monitoring. The technician has the following information:\nLinux computer details:\n\nInterface       IP address    MAC address\neth0            10.1.2.24     A1:B2:C3:F4:E5:D6\n\nSwitch mirror port details:\nInterface       IP address    MAC address\neth1            10.1.2.3      A1:B2:C3:D4:E5:F6\n\nAfter connecting the Linux computer to the mirror port on the switch, which of the following commands should the technician run on the Linux computer?",
        "options": [
            "ifconfig eth0 promisc",
            "ifconfig eth1 up",
            "ifconfig eth0 10.1.2.3",
            "ifconfig eth1 hw ether A1:B2:C3:D4:E5:F6"
        ],
        "correct_answer": 1,
        "description": "The correct answer is 'ifconfig eth0 promisc.' Enabling promiscuous mode allows the network interface to capture all network packets, which is necessary for network monitoring. \n\n- Bringing up the interface with 'ifconfig eth1 up' is not sufficient for monitoring purposes. \n- Setting the IP address with 'ifconfig eth0 10.1.2.3' is irrelevant since the focus is on packet monitoring, not standard network communication. \n- Changing the MAC address with 'ifconfig eth1 hw ether A1:B2:C3:D4:E5:F6' is unrelated to the task of monitoring network traffic."
    },



    {
        "question": "A technician is troubleshooting a wireless connectivity issue in a small office located in a high-rise building. Several APs are mounted in this office. The users report that the network connections frequently disconnect and reconnect throughout the day. Which of the following is the MOST likely cause of this issue?",
        "options": [
            "The AP association time is set too low",
            "EIRP needs to be boosted",
            "Channel overlap is occurring",
            "The RSSI is misreported"
        ],
        "correct_answer": 3,
        "description": "The correct answer is 'Channel overlap is occurring.' This issue arises when multiple access points use overlapping channels, leading to interference and unstable connections. To resolve this, APs should use non-overlapping channels (e.g., 1, 6, 11 in the 2.4 GHz band).\n\n- Setting the AP association time too low would only affect session timeouts and is unrelated to connection instability.\n- Boosting EIRP (Effective Isotropic Radiated Power) could exacerbate interference in a high-density environment.\n- Misreported RSSI (Received Signal Strength Indicator) is unlikely to cause frequent disconnections."
    },
    {
        "question": "A network engineer configured new firewalls with the correct configuration to be deployed to each remote branch. Unneeded services were disabled, and all firewall rules were applied successfully. Which of the following should the network engineer perform NEXT to ensure all the firewalls are hardened successfully?",
        "options": [
            "Ensure an implicit permit rule is enabled",
            "Configure the log settings on the firewalls to the central syslog server",
            "Update the firewalls with current firmware and software",
            "Use the same complex passwords on all firewalls"
        ],
        "correct_answer": 3,
        "description": "The correct answer is 'Update the firewalls with current firmware and software.' Ensuring firewalls have the latest updates addresses potential security vulnerabilities.\n\n- Enabling an implicit permit rule contradicts best practices since it would allow unauthorized traffic.\n- Configuring log settings is important but does not directly harden the firewall.\n- Using the same passwords on all firewalls creates a security risk and violates password management best practices."
    },
    {
        "question": "At which of the following OSI model layers would a technician find an IP header?",
        "options": [
            "Layer 1",
            "Layer 2",
            "Layer 3",
            "Layer 4"
        ],
        "correct_answer": 3,
        "description": "The correct answer is 'Layer 3.' The IP header is part of the Network layer, which is responsible for logical addressing and routing.\n\n- Layer 1 refers to the Physical layer and involves hardware and transmission media.\n- Layer 2 refers to the Data Link layer, responsible for MAC addresses and error detection.\n- Layer 4 refers to the Transport layer, which handles end-to-end communication and protocols like TCP and UDP."
    },
    {
        "question": "An engineer is configuring redundant network links between switches. Which of the following should the engineer enable to prevent network stability issues?",
        "options": [
            "802.1Q",
            "STP",
            "Flow control",
            "CSMA/CD"
        ],
        "correct_answer": 2,
        "description": "The correct answer is 'STP' (Spanning Tree Protocol). STP prevents network loops, which can cause broadcast storms and instability.\n\n- 802.1Q is used for VLAN tagging and does not prevent network loops.\n- Flow control manages data transfer rates but does not address redundancy.\n- CSMA/CD (Carrier Sense Multiple Access with Collision Detection) is used in Ethernet networks but is not relevant to preventing loops."
    },
    {
        "question": "Which of the following routing protocols is used to exchange route information between public autonomous systems?",
        "options": [
            "OSPF",
            "BGP",
            "EIGRP",
            "RIP"
        ],
        "correct_answer": 2,
        "description": "The correct answer is 'BGP' (Border Gateway Protocol). BGP is the standard protocol for exchanging routing information between different autonomous systems on the internet.\n\n- OSPF (Open Shortest Path First) is an interior gateway protocol used within an autonomous system.\n- EIGRP (Enhanced Interior Gateway Routing Protocol) is also an interior protocol, specific to Cisco.\n- RIP (Routing Information Protocol) is outdated and not suitable for public autonomous systems."
    },
    {
        "question": "A fiber link connecting two campus networks is broken. Which of the following tools should an engineer use to detect the exact break point of the fiber link?",
        "options": [
            "OTDR",
            "Tone generator",
            "Fusion splicer",
            "Cable tester",
            "PoE injector"
        ],
        "correct_answer": 1,
        "description": "The correct answer is 'OTDR' (Optical Time Domain Reflectometer). OTDR is specifically designed to locate faults and measure the distance to a break in fiber optic cables.\n\n- A tone generator is used for tracing and identifying copper cables, not fiber.\n- A fusion splicer is used to join fiber cables but does not detect faults.\n- A cable tester is used for copper cables, not fiber.\n- A PoE injector provides power over Ethernet and is unrelated to fault detection."
    },
    {
        "question": "Which of the following can be used to centrally manage credentials for various types of administrative privileges on configured network devices?",
        "options": [
            "SSO",
            "TACACS+",
            "Zero Trust",
            "Separation of duties",
            "Multifactor authentication"
        ],
        "correct_answer": 2,
        "description": "The correct answer is 'TACACS+' (Terminal Access Controller Access-Control System Plus). TACACS+ is a protocol used for centralized authentication and authorization of administrative users on network devices.\n\n- SSO (Single Sign-On) simplifies user access across applications but does not handle administrative privileges for network devices.\n- Zero Trust is a security model, not a protocol for credential management.\n- Separation of duties is a principle to prevent conflicts of interest, not a technical solution.\n- Multifactor authentication enhances security but does not centrally manage credentials."
    },
{
    "question": "Branch users are experiencing issues with videoconferencing. Which of the following will the company MOST likely configure to improve performance for these applications?",
    "options": [
        "Link Aggregation Control Protocol.",
        "Dynamic routing.",
        "Quality of service.",
        "Network load balancer.",
        "Static IP addresses."
    ],
    "correct_answer": 3,
    "description": "The correct answer is Quality of Service (QoS). QoS is designed to prioritize network traffic and ensure that latency-sensitive applications, such as videoconferencing, are given higher priority over less critical traffic. This reduces issues like lag, jitter, and packet loss, which can degrade videoconferencing quality. \n\n- Link Aggregation Control Protocol (LACP) is used to combine multiple network connections for increased bandwidth and redundancy but does not address latency-sensitive traffic prioritization. \n- Dynamic routing adjusts network paths based on changes in topology or link conditions but does not prioritize specific types of traffic. \n- Network load balancers distribute traffic across multiple servers or links but are more suited for balancing server load rather than improving application performance. \n- Static IP addresses simplify device identification but do not affect network performance or traffic prioritization."
},

{
    "question": "Several WIFI users are reporting the inability to connect to the network. WLAN users on the guest network are able to access all network resources without any performance issues. The following table summarizes the findings after a site survey of the area in question:\n\nLocation    SSID           Channel   RSSI    Antenna Type\nAP 1        Corp1          2        -81dBm  Omni\nAP 2        Corp1          1        -82dBm  Omni\nAP 3        Corp1/Guest    5        -44dBm  Directional\nAP 4        Corp1/Guest    11       -41dBm  Directional\n\nWhich of the following should a wireless technician do NEXT to troubleshoot this issue?",
    "options": [
        "Reconfigure the channels to reduce overlap.",
        "Replace the omni antennas with directional antennas.",
        "Update the SSIDs on all the APs.",
        "Decrease power in AP 3 and AP 4."
    ],
    "correct_answer": 1,
    "description": "The correct answer is to reconfigure the channels to reduce overlap. Overlapping channels can cause interference between access points, leading to connectivity issues for users. Ensuring APs use non-overlapping channels (e.g., 1, 6, 11 in 2.4 GHz) improves signal stability and reduces disconnects.\n\n- Replacing omni antennas with directional antennas is unnecessary here since the issue is related to channel overlap, not signal coverage or direction.\n\n- Updating the SSIDs on all the APs would not resolve the issue as SSIDs are identifiers and do not impact the channel interference.\n\n- Decreasing power in AP 3 and AP 4 is unrelated because the guest network users are not facing any issues; the problem lies in the overlapping channels used by AP 1 and AP 2."
},

    {
        "question": "A technician is assisting a user who cannot connect to a network resource. The technician first checks for a link light. According to troubleshooting methodology, this is an example of:",
        "options": [
            "Using a bottom-to-top approach.",
            "Establishing a plan of action.",
            "Documenting a finding.",
            "Questioning the obvious."
        ],
        "correct_answer": 1,
        "description": "The correct answer is using a bottom-to-top approach. This involves starting the troubleshooting process by checking the physical layer, such as the link light, before moving to higher layers in the OSI model. \n\n- Establishing a plan of action occurs after identifying the issue, not as a first step. \n- Documenting a finding comes after troubleshooting to record the outcome. \n- Questioning the obvious involves rechecking common issues, but here the technician is following a structured approach."
    },
    {
        "question": "Which of the following transceiver types can support up to 40Gbps?",
        "options": [
            "SFP+",
            "QSFP+",
            "QSFP",
            "SFP"
        ],
        "correct_answer": 2,
        "description": "The correct answer is QSFP+. QSFP+ transceivers support up to 40Gbps speeds and are commonly used in high-performance networking environments. \n\n- SFP+ supports up to 10Gbps, making it unsuitable for 40Gbps speeds. \n- QSFP is capable of 4x10Gbps, but not 40Gbps in a single channel. \n- SFP is designed for much lower speeds, typically up to 1Gbps."
    },
    {
        "question": "Which of the following TCP ports is used by the Windows OS for file sharing?",
        "options": [
            "53",
            "389",
            "445",
            "1433"
        ],
        "correct_answer": 3,
        "description": "The correct answer is 445. TCP port 445 is used by Windows OS for file sharing, specifically for SMB (Server Message Block) protocol. \n\n- Port 53 is used for DNS (Domain Name System) queries. \n- Port 389 is used for LDAP (Lightweight Directory Access Protocol). \n- Port 1433 is used for SQL Server database communication."
    },
    {
        "question": "A network administrator redesigned the positioning of the APs to create adjacent areas of wireless coverage. After project validation, some users still report poor connectivity when their devices maintain an association to a distanced AP. Which of the following should the network administrator check FIRST?",
        "options": [
            "Validate the roaming settings on the APs and WLAN clients",
            "Verify that the AP antenna type is correct for the new layout",
            "Check to see if MU-MIMO was properly activated on the APs",
            "Deactivate the 2.4GHz band on the APs"
        ],
        "correct_answer": 1,
        "description": "The correct answer is validating the roaming settings on the APs and WLAN clients. Roaming settings determine how devices transition between access points, and improper settings may cause devices to stay associated with distant APs. \n\n- Verifying the AP antenna type may improve coverage, but does not address roaming issues directly. \n- MU-MIMO can improve performance but is not directly related to poor roaming behavior. \n- Deactivating the 2.4GHz band may limit device compatibility, but is unlikely the root cause."
    },
    {
        "question": "Which of the following connector types would have the MOST flexibility?",
        "options": [
            "SFP",
            "BNC",
            "LC",
            "RJ45"
        ],
        "correct_answer": 1,
        "description": "The correct answer is SFP. SFP (Small Form-factor Pluggable) modules provide flexibility because they support a range of fiber and copper media types, allowing for easy upgrades and replacements. \n\n- BNC is typically used for coaxial cables in older or specialized networking applications. \n- LC is a fiber-optic connector with less flexibility compared to SFP. \n- RJ45 is commonly used for Ethernet connections but does not provide the same flexibility as SFP for various media types."
    },
    {
        "question": "Which of the following ports is commonly used by VoIP phones?",
        "options": [
            "20",
            "143",
            "445",
            "5060"
        ],
        "correct_answer": 4,
        "description": "The correct answer is 5060. TCP/UDP port 5060 is used for SIP (Session Initiation Protocol), which is the most common protocol for VoIP communications. \n\n- Port 20 is used for FTP data transfer. \n- Port 143 is used for IMAP email protocol. \n- Port 445 is used for SMB file sharing, not for VoIP."
    },
    {
        "question": "A network engineer is investigating reports of poor network performance. Upon reviewing a report, the engineer finds that jitter at the office is greater than 10ms on the only WAN connection available. Which of the following would be MOST affected by this statistic?",
        "options": [
            "A VoIP sales call with a customer",
            "An in-office video call with a coworker",
            "Routing table from the ISP",
            "Firewall CPU processing time"
        ],
        "correct_answer": 1,
        "description": "The correct answer is a VoIP sales call with a customer. Jitter affects real-time communication like VoIP, causing delays and distortion in voice quality. \n\n- An in-office video call may also be impacted, but typically less severely than VoIP. \n- Routing tables and firewall processing are unlikely to be directly impacted by jitter."
    },
    {
        "question": "A network technician needs to ensure outside users are unable to telnet into any of the servers at the datacenter. Which of the following ports should be blocked when checking firewall configuration?",
        "options": [
            "22",
            "23",
            "80",
            "3389",
            "8080"
        ],
        "correct_answer": 2,
        "description": "The correct answer is 23. Telnet operates over TCP port 23, so blocking this port will prevent external telnet access to the servers. \n\n- Port 22 is used for SSH, a secure alternative to Telnet. \n- Port 80 is used for HTTP traffic, unrelated to Telnet. \n- Port 3389 is used for RDP (Remote Desktop Protocol), not Telnet. \n- Port 8080 is used for alternative HTTP services."
    },
    {
        "question": "A technician is writing documentation regarding a company's server farm. The technician needs to confirm the server name for all Linux servers. Which of the following commands should the technician run?",
        "options": [
            "ipconfig",
            "nslookup",
            "arp",
            "route"
        ],
        "correct_answer": 2,
        "description": "The correct answer is nslookup. The nslookup command is used to query DNS servers and retrieve information about domain names, including server names. \n\n- ipconfig is a Windows command used to display network configuration. \n- arp is used to view the address resolution protocol table. \n- route is used to display or modify the IP routing table."
    },
    {
        "question": "A technician is connecting multiple switches to create a large network for a new office. The switches are unmanaged Layer 2 switches with multiple connections between each pair. The network is experiencing an extreme amount of latency. Which of the following is MOST likely occurring?",
        "options": [
            "Ethernet collisions",
            "A DDoS attack",
            "A broadcast storm",
            "Routing loops"
        ],
        "correct_answer": 3,
        "description": "The correct answer is a broadcast storm. A broadcast storm occurs when broadcast packets flood the network, causing excessive traffic and latency. This is likely due to the multiple connections between unmanaged switches creating loops. \n\n- Ethernet collisions can cause network delays, but are not typically the main cause of latency in this scenario. \n- A DDoS attack would result in excessive external traffic, not internal network issues. \n- Routing loops are more relevant to Layer 3 devices (routers), not unmanaged Layer 2 switches."
    },

    {
        "question": "A store owner would like to have secure wireless access available for both business equipment and patron use. Which of the following features should be configured to allow different wireless access through the same equipment?",
        "options": [
            "MIMO",
            "TKIP",
            "LTE",
            "SSID"
        ],
        "correct_answer": 4,
        "description": "The correct answer is SSID. Configuring different SSIDs allows separate networks for business equipment and patrons, using the same wireless equipment. \n\n- MIMO improves wireless data throughput but does not segregate access for different user groups. \n- TKIP is an encryption protocol used for securing wireless networks, not for separating network access. \n- LTE is a cellular technology, not related to configuring wireless networks."
    },
    {
        "question": "Which of the following systems would MOST likely be found in a screened subnet?",
        "options": [
            "RADIUS",
            "FTP",
            "SQL",
            "LDAP"
        ],
        "correct_answer": 1,
        "description": "The correct answer is RADIUS. RADIUS is used for centralized authentication, typically found in a screened subnet for security reasons. \n\n- FTP, SQL, and LDAP are often used in internal networks, not typically found in a screened subnet, which is designed to protect services like authentication."
    },
    {
        "question": "Which of the following would need to be configured to ensure a device with a specific MAC address is always assigned the same IP address from DHCP?",
        "options": [
            "Scope options",
            "Reservation",
            "Dynamic assignment",
            "Exclusion",
            "Static assignment"
        ],
        "correct_answer": 2,
        "description": "The correct answer is Reservation. A reservation in DHCP ensures that a device with a specific MAC address receives the same IP address every time it connects to the network. \n\n- Scope options define parameters for an entire subnet, not individual devices. \n- Dynamic assignment is for automatic IP assignment without ensuring consistency. \n- Exclusion prevents specific IPs from being assigned but does not guarantee a fixed address. \n- Static assignment requires manual IP configuration on the device itself, bypassing DHCP."
    },
    {
        "question": "Access to a datacenter should be individually recorded by a card reader even when multiple employees enter the facility at the same time. Which of the following allows the enforcement of this policy?",
        "options": [
            "Motion detection",
            "Access control vestibules",
            "Smart lockers",
            "Cameras"
        ],
        "correct_answer": 2,
        "description": "The correct answer is Access control vestibules. These ensure that each individual is recorded entering the datacenter, even when multiple people enter simultaneously. \n\n- Motion detection is used for security, but it does not enforce individual access records. \n- Smart lockers are used for securing items, not controlling access to facilities. \n- Cameras can record activity but do not directly enforce access control."
    },
    {
        "question": "After the A record of a public website was updated, some visitors were unable to access the website. Which of the following should be adjusted to address the issue?",
        "options": [
            "TTL",
            "MX",
            "TXT",
            "SOA"
        ],
        "correct_answer": 1,
        "description": "The correct answer is TTL (Time To Live). TTL controls how long DNS information is cached. After updating the A record, adjusting the TTL will ensure the changes propagate more quickly. \n\n- MX records are used for email routing, not website access. \n- TXT records are for storing text data, not for resolving website addresses. \n- SOA records define authoritative DNS server information but are not related to propagation speed of DNS updates."
    },
    {
        "question": "A network administrator is installing a wireless network at a client's office. Which of the following IEEE 802.11 standards would be BEST to use for multiple simultaneous client access?",
        "options": [
            "CDMA",
            "CSMA/CD",
            "CSMA/CA",
            "GSM"
        ],
        "correct_answer": 3,
        "description": "The correct answer is CSMA/CA (Carrier Sense Multiple Access with Collision Avoidance). This protocol is designed to manage wireless networks and prevent collisions, allowing multiple clients to access the network simultaneously. \n\n- CDMA is a cellular technology used for voice and data communication, not for wireless LANs. \n- CSMA/CD is used in wired Ethernet networks, not in wireless environments. \n- GSM is another cellular technology and does not apply to local area networks."
    },
    {
        "question": "A technician is installing multiple UPS units in a major retail store. The technician is required to keep track of all changes to new and old equipment. Which of the following will allow the technician to record these changes?",
        "options": [
            "Asset tags",
            "A smart locker",
            "An access control vestibule",
            "A camera"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Asset tags. Asset tags are used to track equipment, helping the technician record changes and manage inventory. \n\n- A smart locker is for securely storing items, not for tracking equipment changes. \n- An access control vestibule is used for managing entry to facilities, not for equipment tracking. \n- A camera can record actions but does not provide a systematic method for tracking equipment changes."
    },
    {
        "question": "Which of the following attacks encrypts user data and requires a proper backup implementation to recover?",
        "options": [
            "DDoS",
            "Phishing",
            "Ransomware",
            "MAC spoofing"
        ],
        "correct_answer": 3,
        "description": "The correct answer is Ransomware. Ransomware encrypts user data and demands payment for its decryption. A proper backup system is crucial for recovery. \n\n- DDoS attacks flood a network with traffic, preventing access to resources, but do not encrypt data. \n- Phishing is a social engineering attack designed to steal credentials, not encrypt data. \n- MAC spoofing alters network hardware addresses and is unrelated to encrypting user data."
    },
    {
        "question": "A network administrator wants to analyze attacks directed toward the company's network. Which of the following must the network administrator implement to assist in this goal?",
        "options": [
            "A honeypot",
            "Network segmentation",
            "Antivirus",
            "A screened subnet"
        ],
        "correct_answer": 1,
        "description": "The correct answer is a Honeypot. A honeypot is a security resource that appears vulnerable to attackers and is used to analyze attack methods and behaviors. \n\n- Network segmentation is used to separate network areas for security, but it doesn't specifically monitor attacks. \n- Antivirus software detects and prevents malware but does not focus on analyzing attacks. \n- A screened subnet is used to protect internal networks, but it isn't used to analyze attack patterns."
    },
{
    "question": "A workstation is configured with the following network details:\n\nIP Address     Subnet mask     Default gateway\n10.1.2.23       10.1.2.0/27           10.1.2.1\n\nSoftware on the workstation needs to send a query to the local subnet broadcast address. To which of the following addresses should the software be configured to send the query?",
    "options": [
        "10.1.2.0",
        "10.1.2.1",
        "10.1.2.23",
        "10.1.2.255",
        "10.1.2.31"
    ],
    "correct_answer": 4,
    "description": "The correct answer is 10.1.2.255. In a subnet with a /27 mask, the broadcast address is always the highest address in the range, which is 10.1.2.255 for this subnet. \n\n- 10.1.2.0 is the network address, not the broadcast address, and should not be used for sending queries. \n- 10.1.2.1 is the default gateway, which is used for routing traffic outside the subnet, not for broadcasting within the subnet. \n- 10.1.2.23 is the workstation's IP address, which is the source of the query, not the destination address for broadcasting. \n- 10.1.2.31 is outside the subnet range (since the subnet mask is /27), making it an invalid address for this network."
},


    {
        "question": "A network administrator is configuring a database server and would like to ensure the database engine is listening on a certain port. Which of the following commands should the administrator use to accomplish this goal?",
        "options": [
            "nslookup",
            "netstat -a",
            "ipconfig /a",
            "arp -a"
        ],
        "correct_answer": 2,
        "description": "The correct answer is netstat -a. This command displays all active connections and listening ports, allowing the administrator to confirm if the database engine is listening on the desired port. \n\n- nslookup is used for DNS queries, not for checking network ports. \n- ipconfig /a is not a valid command and would not help in this context. \n- arp -a shows the ARP table and is unrelated to checking listening ports on a server."
    },
    {
        "question": "A technician is implementing a new wireless network to serve guests at a local office. The network needs to provide Internet access but disallow associated stations from communicating with each other. Which of the following would BEST accomplish this requirement?",
        "options": [
            "Wireless client isolation",
            "Port security",
            "Device geofencing",
            "DHCP snooping"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Wireless client isolation. This feature ensures that wireless clients can connect to the internet but are isolated from one another, preventing peer-to-peer communication. \n\n- Port security limits access to devices based on MAC addresses but does not affect communication between clients. \n- Device geofencing restricts access based on location and is not relevant to isolating wireless clients. \n- DHCP snooping is a security feature that helps prevent rogue DHCP servers but does not address client isolation."
    },
    {
        "question": "A company requires a disaster recovery site to have equipment ready to go in the event of a disaster at its main datacenter. The company does not have the budget to mirror all the live data to the disaster recovery site. Which of the following concepts should the company select?",
        "options": [
            "Cold site",
            "Hot site",
            "Warm site",
            "Cloud site"
        ],
        "correct_answer": 3,
        "description": "The correct answer is Warm site. A warm site is equipped with hardware and infrastructure, but it does not have up-to-date data mirroring. It provides a cost-effective solution for disaster recovery without the expense of a fully replicated hot site. \n\n- Cold site provides basic infrastructure but requires setup and data restoration, making it slower for recovery. \n- Hot site mirrors live data and is ready to take over immediately, but it is more expensive. \n- Cloud site is not a defined disaster recovery concept and is less specific than warm sites."
    },
    {
        "question": "An IT technician suspects a break in one of the uplinks that provides connectivity to the core switch. Which of the following command-line tools should the technician use to determine where the incident is occurring?",
        "options": [
            "nslookup",
            "show config",
            "netstat",
            "show interface",
            "show counters"
        ],
        "correct_answer": 4,
        "description": "The correct answer is show interface. This command provides detailed information about the interfaces on a network device, helping the technician identify uplink failures or issues. \n\n- nslookup is used for DNS queries, not troubleshooting network interfaces. \n- show config displays configuration details but does not provide real-time interface status. \n- netstat shows active network connections, not interface health. \n- show counters displays traffic statistics but is not as specific to interface problems as show interface."
    },
    {
        "question": "A technician is connecting DSL for a new customer. After installing and connecting the on-premises equipment, the technician verifies DSL synchronization. When connecting to a workstation, however, the link LEDs on the workstation and modem do not light up. Which of the following should the technician perform during troubleshooting?",
        "options": [
            "Identify the switching loops between the modem and the workstation.",
            "Check for asymmetrical routing on the modem.",
            "Look for a rogue DHCP server on the network.",
            "Replace the cable connecting the modem and the workstation."
        ],
        "correct_answer": 4,
        "description": "The correct answer is Replace the cable connecting the modem and the workstation. A faulty or damaged cable could prevent proper connectivity between the modem and workstation, which is why the LEDs are not lighting up. \n\n- Switching loops could cause network issues but are not related to the LED lights not lighting up. \n- Asymmetrical routing would affect network traffic but is not related to the physical connection between the modem and workstation. \n- A rogue DHCP server could cause IP assignment issues, but this would not affect the physical link LEDs directly."
    },
    {
        "question": "Which of the following services can provide data storage, hardware options, and scalability to a third-party company that cannot afford new devices?",
        "options": [
            "SaaS",
            "IaaS",
            "PaaS",
            "DaaS"
        ],
        "correct_answer": 2,
        "description": "The correct answer is IaaS (Infrastructure as a Service). IaaS offers data storage, hardware options, and scalability, providing the resources needed by a third-party company without having to purchase physical hardware. \n\n- SaaS (Software as a Service) provides software applications over the internet, but it does not focus on hardware resources or data storage. \n- PaaS (Platform as a Service) offers development platforms for building applications, not direct hardware or data storage. \n- DaaS (Desktop as a Service) offers virtual desktop infrastructure, not broad hardware resources."
    },
    {
        "question": "A network administrator is talking to different vendors about acquiring technology to support a new project for a large company. Which of the following documents will MOST likely need to be signed before information about the project is shared?",
        "options": [
            "BYOD policy",
            "NDA",
            "SLA",
            "MOU"
        ],
        "correct_answer": 2,
        "description": "The correct answer is NDA (Non-Disclosure Agreement). An NDA ensures that sensitive information about the project is not disclosed to unauthorized parties, making it a standard document when sharing project details with vendors. \n\n- A BYOD (Bring Your Own Device) policy applies to personal device usage and is unrelated to sharing project details. \n- An SLA (Service Level Agreement) outlines the level of service expected from vendors, but it is not for confidentiality. \n- An MOU (Memorandum of Understanding) outlines the intent of an agreement but is not as focused on confidentiality as an NDA."
    },
    {
        "question": "Two remote offices need to be connected securely over an untrustworthy MAN. Each office needs to access network shares at the other site. Which of the following will BEST provide this functionality?",
        "options": [
            "Client-to-site VPN",
            "Third-party VPN service",
            "Site-to-site VPN",
            "Split-tunnel VPN"
        ],
        "correct_answer": 3,
        "description": "The correct answer is Site-to-site VPN. A site-to-site VPN connects two networks securely over an untrusted network, allowing both offices to access network shares at each site. \n\n- Client-to-site VPN connects an individual user to a network, not two remote offices. \n- Third-party VPN services offer VPN connectivity but are not specifically designed for inter-office networking. \n- Split-tunnel VPN allows users to access multiple networks but does not focus on securely connecting two remote offices."
    },
    {
        "question": "A network requirement calls for segmenting departments into different networks. The campus network is set up with users of each department in multiple buildings. Which of the following should be configured to keep the design simple and efficient?",
        "options": [
            "MDIX",
            "Jumbo frames",
            "Port tagging",
            "Flow control"
        ],
        "correct_answer": 3,
        "description": "The correct answer is Port tagging. Port tagging allows different VLANs to be assigned to specific departments across multiple buildings, enabling network segmentation in a simple and efficient manner. \n\n- MDIX (Medium Dependent Interface Crossover) is related to cable types and does not help with network segmentation. \n- Jumbo frames deal with large packet sizes and are not directly related to segmenting networks. \n- Flow control manages traffic congestion but does not provide segmentation."
    },
    {
        "question": "Which of the following protocols will a security appliance that is correlating network events from multiple devices MOST likely rely on to receive event messages?",
        "options": [
            "Syslog",
            "Session Initiation Protocol",
            "Secure File Transfer Protocol",
            "Server Message Block"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Syslog. Syslog is a standard protocol for sending event messages to centralized log management systems, making it ideal for correlating network events. \n\n- Session Initiation Protocol (SIP) is used for setting up voice and video calls, not for event logging. \n- Secure File Transfer Protocol (SFTP) is used for secure file transfers, not for event message correlation. \n- Server Message Block (SMB) is used for file sharing and network communication, not for logging events."
    }


]

