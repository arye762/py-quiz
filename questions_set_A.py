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
        "description": "The correct answer is Reverse Address Resolution Protocol ( RARP). This protocol helps map MAC addresses to IP addresses, which can assist in identifying inconsistencies caused by MAC spoofing. \n\n- ICMP is used for network diagnostics, not detecting MAC spoofing. \n- DHCP assigns IP addresses dynamically but does not directly detect spoofing. \n- IMAP is unrelated to network layer security."
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
    },

#100 - 200

{
        "question": "Which of the following is MOST commonly used to address CVEs on network equipment and/or operating systems?",
        "options": [
            "Vulnerability assessment",
            "Factory reset",
            "Firmware update",
            "Screened subnet"
        ],
        "correct_answer": 3,
        "description": "The correct answer is Firmware update. Firmware updates patch known vulnerabilities identified by CVEs, enhancing the security and functionality of network equipment and operating systems. \n\n- Vulnerability assessment identifies vulnerabilities but does not resolve them. \n- Factory reset restores default settings but does not address vulnerabilities. \n- Screened subnet is a network design concept unrelated to CVE resolution."
    },
    {
        "question": "A network technician is investigating an issue with handheld devices in a warehouse. Devices have not been connecting to the nearest APs but have been connecting to an AP on the far side of the warehouse. Which of the following is the MOST likely cause of this issue?",
        "options": [
            "The nearest APs are configured for 802.11g.",
            "An incorrect channel assignment is on the nearest APs.",
            "The power level is too high for the AP on the far side.",
            "Interference exists around the AP on the far side."
        ],
        "correct_answer": 3,
        "description": "The correct answer is The power level is too high for the AP on the far side. High power levels cause devices to connect to farther APs instead of closer ones, which impacts connectivity efficiency. \n\n- 802.11g AP configuration would limit speed, not range. \n- Incorrect channel assignment affects interference but not connectivity to distant APs. \n- Interference around the AP on the far side would reduce its effectiveness rather than cause the issue described."
    },
    {
        "question": "Which of the following uses the destination IP address to forward packets?",
        "options": [
            "A bridge",
            "A Layer 2 switch",
            "A router",
            "A repeater"
        ],
        "correct_answer": 3,
        "description": "The correct answer is A router. Routers forward packets based on destination IP addresses, enabling communication between different networks. \n\n- Bridges forward data at Layer 2 using MAC addresses. \n- Layer 2 switches use MAC addresses, not IP addresses, for packet forwarding. \n- Repeaters regenerate signals without considering IP addresses."
    },
    {
        "question": "Which of the following OSI model layers is where conversations between applications are established, coordinated, and terminated?",
        "options": [
            "Session",
            "Physical",
            "Presentation",
            "Data link"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Session. The session layer manages and maintains communication sessions between applications. \n\n- Physical layer deals with the transmission of raw data. \n- Presentation layer handles data translation and encryption. \n- Data link layer ensures reliable data transfer within the same network."
    },
    {
        "question": "A business is using the local cable company to provide Internet access. Which of the following types of cabling will the cable company MOST likely use from the demarcation point back to the central office?",
        "options": [
            "Multimode",
            "Cat 5e",
            "RG-6",
            "Cat 6",
            "100BASE-T"
        ],
        "correct_answer": 3,
        "description": "The correct answer is RG-6. RG-6 coaxial cable is commonly used by cable companies for reliable transmission of internet and TV signals over long distances. \n\n- Multimode fiber is used for high-speed, short-distance data transmission. \n- Cat 5e and Cat 6 cables are for Ethernet connections within buildings, not for ISP infrastructure. \n- 100BASE-T refers to a network standard, not a cable type."
    },
    {
        "question": "A network administrator decided to use SLAAC in an extensive IPv6 deployment to alleviate IP address management. The devices were properly connected into the LAN but autoconfiguration of the IP address did not occur as expected. Which of the following should the network administrator verify?",
        "options": [
            "The network gateway is configured to send router advertisements.",
            "A DHCP server is present on the same broadcast domain as the clients.",
            "The devices support dual stack on the network layer.",
            "The local gateway supports anycast routing."
        ],
        "correct_answer": 1,
        "description": "The correct answer is The network gateway is configured to send router advertisements. SLAAC depends on router advertisements to provide network configuration to devices. \n\n- DHCP servers are not required for SLAAC. \n- Dual stack is irrelevant to SLAAC functionality. \n- Anycast routing does not impact IPv6 autoconfiguration."
    },
    {
        "question": "Which of the following is used to provide networking capability for VMs at Layer 2 of the OSI model?",
        "options": [
            "VPN",
            "VRRP",
            "vSwitch",
            "VIP"
        ],
        "correct_answer": 3,
        "description": "The correct answer is vSwitch. A virtual switch operates at Layer 2 to connect virtual machines within the same host or across hosts. \n\n- VPN and VRRP operate at higher layers for secure communication and redundancy. \n- VIP refers to a virtual IP address, not a Layer 2 networking feature."
    },

    
    {
        "question": "A network administrator is required to ensure that auditors have read-only access to the system logs, while systems administrators have read and write access to the system logs, and operators have no access to the system logs. The network administrator has configured security groups for each of these functional categories. Which of the following security capabilities will allow the network administrator to maintain these permissions with the LEAST administrative effort?",
        "options": [
            "Mandatory access control",
            "User-based permissions",
            "Role-based access",
            "Least privilege"
        ],
        "correct_answer": 3,
        "description": "The correct answer is Role-based access. This approach assigns permissions based on roles rather than individual users, allowing for efficient management of permissions across different functional categories. \n\n- Mandatory access control is highly rigid and better suited for environments with strict security requirements but requires more administrative effort. \n- User-based permissions focus on individual accounts, which increases administrative overhead as the number of users grows. \n- Least privilege is a principle rather than a specific implementation method and would complement role-based access but does not independently solve the problem."
    },
    {
        "question": "Which of the following would be used to expedite MX record updates to authoritative NSs?",
        "options": [
            "UDP forwarding",
            "DNS caching",
            "Recursive lookup",
            "Time to live"
        ],
        "correct_answer": 4,
        "description": "The correct answer is Time to live. Adjusting the TTL value determines how long DNS records are cached by resolvers, allowing changes to propagate more quickly. \n\n- UDP forwarding is unrelated to DNS record updates and is used for routing data packets. \n- DNS caching temporarily stores DNS query results, which can delay updates if not cleared. \n- Recursive lookup is a query process but does not influence the speed of record propagation."
    },
    {
        "question": "A client moving into a new office wants the IP network set up to accommodate 412 network-connected devices that are all on the same subnet. The subnet needs to be as small as possible. Which of the following subnet masks should be used to achieve the required result?",
        "options": [
            "255.255.0.0",
            "255.255.252.0",
            "255.255.254.0",
            "255.255.255.0"
        ],
        "correct_answer": 3,
        "description": "The correct answer is 255.255.254.0. This subnet mask provides 510 usable IP addresses (512 total, minus 2 for network and broadcast), which is the smallest subnet that can accommodate 412 devices. \n\n- 255.255.0.0 provides over 65,000 addresses, far exceeding the requirements and wasting IP space. \n- 255.255.252.0 provides 1022 usable addresses, which is unnecessarily large. \n- 255.255.255.0 provides only 254 usable addresses, which is insufficient for 412 devices."
    },




    {
        "question": "A company is being acquired by a large corporation. As part of the acquisition process, the company's address should now redirect clients to the corporate organization page. Which of the following DNS records needs to be created?",
        "options": [
            "SOA",
            "NS",
            "CNAME",
            "TXT"
        ],
        "correct_answer": 3,
        "description": "The correct answer is CNAME. A Canonical Name (CNAME) record is used to alias one domain name to another, allowing the company's address to redirect clients to the corporate organization page. \n\n- SOA (Start of Authority) defines the primary DNS server for a zone and is unrelated to redirection. \n- NS (Name Server) specifies the authoritative DNS servers for a domain but does not handle redirection. \n- TXT records are used to store text data in DNS, often for verification, not redirection."
    },
    {
        "question": "A user is having difficulty with video conferencing and is looking for assistance. Which of the following would BEST improve performance?",
        "options": [
            "Packet shaping",
            "Quality of service",
            "Port mirroring",
            "Load balancing"
        ],
        "correct_answer": 2,
        "description": "The correct answer is Quality of Service (QoS). QoS prioritizes network traffic, ensuring that video conferencing data receives higher priority and reducing latency and jitter. \n\n- Packet shaping controls bandwidth usage but does not prioritize specific traffic like QoS. \n- Port mirroring duplicates traffic for analysis and does not improve performance. \n- Load balancing distributes traffic across servers but does not prioritize specific application traffic."
    },
    {
        "question": "A network technician is configuring a new firewall for a company with the necessary access requirements to be allowed through the firewall. Which of the following would normally be applied as the LAST rule in the firewall?",
        "options": [
            "Secure SNMP",
            "Port security",
            "Implicit deny",
            "DHCP snooping"
        ],
        "correct_answer": 3,
        "description": "The correct answer is Implicit deny. This rule blocks any traffic that does not match any of the preceding allow rules, ensuring no unintended access is granted. \n\n- Secure SNMP relates to managing devices but is not a firewall rule. \n- Port security protects switch ports but is unrelated to firewall configurations. \n- DHCP snooping prevents unauthorized DHCP servers but is not relevant to firewall rule placement."
    },
    {
        "question": "A technician wants to install a WAP in the center of a room that provides service in a radius surrounding a radio. Which of the following antenna types should the AP utilize?",
        "options": [
            "Omni",
            "Directional",
            "Yagi",
            "Parabolic"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Omni. Omnidirectional antennas distribute the signal evenly in all directions, making them ideal for centrally located WAPs. \n\n- Directional antennas focus the signal in one direction, unsuitable for even coverage. \n- Yagi antennas are highly directional and used for long-range point-to-point connections. \n- Parabolic antennas are used for highly focused, long-distance connections."
    },
    {
        "question": "A systems administrator is running a VoIP network and is experiencing jitter and high latency. Which of the following would BEST help the administrator determine the cause of these issues?",
        "options": [
            "Enabling RADIUS on the network",
            "Configuring SNMP traps on the network",
            "Implementing LDAP on the network",
            "Establishing NTP on the network"
        ],
        "correct_answer": 2,
        "description": "The correct answer is Configuring SNMP traps. SNMP traps monitor network devices for performance issues, helping identify jitter and latency problems. \n\n- RADIUS is used for authentication and does not address VoIP performance. \n- LDAP manages directory services and is unrelated to latency. \n- NTP synchronizes time across devices but does not directly address jitter or latency."
    },
    {
        "question": "The following instructions were published about the proper network configuration for a videoconferencing device: 'Configure a valid static RFC1918 address for your network. Check the option to use a connection over NAT.' Which of the following is a valid IP address configuration for the device?",
        "options": [
            "FE80::1",
            "100.64.0.1",
            "169.254.1.2",
            "172.19.0.2",
            "224.0.0.12"
        ],
        "correct_answer": 4,
        "description": "The correct answer is 172.19.0.2. This address is within the RFC1918 private IP range, suitable for static configuration behind NAT. \n\n- FE80::1 is an IPv6 link-local address, not an RFC1918 address. \n- 100.64.0.1 is in the Carrier-Grade NAT range, not for private use. \n- 169.254.1.2 is an APIPA address, unsuitable for static configurations. \n- 224.0.0.12 is a multicast address, not a private IP address."
    },
    {
        "question": "A network administrator is reviewing interface errors on a switch. Which of the following indicates that a switchport is receiving packets in excess of the configured MTU?",
        "options": [
            "CRC errors",
            "Giants",
            "Runts",
            "Flooding"
        ],
        "correct_answer": 2,
        "description": "The correct answer is Giants. These are packets larger than the Maximum Transmission Unit (MTU) size, causing errors. \n\n- CRC errors indicate data corruption but do not specifically relate to packet size. \n- Runts are packets smaller than the minimum frame size, unrelated to MTU. \n- Flooding occurs when excess traffic is sent to all ports, not related to MTU."
    },
    {
        "question": "A network administrator needs to implement an HDMI over IP solution. Which of the following will the network administrator MOST likely use to ensure smooth video delivery?",
        "options": [
            "Link aggregation control",
            "Port tagging",
            "Jumbo frames",
            "Media access control"
        ],
        "correct_answer": 3,
        "description": "The correct answer is Jumbo frames. These larger packets reduce overhead, making them ideal for high-bandwidth applications like HDMI over IP. \n\n- Link aggregation control combines multiple connections but does not optimize packet delivery. \n- Port tagging organizes traffic but does not directly affect video delivery. \n- Media access control refers to network access control mechanisms, unrelated to HDMI over IP."
    },
    {
        "question": "A network administrator wants to reduce overhead and increase efficiency on a SAN. Which of the following can be configured to achieve these goals?",
        "options": [
            "Port aggregation",
            "Traffic shaping",
            "Jumbo frames",
            "Flow control"
        ],
        "correct_answer": 3,
        "description": "The correct answer is Jumbo frames. Larger packets reduce overhead, improving SAN efficiency. \n\n- Port aggregation combines links for bandwidth but does not directly affect packet overhead. \n- Traffic shaping controls bandwidth but does not optimize packet size. \n- Flow control manages traffic congestion but does not address overhead."
    },
    {
        "question": "A rogue AP was found plugged in and providing Internet access to employees in the break room. Which of the following would be BEST to use to stop this from happening without physically removing the WAP?",
        "options": [
            "Password complexity",
            "Port security",
            "Wireless client isolation",
            "Secure SNMP"
        ],
        "correct_answer": 2,
        "description": "The correct answer is Port security. This feature restricts access to the network by identifying allowed devices, preventing unauthorized access points. \n\n- Password complexity secures accounts but does not block rogue devices. \n- Wireless client isolation prevents devices from communicating but does not address rogue APs. \n- Secure SNMP is for network management, not rogue device prevention."
    },







    
    {
        "question": "A company's network is set up so all Internet-bound traffic from all remote offices exits through a main datacenter. Which of the following network topologies would BEST describe this setup?",
        "options": [
            "Bus",
            "Spine-and-leaf",
            "Hub-and-spoke",
            "Mesh"
        ],
        "correct_answer": 3,
        "description": "The correct answer is Hub-and-spoke. This topology connects remote offices (spokes) to a central location (hub), which routes all Internet-bound traffic. \n\n- Bus topology is not applicable as it connects devices in a linear sequence. \n- Spine-and-leaf is designed for modern data centers, not WAN setups. \n- Mesh topology provides multiple direct connections, making it unnecessary for all traffic to pass through a central hub."
    },
    {
        "question": "To comply with industry requirements, a security assessment on the cloud server should identify which protocols and weaknesses are being exposed to attackers on the Internet. Which of the following tools is the MOST appropriate to complete the assessment?",
        "options": [
            "Use tcpdump and parse the output file in a protocol analyzer.",
            "Use an IP scanner and target the cloud WAN network addressing.",
            "Run netstat in each cloud server and retrieve the running processes.",
            "Use nmap and set the servers' public IPs as the targets."
        ],
        "correct_answer": 4,
        "description": "The correct answer is nmap. It is a versatile tool used for scanning networks to identify open ports, services, and potential vulnerabilities. \n\n- Tcpdump captures packets but does not provide detailed protocol analysis for exposure to attackers. \n- IP scanners identify live hosts but lack the depth to assess protocol weaknesses. \n- Netstat shows running processes locally but does not scan for vulnerabilities across public-facing IPs."
    },
    {
        "question": "A systems administrator is configuring a firewall using NAT with PAT. Which of the following would be BEST suited for the LAN interface?",
        "options": [
            "172.15.0.0/18",
            "172.18.0.0/10",
            "172.23.0.0/16",
            "172.28.0.0/8",
            "172.32.0.0/14"
        ],
        "correct_answer": 3,
        "description": "The correct answer is 172.23.0.0/16. This is part of the private IP range (172.16.0.0 to 172.31.255.255) and is suitable for use in internal LAN configurations with NAT. \n\n- The other options include invalid or non-private IP ranges, making them unsuitable for NAT with PAT configurations."
    },
    {
        "question": "A packet is assigned a value to ensure it does not traverse a network indefinitely. Which of the following BEST represents this value?",
        "options": [
            "Zero Trust",
            "Planned obsolescence",
            "Time to live",
            "Caching"
        ],
        "correct_answer": 3,
        "description": "The correct answer is Time to live (TTL). This value prevents packets from circulating endlessly by decrementing at each hop and discarding packets when TTL reaches zero. \n\n- Zero Trust is a security model, not related to packet traversal. \n- Planned obsolescence relates to product lifecycle. \n- Caching involves storing data temporarily for faster access."
    },
    {
        "question": "Which of the following policies should be referenced when a user wants to access work email on a personal cell phone?",
        "options": [
            "Offboarding policy",
            "Acceptable use policy",
            "BYOD policy",
            "Remote access policy"
        ],
        "correct_answer": 3,
        "description": "The correct answer is BYOD policy. This policy outlines the rules and guidelines for using personal devices to access work resources, including email. \n\n- Offboarding policy applies when an employee leaves the organization. \n- Acceptable use policy governs the general use of IT systems. \n- Remote access policy defines secure connections for offsite work but does not address personal devices specifically."
    },
    {
        "question": "After a firewall replacement, some alarms and metrics related to network availability stopped updating on a monitoring system relying on SNMP. Which of the following should the network administrator do FIRST?",
        "options": [
            "Modify the device's MIB on the monitoring system.",
            "Configure syslog to send events to the monitoring system.",
            "Use port mirroring to redirect traffic to the monitoring system.",
            "Deploy SMB to transfer data to the monitoring system."
        ],
        "correct_answer": 1,
        "description": "The correct answer is to modify the device's MIB on the monitoring system. This ensures the new firewall's SNMP configurations align with the monitoring system's expectations. \n\n- Syslog configuration sends log data but does not address SNMP issues. \n- Port mirroring captures traffic for analysis but does not directly resolve SNMP alarms. \n- SMB is unrelated to SNMP or monitoring systems."
    },
    {
        "question": "At the destination host, which of the following OSI model layers will discard a segment with a bad checksum in the UDP header?",
        "options": [
            "Network",
            "Data link",
            "Transport",
            "Session"
        ],
        "correct_answer": 3,
        "description": "The correct answer is Transport. This layer ensures error checking for segments, and a bad checksum leads to packet discard. \n\n- Network handles packet routing, not error checking for transport-layer protocols. \n- Data link focuses on frame-level errors. \n- Session establishes and maintains communication sessions but does not handle checksum errors."
    },
    {
        "question": "Which of the following VPN configurations should be used to separate Internet and corporate traffic?",
        "options": [
            "Split-tunnel",
            "Remote desktop gateway",
            "Site-to-site",
            "Out-of-band management"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Split-tunnel. This VPN configuration allows corporate traffic to route through the VPN while Internet-bound traffic bypasses it. \n\n- Remote desktop gateway is for accessing remote desktops, not VPN traffic separation. \n- Site-to-site connects two LANs securely but does not separate traffic. \n- Out-of-band management is used for secure device management, not VPN setups."
    },
    {
        "question": "Which of the following is required when connecting an endpoint device with an RJ45 port to a network device with an ST port?",
        "options": [
            "A media converter",
            "A bridge",
            "An MDIX",
            "A load balancer"
        ],
        "correct_answer": 1,
        "description": "The correct answer is a media converter. It is used to bridge different types of network media, such as RJ45 (Ethernet) to ST (fiber). \n\n- A bridge connects two LAN segments but does not convert media types. \n- An MDIX automatically adjusts crossover cables but is irrelevant here. \n- A load balancer distributes traffic but does not connect different media types."
    },






    {
    "question": "A voice engineer is troubleshooting a phone issue. When a call is placed, the caller hears echoes of the receiver's voice. Which of the following are the causes of this issue? (Choose two.)",
    "options": [
        "Jitter",
        "Speed mismatch",
        "QoS misconfiguration",
        "Protocol mismatch",
        "CRC errors",
        "Encapsulation errors"
    ],
    "correct_answer": [1, 3],
    "description": "The correct answers are Jitter and QoS misconfiguration. \n\n- Jitter occurs when there is variation in the delay of packet delivery, which can cause audio to be delayed or echoed. \n- QoS (Quality of Service) misconfiguration can affect the prioritization of voice traffic, leading to poor call quality, including echoes. \n\n- Speed mismatch can cause call quality issues but is less likely to result in echoes. \n- Protocol mismatch typically leads to connection failures, not audio issues. \n- CRC errors and encapsulation errors are more related to packet integrity or frame issues, not echoing during calls."
    },




    {
        "question": "The management team has instituted a 48-hour RTO as part of the disaster recovery plan. Which of the following procedures would meet the policy's requirements?",
        "options": [
            "Recover all systems to a loss of 48 hours of data.",
            "Limit network downtime to a maximum of 48 hours per year.",
            "Recover all systems within 48 hours.",
            "Require 48 hours of system backup maintenance."
        ],
        "correct_answer": 3,
        "description": "The correct answer is 'Recover all systems within 48 hours.' \n\n- The RTO (Recovery Time Objective) refers to the maximum acceptable downtime for systems following a disaster. The goal is to restore all systems within this time frame. \n- Recovering systems to a loss of 48 hours of data is not directly related to the RTO, as it focuses on data loss rather than downtime. \n- Limiting network downtime to 48 hours per year does not address the RTO, which is about the recovery time after an incident. \n- System backup maintenance is unrelated to the actual RTO requirement for recovery."
    },
    {
        "question": "Which of the following cable types would MOST likely be used to provide high-speed network connectivity between nearby buildings?",
        "options": [
            "UTP",
            "Coaxial",
            "Fiber",
            "Cat 5",
            "Twinaxial"
        ],
        "correct_answer": 3,
        "description": "The correct answer is Fiber. \n\n- Fiber optic cables provide high-speed connectivity with significantly higher bandwidth compared to other options, making them ideal for linking buildings. \n- UTP (Unshielded Twisted Pair) and Cat 5 cables are suitable for shorter distances and lower bandwidth, making them less ideal for connecting buildings. \n- Coaxial cables are often used for cable TV and some Internet connections but are not the best option for high-speed networking. \n- Twinaxial is used for short-range high-speed connections but is not commonly used between buildings."
    },
    {
        "question": "Which of the following is the physical security mechanism that would MOST likely be used to enter a secure site?",
        "options": [
            "A landing page",
            "An access control vestibule",
            "A smart locker",
            "A firewall"
        ],
        "correct_answer": 2,
        "description": "The correct answer is 'An access control vestibule.' \n\n- An access control vestibule is a secure entry point that typically controls who can enter a building or facility, ensuring only authorized personnel are allowed access. \n- A landing page is a web page and does not have physical security applications. \n- A smart locker is used for securing items, not for access control. \n- A firewall is a network security device, not a physical security mechanism."
    },
    {
        "question": "Which of the following BEST describes a North-South traffic flow?",
        "options": [
            "A public Internet user accessing a published web server",
            "A database server communicating with another clustered database server",
            "A Layer 3 switch advertising routes to a router",
            "A management application connecting to managed devices"
        ],
        "correct_answer": 1,
        "description": "The correct answer is 'A public Internet user accessing a published web server.' \n\n- North-South traffic flow refers to the data flow between internal network resources (such as servers) and external networks (such as the Internet). \n- A database server communicating with another database server or a switch advertising routes describes internal communication (East-West traffic). \n- A management application connecting to managed devices is internal communication and does not describe North-South traffic flow."
    },
    {
        "question": "A network switch was installed to provide connectivity to cameras monitoring wildlife in a remote location. The organization is concerned that intruders could potentially leverage unattended equipment in the remote location to connect rogue devices and gain access to the organization's resources. Which of the following techniques would BEST address the concern?",
        "options": [
            "Configure port security using MAC filtering.",
            "Manually register the cameras on the switch address table.",
            "Activate PoE+ on the active switchports.",
            "Disable Neighbor Discovery Protocol on the switch."
        ],
        "correct_answer": 1,
        "description": "The correct answer is 'Configure port security using MAC filtering.' \n\n- Port security with MAC filtering helps ensure that only authorized devices, identified by their MAC addresses, can connect to the network. This would prevent rogue devices from being connected. \n- Manually registering cameras in the switch address table would not provide proactive security against unauthorized devices. \n- Activating PoE+ (Power over Ethernet) does not address the security concern related to rogue devices. \n- Disabling Neighbor Discovery Protocol is a security measure but is not specifically aimed at preventing rogue device connections in this scenario."
    },
    {
        "question": "A technician is documenting an application that is installed on a server and needs to verify all existing web and database connections to the server. Which of the following tools should the technician use to accomplish this task?",
        "options": [
            "tracert",
            "ipconfig",
            "netstat",
            "nslookup"
        ],
        "correct_answer": 3,
        "description": "The correct answer is 'netstat.' \n\n- Netstat is a command-line tool used to view all active network connections on a system, including web and database connections. \n- Tracert is used to trace the path packets take to a destination and is not suitable for verifying connections. \n- Ipconfig provides information about the network interfaces and configuration but does not show active connections. \n- Nslookup is used to query DNS records, not to verify network connections."
    },
    {
        "question": "A technician is assisting a user who cannot access network resources when the workstation is connected to a VoIP phone. The technician identifies the phone as faulty and replaces it. According to troubleshooting methodology, which of the following should the technician do NEXT?",
        "options": [
            "Implement the solution.",
            "Test the theory.",
            "Duplicate the issue.",
            "Document the findings.",
            "Verify functionality."
        ],
        "correct_answer": 5,
        "description": "The correct answer is 'Verify functionality.' \n\n- After replacing the faulty device, the next step is to verify that the issue is resolved and the system is functioning properly. \n- Implementing the solution is done in the previous step (replacing the phone). \n- Testing the theory would have been done earlier in the troubleshooting process. \n- Duplicating the issue is unnecessary after identifying the cause and replacing the faulty phone. \n- Documenting findings should be done after verifying the solution is effective."
    },
    {
        "question": "Which of the following OSI model layers contains IP headers?",
        "options": [
            "Presentation",
            "Application",
            "Data link",
            "Network",
            "Transport"
        ],
        "correct_answer": 4,
        "description": "The correct answer is 'Network.' \n\n- The IP header is part of the Network layer (Layer 3) of the OSI model, which is responsible for routing and addressing packets. \n- The Presentation and Application layers handle data representation and application-specific functions, not IP headers. \n- The Data link layer deals with MAC addresses and frames, not IP headers. \n- The Transport layer is responsible for segmenting data and ensuring reliable delivery, but it does not deal with IP headers."
    },
    {
        "question": "A small office is running WiFi 4 APs, and neighboring offices do not want to increase the throughput to associated devices. Which of the following is the MOST cost-efficient way for the office to increase network performance?",
        "options": [
            "Add another AP.",
            "Disable the 2.4GHz radios.",
            "Enable channel bonding.",
            "Upgrade to WiFi 5."
        ],
        "correct_answer": 3,
        "description": "The correct answer is 'Enable channel bonding.' \n\n- Channel bonding allows for wider channels and can increase throughput without the need for additional hardware. This is a cost-efficient solution. \n- Adding another AP could increase performance but involves additional cost for the new hardware. \n- Disabling the 2.4GHz radios may reduce interference, but it does not directly improve throughput. \n- Upgrading to WiFi 5 would provide better performance but involves significant cost for new hardware."
    },
    {
        "question": "A network technician is troubleshooting an application issue. The technician is able to recreate the issue in a virtual environment. According to the troubleshooting methodology, which of the following actions will the technician most likely perform NEXT?",
        "options": [
            "Gather information from the initial report.",
            "Escalate the issue to a supervisor.",
            "Implement a solution to resolve the issue.",
            "Establish a theory of probable cause"
        ],
        "correct_answer": 4,
        "description": "The correct answer is 'Establish a theory of probable cause.' \n\n- After recreating the issue, the next step in troubleshooting is to hypothesize the cause of the problem, which helps guide further testing and solutions. \n- Gathering information should be done earlier in the process. \n- Escalation happens if the technician cannot resolve the issue. \n- Implementing a solution occurs after identifying the root cause."
    },




    
    {
        "question": "Which of the following types of datacenter architectures will MOST likely be used in a large SDN and can be extended beyond the datacenter?",
        "options": [
            "iSCSI",
            "FCoE",
            "Three-tiered network",
            "Spine and leaf",
            "Top-of-rack switching"
        ],
        "correct_answer": 4,
        "description": "The correct answer is Spine and leaf. This architecture is optimized for large SDN environments and is scalable beyond the datacenter, making it ideal for such setups. \n\n- iSCSI and FCoE are storage protocols, not network architectures. \n- Three-tiered networks are often used in traditional architectures but are less scalable than Spine and leaf in SDN environments. \n- Top-of-rack switching is used for physical server connections but doesn't offer the same scalability."
    },
    {
        "question": "A network technician reviews an entry on the syslog server and discovers the following message from a switch: SPANNING-TREE Port 1/1 BLOCKED - Which of the following describes the issue?",
        "options": [
            "A loop was discovered, and the impact was mitigated.",
            "An incorrectly pinned cable was disconnected.",
            "The link-local address on the port is incorrect.",
            "The port was shut down, and it needs to be reactivated."
        ],
        "correct_answer": 1,
        "description": "The correct answer is A loop was discovered, and the impact was mitigated. The message indicates that the port has been blocked due to a spanning-tree loop prevention mechanism. \n\n- An incorrectly pinned cable would not typically trigger this syslog message. \n- The link-local address is not related to spanning-tree protocol. \n- If the port was shut down, the message would reflect that state, not blocking due to a loop."
    },
    {
        "question": "A company just migrated its email service to a cloud solution. After the migration, two-thirds of the internal users were able to connect to their mailboxes, but the connection fails for the other one-third of internal users. Users working externally are not reporting any issues. The network administrator identifies the following output collected from an internal host: c:\\user> nslookup newmail.company.com \nNon-Authoritative answer: \n\nName: newmail.company.com - \nIPs: 3.219.13.186, 64.58.225.184, 184.168.131.243 \nWhich of the following verification tasks should the network administrator perform NEXT?",
        "options": [
            "Check the firewall ACL to verify all required IP addresses are included.",
            "Verify the required router PAT rules are properly configured.",
            "Confirm the internal DNS server is replying to requests for the cloud solution.",
            "Validate the cloud console to determine whether there are unlicensed requests."
        ],
        "correct_answer": 3,
        "description": "The correct answer is Confirm the internal DNS server is replying to requests for the cloud solution. Since the external users are not affected, this indicates that internal DNS resolution may be at fault. \n\n- Checking the firewall ACL might be helpful but is less likely to be the cause. \n- PAT rules affect external communications, which aren't the issue here. \n- Unlicensed requests in the cloud console would affect all users, not just internal ones."
    },
    {
        "question": "A network technician was hired to harden the security of a network. The technician is required to enable encryption and create a password for AP security through the web browser. Which of the following would BEST support these requirements?",
        "options": [
            "ESP",
            "WPA2",
            "IPSec",
            "ACL"
        ],
        "correct_answer": 2,
        "description": "The correct answer is WPA2. WPA2 is the most appropriate encryption standard for securing wireless access points and includes password protection. \n\n- ESP is part of IPSec and is not used for AP security. \n- IPSec is used for securing IP traffic, not for securing wireless networks. \n- ACLs can be used for access control but do not provide encryption or password protection for APs."
    },
    {
        "question": "Which of the following ports are associated with IMAP? (Choose two.)",
        "options": [
            "25",
            "110",
            "143",
            "587",
            "993",
            "995"
        ],
        "correct_answer": [3, 6],
        "description": "The correct answers are 143 and 993. IMAP uses port 143 for standard connections and port 993 for secure IMAP (IMAPS) over SSL/TLS. \n\n- Port 25 is used for SMTP, not IMAP. \n- Port 110 is used for POP3, not IMAP. \n- Port 587 is used for SMTP with STARTTLS."
    },
    {
        "question": "A network administrator is trying to identify a device that is having issues connecting to a switchport. Which of the following would BEST help identify the issue?",
        "options": [
            "A syslog server",
            "Change management records",
            "A rack diagram",
            "The security log"
        ],
        "correct_answer": 1,
        "description": "The correct answer is A syslog server. The syslog server can provide logs related to the switchport connection, helping identify why a device cannot connect. \n\n- Change management records might provide insights but are not as direct as syslog data. \n- A rack diagram shows physical placement but doesn't address connection issues. \n- The security log would only be helpful if the issue is security-related."
    },
    {
        "question": "A company with multiple routers would like to implement an HA network gateway with the least amount of downtime possible. This solution should not require changes on the gateway setting of the network clients. Which of the following should a technician configure?",
        "options": [
            "Automate a continuous backup and restore process of the system's state of the active gateway.",
            "Use a static assignment of the gateway IP address on the network clients.",
            "Configure DHCP relay and allow clients to receive a new IP setting.",
            "Configure a shared VIP and deploy VRRP on the routers."
        ],
        "correct_answer": 4,
        "description": "The correct answer is Configure a shared VIP and deploy VRRP on the routers. VRRP allows for high availability by providing a virtual IP address (VIP) that clients can use, and if one router fails, another takes over without needing client-side configuration changes. \n\n- Automating backup and restore doesn't prevent downtime in the case of failure. \n- Static IP addresses do not provide high availability. \n- DHCP relay and IP changes aren't ideal for minimizing downtime."
    },
    {
        "question": "Which of the following protocols would allow a secure connection to a Linux-based system?",
        "options": [
            "SMB",
            "FTP",
            "RDP",
            "SSH"
        ],
        "correct_answer": 4,
        "description": "The correct answer is SSH. SSH is designed for secure remote connections to systems, including Linux. \n\n- SMB is used for file sharing in Windows environments. \n- FTP is an unencrypted protocol and not secure by default. \n- RDP is for remote desktop access and is generally used in Windows environments."
    },
    {
        "question": "A network administrator is troubleshooting the communication between two Layer 2 switches that are reporting a very high runt count. After trying multiple ports on both switches, the issue persists. Which of the following should the network administrator perform to resolve the issue?",
        "options": [
            "Increase the MTU size on both switches.",
            "Recertify the cable between both switches.",
            "Perform a factory reset on both switches.",
            "Enable debug logging on both switches"
        ],
        "correct_answer": 2,
        "description": "The correct answer is Recertify the cable between both switches. A high runt count is often caused by bad cabling, so recertifying the cable can resolve the issue. \n\n- Increasing the MTU size is unlikely to fix runt count problems, as these are typically caused by physical layer issues. \n- A factory reset would not directly address cable or physical layer issues. \n- Debug logging can provide information but is unlikely to resolve the issue."
    },

    {
    "question": "A technician is troubleshooting a client's report about poor wireless performance. Using a client monitor, the technician notes the following information:\n\nSSID\tSignal (RSSI)\tChannel\nCorporate\t-50\t9\nCorporate\t-69\t10\nCorporate\t-67\t11\nCorporate\t-63\t6\n\nWhich of the following is MOST likely the cause of the issue?",
    "options": [
        "Channel overlap.",
        "Poor signal.",
        "Incorrect power settings.",
        "Wrong antenna type."
    ],
    "correct_answer": 1,
    "description": "The correct answer is channel overlap. The client monitor shows that multiple wireless signals from the same SSID are using adjacent channels (9, 10, 11), which could be causing interference and poor performance. \n\n- Poor signal (RSSI values like -69 and -67) may contribute to the issue, but the primary cause appears to be interference from adjacent channels. \n- Incorrect power settings and wrong antenna type are less likely to cause channel overlap, which is the most common culprit for wireless performance issues."
    },





    
    {
        "question": "Users attending security training at work are advised not to use single words as passwords for corporate applications. Which of the following does this BEST protect against?",
        "options": [
            "An on-path attack.",
            "A brute-force attack.",
            "A dictionary attack.",
            "MAC spoofing.",
            "Denial of service."
        ],
        "correct_answer": 3,
        "description": "The correct answer is a dictionary attack. Single-word passwords are vulnerable to dictionary attacks, where attackers use precompiled lists of common words to guess passwords. \n\n- An on-path attack intercepts communication but does not directly exploit weak passwords. \n- A brute-force attack attempts all combinations, but dictionary attacks are more efficient for common words. \n- MAC spoofing and Denial of service are unrelated to password complexity."
    },
    {
        "question": "A network administrator would like to enable NetFlow on a Layer 3 switch but is concerned about how the feature may impact the switch. Which of the following metrics should the administrator graph using SNMP to BEST measure the feature's impact?",
        "options": [
            "CPU usage.",
            "Temperature.",
            "Electrical consumption.",
            "Bandwidth usage."
        ],
        "correct_answer": 1,
        "description": "The correct answer is CPU usage. Enabling NetFlow can increase the CPU load on the switch due to the extra processing required to monitor and record traffic flows. \n\n- Temperature, electrical consumption, and bandwidth usage are not directly impacted by NetFlow configuration, making them less relevant for measuring the feature's impact."
    },
    {
        "question": "Which of the following would be used to enforce and schedule critical updates with supervisory approval and include backup plans in case of failure?",
        "options": [
            "Business continuity plan.",
            "Onboarding and offboarding policies.",
            "Acceptable use policy.",
            "System life cycle.",
            "Change management."
        ],
        "correct_answer": 5,
        "description": "The correct answer is change management. Change management ensures that updates are scheduled, approved, and have backup plans in case of failure. \n\n- Business continuity plans focus on maintaining operations during disasters, not specifically on updates. \n- Onboarding/offboarding policies and acceptable use policies are not directly related to updating systems. \n- System life cycle outlines the stages of a system but doesn’t focus on update scheduling."
    },
    {
        "question": "A newly installed VoIP phone is not getting the DHCP IP address it needs to connect to the phone system. Which of the following tasks need to be completed to allow the phone to operate correctly?",
        "options": [
            "Assign the phone's switchport to the correct VLAN.",
            "Statically assign the phone's gateway address.",
            "Configure a route on the VoIP network router.",
            "Implement a VoIP gateway."
        ],
        "correct_answer": 1,
        "description": "The correct answer is assign the phone's switchport to the correct VLAN. VoIP phones rely on proper VLAN configuration to get DHCP addresses and connect to the phone system. \n\n- Statically assigning the gateway address, configuring a route, or implementing a VoIP gateway are less likely to resolve the issue if the VLAN configuration is missing."
    },
    {
        "question": "Users are reporting intermittent WiFi connectivity in specific parts of a building. Which of the following should the network administrator check FIRST when troubleshooting this issue? (Choose two.)",
        "options": [
            "Site survey.",
            "EIRP.",
            "AP placement.",
            "Captive portal.",
            "SSID assignment.",
            "AP association time."
        ],
        "correct_answer": [1, 3],
        "description": "The correct answers are site survey and AP placement. A site survey will help identify coverage gaps, and proper AP placement ensures good signal strength in all areas of the building. \n\n- EIRP measures transmission power, but AP placement is often the more immediate solution. \n- Captive portals and SSID assignment are not primary causes of connectivity issues. \n- AP association time refers to the time it takes to connect, but AP placement is more crucial."
    },
    {
        "question": "A technician is setting up a new router, configuring ports, and allowing access to the Internet. However, none of the users connected to this new router are able to connect to the Internet. Which of the following does the technician need to configure?",
        "options": [
            "Tunneling.",
            "Multicast routing.",
            "Network address translation.",
            "Router advertisement."
        ],
        "correct_answer": 3,
        "description": "The correct answer is network address translation (NAT). NAT is required to allow users on the private network to connect to the internet via a public IP address. \n\n- Tunneling and multicast routing are not necessary for this basic connectivity. \n- Router advertisement is used for IPv6 and might not directly affect Internet connectivity."
    },
    {
        "question": "A network administrator is testing performance improvements by configuring channel bonding on an 802.11ac AP. Although a site survey detected the majority of the 5GHz frequency spectrum was idle, being used only by the company's WLAN and a nearby government radio system, the AP is not allowing the administrator to manually configure a large portion of the 5GHz frequency range. Which of the following would be BEST to configure for the WLAN being tested?",
        "options": [
            "Upgrade the equipment to an AP that supports manual configuration of the EIRP power settings.",
            "Switch to 802.11n, disable channel auto-selection, and enforce channel bonding on the configuration.",
            "Set up the AP to perform a dynamic selection of the frequency according to regulatory requirements.",
            "Deactivate the band 5GHz to avoid interference with the government radio."
        ],
        "correct_answer": 3,
        "description": "The correct answer is set up the AP to perform a dynamic selection of the frequency according to regulatory requirements. Regulatory constraints may prevent manual selection of certain frequencies, and dynamic frequency selection (DFS) allows the AP to automatically select the best available channel. \n\n- Upgrading equipment or switching to 802.11n might not address regulatory constraints. \n- Deactivating the 5GHz band would reduce bandwidth availability and is not a recommended solution."
    },
    {
        "question": "Which of the following options represents the participating computers in a network?",
        "options": [
            "Nodes.",
            "CPUs.",
            "Servers.",
            "Clients."
        ],
        "correct_answer": 1,
        "description": "The correct answer is nodes. In networking, nodes refer to devices that participate in the network, such as computers, routers, and switches. \n\n- CPUs refer to the central processing units of computers, not the entire networked device. \n- Servers and clients are specific types of nodes, but 'nodes' is the more general term."
    },
    {
        "question": "An administrator is working with the local ISP to troubleshoot an issue. Which of the following should the ISP use to define the furthest point on the network that the administrator is responsible for troubleshooting?",
        "options": [
            "Firewall.",
            "A CSU/DSU.",
            "Demarcation point.",
            "Router.",
            "Patch panel."
        ],
        "correct_answer": 3,
        "description": "The correct answer is demarcation point. The demarcation point is where responsibility for the network shifts from the ISP to the customer. \n\n- The firewall, CSU/DSU, router, and patch panel are devices that can be involved in troubleshooting but are not used to define responsibility boundaries."
    },
    {
        "question": "To access production applications and data, developers must first connect remotely to a different server. From there, the developers are able to access production data. Which of the following does this BEST represent?",
        "options": [
            "A management plane.",
            "A proxy server.",
            "An out-of-band management device.",
            "A site-to-site VPN.",
            "A jump box."
        ],
        "correct_answer": 5,
        "description": "The correct answer is a jump box. A jump box is a server used to access other servers or networks remotely, typically as an extra security layer. \n\n- A management plane is responsible for managing network devices. \n- A proxy server acts as an intermediary for requests, not for remote access. \n- An out-of-band management device is used for managing devices separately from regular network traffic. \n- A site-to-site VPN is used for secure connections between two sites, not individual device access."
    },



    
    {
        "question": "Which of the following is conducted frequently to maintain an updated list of a system's weaknesses?",
        "options": [
            "Penetration test.",
            "Posture assessment.",
            "Risk assessment.",
            "Vulnerability scan."
        ],
        "correct_answer": 4,
        "description": "The correct answer is vulnerability scan. This tool is used frequently to scan systems for weaknesses and vulnerabilities that need to be addressed. \n\n- A penetration test is more intrusive and typically done less frequently, simulating a real-world attack. \n- A posture assessment evaluates overall security health but is broader in scope. \n- A risk assessment involves evaluating potential threats but not necessarily maintaining a list of weaknesses."
    },
    {
        "question": "A systems administrator wants to use the least amount of equipment to segment two departments that have cables terminating in the same room. Which of the following would allow this to occur?",
        "options": [
            "A load balancer.",
            "A proxy server.",
            "A Layer 3 switch.",
            "A hub.",
            "A Layer 7 firewall."
        ],
        "correct_answer": 3,
        "description": "The correct answer is a Layer 3 switch. A Layer 3 switch can be used to segment traffic between different departments using VLANs while minimizing the need for additional equipment. \n\n- A load balancer is used to distribute traffic evenly across servers, not for segmentation. \n- A proxy server handles requests on behalf of clients but doesn't segment traffic. \n- A hub is a simple device that doesn’t provide segmentation and broadcasts data to all ports. \n- A Layer 7 firewall works on application data, which is not ideal for simple segmentation."
    },
    {
        "question": "An administrator needs to connect two laptops directly to each other using 802.11ac but does not have an AP available. Which of the following describes this configuration?",
        "options": [
            "Basic service set.",
            "Extended service set.",
            "Independent basic service set.",
            "MU-MIMO."
        ],
        "correct_answer": 3,
        "description": "The correct answer is Independent Basic Service Set (IBSS). This configuration allows two devices to communicate directly with each other without the need for an access point. \n\n- Basic Service Set (BSS) requires an access point. \n- Extended Service Set (ESS) refers to a network with multiple access points. \n- MU-MIMO is a technology that allows multiple devices to communicate simultaneously, but it does not describe a direct connection between two laptops."
    },

    {
        "question": "A network administrator is installing a new server in the datacenter. The administrator is concerned the amount of traffic generated will exceed 1GB, and higher-throughput NICs are not available for installation. Which of the following is the BEST solution for this issue?",
        "options": [
            "Install an additional NIC and configure LACP.",
            "Remove some of the applications from the server.",
            "Configure the NIC to use full duplex.",
            "Configure port mirroring to send traffic to another server.",
            "Install an SSD to decrease data processing time."
        ],
        "correct_answer": 1,
        "description": "The correct answer is install an additional NIC and configure LACP (Link Aggregation Control Protocol). LACP allows you to combine multiple NICs into a single logical connection, which can increase throughput beyond 1GB. \n\n- Removing applications from the server is not a viable solution for increasing throughput. \n- Configuring the NIC to use full duplex will not increase the total throughput beyond the NIC's physical limits. \n- Port mirroring is used for traffic monitoring, not improving throughput. \n- Installing an SSD will help with data processing speeds but will not address the throughput issue."
    },
    {
        "question": "A malicious user is using special software to perform an on-path attack. Which of the following best practices should be configured to mitigate this threat?",
        "options": [
            "Dynamic ARP inspection.",
            "Role-based access.",
            "Control plane policing.",
            "MAC filtering."
        ],
        "correct_answer": 1,
        "description": "The correct answer is Dynamic ARP inspection. This helps prevent man-in-the-middle attacks by ensuring that only valid ARP requests are processed, mitigating on-path (man-in-the-middle) attacks. \n\n- Role-based access controls are important for limiting permissions but do not specifically protect against on-path attacks. \n- Control plane policing helps manage network traffic but is not directly related to ARP spoofing. \n- MAC filtering is a security measure for restricting device access based on MAC addresses, but it is not as effective against on-path attacks as ARP inspection."
    },
    {
        "question": "Which of the following can be used to store various types of devices and provide contactless delivery to users?",
        "options": [
            "Asset tags.",
            "Biometrics.",
            "Access control vestibules.",
            "Smart lockers."
        ],
        "correct_answer": 4,
        "description": "The correct answer is smart lockers. Smart lockers provide a secure way to store devices and allow users to retrieve them via contactless methods, such as using an access code or RFID. \n\n- Asset tags are used for inventory tracking but don't provide contactless delivery. \n- Biometrics are used for identification and access but are not used for storage or delivery. \n- Access control vestibules manage building entry and security but are not designed for device storage or delivery."
    },
    {
        "question": "A technician recently set up a small office network for nine users. When the installation was complete, all the computers on the network showed addresses ranging from 169.254.0.0 to 169.254.255.255. Which of the following types of address ranges does this represent?",
        "options": [
            "Private.",
            "Public.",
            "APIPA.",
            "Classless."
        ],
        "correct_answer": 3,
        "description": "The correct answer is APIPA (Automatic Private IP Addressing). This range (169.254.0.0 - 169.254.255.255) is automatically assigned by the operating system when a device cannot obtain an IP address from a DHCP server. \n\n- Private IP addresses are from ranges defined by RFC 1918 and are not in the APIPA range. \n- Public IP addresses are globally routable, but the addresses in question are not. \n- Classless refers to IP address allocation methods that do not use fixed subnets, which is unrelated to APIPA."
    },
    {
        "question": "Which of the following OSI model layers is where a technician would view UDP information?",
        "options": [
            "Physical.",
            "Data link.",
            "Network.",
            "Transport."
        ],
        "correct_answer": 4,
        "description": "The correct answer is Transport. UDP (User Datagram Protocol) operates at the Transport layer of the OSI model. This is where connectionless communication protocols are managed. \n\n- The Physical layer deals with the transmission of raw data over physical media. \n- The Data link layer is responsible for node-to-node data transfer, not higher-level protocols like UDP. \n- The Network layer handles routing and addressing, but not UDP traffic."
    },
    {
        "question": "A network technician at a university is assisting with the planning of a simultaneous software deployment to multiple computers in one classroom in a building. Which of the following would be BEST to use?",
        "options": [
            "Multicast.",
            "Anycast.",
            "Unicast.",
            "Broadcast."
        ],
        "correct_answer": 1,
        "description": "The correct answer is multicast. Multicast allows the technician to send data to a specific group of recipients (multiple computers in the classroom) without flooding the entire network. \n\n- Anycast is used to route traffic to the nearest available server, not for simultaneous deployment. \n- Unicast is a one-to-one communication method, which would not be efficient for multiple machines. \n- Broadcast sends data to all devices on the network, which is not ideal for targeted deployment."
    },
    {
    "question": "A network administrator is reviewing the following metrics from a network management system regarding a switchport. The administrator suspects an issue because users are calling in regards to the switch port's performance:\n\nMetric                               Value\n-----------------------------------------------\nUptime                              201 days, 3 hours, 18 minutes\nMDIX                               On\nCRCs                                0\nGiants                             2508\nOutput queue maximum          40\nPackets input                     136208849\nPackets output                    64458087024\n\nBased on the information in the chart above, which of the following is the cause of these performance issues?",
    "options": [
        "The connected device is exceeding the configured MTU.",
        "The connected device is sending too many packets.",
        "The switchport has been up for too long.",
        "The connected device is receiving too many packets.",
        "The switchport does not have enough CRCs."
    ],
    "correct_answer": 1,
    "description": "The correct answer is the connected device is exceeding the configured MTU. The large number of 'Giants' (oversized packets) suggests that the connected device is sending packets larger than the allowed MTU, causing performance issues.\n\n- While the uptime being long can contribute to performance degradation, it is not the root cause.\n- CRCs are zero, indicating no errors on the network, ruling out physical issues.\n- The device receiving too many packets is unlikely to cause 'Giants' or performance issues.\n- CRCs are not the issue here since there are no errors."
    },




    
    {
        "question": "Which of the following describes the BEST device to configure as a DHCP relay?",
        "options": [
            "Bridge",
            "Router",
            "Layer 2 switch",
            "Hub"
        ],
        "correct_answer": 2,
        "description": "The correct answer is a router. A DHCP relay forwards DHCP messages between clients and servers across different networks. \n\n- A bridge simply connects two networks at Layer 2, but doesn't relay DHCP messages. \n- A Layer 2 switch operates at the Data Link Layer and typically does not handle DHCP relay functions. \n- A hub is a basic network device that doesn't have the capability to relay DHCP messages."
    },
    {
        "question": "Which of the following compromises Internet-connected devices and makes them vulnerable to becoming part of a botnet? (Choose two.)",
        "options": [
            "Deauthentication attack",
            "Malware infection",
            "IP spoofing",
            "Firmware corruption",
            "Use of default credentials",
            "Dictionary attack"
        ],
        "correct_answer": [2, 5],
        "description": "The correct answers are Malware infection and Use of default credentials. Both issues leave devices vulnerable to botnet compromise. \n\n- A deauthentication attack can disrupt communication but does not directly compromise the device. \n- IP spoofing is a method used in attacks but doesn't inherently make devices part of a botnet. \n- Firmware corruption may cause issues, but it doesn't directly contribute to botnet vulnerabilities. \n- Default credentials are often exploited in botnet attacks as attackers easily gain control of devices with unchanged factory settings."
    },
    {
        "question": "A network administrator is planning a WLAN for a soccer stadium and was advised to use MU-MIMO to improve connection performance in high-density areas. The project requires compatibility with clients connecting using 2.4GHz or 5GHz frequencies. Which of the following would be the BEST wireless standard for this project?",
        "options": [
            "802.11ac",
            "802.11ax",
            "802.11g",
            "802.11n"
        ],
        "correct_answer": 2,
        "description": "The correct answer is 802.11ax. This standard supports MU-MIMO and is designed for high-density environments, providing improved performance. \n\n- 802.11ac also supports MU-MIMO, but 802.11ax provides better overall performance in crowded environments, supporting both 2.4GHz and 5GHz bands. \n- 802.11g is an older standard with slower speeds and does not support MU-MIMO. \n- 802.11n is better than 802.11g but is still less efficient than 802.11ac or 802.11ax in terms of performance in high-density areas."
    },
    {
        "question": "An organization purchased an allocation of public IPv4 addresses. Instead of receiving the network address and subnet mask, the purchase paperwork indicates the allocation is a /28. This type of notation is referred to as:",
        "options": [
            "CIDR",
            "classful",
            "classless",
            "RFC1918"
        ],
        "correct_answer": 1,
        "description": "The correct answer is CIDR (Classless Inter-Domain Routing). CIDR notation, such as /28, represents the number of bits in the network portion of the address. \n\n- Classful addressing is the older method of addressing (Class A, B, C), which is now largely obsolete. \n- Classless addressing, while used in CIDR, is not the specific notation being described. \n- RFC1918 refers to private IP address ranges and is unrelated to the /28 CIDR notation."
    },
    {
        "question": "A network technician is reviewing a document that specifies how to handle access to company resources, such as the Internet and printers, when devices are not part of the company's assets. Which of the following agreements would a user be required to accept before using the company's resources?",
        "options": [
            "BYOD",
            "DLP",
            "AUP",
            "MOU"
        ],
        "correct_answer": 3,
        "description": "The correct answer is AUP (Acceptable Use Policy). An AUP outlines the rules for using company resources. \n\n- BYOD (Bring Your Own Device) allows personal devices on the company network but doesn't specify acceptable usage. \n- DLP (Data Loss Prevention) is a strategy for preventing sensitive data loss, not related to access rules. \n- MOU (Memorandum of Understanding) is a formal agreement but not specific to network access or usage policies."
    },
    {
        "question": "Which of the following records can be used to track the number of changes on a DNS zone?",
        "options": [
            "SOA",
            "SRV",
            "TXT",
            "NS"
        ],
        "correct_answer": 1,
        "description": "The correct answer is SOA (Start of Authority). The SOA record contains information about the DNS zone, including the serial number that changes with every update. \n\n- SRV records are used to define specific services, not for tracking zone changes. \n- TXT records are for arbitrary text, not zone changes. \n- NS records define name servers but do not track changes."
    },
    {
        "question": "A network administrator is trying to add network redundancy for the server farm. Which of the following can the network administrator configure to BEST provide this capability?",
        "options": [
            "VRRP",
            "DNS",
            "UPS",
            "RPO"
        ],
        "correct_answer": 1,
        "description": "The correct answer is VRRP (Virtual Router Redundancy Protocol). VRRP provides network redundancy by allowing multiple routers to act as a virtual router. \n\n- DNS (Domain Name System) resolves domain names but doesn't provide redundancy. \n- UPS (Uninterruptible Power Supply) provides power redundancy but not network redundancy. \n- RPO (Recovery Point Objective) is a disaster recovery term and not a direct method for network redundancy."
    },
    {
        "question": "A network administrator is adding a new switch to the network. Which of the following network hardening techniques would be BEST to use once the switch is in production?",
        "options": [
            "Disable unneeded ports",
            "Disable SSH service",
            "Disable MAC filtering",
            "Disable port security"
        ],
        "correct_answer": 1,
        "description": "The correct answer is to disable unneeded ports. This minimizes the attack surface and reduces the potential for unauthorized access. \n\n- Disabling SSH service would limit remote access to the switch, but it could hinder legitimate management tasks. \n- Disabling MAC filtering would weaken security by allowing any device to connect. \n- Disabling port security could leave the switch vulnerable to unauthorized devices connecting."
    },
    {
        "question": "A network administrator is troubleshooting an issue with a new Internet connection. The ISP is asking detailed questions about the configuration of the router that the network administrator is troubleshooting. Which of the following commands is the network administrator using? (Choose two.)",
        "options": [
            "tcpdump",
            "show config",
            "hostname",
            "show route",
            "netstat",
            "show ip arp"
        ],
        "correct_answer": [2, 4],
        "description": "The correct answers are 'show config' and 'show route'. These commands provide detailed information about the router's configuration and routing information. \n\n- tcpdump is used to capture network traffic and is not suitable for viewing configuration details. \n- hostname displays the router's name, but it's not useful for troubleshooting configuration issues. \n- netstat shows active connections but not the router's configuration. \n- show ip arp provides ARP table information but does not give details about the router's full configuration."
    },
    {
        "question": "Which of the following is the MOST appropriate use case for the deployment of a clientless VPN?",
        "options": [
            "Secure web access to internal corporate resources.",
            "Upgrade security via the use of an NFV technology.",
            "Connect two datacenters across the Internet.",
            "Increase VPN availability by using a SDWAN technology."
        ],
        "correct_answer": 1,
        "description": "The correct answer is to secure web access to internal corporate resources. A clientless VPN allows secure access via a web browser without needing specialized client software. \n\n- NFV (Network Functions Virtualization) is not directly related to clientless VPNs. \n- Connecting datacenters across the Internet typically requires a different type of VPN, not clientless. \n- SD-WAN improves availability but is not specifically related to clientless VPN use."
    },







        {
            "question": "Which of the following security controls indicates unauthorized hardware modifications?",
            "options": [
                "Biometric authentication",
                "Media device sanitization",
                "Change management policy",
                "Tamper-evident seals"
            ],
            "correct_answer": 4,
            "description": "The correct answer is Tamper-evident seals. These seals provide a clear visual indication when hardware has been accessed or tampered with. \n\n- Biometric authentication is a security control for user authentication, not hardware modifications. \n- Media device sanitization is used for ensuring data on devices is securely erased, not for detecting physical tampering. \n- Change management policy governs procedural changes, not hardware security."
        },
        {
            "question": "A network technician needs to install security updates on several switches on the company's network. The management team wants this completed as quickly and efficiently as possible. Which of the following should the technician do to perform the updates?",
            "options": [
                "Upload the security update onto each switch using a terminal emulator and a console cable.",
                "Configure a TFTP server, SSH into each device, and perform the update.",
                "Replace each old switch with new switches that have the updates already performed.",
                "Connect a USB memory stick to each switch and perform the update."
            ],
            "correct_answer": 2,
            "description": "The correct answer is to configure a TFTP server, SSH into each device, and perform the update. This allows centralized management of updates across multiple devices. \n\n- Uploading the update via a console cable is manual and time-consuming for multiple switches. \n- Replacing old switches is a more costly and disruptive approach. \n- Using a USB stick requires physical interaction with each switch, which is also inefficient for multiple devices."
        },
        {
            "question": "Which of the following describes traffic going in and out of a data center from the internet?",
            "options": [
                "Demarcation point",
                "North-South",
                "Fibre Channel",
                "Spine and leaf"
            ],
            "correct_answer": 2,
            "description": "The correct answer is North-South. This refers to the flow of data between the data center and external networks, such as the internet. \n\n- Demarcation point is the point where the service provider's responsibility ends and the customer's network begins, but it doesn't describe the traffic flow. \n- Fibre Channel is used for high-speed storage networks, not for internet traffic. \n- Spine and leaf refers to a type of network architecture used within data centers for internal traffic, not external."
        },
        {
            "question": "A technician is troubleshooting a connectivity issue with an end user. The end user can access local network shares and intranet pages but is unable to access the internet or remote resources. Which of the following needs to be reconfigured?",
            "options": [
                "The IP address",
                "The subnet mask",
                "The gateway address",
                "The DNS servers"
            ],
            "correct_answer": 3,
            "description": "The correct answer is the gateway address. The gateway address is required to route traffic between the local network and external resources, such as the internet. \n\n- The IP address is likely correct, as the user can access local resources. \n- The subnet mask is also likely correct since local communication works. \n- DNS servers help resolve domain names but are not responsible for routing traffic outside the local network."
        },
        {
            "question": "An IT administrator received an assignment with the following objectives:\n✑ Conduct a total scan within the company's network for all connected hosts.\n✑ Detect all the types of operating systems running on all devices.\n✑ Discover all services offered by hosts on the network.\n✑ Find open ports and detect security risks.\nWhich of the following command-line tools can be used to achieve these objectives?",
            "options": [
                "nmap",
                "arp",
                "netstat",
                "tcpdump"
            ],
            "correct_answer": 1,
            "description": "The correct answer is nmap. Nmap is a powerful network scanning tool that can discover devices, identify operating systems, and detect open ports and services. \n\n- arp is used for mapping IP addresses to MAC addresses, but it doesn't perform network-wide scans. \n- netstat provides information about current network connections but doesn't perform scans. \n- tcpdump is used to capture and analyze network traffic but does not scan for open ports or services."
        },
        {
            "question": "A network manager is configuring switches in IDFs to ensure unauthorized client computers are not connecting to a secure wired network. Which of the following is the network manager MOST likely performing?",
            "options": [
                "Disabling unneeded switchports",
                "Changing the default VLAN",
                "Configuring DHCP snooping",
                "Writing ACLs to prevent access to the switch"
            ],
            "correct_answer": 1,
            "description": "The correct answer is disabling unneeded switchports. Disabling unused ports helps prevent unauthorized devices from connecting to the network. \n\n- Changing the default VLAN is more about network organization than security. \n- Configuring DHCP snooping is a security feature for preventing rogue DHCP servers, not unauthorized client connections. \n- ACLs can prevent network access but don't address physical switchport security directly."
        },
        {
            "question": "At which of the following OSI model layers does routing occur?",
            "options": [
                "Data link",
                "Transport",
                "Physical",
                "Network"
            ],
            "correct_answer": 4,
            "description": "The correct answer is Network. Routing occurs at the Network layer (Layer 3) of the OSI model, where packets are forwarded based on IP addresses. \n\n- Data link layer (Layer 2) deals with MAC addresses and frames, not routing. \n- Transport layer (Layer 4) deals with end-to-end communication and flow control. \n- Physical layer (Layer 1) is concerned with transmitting raw bits over the physical medium."
        },
        {
            "question": "An auditor assessing network best practices was able to connect a rogue switch into a network jack and get network connectivity. Which of the following controls would BEST address this risk?",
            "options": [
                "Activate port security on the switchports providing end user access.",
                "Deactivate Spanning Tree Protocol on network interfaces that are facing public areas.",
                "Disable Neighbor Resolution Protocol in the Layer 2 devices.",
                "Ensure port tagging is in place for network interfaces in guest areas."
            ],
            "correct_answer": 1,
            "description": "The correct answer is to activate port security on the switchports providing end user access. Port security helps prevent unauthorized devices from connecting to the network by limiting the number of MAC addresses per port. \n\n- Deactivating Spanning Tree Protocol could lead to network loops and instability, and doesn't prevent unauthorized devices. \n- Disabling Neighbor Resolution Protocol is not related to physical security concerns. \n- Port tagging is more related to VLAN management than physical device security."
        },
        {
            "question": "A technician knows the MAC address of a device and is attempting to find the device's IP address. Which of the following should the technician look at to find the IP address? (Choose two.)",
            "options": [
                "ARP table",
                "DHCP leases",
                "IP route table",
                "DNS cache",
                "MAC address table",
                "STP topology"
            ],
            "correct_answer": [1, 2],
            "description": "The correct answers are ARP table and DHCP leases. The ARP table maps IP addresses to MAC addresses, and DHCP leases contain the IP addresses assigned to devices. \n\n- The IP route table is used for routing information and doesn't map MAC addresses to IP addresses. \n- DNS cache stores domain name resolutions, not IP addresses for MAC addresses. \n- The MAC address table is for network switches to map MAC addresses to switch ports, not IP addresses. \n- STP topology is for managing network loops and does not relate to IP-MAC address resolution."
        },
        {
            "question": "A user in a branch office reports that access to all files has been lost after receiving a new PC. All other users in the branch can access fileshares. The IT engineer who is troubleshooting this incident is able to ping the workstation from the branch router, but the machine cannot, ping the router. Which of the following is MOST likely the cause of the incident?",
            "options": [
                "Incorrect subnet mask",
                "Incorrect DNS server",
                "Incorrect IP class",
                "Incorrect TCP port"
            ],
            "correct_answer": 1,
            "description": "The correct answer is Incorrect subnet mask. The subnet mask defines the network portion of the IP address, and if it's incorrect, the computer may not be able to communicate with devices outside its subnet, such as the router. \n\n- The DNS server setting is unrelated to IP address routing and would not affect the ability to ping the router. \n- The IP class relates to the overall network structure but does not typically cause local connectivity issues. \n- TCP ports are used for specific services, not for basic network connectivity issues like this one."
        },




    
    {
        "question": "A network administrator would like to purchase a device that provides access ports to endpoints and has the ability to route between networks. Which of the following would be BEST for the administrator to purchase?",
        "options": [
            "An IPS",
            "A Layer 3 switch",
            "A router",
            "A wireless LAN controller"
        ],
        "correct_answer": 2,
        "description": "The correct answer is a Layer 3 switch. A Layer 3 switch combines the functionality of a traditional switch and a router, allowing it to route traffic between different networks while providing access ports for endpoints. \n\n- An IPS (Intrusion Prevention System) is used for security, not routing. \n- A router can also route traffic, but it typically does not provide direct access ports like a switch. \n- A wireless LAN controller is used for managing wireless access points, not for routing between networks."
    },
    {
        "question": "A false camera is installed outside a building to assist with physical security. Which of the following is the device assisting?",
        "options": [
            "Detection",
            "Recovery",
            "Identification",
            "Prevention"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Detection. A false camera, although not actively monitoring, can deter potential intruders by creating the appearance of surveillance. Its primary role is to aid in detecting unauthorized activity by intimidating potential threats. \n\n- Recovery refers to systems that help recover from incidents, not prevent or detect them. \n- Identification is about recognizing individuals or objects, which is not the role of a false camera. \n- Prevention refers to devices or systems that directly stop security threats, not just detect them."
    },
    {
        "question": "Which of the following types of attacks can be used to gain credentials by setting up rogue APs with identical corporate SSIDs?",
        "options": [
            "VLAN hopping",
            "Evil twin",
            "DNS poisoning",
            "Social engineering"
        ],
        "correct_answer": 2,
        "description": "The correct answer is Evil twin. An evil twin attack involves setting up rogue access points (APs) with the same SSID as a legitimate corporate network, tricking users into connecting to them and revealing credentials. \n\n- VLAN hopping is an attack on VLAN configurations, not related to rogue APs. \n- DNS poisoning targets domain name systems, not wireless networks. \n- Social engineering involves manipulating people to disclose information, which is different from exploiting network vulnerabilities."
    },
    {
        "question": "Which of the following protocols is widely used in large-scale enterprise networks to support complex networks with multiple routers and balance traffic load on multiple links?",
        "options": [
            "OSPF",
            "RIPv2",
            "QoS",
            "STP"
        ],
        "correct_answer": 1,
        "description": "The correct answer is OSPF. Open Shortest Path First (OSPF) is a widely used routing protocol in large-scale networks due to its scalability and ability to balance traffic across multiple links. \n\n- RIPv2 is an older protocol, less efficient for large networks. \n- QoS (Quality of Service) is used to manage bandwidth, not to balance traffic load across links. \n- STP (Spanning Tree Protocol) prevents loops in Ethernet networks but does not balance traffic."
    },
    {
        "question": "A network engineer is investigating reports of poor network performance. Upon reviewing a report, the engineer finds hundreds of CRC errors on an interface. Which of the following is the MOST likely cause of these errors?",
        "options": [
            "A bad wire on the Cat 5e cable",
            "The wrong VLAN assignment to the switchport",
            "A misconfigured QoS setting on the router",
            "Both sides of the switch trunk set to full duplex"
        ],
        "correct_answer": 1,
        "description": "The correct answer is a bad wire on the Cat 5e cable. CRC (Cyclic Redundancy Check) errors often occur when there are physical layer issues, such as a damaged or improperly connected cable, causing data corruption. \n\n- The wrong VLAN assignment would typically cause a network segmentation issue, not CRC errors. \n- Misconfigured QoS settings affect traffic prioritization, not the physical layer errors like CRC. \n- Full duplex misconfiguration on both sides of the switch trunk can cause issues but is less likely to result in CRC errors."
    },
    {
        "question": "Which of the following is considered a physical security detection device?",
        "options": [
            "Cameras",
            "Biometric readers",
            "Access control vestibules",
            "Locking racks"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Cameras. Cameras are used to detect and monitor physical activity, making them a key part of physical security detection systems. \n\n- Biometric readers authenticate individuals but do not detect security breaches. \n- Access control vestibules control physical access, but they do not detect security events. \n- Locking racks secure hardware but are not used for detection."
    },
    {
        "question": "A network is experiencing extreme latency when accessing a particular website. Which of the following commands will BEST help identify the issue?",
        "options": [
            "ipconfig",
            "netstat",
            "tracert",
            "ping"
        ],
        "correct_answer": 3,
        "description": "The correct answer is tracert. Tracert (Traceroute) traces the path packets take to reach a destination and helps identify where latency is occurring along the route. \n\n- ipconfig displays IP configuration details, not network path information. \n- netstat shows active connections but does not trace packet paths. \n- ping checks basic connectivity, but tracert provides more detailed insight into latency along the network route."
    },
    {
        "question": "A technician needs to configure a routing protocol for an internet-facing edge router. Which of the following routing protocols will the technician MOST likely use?",
        "options": [
            "BGP",
            "RIPv2",
            "OSPF",
            "EIGRP"
        ],
        "correct_answer": 1,
        "description": "The correct answer is BGP. Border Gateway Protocol (BGP) is commonly used for routing between different autonomous systems on the internet, making it ideal for an edge router facing the internet. \n\n- RIPv2 is an older, less scalable protocol typically used for smaller networks. \n- OSPF is a link-state protocol used within an organization's network but not ideal for routing between different organizations. \n- EIGRP is a Cisco-specific protocol often used within private networks but less commonly used for internet-facing routers."
    },
    {
        "question": "A technician is monitoring a network interface and notices the device is dropping packets. The cable and interfaces, however, are in working order. Which of the following is MOST likely the cause?",
        "options": [
            "OID duplication",
            "MIB mismatch",
            "CPU usage",
            "Encapsulation errors"
        ],
        "correct_answer": 3,
        "description": "The correct answer is encapsulation errors. Encapsulation errors occur when packets are improperly encapsulated and dropped during transmission, even if the physical layer (cable and interface) is working. \n\n- OID (Object Identifier) duplication and MIB (Management Information Base) mismatch are SNMP-related issues, not directly related to dropped packets. \n- High CPU usage could affect performance but is not the most likely cause of dropped packets in this scenario."
    },
    {
        "question": "A technician installed an 8-port switch in a user's office. The user needs to add a second computer in the office, so the technician connects both PCs to the switch and connects the switch to the wall jack. However, the new PC cannot connect to network resources. The technician then observes the following: \n✑ The new computer does not get an IP address on the client's VLAN. \n✑ Both computers have a link light on their NICs. \n✑ The new PC appears to be operating normally except for the network issue. \n✑ The existing computer operates normally. \nWhich of the following should the technician do NEXT to address the situation?",
        "options": [
            "Contact the network team to resolve the port security issue.",
            "Contact the server team to have a record created in DNS for the new PC.",
            "Contact the security team to review the logs on the company's SIEM.",
            "Contact the application team to check NetFlow data from the connected switch."
        ],
        "correct_answer": 1,
        "description": "The correct answer is to contact the network team to resolve the port security issue. Port security on the switch may have been configured to allow only specific devices to connect, preventing the new PC from obtaining an IP address. \n\n- DNS issues would cause name resolution problems, not an IP address assignment issue. \n- SIEM logs and NetFlow data are unrelated to the current issue, which seems to be more of a network configuration issue."
    },
    













]

