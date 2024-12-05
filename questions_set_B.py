questions_set_B = [

#201-250

    
    {
        "question": "A network administrator needs to provide remote clients with access to an internal web application. Which of the following methods provides the HIGHEST flexibility and compatibility while encrypting only the connection to the web application?",
        "options": [
            "Clientless VPN",
            "Virtual desktop",
            "Virtual network computing",
            "mGRE tunnel"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Clientless VPN. This method allows users to access internal web applications directly from a browser without installing additional software, providing high flexibility and compatibility while encrypting only the web application's connection. \n\n- Virtual desktop offers broader access but requires additional setup and is less focused on single applications. \n- Virtual network computing provides remote desktop functionality but does not encrypt connections by default. \n- mGRE tunnel is designed for site-to-site connections, not for individual user application access."
    },
    {
        "question": "A network engineer receives the following when connecting to a switch to configure a port: telnet 10.1.200.1\nConnecting to 10.1.200.1..Could not open connection to the host, on port 23: Connect failed.\nWhich of the following is the MOST likely cause for the failure?",
        "options": [
            "The network engineer is using the wrong protocol.",
            "The network engineer does not have permission to configure the device.",
            "SNMP has been secured with an ACL.",
            "The switchport the engineer is trying to configure is down."
        ],
        "correct_answer": 1,
        "description": "The correct answer is that the network engineer is using the wrong protocol. Telnet uses port 23, which may be disabled on modern systems in favor of more secure protocols like SSH. \n\n- Permissions issues would not typically result in a port error. \n- SNMP with ACLs does not impact Telnet connectivity. \n- A down switchport would affect connected devices but not Telnet's ability to connect to the host itself."
    },
    {
        "question": "A network attack caused a network outage by wiping the configuration and logs of the border firewall. Which of the following sources, in an investigation to determine how the firewall was compromised, can provide the MOST detailed data?",
        "options": [
            "Syslog server messages",
            "MIB of the attacked firewall",
            "Network baseline reports",
            "NetFlow aggregate data"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Syslog server messages. Syslog servers collect detailed log data from devices, including configuration changes and security events, making them the best source for forensic analysis. \n\n- The MIB contains management data but lacks event logs. \n- Network baseline reports help compare normal and abnormal traffic but do not provide detailed logs. \n- NetFlow data aggregates traffic flow but does not contain configuration or log details."
    },
    {
        "question": "A network engineer needs to reduce the overhead of file transfers. Which of the following configuration changes would accomplish that goal?",
        "options": [
            "Link aggregation",
            "Jumbo frames",
            "Port security",
            "Flow control",
            "Lower FTP port"
        ],
        "correct_answer": 2,
        "description": "The correct answer is Jumbo frames. Jumbo frames increase the maximum transmission unit (MTU), reducing overhead by allowing more data to be sent per packet, which improves efficiency in file transfers. \n\n- Link aggregation increases bandwidth but does not directly reduce overhead. \n- Port security relates to access control, not file transfer efficiency. \n- Flow control manages traffic but does not reduce packet overhead. \n- Lowering the FTP port is unrelated to overhead reduction."
    },
    {
        "question": "Which of the following devices have the capability to allow communication between two different subnetworks? (Choose two.)",
        "options": [
            "IDS",
            "Access point",
            "Layer 2 switch",
            "Layer 3 switch",
            "Router",
            "Media converter"
        ],
        "correct_answer": [4, 5],
        "description": "The correct answers are Layer 3 switch and Router. Both devices operate at Layer 3 of the OSI model, enabling communication between different subnetworks by routing packets based on IP addresses. \n\n- IDS is a monitoring tool, not a routing device. \n- Access points provide wireless connectivity but do not route traffic between subnetworks. \n- Layer 2 switches operate at the Data Link Layer and cannot route packets between subnetworks. \n- Media converters change the transmission medium but do not facilitate inter-subnet communication."
    },
    {
        "question": "A network technician is implementing a solution that will allow end users to gain access to multiple applications after logging on. Which of the following authentication methods would allow this type of access?",
        "options": [
            "SSO",
            "LDAP",
            "EAP",
            "TACACS+"
        ],
        "correct_answer": 1,
        "description": "The correct answer is SSO (Single Sign-On). SSO allows users to authenticate once and gain access to multiple applications or systems without needing to log in again, enhancing user experience and productivity. \n\n- LDAP is a protocol for accessing directory services, not for unified authentication. \n- EAP is primarily used for wireless authentication. \n- TACACS+ is focused on centralized device management, not end-user application access."
    },
    {
        "question": "An administrator is attempting to add a new system to monitoring but is unsuccessful. The administrator notices the system is similar to another one on the network; however, the new one has an updated OS version. Which of the following should the administrator consider updating?",
        "options": [
            "Management information bases",
            "System baseline",
            "Network device logs",
            "SNMP traps"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Management Information Bases (MIBs). Updated MIBs provide compatibility with the new system's OS version, ensuring proper communication with monitoring tools. \n\n- Updating the system baseline involves performance standards, not monitoring compatibility. \n- Network device logs contain historical data but do not impact monitoring capabilities. \n- SNMP traps send alerts but are not related to MIB updates."
    },
    {
    "question": "A network technician receives a report about a performance issue on a client PC that is connected to port 1/3 on a network switch. The technician observes the following configuration output from the switch:\n\n1/1 Client PC Connected Full 1000\n1/2 Client PC Connected Full 1000\n1/3 Client PC Connected Full 10\n\nWhich of the following is a cause of the issue on port 1/3?",
    "options": [
        "Speed",
        "Duplex",
        "Errors",
        "VLAN"
    ],
    "correct_answer": 1,
    "description": "The correct answer is Speed. The speed setting for port 1/3 is only 10 Mbps, while other ports are set to 1000 Mbps. This mismatch can cause significant performance degradation for devices connected to port 1/3. \n\n- Duplex is correctly set to Full, so it is not the cause of the issue. \n- Errors indicate potential transmission issues but are not directly linked to the observed configuration. \n- VLAN configuration is unrelated to port speed."
},

{
    "question": "Which of the following would be used when connecting devices that have different physical characteristics?",
    "options": [
        "A proxy server",
        "An industrial control system",
        "A load balancer",
        "A media converter"
    ],
    "correct_answer": 4,
    "description": "The correct answer is Media Converter. Media converters are used to connect devices with different physical media, such as converting fiber optics to copper. \n\n- Proxy servers are used for managing network traffic, not physical connections. \n- Industrial control systems are used for automation, not connecting devices with different media. \n- Load balancers distribute network traffic but do not resolve physical connection differences."
},

{
    "question": "A Fortune 500 firm is deciding on the kind of data center equipment to install given its five-year budget outlook. The Chief Information Officer is comparing equipment based on the life expectancy of different models. Which of the following concepts BEST represents this metric?",
    "options": [
        "MTBF",
        "MTTR",
        "RPO",
        "RTO"
    ],
    "correct_answer": 1,
    "description": "The correct answer is MTBF (Mean Time Between Failures). MTBF indicates the average operating time between failures, making it a key metric for determining equipment reliability over a long-term budget outlook. \n\n- MTTR (Mean Time to Repair) measures how quickly a device can be repaired but does not indicate overall reliability. \n- RPO (Recovery Point Objective) is related to data recovery, not equipment reliability. \n- RTO (Recovery Time Objective) deals with the time it takes to restore operations after a failure."
},












    {
        "question": "A network administrator installed an additional IDF during a building expansion project. Which of the following documents need to be updated to reflect the change? (Choose two.)",
        "options": [
            "Data loss prevention policy",
            "BYOD policy",
            "Acceptable use policy",
            "Non-disclosure agreement",
            "Disaster recovery plan",
            "Physical network diagram"
        ],
        "correct_answer": [5, 6],
        "description": "The correct answers are Disaster Recovery Plan and Physical Network Diagram. Adding an IDF affects the physical infrastructure and disaster recovery strategies. \n\n- Data loss prevention policy and BYOD policy are unrelated to physical network changes. \n- Acceptable use policies and non-disclosure agreements are administrative documents, not technical updates."
    },
    {
        "question": "Which of the following BEST describes hosting several businesses on the same physical infrastructure?",
        "options": [
            "Hybrid",
            "Elasticity",
            "IaaS",
            "Multitenancy"
        ],
        "correct_answer": 4,
        "description": "The correct answer is Multitenancy. Multitenancy allows multiple tenants (businesses) to share the same physical infrastructure while isolating their resources logically. \n\n- Hybrid refers to mixed deployment models, not shared hosting. \n- Elasticity involves scaling resources, unrelated to shared infrastructure. \n- IaaS is a type of cloud service but does not specifically describe shared infrastructure for multiple businesses."
    },
    {
        "question": "A company streams video to multiple devices across a campus. When this happens, several users report a degradation of network performance. Which of the following would MOST likely address this issue?",
        "options": [
            "Enable IGMP snooping on the switches.",
            "Implement another DHCP server.",
            "Reconfigure port tagging for the video traffic.",
            "Change the SSID of the APs."
        ],
        "correct_answer": 1,
        "description": "The correct answer is Enable IGMP snooping on the switches. IGMP snooping helps manage multicast traffic more efficiently, improving network performance in video streaming scenarios. \n\n- Another DHCP server would not address network performance issues. \n- Reconfiguring port tagging is related to VLAN management, not directly solving performance degradation. \n- Changing the SSID would affect wireless network naming, not video traffic handling."
    },
    {
        "question": "The power company notifies a network administrator that it will be turning off the power to the building over the weekend. Which of the following is the BEST solution to prevent the servers from going down?",
        "options": [
            "Redundant power supplies",
            "Uninterruptible power supply",
            "Generator",
            "Power distribution unit"
        ],
        "correct_answer": 3,
        "description": "The correct answer is Generator. A generator can provide long-term power backup in the event of an outage, ensuring that the servers remain operational over the weekend. \n\n- Redundant power supplies are good for preventing failure within the system but won't solve a complete power outage. \n- An uninterruptible power supply (UPS) provides short-term backup power but is not designed to last for an extended period. \n- A power distribution unit (PDU) helps manage power distribution but does not supply backup power."
    },
    {
        "question": "A technician is trying to determine whether an LACP bundle is fully operational. Which of the following commands will the technician MOST likely use?",
        "options": [
            "show interface",
            "show config",
            "show route",
            "show arp"
        ],
        "correct_answer": 1,
        "description": "The correct answer is show interface. This command shows the status of network interfaces, including LACP (Link Aggregation Control Protocol) status. \n\n- show config shows the current device configuration, not the operational status of interfaces. \n- show route displays the routing table, not LACP information. \n- show arp shows the address resolution protocol table, unrelated to LACP."
    },
    {
        "question": "A network administrator wants to check all network connections and see the output in integer form. Which of the following commands should the administrator run on the command line?",
        "options": [
            "netstat",
            "netstat -a",
            "netstat -e",
            "netstat -n"
        ],
        "correct_answer": 4,
        "description": "The correct answer is netstat -n. The -n flag ensures that network addresses and port numbers are shown in numeric (integer) form, without DNS resolution. \n\n- netstat shows network statistics but may include hostnames, not necessarily integers. \n- netstat -a shows all connections but does not focus on numeric output. \n- netstat -e provides Ethernet statistics, unrelated to listing connections."
    },
    {
        "question": "Which of the following connectors and terminations are required to make a Cat 6 cable that connects from a PC to a non-capable MDIX switch? (Choose two.)",
        "options": [
            "TIA-568-A - TIA-568-B",
            "TIA-568-B - TIA-568-B",
            "RJ11",
            "RJ45",
            "F-type"
        ],
        "correct_answer": [2, 4],
        "description": "The correct answers are TIA-568-B - TIA-568-B and RJ45. For a Cat 6 cable, TIA-568-B wiring standard and RJ45 connectors are used to ensure proper connectivity. \n\n- TIA-568-A - TIA-568-B is a mix of wiring standards but not the correct pair for Cat 6 cabling. \n- RJ11 is used for telephone connections, not networking. \n- F-type is used for coaxial cable, not Ethernet cables."
    },
    {
        "question": "A technician is configuring a wireless network and needs to ensure users agree to an AUP before connecting. Which of the following should be implemented to achieve this goal?",
        "options": [
            "Captive portal",
            "Geofencing",
            "Wireless client isolation",
            "Role-based access"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Captive portal. A captive portal is a web page that users see before accessing the network, where they can agree to the AUP (Acceptable Use Policy). \n\n- Geofencing is used for location-based access restrictions, not for AUP agreements. \n- Wireless client isolation is a security feature, not for policy agreement. \n- Role-based access defines user roles but does not enforce policy agreement."
    },
    {
        "question": "A network technician needs to determine the IPv6 address of a malicious website. Which of the following record types would provide this information?",
        "options": [
            "A",
            "AAAA",
            "CNAME",
            "PTR"
        ],
        "correct_answer": 2,
        "description": "The correct answer is AAAA. The AAAA record in DNS provides the IPv6 address of a domain or website. \n\n- A record provides the IPv4 address, not IPv6. \n- CNAME is a canonical name record, used for aliases, not directly for IP addresses. \n- PTR is used for reverse DNS lookup, not for finding the address of a domain."
    },
    {
        "question": "A technician is troubleshooting a report about network connectivity issues on a workstation. Upon investigation, the technician notes the workstation is showing an APIPA address on the network interface. The technician verifies that the VLAN assignment is correct and that the network interface has connectivity. Which of the following is MOST likely the issue the workstation is experiencing?",
        "options": [
            "DHCP exhaustion",
            "A rogue DHCP server",
            "A DNS server outage",
            "An incorrect subnet mask"
        ],
        "correct_answer": 1,
        "description": "The correct answer is DHCP exhaustion. An APIPA address is typically assigned when the DHCP server cannot provide an IP address, likely due to exhaustion of available addresses. \n\n- A rogue DHCP server could cause IP assignment issues, but exhaustion is a more likely cause. \n- A DNS server outage would not cause an APIPA address to be assigned. \n- An incorrect subnet mask would cause network segmentation issues but not specifically trigger APIPA address assignment."
    },










    {
        "question": "A network technician has determined the cause of a network disruption. Which of the following is the NEXT step for the technician to perform?",
        "options": [
            "Validate the findings in a top-to-bottom approach.",
            "Duplicate the issue, if possible.",
            "Establish a plan of action to resolve the issue.",
            "Document the findings and actions."
        ],
        "correct_answer": 3,
        "description": "The correct answer is to document the findings and actions. This ensures that all steps are properly recorded for future reference and troubleshooting. \n\n- Validating the findings top-to-bottom can come after documenting, but it's not the immediate next step. \n- Duplicating the issue might be needed later, but it’s not necessary if the cause is already identified. \n- Establishing a plan of action is important, but documentation should be prioritized first."
    },
    {
        "question": "Which of the following types of connections would need to be set up to provide access from the internal network to an external network so multiple satellite offices can communicate securely using various ports and protocols?",
        "options": [
            "Client-to-site VPN",
            "Clientless VPN",
            "RDP",
            "Site-to-site VPN",
            "SSH"
        ],
        "correct_answer": 4,
        "description": "The correct answer is site-to-site VPN. This type of VPN connects two networks (internal and external) securely, enabling communication between multiple satellite offices. \n\n- Client-to-site VPN is for remote users connecting to the internal network, not for inter-office communication. \n- Clientless VPN requires no software but doesn’t provide the same network-wide access as a site-to-site VPN. \n- RDP is a protocol for remote desktop access, not a network connection method. \n- SSH is typically used for secure remote command-line access, not for network connectivity."
    },
    {
        "question": "A corporate client is experiencing global system outages. The IT team has identified multiple potential underlying causes throughout the enterprise. Each team member has been assigned an area to troubleshoot. Which of the following approaches is being used?",
        "options": [
            "Divide-and-conquer",
            "Top-to-bottom",
            "Bottom-to-top",
            "Determine if anything changed"
        ],
        "correct_answer": 1,
        "description": "The correct answer is divide-and-conquer. This approach involves breaking down a complex problem into smaller parts and addressing them separately, which is ideal for large-scale system outages. \n\n- Top-to-bottom and bottom-to-top approaches are methods for troubleshooting, but they focus on a single starting point, not distributed tasks. \n- 'Determine if anything changed' is part of the troubleshooting process but not the strategy being used in this scenario."
    },
    {
        "question": "Which of the following use cases would justify the deployment of an mGRE hub-and-spoke topology?",
        "options": [
            "An increase in network security using encryption and packet encapsulation",
            "A network expansion caused by an increase in the number of branch locations to the headquarters",
            "A mandatory requirement to increase the deployment of an SDWAN network",
            "An improvement in network efficiency by increasing the useful packet payload"
        ],
        "correct_answer": 2,
        "description": "The correct answer is a network expansion caused by an increase in the number of branch locations to the headquarters. mGRE hub-and-spoke topologies are ideal for connecting multiple remote sites (branches) to a central location (headquarters). \n\n- mGRE does improve network efficiency, but its main purpose is to support scalable network expansions. \n- It does not directly focus on encryption or packet encapsulation as its primary use. \n- SDWAN deployment might require different topologies."
    },
    {
        "question": "Which of the following needs to be tested to achieve a Cat 6a certification for a company's data cabling?",
        "options": [
            "RJ11",
            "LC ports",
            "Patch panel",
            "F-type connector"
        ],
        "correct_answer": 3,
        "description": "The correct answer is patch panel. Cat 6a certification requires testing for performance across all components of the cabling infrastructure, including patch panels, to ensure the full system meets performance standards. \n\n- RJ11 is used for telephony connections and is unrelated to Cat 6a certification. \n- LC ports are fiber-optic components, not part of the copper cable certification. \n- F-type connectors are used for coaxial cables, not for Cat 6a cabling."
    },
    {
        "question": "A network technician is responding to an issue with a local company. To which of the following documents should the network technician refer to determine the scope of the issue?",
        "options": [
            "MTTR",
            "MOU",
            "NDA",
            "SLA"
        ],
        "correct_answer": 4,
        "description": "The correct answer is SLA (Service Level Agreement). The SLA defines the scope of services, including response times and issue resolution, which will guide the technician in understanding the scope of the issue. \n\n- MTTR (Mean Time to Repair) measures the time taken to repair an issue but does not define the scope. \n- MOU (Memorandum of Understanding) outlines general agreements but not specific operational issues. \n- NDA (Non-Disclosure Agreement) is related to confidentiality, not the scope of technical issues."
    },
    {
        "question": "A company wants to set up a backup data center that can become active during a disaster. The site needs to contain network equipment and connectivity. Which of the following strategies should the company employ?",
        "options": [
            "Active-active",
            "Warm",
            "Cold",
            "Cloud"
        ],
        "correct_answer": 2,
        "description": "The correct answer is warm. A warm site provides the necessary infrastructure, but it may not have the latest data or be immediately operational. It strikes a balance between cost and recovery speed. \n\n- Active-active sites are fully functional at all times, but they are more expensive. \n- Cold sites lack infrastructure, requiring a longer recovery time. \n- Cloud-based backup centers are viable but depend on external providers."
    },
    {
        "question": "Which of the following would be used to forward requests and replies between a DHCP server and client?",
        "options": [
            "Relay",
            "Lease",
            "Scope",
            "Range"
        ],
        "correct_answer": 1,
        "description": "The correct answer is relay. A DHCP relay agent forwards DHCP requests and replies between clients and servers across different networks. \n\n- Lease refers to the time period a DHCP client is assigned an IP address, not forwarding requests. \n- Scope refers to the range of IP addresses a DHCP server can assign. \n- Range is part of the scope, not specifically used to forward requests."
    },
    {
        "question": "Network connectivity in an extensive forest reserve was achieved using fiber optics. A network fault was detected, and now the repair team needs to check the integrity of the fiber cable. Which of the following actions can reduce repair time?",
        "options": [
            "Using a tone generator and wire map to determine the fault location",
            "Using a multimeter to locate the fault point",
            "Using an OTDR in one end of the optic cable to get the fiber length information",
            "Using a spectrum analyzer and comparing the current wavelength with a working baseline"
        ],
        "correct_answer": 3,
        "description": "The correct answer is using an OTDR (Optical Time Domain Reflectometer). An OTDR allows for precise location of faults by measuring the time it takes for light to return, helping to reduce repair time. \n\n- Tone generators and wire maps are useful for copper cables, not fiber optics. \n- Multimeters cannot accurately locate fiber optic cable faults. \n- Spectrum analyzers are used for signal analysis, not fault detection."
    },
    {
        "question": "A small office has a wireless network with several access points that are used by mobile devices. Users occasionally report that the wireless connection drops or becomes very slow. Reports confirm that this only happens when the devices are connected to the office wireless network. Which of the following is MOST likely the cause?",
        "options": [
            "The configuration of the encryption protocol",
            "Interference from other devices",
            "Insufficient bandwidth capacity",
            "Duplicate SSIDs"
        ],
        "correct_answer": 2,
        "description": "The correct answer is interference from other devices. Wireless networks can experience slowdowns or drops in connection if there is interference from other wireless signals, such as from microwaves or neighboring networks. \n\n- Encryption protocol configuration issues might affect security but would not typically cause performance issues. \n- Insufficient bandwidth could be an issue, but interference is more likely. \n- Duplicate SSIDs might cause network confusion but would not cause frequent slowdowns or drops in connection."
    },

  {
        "question": "Which of the following is a benefit of the spine-and-leaf network topology?",
        "options": [
            "Increased network security.",
            "Stable network latency.",
            "Simplified network management.",
            "Eliminated need for inter-VLAN routing."
        ],
        "correct_answer": 2,
        "description": "The correct answer is simplified network management. The spine-and-leaf topology is designed for ease of management by providing a predictable, flat architecture where each device connects to both spine switches, ensuring efficient routing. \n\n- Increased network security is not a direct benefit of the spine-and-leaf topology; security is generally managed through additional network configurations. \n- Stable network latency is not inherent to the topology itself, as it depends on network traffic and infrastructure. \n- Inter-VLAN routing is still required in spine-and-leaf topologies, as VLANs need to be routed between switches."
    },
    {
        "question": "A technician performed a manual reconfiguration of a firewall, and network connectivity was reestablished. Some connection events that were previously sent to a syslog server are no longer being generated by the firewall. Which of the following should the technician perform to fix the issue?",
        "options": [
            "Adjust the proper logging level on the new firewall.",
            "Tune the filter for logging the severity level on the syslog server.",
            "Activate NetFlow traffic between the syslog server and the firewall.",
            "Restart the SNMP service running on the syslog server."
        ],
        "correct_answer": 1,
        "description": "The correct answer is adjust the proper logging level on the new firewall. After the firewall reconfiguration, it’s likely that the logging level settings were changed, preventing logs from being sent to the syslog server. \n\n- Tuning the filter on the syslog server may adjust which events are recorded, but it will not fix the issue if the firewall is not generating the logs. \n- NetFlow traffic is typically used for flow data monitoring, not for logging specific events like syslog. \n- Restarting the SNMP service will not resolve issues related to logging configuration."
    },
    {
    "question": "A company rents out a large event space and includes wireless internet access for each tenant. Tenants reserve a two-hour window from the company each week, which includes a tenant-specific SSID. However, all users share the company's network hardware. The network support team is receiving complaints from tenants that some users are unable to connect to the wireless network. Upon investigation, the support team discovers a pattern indicating that after a tenant with a particularly large attendance ends its sessions, tenants throughout the day are unable to connect. The following settings are common to all network configurations:\n\nWireless encryption: WPA2\nCaptive portal: Disabled\nAP isolation: Enabled\nSubnet mask: 255.255.255.0\nDNS server: 10.0.0.1\nDefault gateway: 10.1.10.1\nDHCP scope begin: 10.1.10.10\nDHCP scope end: 10.1.10.150\nDHCP lease time: 24 hours",
    "options": [
        "Change to WPA encryption.",
        "Change the DNS server to 10.1.10.1.",
        "Change the default gateway to 10.0.0.1.",
        "Change the DHCP scope end to 10.1.10.250.",
        "Disable AP isolation.",
        "Change the subnet mask to 255.255.255.192.",
        "Reduce the DHCP lease time to four hours."
    ],
    "correct_answer": [4, 6],
    "description": "The correct answers are 'Change the DHCP scope end to 10.1.10.250' and 'Reduce the DHCP lease time to four hours'. \n\n- Changing the DHCP scope end to 10.1.10.250 will allow more IP addresses for new tenants as the current range (10.1.10.10 - 10.1.10.150) may run out, causing connection issues. \n\n- Reducing the DHCP lease time to four hours ensures that IP addresses are reassigned more frequently, making it easier for tenants to get an IP when a previous session ends. \n\n- WPA encryption and DNS settings are not directly related to the issue of tenants being unable to connect after high-traffic sessions. \n\n- Disabling AP isolation would allow tenants to communicate with each other, but it doesn't address the root cause of connection issues caused by exhausted IP addresses or long DHCP lease times."
  },


    {
        "question": "A user from a remote office is reporting slow file transfers. Which of the following tools will an engineer MOST likely use to get detailed measurement data?",
        "options": [
            "Packet capture",
            "iPerf",
            "NetFlow analyzer",
            "Internet speed test"
        ],
        "correct_answer": 2,
        "description": "The correct answer is iPerf. iPerf is a network testing tool that measures the bandwidth between two hosts, providing detailed performance data. \n\n- Packet capture is useful for analyzing the contents of network traffic, but it won't give direct performance metrics like throughput. \n- A NetFlow analyzer monitors traffic patterns, but it doesn't provide detailed performance measurements specific to a single transfer. \n- An Internet speed test provides a basic measure of bandwidth but is not suitable for detailed network performance analysis."
    },
    {
        "question": "When accessing corporate network resources, users are required to authenticate to each application they try to access. Which of the following concepts does this BEST represent?",
        "options": [
            "SSO",
            "Zero Trust",
            "VPN",
            "Role-based access control"
        ],
        "correct_answer": 1,
        "description": "The correct answer is SSO (Single Sign-On). SSO allows users to authenticate once and gain access to multiple resources without needing to log in repeatedly. \n\n- Zero Trust focuses on security principles, ensuring trust is never assumed, regardless of network location. \n- VPN (Virtual Private Network) secures network traffic but does not directly relate to authentication across applications. \n- Role-based access control defines what resources a user can access based on their role, but it doesn't require authentication for each application."
    },
    {
        "question": "Logs show an unauthorized IP address entering a secure part of the network every night at 8:00 p.m. The network administrator is concerned that this IP address will cause an issue to a critical server and would like to deny the IP address at the edge of the network. Which of the following solutions would address these concerns?",
        "options": [
            "Changing the VLAN of the web server",
            "Changing the server's IP address",
            "Implementing an ACL",
            "Installing a rule on the firewall connected to the web server"
        ],
        "correct_answer": 3,
        "description": "The correct answer is implementing an ACL (Access Control List). An ACL can be configured on the edge of the network to deny traffic from the unauthorized IP address. \n\n- Changing the VLAN or the server's IP address may be possible solutions, but they are more complex and may not fully address the root of the issue. \n- Installing a firewall rule directly on the web server could help, but managing access control at the network edge using an ACL is more efficient and scalable."
    },
    {
        "question": "A network administrator is troubleshooting a connectivity performance issue. As part of the troubleshooting process, the administrator performs a traceroute from the client to the server, and also from the server to the client. While comparing the outputs, the administrator notes they show different hops between the hosts. Which of the following BEST explains these findings?",
        "options": [
            "Asymmetric routing",
            "A routing loop",
            "A switch loop",
            "An incorrect gateway"
        ],
        "correct_answer": 1,
        "description": "The correct answer is asymmetric routing. Asymmetric routing occurs when packets take different paths in each direction between two hosts, which is common in some network configurations. \n\n- A routing loop happens when packets continuously circulate in a loop without reaching their destination, which would cause the traceroute to show repeated hops. \n- A switch loop is related to issues within Layer 2 devices and wouldn't cause different traceroute outputs. \n- An incorrect gateway would typically result in a complete failure to reach the destination, not different routing paths."
    },
    {
        "question": "A technician is troubleshooting reports that a networked printer is unavailable. The printer's IP address is configured with a DHCP reservation, but the address cannot be pinged from the print server in the same subnet. Which of the following is MOST likely the cause of the connectivity failure?",
        "options": [
            "Incorrect VLAN",
            "DNS failure",
            "DHCP scope exhaustion",
            "Incorrect gateway"
        ],
        "correct_answer": 1,
        "description": "The correct answer is incorrect VLAN. If the printer is configured for a specific VLAN that is different from the print server's VLAN, communication will fail even if they are on the same subnet. \n\n- DNS failure would affect name resolution but not direct IP address pinging. \n- DHCP scope exhaustion would prevent the printer from receiving an IP address, but the printer already has a reservation, so this is unlikely. \n- Incorrect gateway settings would cause issues with external communication but not with local communication within the same subnet."
    },
    {
        "question": "A systems operator is granted access to a monitoring application, configuration application, and timekeeping application. The operator is denied access to the financial and project management applications by the system's security configuration. Which of the following BEST describes the security principle in use?",
        "options": [
            "Network access control",
            "Least privilege",
            "Multifactor authentication",
            "Separation of duties"
        ],
        "correct_answer": 2,
        "description": "The correct answer is least privilege. The principle of least privilege ensures users only have access to the resources they need to perform their duties, minimizing exposure to sensitive data. \n\n- Network access control defines rules for allowing or blocking network traffic but doesn't specifically control user access to individual applications. \n- Multifactor authentication is a security measure for verifying a user's identity, but it does not relate to access control to specific applications. \n- Separation of duties divides responsibilities to prevent fraud or error, but it is not about restricting access to applications."
    },
    {
        "question": "A technician is connecting a Cat 6 Ethernet cable to a device that only has LC ports. Which of the following will the technician MOST likely use to accomplish this task?",
        "options": [
            "A bridge",
            "A media converter",
            "A repeater",
            "A router"
        ],
        "correct_answer": 2,
        "description": "The correct answer is a media converter. A media converter is used to convert between different types of media or interfaces, such as from Ethernet (Cat 6) to fiber (LC ports). \n\n- A bridge connects two networks at the data link layer but does not convert between cable types. \n- A repeater boosts the signal but does not change the type of connection or cable used. \n- A router directs traffic between networks, but it does not convert the physical layer of a connection."
    },


    {
        "question": "After a critical power issue, the network team was not receiving UPS status notifications. The network team would like to be alerted on these status changes. Which of the following would be BEST to use for these notifications?",
        "options": [
            "Traps",
            "MIB",
            "NetFlow",
            "Syslog"
        ],
        "correct_answer": 1,
        "description": "The correct answer is traps. Traps are used to send alerts from devices like UPS systems to the monitoring system when there is an event, such as a power issue. \n\n- MIB (Management Information Base) is a database used for storing management information but does not send alerts. \n- NetFlow is used for monitoring network traffic, not for device alerts. \n- Syslog is typically used for logging system messages and events but is not as immediate for sending notifications like traps."
    },
    {
        "question": "Users in a branch can access an in-house database server, but it is taking too long to fetch records. The analyst does not know whether the issue is being caused by network latency. Which of the following will the analyst MOST likely use to retrieve the metrics that are needed to resolve this issue?",
        "options": [
            "SNMP",
            "Link state",
            "Syslog",
            "QoS",
            "Traffic shaping"
        ],
        "correct_answer": 1,
        "description": "The correct answer is SNMP. SNMP (Simple Network Management Protocol) allows the analyst to monitor network devices and retrieve performance metrics, helping to diagnose network latency issues. \n\n- Link state is related to the state of network routing and is not used for measuring latency. \n- Syslog logs system messages but doesn't provide detailed network metrics. \n- QoS and traffic shaping are used for managing network traffic, not specifically for measuring latency."
    },
    {
        "question": "At which of the following OSI model layers does an IMAP client run?",
        "options": [
            "Layer 2",
            "Layer 4",
            "Layer 6",
            "Layer 7"
        ],
        "correct_answer": 4,
        "description": "The correct answer is Layer 7. IMAP (Internet Message Access Protocol) operates at Layer 7, the Application Layer, as it is a protocol used for retrieving emails from a server. \n\n- Layer 2 deals with data link protocols, which are not related to IMAP. \n- Layer 4 deals with transport protocols like TCP, which IMAP relies on but does not directly operate at. \n- Layer 6 refers to the Presentation Layer, which is also unrelated to IMAP."
    },
    {
        "question": "Which of the following would be the MOST cost-effective recovery solution for a company's lower-priority applications?",
        "options": [
            "Warm site",
            "Cloud site",
            "Hot site",
            "Cold site"
        ],
        "correct_answer": 4,
        "description": "The correct answer is cold site. A cold site is the most cost-effective option as it provides a basic infrastructure without the immediate replication of critical data, making it suitable for lower-priority applications. \n\n- A warm site provides partially configured systems and data, but it's more expensive than a cold site. \n- A hot site offers a fully redundant and ready-to-go infrastructure, which is the most expensive option. \n- A cloud site can be more flexible but is generally not the cheapest for lower-priority applications."
    },
    {
        "question": "Which of the following network devices can perform routing between VLANs?",
        "options": [
            "Layer 2 switch",
            "Layer 3 switch",
            "Load balancer",
            "Bridge"
        ],
        "correct_answer": 2,
        "description": "The correct answer is Layer 3 switch. Layer 3 switches are capable of routing traffic between VLANs by performing IP routing functions. \n\n- A Layer 2 switch operates only at the data link layer and cannot route between VLANs. \n- Load balancers distribute network traffic but do not perform routing. \n- A bridge is used to connect network segments but does not perform routing between VLANs."
    },
    {
        "question": "A network administrator wants to test the throughput of a new metro Ethernet circuit to verify that its performance matches the requirements specified in the SLA. Which of the following would BEST help measure the throughput?",
        "options": [
            "iPerf",
            "Ping",
            "NetFlow",
            "Netstat"
        ],
        "correct_answer": 1,
        "description": "The correct answer is iPerf. iPerf is a tool designed specifically to measure network throughput by testing the bandwidth between two endpoints. \n\n- Ping is useful for testing network connectivity but does not measure throughput. \n- NetFlow is used for monitoring traffic patterns but does not directly test throughput. \n- Netstat shows network statistics but does not measure bandwidth."
    },
    {
        "question": "A Wi-Fi network was recently deployed in a new, multilevel building. Several issues are now being reported related to latency and drops in coverage. Which of the following is the FIRST step to troubleshoot the issues?",
        "options": [
            "Perform a site survey",
            "Review the AP placement",
            "Monitor channel utilization",
            "Test cable attenuation"
        ],
        "correct_answer": 1,
        "description": "The correct answer is to perform a site survey. A site survey helps identify the optimal placement of wireless access points (APs) and can reveal any coverage or interference issues in the building. \n\n- Reviewing AP placement is important but can be informed by the results of the site survey. \n- Monitoring channel utilization helps identify interference, but the site survey is the first step. \n- Testing cable attenuation is irrelevant to Wi-Fi coverage issues, as it pertains to wired connections."
    },
    {
        "question": "Which of the following is the primary function of the core layer of the three-tiered model?",
        "options": [
            "Routing",
            "Repeating",
            "Bridging",
            "Switching"
        ],
        "correct_answer": 1,
        "description": "The correct answer is routing. The core layer in a three-tiered network model is primarily responsible for routing traffic between different network segments. \n\n- Repeating and bridging are functions of other layers, not the core layer. \n- Switching is typically performed in the distribution layer or access layer, not the core layer."
    },
    {
        "question": "An IT officer is installing a new WAP. Which of the following must the officer change to connect users securely to the WAP?",
        "options": [
            "AES encryption",
            "Channel to the highest frequency within the band",
            "TKIP encryption protocol",
            "Dynamic selection of the frequency"
        ],
        "correct_answer": 1,
        "description": "The correct answer is AES encryption. AES (Advanced Encryption Standard) is a secure encryption protocol used to protect Wi-Fi networks and should be enabled to ensure secure user connections to the WAP. \n\n- The highest frequency within the band can help with performance but does not ensure security. \n- TKIP is an older and less secure encryption protocol compared to AES. \n- Dynamic selection of frequency helps with interference but does not address security."
    },
    {
        "question": "To comply with an industry regulation, all communication destined to a secure server should be logged and archived on a storage device. Which of the following can be configured to fulfill this requirement?",
        "options": [
            "QoS traffic classification",
            "Port mirroring",
            "Flow control",
            "Link Aggregation Control Protocol"
        ],
        "correct_answer": 2,
        "description": "The correct answer is port mirroring. Port mirroring allows for the copying of traffic on a network port to another device for monitoring and logging, making it suitable for archiving communications to a secure server. \n\n- QoS traffic classification prioritizes traffic but does not log it. \n- Flow control manages traffic flow but does not provide logging or archiving. \n- Link Aggregation Control Protocol (LACP) combines multiple network connections, which does not involve logging or archiving traffic."
    }















]
