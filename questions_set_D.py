questions_set_D = [
# 651-700



    {
        "question": "Which of the following should a junior security administrator recommend implementing to mitigate malicious network activity?",
        "options": [
            "Intrusion prevention system",
            "Load balancer",
            "Access logging",
            "Endpoint encryption"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Intrusion prevention system (IPS). IPS monitors network traffic and can actively block malicious activity, which is crucial for mitigating attacks. \n\n- A load balancer helps distribute traffic but doesn't specifically mitigate malicious network activity. \n- Access logging is important for auditing but doesn't prevent malicious behavior. \n- Endpoint encryption secures data but does not directly prevent network-based attacks."
    },
    {
        "question": "A client wants to increase overall security after a recent breach. Which of the following would be best to implement? (Choose two.)",
        "options": [
            "Least privilege network access",
            "Dynamic inventories",
            "Central policy management",
            "Zero-touch provisioning",
            "Configuration drift prevention",
            "Subnet range limits"
        ],
        "correct_answer": [1, 3],
        "description": "The correct answers are Least privilege network access and Central policy management. \n\n- Least privilege network access limits access to resources, minimizing the potential for damage in case of a breach. \n- Central policy management allows for uniform security configurations across systems, improving overall security. \n\n- Dynamic inventories and Zero-touch provisioning focus on system setup but aren't directly linked to increasing security. \n- Configuration drift prevention maintains consistency but doesn't directly enhance security after a breach. \n- Subnet range limits control traffic but are not as effective as the other options in addressing a breach."
    },
    {
        "question": "Which of the following passwords would provide the best defense against a brute-force attack?",
        "options": [
            "ThisIsMyPasswordForWork",
            "Qwerty!@#$",
            "Password!1",
            "T5!8j5"
        ],
        "correct_answer": 4,
        "description": "The correct answer is T5!8j5. This password is the most complex, combining upper and lowercase letters, numbers, and special characters, making it harder for a brute-force attack to guess. \n\n- 'ThisIsMyPasswordForWork' is easy to guess because it contains common phrases. \n- 'Qwerty!@#$' is a weak password because it follows common keyboard patterns. \n- 'Password!1' is a common password with predictable patterns, making it vulnerable to brute-force attacks."
    },
    {
        "question": "Which of the following is most likely to be implemented to actively mitigate intrusions on a host device?",
        "options": [
            "HIDS",
            "NIDS",
            "HIPS",
            "NIPS"
        ],
        "correct_answer": 3,
        "description": "The correct answer is HIPS (Host Intrusion Prevention System). HIPS actively monitors and protects a host device from malicious activity, providing real-time defense. \n\n- HIDS (Host Intrusion Detection System) detects but does not actively prevent attacks. \n- NIDS and NIPS focus on network-level detection and prevention, not host-level defense."
    },
    {
        "question": "A network administrator wants to know which systems on the network are at risk of a known vulnerability. Which of the following should the administrator reference?",
        "options": [
            "SLA",
            "Patch management policy",
            "NDA",
            "Site survey report",
            "CVE"
        ],
        "correct_answer": 5,
        "description": "The correct answer is CVE (Common Vulnerabilities and Exposures). CVEs provide a publicly available list of known vulnerabilities, helping administrators identify systems at risk. \n\n- SLAs (Service Level Agreements) define service expectations but do not identify vulnerabilities. \n- Patch management policies outline the process for applying patches but do not directly identify vulnerabilities. \n- NDAs (Non-Disclosure Agreements) are for confidentiality, not vulnerabilities. \n- A site survey report might include network topology, but it doesn't provide specific vulnerability information."
    },
    {
        "question": "A network engineer is upgrading an existing edge gateway. The company currently uses a router and needs to be able to filter on all OSI layers. Which of the following should the engineer use to upgrade the gateway?",
        "options": [
            "NGFW",
            "Proxy",
            "Layer 3 switch",
            "Load balancer"
        ],
        "correct_answer": 1,
        "description": "The correct answer is NGFW (Next-Generation Firewall). NGFWs provide advanced filtering and security across all OSI layers, including application-level filtering. \n\n- A proxy can act as a middleman for requests but does not provide full OSI-layer filtering. \n- A Layer 3 switch operates at the network layer and is used for routing, not comprehensive filtering. \n- A load balancer distributes traffic but does not focus on filtering security threats."
    },
    {
        "question": "Which of the following architectures would allow the network-forwarding elements to adapt to new business requirements with the least amount of operating effort?",
        "options": [
            "Software-defined network",
            "Spine and leaf",
            "Three-tier",
            "Backbone"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Software-defined network (SDN). SDNs allow for flexible, centralized control of network forwarding elements, making it easier to adapt to changing business requirements. \n\n- Spine and leaf, three-tier, and backbone architectures are traditional approaches that may require more manual configuration and adjustments as business needs evolve."
    },
    {
        "question": "A customer lost the connection to the telephone system. The administration console is configured with multiple network interfaces and is connected to multiple switches. The network administrator troubleshoots and verifies the following:\n• The support team is able to connect remotely to the administration console.\n• Rebooting the switch shows solid link and activity lights even on unused ports.\n• Rebooting the telephone system does not bring the system back online.\n• The console is able to connect directly to individual modules successfully. Which of the following is the most likely reason the customer lost the connection?",
        "options": [
            "A switch failed.",
            "The console software needs to be reinstalled.",
            "The cables to the modules need to be replaced.",
            "A module failed."
        ],
        "correct_answer": 4,
        "description": "The correct answer is A module failed. Given the troubleshooting steps, the issue seems to be isolated to a specific module rather than the entire system, and the console can connect to individual modules successfully. \n\n- A switch failure would likely affect more than just the telephone system and would impact connectivity to other devices. \n- Reinstalling the console software is unlikely to fix a hardware issue. \n- Replacing cables would typically not resolve an issue where the console can connect to individual modules."
    },
    {
        "question": "A network security technician is designing a solution for a secure remote access scheme with the following requirements:\n• The solution must allow for users at multiple locations to access corporate resources.\n• The on-premises equipment will not handle non-corporate, resource-bound traffic.\nWhich of the following should the network security technician consider when designing the solution? (Choose two.)",
        "options": [
            "Clientless VPN",
            "Personal VPN",
            "Full-tunnel VPN",
            "Client-to-site VPN",
            "Site-to-site VPN",
            "Split-tunnel VPN"
        ],
        "correct_answer": [1, 6],
        "description": "The correct answers are Clientless VPN and Split-tunnel VPN. \n\n- A clientless VPN allows users to access corporate resources without needing a client application, while Split-tunnel VPN allows users to send corporate traffic through the VPN while non-corporate traffic goes directly to the internet. \n\n- Personal VPN and Site-to-site VPN are more appropriate for personal or office-to-office connectivity, not individual remote access. \n- Full-tunnel VPN routes all traffic through the VPN, which isn't necessary in this case."
    },
    {
        "question": "Which of the following uses an automated script to make configuration changes when interacting with a web application?",
        "options": [
            "SSH",
            "FTP",
            "API",
            "GUI"
        ],
        "correct_answer": 3,
        "description": "The correct answer is API. An API (Application Programming Interface) allows automated scripts to interact with a web application and make configuration changes programmatically. \n\n- SSH and FTP are used for secure communication and file transfer, respectively, but do not involve making configuration changes via scripts. \n- GUI refers to a graphical user interface, which typically requires manual interaction rather than automated scripts."
    },




    
    {
        "question": "Which of the following ports is used for secure email?",
        "options": [
            "25",
            "110",
            "143",
            "587"
        ],
        "correct_answer": 4,
        "description": "The correct answer is port 587. Port 587 is used for sending email securely with the SMTP protocol, typically utilizing STARTTLS for encryption. \n\n- Port 25 is used for non-secure email transmission and is often blocked by ISPs for sending mail. \n- Port 110 is used for the POP3 email protocol, which is unencrypted by default. \n- Port 143 is used for IMAP, which is also unencrypted unless encrypted with SSL/TLS."
    },
    {
        "question": "A network administrator wants to install new VoIP switches in a small network closet but is concerned about the current heat level of the room. Which of the following should the administrator take into consideration before installing the new equipment?",
        "options": [
            "The power load of the switches",
            "The humidity in the room",
            "The fire suppression system",
            "The direction of airflow within the switches"
        ],
        "correct_answer": 1,
        "description": "The correct answer is the power load of the switches. VoIP switches can generate significant heat, and the power consumption should be considered to prevent overheating and ensure sufficient cooling. \n\n- While humidity can affect equipment longevity, it is not as critical as power load when considering heat levels. \n- A fire suppression system is important, but it is not directly related to managing heat in the room. \n- Airflow direction within the switches is a concern, but it is secondary to the overall power load and ventilation needs of the room."
    },
    {
        "question": "Which of the following is the next step to take after successfully testing a root cause theory?",
        "options": [
            "Determine resolution steps.",
            "Duplicate the problem in a lab.",
            "Present the theory for approval.",
            "Implement the solution to the problem."
        ],
        "correct_answer": 1,
        "description": "The correct answer is to determine resolution steps. Once the root cause has been identified, the next logical step is to figure out how to resolve the issue. \n\n- Duplicating the problem in a lab might be useful in some cases but is not always necessary once a root cause has been confirmed. \n- Presenting the theory for approval could be part of a larger process but is not the immediate next step. \n- Implementing the solution to the problem would come after resolution steps have been determined."
    },
    {
        "question": "A network administrator is configuring a new switch and wants to ensure that only assigned devices can connect to the switch. Which of the following should the administrator do?",
        "options": [
            "Configure ACLs.",
            "Implement a captive portal.",
            "Enable port security.",
            "Disable unnecessary services."
        ],
        "correct_answer": 3,
        "description": "The correct answer is to enable port security. Port security allows the administrator to specify which devices are allowed to connect to a switch port by their MAC address. \n\n- ACLs (Access Control Lists) are used to filter traffic but do not control which devices can physically connect. \n- A captive portal is typically used for web authentication and not relevant for restricting physical device connections. \n- Disabling unnecessary services improves security but does not directly control which devices connect to the switch."
    },
    {
        "question": "Which of the following does OSPF use to communicate routing updates?",
        "options": [
            "Unicast",
            "Anycast",
            "Multicast",
            "Broadcast"
        ],
        "correct_answer": 3,
        "description": "The correct answer is multicast. OSPF uses multicast to send routing updates to a specific group of routers (224.0.0.5 for all routers, 224.0.0.6 for DR routers). \n\n- Unicast sends data to a single destination, which is not efficient for routing updates. \n- Anycast sends data to the nearest of a group of destinations, but OSPF does not use this method. \n- Broadcast was used in older technologies, but multicast is more efficient for OSPF communication."
    },
    {
        "question": "A user notifies a network administrator about losing access to a remote file server. The network administrator is able to ping the server and verifies the current firewall rules do not block access to the network fileshare. Which of the following tools would help identify which ports are open on the remote file server?",
        "options": [
            "dig",
            "nmap",
            "tracert",
            "nslookup"
        ],
        "correct_answer": 2,
        "description": "The correct answer is nmap. nmap is a powerful network scanning tool that can identify which ports are open on a remote system, helping to troubleshoot access issues. \n\n- dig is used to query DNS records and would not help with port scanning. \n- tracert is used for tracing the route of packets between two devices, not for identifying open ports. \n- nslookup is a tool for querying DNS and resolving hostnames, not for checking open ports."
    },
    {
        "question": "A security team would like to use a system in an isolated network to record the actions of potential attackers. Which of the following solutions is the security team implementing?",
        "options": [
            "Perimeter network",
            "Honeypot",
            "Zero trust infrastructure",
            "Network segmentation"
        ],
        "correct_answer": 2,
        "description": "The correct answer is a honeypot. A honeypot is a system designed to attract and trap potential attackers to monitor and record their actions. \n\n- A perimeter network is used to create a buffer zone between internal and external networks, but it is not designed to record attacker activity. \n- Zero trust infrastructure focuses on verifying all access requests, regardless of their source, but does not specifically deal with recording attacker actions. \n- Network segmentation is a security practice to isolate parts of the network but does not focus on tracking attackers."
    },
    {
        "question": "An organization has a factory automation solution that requires accurate timing between devices. Which of the following should the network administrator implement?",
        "options": [
            "PTP",
            "NTP",
            "NTS",
            "DoT"
        ],
        "correct_answer": 1,
        "description": "The correct answer is PTP (Precision Time Protocol). PTP provides the highly accurate time synchronization needed for factory automation systems. \n\n- NTP (Network Time Protocol) is commonly used but does not provide the same level of precision as PTP. \n- NTS (Network Time Security) is used to secure time synchronization but does not provide the same level of accuracy as PTP. \n- DoT (DNS over TLS) encrypts DNS queries and is unrelated to time synchronization."
    },
    {
        "question": "A network administrator needs to set up a file server to allow user access. The organization uses DHCP to assign IP addresses. Which of the following is the best solution for the administrator to set up?",
        "options": [
            "A separate scope for the file server using a /32 subnet",
            "A reservation for the server based on the MAC address",
            "A static IP address within the DHCP IP range",
            "A SLAAC for the server"
        ],
        "correct_answer": 2,
        "description": "The correct answer is a reservation for the server based on the MAC address. This ensures the server always receives the same IP address from the DHCP server. \n\n- A /32 subnet would limit the file server to a single IP address, making it impractical for this scenario. \n- A static IP address is possible but not optimal for DHCP environments. \n- SLAAC (Stateless Address Autoconfiguration) is used for IPv6 address assignment, not typically used for servers in DHCP environments."
    },
    {
        "question": "Which of the following ports is a secure protocol?",
        "options": [
            "20",
            "23",
            "443",
            "445"
        ],
        "correct_answer": 3,
        "description": "The correct answer is port 443. Port 443 is used for HTTPS, a secure protocol for web traffic that encrypts the data transmitted between the client and server. \n\n- Port 20 is used for FTP data transfer, which is not secure. \n- Port 23 is used for Telnet, which is also insecure. \n- Port 445 is used for SMB, which can be secure but is commonly exploited if not properly configured."
    },





    {
        "question": "Users are moving back into an office that had been vacant for a while. Ten workstations are hooked up in the office, but one workstation cannot obtain a link with the switch. A network engineer checks the documentation and cable labeling, and everything is hooked up as expected. The engineer moves the connection to a different switchport, but a link still cannot be obtained. When the engineer puts a tone generator on the infrastructure cable, no tone is heard at the far end. Which of the following issues is the engineer MOST likely trying to find?",
        "options": [
            "A bad switchport",
            "A break in the cable",
            "A cable short",
            "Cable interference"
        ],
        "correct_answer": 2,
        "description": "The correct answer is a break in the cable. The fact that no tone is heard when a tone generator is used suggests the cable is broken somewhere along its length. \n\n- A bad switchport would result in no connection, but the cable itself would still be functional. \n- A cable short would likely cause electrical issues and could be detected with a different troubleshooting tool. \n- Cable interference generally causes signal degradation but would not prevent a link from being established as described in this scenario."
    },
    {
        "question": "A network administrator is working to configure a new device to provide Layer 2 connectivity to various endpoints including several WAPs. Which of the following devices will the administrator MOST likely configure?",
        "options": [
            "WLAN controller",
            "Cable modem",
            "Load balancer",
            "Switch",
            "Hub"
        ],
        "correct_answer": 4,
        "description": "The correct answer is a switch. A switch operates at Layer 2 and is used to connect various devices, including wireless access points (WAPs), providing the necessary connectivity between endpoints. \n\n- A WLAN controller manages wireless access points but is not primarily used for Layer 2 connectivity. \n- A cable modem is used to connect a network to the internet, not for Layer 2 endpoint connectivity. \n- A load balancer distributes traffic across multiple servers, but it does not directly provide Layer 2 connectivity. \n- A hub is an outdated device that broadcasts data to all connected devices, but it is less efficient compared to a switch."
    },
    {
        "question": "A network deployment engineer is deploying a new single-channel 10G optical connection. Which of the following optics should the engineer MOST likely use to satisfy this requirement?",
        "options": [
            "QSFP",
            "QSFP+",
            "SFP",
            "SFP+"
        ],
        "correct_answer": 4,
        "description": "The correct answer is SFP+. SFP+ is the most common form factor for 10G optical connections, specifically for single-channel 10G applications. \n\n- QSFP and QSFP+ are used for multi-channel configurations and higher data rates (e.g., 40G or 100G), not typically for a single-channel 10G connection. \n- SFP is the previous generation of the SFP+ form factor and supports lower data rates, making it unsuitable for 10G applications."
    },
    {
        "question": "Which of the following is an advantage of using the cloud as a redundant data center?",
        "options": [
            "The process of changing cloud providers is easy.",
            "Better security for company data is provided.",
            "The initial capital expenses are lower.",
            "The need for backups is eliminated."
        ],
        "correct_answer": 3,
        "description": "The correct answer is the initial capital expenses are lower. Cloud providers typically offer a pay-as-you-go model, which reduces the need for significant upfront investments in infrastructure and equipment. \n\n- Changing cloud providers can be complex, involving data migration and service interruptions, making it not an easy process. \n- While cloud services often provide good security, it is not guaranteed to be better than on-premises solutions, as security depends on the configuration and management. \n- Backups are still necessary in the cloud; redundancy does not eliminate the need for regular backups."
    },
    {
        "question": "A network administrator corrected a rule on a misconfigured firewall. Which of the following should the administrator do NEXT when applying the network troubleshooting methodology?",
        "options": [
            "Verify full system functionality.",
            "Document actions and lessons learned.",
            "Establish a theory of probable cause.",
            "Identify potential effects."
        ],
        "correct_answer": 1,
        "description": "The correct answer is verify full system functionality. After correcting a firewall rule, the next step is to verify that the system is functioning as expected and that the issue has been resolved. \n\n- Documenting actions and lessons learned should occur after confirming the system's functionality. \n- Establishing a theory of probable cause and identifying potential effects are steps in earlier stages of the troubleshooting process."
    },
    {
        "question": "Which of the following technologies would MOST likely be used to prevent the loss of connection between a virtual server and network storage devices?",
        "options": [
            "Multipathing",
            "VRRP",
            "Port aggregation",
            "NIC teaming"
        ],
        "correct_answer": 1,
        "description": "The correct answer is multipathing. Multipathing involves using multiple network paths to ensure continued connectivity to storage devices in case one path fails. \n\n- VRRP (Virtual Router Redundancy Protocol) is used for router redundancy, not for storage device connection reliability. \n- Port aggregation is used to increase bandwidth by combining multiple network connections but does not necessarily provide redundancy. \n- NIC teaming combines multiple network interfaces for load balancing and failover, but multipathing specifically addresses storage device connectivity."
    },
    {
        "question": "Which of the following services provides the network information for the address when IPv6 is used for SLAAC addressing?",
        "options": [
            "EUI-64",
            "IPv6 unicast routing",
            "Router advertisement",
            "DHCPv6"
        ],
        "correct_answer": 3,
        "description": "The correct answer is router advertisement. Router advertisements are part of the SLAAC process (Stateless Address Autoconfiguration) in IPv6, which allows devices to automatically configure their IP address based on information provided by a router. \n\n- EUI-64 is a method used to generate the interface identifier for IPv6, but it is not responsible for providing network information. \n- IPv6 unicast routing refers to routing IPv6 traffic to specific destinations, not the address assignment process. \n- DHCPv6 is used for stateful address assignment, but it is not required for SLAAC."
    },
    {
        "question": "A network engineer needs to enable device monitoring using authentication and encryption. Which of the following protocols offers this option?",
        "options": [
            "ESP",
            "SNMPv3",
            "NetFlow",
            "SSLv3"
        ],
        "correct_answer": 2,
        "description": "The correct answer is SNMPv3. SNMPv3 (Simple Network Management Protocol version 3) provides authentication and encryption for secure device monitoring. \n\n- ESP (Encapsulating Security Payload) is used in IPsec for encryption, but it is not designed for device monitoring. \n- NetFlow is used for monitoring network traffic but does not provide encryption or authentication by itself. \n- SSLv3 is a secure protocol used for encrypted communication but is not used for device monitoring."
    },
    {
        "question": "Users are reporting performance issues when attempting to access the main fileshare server. Which of the following steps should a network administrator perform NEXT based on the network troubleshooting methodology?",
        "options": [
            "Implement a fix to resolve the connectivity issues.",
            "Determine if anything has changed.",
            "Establish a theory of probable cause.",
            "Document all findings, actions, and lessons learned."
        ],
        "correct_answer": 2,
        "description": "The correct answer is determine if anything has changed. Before implementing a fix, the network administrator should check for recent changes that may have impacted the server's performance. \n\n- Implementing a fix without understanding the root cause could be premature. \n- Establishing a theory of probable cause happens earlier in the troubleshooting process. \n- Documenting findings occurs after the issue has been resolved."
    },



    {
        "question": "A network administrator is implementing process changes based on recommendations following a recent penetration test. The testers used a method to gain access to the network that involved exploiting a publicly available and fixed remote code execution vulnerability in the VPN appliance. Which of the following should the administrator do to BEST prevent this from happening again?",
        "options": [
            "Change default passwords on internet-facing hardware.",
            "Implement robust ACLs with explicit deny-all entries.",
            "Create private VLANs for management plane traffic.",
            "Routinely upgrade all network equipment firmware."
        ],
        "correct_answer": 4,
        "description": "The correct answer is to routinely upgrade all network equipment firmware. This ensures that known vulnerabilities, such as remote code execution vulnerabilities, are patched to prevent exploitation. \n\n- Changing default passwords helps reduce vulnerabilities but does not address issues with outdated firmware. \n- ACLs can limit access but may not prevent vulnerabilities that are already known. \n- Private VLANs can isolate sensitive traffic but are not a comprehensive solution for firmware vulnerabilities."
    },
    {
        "question": "A technician is troubleshooting a computer issue for a user who works in a new annex of an office building. The user is reporting slow speeds and intermittent connectivity. The computer is connected via a Cat 6 cable to a distribution switch that is 492ft (150m) away. Which of the following should the technician implement to correct the issue?",
        "options": [
            "Increase the bandwidth allocation to the computer.",
            "Install an access switch in the annex and run fiber to the distribution switch.",
            "Run a Cat 7 cable from the computer to the distribution switch.",
            "Enable the computer to support jumbo frames."
        ],
        "correct_answer": 2,
        "description": "The correct answer is to install an access switch in the annex and run fiber to the distribution switch. The maximum distance for a Cat 6 cable is around 328 feet (100 meters), so the cable is too long, causing performance issues. Fiber is ideal for long-distance connections. \n\n- Increasing bandwidth allocation does not address the physical distance issue. \n- Cat 7 cable is designed for higher frequencies but still has similar limitations to Cat 6 in terms of distance. \n- Enabling jumbo frames would not resolve the physical layer issue of distance."
    },
    {
        "question": "A technician is troubleshooting intermittent connectivity between devices and viewing the following syslog entries from a switch:\n21 Feb 2022 16:02:0231 NOTIFICATION %LINK-I-DOWN: G1/10\n21 Feb 2022 16:02:0262 NOTIFICATION %LINK-I-UP: G1/10\n21 Feb 2022 16:03:5321 NOTIFICATION %LINK-I-DOWN: G1/10\n21 Feb 2022 16:03:7873 NOTIFICATION %LINK-I-UP: G1/10\nWhich of the following are these entries indicative of?",
        "options": [
            "DDoS attack",
            "Jitter",
            "Latency",
            "Link flapping"
        ],
        "correct_answer": 4,
        "description": "The correct answer is link flapping. The syslog entries show the link going up and down repeatedly, indicating a physical layer issue like a loose connection or faulty cable. \n\n- A DDoS attack would not cause intermittent link status changes like this. \n- Jitter and latency are network performance issues, not physical layer connectivity problems."
    },
    {
        "question": "Which of the following can be used to aggregate logs from different devices and would make analysis less difficult?",
        "options": [
            "Syslog",
            "SIEM",
            "Event logs",
            "NetFlow"
        ],
        "correct_answer": 2,
        "description": "The correct answer is SIEM. A SIEM (Security Information and Event Management) system collects, aggregates, and analyzes log data from multiple sources, helping with easier detection of security incidents. \n\n- Syslog is a standard for transmitting log data but does not provide aggregation and analysis features like SIEM. \n- Event logs are basic logs from individual systems and do not aggregate data. \n- NetFlow is primarily used for traffic analysis, not log aggregation."
    },
    {
        "question": "A network administrator is checking to see if anything has changed. Which of the following steps of the troubleshooting methodology is involved?",
        "options": [
            "Identify the problem.",
            "Test the theory.",
            "Establish a theory.",
            "Document findings."
        ],
        "correct_answer": 2,
        "description": "The correct answer is to establish a theory. In troubleshooting, after identifying the problem, the technician formulates a theory of what could have changed or caused the issue. \n\n- Identifying the problem is done at the start of the troubleshooting process. \n- Testing the theory occurs after formulating a hypothesis. \n- Documenting findings happens at the end of the troubleshooting process."
    },
    {
        "question": "An older web server on a screened subnet is serving unencrypted web traffic. The server is not capable of serving HTTPS traffic directly, but the firewall is capable of doing so. Which of the following should be done to encrypt all traffic coming into the web server from outside the network? (Choose two.)",
        "options": [
            "A certificate should be installed on the server.",
            "Incoming port 80 traffic at the firewall should be forwarded to port 443 on the server.",
            "Incoming port 80 traffic at the firewall should be forwarded to port 80 on the server.",
            "Incoming port 443 traffic at the firewall should be forwarded to port 80 on the server.",
            "A certificate should be installed on the firewall.",
            "A proxy server should be installed on the screened subnet."
        ],
        "correct_answer": [4, 5],
        "description": "The correct answers are to forward incoming port 443 traffic at the firewall to port 80 on the server and to install a certificate on the firewall. Since the web server cannot serve HTTPS directly, the firewall can handle the encryption by terminating the SSL connection. \n\n- Installing a certificate on the server would not help since the server cannot serve HTTPS directly. \n- Forwarding traffic from port 80 to port 443 does not achieve encryption. \n- A proxy server is unnecessary if the firewall can handle SSL termination."
    },
    {
        "question": "A network manager wants to set up a remote access system for the engineering staff. Access to this system will be over a public IP and secured with an ACL. Which of the following best describes this system?",
        "options": [
            "VPN",
            "Secure Shell",
            "Jump server",
            "API"
        ],
        "correct_answer": 1,
        "description": "The correct answer is VPN (Virtual Private Network). A VPN allows remote users to securely connect to a private network over a public IP, and ACLs can control access. \n\n- Secure Shell (SSH) is used for secure command-line access, not for remote access to a network. \n- A jump server is used to access other servers securely but does not provide a direct remote access solution. \n- An API is a method for communication between systems, not for remote access."
    },
    {
        "question": "A company is hosting a secure server that requires all connections to the server to be encrypted. A junior administrator needs to harden the web server. The following ports on the web server are open:\n443\n80\n22\n587\nWhich of the following ports should be disabled?",
        "options": [
            "22",
            "80",
            "443",
            "587"
        ],
        "correct_answer": 2,
        "description": "The correct answer is port 80. Since the company requires all connections to the server to be encrypted, HTTP (port 80) should be disabled, leaving HTTPS (port 443) open. \n\n- Port 22 is used for SSH and should remain open for secure administrative access. \n- Port 587 is used for secure email submission and should remain open if email services are required. \n- Port 443 is already secured for encrypted connections and should not be disabled."
    },
    {
        "question": "Which of the following IP transmission types encrypts all of the transmitted data?",
        "options": [
            "ESP",
            "AH",
            "GRE",
            "UDP",
            "TCP"
        ],
        "correct_answer": 1,
        "description": "The correct answer is ESP (Encapsulating Security Payload). ESP encrypts both the header and the payload, providing confidentiality for the transmitted data. \n\n- AH (Authentication Header) provides authentication but does not encrypt the data. \n- GRE (Generic Routing Encapsulation) does not provide encryption. \n- UDP and TCP are transport protocols that do not inherently provide encryption."
    },



    
    {
        "question": "A user is unable to reach any resources on the internet. A technician goes to the site and obtains the following output from the workstation:\n\nNetwork Destination    Netmask        Gateway        Interface    Metric\n10.10.51.0            255.255.255.0  On-Link        10.10.51.147  291\n10.10.51.147           255.255.255.255 On-Link        10.10.51.147  291\n10.10.51.255           255.255.255.255 On-Link        10.10.51.147  297\n127.0.0.0              255.0.0.0     On-Link        127.0.0.1     331\n127.0.0.1              255.255.255.255 On-Link        127.0.0.1     331\n127.255.255.255       255.255.255.255 On-Link        127.0.0.1     331\n224.0.0.0              240.0.0.0     On-Link        127.0.0.1     331\n224.0.0.0              240.0.0.0     On-Link        10.10.51.147  291\n255.255.255.255       255.255.255.255 On-Link        127.0.0.1     331\n255.255.255.255       255.255.255.255 On-Link        10.10.51.147  291\n\nWhich of the following commands should the technician use to correct the issue?",
        "options": [
            "route ADD 0.0.0.0 MASK 0.0.0.0 10.10.51.10 metric 35",
            "route CHANGE 10.10.51.0 MASK 255.255.255.255 10.10.52.1 metric 5",
            "route CHANGE 10.10.51.255 MASK 255.0.0.0 On-Link metric 1",
            "route DELETE 127.255.255.255"
        ],
        "correct_answer": 1,
        "description": "The correct answer is route ADD 0.0.0.0 MASK 0.0.0.0 10.10.51.10 metric 35. This command adds a route for the default gateway, which is missing in the output. \n\n- route CHANGE 10.10.51.0 MASK 255.255.255.255 10.10.52.1 metric 5 would incorrectly modify an existing network, causing more issues. \n- route CHANGE 10.10.51.255 MASK 255.0.0.0 On-Link metric 1 would incorrectly change the network to On-Link, preventing connectivity. \n- route DELETE 127.255.255.255 deletes a loopback address route, which is not related to the internet connectivity issue."
    },
    {
        "question": "A network manager wants to view network traffic for devices connected to a switch. A network engineer connects an appliance to a free port on the switch and needs to configure the switch port connected to the appliance. Which of the following is the best option for the engineer to enable?",
        "options": [
            "Trunking",
            "Port mirroring",
            "Full duplex",
            "SNMP"
        ],
        "correct_answer": 2,
        "description": "The correct answer is Port mirroring. This allows the network engineer to view traffic from the appliance and monitor network activity. \n\n- Trunking is used for passing multiple VLANs through a single connection and is not focused on monitoring traffic. \n- Full duplex ensures bidirectional communication but does not specifically help in monitoring network traffic. \n- SNMP is used for network management but does not directly allow the viewing of live traffic."
    },
    {
        "question": "An IT administrator needs to connect older smart-plug devices to the network. The administrator wants to prevent future issues from occurring by using an 802.11 standard that only operates on the 2.4GHz frequency. Which of the following standards should the administrator choose?",
        "options": [
            "802.11a",
            "802.11ac",
            "802.11ax",
            "802.11b"
        ],
        "correct_answer": 4,
        "description": "The correct answer is 802.11b. This standard operates exclusively on the 2.4GHz frequency and would be ideal for the older smart-plug devices. \n\n- 802.11a operates on the 5GHz frequency, making it incompatible with the requirement for 2.4GHz. \n- 802.11ac and 802.11ax support dual-band frequencies (2.4GHz and 5GHz), but are more advanced and may not be needed for older devices."
    },
    {
        "question": "A network contains 25 access points. Which of the following devices would be best to change configurations on all the devices remotely?",
        "options": [
            "WLAN controller",
            "Load balancer",
            "Bridge",
            "Layer 3 switch"
        ],
        "correct_answer": 1,
        "description": "The correct answer is WLAN controller. A WLAN controller allows remote management and configuration of multiple access points in a wireless network. \n\n- A Load balancer is used to distribute network traffic evenly across multiple servers but does not help in managing access points. \n- A Bridge connects two or more network segments but is not used for centralized management of access points. \n- A Layer 3 switch is used for routing between VLANs, not for configuring access points."
    },
    {
        "question": "Which of the following is used to estimate the average life span of a device?",
        "options": [
            "RTO",
            "RPO",
            "MTBF",
            "MTTR"
        ],
        "correct_answer": 3,
        "description": "The correct answer is MTBF (Mean Time Between Failures). MTBF is used to estimate the average lifespan of a device by calculating the time between failures. \n\n- RTO (Recovery Time Objective) refers to the amount of time it takes to restore a system after failure. \n- RPO (Recovery Point Objective) relates to the amount of data loss that is acceptable during a failure. \n- MTTR (Mean Time to Repair) refers to the average time taken to repair a failed device."
    },
    {
        "question": "An IT administrator is creating an alias to the primary customer's domain. Which of the following DNS record types does this represent?",
        "options": [
            "CNAME",
            "MX",
            "A",
            "PTR"
        ],
        "correct_answer": 1,
        "description": "The correct answer is CNAME. A CNAME (Canonical Name) record is used to create an alias for a domain, pointing it to another domain. \n\n- MX (Mail Exchange) records are used to specify mail servers for a domain. \n- A (Address) records are used to map domain names to IP addresses. \n- PTR (Pointer) records are used for reverse DNS lookups, mapping IP addresses to domain names."
    },
    {
        "question": "Which of the following is a characteristic of the application layer?",
        "options": [
            "It relies upon other layers for packet delivery.",
            "It checks independently for packet loss.",
            "It encrypts data in transit.",
            "It performs address translation."
        ],
        "correct_answer": 1,
        "description": "The correct answer is It relies upon other layers for packet delivery. The application layer relies on the transport layer and lower layers for delivering data packets. \n\n- The application layer does not independently check for packet loss, which is handled by the transport layer (TCP). \n- Encryption of data is typically handled by protocols like SSL/TLS, which can operate at various layers. \n- Address translation is performed at the network layer (e.g., NAT) and not the application layer."
    },
    {
        "question": "Which of the following is the best VPN to use for only encrypting and routing data for a specific destination?",
        "options": [
            "Split-tunnel",
            "Site-to-site",
            "Client",
            "Layer 2"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Split-tunnel. Split tunneling allows the VPN to route only certain traffic (e.g., to a specific destination) through the VPN, while other traffic can go directly to the internet. \n\n- Site-to-site VPNs are used to connect two networks securely but do not apply to routing traffic for a single destination. \n- Client VPNs are typically used for remote access and routing all traffic through the VPN. \n- Layer 2 VPNs provide a virtual LAN, which is not necessary for routing data for a specific destination."
    },
    {
        "question": "Which of the following is used when a workstation sends a DHCP broadcast to a server on another LAN?",
        "options": [
            "Reservation",
            "Dynamic assignment",
            "Helper address",
            "DHCP offer"
        ],
        "correct_answer": 3,
        "description": "The correct answer is Helper address. A helper address forwards DHCP broadcast messages to a DHCP server on another LAN. \n\n- Reservation is used to assign a specific IP address to a device. \n- Dynamic assignment refers to the process of assigning IP addresses to devices dynamically, but not specifically related to broadcasts. \n- DHCP offer is the message the DHCP server sends back in response to a DHCP request."
    },
    {
        "question": "An administrator is adjusting the routing policy to ensure the headquarters location can connect to a new out-of-state branch office via BGP. Which of the following types of networks is being described?",
        "options": [
            "PAN",
            "MAN",
            "LAN",
            "WAN"
        ],
        "correct_answer": 4,
        "description": "The correct answer is WAN (Wide Area Network). A WAN connects geographically dispersed locations, such as branch offices in different states. \n\n- PAN (Personal Area Network) covers a small, local area (e.g., personal devices). \n- MAN (Metropolitan Area Network) connects networks within a city or large campus. \n- LAN (Local Area Network) connects devices within a single location or office."
    }



]
