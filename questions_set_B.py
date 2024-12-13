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
    "question": "A company rents out a large event space and includes wireless internet access for each tenant. Tenants reserve a two-hour window from the company each week, which includes a tenant-specific SSID. However, all users share the company's network hardware. The network support team is receiving complaints from tenants that some users are unable to connect to the wireless network. Upon investigation, the support team discovers a pattern indicating that after a tenant with a particularly large attendance ends its sessions, tenants throughout the day are unable to connect. The following settings are common to all network configurations:(Choose two.) \n\nWireless encryption: WPA2\nCaptive portal: Disabled\nAP isolation: Enabled\nSubnet mask: 255.255.255.0\nDNS server: 10.0.0.1\nDefault gateway: 10.1.10.1\nDHCP scope begin: 10.1.10.10\nDHCP scope end: 10.1.10.150\nDHCP lease time: 24 hours",
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
    },



    


    {
        "question": "Which of the following routing protocols is generally used by major ISPs for handling large-scale internet traffic?",
        "options": [
            "RIP",
            "EIGRP",
            "OSPF",
            "BGP"
        ],
        "correct_answer": 4,
        "description": "The correct answer is BGP (Border Gateway Protocol). It is specifically designed for large-scale networks like the internet, used by ISPs to exchange routing information across autonomous systems. \n\n- RIP is outdated and only suitable for small networks. \n- EIGRP is a Cisco proprietary protocol used within internal networks, not across ISPs. \n- OSPF is suitable for enterprise networks but not designed for global ISP-level routing."
    },
    {
        "question": "A technician is consolidating a topology with multiple SSIDs into one unique SSID deployment. Which of the following features will be possible after this new configuration?",
        "options": [
            "Seamless roaming",
            "Basic service set",
            "WPA",
            "MU-MIMO"
        ],
        "correct_answer": 1,
        "description": "The correct answer is seamless roaming. With a single SSID, devices can switch between access points without dropping the connection, improving user experience. \n\n- Basic service set refers to a single AP and is not directly related to seamless roaming. \n- WPA is a security protocol and does not impact SSID configuration. \n- MU-MIMO improves wireless performance but is unrelated to SSIDs."
    },
    {
        "question": "Which of the following is used to provide disaster recovery capabilities to spin up all critical devices using internet resources?",
        "options": [
            "Cloud site",
            "Hot site",
            "Cold site",
            "Warm site"
        ],
        "correct_answer": 1,
        "description": "The correct answer is cloud site. Cloud sites allow businesses to quickly deploy critical services over the internet, ensuring business continuity during disasters. \n\n- Hot sites are physical locations that mirror the primary site but are less flexible than cloud solutions. \n- Cold sites require setup before operation, delaying recovery. \n- Warm sites offer partial infrastructure but still require additional setup."
    },
    {
        "question": "Which of the following attack vectors represents a large number of devices sending access requests to a website, making it unavailable to respond?",
        "options": [
            "Virus",
            "Botnet",
            "ARP spoofing",
            "DDoS"
        ],
        "correct_answer": 4,
        "description": "The correct answer is DDoS (Distributed Denial of Service). DDoS attacks flood a website with excessive requests, disrupting service. \n\n- A virus is malware designed to spread and cause damage but does not generate such network traffic. \n- A botnet is a collection of infected devices often used in DDoS attacks but is not the attack itself. \n- ARP spoofing is a man-in-the-middle attack targeting local network communications."
    },
    {
        "question": "Several end users viewing a training video report seeing pixelated images while watching. A network administrator reviews the core switch and is unable to find an immediate cause. Which of the following BEST explains what is occurring?",
        "options": [
            "Jitter",
            "Bandwidth",
            "Latency",
            "Giants"
        ],
        "correct_answer": 2,
        "description": "The correct answer is bandwidth. Insufficient bandwidth can result in poor video quality, causing pixelation. \n\n- Jitter refers to inconsistent packet arrival, which typically results in stuttering or delays. \n- Latency causes delays in data transfer but does not directly impact video resolution. \n- Giants are oversized packets and do not typically relate to video pixelation."
    },
    {
        "question": "An international company is transferring its IT assets, including a number of WAPs, from the United States to an office in Europe for deployment. Which of the following considerations should the company research before implementing the wireless hardware?",
        "options": [
            "WPA2 cipher",
            "Regulatory impacts",
            "CDMA configuration",
            "802.11 standards"
        ],
        "correct_answer": 2,
        "description": "The correct answer is regulatory impacts. Different regions have varying wireless frequency and power output regulations that must be adhered to. \n\n- WPA2 cipher is a security protocol and does not relate to regulatory compliance. \n- CDMA is a mobile communication standard irrelevant to WAPs. \n- 802.11 standards are consistent globally but do not address regional legal requirements."
    },
    {
        "question": "A company is moving to a new building designed with a guest waiting area that has existing network ports. Which of the following practices would BEST secure the network?",
        "options": [
            "Ensure all guests sign an NDA.",
            "Disable unneeded switchports in the area.",
            "Lower the radio strength to reduce Wi-Fi coverage in the waiting area.",
            "Enable MAC filtering to block unknown hardware addresses."
        ],
        "correct_answer": 2,
        "description": "The correct answer is to disable unneeded switchports in the area. This prevents unauthorized access via physical connections. \n\n- Signing an NDA is unrelated to technical security. \n- Lowering Wi-Fi strength may reduce coverage but does not secure wired ports. \n- MAC filtering is a secondary measure and is not as effective against physical threats."
    },
    {
        "question": "A network technician receives a support ticket about an employee who has misplaced a company-owned cell phone that contains private company information. Which of the following actions should the network technician take to prevent data loss?",
        "options": [
            "Disable the user account.",
            "Lock the phone.",
            "Turn off the service.",
            "Execute remote wipe."
        ],
        "correct_answer": 4,
        "description": "The correct answer is to execute a remote wipe. This ensures sensitive data on the phone is erased, preventing unauthorized access. \n\n- Disabling the user account only limits access to some services. \n- Locking the phone provides limited protection if the device is physically compromised. \n- Turning off service affects connectivity but does not protect stored data."
    },
    {
        "question": "A network technician is having issues connecting an IoT sensor to the internet. The WLAN settings were entered via a custom command line, and a proper IP address assignment was received on the wireless interface. However, when trying to connect to the internet, only HTTP redirections are being received when data is requested. Which of the following will point to the root cause of the issue?",
        "options": [
            "Verifying if an encryption protocol mismatch exists.",
            "Verifying if a captive portal is active for the WLAN.",
            "Verifying the minimum RSSI for operation in the device's documentation.",
            "Verifying EIRP power settings on the access point."
        ],
        "correct_answer": 2,
        "description": "The correct answer is verifying if a captive portal is active for the WLAN. Captive portals often redirect users to a login page before allowing internet access. \n\n- Encryption mismatches usually prevent connection, not redirections. \n- Minimum RSSI affects signal strength but not redirections. \n- EIRP power settings influence coverage but do not explain HTTP redirections."
    },
    {
        "question": "Which of the following topologies requires the MOST connections when designing a network?",
        "options": [
            "Mesh",
            "Star",
            "Bus",
            "Ring"
        ],
        "correct_answer": 1,
        "description": "The correct answer is mesh. A full mesh topology requires a direct connection between every pair of nodes, resulting in the highest number of connections. \n\n- Star has a central hub with fewer connections. \n- Bus connects all devices along a single line. \n- Ring uses a closed loop with fewer connections than mesh."
    },
    {
        "question": "A technician removes an old PC from the network and replaces it with a new PC that is unable to connect to the LAN. Which of the following is MOST likely the cause of the issue?",
        "options": [
            "Port security",
            "Port tagging",
            "Port aggregation",
            "Port mirroring"
        ],
        "correct_answer": 1,
        "description": "The correct answer is port security. Port security prevents unauthorized devices from connecting by allowing only specified MAC addresses. \n\n- Port tagging is used for VLAN assignments. \n- Port aggregation combines multiple ports for increased bandwidth. \n- Port mirroring is used for traffic monitoring, not access control."
    },






    {
        "question": "A medical building offers patients Wi-Fi in the waiting room. Which of the following security features would be the BEST solution to provide secure connections and keep the medical data protected?",
        "options": [
            "Isolating the guest network",
            "Securing SNMP",
            "MAC filtering",
            "Disabling unneeded switchports"
        ],
        "correct_answer": 1,
        "description": "The correct answer is isolating the guest network. This ensures that guest devices are separated from the internal network, safeguarding sensitive medical data and preventing unauthorized access. \n\n- Securing SNMP only protects management communication and does not isolate guest traffic. \n- MAC filtering is not scalable and offers limited security against determined attackers. \n- Disabling unneeded switchports secures unused physical ports but does not address Wi-Fi guest access."
    },
    {
        "question": "An administrator notices that after contact with several switches in an MDF they failed due to electrostatic discharge. Which of the following sensors should the administrator deploy to BEST monitor static electricity conditions in the MDF?",
        "options": [
            "Temperature",
            "Humidity",
            "Smoke",
            "Electrical"
        ],
        "correct_answer": 2,
        "description": "The correct answer is humidity. Low humidity increases the likelihood of electrostatic discharge, which can damage sensitive electronics. Monitoring humidity ensures it stays within a safe range to prevent ESD. \n\n- Temperature monitoring is important but unrelated to ESD. \n- Smoke sensors detect fire, not static conditions. \n- Electrical sensors measure power usage or surges, not ESD risks."
    },
    {
        "question": "A network administrator is reviewing the network device logs on a syslog server. The messages are normal, but the time stamps on the messages are incorrect. Which of the following actions should the administrator take to ensure the log message time stamps are correct?",
        "options": [
            "Change the NTP settings on the network device.",
            "Change the time on the syslog server.",
            "Update the network device firmware.",
            "Adjust the timeout settings on the syslog server.",
            "Adjust the SSH settings on the network device."
        ],
        "correct_answer": 1,
        "description": "The correct answer is changing the NTP settings on the network device. NTP (Network Time Protocol) ensures accurate time synchronization between devices, critical for proper logging. \n\n- Changing the time on the syslog server is a temporary fix and not scalable. \n- Updating firmware may improve functionality but will not resolve time sync issues. \n- Adjusting timeout or SSH settings is unrelated to timestamp accuracy."
    },
    {
        "question": "Two network technicians are installing a fiber-optic link between routers. The technicians used a light meter to verify the correct fibers. However, when they connect the fibers to the router interface, the link does not connect. Which of the following would explain the issue? (Choose two.)",
        "options": [
            "They used the wrong type of fiber transceiver.",
            "Incorrect TX/RX polarity exists on the link.",
            "The connection has duplexing configuration issues.",
            "Halogen light fixtures are causing interference.",
            "One of the technicians installed a loopback adapter.",
            "The RSSI was not strong enough on the link."
        ],
        "correct_answer": [1, 2],
        "description": "The correct answers are using the wrong type of fiber transceiver and incorrect TX/RX polarity. Mismatched transceivers can prevent data transmission, while incorrect polarity misaligns transmit and receive signals. \n\n- Duplexing issues would impact communication but not prevent a link. \n- Halogen fixtures do not interfere with fiber-optic links. \n- A loopback adapter would isolate the device, but this is unlikely. \n- RSSI (signal strength) does not apply to fiber links."
    },
    {
        "question": "Which of the following protocols would enable a company to upgrade its internet connection by acquiring its own public IP prefixes and autonomous system number?",
        "options": [
            "EIGRP",
            "BGP",
            "IPv6",
            "MPLS"
        ],
        "correct_answer": 2,
        "description": "The correct answer is BGP (Border Gateway Protocol). BGP allows organizations to manage their public IP prefixes and communicate with other networks using their autonomous system number. \n\n- EIGRP is a Cisco-proprietary internal routing protocol, not for external IP management. \n- IPv6 provides a larger address space but does not handle internet routing. \n- MPLS is a network transport technology, not a routing protocol."
    },
    {
        "question": "A network technician is performing tests on a potentially faulty network card that is installed in a server. Which of the following addresses will MOST likely be used during traffic diagnostic tests?",
        "options": [
            "10.10.10.10",
            "127.0.0.1",
            "192.168.0.1",
            "255.255.255.0"
        ],
        "correct_answer": 2,
        "description": "The correct answer is 127.0.0.1. This is the loopback address used to test the local network interface on the device itself. \n\n- 10.10.10.10 and 192.168.0.1 are private IPs used for network devices, not diagnostics. \n- 255.255.255.0 is a subnet mask, not an address."
    },
    {
        "question": "An administrator would like to create a fault-tolerant ring between three switches within a Layer 2 network. Which of the following Ethernet features should the administrator employ?",
        "options": [
            "Spanning Tree Protocol",
            "Open Shortest Path First",
            "Port mirroring",
            "An interior gateway protocol"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Spanning Tree Protocol (STP). STP prevents loops in Layer 2 networks by blocking redundant paths until needed for failover. \n\n- OSPF is used for Layer 3 routing, not Layer 2. \n- Port mirroring is for traffic analysis, not fault tolerance. \n- Interior gateway protocols focus on routing, not Layer 2 redundancy."
    },
    {
        "question": "During a risk assessment, which of the following should be considered when planning to mitigate high CPU utilization of a firewall?",
        "options": [
            "Recovery time objective",
            "Uninterruptible power supply",
            "NIC teaming",
            "Load balancing"
        ],
        "correct_answer": 4,
        "description": "The correct answer is load balancing. Distributing traffic across multiple firewalls reduces CPU load and improves performance. \n\n- Recovery time objective is for disaster recovery planning. \n- UPS ensures power availability but does not reduce CPU load. \n- NIC teaming improves network redundancy but not firewall processing capacity."
    },
    {
        "question": "A network engineer is monitoring a fiber uplink to a remote office and notes the uplink has been operating at 100% capacity for a long duration. Which of the following performance metrics is MOST likely to be impacted with sustained link saturation?",
        "options": [
            "Latency",
            "Jitter",
            "Speed",
            "Bandwidth"
        ],
        "correct_answer": 1,
        "description": "The correct answer is latency. Sustained saturation can delay packet processing, increasing latency. \n\n- Jitter affects consistency but is secondary to latency in saturation scenarios. \n- Speed is not affected directly as it is a fixed link capacity. \n- Bandwidth is the capacity being saturated, not a metric impacted by it."
    },



    {
        "question": "Which of the following would be used to adjust resources dynamically for a virtual web server under variable loads?",
        "options": [
            "Elastic computing.",
            "Scalable networking.",
            "Hybrid deployment.",
            "Multitenant hosting."
        ],
        "correct_answer": 1,
        "description": "The correct answer is Elastic computing. This allows for dynamic allocation of computing resources based on load requirements, ensuring optimal performance during variable demand. \n\n- Scalable networking focuses on expanding network capacity, which is not directly related to resource adjustment for web servers. \n- Hybrid deployment combines on-premises and cloud resources but does not inherently adjust resources dynamically. \n- Multitenant hosting refers to sharing a single server among multiple users, which does not offer dynamic scaling capabilities."
    },
    {
        "question": "A technician discovered that some information on the local database server was changed during a file transfer to a remote server. Which of the following should concern the technician the MOST?",
        "options": [
            "Confidentiality.",
            "Integrity.",
            "DDoS.",
            "On-path attack."
        ],
        "correct_answer": 2,
        "description": "The correct answer is Integrity. The modification of information during transfer indicates a potential compromise of data integrity, meaning the data is no longer accurate or trustworthy. \n\n- Confidentiality refers to the unauthorized access of data, which is not directly related to data modification. \n- DDoS attacks aim to overwhelm a server but do not change data during transfer. \n- An on-path attack involves intercepting communications but may not necessarily modify the data."
    },


{
    "question": "During a client audit, a network analyst is tasked with recommending changes to upgrade the client network and readiness. A field technician has submitted the following report:\n\nBuilding B is connected to Building A via site-to-site directional antennas.\n\nThirty additional users have been added recently and are not shown on the network map.\n\nThe IT closet and storage room share a space that has poor ventilation.\n\nPerformance reports show optimal network performance but little on system health.\n\nBased on this report, which of the following metrics or sensors would be the BEST recommendation to the client?",
    "options": [
        "Electrical.",
        "Humidity.",
        "Flooding.",
        "Temperature."
    ],
    "correct_answer": 4,
    "description": "The correct answer is Temperature. Poor ventilation in the IT closet and storage room can cause heat buildup, potentially damaging hardware or causing performance issues. Monitoring temperature is crucial to maintain system health and performance.\n\n- Electrical sensors monitor power levels, which are not directly related to ventilation issues. \n- Humidity sensors measure moisture levels, which are important for avoiding condensation but are not the main concern here. \n- Flooding sensors detect water presence, which does not address the primary issue of poor ventilation or heat management in this case."
},




    {
        "question": "After HVAC failures caused network outages, the support team decides to monitor the temperatures of all the devices. The network administrator cannot find a command that will display this information. Which of the following will retrieve the necessary information?",
        "options": [
            "SNMP OID values.",
            "NetFlow data export.",
            "Network baseline configurations.",
            "Security information and event management."
        ],
        "correct_answer": 1,
        "description": "The correct answer is SNMP OID values. SNMP (Simple Network Management Protocol) provides a method to query and retrieve information about network devices, including temperature readings, through OID (Object Identifier) values. \n\n- NetFlow data export is focused on analyzing traffic flow and bandwidth usage, not device monitoring. \n- Network baseline configurations are for performance comparisons, not real-time data retrieval. \n- Security information and event management (SIEM) tools focus on logging and analyzing security-related events, not environmental monitoring."
    },
    {
        "question": "Several employees have expressed concerns about the company monitoring their internet activity when they are working from home. The company wants to mitigate this issue and reassure employees that their private internet activity is not being monitored. Which of the following would satisfy company and employee needs?",
        "options": [
            "Split tunnel.",
            "Full tunnel.",
            "Site-to-site tunnel.",
            "Virtual desktop."
        ],
        "correct_answer": 1,
        "description": "The correct answer is Split tunnel. Split tunneling allows users to route work-related traffic through the company VPN while non-work traffic uses the local internet connection, ensuring privacy for personal activity. \n\n- Full tunnel routes all traffic through the VPN, potentially causing privacy concerns. \n- Site-to-site tunnel connects entire networks, not individual users, and does not address personal internet activity. \n- Virtual desktop isolates the work environment but does not prevent monitoring of personal internet traffic."
    },
    {
        "question": "A company needs a redundant link to provide a channel to the management network in an incident response scenario. Which of the following remote access methods provides the BEST solution?",
        "options": [
            "Out-of-band access.",
            "Split-tunnel connections.",
            "Virtual network computing.",
            "Remote desktop gateways."
        ],
        "correct_answer": 1,
        "description": "The correct answer is Out-of-band access. Out-of-band access provides a dedicated channel for network management, even during main network failures, ensuring redundancy in incident response scenarios. \n\n- Split-tunnel connections are not designed for redundant management. \n- Virtual network computing (VNC) provides remote access but relies on the network being functional. \n- Remote desktop gateways are dependent on the main network and do not offer independent access."
    },
    {
        "question": "An engineer is gathering data to determine the effectiveness of UPSs in use at remote retail locations. Which of the following statistics can the engineer use to determine the availability of the remote network equipment?",
        "options": [
            "Uptime.",
            "NetFlow baseline.",
            "SNMP traps.",
            "Interface statistics."
        ],
        "correct_answer": 1,
        "description": "The correct answer is Uptime. Uptime measures how long a device has been operational, making it a key metric for determining equipment availability at remote locations. \n\n- NetFlow baseline focuses on traffic analysis, not equipment availability. \n- SNMP traps provide alerts but do not offer a historical availability measure. \n- Interface statistics are specific to network interfaces, not overall device availability."
    },
    {
        "question": "Which of the following can be used to decrease latency during periods of high utilization of a firewall?",
        "options": [
            "Hot site.",
            "NIC teaming.",
            "HA pair.",
            "VRRP."
        ],
        "correct_answer": 3,
        "description": "The correct answer is HA pair. High Availability (HA) pairs allow load sharing and redundancy, which can reduce latency during high utilization by distributing traffic across multiple firewalls. \n\n- Hot site is a disaster recovery option, not relevant to reducing firewall latency. \n- NIC teaming improves network interface redundancy and performance but does not directly address firewall load. \n- VRRP (Virtual Router Redundancy Protocol) provides router failover, not firewall performance optimization."
    },
    {
        "question": "A network administrator needs to configure a server to use the most accurate NTP reference available. Which of the following NTP devices should the administrator select?",
        "options": [
            "Stratum 1.",
            "Stratum 2.",
            "Stratum 3.",
            "Stratum 4."
        ],
        "correct_answer": 1,
        "description": "The correct answer is Stratum 1. Stratum 1 NTP servers directly synchronize with a precise time source like an atomic clock, offering the highest accuracy. \n\n- Stratum 2 servers are slightly less accurate as they synchronize with Stratum 1 servers. \n- Stratum 3 and Stratum 4 servers are progressively less accurate, as they synchronize with higher-stratum servers."
    },
    {
        "question": "Which of the following devices is used to configure and centrally manage access points installed at different locations?",
        "options": [
            "Wireless controller.",
            "Load balancer.",
            "Proxy server.",
            "VPN concentrator."
        ],
        "correct_answer": 1,
        "description": "The correct answer is Wireless controller. Wireless controllers allow centralized management of multiple access points, simplifying configuration and monitoring across locations. \n\n- Load balancer is used to distribute traffic across servers, not access points. \n- Proxy server handles client requests for internet resources, not wireless management. \n- VPN concentrator is for managing secure remote connections, not access points."
    },



    {
        "question": "A user reports that a new VoIP phone works properly, but the computer that is connected to the phone cannot access any network resources. Which of the following MOST likely needs to be configured correctly to provide network connectivity to the computer?",
        "options": [
            "Port duplex settings",
            "Port aggregation",
            "ARP settings",
            "VLAN tags",
            "MDIX settings"
        ],
        "correct_answer": 4,
        "description": "The correct answer is VLAN tags. If the computer is connected to a VoIP phone, the network setup likely involves VLANs to separate voice and data traffic. The computer might not have the correct VLAN tag configured to access the data network. \n\n- Port duplex settings relate to the speed of communication but are not likely to cause issues with access to network resources. \n- Port aggregation is used to increase bandwidth and does not directly relate to this issue. \n- ARP settings are used to map IP addresses to MAC addresses but are not directly involved in VLAN configurations. \n- MDIX settings automatically detect and correct the cable type (straight-through or crossover) and aren't likely to be the issue."
    },
    {
        "question": "A technician is investigating packet loss to a device that has varying data bursts throughout the day. Which of the following will the technician MOST likely configure to resolve the issue?",
        "options": [
            "Flow control",
            "Jumbo frames",
            "Duplex",
            "Port mirroring"
        ],
        "correct_answer": 1,
        "description": "The correct answer is flow control. Flow control helps manage the rate at which data is sent to avoid packet loss during bursts of data. \n\n- Jumbo frames are larger packet sizes that can increase efficiency, but they are not directly related to preventing packet loss due to varying data bursts. \n- Duplex settings affect the communication method (half or full), but they are unlikely to resolve packet loss related to burst data. \n- Port mirroring is used for network monitoring and troubleshooting but does not directly address packet loss caused by data bursts."
    },
    {
        "question": "Which of the following connector types would be used to connect to the demarcation point and provide network access to a cable modem?",
        "options": [
            "F-type",
            "RJ45",
            "LC",
            "RJ11"
        ],
        "correct_answer": 1,
        "description": "The correct answer is F-type. F-type connectors are commonly used for cable modem connections at the demarcation point, providing a secure connection for coaxial cables. \n\n- RJ45 is used for Ethernet connections, not for coaxial cable-based modem connections. \n- LC connectors are used for fiber optic cables, which are not typically used at the demarcation point for cable modems. \n- RJ11 is used for telephone connections, not for broadband Internet access."
    },
    {
        "question": "Which of the following provides guidance to an employee about restricting non-business access to the company's videoconferencing solution?",
        "options": [
            "Acceptable use policy",
            "Data loss prevention",
            "Remote access policy",
            "Standard operating procedure"
        ],
        "correct_answer": 1,
        "description": "The correct answer is acceptable use policy. This policy defines the acceptable use of company resources, including videoconferencing solutions, and restricts non-business access. \n\n- Data loss prevention (DLP) deals with protecting sensitive data, not specifically regulating access to company tools. \n- Remote access policy addresses access to company networks remotely, not access to videoconferencing tools. \n- Standard operating procedure (SOP) outlines general procedures, but an acceptable use policy is more directly focused on access restrictions."
    },
    {
        "question": "Which of the following would MOST likely utilize PoE?",
        "options": [
            "A camera",
            "A printer",
            "A hub",
            "A modem"
        ],
        "correct_answer": 1,
        "description": "The correct answer is a camera. Power over Ethernet (PoE) is typically used to provide both power and data connectivity to devices like IP cameras. \n\n- A printer generally requires more power than PoE can supply, so it typically uses a separate power source. \n- A hub, which is a networking device, does not typically require PoE for operation. \n- A modem generally receives power from a wall outlet and does not use PoE."
    },
    {
        "question": "A security administrator is trying to prevent incorrect IP addresses from being assigned to clients on the network. Which of the following would MOST likely prevent this and allow the network to continue to operate?",
        "options": [
            "Configuring DHCP snooping on the switch",
            "Preventing broadcast messages leaving the client network",
            "Blocking ports 67/68 on the client network",
            "Enabling port security on access ports"
        ],
        "correct_answer": 1,
        "description": "The correct answer is configuring DHCP snooping on the switch. DHCP snooping prevents unauthorized DHCP servers from assigning IP addresses to clients, ensuring proper address assignment. \n\n- Preventing broadcast messages is not effective in stopping incorrect IP address assignments. \n- Blocking ports 67/68 would block DHCP traffic, which would stop all DHCP functions and prevent network connectivity. \n- Enabling port security is useful for limiting access to specific MAC addresses but does not directly prevent incorrect IP address assignments."
    },
    {
        "question": "Which of the following can have multiple VLAN interfaces?",
        "options": [
            "Hub",
            "Layer 3 switch",
            "Bridge",
            "Load balancer"
        ],
        "correct_answer": 2,
        "description": "The correct answer is Layer 3 switch. A Layer 3 switch can route traffic between different VLANs and can have multiple VLAN interfaces. \n\n- A hub does not support VLANs and does not have interfaces to handle multiple VLANs. \n- A bridge connects two network segments but does not have multiple VLAN interfaces. \n- A load balancer manages network traffic across servers but does not specifically support VLAN interfaces."
    },
    {
        "question": "A network technician needs to ensure that all files on a company's network can be moved in a safe and protected manner without interception from someone who is not the intended recipient. Which of the following would allow the network technician to meet these requirements?",
        "options": [
            "FTP",
            "TFTP",
            "SMTP",
            "SFTP"
        ],
        "correct_answer": 4,
        "description": "The correct answer is SFTP. Secure File Transfer Protocol (SFTP) encrypts files during transfer, ensuring they are protected from interception. \n\n- FTP is an insecure file transfer protocol that does not encrypt data. \n- TFTP (Trivial File Transfer Protocol) also does not provide encryption or security. \n- SMTP is a protocol for sending emails and is not used for securely transferring files."
    },
    {
        "question": "A device is connected to a managed Layer 3 network switch. The MAC address of the device is known, but the static IP address assigned to the device is not. Which of the following features of a Layer 3 network switch should be used to determine the IPv4 address of the device?",
        "options": [
            "MAC table",
            "Neighbor Discovery Protocol",
            "ARP table",
            "IPConfig",
            "ACL table"
        ],
        "correct_answer": 3,
        "description": "The correct answer is ARP table. The ARP table stores IP-to-MAC address mappings, which can help determine the IP address assigned to the device using its known MAC address. \n\n- The MAC table stores MAC addresses and associated switch ports but does not store IP addresses. \n- Neighbor Discovery Protocol (NDP) is used in IPv6 networks, not for determining IP addresses in an IPv4 network. \n- IPConfig is a command-line tool on Windows for displaying network configuration, but it would not be used on the switch. \n- ACL tables are used for filtering network traffic, not for determining IP addresses."
    },
    {
        "question": "Which of the following is the IEEE link cost for a Fast Ethernet interface in STP calculations?",
        "options": [
            "2",
            "4",
            "19",
            "100"
        ],
        "correct_answer": 2,
        "description": "The correct answer is 19. In STP calculations, the default link cost for Fast Ethernet is 19. \n\n- 2 is the cost for a 10 Mbps Ethernet link in STP. \n- 4 is the cost for a 100 Mbps Ethernet link, not for Fast Ethernet. \n- 100 is the cost for a gigabit Ethernet link."
    },


    {
    "question": "Two users on a LAN establish a video call. Which of the following OSI model layers ensures the initiation, coordination, and termination of the call?",
    "options": [
        "Session",
        "Physical",
        "Transport",
        "Data link"
    ],
    "correct_answer": 1,
    "description": "The correct answer is Session. The session layer is responsible for establishing, maintaining, and terminating sessions between devices, such as during a video call. \n\n- The physical layer handles the actual transmission of data but does not manage session initiation. \n- The transport layer ensures reliable data transfer but does not coordinate session management. \n- The data link layer is responsible for the physical addressing and error detection of data but does not manage sessions."
},

{
    "question": "A network administrator received a report stating a critical vulnerability was detected on an application that is exposed to the internet. Which of the following is the appropriate NEXT step?",
    "options": [
        "Check for the existence of a known exploit in order to assess the risk.",
        "Immediately shut down the vulnerable application server.",
        "Install a network access control agent on the server.",
        "Deploy a new server to host the application."
    ],
    "correct_answer": 1,
    "description": "The correct answer is to check for the existence of a known exploit. This allows the network administrator to assess the risk and determine if the vulnerability is actively being exploited. \n\n- Shutting down the server immediately might disrupt services and may not be the most effective first step. \n- Installing a network access control agent or deploying a new server are reactive solutions that do not directly address the immediate security risk posed by the vulnerability."
},

{
    "question": "A company is utilizing multifactor authentication for data center access. Which of the following is the MOST effective security mechanism against physical intrusions due to stolen credentials?",
    "options": [
        "Biometrics security hardware",
        "Access card readers",
        "Access control vestibule",
        "Motion detection cameras"
    ],
    "correct_answer": 1,
    "description": "The correct answer is biometrics security hardware. Biometrics, such as fingerprint or facial recognition, are a strong form of authentication and cannot be stolen like physical access cards. \n\n- Access card readers rely on something that can be stolen or duplicated. \n- An access control vestibule helps to restrict entry but does not provide authentication, which biometrics do. \n- Motion detection cameras are useful for monitoring, but they do not prevent physical intrusions."
},

{
    "question": "A help desk technician is concerned that a client's network cable issues may be causing intermittent connectivity. Which of the following would help the technician determine if this is the issue?",
    "options": [
        "Run the show interface command on the switch.",
        "Run the traceroute command on the server.",
        "Run iperf on the technician's desktop.",
        "Ping the client's computer from the router.",
        "Run a port scanner on the client's IP address."
    ],
    "correct_answer": 1,
    "description": "The correct answer is running the show interface command on the switch. This command provides detailed information about the interface, including errors that might be related to cable issues. \n\n- Traceroute is useful for identifying routing issues, not physical layer problems. \n- iperf tests bandwidth performance but may not reveal intermittent connectivity due to cable problems. \n- Pinging the client's computer can confirm connectivity but does not provide specific information about cable issues."
},

{
    "question": "An ISP is unable to provide services to a user in a remote area through cable and DSL. Which of the following is the NEXT best solution to provide services without adding external infrastructure?",
    "options": [
        "Fiber",
        "Leased line",
        "Satellite",
        "Metro optical"
    ],
    "correct_answer": 3,
    "description": "The correct answer is satellite. Satellite internet is ideal for remote areas where traditional wired options, such as cable and DSL, are unavailable. \n\n- Fiber and leased lines require significant infrastructure and might not be feasible in remote areas. \n- Metro optical is typically used in urban areas for high-speed connections, not remote locations."
},

{
    "question": "A new global ISP needs to connect from central offices in North America to the United Kingdom. Which of the following would be the BEST cabling solution for this project?",
    "options": [
        "Single-mode",
        "Coaxial",
        "Cat 6a",
        "Twinaxial"
    ],
    "correct_answer": 1,
    "description": "The correct answer is single-mode fiber. Single-mode fiber is designed for long-distance, high-speed connections, making it the best option for transatlantic connections. \n\n- Coaxial and Cat 6a cables are typically used for shorter distances and are not suitable for intercontinental connections. \n- Twinaxial cables are used in data centers for short-distance communication, not for global connections."
},

{
    "question": "A network engineer developed a plan of action to resolve an ongoing issue. Which of the following steps should the engineer take NEXT?",
    "options": [
        "Verify full system functionality and implement preventative measures.",
        "Implement the solution to resolve the problem.",
        "Document findings, actions, outcomes, and lessons learned.",
        "Establish a theory of probable cause."
    ],
    "correct_answer": 2,
    "description": "The correct answer is to implement the solution to resolve the problem. After developing a plan of action, the next step is to implement the solution to address the issue. \n\n- Verifying functionality and implementing preventative measures comes after the solution is implemented. \n- Documenting findings and lessons learned is done after the solution has been applied. \n- Establishing a theory of probable cause is a step that comes before developing a plan of action."
},

{
    "question": "Which of the following documents would be used to define uptime commitments from a provider, along with details on measurement and enforcement?",
    "options": [
        "NDA",
        "SLA",
        "MOU",
        "AUP"
    ],
    "correct_answer": 2,
    "description": "The correct answer is SLA (Service Level Agreement). An SLA defines uptime commitments, performance standards, and the measurement and enforcement of these standards. \n\n- NDA (Non-Disclosure Agreement) is used for confidentiality, not service levels. \n- MOU (Memorandum of Understanding) is an agreement outlining the intention of parties but does not detail specific commitments like uptime. \n- AUP (Acceptable Use Policy) defines acceptable usage of a service, not service levels."
},




{
    "question": "A network administrator is setting up a new phone system and needs to define the location where VoIP phones can download configuration files. Which of the following DHCP services can be used to accomplish this task?",
    "options": [
        "Scope options",
        "Exclusion ranges",
        "Lease time",
        "Relay"
    ],
    "correct_answer": 1,
    "description": "The correct answer is Scope options. Scope options in DHCP allow the administrator to specify various network configurations, such as the location where VoIP phones can download configuration files, through the DHCP server. \n\n- Exclusion ranges are used to prevent certain IP addresses from being assigned within the DHCP scope. \n- Lease time determines how long an IP address is assigned to a device, but it does not specify configuration file locations. \n- Relay is used to forward DHCP requests from clients to DHCP servers across different subnets, not to specify configuration file locations."
},

{
    "question": "Switch 3 was recently added to an existing stack to extend connectivity to various parts of the network. After the update, new employees were not able to print to the main networked copiers from their workstations. Following are the port configurations for the switch stack in question:\n\n**Switch 1 Configuration:**\n- Ports 1–12 (Workstations): VLAN 20, Status: Active\n- Ports 13–24 (Printers): VLAN 60, Status: Active\n- Ports 25–36 (Workstations): VLAN 20, Status: Active\n- Ports 37–44 (Wireless APs): VLAN 80, Status: Active\n- Ports 45–48 (Uplink): VLAN 20/60/80, Status: Active\n\n**Switch 2 Configuration:**\n- Ports 1–12 (Workstations): VLAN 20, Status: Active\n- Ports 13–24 (Printers): VLAN 60, Status: Active\n- Ports 25–36 (Workstations): VLAN 20, Status: Active\n- Ports 37–44 (Wireless APs): VLAN 80, Status: Active\n- Ports 45–48 (Uplink): VLAN 20/60/80, Status: Active\n\n**Switch 3 Configuration:**\n- Ports 1–12 (Workstations): VLAN 20, Status: Active\n- Ports 13–24 (Printers): VLAN 80, Status: Shut down\n- Ports 25–36 (Workstations): VLAN 20, Status: Shut down\n- Ports 37–44 (Wireless APs): VLAN 80, Status: Shut down\n- Ports 45–48 (Uplink): VLAN 20/60/80, Status: Active\n\nWhich of the following should be configured to resolve the issue? (Choose two.)",
    "options": [
        "Enable the printer ports on Switch 3.",
        "Reconfigure the duplex settings on the printer ports on Switch 3.",
        "Reconfigure the VLAN on all printer ports to VLAN 20.",
        "Enable all ports that are shut down on the stack.",
        "Reconfigure the VLAN on the printer ports on Switch 3.",
        "Enable wireless APs on Switch 3."
    ],
    "correct_answer": [1, 4],
    "description": "The correct answers are:\n\n1. **Enable the printer ports on Switch 3.**\n   - The printer ports on Switch 3 are currently marked as 'Shut down,' which prevents communication with the networked copiers. Enabling these ports is crucial to allow the new employees' workstations to communicate with the printers.\n\n4. **Enable all ports that are shut down on the stack.**\n   - Multiple ports across the stack are in a 'Shut down' state, as seen in the configuration tables. Enabling these ports will ensure connectivity and functionality for all devices connected to these ports.\n\n- **Reconfiguring the duplex settings (Option 2):** This is not required as all ports are already configured for full duplex, which is appropriate for the network.\n- **Reconfiguring the VLAN on all printer ports to VLAN 20 (Option 3):** This is unnecessary because VLAN 20 is already configured for printer ports in Switch 1 and Switch 2. The issue lies with the ports being disabled, not VLAN misconfiguration.\n- **Reconfiguring the VLAN on printer ports on Switch 3 (Option 5):** The VLAN assignment for printer ports on Switch 3 is correctly set to VLAN 80. Changing it to VLAN 20 would not align with the existing VLAN assignments for printers.\n- **Enabling wireless APs on Switch 3 (Option 6):** This option is irrelevant to resolving the printer connectivity issue as it pertains to wireless access points, not printers."
},



#301-350




    {
        "question": "An engineer needs to restrict the database servers that are in the same subnet from communicating with each other. The database servers will still need to communicate with the application servers in a different subnet. In some cases, the database servers will be clustered, and the servers will need to communicate with other cluster members. Which of the following technologies will be BEST to use to implement this filtering without creating rules?",
        "options": [
            "Private VLANs",
            "Access control lists",
            "Firewalls",
            "Control plane policing"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Private VLANs. Private VLANs can isolate devices within the same subnet while still allowing specific traffic, such as cluster communications, to pass through. \n\n- Access control lists (ACLs) require manually defined rules, which contradict the requirement for a solution without rules. \n- Firewalls operate at a different level and are not suitable for intra-subnet communication restrictions. \n- Control plane policing is used to manage and limit control plane traffic, not inter-device communication."
    },
    {
        "question": "A technician was cleaning a storage closet and found a box of transceivers labeled 8Gbps. Which of the following protocols uses those transceivers?",
        "options": [
            "Coaxial over Ethernet",
            "Internet Small Computer Systems Interface",
            "Fibre Channel",
            "Gigabit interface converter"
        ],
        "correct_answer": 3,
        "description": "The correct answer is Fibre Channel. Fibre Channel is a high-speed protocol that supports 8Gbps transceivers, commonly used in SAN (Storage Area Network) environments. \n\n- Coaxial over Ethernet does not utilize transceivers for Fibre Channel speeds. \n- Internet Small Computer Systems Interface (iSCSI) is a protocol for transmitting SCSI commands over IP, not related to these transceivers. \n- Gigabit interface converter (GBIC) is an older technology that does not support 8Gbps speeds."
    },
    {
        "question": "A customer wants to log in to a vendor's server using a web browser on a laptop. Which of the following would require the LEAST configuration to allow encrypted access to the server?",
        "options": [
            "Secure Sockets Layer",
            "Site-to-site VPN",
            "Remote desktop gateway",
            "Client-to-site VPN"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Secure Sockets Layer (SSL). SSL enables encrypted communication directly through a web browser without requiring complex configuration. \n\n- Site-to-site VPNs are used to connect networks, requiring additional configuration and are not ideal for individual browser-based connections. \n- Remote desktop gateways involve significant setup and are not designed for direct web browser communication. \n- Client-to-site VPNs require the installation and configuration of a VPN client, adding complexity."
    },
    {
        "question": "A user calls the IT department to report being unable to log in after locking the computer. The user resets the password, but later in the day the user is again unable to log in after locking the computer. Which of the following attacks against the user is MOST likely taking place?",
        "options": [
            "Brute-force",
            "On-path",
            "Deauthentication",
            "Phishing"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Brute-force. Brute-force attacks repeatedly try different combinations of passwords to gain access to an account, which can explain the repeated lockouts. \n\n- On-path attacks intercept communication but do not cause lockouts. \n- Deauthentication attacks disrupt network connectivity but are unrelated to account lockouts. \n- Phishing involves tricking the user into revealing sensitive information and does not explain repeated lockouts."
    },
    {
        "question": "A network administrator determines that even when optimal wireless coverage is configured, the network users still report constant disconnections. After troubleshooting, the administrator determines that moving from one location to another causes the disconnection. Which of the following settings should provide better network stability?",
        "options": [
            "Client association timeout",
            "RSSI roaming threshold",
            "RF attenuation ratio",
            "EIRP power setting"
        ],
        "correct_answer": 2,
        "description": "The correct answer is RSSI roaming threshold. Configuring the RSSI roaming threshold ensures smooth transitions between access points as devices move, improving stability. \n\n- Client association timeout affects how long a device remains connected but does not address disconnections while roaming. \n- RF attenuation ratio pertains to signal degradation due to obstacles, not roaming. \n- EIRP power setting controls signal strength but does not directly impact roaming behavior."
    },
    {
        "question": "At which of the following layers of the OSI model will the administrator MOST likely start to troubleshoot when a network is experiencing a number of CRC errors?",
        "options": [
            "Layer 1",
            "Layer 2",
            "Layer 3",
            "Layer 4",
            "Layer 5",
            "Layer 6",
            "Layer 7"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Layer 1. CRC errors often indicate issues with the physical layer, such as cabling or interference. \n\n- Layer 2 involves data link issues, which might show CRC errors, but the root cause usually lies in Layer 1. \n- Layers 3 to 7 deal with higher-level protocols and are not directly responsible for CRC errors."
    },
    {
        "question": "Which of the following uses the link-state routing algorithm and operates within a single autonomous system?",
        "options": [
            "EIGRP",
            "OSPF",
            "RIP",
            "BGP"
        ],
        "correct_answer": 2,
        "description": "The correct answer is OSPF. OSPF uses the link-state routing algorithm and is designed for operation within a single autonomous system. \n\n- EIGRP is a distance-vector protocol, not a link-state protocol. \n- RIP uses the distance-vector algorithm and is less efficient than OSPF. \n- BGP operates between autonomous systems, not within a single one."
    },


    {
        "question": "A network administrator is designing a wireless network. The administrator must ensure a rented office space has a sufficient signal. Reducing exposure to the wireless network is important, but it is secondary to the primary objective. Which of the following would MOST likely facilitate the correct accessibility to the Wi-Fi network?",
        "options": [
            "Polarization",
            "Channel utilization",
            "Channel bonding",
            "Antenna type",
            "MU-MIMO"
        ],
        "correct_answer": 4,
        "description": "The correct answer is antenna type. Selecting the proper antenna type ensures that the Wi-Fi signal reaches the intended area within the rented office space while minimizing interference. \n\n- Polarization focuses on the alignment of the signal but does not primarily affect coverage area. \n- Channel utilization optimizes bandwidth but does not ensure sufficient coverage. \n- Channel bonding improves throughput but does not directly address signal accessibility. \n- MU-MIMO enhances multi-device connectivity but does not resolve overall coverage issues."
    },
    {
        "question": "An office area contains two PoE-enabled WAPs. After the area was remodeled, new cable uplinks were installed in the ceiling above the fluorescent lights. However, after the WAPs were reconnected, users reported slowness and application errors. An intern reviewed the network and discovered a lot of CRC errors. A network engineer reviewed the intern's work and realized UTP cabling was used. Which of the following is the MOST likely cause of the CRC errors?",
        "options": [
            "Insufficient power at the antennas",
            "PoE and UTP incompatibility",
            "Electromagnetic interference",
            "Wrong cable pinout"
        ],
        "correct_answer": 3,
        "description": "The correct answer is electromagnetic interference. Fluorescent lights can cause electromagnetic interference (EMI), which affects signal transmission through UTP cables. \n\n- Insufficient power at the antennas would not cause CRC errors but may reduce performance. \n- PoE and UTP are compatible; incompatibility is unlikely the issue. \n- Wrong cable pinout results in connectivity failures, not CRC errors."
    },
    {
        "question": "Several users with older devices are reporting intermittent connectivity while in an outdoor patio area. After some research, the network administrator determines that an outdoor WAP might help with the issue. However, the company does not want the signal to bleed into the building and cause interference. Which of the following should the network administrator perform to BEST resolve the issue?",
        "options": [
            "Disable the SSID broadcast on the WAP in the patio area.",
            "Install a WAP and enable 5GHz only within the patio area.",
            "Install a directional WAP in the direction of the patio.",
            "Install a repeater on the back wall of the patio area."
        ],
        "correct_answer": 3,
        "description": "The correct answer is install a directional WAP in the direction of the patio. A directional WAP focuses the signal in a specific area, ensuring connectivity without causing interference within the building. \n\n- Disabling the SSID broadcast does not prevent interference. \n- Enabling only 5GHz may improve performance but does not address directional signal control. \n- A repeater extends coverage but does not control signal bleed effectively."
    },
    {
        "question": "Which of the following is most likely to have the HIGHEST latency while being the most accessible?",
        "options": [
            "Satellite",
            "DSL",
            "Cable",
            "4G"
        ],
        "correct_answer": 1,
        "description": "The correct answer is satellite. Satellite internet typically experiences the highest latency due to the long distance data must travel between the satellite and the Earth. \n\n- DSL and cable have much lower latencies and are common in urban areas. \n- 4G offers lower latency and is widely accessible compared to satellite."
    },
    {
        "question": "Which of the following is used to elect an STP root?",
        "options": [
            "A bridge ID",
            "A bridge protocol data unit",
            "Interface port priority",
            "A switch's root port"
        ],
        "correct_answer": 1,
        "description": "The correct answer is a bridge ID. The bridge ID, which includes the switch's priority and MAC address, is used to elect the root bridge in Spanning Tree Protocol (STP). \n\n- A bridge protocol data unit is used for communication but does not elect the root. \n- Interface port priority determines path selection, not root election. \n- A root port is chosen after the root bridge is elected."
    },
    {
        "question": "Which of the following commands can be used to display the IP address, subnet address, gateway address, and DNS address on a Windows computer?",
        "options": [
            "netstat -a",
            "ifconfig",
            "ip addr",
            "ipconfig /all"
        ],
        "correct_answer": 4,
        "description": "The correct answer is ipconfig /all. This command provides detailed network configuration information, including IP, subnet, gateway, and DNS addresses on Windows systems. \n\n- netstat -a shows active connections and listening ports, not detailed network configurations. \n- ifconfig and ip addr are Linux commands, not native to Windows."
    },

    {
        "question": "A user calls the help desk to report being unable to reach a file server. The technician logs in to the user’s computer and verifies that pings fail to respond back when trying to reach the file server. Which of the following would BEST help the technician verify whether the file server is reachable?",
        "options": [
            "netstat",
            "ipconfig",
            "nslookup",
            "traceroute"
        ],
        "correct_answer": 4,
        "description": "The correct answer is traceroute. It helps determine the path to the file server and identifies where communication is failing. \n\n- netstat is for checking active connections but does not verify server reachability. \n- ipconfig provides network configuration details, which are useful but not specific to reachability. \n- nslookup is used for DNS resolution, not for tracing the network path."
    },
    {
        "question": "An employee reports to a network administrator that internet access is not working. Which of the following should the administrator do FIRST?",
        "options": [
            "Establish a theory of probable cause.",
            "Identify symptoms.",
            "Determine if anything has changed.",
            "Ask the user to restart the computer."
        ],
        "correct_answer": 2,
        "description": "The correct answer is Identify symptoms. This step gathers crucial information about the problem before proceeding to analysis or troubleshooting. \n\n- Establishing a theory of probable cause comes after identifying symptoms. \n- Determining if anything has changed requires prior identification of symptoms. \n- Asking the user to restart the computer is a common step but should only come after identifying symptoms."
    },
    {
        "question": "A security engineer is installing a new IDS on the network. The engineer has asked a network administrator to ensure all traffic entering and leaving the router interface is available for the IDS. Which of the following should the network administrator do?",
        "options": [
            "Install a network tap for the IDS.",
            "Configure ACLs to route traffic to the IDS.",
            "Install an additional NIC into the IDS.",
            "Install a loopback adapter for the IDS.",
            "Add an additional route on the router for the IDS."
        ],
        "correct_answer": 1,
        "description": "The correct answer is Install a network tap for the IDS. A network tap enables passive traffic monitoring, ensuring all traffic is visible to the IDS. \n\n- Configuring ACLs routes traffic but does not provide a comprehensive traffic view for the IDS. \n- Adding an additional NIC to the IDS does not address visibility for all router traffic. \n- Installing a loopback adapter is unrelated to traffic visibility. \n- Adding an additional route to the router does not provide full traffic monitoring for the IDS."
    },
    {
        "question": "An employee working in a warehouse facility is experiencing interruptions in mobile applications while walking around the facility. According to a recent site survey, the WLAN comprises autonomous APs that are directly connected to the internet, providing adequate signal coverage. Which of the following is the BEST solution to improve network stability?",
        "options": [
            "Implement client roaming using an extended service deployment employing a wireless controller.",
            "Remove omnidirectional antennas and adopt a directional bridge.",
            "Ensure all APs of the warehouse support MIMO and Wi-Fi 4.",
            "Verify that the level of EIRP power settings is set to the maximum permitted by regulations."
        ],
        "correct_answer": 1,
        "description": "The correct answer is Implement client roaming using an extended service deployment employing a wireless controller. This solution ensures seamless handoff between APs, reducing interruptions. \n\n- Removing omnidirectional antennas and adopting a directional bridge does not address roaming issues. \n- Supporting MIMO and Wi-Fi 4 is beneficial but does not resolve roaming problems. \n- Setting EIRP power to maximum might improve coverage but won't ensure stable roaming."
    },
    {
        "question": "Which of the following will reduce routing table lookups by performing packet forwarding decisions independently of the network layer header?",
        "options": [
            "MPLS",
            "mGRE",
            "EIGRP",
            "VRRP"
        ],
        "correct_answer": 1,
        "description": "The correct answer is MPLS. It uses labels for packet forwarding, bypassing the need for routing table lookups, which improves efficiency. \n\n- mGRE is used for dynamic tunneling, not routing optimization. \n- EIGRP is a routing protocol and does not bypass routing table lookups. \n- VRRP is used for router redundancy, not packet forwarding optimization."
    },
    {
        "question": "While walking from the parking lot to an access-controlled door, an employee sees an authorized user open the door. Then the employee notices that another person catches the door before it closes and goes inside. Which of the following attacks is taking place?",
        "options": [
            "Tailgating",
            "Piggybacking",
            "Shoulder surfing",
            "Phishing"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Tailgating. This occurs when an unauthorized person follows an authorized user through a secure door without authentication. \n\n- Piggybacking implies consent from the authorized person, which is not described in this scenario. \n- Shoulder surfing involves spying on sensitive information, unrelated to physical access. \n- Phishing is a social engineering attack, unrelated to physical access control."
    },
{
    "question": "Given the following information:\n\nConnection details:\n\n- PC A to Switch 1: 394ft (120m), Cat 5, Straight-through\n- Switch 1 to Switch 2: 3.3ft (1m), Cat 6, Crossover\n- Switch 2 to PC B: 16ft (5m), Cat 5, Straight-through\n\nWhich of the following would cause performance degradation between PC A and PC B?",
    "options": [
        "Attenuation",
        "Interference",
        "Decibel loss",
        "Incorrect pinout"
    ],
    "correct_answer": 1,
    "description": "The correct answer is Attenuation. Attenuation refers to the loss of signal strength over long cable distances. The 394ft (120m) Cat 5 cable exceeds the recommended maximum length for Ethernet (100m), which can result in signal degradation. \n\n- Interference is caused by electromagnetic signals from external sources but is less likely in this scenario with shielded cables.\n- Decibel loss is a measurement of signal loss that could be related to attenuation but is not the direct cause here.\n- Incorrect pinout results in improper connectivity, but the question specifies that the configurations are correct (Straight-through and Crossover as needed)."
},


    {
        "question": "An engineer recently decided to upgrade the firmware on a router. During the upgrade, the help desk received calls about a network outage, and a critical ticket was opened. The network manager would like to create a policy to prevent this from happening in the future. Which of the following documents should the manager create?",
        "options": [
            "Change management",
            "Incident response",
            "Standard operating procedure",
            "System life cycle"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Change management. This policy ensures that all changes, including firmware upgrades, follow a structured process to minimize disruption to network operations. \n\n- Incident response deals with identifying and mitigating security incidents, not preventing planned disruptions. \n- Standard operating procedures are general operational guidelines but do not focus specifically on changes. \n- System life cycle focuses on the stages of a system's development and retirement, not operational changes."
    },
    {
        "question": "A technician is deploying a new SSID for an industrial control system. The control devices require the network to use encryption that employs TKIP and a symmetrical password to connect. Which of the following should the technician configure to ensure compatibility with the control devices?",
        "options": [
            "WPA2-Enterprise",
            "WPA-Enterprise",
            "WPA-PSK",
            "WPA2-PSK"
        ],
        "correct_answer": 3,
        "description": "The correct answer is WPA-PSK. WPA with Pre-Shared Key (PSK) uses TKIP encryption and a shared password, ensuring compatibility with legacy control systems. \n\n- WPA2-Enterprise and WPA-Enterprise require an authentication server, which is not compatible with the described setup. \n- WPA2-PSK employs stronger encryption (AES), which may not be supported by the control devices relying on TKIP."
    },
    {
        "question": "Which of the following ports should be used to securely receive mail that is synchronized across multiple devices?",
        "options": [
            "25",
            "110",
            "443",
            "993"
        ],
        "correct_answer": 4,
        "description": "The correct answer is 993. This port is used for secure IMAP (Internet Message Access Protocol) connections, which allow mail synchronization across multiple devices. \n\n- Port 25 is used for sending emails via SMTP, not receiving them. \n- Port 110 is for unencrypted POP3, which does not support synchronization. \n- Port 443 is for HTTPS traffic and unrelated to email protocols."
    },
    {
        "question": "A network administrator is getting reports of some internal users who cannot connect to network resources. The users state they were able to connect last week, but not today. No changes have been configured on the network devices or server during the last few weeks. Which of the following is the MOST likely cause of the issue?",
        "options": [
            "The client DHCP scope is fully utilized.",
            "The wired network is experiencing electrical interference.",
            "The captive portal is down and needs to be restarted.",
            "SNMP traps are being received.",
            "The packet counter on the router interface is high."
        ],
        "correct_answer": 1,
        "description": "The correct answer is The client DHCP scope is fully utilized. If the DHCP server runs out of available IP addresses, new devices cannot connect to the network. \n\n- Electrical interference affects wireless networks, not wired connections. \n- A captive portal issue typically affects public Wi-Fi users, not internal users. \n- SNMP traps monitor network events but do not directly cause connectivity issues. \n- A high packet counter on the router interface indicates traffic volume but is unlikely to prevent connectivity."
    },
    {
        "question": "A network administrator needs to provide evidence to confirm that recent network outages were caused by increased traffic generated by a recently released application. Which of the following actions will BEST support the administrator's response?",
        "options": [
            "Generate a network baseline report for comparison.",
            "Export the firewall traffic logs.",
            "Collect the router's NetFlow data.",
            "Plot interface statistics for dropped packets."
        ],
        "correct_answer": 3,
        "description": "The correct answer is Collect the router's NetFlow data. NetFlow provides detailed information about traffic patterns and can identify the specific application causing the increase. \n\n- A baseline report helps compare normal and current activity but does not pinpoint the cause of traffic. \n- Firewall logs show allowed and blocked traffic but may not attribute traffic to a specific application. \n- Interface statistics highlight dropped packets but do not provide traffic details."
    },
    {
        "question": "During a recent security audit, a contracted penetration tester discovered the organization uses a number of insecure protocols. Which of the following ports should be disallowed so only encrypted protocols are allowed? (Choose two.)",
        "options": [
            "22",
            "23",
            "69",
            "443",
            "587",
            "8080"
        ],
        "correct_answer": [2, 3],
        "description": "The correct answers are 23 and 69. Port 23 is used for Telnet, and port 69 is for TFTP, both of which are insecure protocols that do not encrypt data. \n\n- Port 22 is used for SSH, which is secure. \n- Port 443 is used for HTTPS, providing encrypted web communication. \n- Port 587 is for secure email submission. \n- Port 8080 is typically used for web traffic and may or may not be encrypted depending on configuration."
    },
    {
        "question": "A technician is configuring a static IP address on a new device in a newly created subnet. The work order specifies the following requirements:\n- The IP address should use the highest address available in the subnet.\n- The default gateway needs to be set to 172.28.85.94.\n- The subnet mask needs to be 255.255.255.224.\n\nWhich of the following addresses should the engineer apply to the device?",
        "options": [
            "172.28.85.93",
            "172.28.85.95",
            "172.28.85.254",
            "172.28.85.255"
        ],
        "correct_answer": 1,
        "description": "The correct answer is 172.28.85.93. With a subnet mask of 255.255.255.224, the highest usable address in the subnet is 172.28.85.93. \n\n- 172.28.85.95 is the broadcast address for the subnet and cannot be assigned to a device. \n- 172.28.85.254 and 172.28.85.255 are outside the range of the specified subnet."
    },
    {
        "question": "A network technician is troubleshooting an area where the wireless connection to devices is poor. The technician theorizes that the signal-to-noise ratio in the area is causing the issue. Which of the following should the technician do NEXT?",
        "options": [
            "Run diagnostics on the relevant devices.",
            "Move the access point to a different location.",
            "Escalate the issue to the vendor's support team.",
            "Remove any electronics that might be causing interference."
        ],
        "correct_answer": 2,
        "description": "The correct answer is Move the access point to a different location. Relocating the access point can improve the signal-to-noise ratio and provide better wireless coverage. \n\n- Running diagnostics provides information but does not directly resolve the issue. \n- Escalating the issue to the vendor is premature without attempting basic fixes. \n- Removing electronics may help but is not the first step to address poor coverage."
    },
    {
        "question": "Which of the following must be functioning properly in order for a network administrator to create an accurate timeline during a troubleshooting process?",
        "options": [
            "NTP",
            "IP helper",
            "Syslog",
            "MySQL"
        ],
        "correct_answer": 1,
        "description": "The correct answer is NTP. Network Time Protocol (NTP) ensures that all devices on the network have synchronized timestamps, enabling accurate timelines. \n\n- IP helper is used for DHCP relay and unrelated to time synchronization. \n- Syslog collects and stores logs but requires synchronized timestamps to be effective. \n- MySQL is a database system and not involved in network troubleshooting timelines."
    },
    {
        "question": "A large metropolitan city is looking to standardize the ability for police department laptops to connect to the city government's VPN. The city would like a wireless solution that provides the largest coverage across the city with a minimal number of transmission towers. Latency and overall bandwidth needs are not high priorities. Which of the following would BEST meet the city's needs?",
        "options": [
            "5G",
            "LTE",
            "Wi-Fi 4",
            "Wi-Fi 5",
            "Wi-Fi 6"
        ],
        "correct_answer": 2,
        "description": "The correct answer is LTE. LTE offers wide coverage and requires fewer transmission towers, making it ideal for a city-wide network with moderate bandwidth and latency requirements. \n\n- 5G provides faster speeds but requires more towers due to limited range. \n- Wi-Fi 4, Wi-Fi 5, and Wi-Fi 6 are local-area technologies and not suitable for city-wide coverage."
    },


    {
        "question": "Which of the following physical security methods is the MOST effective to prevent tailgating?",
        "options": [
            "Biometrics in an access control vestibule.",
            "IP cameras with motion detection.",
            "Smart lockers with tamper protection.",
            "Badge readers plus a PIN pad."
        ],
        "correct_answer": 1,
        "description": "The correct answer is biometrics in an access control vestibule. This method effectively ensures only authorized personnel can enter, as it combines physical barriers with advanced biometric verification. \n\n- IP cameras with motion detection can record incidents but do not actively prevent tailgating. \n- Smart lockers with tamper protection are unrelated to controlling physical access. \n- Badge readers plus a PIN pad add security but do not directly prevent tailgating without physical barriers."
    },
    {
        "question": "A network client is trying to connect to the wrong TCP port. Which of the following responses would the client MOST likely receive?",
        "options": [
            "RST.",
            "FIN.",
            "ICMP Time Exceeded.",
            "Redirect."
        ],
        "correct_answer": 1,
        "description": "The correct answer is RST (Reset). When a client tries to connect to an incorrect TCP port, the server will send an RST packet to indicate the connection attempt is invalid. \n\n- FIN is used to gracefully close a connection, not reject one. \n- ICMP Time Exceeded is used in routing and not related to TCP port connections. \n- Redirect is used to inform the client of a different route, not for incorrect TCP port attempts."
    },
    {
        "question": "A company's data center is hosted at its corporate office to ensure greater control over the security of sensitive data. During times when there are increased workloads, some of the company's non-sensitive data is shifted to an external cloud provider. Which of the following cloud deployment models does this describe?",
        "options": [
            "Hybrid.",
            "Community.",
            "Public.",
            "Private."
        ],
        "correct_answer": 1,
        "description": "The correct answer is hybrid. A hybrid cloud model combines on-premises data centers with external cloud services, allowing flexibility to handle varying workloads. \n\n- Community clouds are shared environments tailored to a specific group or industry. \n- Public clouds are entirely external and not managed by the company. \n- Private clouds are hosted entirely on-premises or dedicated infrastructure, with no external cloud integration."
    },
{
  "question": "A network engineer needs to create a subnet that has the capacity for five VLANs, with the following number of clients to be allowed on each:\n\nVLAN 10 - 50 users\nVLAN 20 - 35 users\nVLAN 30 - 20 users\nVLAN 40 - 75 users\nVLAN 50 - 130 users\n\nWhich of the following is the SMALLEST subnet capable of this setup that also has the capacity to double the number of clients in the future?",
  "options": [
    "10.0.0.0/21",
    "10.0.0.0/22",
    "10.0.0.0/23",
    "10.0.0.0/24"
  ],
  "correct_answer": 1,
  "description": "The correct answer is 10.0.0.0/21. A /21 subnet provides 2048 IP addresses, which is enough for the total number of current users (310) and leaves room for doubling the number of clients in the future (620). \n\n- A /22 subnet provides 1024 addresses, which is insufficient for the required setup and future growth.\n- A /23 subnet provides 512 addresses, which is not enough to support all five VLANs now and in the future.\n- A /24 subnet only provides 256 addresses, which is far too small for this setup and future growth."
},

  {
    "question": "A network technician is selecting a replacement for a damaged fiber cable that goes directly to an SFP transceiver on a network switch. Which of the following cable connectors should be used?",
    "options": [
      "RJ45",
      "LC",
      "MT",
      "F-type"
    ],
    "correct_answer": 2,
    "description": "The correct answer is LC. LC connectors are commonly used for fiber optic connections and are compatible with Small Form-factor Pluggable (SFP) transceivers on network switches. \n\n- RJ45 connectors are used for Ethernet cables and do not work with fiber optics or SFP transceivers.\n- MT (MTP/MPO) connectors are used in multi-fiber connections, typically for high-density applications, and are not suitable for direct fiber-to-SFP connections.\n- F-type connectors are used for coaxial cable connections, not fiber optic cables."
  },
  {
    "question": "A company is deploying a SAN at headquarters and a branch office 1,000mi (1,609km) away that will access small amounts of data. Which of the following types of connections would be MOST cost effective to implement?",
    "options": [
      "iSCSI",
      "FCoE",
      "Ethernet",
      "FC"
    ],
    "correct_answer": 1,
    "description": "The correct answer is iSCSI. iSCSI is a cost-effective solution for connecting storage devices over long distances, using existing IP networks. It is ideal for accessing small amounts of data and does not require expensive infrastructure. \n\n- FCoE (Fibre Channel over Ethernet) is a more expensive option and typically used in high-performance environments that require high throughput.\n- Ethernet is a general-purpose network protocol and can work for SANs, but iSCSI is the specific solution for storage networking over Ethernet.\n- FC (Fibre Channel) is a high-speed protocol typically used for enterprise-level SANs, but it requires dedicated, expensive hardware for long-distance connections."
  },
  {
    "question": "A company wants to add a local redundant data center to its network in case of failure at its primary location. Which of the following would give the LEAST amount of redundancy for the company's network?",
    "options": [
      "Cold site",
      "Hot site",
      "Cloud site",
      "Warm site"
    ],
    "correct_answer": 1,
    "description": "The correct answer is Cold site. A cold site is essentially an empty data center space with no equipment or active services, meaning it requires significant setup before it can be used in case of failure. It offers the least redundancy. \n\n- Hot site provides full redundancy, with an active, running replica of the primary data center ready to take over at any time.\n- Cloud site offers flexibility and redundancy through cloud-based services, often with multiple backup options.\n- Warm site is a compromise between a cold site and hot site, with partially configured equipment and systems that can be quickly made operational."
  },



  {
    "question": "A new student is given credentials to log on to the campus Wi-Fi. The student stores the password in a laptop and is able to connect: however, the student is not able to connect with a phone when only a short distance from the laptop. Given the following information:\n\nSignal strength                                  90%\nCoverage                                            80%\nInterference                                       15%\nNumber of connection attempts     10\n\nWhich of the following is MOST likely causing this connection failure?",
    "options": [
      "Transmission speed",
      "Incorrect passphrase",
      "Channel overlap",
      "Antenna cable attenuation/signal loss"
    ],
    "correct_answer": 3,
    "description": "The correct answer is Channel overlap. The Wi-Fi network is likely experiencing interference from nearby networks using the same or similar channels, which can cause connectivity issues for devices at the edge of the coverage area, such as the student's phone. \n\n- Transmission speed typically does not affect initial connection attempts unless the signal is weak or the network is congested, but this is not the most likely cause here.\n- Incorrect passphrase would cause authentication failures, but the student can connect from the laptop, indicating the passphrase is correct.\n- Antenna cable attenuation or signal loss would typically affect all devices, not just the phone, and is less likely given the signal strength is already strong."
  },
  {
    "question": "A technician manages a DHCP scope but needs to allocate a portion of the scope’s subnet for statically assigned devices. Which of the following DHCP concepts would be BEST to use to prevent IP address conflicts?",
    "options": [
      "Dynamic assignment",
      "Exclusion range",
      "Address reservation",
      "IP helper"
    ],
    "correct_answer": 3,
    "description": "The correct answer is Address reservation. Address reservation allows the DHCP server to always assign the same IP address to a device based on its MAC address, preventing conflicts with dynamically assigned addresses. \n\n- Dynamic assignment is the default method of allocating IP addresses and is not effective for statically assigned devices.\n- Exclusion range is used to prevent the DHCP server from assigning IP addresses in a specified range, but address reservation is a better solution for ensuring static IP assignments.\n- IP helper is used to forward DHCP requests from clients on remote networks to the DHCP server and is not relevant to preventing IP address conflicts."
  },
  {
    "question": "Due to a surge in business, a company is onboarding an unusually high number of salespeople. The salespeople are assigned desktops that are wired to the network. The last few salespeople to be onboarded are able to access corporate materials on the network but not sales-specific resources. Which of the following is MOST likely the cause?",
    "options": [
      "The switch was configured with port security.",
      "Newly added machines are running into DHCP conflicts.",
      "The IPS was not configured to recognize the new users.",
      "Recently added users were assigned to the wrong VLAN"
    ],
    "correct_answer": 4,
    "description": "The correct answer is Recently added users were assigned to the wrong VLAN. VLAN misconfigurations can prevent access to specific network resources, such as sales-specific resources. \n\n- Port security would restrict access based on MAC addresses, but it would prevent any connection, not just specific resources.\n- DHCP conflicts would affect the ability to connect to the network, but the users can access corporate materials, suggesting IP assignment is functioning properly.\n- IPS (Intrusion Prevention System) configuration issues would typically block or alert on malicious activity, not affect access to resources directly."
  },
  {
    "question": "A technician wants to monitor and provide traffic segmentation across the network. The technician would like to assign each department a specific identifier. Which of the following will the technician MOST likely use?",
    "options": [
      "Flow control",
      "Traffic shaping",
      "VLAN tagging",
      "Network performance baselines"
    ],
    "correct_answer": 3,
    "description": "The correct answer is VLAN tagging. VLAN tagging is used to assign specific identifiers (tags) to traffic from different departments, enabling traffic segmentation and monitoring across the network. \n\n- Flow control manages the rate of data transmission between devices but does not segment traffic by department.\n- Traffic shaping controls the amount and rate of traffic to ensure efficient network utilization but does not provide segmentation.\n- Network performance baselines are used to monitor network performance but do not segment traffic by department."
  },
  {
    "question": "Network users reported that a recent firmware upgrade to a firewall did not resolve the issue that prompted the upgrade. Which of the following should be performed NEXT?",
    "options": [
      "Reopen the service ticket, request a new maintenance window, and roll back to the anterior firmware version.",
      "Gather additional information to ensure users' concerns are not been caused by a different issue with similar symptoms.",
      "Employ a divide-and-conquer troubleshooting methodology by engaging the firewall vendor's support.",
      "Escalate the issue to the IT management team in order to negotiate a new SLA with the user's manager."
    ],
    "correct_answer": 2,
    "description": "The correct answer is Gather additional information to ensure users' concerns are not been caused by a different issue with similar symptoms. This is an important step to rule out any new causes or misdiagnosis of the issue after the firmware upgrade. \n\n- Rolling back to the previous firmware version should be considered after further troubleshooting, not as the immediate next step.\n- Engaging vendor support may be necessary, but first, additional information should be gathered to ensure the issue is properly diagnosed.\n- Escalating to management is not appropriate unless all troubleshooting steps have been exhausted."
  },
  {
    "question": "An administrator would like to allow Windows clients from outside the office to access workstations without using third-party software. Which of the following access methods would meet this requirement?",
    "options": [
      "Remote desktop gateway",
      "Split tunnel",
      "Site-to-site VPN",
      "VNC"
    ],
    "correct_answer": 1,
    "description": "The correct answer is Remote desktop gateway. A Remote Desktop Gateway allows users to securely connect to internal workstations over the internet without the need for third-party software, as it provides a secure channel for remote desktop connections. \n\n- Split tunnel is a VPN configuration that allows users to access both the local network and the internet simultaneously, but it is not specifically for accessing workstations.\n- Site-to-site VPN connects entire networks to each other, not individual users to workstations.\n- VNC requires third-party software for both the client and the server side, and thus does not meet the requirement of not using third-party software."
  },


    {
        "question": "A client who shares office space and an IT closet with another company recently reported connectivity issues throughout the network. Multiple third-party vendors regularly perform on-site maintenance in the shared IT closet. Which of the following security techniques would BEST secure the physical networking equipment?",
        "options": [
            "Disabling unneeded switchports",
            "Implementing role-based access",
            "Changing the default passwords",
            "Configuring an access control list"
        ],
        "correct_answer": 2,
        "description": "The correct answer is implementing role-based access. By restricting physical access to networking equipment based on roles, you ensure that only authorized personnel can make changes or perform maintenance. \n\n- Disabling unneeded switchports is a good security measure for the network but doesn't secure physical access to the equipment. \n- Changing the default passwords helps secure devices but does not address physical access control. \n- Configuring an access control list (ACL) applies to network traffic rather than physical access to networking equipment."
    },
    {
        "question": "A network engineer is investigating issues on a Layer 2 switch. The department typically shares a switchport during meetings for presentations, but after the first user shares, no other users can connect. Which of the following is MOST likely related to this issue?",
        "options": [
            "Spanning Tree Protocol is enabled on the switch.",
            "VLAN trunking is enabled on the switch.",
            "Port security is configured on the switch.",
            "Dynamic ARP inspection is configured on the switch."
        ],
        "correct_answer": 3,
        "description": "The correct answer is port security is configured on the switch. Port security is a feature that limits the number of MAC addresses that can be learned on a port, which can cause issues if multiple devices attempt to use the same port. \n\n- Spanning Tree Protocol helps prevent loops but would not cause issues with multiple users connecting to a switchport. \n- VLAN trunking is used to carry multiple VLANs over a single link, which is unrelated to this specific issue. \n- Dynamic ARP inspection is used to protect against ARP spoofing attacks and would not cause connectivity issues based on port sharing."
    },
    {
        "question": "A company's web server is hosted at a local ISP. This is an example of:",
        "options": [
            "Colocation",
            "An on-premises data center",
            "A branch office",
            "A cloud provider"
        ],
        "correct_answer": 1,
        "description": "The correct answer is colocation. Colocation refers to renting space at an ISP's data center where the company owns and manages the servers, but the ISP provides the infrastructure and physical security. \n\n- An on-premises data center means the company owns and operates the data center on-site, which is not the case here. \n- A branch office refers to a secondary location of a business, not a hosting facility. \n- A cloud provider refers to services provided by companies like AWS or Azure, where servers and infrastructure are virtualized and managed remotely."
    },
    {
        "question": "A network administrator is preparing answers for an annual risk assessment that is required for compliance purposes. Which of the following would be an example of an internal threat?",
        "options": [
            "An approved vendor with on-site offices",
            "An infected client that pulls reports from the firm",
            "A malicious attacker from within the same country",
            "A malicious attacker attempting to socially engineer access into corporate offices"
        ],
        "correct_answer": 3,
        "description": "The correct answer is a malicious attacker from within the same country. An internal threat refers to an individual or entity inside the organization or with authorized access attempting to exploit or harm the company. \n\n- An approved vendor with on-site offices is a trusted third party, not an internal threat. \n- An infected client pulling reports may be an external threat if the client is compromised, not an internal one. \n- A malicious attacker attempting to socially engineer access could be an external threat, depending on the situation."
    },
    {
        "question": "Classification using labels according to information sensitivity and impact in case of unauthorized access or leakage is a mandatory component of:",
        "options": [
            "An acceptable use policy",
            "A memorandum of understanding",
            "Data loss prevention",
            "A non-disclosure agreement"
        ],
        "correct_answer": 3,
        "description": "The correct answer is data loss prevention (DLP). DLP systems are used to classify and protect sensitive data based on its importance and risk, and they help prevent unauthorized access or leakage. \n\n- An acceptable use policy defines the rules for using company resources but does not address data classification directly. \n- A memorandum of understanding outlines the terms of an agreement but does not classify data. \n- A non-disclosure agreement is used to protect confidential information between parties but does not involve data classification or loss prevention."
    },


    #351-400

    
    {
        "question": "A technician is trying to install a VoIP phone, but the phone is not turning on. The technician checks the cable going from the phone to the switch, and the cable is good. Which of the following actions is needed for this phone to work?",
        "options": [
            "Add a PoE injector.",
            "Enable MDIX.",
            "Use a crossover cable.",
            "Reconfigure the port."
        ],
        "correct_answer": 1,
        "description": "The correct answer is to add a PoE injector. VoIP phones require Power over Ethernet (PoE) to function properly, and if the phone is not turning on despite a good cable, it likely lacks the necessary power supply. \n\n- MDIX (Medium Dependent Interface Crossover) deals with cable orientation and is not related to power supply issues. \n- A crossover cable is used for connecting similar devices, but it will not solve the power issue. \n- Reconfiguring the port is unlikely to resolve power-related problems."
    },
    {
        "question": "Which of the following is MOST appropriate for enforcing bandwidth limits when the performance of an application is not affected by the use of buffering but is heavily impacted by packet drops?",
        "options": [
            "Traffic shaping",
            "Traffic policing",
            "Traffic marking",
            "Traffic classification"
        ],
        "correct_answer": 2,
        "description": "The correct answer is traffic policing. Traffic policing is used to enforce bandwidth limits and drop packets that exceed the set limits, which helps prevent packet loss that impacts application performance. \n\n- Traffic shaping is used to smooth out traffic bursts, not enforce strict bandwidth limits. \n- Traffic marking involves tagging packets for QoS, but it does not limit bandwidth. \n- Traffic classification helps prioritize traffic but does not enforce limits."
    },
    {
        "question": "A client utilizes mobile tablets to view high-resolution images and videos via Wi-Fi within a corporate office building. The previous administrator installed multiple high-density APs with Wi-Fi 5, providing maximum coverage, but the measured performance is still below expected levels. Which of the following would provide the BEST solution?",
        "options": [
            "Channel bonding",
            "EIRP power settings",
            "Antenna polarization",
            "A directional antenna"
        ],
        "correct_answer": 1,
        "description": "The correct answer is channel bonding. Channel bonding allows more bandwidth to be used by combining adjacent channels, which is essential in high-density areas with high traffic. \n\n- EIRP power settings control signal strength but are less likely to resolve performance issues in dense environments. \n- Antenna polarization and directional antennas are useful for specific areas but would not provide the best solution for a general office setting with multiple users."
    },
    {
        "question": "A network technician is troubleshooting a new web server connectivity issue. The network technician discovers the following on the support ticket:\n\n• The server’s IP address can be pinged from the client PCs.\n• Access to the web resource works correctly when on the server's console.\n• No clients can access the server’s data via URL.\n• The server does not have a firewall configured.\n• No ACLs are preventing connectivity from the client's network.\n• All services on the server are operating normally, which was confirmed by the server team.\n\nWhich of the following actions will resolve the issue?",
        "options": [
            "Reset port security on the switchport connecting the server.",
            "Adjust the web server's NTP setting to match the client settings.",
            "Configure A records for the web server.",
            "Install the correct MIB on the web server."
        ],
        "correct_answer": 3,
        "description": "The correct answer is to configure A records for the web server. The issue likely stems from the clients not being able to resolve the server's domain name. Configuring the correct A records will allow clients to connect via the URL. \n\n- Resetting port security could cause disruptions but is not the likely cause here since IP pings are successful. \n- NTP (Network Time Protocol) adjustments are unnecessary as the server is already accessible from its console. \n- Installing the correct MIB (Management Information Base) is unnecessary for connectivity issues."
    },
    {
        "question": "Which of the following layers of the OSI model has new protocols activated when a user moves from a wireless to a wired connection?",
        "options": [
            "Data link",
            "Network",
            "Transport",
            "Session"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Data link. When switching from wireless to wired, the data link layer (Layer 2) is responsible for initializing and managing the new connection. It handles the hardware addressing (MAC addresses) and manages data framing for communication. \n\n- The network layer (Layer 3) manages routing, not the specifics of connection type. \n- The transport layer (Layer 4) handles end-to-end communication, but it doesn't directly relate to the switch from wireless to wired. \n- The session layer (Layer 5) manages session initiation and termination, not physical connections."
    },
    {
        "question": "A technician is assisting a user who cannot connect to a website. The technician attempts to ping the default gateway and DNS server of the workstation. According to troubleshooting methodology, this is an example of:",
        "options": [
            "a divide-and-conquer approach.",
            "a bottom-up approach.",
            "a top-to-bottom approach.",
            "implementing a solution."
        ],
        "correct_answer": 3,
        "description": "The correct answer is a top-to-bottom approach. In the OSI model, this troubleshooting approach starts from the network layer and moves down to the physical layer, checking basic connectivity like the gateway and DNS server. \n\n- A divide-and-conquer approach splits the problem into smaller sections and tackles each individually, which doesn't match the scenario. \n- The bottom-up approach starts with the physical layer and moves up, which is the opposite of the approach taken here."
    },
    {
        "question": "Which of the following is the NEXT step to perform network troubleshooting after identifying an issue?",
        "options": [
            "Implement a solution.",
            "Establish a theory.",
            "Escalate the issue.",
            "Document the findings."
        ],
        "correct_answer": 3,
        "description": "The correct answer is escalate the issue. After identifying the issue, the next step in troubleshooting is to escalate if necessary, especially if the solution is beyond the technician's scope or expertise. \n\n- Implementing a solution comes after further investigation or escalation. \n- Establishing a theory is an earlier troubleshooting step. \n- Documenting findings is part of closing the issue after resolution."
    },
    {
        "question": "A network team is getting reports that air conditioning is out in an IDF. The team would like to determine whether additional network issues are occurring. Which of the following should the network team do?",
        "options": [
            "Confirm that memory usage on the network devices in the IDF is normal.",
            "Access network baseline data for references to an air conditioning issue.",
            "Verify severity levels on the corporate syslog server.",
            "Check for SNMP traps from a network device in the IDF.",
            "Review interface statistics looking for cyclic redundancy errors."
        ],
        "correct_answer": 2,
        "description": "The correct answer is to access network baseline data for references to an air conditioning issue. By comparing current performance against baseline data, the team can determine if environmental issues (like air conditioning failure) are causing network problems. \n\n- Memory usage is less likely to be directly impacted by air conditioning problems. \n- Severity levels on the syslog server might help with general troubleshooting but won't directly address environmental factors. \n- SNMP traps and interface statistics may show signs of issues but aren't directly related to air conditioning problems."
    },
    {
        "question": "Which of the following is the MOST cost-effective alternative that provides proper cabling and supports gigabit Ethernet devices?",
        "options": [
            "Twisted cable with a minimum Cat 5e certification",
            "Multimode fiber with an SC connector",
            "Twinaxial cabling using an F-type connector",
            "Cable termination using TIA/EIA-568-B"
        ],
        "correct_answer": 1,
        "description": "The correct answer is twisted cable with a minimum Cat 5e certification. Cat 5e cables are cost-effective and can handle gigabit Ethernet speeds, making them the most suitable choice for this scenario. \n\n- Multimode fiber and Twinaxial cabling are more expensive and typically used for specific high-speed or long-distance applications. \n- Cable termination standards like TIA/EIA-568-B are important but do not determine the most cost-effective solution for gigabit Ethernet."
    },
    {
        "question": "A technician is installing the Wi-Fi infrastructure for legacy industrial machinery at a warehouse. The equipment only supports 802.11a and 802.11b standards. Speed of transmission is the top business requirement. Which of the following is the correct maximum speed for this scenario?",
        "options": [
            "11Mbps",
            "54Mbps",
            "128Mbps",
            "144Mbps"
        ],
        "correct_answer": 2,
        "description": "The correct answer is 54Mbps. Both 802.11a and 802.11b standards support a maximum speed of 54Mbps, making this the highest speed available for the legacy equipment. \n\n- 802.11b supports a maximum speed of 11Mbps, and 802.11a supports up to 54Mbps. \n- 128Mbps and 144Mbps are speeds supported by later Wi-Fi standards (802.11g, 802.11n), but not by 802.11a or 802.11b."
    },


    {
        "question": "Which of the following would be the BEST choice to connect branch sites to a main office securely?",
        "options": [
            "VPN headend",
            "Proxy server",
            "Bridge",
            "Load balancer"
        ],
        "correct_answer": 1,
        "description": "The correct answer is VPN headend. A VPN headend is responsible for managing secure connections between remote branch offices and a central network, ensuring the privacy and integrity of data during transmission. \n\n- Proxy servers are used for filtering content, not establishing secure connections. \n- Bridges are used for connecting network segments and do not provide security for remote connections. \n- Load balancers distribute traffic across servers but do not establish secure connections."
    },
    {
        "question": "Due to concerns around single points of failure, a company decided to add an additional WAN to the network. The company added a second MPLS vendor to the current MPLS WAN and deployed an additional WAN router at each site. Both MPLS providers use OSPF on the WAN network, and EIGRP is run internally. The first site to go live with the new WAN is successful, but when the second site is activated significant network issues occur. Which of the following is the MOST likely cause for the WAN instability?",
        "options": [
            "A CDP neighbor has changed",
            "Asymmetrical routing",
            "A switching loop",
            "An incorrect IP address"
        ],
        "correct_answer": 2,
        "description": "The correct answer is Asymmetrical routing. Asymmetrical routing occurs when data packets take different paths from source to destination and back, causing inconsistencies in the traffic flow and resulting in network instability. \n\n- A CDP neighbor change might cause updates in routing information but is less likely to cause overall WAN instability. \n- A switching loop could cause network congestion, but it is typically a problem within the LAN rather than with WAN routers. \n- An incorrect IP address would prevent communication but would not typically result in widespread network instability."
    },
    {
        "question": "During the troubleshooting of an E1 line, the point-to-point link on the core router was accidentally unplugged and left unconnected for several hours. However, the network management team was not notified. Which of the following could have been configured to allow early detection and possible resolution of the issue?",
        "options": [
            "Traps",
            "MIB",
            "OID",
            "Baselines"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Traps. SNMP traps are configured to notify administrators immediately when a specific event, such as a device failure, occurs. This would have allowed the network team to detect the unplugged link quickly. \n\n- MIB (Management Information Base) is used to define what information can be monitored, but it doesn't actively notify about issues. \n- OID (Object Identifier) is used to identify specific variables within the MIB but is not responsible for notifications. \n- Baselines are used for performance measurement and comparison, not for immediate issue detection."
    },
    {
        "question": "Which of the following layers of the OSI model receives data from the application layer and converts it into syntax that is readable by other devices on the network?",
        "options": [
            "Layer 1",
            "Layer 3",
            "Layer 6",
            "Layer 7"
        ],
        "correct_answer": 3,
        "description": "The correct answer is Layer 6. Layer 6, the Presentation Layer, is responsible for converting data from the application layer into a format that other devices can understand, often involving encryption, compression, or translation. \n\n- Layer 1 (Physical Layer) deals with the transmission of raw data bits over a physical medium. \n- Layer 3 (Network Layer) is responsible for routing data between devices but does not convert data formats. \n- Layer 7 (Application Layer) is the top layer and provides services directly to end-users, but it does not convert data for network communication."
    },
    {
        "question": "Which of the following topologies is designed to fully support applications hosted in on-premises data centers, public or private clouds, and SaaS services?",
        "options": [
            "SDWAN",
            "MAN",
            "PAN",
            "MPLS"
        ],
        "correct_answer": 1,
        "description": "The correct answer is SDWAN. SDWAN (Software-Defined Wide Area Network) is designed to provide flexible, secure, and efficient connections between on-premises, cloud, and SaaS environments, allowing for optimal performance across diverse network topologies. \n\n- MAN (Metropolitan Area Network) is designed for citywide connectivity, not specifically for integrating cloud services. \n- PAN (Personal Area Network) is used for short-range communications and would not support enterprise-scale applications. \n- MPLS (Multiprotocol Label Switching) is used for managing traffic flow but lacks the flexibility and cloud integration capabilities of SDWAN."
    },
    {
        "question": "A Chief Executive Officer and a network administrator came to an agreement with a vendor to purchase new equipment for the data center. A document was drafted so all parties would be informed about the scope of the project before it started. Which of the following terms BEST describes the document used?",
        "options": [
            "Contract",
            "Project charter",
            "Memorandum of understanding",
            "Non-disclosure agreement"
        ],
        "correct_answer": 2,
        "description": "The correct answer is Project charter. A project charter is a formal document that outlines the scope, objectives, and stakeholders of a project, ensuring all parties understand their roles and responsibilities before work begins. \n\n- A contract is a legally binding agreement but focuses on the terms of the agreement rather than project scope. \n- A Memorandum of Understanding (MOU) is typically used for informal agreements and may not provide the level of detail found in a project charter. \n- A Non-disclosure agreement (NDA) protects confidential information but does not define project scope."
    },
    {
        "question": "ARP spoofing would normally be a part of:",
        "options": [
            "an on-path attack",
            "DNS poisoning",
            "a DoS attack",
            "a rogue access point"
        ],
        "correct_answer": 1,
        "description": "The correct answer is an on-path attack. ARP spoofing is used in on-path attacks (formerly known as man-in-the-middle attacks) where the attacker impersonates a legitimate device on the network by sending fake ARP messages, allowing them to intercept or modify traffic. \n\n- DNS poisoning is a different attack where fake DNS records are used to redirect traffic but is not related to ARP spoofing. \n- A DoS attack (Denial of Service) aims to overwhelm a system or network with traffic, not to manipulate traffic. \n- A rogue access point refers to an unauthorized Wi-Fi device on a network, not a method of manipulating ARP."
    },
    {
        "question": "A corporation is looking for a method to secure all traffic between a branch office and its data center in order to provide a zero-touch experience for all staff members who work there. Which of the following would BEST meet this requirement?",
        "options": [
            "Site-to-site VPN",
            "VNC",
            "Remote desktop gateway",
            "Virtual LANs"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Site-to-site VPN. A Site-to-site VPN provides secure communication between a branch office and the data center, ensuring that all traffic is encrypted and protected without requiring individual staff interaction. \n\n- VNC (Virtual Network Computing) and Remote desktop gateway are used for remote desktop access, not securing traffic between sites. \n- Virtual LANs (VLANs) are used to segment a network but do not provide security between geographically separated sites."
    },
    {
        "question": "A company cell phone was stolen from a technician's vehicle. The cell phone has a passcode, but it contains sensitive information about clients and vendors. Which of the following should also be enabled?",
        "options": [
            "Factory reset",
            "Autolock",
            "Encryption",
            "Two-factor authentication"
        ],
        "correct_answer": 3,
        "description": "The correct answer is Encryption. Encryption protects sensitive data by making it unreadable to unauthorized users, even if the device is lost or stolen. \n\n- A factory reset would erase data but would not protect it if the device is accessed before reset. \n- Autolock is a security feature that locks the device after inactivity but does not protect the data itself. \n- Two-factor authentication is essential for access control but would not protect data on a stolen device."
    },
    {
        "question": "An organization is interested in purchasing a backup solution that supports the organization's goals. Which of the following concepts would specify the maximum duration that a given service can be down before impacting operations?",
        "options": [
            "MTTR",
            "RTO",
            "MTBF",
            "RPO"
        ],
        "correct_answer": 2,
        "description": "The correct answer is RTO (Recovery Time Objective). RTO specifies the maximum acceptable downtime for a service, ensuring that operations can resume within an acceptable timeframe to avoid significant impact. \n\n- MTTR (Mean Time to Repair) measures the time required to fix a service after failure but does not specify the downtime tolerance. \n- MTBF (Mean Time Between Failures) is a reliability metric and does not address acceptable downtime. \n- RPO (Recovery Point Objective) focuses on the amount of data loss that can be tolerated, not downtime."
    },




    {
        "question": "During an annual review of policy documents, a company decided to adjust its recovery time frames. The company agreed that critical applications can be down for no more than six hours, and the acceptable amount of data loss is no more than two hours. Which of the following should be documented as the RPO?",
        "options": [
            "Two hours",
            "Four hours",
            "Six hours",
            "Eight hours"
        ],
        "correct_answer": 1,
        "description": "The correct answer is two hours. The Recovery Point Objective (RPO) represents the maximum acceptable amount of data loss, which in this case is no more than two hours. \n\n- Six hours refers to the maximum allowable downtime, which is part of the Recovery Time Objective (RTO), not the RPO. \n- Four hours and eight hours are not relevant since the data loss must be capped at two hours."
    },
    {
        "question": "A network administrator is given the network 80.87.78.0/26 for specific device assignments. Which of the following describes this network?",
        "options": [
            "80.87.78.0 - 80.87.78.14",
            "80.87.78.0 - 80.87.78.110",
            "80.87.78.1 - 80.87.78.62",
            "80.87.78.1 - 80.87.78.158"
        ],
        "correct_answer": 3,
        "description": "The correct answer is 80.87.78.1 - 80.87.78.62. A /26 subnet has 64 IP addresses (including network and broadcast addresses), and the valid host range begins from 80.87.78.1 to 80.87.78.62. \n\n- 80.87.78.0 - 80.87.78.14 and 80.87.78.0 - 80.87.78.110 are incorrect because they do not correctly reflect the range of valid IP addresses for a /26 subnet. \n- 80.87.78.1 - 80.87.78.158 exceeds the valid host range for a /26 subnet."
    },
    {
        "question": "An organization set up its offices so that a desktop is connected to the network through a VoIP phone. The VoIP vendor requested that voice traffic be segmented separately from non-voice traffic. Which of the following would allow the organization to configure multiple devices with network isolation on a single switch port?",
        "options": [
            "Subinterfaces",
            "Link aggregation",
            "Load balancing",
            "Tunneling"
        ],
        "correct_answer": 1,
        "description": "The correct answer is subinterfaces. Subinterfaces allow multiple virtual LANs (VLANs) to be configured on a single physical switch port, enabling network traffic segmentation. \n\n- Link aggregation involves combining multiple physical links into one logical connection but does not isolate traffic types. \n- Load balancing and tunneling are unrelated to segmenting traffic on a switch port."
    },
    {
        "question": "An attacker targeting a large company was able to inject malicious A records into internal name resolution servers. Which of the following attack types was MOST likely used?",
        "options": [
            "DNS poisoning",
            "On-path",
            "IP spoofing",
            "Rogue DHCP"
        ],
        "correct_answer": 1,
        "description": "The correct answer is DNS poisoning. This attack type involves inserting malicious DNS records into a DNS server, redirecting traffic to malicious destinations. \n\n- On-path attacks involve intercepting or altering communications but do not specifically target DNS records. \n- IP spoofing involves falsifying IP addresses but is unrelated to DNS record manipulation. \n- Rogue DHCP involves unauthorized DHCP servers, not DNS poisoning."
    },
    {
        "question": "The following DHCP scope was configured for a new VLAN dedicated to a large deployment of 325 IoT sensors:\n\nDHCP network scope: 10.10.0.0/24\nExclusion range: 10.10.10.1-10.10.10.10\nGateway: 10.10.10.1\nDNS: 10.10.10.2\nDHCP option 66(TFTP): 10.10.10.4\nDHCP option 4(NTP): 10.10.10.6\n\nThe first 244 IoT sensors were able to connect to the TFTP server, download the configuration file, and register to an IoT management system. The other sensors are being shown as offline. Which of the following should be performed to determine the MOST likely cause of the partial deployment of the sensors?",
        "options": [
            "Check the gateway connectivity to the TFTP server.",
            "Check the DHCP network scope.",
            "Check whether the NTP server is online.",
            "Check the IoT devices for a hardware failure."
        ],
        "correct_answer": 2,
        "description": "The correct answer is check the DHCP network scope. Since only a portion of the IoT devices are connecting successfully, it suggests a DHCP scope issue, possibly running out of available IP addresses for the remaining devices. \n\n- Checking the gateway, NTP server, or IoT devices for hardware failure is not the most logical first step since the problem seems to be related to IP address assignment."
    },
    {
        "question": "A network technician receives a report from the server team that a server's network connection is not working correctly. The server team confirms the server is operating correctly except for the network connection. The technician checks the switchport connected to the server and reviews the following data:\n\nMetric Value\nBytes input 441, 164, 698\nBytes output 2, 625, 115, 257\nRunts 0\nCRC's 5,489\nCollisions 1\nMDIX On\nSpeed 1,000\nDuplex Full\n\nWhich of the following should the network technician perform to correct the issue?",
        "options": [
            "Replace the Cat 5 patch cable with a Cat 6 cable.",
            "Install a crossover cable between the server and the switch.",
            "Reset the switchport configuration.",
            "Use NetFlow data from the switch to isolate the issue.",
            "Disable MDIX on the switchport and reboot the server."
        ],
        "correct_answer": 3,
        "description": "The correct answer is reset the switchport configuration. The high number of CRC errors suggests there may be an issue with the switchport configuration, likely caused by an incorrect setting or mismatch. Resetting the configuration can resolve this. \n\n- Replacing the patch cable or installing a crossover cable may not resolve the issue, as the physical link seems fine. \n- NetFlow data may help with troubleshooting but is not the immediate solution. \n- Disabling MDIX is not necessary since the port is operating in the correct MDIX mode."
    },
    {
        "question": "Which of the following would be BEST to install to find and block any malicious users within a network?",
        "options": [
            "IDS",
            "IPS",
            "SCADA",
            "ICS"
        ],
        "correct_answer": 2,
        "description": "The correct answer is IPS (Intrusion Prevention System). An IPS actively monitors and blocks malicious network traffic in real time, offering better protection than an IDS (Intrusion Detection System) which only detects threats. \n\n- SCADA and ICS are systems related to industrial control and automation, not security."
    },
    {
        "question": "Which of the following can be used to validate domain ownership by verifying the presence of pre-agreed content contained in a DNS record?",
        "options": [
            "SOA",
            "SRV",
            "AAA",
            "TXT"
        ],
        "correct_answer": 4,
        "description": "The correct answer is TXT. A TXT record in DNS is used to store arbitrary text, and it can be used for domain ownership validation by verifying the presence of specific content. \n\n- SOA, SRV, and AAA records are used for different purposes like defining authoritative DNS servers, service records, and authentication, but they do not support domain ownership verification."
    },
    {
        "question": "Network traffic is being compromised by DNS poisoning every time a company's router is connected to the internet. The network team detects a non-authorized DNS server being assigned to the network clients and remediates the incident by setting a trusted DNS server, but the issue occurs again after internet exposure. Which of the following best practices should be implemented on the router?",
        "options": [
            "Change the device's default password.",
            "Disable router advertisement guard.",
            "Activate control plane policing.",
            "Disable unneeded network services."
        ],
        "correct_answer": 4,
        "description": "The correct answer is disable unneeded network services. Disabling unnecessary services on the router will reduce its exposure to attacks, such as DNS poisoning. \n\n- Changing the default password is important but does not directly prevent DNS poisoning. \n- Router advertisement guard and control plane policing are useful for other attacks but not directly for mitigating DNS poisoning."
    },
    {
        "question": "A network administrator installed a new data and VoIP network. Users are now experiencing poor call quality when making calls. Which of the following should the administrator do to increase VoIP performance?",
        "options": [
            "Configure a voice VLAN.",
            "Configure LACP on all VoIP phones.",
            "Configure PoE on the network.",
            "Configure jumbo frames on the network."
        ],
        "correct_answer": 1,
        "description": "The correct answer is configure a voice VLAN. A dedicated voice VLAN helps prioritize VoIP traffic and reduces latency, improving call quality. \n\n- LACP, PoE, and jumbo frames do not specifically address VoIP performance or call quality."
    },




    {
        "question": "A Wi-Fi network was originally configured to be able to handle interference from a microwave oven. The microwave oven was recently removed from the office. Now the network administrator wants to optimize the system to maximize the range of the signal. The main sources of signal degradation are the numerous cubicles and wooden walls between the WAP and the intended destination. Which of the following actions should the administrator take?",
        "options": [
            "Implement CDMA.",
            "Change from omni to directional.",
            "Change the SSID.",
            "Change the frequency."
        ],
        "correct_answer": 2,
        "description": "The correct answer is to change from omni to directional antennas. Directional antennas focus the signal in a specific direction, which helps overcome obstacles like cubicles and wooden walls, improving the range of the Wi-Fi network. \n\n- CDMA is used in cellular networks and is not relevant to Wi-Fi optimization. \n- Changing the SSID only changes the network's name and does not affect range. \n- Changing the frequency may help with interference but is less effective for overcoming physical obstructions compared to using directional antennas."
    },
    {
        "question": "Which of the following issues are present with RIPv2? (Choose two.)",
        "options": [
            "Route poisoning",
            "Time to converge",
            "Scalability",
            "Unicast",
            "Adjacent neighbors",
            "Maximum transmission unit"
        ],
        "correct_answer": [2, 3],
        "description": "The correct answers are scalability and time to converge. RIPv2 has limitations in terms of scalability because it uses hop count as its metric, which becomes inefficient in larger networks. It also has a slow convergence time, meaning it takes longer to detect network changes and stabilize. \n\n- Route poisoning is a technique used to prevent routing loops but is not a problem with RIPv2. \n- Unicast, adjacent neighbors, and maximum transmission unit (MTU) are not specific issues with RIPv2."
    },
    {
        "question": "Which of the following protocols can be used to change device configurations via encrypted and authenticated sessions? (Choose two.)",
        "options": [
            "SNMPv3",
            "SSH",
            "Telnet",
            "IPSec",
            "ESP",
            "Syslog"
        ],
        "correct_answer": [1, 2],
        "description": "The correct answers are SNMPv3 and SSH. SNMPv3 provides encryption and authentication for network device management, and SSH is used for secure remote administration of devices, both ensuring secure and authenticated sessions. \n\n- Telnet does not provide encryption and is insecure. \n- IPSec and ESP are security protocols used for encrypting traffic, but they are not specifically for managing device configurations. \n- Syslog is used for logging and monitoring but does not change device configurations."
    },
    {
        "question": "An administrator wants to increase the availability of a server that is connected to the office network. Which of the following allows for multiple NICs to share a single IP address and offers maximum performance while providing fault tolerance in the event of a NIC failure?",
        "options": [
            "Multipathing",
            "Spanning Tree Protocol",
            "First Hop Redundancy Protocol",
            "Elasticity"
        ],
        "correct_answer": 1,
        "description": "The correct answer is multipathing. Multipathing allows multiple network interface cards (NICs) to work together to share a single IP address, providing both performance improvements and fault tolerance. If one NIC fails, the traffic can be rerouted through another NIC. \n\n- Spanning Tree Protocol is used to prevent network loops in switches, not for NIC redundancy. \n- First Hop Redundancy Protocol ensures availability of the default gateway, but does not manage NICs. \n- Elasticity refers to the ability of a system to scale resources dynamically, but it is not related to NIC redundancy."
    },
    {
        "question": "A network administrator has received calls every day for the past few weeks from three users who cannot access the network. The administrator asks all the users to reboot their PCs, but the same users still cannot access the system. The following day, three different users report the same issue, and the administrator asks them all to reboot their PCs; however, this does not fix the issue. Which of the following is MOST likely occurring?",
        "options": [
            "Incorrect firewall settings",
            "Inappropriate VLAN assignment",
            "Hardware failure",
            "Overloaded CAM table in switch",
            "DHCP scope exhaustion"
        ],
        "correct_answer": 5,
        "description": "The correct answer is DHCP scope exhaustion. If the DHCP scope is exhausted, new devices will be unable to obtain an IP address, preventing them from accessing the network. \n\n- Incorrect firewall settings typically affect specific users or applications but would not affect multiple users across different days. \n- Inappropriate VLAN assignment may cause network issues but typically affects users who should not be in the same VLAN. \n- Hardware failure usually causes broader issues, such as no network connectivity at all, not just for a specific set of users. \n- An overloaded CAM table can cause issues with switch performance but is not as likely as DHCP exhaustion in this scenario."
    },
    {
        "question": "A network technician recently installed 35 additional workstations. After installation, some users are unable to access network resources. Many of the original workstations that are experiencing the network access issue were offline when the new workstations were turned on. Which of the following is the MOST likely cause of this issue?",
        "options": [
            "Incorrect VLAN setting",
            "Insufficient DHCP scope",
            "Improper NIC setting",
            "Duplicate IP address"
        ],
        "correct_answer": 4,
        "description": "The correct answer is duplicate IP address. When multiple devices share the same IP address, it causes network conflicts, resulting in some devices being unable to access network resources. The fact that some of the original workstations were offline when the new workstations were powered on suggests an IP address conflict. \n\n- Incorrect VLAN setting would affect network segmentation, but it wouldn't typically cause IP conflicts. \n- Insufficient DHCP scope would prevent devices from obtaining IP addresses but would not cause a conflict. \n- Improper NIC setting may cause connectivity issues but is less likely than a duplicate IP."
    },
    {
        "question": "A WAN technician reviews activity and identifies newly installed hardware that is causing outages over an eight-hour period. Which of the following should be considered FIRST?",
        "options": [
            "Network performance baselines",
            "VLAN assignments",
            "Routing table",
            "Device configuration review"
        ],
        "correct_answer": 4,
        "description": "The correct answer is device configuration review. The newly installed hardware could be misconfigured, which may lead to network outages. A thorough review of the device's configuration is the first step to identify potential issues. \n\n- Network performance baselines are important for comparison, but reviewing the device configuration is the most direct action. \n- VLAN assignments and routing tables may be factors, but reviewing the device configuration should come first."
    },
    {
        "question": "Which of the following would enable a network technician to implement dynamic routing?",
        "options": [
            "An IPS",
            "A bridge",
            "A Layer 3 switch",
            "A hub"
        ],
        "correct_answer": 3,
        "description": "The correct answer is a Layer 3 switch. A Layer 3 switch operates at the network layer and supports dynamic routing protocols, allowing for efficient routing decisions in large networks. \n\n- An IPS (Intrusion Prevention System) is used for security, not routing. \n- A bridge operates at Layer 2 and does not support dynamic routing. \n- A hub is a basic device that does not support routing or Layer 3 functionality."
    },
    {
        "question": "Which of the following would be BEST suited for a long cable run with a 40Gbps bandwidth?",
        "options": [
            "Cat 5e",
            "Cat 6a",
            "Cat 7",
            "Cat 8"
        ],
        "correct_answer": 4,
        "description": "The correct answer is Cat 8. Cat 8 cables are designed for high-speed data transmission up to 40Gbps over short distances (up to 30 meters). This makes them ideal for long cable runs with high bandwidth demands. \n\n- Cat 5e and Cat 6a are suitable for lower bandwidths (up to 1Gbps and 10Gbps, respectively) and are not capable of handling 40Gbps. \n- Cat 7 is a high-performance cable but does not support 40Gbps bandwidth over long distances as effectively as Cat 8."
    },
{
    "question": "A network administrator is investigating a network event that is causing all communication to stop. The network administrator is unable to use SSH to connect to the switch but is able to gain access using the serial console port. While monitoring port statistics, the administrator sees the following:\n\nMetric                        | Value            | Metric                    | Value\n--------------------------------|------------------|---------------------------|-----------------\nTotal Rx (bps)                 | 23,041,464       | Total Tx (bps)            | 621,032\nUnicast Rx (Pkts/sec)          | 102,465          | Unicast Tx (Pkts/sec)     | 66\nB/Mcast Rx (Pkts/sec)          | 21,456,465       | B/Mcast Tx (Pkts/sec)     | 7\nUtilization Rx                 | 2.3%             | Utilization Tx            | 0.06%\n\nWhich of the following is MOST likely causing the network outage?",
    "options": [
        "Duplicate IP address",
        "High collisions",
        "Asynchronous route",
        "Switch loop"
    ],
    "correct_answer": 4,
    "description": "The correct answer is Switch loop. The statistics show a high number of broadcast/multicast packets (21,456,465 received vs. only 7 transmitted), which is characteristic of a switch loop. In a switch loop, broadcast packets continuously circulate through the network, overwhelming resources and causing a network outage. \n\n- A duplicate IP address would cause network issues but would not generate high numbers of broadcast packets.\n- High collisions would affect data transmission but wouldn't produce the high number of broadcast packets shown here.\n- An asynchronous route is unrelated to broadcast traffic and would typically cause routing issues rather than a complete communication failure."
},



  {
    "question": "Which of the following is a valid and cost-effective solution to connect a fiber cable into a network switch without available SFP ports?",
    "options": [
      "Use a media converter and a UTP cable",
      "Install an additional transceiver module and use GBICs",
      "Change the type of connector from SC to F-type",
      "Use a loopback adapter to make the connection"
    ],
    "correct_answer": 1,
    "description": "The correct answer is 'Use a media converter and a UTP cable'. A media converter can be used to connect fiber to copper or other types of cabling, allowing flexibility in connecting devices that lack SFP ports. \n\n- Installing a transceiver module and using GBICs can be costly and unnecessary if a media converter is available. \n- Changing the type of connector from SC to F-type is unrelated to fiber network connections and does not solve the issue. \n- A loopback adapter would not provide the correct connection method for fiber optic cables, as it is typically used for network testing purposes."
  },
  {
    "question": "A network device needs to discover a server that can provide it with an IPv4 address. Which of the following does the device need to send the request to?",
    "options": [
      "Default gateway",
      "Broadcast address",
      "Unicast address",
      "Link local address"
    ],
    "correct_answer": 2,
    "description": "The correct answer is 'Broadcast address'. When a device needs to discover a server (typically a DHCP server) for an IPv4 address, it sends a broadcast request because it does not yet have an IP address to target a specific server. \n\n- The default gateway is used for routing traffic outside the local subnet, not for discovering an IPv4 address. \n- A unicast address is used for sending data to a specific device with a known address, not for initial network discovery. \n- A link-local address is used for communication within the local network but is not used for discovering a DHCP server."
  },
  {
    "question": "Which of the following is an example of on-demand scalable hardware that is typically housed in the vendor's data center?",
    "options": [
      "DaaS",
      "IaaS",
      "PaaS",
      "SaaS"
    ],
    "correct_answer": 2,
    "description": "The correct answer is 'IaaS' (Infrastructure as a Service). IaaS provides on-demand scalable hardware resources such as servers, storage, and networking, all hosted in the vendor's data center. \n\n- DaaS (Desktop as a Service) is a cloud computing service offering virtual desktops but does not focus on scalable hardware. \n- PaaS (Platform as a Service) provides development platforms but is not focused on hardware. \n- SaaS (Software as a Service) provides software applications over the internet and is not related to hardware scalability."
  },
  {
    "question": "A network security engineer locates an unapproved wireless bridge connected to the corporate LAN that is broadcasting a hidden SSID, providing unauthenticated access to internal resources. Which of the following types of attacks BEST describes this finding?",
    "options": [
      "Rogue access point",
      "Evil twin",
      "ARP spoofing",
      "VLAN hopping"
    ],
    "correct_answer": 1,
    "description": "The correct answer is 'Rogue access point'. A rogue access point is an unauthorized device connected to the network, potentially compromising network security by allowing unauthenticated access. \n\n- An evil twin is a type of rogue access point that mimics a legitimate one to deceive users into connecting to it. \n- ARP spoofing is a technique used to intercept network traffic but does not describe this particular situation. \n- VLAN hopping involves unauthorized access to different VLANs but does not directly apply to this case of rogue access."
  },
  {
    "question": "While setting up a new workstation, a technician discovers that the network connection is only 100 full duplex (FD), although it is connected to a gigabit switch. While reviewing the interface information in the switch CLI, the technician notes the port is operating at 100FD but shows many RX and TX errors. The technician moves the computer to another switchport and experiences the same issues. Which of the following is MOST likely the cause of the low data rate and port errors?",
    "options": [
      "Bad switchports",
      "Faulty drivers",
      "Cable length",
      "Incorrect pin-out"
    ],
    "correct_answer": 4,
    "description": "The correct answer is 'Incorrect pin-out'. The incorrect wiring of the Ethernet cable or misconfiguration of the cable's pin-out can cause issues like low data rates and errors, even when connected to a gigabit switch. \n\n- Bad switchports could lead to issues, but the problem persists on different ports, suggesting it's not a switch issue. \n- Faulty drivers may affect network performance but are less likely to cause consistent RX and TX errors on multiple switch ports. \n- Cable length could cause performance issues, but it's more likely a pin-out issue if the problem is occurring consistently across different switchports."
  },
  {
    "question": "A technician is contracted to install a redundant cluster of devices from the ISP in case of hardware failure within the network. Which of the following would provide BEST redundant solution in Layer 2 devices?",
    "options": [
      "Multiple routers",
      "Multiple switches",
      "Multiple firewalls",
      "Multiple bridges"
    ],
    "correct_answer": 2,
    "description": "The correct answer is 'Multiple switches'. Using multiple switches provides redundancy in Layer 2 of the OSI model by ensuring network traffic can continue even if one switch fails. \n\n- Multiple routers would provide redundancy at Layer 3 (network layer) but are not the best solution for Layer 2 redundancy. \n- Multiple firewalls provide redundancy for security but do not directly address Layer 2 redundancy. \n- Multiple bridges are used to extend networks but are less commonly used for redundancy compared to switches."
  },
  {
    "question": "Which of the following documents is MOST likely to be associated with identifying and documenting critical applications?",
    "options": [
      "Software development life-cycle policy",
      "User acceptance testing plan",
      "Change management policy",
      "Business continuity plan"
    ],
    "correct_answer": 4,
    "description": "The correct answer is 'Business continuity plan'. A business continuity plan identifies and documents critical applications and resources required to maintain operations during disruptive events. \n\n- A software development life-cycle policy focuses on the development process of software and is not directly related to identifying critical applications. \n- A user acceptance testing plan is used to validate software before deployment, not to identify critical business applications. \n- A change management policy governs changes to IT systems but does not focus on identifying critical applications."
  },
  {
    "question": "A security vendor needs to add a note to the DNS to validate the ownership of a company domain before services begin. Which of the following records did the security company MOST likely ask the company to configure?",
    "options": [
      "TXT",
      "AAAA",
      "CNAME",
      "SRV"
    ],
    "correct_answer": 1,
    "description": "The correct answer is 'TXT'. A TXT record is often used to store arbitrary text, including validation information for domain ownership, which is commonly required by security vendors. \n\n- AAAA records are used for IPv6 addresses, not for domain validation. \n- CNAME records map one domain name to another but are not used for ownership validation. \n- SRV records are used to define service-related information but are not related to domain validation."
  },
  {
    "question": "A client who shares office space and an IT closet with another company recently reported connectivity issues throughout the network. Multiple third-party vendors regularly perform on-site maintenance in the shared IT closet. Which of the following security techniques would BEST secure the physical networking equipment?",
    "options": [
      "Disabling unneeded switchports",
      "Implementing role-based access",
      "Enable logging",
      "Configuring an access control list"
    ],
    "correct_answer": 2,
    "description": "The correct answer is 'Implementing role-based access'. Role-based access control (RBAC) restricts physical access to networking equipment based on user roles, ensuring only authorized personnel can interact with critical infrastructure. \n\n- Disabling unneeded switchports helps prevent unauthorized network access but does not address physical security. \n- Enabling logging is useful for monitoring access but does not prevent unauthorized physical access. \n- Configuring an access control list (ACL) is related to network security, not physical security."
  },
  {
    "question": "A help desk engineer needs to configure two servers to have the same public IP addresses. Which of the following technologies should the engineer use?",
    "options": [
      "NAT",
      "VIP",
      "DNS caching",
      "RFC 1918",
      "SDWAN"
    ],
    "correct_answer": 2,
    "description": "The correct answer is 'VIP' (Virtual IP). A Virtual IP (VIP) allows multiple servers to share the same public IP address, often used for load balancing or redundancy purposes. \n\n- NAT (Network Address Translation) allows for mapping private IP addresses to public addresses, but it is not designed to have the same public IP address on multiple servers. \n- DNS caching stores DNS query results locally but does not manage IP address configurations. \n- RFC 1918 defines private IP address ranges, but does not directly enable the use of the same public IP address. \n- SDWAN (Software-Defined Wide Area Network) is used for WAN optimization and not for configuring multiple servers with the same IP address."
  }

















]
