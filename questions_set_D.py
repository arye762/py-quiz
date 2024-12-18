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
        "correct_answer": 3,
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
    },

    
    {
        "question": "A company wants to implement a disaster recovery site for non-critical applications, which can tolerate a short period of downtime. Which of the following types of sites should the company implement to achieve this goal?",
        "options": [
            "Hot",
            "Cold",
            "Warm",
            "Passive"
        ],
        "correct_answer": 3,
        "description": "The correct answer is Warm. A warm site strikes a balance by offering faster recovery than a cold site but at a lower cost than a hot site, making it ideal for non-critical applications with some tolerance for downtime. \n\n- Hot sites are fully operational backups but are costly and unnecessary for non-critical applications. \n- Cold sites are cheap but require significant setup time, unsuitable for minimizing downtime. \n- Passive is not a standard disaster recovery site classification."
    },
    {
        "question": "Which of the following can be used to identify users after an action has occurred?",
        "options": [
            "Access control vestibule",
            "Cameras",
            "Asset tag",
            "Motion detectors"
        ],
        "correct_answer": 2,
        "description": "The correct answer is Cameras. Cameras provide visual evidence and logs that can be reviewed to identify users after an action occurs. \n\n- Access control vestibules regulate entry but do not track users' actions. \n- Asset tags are used for identifying equipment, not users. \n- Motion detectors sense movement but do not provide user identification."
    },
    {
        "question": "Which of the following standards would apply to a 10GB network link that is 1.86mi (3km)?",
        "options": [
            "10GBASE-TX",
            "10GBASE-T",
            "10GBASE-SR",
            "10GBASE-LR"
        ],
        "correct_answer": 4,
        "description": "The correct answer is 10GBASE-LR. This standard supports long-range fiber-optic communication, making it suitable for a 3km distance. \n\n- 10GBASE-TX and 10GBASE-T are copper-based standards and not suitable for such long distances. \n- 10GBASE-SR is designed for short-range fiber, typically less than 300m."
    },
    {
        "question": "Which of the following kinds of targeted attacks uses multiple computers or bots to request the same resource repeatedly?",
        "options": [
            "On-path",
            "DDoS",
            "ARP spoofing",
            "MAC flooding"
        ],
        "correct_answer": 2,
        "description": "The correct answer is DDoS. A Distributed Denial of Service (DDoS) attack uses multiple systems to flood a target with requests, overwhelming it. \n\n- On-path attacks intercept communications but do not involve resource flooding. \n- ARP spoofing manipulates address resolution but does not flood resources. \n- MAC flooding overwhelms switch tables but is not typically distributed."
    },
    {
        "question": "A local service provider connected 20 schools in a large city with a fiber-optic switched network. Which of the following network types did the provider set up?",
        "options": [
            "LAN",
            "MAN",
            "CAN",
            "WAN"
        ],
        "correct_answer": 2,
        "description": "The correct answer is MAN. A Metropolitan Area Network (MAN) is designed to cover a citywide area, such as connecting schools within a large city. \n\n- LANs are limited to smaller areas, like a single building. \n- CANs are for campus-sized networks but are smaller in scope than a MAN. \n- WANs span wider geographic areas, typically between cities or countries."
    },
    {
        "question": "A systems administrator is looking for operating system information, running services, and network ports that are available on a server. Which of the following software tools should the administrator use to accomplish this task?",
        "options": [
            "nslookup",
            "nmap",
            "traceroute",
            "netstat"
        ],
        "correct_answer": 2,
        "description": "The correct answer is nmap. Nmap is a network scanning tool that provides detailed information about open ports, services, and OS details. \n\n- nslookup is used for DNS queries and does not analyze servers. \n- Traceroute maps the path packets take but does not provide server details. \n- Netstat shows active connections but lacks comprehensive scanning capabilities."
    },
    {
        "question": "Which of the following should be configured on a separate network segment without access to the primary company network when security is a concern?",
        "options": [
            "Email server",
            "IoT devices",
            "Wireless LAN controller",
            "Voice gateway"
        ],
        "correct_answer": 2,
        "description": "The correct answer is IoT devices. IoT devices often have weaker security and should be isolated to reduce the risk of compromising the main network. \n\n- Email servers need direct access to the network to function effectively. \n- Wireless LAN controllers integrate with the primary network to manage Wi-Fi. \n- Voice gateways are typically secure and part of the main network."
    },
    {
        "question": "A firewall administrator observes log entries of traffic being allowed to a web server on port 80 and port 443. The policy for this server is to only allow traffic on port 443. The firewall administrator needs to investigate how this change occurred to prevent a reoccurrence. Which of the following should the firewall administrator do next?",
        "options": [
            "Consult the firewall audit logs.",
            "Change the policy to allow port 80.",
            "Remove the server object from the firewall policy.",
            "Check the network baseline."
        ],
        "correct_answer": 1,
        "description": "The correct answer is to consult the firewall audit logs. Logs can reveal who made the change and when it occurred, providing insight into potential issues. \n\n- Changing the policy to allow port 80 contradicts the stated requirement. \n- Removing the server object may disrupt legitimate operations. \n- Checking the network baseline would not help identify configuration changes."
    },
    {
        "question": "A customer hired a network consultant to provide advice on the installation of new wireless access. The customer has several devices that operate in either the 5.0GHz range or the 2.4GHz range, and the best performance must be available. Which of the following standards should the technician suggest?",
        "options": [
            "802.11a",
            "802.11b",
            "802.11g",
            "802.11n"
        ],
        "correct_answer": 4,
        "description": "The correct answer is 802.11n. This standard supports both 2.4GHz and 5GHz frequencies, offering compatibility and optimal performance. \n\n- 802.11a operates only on 5GHz and lacks broader compatibility. \n- 802.11b and 802.11g are limited to 2.4GHz and provide slower speeds than 802.11n."
    },
    {
        "question": "A technician is expanding a wireless network and adding new access points. The company requires that each access point broadcast the same SSID. Which of the following should the technician implement for this requirement?",
        "options": [
            "MIMO",
            "Roaming",
            "Channel bonding",
            "Extended service set"
        ],
        "correct_answer": 4,
        "description": "The correct answer is Extended Service Set (ESS). ESS allows multiple access points to share the same SSID, enabling seamless connectivity. \n\n- MIMO improves speed and reliability but does not address SSID consistency. \n- Roaming deals with transitioning between access points but requires an ESS. \n- Channel bonding increases bandwidth but does not affect SSIDs."
    },



    {
        "question": "Which of the following DNS records maps an alias to a true name?",
        "options": [
            "AAAA",
            "NS",
            "TXT",
            "CNAME"
        ],
        "correct_answer": 4,
        "description": "The correct answer is CNAME. CNAME (Canonical Name) records map an alias to the true canonical name of a domain, enabling redirection. \n\n- AAAA records map a hostname to an IPv6 address, not an alias. \n- NS records indicate the authoritative name servers for a domain, unrelated to aliases. \n- TXT records store text-based information, such as SPF data for email authentication, and do not handle aliasing."
    },
    {
        "question": "Which of the following combinations of single cables and transceivers will allow a server to have 40GB of network throughput? (Choose two.)",
        "options": [
            "SFP+",
            "SFP",
            "QSFP+",
            "Multimode",
            "Cat 6a",
            "Cat 5e"
        ],
        "correct_answer": [3, 4],
        "description": "The correct answers are QSFP+ and Multimode. QSFP+ supports high-speed 40Gbps connections, and multimode fiber is suitable for such high-bandwidth requirements. \n\n- SFP+ is limited to 10Gbps, insufficient for 40Gbps throughput. \n- SFP supports lower speeds and is not suitable for 40Gbps. \n- Cat 6a supports 10Gbps over copper, insufficient for 40Gbps. \n- Cat 5e is limited to 1Gbps, far below the needed throughput."
    },
    {
        "question": "A global company has acquired a local company. The companies are geographically separate. The IP address ranges for the two companies are as follows:\n• Global company: 10.0.0.0/16\n• Local company: 10.0.0.0/24\nWhich of the following can the network engineer do to quickly connect the two companies?",
        "options": [
            "Assign static routing to advertise the local company's network",
            "Assign an overlapping IP address range to both companies",
            "Assign a new IP address range to the local company",
            "Assign a NAT range to the local company"
        ],
        "correct_answer": 4,
        "description": "The correct answer is Assign a NAT range to the local company. NAT (Network Address Translation) resolves the IP address overlap, enabling immediate connectivity between the networks. \n\n- Static routing does not address the overlapping IP ranges. \n- Overlapping IP address ranges would exacerbate routing conflicts. \n- Assigning a new IP address range would require time-consuming reconfiguration."
    },
    {
        "question": "A user is unable to navigate to a website because the provided URL is not resolving to the correct IP address. Other users are able to navigate to the intended website without issue. Which of the following is most likely causing this issue?",
        "options": [
            "Hosts file",
            "Self-signed certificate",
            "Nameserver record",
            "IP helper"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Hosts file. A misconfigured hosts file on the user's device can override DNS resolution, leading to incorrect IP mappings. \n\n- Self-signed certificates affect HTTPS validation but do not influence IP resolution. \n- Nameserver record issues would impact all users, not just one. \n- IP helpers facilitate DHCP relay but are unrelated to DNS."
    },
    {
        "question": "A technician completed troubleshooting and was able to fix an issue. Which of the following is the best method the technician can use to pass along the exact steps other technicians should follow in case the issue arises again?",
        "options": [
            "Use change management to build a database",
            "Send an email stating that the issue is resolved",
            "Document the lessons learned",
            "Close the ticket and inform the users"
        ],
        "correct_answer": 3,
        "description": "The correct answer is Document the lessons learned. Comprehensive documentation ensures that future technicians have a clear guide for resolving similar issues efficiently. \n\n- Change management focuses on implementing changes, not documenting troubleshooting. \n- Emails may be overlooked and lack central organization. \n- Closing the ticket addresses the current issue but does not aid future troubleshooting."
    },
    {
        "question": "Which of the following most likely determines the size of a rack for installation? (Choose two.)",
        "options": [
            "KVM size",
            "Switch depth",
            "Hard drive size",
            "Cooling fan speed",
            "Outlet amperage",
            "Server height"
        ],
        "correct_answer": [2, 6],
        "description": "The correct answers are Switch depth and Server height. These physical dimensions determine the rack's size and capacity. \n\n- KVM size is small and does not dictate rack dimensions. \n- Hard drive size relates to server capacity, not rack dimensions. \n- Cooling fan speed affects temperature control but not rack size. \n- Outlet amperage pertains to electrical provisioning, not physical rack size."
    },
    {
        "question": "A network technician is troubleshooting a connectivity issue. All users within the network report that they are unable to navigate to websites on the internet; however, they can still access local network resources. The technician issues a command and receives the following results:\nPinging comptia.com [172.67.217.56] with 32 bytes of data:\nReply from 172.67.217.56: TTL expired in transit.\nWhich of the following best explains the result of this command?",
        "options": [
            "Incorrect VLAN settings",
            "Upstream routing loop",
            "Network collisions",
            "DNS misconfiguration"
        ],
        "correct_answer": 2,
        "description": "The correct answer is Upstream routing loop. TTL expired messages indicate a loop in the network routing, preventing packets from reaching their destination. \n\n- Incorrect VLAN settings would block connectivity entirely, not cause looping. \n- Network collisions slow traffic but do not generate TTL errors. \n- DNS misconfiguration would prevent name resolution, not cause TTL expiration."
    },
    {
        "question": "A network engineer is configuring new switches. Some of the trunk ports are in a blocking state. Which of the following should the network engineer reconfigure?",
        "options": [
            "STP",
            "Port mirroring",
            "Flow control",
            "LACP"
        ],
        "correct_answer": 1,
        "description": "The correct answer is STP. The Spanning Tree Protocol (STP) prevents loops in switched networks by blocking redundant paths, which might require reconfiguration if incorrect. \n\n- Port mirroring duplicates traffic for analysis, unrelated to blocking states. \n- Flow control manages data rate but does not impact STP operations. \n- LACP aggregates links but does not directly influence port blocking."
    },
    {
        "question": "Which of the following would most likely affect design considerations when building out an IDF?",
        "options": [
            "The source panel amperage",
            "The fire suppression system",
            "The humidity levels",
            "The cable transmission speeds"
        ],
        "correct_answer": 4,
        "description": "The correct answer is The cable transmission speeds. IDF design must account for transmission speeds to ensure compatibility with network standards and reduce latency. \n\n- Source panel amperage relates to power provisioning but does not affect network design. \n- Fire suppression ensures safety but does not impact data flow. \n- Humidity control preserves equipment but is secondary to transmission considerations."
    },
    {
        "question": "A building was recently remodeled in order to expand the front lobby. Some mobile users have been unable to connect to the available network jacks within the new lobby, while others have had no issues. Which of the following is the most likely cause of the connectivity issues?",
        "options": [
            "LACP",
            "Port security",
            "802.11 ax",
            "Duplex settings"
        ],
        "correct_answer": 2,
        "description": "The correct answer is Port security. Port security could block unauthorized devices from connecting, leading to selective connectivity issues. \n\n- LACP relates to link aggregation, not individual port access. \n- 802.11 ax is a wireless standard and unrelated to wired jacks. \n- Duplex settings impact connection speed but not device authorization."
    },
{
        "question": "A network administrator for a small office is adding a passive IDS to its network switch for the purpose of inspecting network traffic. Which of the following should the administrator use?",
        "options": [
            "SNMP trap",
            "Port mirroring",
            "Syslog collection",
            "API integration"
        ],
        "correct_answer": 2,
        "description": "The correct answer is Port mirroring. Port mirroring duplicates traffic from specific ports to another port where the IDS is connected, allowing the IDS to inspect traffic without interfering with normal operations. \n\n- SNMP trap is for alerting and monitoring, not inspecting traffic. \n- Syslog collection gathers logs but does not analyze live traffic. \n- API integration connects applications but does not facilitate traffic inspection."
    },
    {
        "question": "When internal users attempt to access the company website, they are redirected to an inappropriate website. Which of the following is this scenario an example of?",
        "options": [
            "DNS poisoning",
            "On-path attack",
            "VLAN hopping",
            "ARP spoofing"
        ],
        "correct_answer": 1,
        "description": "The correct answer is DNS poisoning. DNS poisoning corrupts the DNS cache to redirect users to malicious websites. \n\n- On-path attacks intercept communication but do not involve DNS. \n- VLAN hopping targets VLAN segmentation, not domain redirection. \n- ARP spoofing alters IP-to-MAC address mappings, not DNS resolution."
    },
    {
        "question": "Which of the following authentication protocols should be used when securing a basic wireless network? (Choose two.)",
        "options": [
            "WPA2",
            "RDP",
            "WPA",
            "SSL",
            "SNMP",
            "EAP"
        ],
        "correct_answer": [1, 6],
        "description": "The correct answers are WPA2 and EAP. WPA2 is the industry standard for wireless security, while EAP provides flexible authentication mechanisms. \n\n- RDP is for remote desktop connections, not wireless security. \n- WPA is an older protocol with weaker security than WPA2. \n- SSL secures web traffic but is unrelated to wireless authentication. \n- SNMP is for network management, not authentication."
    },
    {
        "question": "In order to prepare for a fire or natural disaster, a Chief Executive Officer would like the network administrator to set up a site with no equipment. Which of the following should the network administrator set up?",
        "options": [
            "A warm site",
            "A cold site",
            "A hot site",
            "A site provided by the ISP"
        ],
        "correct_answer": 2,
        "description": "The correct answer is A cold site. A cold site provides a physical location with power and basic infrastructure but no pre-installed equipment, making it a cost-effective option for disaster preparedness. \n\n- Warm sites have equipment but lack full operational readiness. \n- Hot sites are fully operational and costly, exceeding the CEO's requirements. \n- A site provided by the ISP refers to internet services, not disaster recovery."
    },
    {
        "question": "Which of the following would allow a network administrator to analyze attacks coming from the internet without affecting latency?",
        "options": [
            "IPS",
            "IDS",
            "Load balancer",
            "Firewall"
        ],
        "correct_answer": 2,
        "description": "The correct answer is IDS. An Intrusion Detection System analyzes traffic passively and does not interfere with data flow, preserving latency. \n\n- IPS actively blocks threats, which can affect latency. \n- Load balancers manage traffic distribution, not attack analysis. \n- Firewalls enforce rules but do not specialize in detailed attack analysis."
    },
    {
        "question": "A Chief Information Officer is concerned about environmental issues in the data center at corporate headquarters. Which of the following are the most common sensors installed in a data center? (Choose two.)",
        "options": [
            "Carbon monoxide",
            "Air flow",
            "Flooding",
            "Humidity",
            "Electrical",
            "Temperature"
        ],
        "correct_answer": [4, 6],
        "description": "The correct answers are Humidity and Temperature. Humidity sensors prevent condensation that could damage equipment, and temperature sensors ensure the data center remains within operational limits. \n\n- Carbon monoxide sensors are for human safety, not equipment. \n- Airflow sensors monitor cooling but are less critical than humidity and temperature. \n- Flooding sensors are situational and not universally necessary. \n- Electrical sensors monitor circuits, not environmental conditions."
    },
    {
        "question": "Which of the following routing technologies uses a successor and a feasible successor?",
        "options": [
            "IS-IS",
            "OSPF",
            "BGP",
            "EIGRP"
        ],
        "correct_answer": 4,
        "description": "The correct answer is EIGRP. EIGRP (Enhanced Interior Gateway Routing Protocol) uses the concepts of successor and feasible successor to ensure efficient and loop-free routing. \n\n- IS-IS and OSPF are link-state protocols and do not use these terms. \n- BGP is a path vector protocol and operates differently from EIGRP."
    },
    {
        "question": "A hacker used a packet sniffer on the network to capture the hardware address of the server. Which of the following types of attacks can the hacker perform now?",
        "options": [
            "Piggybacking",
            "MAC spoofing",
            "Evil twin",
            "VLAN hopping"
        ],
        "correct_answer": 2,
        "description": "The correct answer is MAC spoofing. By using the captured hardware address, a hacker can impersonate the server on the network. \n\n- Piggybacking refers to unauthorized physical access, not network impersonation. \n- Evil twin involves setting up rogue wireless access points, not MAC addresses. \n- VLAN hopping targets VLAN segregation, not MAC address usage."
    },
    {
        "question": "Which of the following are the most likely reasons voltage calculations are made before installing equipment? (Choose two.)",
        "options": [
            "To ensure equipment is not damaged",
            "To send reports for compliance regulations",
            "To speed up the installation process",
            "To ensure compatibility",
            "To meet legal requirements",
            "To ensure the grounding is being maintained"
        ],
        "correct_answer": [1, 4],
        "description": "The correct answers are To ensure equipment is not damaged and To ensure compatibility. Calculating voltage prevents damage to sensitive equipment and ensures it operates within specified ranges. \n\n- Compliance regulations may require reporting but are not directly tied to voltage. \n- Speeding up installation is unrelated to electrical safety. \n- Legal requirements rarely focus on voltage calculations. \n- Grounding is critical but distinct from voltage calculations."
    },
    {
        "question": "A network technician is troubleshooting a specific port on a switch. Which of the following commands should the technician use to see the port configuration?",
        "options": [
            "show route",
            "show interface",
            "show arp",
            "show port"
        ],
        "correct_answer": 2,
        "description": "The correct answer is show interface. This command displays detailed information about a port's configuration, including speed, status, and errors. \n\n- show route displays routing tables, not port details. \n- show arp provides IP-to-MAC mappings, unrelated to port configurations. \n- show port is not a standard command for viewing detailed port settings."
    },





    
    {
        "question": "A company is sending a switch to a remote site to be reused. An administrator needs to move the switch and ensure no network settings persist. Which of the following databases does the administrator need to delete?",
        "options": [
            "VLAN",
            "STP",
            "ARP",
            "Trunking"
        ],
        "correct_answer": 3,
        "description": "The correct answer is ARP. The Address Resolution Protocol (ARP) table stores the mappings between IP addresses and MAC addresses, which are dynamically learned and not intended to persist. \n\n- VLAN configurations define network segments and are needed for network segmentation, so deleting them would be inappropriate. \n- STP (Spanning Tree Protocol) and Trunking configurations relate to network loop prevention and VLAN management but do not need to be cleared for a fresh setup."
    },
    {
        "question": "A network administrator needs to back up the configurations of all network devices and store the configurations off-line until they are needed. Which of the following should the administrator use to back up the configurations securely?",
        "options": [
            "SFTP",
            "Syslog",
            "Telnet",
            "SNMP"
        ],
        "correct_answer": 1,
        "description": "The correct answer is SFTP. Secure File Transfer Protocol (SFTP) is used to securely transfer files, making it the best choice for backing up configurations. \n\n- Syslog is used for sending event logs, not for file backups. \n- Telnet is insecure and should not be used for transferring sensitive data. \n- SNMP is used for network management and monitoring, not for backing up configurations."
    },
    {
        "question": "A network technician is working to upgrade an existing wireless system in order to improve the coverage of APs throughout the building. Which of the following should the technician perform to determine the optimal placement of APs for the new wireless system?",
        "options": [
            "Cable testing",
            "Network assessment",
            "Site survey",
            "Packet capture"
        ],
        "correct_answer": 3,
        "description": "The correct answer is Site survey. A site survey is essential to determine the best placement of access points (APs) by evaluating signal strength, coverage areas, and interference. \n\n- Cable testing is used for verifying the physical layer of the network, not wireless coverage. \n- Network assessment involves evaluating overall network performance but does not specifically address AP placement. \n- Packet capture is used for analyzing traffic and troubleshooting, not for planning wireless coverage."
    },
    {
        "question": "A network administrator is preparing new switches that will be deployed to support a network extension project. The lead network engineer has already provided documentation to ensure the switches are set up properly. Which of the following did the engineer most likely provide?",
        "options": [
            "Physical network diagram",
            "Site survey reports",
            "Baseline configurations",
            "Logical network diagram"
        ],
        "correct_answer": 3,
        "description": "The correct answer is Baseline configurations. Baseline configurations are the standardized settings that should be applied to ensure consistency across network devices. \n\n- A physical network diagram shows the actual physical connections but does not include device configurations. \n- Site survey reports are used for planning the placement of devices, not for configuration. \n- Logical network diagrams depict how the network functions at a conceptual level but do not specify individual configurations."
    },
    {
        "question": "Which of the following is the first step a network administrator should take in the troubleshooting methodology?",
        "options": [
            "Establish a plan of action.",
            "Document findings and outcomes.",
            "Test the theory to determine cause.",
            "Identify the problem."
        ],
        "correct_answer": 4,
        "description": "The correct answer is Identify the problem. The first step in troubleshooting is to clearly identify the issue before any corrective action is taken. \n\n- Establishing a plan of action comes after identifying the problem. \n- Documenting findings and outcomes is done throughout the troubleshooting process and is not the first step. \n- Testing the theory comes after identifying the problem and forming a hypothesis."
    },
    {
        "question": "A network administrator needs to implement a solution to mediate access to the internet. Which of the following should the administrator most likely implement?",
        "options": [
            "Router",
            "Cloud gateway",
            "Proxy",
            "Intrusion prevention system"
        ],
        "correct_answer": 3,
        "description": "The correct answer is Proxy. A proxy server is commonly used to control and monitor internet access, acting as an intermediary between the user and the internet. \n\n- A router is primarily used to route traffic between networks but doesn't specifically control access to the internet. \n- A cloud gateway provides cloud network connectivity, not access mediation. \n- An intrusion prevention system (IPS) is used for security and threat detection, not access control."
    },
    {
        "question": "Which of the following steps of the troubleshooting methodology would most likely include checking through each level of the OSI model after the problem has been identified?",
        "options": [
            "Establish a theory.",
            "Implement the solution.",
            "Create a plan of action.",
            "Verify functionality"
        ],
        "correct_answer": 4,
        "description": "The correct answer is Verify functionality. After identifying and resolving the problem, the technician checks the system's functionality to ensure the issue has been properly addressed, which may involve reviewing multiple layers of the OSI model. \n\n- Establishing a theory comes earlier in the troubleshooting process, not after the problem is identified. \n- Implementing the solution is done after formulating a plan but does not involve verifying the system's functionality. \n- Creating a plan of action happens before resolving the issue."
    },
    {
        "question": "A company upgrades its network and PCs to gigabit speeds. After the upgrade, users are not getting the expected performance. Technicians discover that the speeds of the endpoint NICs are inconsistent. Which of the following should be checked first to troubleshoot the issue?",
        "options": [
            "Speed mismatches",
            "Load balancer settings",
            "Devices’ duplex settings",
            "Office wiring category"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Speed mismatches. The first thing to check is whether the NICs are configured for the correct speed, as mismatched speeds can cause inconsistent performance. \n\n- Load balancer settings are typically not related to NIC speed inconsistencies. \n- Duplex settings, while important, are less likely to cause inconsistencies if the speeds are mismatched. \n- Office wiring category refers to the physical layer, which is less likely to be the cause of inconsistent NIC speeds."
    },
    {
        "question": "A network technician must connect a newly installed access switch in a warehouse to the distribution switch in the telecommunications closet. The distance between the two switches is 1,640ft (500m). Which of the following is the best cable choice?",
        "options": [
            "Fiber",
            "Cat 5e",
            "Cat 6a",
            "Coaxial"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Fiber. Fiber optic cables are capable of supporting high speeds over long distances, such as 500 meters, making them ideal for this scenario. \n\n- Cat 5e and Cat 6a cables have distance limitations of around 100 meters for gigabit speeds, making them unsuitable for this distance. \n- Coaxial cables are outdated and typically not used for modern network installations."
    },
    {
        "question": "After installing a new 6E wireless router in a small office, a technician notices that some wireless devices are not able to achieve the rated speeds. Which of the following should the technician check to troubleshoot the issue? (Choose two.)",
        "options": [
            "Client device compatibility",
            "Back-end cabling",
            "Weather phenomena",
            "Voltage source requirements",
            "Interference levels",
            "Processing power"
        ],
        "correct_answer": [1, 5],
        "description": "The correct answers are Client device compatibility and Processing power. The first thing to check is whether the devices are compatible with Wi-Fi 6E and capable of achieving the rated speeds. Additionally, ensure the devices have sufficient processing power to handle the faster speeds. \n\n- Back-end cabling is not as likely to affect wireless speeds as the issue is with the wireless connection. \n- Weather phenomena typically do not impact indoor Wi-Fi performance. \n- Voltage source requirements are unlikely to cause speed issues for most devices."
    },


    
    {
        "question": "A company is upgrading the network switches at its backup data center, which is geographically separated from the main data center. The company hired a contractor to physically install and cable the new switches in their cabinets. Which of the following should the network engineering team provide to ensure the job is completed accurately?",
        "options": [
            "Rack diagram",
            "IDF diagram",
            "Site survey",
            "Logical diagram"
        ],
        "correct_answer": 1,
        "description": "The correct answer is the rack diagram. This provides a clear and detailed plan for where each switch should be placed in the rack, ensuring proper installation and cabling. \n\n- The IDF diagram is useful for documenting intermediate distribution frames but is less specific to the rack layout. \n- A site survey is typically used for planning network placement but does not focus on physical installation specifics. \n- The logical diagram shows network connections but lacks the granularity needed for physical installations."
    },
    {
        "question": "A network engineer is troubleshooting application connectivity issues between a server and a client. The network engineer needs to view the certificate exchange between the two hosts. Which of the following tools should the network engineer use?",
        "options": [
            "dig",
            "tcpdump",
            "nmap",
            "traceroute"
        ],
        "correct_answer": 2,
        "description": "The correct answer is tcpdump. This tool allows the network engineer to capture and analyze network traffic, including the certificate exchange between the client and the server. \n\n- Dig is used for DNS lookups and would not be suitable for capturing traffic. \n- Nmap is used for network scanning and security auditing, but not for monitoring certificate exchanges. \n- Traceroute helps identify the path packets take across the network but does not capture traffic details such as certificates."
    },
    {
        "question": "A network technician needs to determine which RJ45 jack in a patch panel corresponds to the RJ45 drop in the Chief Executive Officer's office. Which of the following tools would be best for the technician to use?",
        "options": [
            "Fusion splicer",
            "Cable tester",
            "Tone generator",
            "Spectrum analyzer"
        ],
        "correct_answer": 3,
        "description": "The correct answer is the tone generator. This tool sends a signal through the cable, allowing the technician to trace it and identify the correct RJ45 jack. \n\n- A fusion splicer is used for joining fiber optic cables, not for tracing copper cables. \n- A cable tester checks for continuity and signal integrity but does not help in locating cables. \n- A spectrum analyzer is used to analyze radio frequency signals and is not suitable for this task."
    },
    {
        "question": "Which of the following is the DNS feature that controls how long a lookup is stored in cache on a server?",
        "options": [
            "CNAME",
            "TTL",
            "SOA",
            "SRV"
        ],
        "correct_answer": 2,
        "description": "The correct answer is TTL (Time to Live). This setting controls how long a DNS record is cached by a server or resolver. \n\n- CNAME is a record type that maps one domain to another but does not affect cache duration. \n- SOA (Start of Authority) is a DNS record that provides information about the domain but does not relate to caching. \n- SRV records are used to define services but do not influence the cache duration."
    },
    {
        "question": "A customer is having issues accessing local resources on the network. A technician questions the user and discovers that a small switch had been taken out of storage and installed so that additional devices could be connected in the room. The technician runs the ping command from the PC to the network server and does not find any issues. However, data transfers to the server are slow, and the transfer appears to be locked up at times. Which of the following is the most likely cause of the issue?",
        "options": [
            "Duplexing mismatch",
            "Reversed TX/RX pinouts",
            "Cable crosstalk",
            "Failed transceiver"
        ],
        "correct_answer": 1,
        "description": "The correct answer is duplexing mismatch. This occurs when devices on opposite ends of a connection are set to different duplex modes, leading to slow or inconsistent communication. \n\n- Reversed TX/RX pinouts could cause connectivity issues but are less likely to result in slow, inconsistent data transfers. \n- Cable crosstalk would typically lead to signal degradation or errors, not slow transfer speeds. \n- A failed transceiver would cause complete loss of connectivity, rather than slow performance."
    },
    {
        "question": "A network administrator is planning to implement device monitoring to enhance network visibility. The security team requires that the solution provides authentication and encryption. Which of the following meets these requirements?",
        "options": [
            "SIEM",
            "Syslog",
            "NetFlow",
            "SNMPv3"
        ],
        "correct_answer": 4,
        "description": "The correct answer is SNMPv3. This version of the Simple Network Management Protocol includes built-in authentication and encryption, making it suitable for secure monitoring. \n\n- SIEM (Security Information and Event Management) is for security event analysis and does not focus on device monitoring with encryption. \n- Syslog is typically unencrypted, making it unsuitable for secure device monitoring. \n- NetFlow is used for network traffic analysis but does not provide authentication or encryption by itself."
    },
    {
        "question": "Users are reporting issues with connecting to the wireless router. The technician discovers neighboring wireless APs that are not part of the network are on the same 5GHz frequency. Which of the following best describes the issue?",
        "options": [
            "Distance limitation",
            "Absorption",
            "Signal-to-noise ratio",
            "Interference"
        ],
        "correct_answer": 4,
        "description": "The correct answer is interference. Wireless networks can experience performance issues when nearby networks operate on the same frequency, causing signal overlap and interference. \n\n- Distance limitation affects signal strength but would not necessarily cause interference between networks. \n- Absorption refers to signal loss due to obstacles but does not address the presence of competing networks. \n- Signal-to-noise ratio (SNR) is a measure of signal clarity, but interference is the primary issue in this scenario."
    },
    {
        "question": "When a user makes a VoIP phone call and finishes speaking, the user experiences a delay in hearing a response. Which of the following should the network engineer check?",
        "options": [
            "Jitter",
            "Latency",
            "Bandwidth",
            "CRC errors"
        ],
        "correct_answer": 2,
        "description": "The correct answer is latency. Latency refers to the time delay in sending and receiving data over the network, which can cause delays in VoIP communications. \n\n- Jitter refers to variability in packet arrival times and can cause audio distortion but is less likely to cause consistent delays. \n- Bandwidth is related to the amount of data that can be transmitted but does not directly cause delays in response times. \n- CRC errors indicate data corruption, which would typically result in dropped calls or distorted audio, not delays."
    },
    {
        "question": "A network administrator needs to connect two network closets that are 492ft (150m) away from each other. Which of the following cable types should the administrator install between the closets?",
        "options": [
            "Single-mode fiber",
            "Coaxial",
            "DAC",
            "STP"
        ],
        "correct_answer": 1,
        "description": "The correct answer is single-mode fiber. This type of fiber optic cable is ideal for long-distance connections, as it supports high-speed data transmission over long distances, such as the 492ft (150m) distance in this case. \n\n- Coaxial cable is suitable for shorter distances and lower bandwidth requirements. \n- DAC (Direct Attach Copper) is typically used for short distances and lower-speed connections, not for 492ft distances. \n- STP (Shielded Twisted Pair) is suitable for shorter distances but does not offer the same performance as fiber optic cable over long distances."
    },
    {
        "question": "A systems administrator is investigating why users cannot reach a Linux web server with a browser but can ping the server IP. The server is online, the web server process is running, and the link to the switch is up. Which of the following commands should the administrator run on the server first?",
        "options": [
            "traceroute",
            "netstat",
            "tcpdump",
            "arp"
        ],
        "correct_answer": 3,
        "description": "The correct answer is tcpdump. This tool allows the administrator to capture and analyze network traffic, helping identify if the server is receiving HTTP requests and if any network issues are causing the browser to fail to load the page. \n\n- Traceroute helps trace the network path but is not useful for analyzing traffic on the server itself. \n- Netstat shows active connections but does not provide information about traffic reaching the server. \n- ARP is used for resolving IP addresses to MAC addresses, but it is not relevant to the issue of web server access."
    },





    {
        "question": "Which of the following disaster recovery metrics is used to describe the amount of data that is lost since the last backup?",
        "options": [
            "MTTR",
            "RTO",
            "RPO",
            "MTBF"
        ],
        "correct_answer": 3,
        "description": "The correct answer is RPO (Recovery Point Objective). RPO defines the maximum acceptable amount of data loss measured in time, typically from the last backup. \n\n- MTTR (Mean Time to Repair) is a metric for the time taken to repair a system. \n- RTO (Recovery Time Objective) is focused on the time it takes to restore the system, not data loss. \n- MTBF (Mean Time Between Failures) is the average time between failures of a system."
    },
    {
        "question": "Which of the following OSI model layers will ensure messages are transmitted to their destinations and no data is duplicated?",
        "options": [
            "Session",
            "Data link",
            "Network",
            "Transport"
        ],
        "correct_answer": 4,
        "description": "The correct answer is Transport. The Transport layer (Layer 4) ensures reliable data transmission, including error checking and flow control, ensuring data reaches its destination without duplication. \n\n- Session layer manages communication sessions, but it doesn’t handle reliable data delivery. \n- Data link layer is responsible for physical addressing and error detection but not reliability at the message level. \n- Network layer handles routing and addressing but not data reliability."
    },
    {
        "question": "A Wi-Fi network was recently deployed in a new, multilevel building. Several issues are now being reported related to latency and drops in coverage. Which of the following is the first step to troubleshoot the issues?",
        "options": [
            "Create a network diagram.",
            "Review the AP placement.",
            "Monitor channel utilization.",
            "Test cable attenuation."
        ],
        "correct_answer": 2,
        "description": "The correct answer is Review the AP placement. The placement of Access Points (APs) is critical for coverage and performance in multi-level buildings. Poor placement can cause coverage issues, latency, and dropped connections. \n\n- A network diagram is useful but doesn’t directly address coverage issues. \n- Monitoring channel utilization helps in congested networks but is secondary to ensuring proper AP placement. \n- Testing cable attenuation isn’t relevant to Wi-Fi issues unless there’s a physical cable problem."
    },
    {
        "question": "Users report that a database server responds slowly or drops connections to other servers at random during busy times. A technician notices the database and servers are connected to an access switch in the office. Which of the following should the technician do to improve the performance of the database server?",
        "options": [
            "Use different ports on the access switch.",
            "Implement LACP on the connection to the database server.",
            "Move the cable connection for users to the same switch as the database server.",
            "Move the server connection from the access switch to the core switch."
        ],
        "correct_answer": 4,
        "description": "The correct answer is Move the server connection from the access switch to the core switch. The core switch typically has higher capacity and better performance for handling server-to-server communication. \n\n- Using different ports may not solve congestion issues if the access switch is underperforming. \n- LACP (Link Aggregation Control Protocol) could help with bandwidth but doesn’t address the root cause if the access switch is overloaded. \n- Moving the user connection closer to the database server doesn’t address server-side network performance."
    },
    {
        "question": "An application is not working. When the log files are reviewed, the application continuously tries to reach the following destination: Destination: :1/128. Which of the following is most likely associated with this IP address?",
        "options": [
            "APIPA",
            "Default gateway",
            "Link local",
            "Loopback"
        ],
        "correct_answer": 4,
        "description": "The correct answer is Loopback. The IP address :1/128 is the IPv6 loopback address, which is used for testing network functionality within the same device. \n\n- APIPA (Automatic Private IP Addressing) is used when a device cannot obtain an IP address from a DHCP server. \n- Default gateway is used for routing traffic outside the local network. \n- Link local addresses are used for communication within a local network segment, but they are not the same as the loopback address."
    },
    {
        "question": "A technician wants to assign addresses to PCs on a subnet that uses IPv4 and IPv6. The DHCP server only supports IPv4. Which of the following can the technician use to assign IPv6 addresses without DHCP?",
        "options": [
            "SLAAC",
            "APIPA",
            "MAC reservation",
            "IPv4 to IPv6 tunnel"
        ],
        "correct_answer": 1,
        "description": "The correct answer is SLAAC (Stateless Address Autoconfiguration). SLAAC allows devices to automatically assign themselves an IPv6 address without needing a DHCP server. \n\n- APIPA is used for automatic IPv4 addressing when DHCP is not available. \n- MAC reservation is used for assigning static IP addresses to devices based on their MAC address, but it only works for IPv4. \n- IPv4 to IPv6 tunnel is used to tunnel IPv6 traffic over IPv4 networks, not for assigning IPv6 addresses."
    },
    {
        "question": "A network technician is troubleshooting an issue that involves connecting to a server via SSH. The server has one network interface that does not support subinterfaces. The technician runs a command on the server and receives the following output: Proto Local address Foreign address State TCP 0.0.0.0:22 0.0.0.0 LISTENING TCP 0.0.0.0:23 0.0.0.0 LISTENING TCP 0.0.0.0:443 0.0.0.0 LISTENING TCP 10.10.10.15:22 10.10.10.42:21231 ESTABLISHED On the host, the technician runs another command and receives the following: Destination Gateway Genmask Flags Iface default 31.242.12.9 0.0.0.0 UG eth0 192.168.1.0 0.0.0.0 255.255.255.0 UG eth1 Which of the following best explains the issue?",
        "options": [
            "A firewall is blocking access to the server.",
            "The server is plugged into a trunk port.",
            "The host does not have a route to the server.",
            "The server is not running the SSH daemon."
        ],
        "correct_answer": 3,
        "description": "The correct answer is The host does not have a route to the server. The output shows that the host does not have a proper route to reach the server's IP address, causing connectivity issues. \n\n- A firewall might block access, but there is no indication of a firewall-related issue in the output. \n- The server is not plugged into a trunk port, as there is no evidence of VLAN configuration issues. \n- The SSH daemon is running on the server, as evidenced by the LISTENING state for port 22."
    },
    {
    "question": "A network technician is configuring a new subnet on the distribution switch to support 15 network printers. Which of the following available subnets is the best choice to support all 15 printers on the LAN?",
    "options": [
        "10.1.15.0/27",
        "10.8.4.0/30",
        "10.10.8.0/28",
        "10.15.1.0/29"
    ],
    "correct_answer": 1,
    "description": "The correct answer is 10.1.15.0/27. This subnet provides 32 IP addresses (30 usable), which exceeds the requirement for 15 printers while allowing room for growth or additional devices. \n\n- 10.8.4.0/30 provides only 4 IP addresses (2 usable), which is insufficient for 15 printers. \n- 10.10.8.0/28 provides 16 IP addresses (14 usable), meeting the requirement but leaving no room for additional devices. \n- 10.15.1.0/29 provides 8 IP addresses (6 usable), which is not enough for 15 printers."
    },



    {
        "question": "A user is trying to reach an internet destination. A systems administrator thinks that packets are being dropped in transit. Which of the following command-line tools would confirm if the packets are being dropped?",
        "options": [
            "nslookup",
            "traceroute",
            "arp",
            "telnet"
        ],
        "correct_answer": 2,
        "description": "The correct answer is traceroute. This tool is used to trace the route that packets take from the source to the destination and identify where packets are being lost or delayed in transit. \n\n- nslookup is used to query DNS records, not for tracing packet loss. \n- arp is used for resolving IP addresses to MAC addresses and does not help in troubleshooting packet loss. \n- telnet is used for testing remote server connections and does not provide insights into packet loss."
    },
    {
        "question": "A security engineer wants to provide a secure, dedicated, alternate access method into an IT network infrastructure to administer connected devices and IT assets. Which of the following is the engineer most likely to implement?",
        "options": [
            "Remote desktop gateway",
            "Authentication and authorization controls",
            "Out-of-band management",
            "Secure Shell"
        ],
        "correct_answer": 3,
        "description": "The correct answer is out-of-band management. This method provides secure, dedicated access to network devices even when the primary network is unavailable. \n\n- Remote desktop gateway provides secure access to remote desktops but does not specifically address out-of-band management. \n- Authentication and authorization controls are important for security but do not directly provide a dedicated access method. \n- Secure Shell (SSH) is used for secure remote access but does not specifically address alternate access when network infrastructure is down."
    },
    {
        "question": "Which of the following network types is composed of computers that can all communicate with one another with equal permissions and allows users to directly share what is on or attached to their computers?",
        "options": [
            "Local area network",
            "Peer-to-peer network",
            "Client-server network",
            "Personal area network"
        ],
        "correct_answer": 2,
        "description": "The correct answer is peer-to-peer network. In a peer-to-peer network, all devices have equal access and can directly share resources with one another. \n\n- Local area network refers to a network of devices within a limited geographic area but does not specify the communication model. \n- Client-server network uses a server to manage resources and clients request services, so devices don't have equal permissions. \n- Personal area network typically refers to smaller networks, like Bluetooth, and is not designed for direct sharing of resources between multiple computers."
    },
    {
        "question": "A network technician is planning the infrastructure for a new data center that will support a 10GBASE-T network. Traffic in the data center is expected to be high, and data integrity is very important. Which of the following would the network technician most likely include in the plan?",
        "options": [
            "UTP plenum",
            "Cat 6a STP",
            "PoE injector",
            "Riser Cat 5e"
        ],
        "correct_answer": 2,
        "description": "The correct answer is Cat 6a STP. Cat 6a shielded twisted pair (STP) cabling is designed to support high data transfer rates like 10GBASE-T, and the shielding helps reduce electromagnetic interference, ensuring better data integrity. \n\n- UTP plenum refers to unshielded twisted pair cables designed for specific environments but lacks the shielding required for high-performance applications. \n- PoE injector is used to deliver power over Ethernet, but it doesn't relate to the cabling infrastructure needed for 10GBASE-T. \n- Riser Cat 5e is a lower-grade cable compared to Cat 6a and may not support high-speed 10GBASE-T connections effectively."
    },
    {
        "question": "A company that replicated the production environment in a cloud environment is starting to use a load balancer to evenly distribute requests between both environments. Which of the following does this scenario best describe?",
        "options": [
            "High availability",
            "NIC teaming",
            "FHRP",
            "Configuration backup"
        ],
        "correct_answer": 1,
        "description": "The correct answer is high availability. The use of a load balancer to distribute requests between replicated environments ensures that the service remains available even if one environment fails. \n\n- NIC teaming refers to combining multiple network interfaces for redundancy or increased bandwidth, but it does not describe the load balancing across replicated environments. \n- FHRP (First Hop Redundancy Protocol) is used to provide fault tolerance for network gateways, not for distributing requests across multiple environments. \n- Configuration backup ensures that configurations are saved, but it does not describe the load balancing of active requests."
    },
    {
        "question": "Which of the following documents dictates the uptimes that were agreed upon by the involved parties?",
        "options": [
            "MOU",
            "BYOD",
            "SLA",
            "NDA"
        ],
        "correct_answer": 3,
        "description": "The correct answer is SLA (Service Level Agreement). An SLA is a contract that outlines the expected uptime and performance standards agreed upon by the service provider and the customer. \n\n- MOU (Memorandum of Understanding) is an agreement between parties, but it does not typically detail service levels or uptimes. \n- BYOD (Bring Your Own Device) policy refers to guidelines around personal device usage in a corporate environment and does not address uptime. \n- NDA (Non-Disclosure Agreement) is a legal contract focused on protecting confidential information, not service uptime."
    },
    {
        "question": "Which of the following attacks can be effectively protected against by using techniques to check if a connection was made by a human user? (Choose two.)",
        "options": [
            "Brute-force",
            "Dictionary",
            "On-path attack",
            "Phishing",
            "Shoulder surfing",
            "Evil twin"
        ],
        "correct_answer": [1, 4],
        "description": "The correct answers are brute-force and phishing. Techniques such as CAPTCHAs or behavioral analysis can help distinguish human users from automated attacks, making it harder for brute-force or phishing attacks to succeed. \n\n- Dictionary attacks rely on trying many passwords from a predefined list, and although checking for human interaction can help, it is not the primary defense. \n- On-path attacks involve intercepting communications and are not necessarily stopped by checking human users. \n- Shoulder surfing is a physical attack where an attacker observes someone entering sensitive information, which is not directly related to human verification methods. \n- Evil twin attacks involve rogue access points and do not directly relate to checking for human user connections."
    },
    {
        "question": "A network administrator is investigating a network connectivity issue. The administrator runs a command to view the status of the network cards. The administrator receives the following output: RX packets:45332 errors: 45332 dropped:0 overruns 0 frame:0. Which of the following should the administrator troubleshoot based on the output?",
        "options": [
            "Physical layer components",
            "VLAN tagging configuration",
            "Buffers on the card filling up",
            "TCP/IP address settings"
        ],
        "correct_answer": 1,
        "description": "The correct answer is physical layer components. The fact that both packets sent and errors are the same suggests a potential issue with the physical layer, such as faulty cables or a bad network interface card (NIC). \n\n- VLAN tagging configuration would not typically cause errors in received packets without affecting dropped packets. \n- Buffers filling up would cause dropped packets, but in this case, no packets are dropped. \n- TCP/IP address settings are not relevant to the packet errors shown."
    },
    {
        "question": "Which of the following records is the main type in a reverse DNS lookup zone?",
        "options": [
            "PTR",
            "AAAA",
            "CNAME",
            "TXT"
        ],
        "correct_answer": 1,
        "description": "The correct answer is PTR. PTR (Pointer) records are used in reverse DNS lookups to map an IP address to a domain name. \n\n- AAAA records are used to map IPv6 addresses to domain names. \n- CNAME records are used for aliasing domain names. \n- TXT records are used to store arbitrary text in DNS records, but not for reverse lookups."
    },
    {
        "question": "Which of the following policies would be best to refer to when trying to prevent a disgruntled employee from copying sensitive materials off company servers after termination?",
        "options": [
            "Incident response plan",
            "Offboarding",
            "Change management",
            "Acceptable use"
        ],
        "correct_answer": 2,
        "description": "The correct answer is offboarding. An offboarding policy includes processes to ensure that terminated employees no longer have access to company resources and that all sensitive data is protected. \n\n- Incident response plan addresses responses to security incidents, not specifically employee terminations. \n- Change management refers to processes for handling changes in IT systems but does not deal with employee terminations. \n- Acceptable use policy outlines what employees are allowed to do with company resources but does not focus on post-termination access."
    },


    {
        "question": "Which of the following routing protocols uses attributes to select the best path?",
        "options": [
            "EIGRP",
            "BGP",
            "OSPF",
            "RIP"
        ],
        "correct_answer": 2,
        "description": "The correct answer is BGP (Border Gateway Protocol). BGP is a path vector protocol that uses attributes such as AS path, next-hop, and local preference to determine the best path. \n\n- EIGRP uses a distance-vector algorithm and is not based solely on attributes like BGP. \n- OSPF uses link-state information and does not use path attributes to select routes. \n- RIP is based on hop count and does not use attributes for route selection."
    },
    {
        "question": "Which of the following is most closely associated with the management plane?",
        "options": [
            "Routing table",
            "Current configuration",
            "File operations",
            "Console port"
        ],
        "correct_answer": 4,
        "description": "The correct answer is Console port. The management plane controls the management functions of the network devices, including configuration and troubleshooting. The console port provides direct access to manage a device. \n\n- Routing table is associated with the data plane. \n- Current configuration refers to settings, which are part of the management plane but not as closely associated as the console port. \n- File operations are related to the storage or file system, not management plane functions."
    },
    {
        "question": "A technician is working on a ticket for a user in the human resources department who received a new PC that does not connect to the internet. All users in human resources can access the internet. The technician can ping the PC from the human resources router but not from the IT network. Which of the following is the most likely cause of the issue?",
        "options": [
            "Duplicate IP address",
            "Misconfigured RIP",
            "Improper VLAN assignment",
            "Incorrect default gateway"
        ],
        "correct_answer": 3,
        "description": "The correct answer is Improper VLAN assignment. Since the technician can ping the PC from the human resources router, it suggests the PC is connected to the correct network but is not properly configured to communicate with the IT network. \n\n- A duplicate IP address would cause a more widespread network issue. \n- Misconfigured RIP would affect routing but is unlikely to cause the specific issue described. \n- Incorrect default gateway could lead to connectivity issues, but improper VLAN assignment is the most likely cause given the symptoms."
    },
    {
        "question": "A local company is planning to upgrade its current wireless network solution to achieve better performance and improve employees' experience. The solution will require a 5GHz radio band to support all current company devices. Which of the following should be considered as an option for the upgrade?",
        "options": [
            "802.11",
            "802.11b",
            "802.11n",
            "802.11g"
        ],
        "correct_answer": 3,
        "description": "The correct answer is 802.11n. 802.11n supports both 2.4GHz and 5GHz frequencies, offering better performance, higher throughput, and greater range compared to older standards. \n\n- 802.11 and 802.11b are outdated standards and do not support 5GHz. \n- 802.11g supports 2.4GHz but does not provide the improved performance and range of 802.11n, especially on 5GHz."
    },
    {
        "question": "Which of the following is a hybrid routing protocol?",
        "options": [
            "BGP",
            "RIPv2",
            "OSPF",
            "EIGRP"
        ],
        "correct_answer": 4,
        "description": "The correct answer is EIGRP (Enhanced Interior Gateway Routing Protocol). EIGRP is a hybrid routing protocol, combining characteristics of both distance-vector and link-state protocols. \n\n- BGP is a path vector protocol, not hybrid. \n- RIPv2 is a distance-vector protocol. \n- OSPF is a link-state protocol."
    },
    {
        "question": "Which of the following describes a situation in which an employee knowingly allows someone access to a restricted area without verifying authentication?",
        "options": [
            "Piggybacking",
            "Tailgating",
            "Shoulder surfing",
            "Phishing"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Piggybacking. Piggybacking refers to the act of allowing someone to follow an authorized person into a restricted area, typically without verification. \n\n- Tailgating is similar but involves following someone without their knowledge or consent. \n- Shoulder surfing involves observing someone’s activities, usually to steal information. \n- Phishing is a social engineering attack that typically involves deceiving users into revealing credentials."
    },
    {
        "question": "An engineer is concerned about date and time synchronization across networked devices. Which of the following should be used to address this concern?",
        "options": [
            "NTP",
            "SIP",
            "IMAP",
            "SMB"
        ],
        "correct_answer": 1,
        "description": "The correct answer is NTP (Network Time Protocol). NTP ensures that all networked devices maintain synchronized clocks, which is crucial for accurate logging, scheduling, and coordination. \n\n- SIP is a protocol used in voice communication, not for time synchronization. \n- IMAP is used for email retrieval, and SMB is a file-sharing protocol, neither of which address time synchronization."
    },
    {
        "question": "A network administrator is setting up a web-based application for a company. The application needs to be continually accessible to all end users. Which of the following would best ensure this need is fulfilled?",
        "options": [
            "NIC teaming",
            "Cold site",
            "Snapshots",
            "High availability"
        ],
        "correct_answer": 4,
        "description": "The correct answer is High availability. High availability ensures that the application remains accessible even in the event of a failure, by providing redundancy and failover mechanisms. \n\n- NIC teaming provides redundancy for network interfaces but is not focused on application availability. \n- Cold sites are disaster recovery sites that are not equipped to ensure continuous service. \n- Snapshots capture the state of a system at a particular point in time but do not ensure continuous access."
    },
    {
        "question": "Users report that the network is slower than usual when accessing on-premises email. Which of the following should a network technician do to confirm the issue?",
        "options": [
            "Review the logging levels of network devices.",
            "Check the audit logs to see if users are accessing email.",
            "Compare the network baselines to the current network status.",
            "Verify that users who are trying to access email have LDAP accounts."
        ],
        "correct_answer": 3,
        "description": "The correct answer is Compare the network baselines to the current network status. Comparing the current network performance to a baseline allows the technician to identify if the network is operating outside normal parameters, which could explain the slowdown. \n\n- Reviewing logging levels might provide some insight but is less direct than comparing performance metrics. \n- Checking audit logs for user activity does not directly address network speed issues. \n- Verifying LDAP accounts is unrelated to network performance issues."
    },
    {
        "question": "A technician just validated a theory that resolved a network outage. The technician then verified that all users could access resources. Which of the following is the next step the technician should take in the network troubleshooting methodology?",
        "options": [
            "Verify the services are restored.",
            "Test a new theory.",
            "Write the lessons learned.",
            "Identify where the network outage is occurring."
        ],
        "correct_answer": 1,
        "description": "The correct answer is Verify the services are restored. After confirming that users can access resources, the technician should ensure that all services are fully operational and that the issue is completely resolved. \n\n- Testing a new theory is not necessary after confirming that the issue has been resolved. \n- Writing lessons learned is important but comes after confirming full resolution. \n- Identifying where the outage occurred has already been addressed in the previous troubleshooting steps."
    },




    {
        "question": "A company’s cloud model consists of the following:\n• An on-premises data center\n• An IaaS cloud provider\n• A private-direct connection from on premises to IaaS\nWhich of the following best describes the deployment model the company is using?",
        "options": [
            "Public",
            "Private",
            "Hybrid",
            "Community"
        ],
        "correct_answer": 3,
        "description": "The correct answer is Hybrid. This deployment model combines both on-premises infrastructure with cloud-based resources. \n\n- Public is a cloud model where services are provided over the public internet, not involving on-premises infrastructure. \n- Private cloud refers to an infrastructure dedicated solely to a single organization, without integration to public cloud services. \n- Community cloud is shared by several organizations with common goals but does not fit the scenario where both on-premises and IaaS are integrated."
    },
    {
        "question": "A network technician is troubleshooting a port channel issue. When logging in to one of the switches, the technician sees the following information displayed:\nNative VLAN mismatch detected on interface g0/1\nWhich of the following layers of the OSI model is most likely to be where the issue resides?",
        "options": [
            "Layer 2",
            "Layer 3",
            "Layer 5",
            "Layer 6"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Layer 2. VLAN mismatches are related to Layer 2 issues, which deal with data link protocols such as Ethernet. \n\n- Layer 3 refers to IP routing, and the issue is not related to routing. \n- Layer 5 (Session) and Layer 6 (Presentation) handle session management and data formatting, which do not apply to VLAN mismatches."
    },
    {
        "question": "A network engineer installed a new fiber uplink for an office and wants to make sure that the link meets throughput requirements. Which of the following tools should the engineer use to verify that the new link is sufficient?",
        "options": [
            "tcpdump",
            "ping",
            "iperf",
            "netstat"
        ],
        "correct_answer": 3,
        "description": "The correct answer is iperf. It is used to test and measure network throughput between two endpoints. \n\n- tcpdump is a packet capture tool, useful for analyzing traffic but not for measuring throughput. \n- ping checks basic network connectivity, but it does not provide throughput measurements. \n- netstat provides network statistics, but it does not measure throughput."
    },
    {
        "question": "A network technician has identified a breach and is attempting to determine how the attacker connected to a device on the network. The technician uses tcpdump to perform a port scan and receives the following result:\n\n0.10.10.19:9444  10.10.10.44:59824  SYN-ACK\n10.10.10.19:24123  10.10.10.51:22    SYN\n10.10.10.51:22     10.10.10.19:24123  SYN-ACK\n10.10.10.19:52091  10.10.10.51:23    SYN\n10.10.10.51:23     10.10.10.19:52091  RST\n10.10.10.19:42786  10.10.10.51:3389   SYN\n10.10.10.19:42787  10.10.10.51:3389   SYN\n10.10.10.44:59824  10.10.10.19:9444   SYN-ACK\n\nWhich of the following describes how the attacker connected to the device?",
        "options": [
            "The attacker used Telnet.",
            "The attacker used VNC.",
            "The attacker used SSH.",
            "The attacker used RDP."
        ],
        "correct_answer": 4,
        "description": "The correct answer is RDP. The evidence of SYN packets on port 3389 indicates Remote Desktop Protocol (RDP) traffic. \n\n- Telnet uses port 23, but there is no evidence of Telnet traffic in the capture. \n- VNC typically uses ports 5900+ for remote desktop connections, not port 3389. \n- SSH uses port 22, which is seen in the capture, but the primary connection is on port 3389 (RDP)."
    },
    {
        "question": "A software developer changed positions within a company and is now a sales engineer. The security team discovered that the former software developer had been modifying code to implement small features requested by customers. Which of the following would be the best thing for the security administrator to implement to prevent this from happening?",
        "options": [
            "A software patching policy",
            "A role-based access control policy",
            "Firewalls on the software development servers",
            "Longer and more complex password requirements"
        ],
        "correct_answer": 2,
        "description": "The correct answer is a role-based access control policy. This ensures that employees only have access to the resources they need based on their role. \n\n- A software patching policy is important for security but does not address the issue of unauthorized code modification. \n- Firewalls protect networks but do not directly limit access to code modification. \n- Password policies are important for security, but they do not prevent unauthorized actions by someone with the right access."
    },
    {
        "question": "An IT intern moved the location of a WAP from one conference room to another. The WAP was unable to boot following the move. Which of the following should be used to fix the issue?",
        "options": [
            "Antenna",
            "WLAN controller",
            "Media converter",
            "PoE injector"
        ],
        "correct_answer": 4,
        "description": "The correct answer is PoE injector. Power over Ethernet (PoE) is used to power WAPs through the Ethernet cable, and it may not have been properly connected after the move. \n\n- Antenna is needed for signal propagation, but the issue seems to be power-related. \n- WLAN controller manages wireless settings but does not provide power to the device. \n- Media converter is used for different media types but is not related to WAP power issues."
    },
    {
        "question": "A trusted vendor emailed a security advisory to an engineer. The advisory listed publicly disclosed security issues and resolutions for the vendor's installed network devices. Which of the following describes this security concept?",
        "options": [
            "CVE",
            "Exploits",
            "Zero day",
            "SSO"
        ],
        "correct_answer": 1,
        "description": "The correct answer is CVE (Common Vulnerabilities and Exposures). CVEs are publicly disclosed security vulnerabilities and provide resolutions. \n\n- Exploits refer to the code or techniques used to take advantage of vulnerabilities. \n- Zero day refers to vulnerabilities that are unknown to the vendor and have no patch, unlike publicly disclosed CVEs. \n- SSO (Single Sign-On) is an authentication method, not a vulnerability concept."
    },
    {
        "question": "A network technician for a bank configured a WLAN that provides good coverage. Bank employees are now reporting Wi-Fi issues when the microwave in the lunch room area is used. Which of the following frequencies should the technician use to minimize interference?",
        "options": [
            "2.4GHz",
            "5MHz",
            "5GHz",
            "700MHz"
        ],
        "correct_answer": 3,
        "description": "The correct answer is 5GHz. The 5GHz frequency is less susceptible to interference from microwave ovens, which typically interfere with the 2.4GHz range. \n\n- 2.4GHz is more prone to interference from microwaves. \n- 5MHz is not a valid frequency for WLANs. \n- 700MHz is used for different types of wireless communication and is not suitable for WLANs."
    },
    {
        "question": "A technician is configuring a wireless access point in a public space for guests to use. Which of the following should the technician configure so that only approved connections are allowed?",
        "options": [
            "Geofencing",
            "Captive portal",
            "Secure SNMP",
            "Private VLANs"
        ],
        "correct_answer": 2,
        "description": "The correct answer is Captive portal. This allows users to authenticate or accept terms before accessing the network. \n\n- Geofencing is used for location-based services, not for controlling network access. \n- Secure SNMP is for managing network devices and does not control user access. \n- Private VLANs isolate traffic within a network but do not authenticate users."
    },
    {
        "question": "A network technician added a new workstation to the network and needs to make a custom, shielded cable that is 492ft (150m) with both ends wired to TIA/EIA-568A standards. The workstation is not establishing a link to the switchport. Which of the following is the cause of the issue?",
        "options": [
            "Cable shielding",
            "Attenuation",
            "Incorrect pinout",
            "Near-end crosstalk"
        ],
        "correct_answer": 2,
        "description": "The correct answer is Attenuation. Over long distances, signal degradation (attenuation) occurs, which can prevent a link from being established. \n\n- Cable shielding protects against electromagnetic interference but is not the primary issue in this case. \n- Incorrect pinout would cause a direct wiring issue, but the cable is wired correctly. \n- Near-end crosstalk is related to interference but does not explain the lack of a link over a long distance."
    },



    {
        "question": "Users in a remote office report that corporate web server pages are taking a long time to load, whereas users in the main corporate office do not have any issues. Which of the following is the best metric for a network administrator to check?",
        "options": [
            "Jitter across the network.",
            "Hop-by-hop network latency.",
            "Server interface CRC errors.",
            "Server NetFlow data."
        ],
        "correct_answer": 2,
        "description": "The correct answer is hop-by-hop network latency. This metric allows the network administrator to identify delays across the network path, helping to pinpoint where the slowdown occurs. \n\n- Jitter measures variations in latency, which could be less useful for understanding slow page loading. \n- Server interface CRC errors indicate issues with the physical layer but don't directly explain latency. \n- Server NetFlow data provides traffic insights but is not focused on pinpointing latency-related issues."
    },
    {
        "question": "In which of the following locations is a VPN headend found?",
        "options": [
            "Distribution",
            "Access",
            "Core",
            "WAN edge"
        ],
        "correct_answer": 4,
        "description": "The correct answer is WAN edge. A VPN headend is typically located at the WAN edge, where the company's network interfaces with the external network, providing secure access to remote users. \n\n- The distribution and core layers of a network are primarily concerned with internal traffic routing and not directly with remote access. \n- Access refers to the point where users connect to the network but not where the VPN headend is typically deployed."
    },
    {
        "question": "A user returns to the office after working remotely for an extended period. The user is reporting limited access to the office wireless network and the inability to reach company resources on the network. The user connected to the guest network, ensured all patches were applied, and checked to make sure software was up to date. Which of the following is most likely the cause of the issue?",
        "options": [
            "The laptop drivers need to be updated to support a new wireless infrastructure.",
            "The wireless passphrase has been cycled and needs to be updated.",
            "The NAC appliance has labeled the laptop as non-compliant.",
            "The WAP transmit power is too low and cannot complete user authentication."
        ],
        "correct_answer": 3,
        "description": "The correct answer is the NAC appliance has labeled the laptop as non-compliant. Network Access Control (NAC) systems often enforce compliance policies and may block access to the network if the device doesn't meet security standards. \n\n- Updating the laptop drivers may not resolve access issues if the device is labeled as non-compliant by NAC. \n- The wireless passphrase could be an issue, but this would typically affect all users and not just a single device. \n- Low WAP transmit power might affect signal strength but wouldn't directly cause the device to be non-compliant."
    },
    {
        "question": "A consultant is working with two international companies. The companies will be sharing cloud resources for a project. Which of the following documents would provide an agreement on how to utilize the resources?",
        "options": [
            "MOU",
            "NDA",
            "AUP",
            "SLA"
        ],
        "correct_answer": 1,
        "description": "The correct answer is MOU (Memorandum of Understanding). An MOU outlines the terms of collaboration and resource sharing between organizations. \n\n- An NDA (Non-Disclosure Agreement) focuses on confidentiality but doesn't specify resource usage. \n- An AUP (Acceptable Use Policy) defines acceptable usage of resources but doesn't focus on intercompany collaboration. \n- An SLA (Service Level Agreement) specifies the level of service but is not the right document for outlining resource-sharing terms."
    },
    {
        "question": "A technician is investigating an intermittent connectivity issue that occurs when specific WAPs are turned on. The technician checks into the issue further and finds the WAPs that are having issues share channel five. Which of the following is most likely causing the issue?",
        "options": [
            "Polarization",
            "Interference",
            "Incorrect channel",
            "Low power levels"
        ],
        "correct_answer": 2,
        "description": "The correct answer is interference. Wi-Fi channels can experience interference, especially if multiple WAPs are on the same channel, causing intermittent connectivity issues. \n\n- Polarization relates to antenna alignment and would not cause interference in this context. \n- Incorrect channels can cause issues but are less likely if the WAPs are using the same channel correctly. \n- Low power levels would cause weak signal issues but not the intermittent connectivity specifically observed when turning on WAPs."
    },
    {
        "question": "Which of the following attacks is typically used to guess a password?",
        "options": [
            "Brute-force",
            "DDoS",
            "DNS poisoning",
            "Rogue DHCP",
            "Ransomware"
        ],
        "correct_answer": 1,
        "description": "The correct answer is brute-force. A brute-force attack involves systematically guessing all possible passwords until the correct one is found. \n\n- DDoS (Distributed Denial of Service) targets network resources, not password guessing. \n- DNS poisoning involves corrupting the DNS cache, not guessing passwords. \n- Rogue DHCP and ransomware do not focus on password guessing either."
    },
    {
        "question": "A company is undergoing expansion but does not have sufficient rack space in its data center. Which of the following would be best to allow the company to host its new equipment without major investment in facilities?",
        "options": [
            "Using a colocation service",
            "Using available rack space in branch offices",
            "Using a flat network topology",
            "Reorganizing the network rack and installing top-of-rack switching"
        ],
        "correct_answer": 1,
        "description": "The correct answer is using a colocation service. Colocation allows the company to host its equipment in a third-party data center, saving costs on facility expansion. \n\n- Using branch office rack space could complicate network management and create security concerns. \n- A flat network topology does not address the need for physical space. \n- Reorganizing the rack may provide short-term relief but doesn't solve the long-term space issue."
    },
    {
        "question": "Which of the following is the most accurate NTP time source that is capable of being accessed across a network connection?",
        "options": [
            "Stratum 0 device",
            "Stratum 1 device",
            "Stratum 7 device",
            "Stratum 16 device"
        ],
        "correct_answer": 2,
        "description": "The correct answer is Stratum 1 device. Stratum 1 devices are directly connected to a highly accurate time source (such as an atomic clock) and are accessible across a network. \n\n- Stratum 0 devices are highly accurate but are not network-accessible. \n- Stratum 7 and Stratum 16 devices are further from the time source and are less accurate."
    },
    {
        "question": "A user cannot connect to the network, although others in the office are unaffected. The network technician sees that the link lights on the NIC are not on. The technician needs to check which switchport the user is connected to, but the cabling is not labeled. Which of the following is the best way for the technician to find where the computer is connected?",
        "options": [
            "Look up the computer's IP address in the switch ARP table.",
            "Use a cable tester to trace the cable.",
            "Look up the computer's MAC address in the switch CAM table.",
            "Use a tone generator to trace the cable."
        ],
        "correct_answer": 3,
        "description": "The correct answer is look up the computer's MAC address in the switch CAM table. The switch CAM table (Content Addressable Memory) maps MAC addresses to switch ports, making it the quickest way to locate where the computer is connected. \n\n- Looking up the IP address in the ARP table could work, but MAC address is a more direct approach. \n- A cable tester or tone generator are tools for physical cable tracing, but using the switch's table is more efficient."
    },
    {
        "question": "Which of the following policies outlines the software and hardware requirements for using personally owned devices to conduct business?",
        "options": [
            "DLP",
            "AUP",
            "BYOD",
            "NDA"
        ],
        "correct_answer": 3,
        "description": "The correct answer is BYOD (Bring Your Own Device). A BYOD policy outlines the requirements for using personal devices for business purposes, including both software and hardware guidelines. \n\n- DLP (Data Loss Prevention) deals with protecting sensitive data, not personal device usage. \n- AUP (Acceptable Use Policy) covers general usage rules but doesn't specifically focus on personal devices. \n- NDA (Non-Disclosure Agreement) relates to confidentiality, not device policies."
    },


#801-850



    {
        "question": "Which of the following should be used to manage outside cables that need to be routed to various multimode uplinks?",
        "options": [
            "Fiber distribution panel",
            "110 punchdown block",
            "PDU",
            "TIA/EIA-568A patch bay",
            "Cat 6 patch panel"
        ],
        "correct_answer": 1,
        "description": "The correct answer is fiber distribution panel. This panel is designed to organize and manage fiber optic cables, especially in situations where cables need to be routed to multimode uplinks. \n\n- A 110 punchdown block is used for terminating twisted pair cables, not fiber cables. \n- A PDU (Power Distribution Unit) is used for power management, not cable organization. \n- The TIA/EIA-568A patch bay is for organizing twisted pair cables, not fiber optic cables. \n- A Cat 6 patch panel is for Ethernet connections and is not suited for managing fiber optic cables."
    },
    {
        "question": "Staff members notify a network technician that the wireless network is not working as expected and connectivity to wireless devices is intermittent. Some devices connect but then disconnect. The technician reviews the logs on the WAP controller and identifies thousands of connection attempts from unrecognized devices within a short amount of time. Which of the following is the most likely reason for the wireless network connectivity issue?",
        "options": [
            "Wrong SSID",
            "Denial of service",
            "Interference",
            "Poor coverage"
        ],
        "correct_answer": 2,
        "description": "The correct answer is denial of service. The large number of connection attempts from unrecognized devices indicates a denial of service (DoS) attack, where the attacker floods the network with connection requests, causing disruption. \n\n- Wrong SSID would cause devices to be unable to connect, but would not lead to intermittent connectivity issues. \n- Interference can cause connectivity issues but would not result in unrecognized device attempts in the logs. \n- Poor coverage would result in intermittent connectivity but not in a high number of connection attempts from unrecognized devices."
    },
    {
        "question": "A user is connecting a smartwatch to a smartphone for internet access. Which of the following network types is the user employing?",
        "options": [
            "MAN",
            "PAN",
            "LAN",
            "WLAN"
        ],
        "correct_answer": 2,
        "description": "The correct answer is PAN (Personal Area Network). A PAN is a small network designed to connect devices in close proximity, such as a smartwatch and smartphone. \n\n- MAN (Metropolitan Area Network) is a larger network covering a city or region, not suitable for this scenario. \n- LAN (Local Area Network) is a network within a building or campus, but a PAN is more appropriate for connecting personal devices. \n- WLAN (Wireless Local Area Network) refers to wireless networks in a local area, but the focus here is on the personal connection between the smartwatch and smartphone."
    },
    {
        "question": "An online gaming company needs a cloud solution that will allow for more virtual resources to be deployed when tournaments are held. The number of users who access the service increases during tournaments. The company also needs the resources to return to baseline levels once the resources are not needed in order to reduce cost. Which of the following cloud concepts would provide the best solution?",
        "options": [
            "Scalability",
            "Hybrid",
            "Multitenancy",
            "Elasticity"
        ],
        "correct_answer": 4,
        "description": "The correct answer is elasticity. Elasticity in cloud computing refers to the ability to scale resources up or down quickly based on demand, making it ideal for the gaming company's needs. \n\n- Scalability refers to the ability to increase capacity, but elasticity specifically focuses on dynamic adjustments to resource levels. \n- Hybrid cloud solutions involve both on-premises and cloud resources, which may not address the need for quick resource scaling. \n- Multitenancy refers to the sharing of cloud resources among multiple users but does not address the need for dynamic resource allocation."
    },
    {
        "question": "A technician reviews a network performance report and finds a high level of collisions happening on the network. At which of the following layers of the OSI model would these collisions be found?",
        "options": [
            "Layer 1",
            "Layer 3",
            "Layer 4",
            "Layer 7"
        ],
        "correct_answer": 1,
        "description": "The correct answer is Layer 1. Collisions typically occur at Layer 1 (Physical layer) of the OSI model, where devices are transmitting data over the network medium. \n\n- Layer 3 (Network layer) deals with routing and IP addressing, not collisions. \n- Layer 4 (Transport layer) handles end-to-end communication and error handling, but not physical collisions. \n- Layer 7 (Application layer) involves high-level data interactions, not the physical transmission of data."
    },
    {
        "question": "An attacker is using an unknown vulnerability that allows malicious actors to utilize the print spooler to gain system privileges on a computer. Which of the following is this scenario an example of?",
        "options": [
            "Honeypot",
            "Zero-day attack",
            "Internal threat",
            "External threat"
        ],
        "correct_answer": 2,
        "description": "The correct answer is a zero-day attack. This type of attack targets vulnerabilities that are unknown to the software vendor, making them particularly dangerous. \n\n- A honeypot is a decoy system designed to attract attackers, not a real security threat. \n- An internal threat involves malicious actions from within an organization, but this attack involves an unknown vulnerability, not an insider. \n- An external threat comes from outside the organization, but the term 'zero-day' better describes the nature of this attack."
    },
    {
        "question": "Which of the following is the first step to troubleshoot a network issue?",
        "options": [
            "Identify the problem",
            "Document the findings",
            "Establish a theory of probable cause",
            "Test the theory to determine the cause"
        ],
        "correct_answer": 1,
        "description": "The correct answer is to identify the problem. Before troubleshooting, the technician needs to fully understand the issue by gathering information. \n\n- Documenting findings comes after identifying the problem and is part of the process of resolving it. \n- Establishing a theory comes after identifying the problem. \n- Testing the theory is the next step after establishing the cause."
    },
    {
        "question": "A network security engineer is investigating a potentially malicious insider on the network. The network security engineer would like to view all traffic coming from the user's PC to the switch without interrupting any traffic or having any downtime. Which of the following should the network security engineer do?",
        "options": [
            "Turn on port security",
            "Implement dynamic ARP inspection",
            "Configure 802.1Q",
            "Enable port mirroring"
        ],
        "correct_answer": 4,
        "description": "The correct answer is enabling port mirroring. Port mirroring allows a network security engineer to monitor traffic on a specific port without interrupting the network's traffic flow. \n\n- Turning on port security helps to secure a port but does not allow for monitoring traffic. \n- Dynamic ARP inspection helps detect ARP spoofing but is not designed for monitoring traffic. \n- Configuring 802.1Q is for VLAN tagging, not monitoring traffic."
    },
    {
        "question": "Which of the following is most closely associated with attempting to actively prevent network intrusion?",
        "options": [
            "IDS",
            "Firewall",
            "IPS",
            "VPN"
        ],
        "correct_answer": 3,
        "description": "The correct answer is IPS (Intrusion Prevention System). An IPS actively monitors network traffic and can block malicious activity in real time. \n\n- IDS (Intrusion Detection System) detects potential threats but does not prevent them. \n- A firewall is primarily used to block unauthorized access but does not specifically monitor or block malicious network activity. \n- A VPN (Virtual Private Network) encrypts traffic but does not prevent intrusion attempts."
    },
    {
        "question": "A network administrator connects two unmanaged switches together with a straight-through Ethernet cable. The administrator reviews the connection and notices that the uplinks are not on. Which of the following options offers the best solution for the issue?",
        "options": [
            "A rollover cable needs to be used",
            "The switches needs to be rebooted after connecting",
            "The ports need to be enabled",
            "The ports need the IP address configured",
            "A crossover cable needs to be used"
        ],
        "correct_answer": 5,
        "description": "The correct answer is a crossover cable. When connecting two switches directly, a crossover cable is required to ensure correct transmission and reception of data. \n\n- A rollover cable is used for console connections, not for connecting switches. \n- Rebooting the switches is unnecessary if the correct cable is used. \n- Enabling ports is important but would not resolve the issue of incorrect cabling. \n- Assigning an IP address is unnecessary for direct switch-to-switch connections."
    },




    {
        "question": "A network administrator has been assigned to a team that is currently troubleshooting a large-scale outage. The network administrator makes some configuration changes to an on-premises router to see if the link comes up. Which of the following troubleshooting stages is described in this scenario?",
        "options": [
            "Establish a theory of probable cause.",
            "Verify full system functionality.",
            "Establish a plan of action to resolve the problem.",
            "Test the theory to determine the cause."
        ],
        "correct_answer": 4,
        "description": "The correct answer is 'Test the theory to determine the cause.' The administrator is testing the configuration changes to see if the issue is resolved, which is a key part of testing the theory of what may be causing the outage. \n\n- Establishing a theory of probable cause would have been done before this step. \n- Verifying system functionality comes after testing and confirming the issue has been addressed. \n- Establishing a plan of action typically happens after identifying the cause."
    },
    {
        "question": "A company is implementing a secure remote access solution for multiple employees. Which of the following should the company use?",
        "options": [
            "Remote desktop connection",
            "Virtual desktop",
            "Site-to-site VPN",
            "Client-to-site VPN"
        ],
        "correct_answer": 4,
        "description": "The correct answer is 'Client-to-site VPN.' This type of VPN is designed to allow individual remote users to securely access the company network. \n\n- Remote desktop connection provides access to a specific computer, not the entire network. \n- Virtual desktops offer desktop environments but may not be suitable for all remote access needs. \n- Site-to-site VPN connects entire networks, not individual users."
    },
    {
        "question": "A user wants to avoid using a password to access a third-party website. Which of the following does the user need in order to allow this type of access to the third-party website?",
        "options": [
            "Multifactor",
            "RADIUS",
            "SSO",
            "Local authentication"
        ],
        "correct_answer": 3,
        "description": "The correct answer is 'SSO' (Single Sign-On). SSO allows users to access multiple applications with a single authentication process, eliminating the need to remember passwords for each service. \n\n- Multifactor authentication requires multiple verification steps but does not eliminate password use. \n- RADIUS is an authentication protocol, not a solution for avoiding passwords. \n- Local authentication is specific to a device, not web services."
    },
    {
        "question": "Which of the following is required for hosts to receive DHCP addresses from a server that is located on a different subnet?",
        "options": [
            "DHCP scope",
            "DHCP snooping",
            "DHCP reservations",
            "DHCP relay"
        ],
        "correct_answer": 4,
        "description": "The correct answer is 'DHCP relay.' A DHCP relay allows DHCP requests to be forwarded from clients on one subnet to a DHCP server on a different subnet. \n\n- DHCP scope is a range of IP addresses assigned by a DHCP server, not related to cross-subnet communication. \n- DHCP snooping is a security feature to prevent rogue DHCP servers. \n- DHCP reservations are for specific IP addresses, not cross-subnet functionality."
    },
    {
        "question": "A network engineer needs to change an entire subnet of SLAAC-configured workstation addresses. Which of the following methods would be the best for the engineer to use?",
        "options": [
            "Change the address prefix in ARP in order for the workstations to retrieve their new addresses.",
            "Change the address prefix in a router in order for the router to advertise the new prefix with an ND.",
            "Change the address prefix scope in a DHCP server in order for the workstations to retrieve their new addresses.",
            "Change the workstations’ address prefix manually because an automated method does not exist."
        ],
        "correct_answer": 2,
        "description": "The correct answer is 'Change the address prefix in a router in order for the router to advertise the new prefix with an ND (Neighbor Discovery Protocol).' SLAAC (Stateless Address Autoconfiguration) relies on routers to advertise address prefixes. \n\n- Changing the ARP (Address Resolution Protocol) is not relevant to updating IPv6 address prefixes. \n- DHCP is not typically used with SLAAC, as it is designed for dynamic IP address assignment in IPv4. \n- Manually changing workstations is inefficient and not automated."
    },
    {
        "question": "A network administrator is configuring DCHP and wants to explicitly set an IP address based on a MAC address. Which of the following should the administrator use?",
        "options": [
            "Dynamic assignment",
            "Static IP on the server",
            "IP helper",
            "Exclusion range",
            "Reservation"
        ],
        "correct_answer": 5,
        "description": "The correct answer is 'Reservation.' DHCP reservations allow a specific IP address to be assigned to a device based on its MAC address. \n\n- Dynamic assignment is for automatic IP address allocation without specifying a device. \n- Static IP on the server is a manual configuration, not related to DHCP. \n- IP helper forwards DHCP requests but does not assign addresses. \n- Exclusion range prevents the DHCP server from assigning certain IP addresses, but it does not provide a fixed address for a device."
    },
    {
        "question": "An administrator wants to host services on the internet using an internal server. The server is configured with an RFC1918 address, and the administrator wants to make the services that are hosted on the server available on one of the company's public IP addresses. Which of the following should the administrator configure to allow this access?",
        "options": [
            "IPv6 tunneling",
            "Virtual IP",
            "Dual stack",
            "EUI-64"
        ],
        "correct_answer": 2,
        "description": "The correct answer is 'Virtual IP.' A Virtual IP (VIP) allows an internal server with an RFC1918 address to be accessed via a public IP address. \n\n- IPv6 tunneling is used to encapsulate IPv6 traffic over IPv4 networks, not for exposing services. \n- Dual stack supports both IPv4 and IPv6 but does not specifically address NAT or public IP exposure. \n- EUI-64 is an IPv6 address configuration method, not a solution for exposing internal services."
    },
    {
        "question": "A network administrator is trying to create a subnet, which is the most efficient size possible, for 31 laptops. Which of the following network subnets would be best in this situation?",
        "options": [
            "10.10.10.0/24",
            "10.10.10.0/25",
            "10.10.10.0/26",
            "10.10.10.0/27"
        ],
        "correct_answer": 3,
        "description": "The correct answer is 10.10.10.0/26. A /26 subnet provides 64 IP addresses, with 62 usable addresses, which is sufficient for 31 devices while leaving room for growth or additional devices. \n\n- 10.10.10.0/24 provides too many addresses (254 usable), wasting IP space. \n- 10.10.10.0/27 offers only 30 usable IPs, which is not enough for 31 devices. \n- 10.10.10.0/25 provides 126 usable IPs, which is excessive for just 31 devices."
    },
    {
        "question": "Users at a company will require more bandwidth on their wireless laptops because of a migration to the cloud. The company's current infrastructure contains four 802.11n access points, which are creating a bottleneck. Hardware upgrades are not an option. Which of the following configurations will provide a solution?",
        "options": [
            "Increasing RSSI",
            "MIMO",
            "Channel bonding",
            "Reconfiguring SSID"
        ],
        "correct_answer": 3,
        "description": "The correct answer is 'Channel bonding.' Channel bonding increases the available bandwidth by combining multiple channels, which is especially important for 802.11n wireless networks. \n\n- Increasing RSSI (Received Signal Strength Indicator) does not directly increase bandwidth, but rather the signal quality. \n- MIMO (Multiple Input, Multiple Output) is a feature of 802.11n but doesn't directly resolve bandwidth issues unless paired with proper configuration. \n- Reconfiguring SSID does not affect bandwidth."
    },
    {
        "question": "Which of the following should be implemented to allow remote users to access network resources while only redirecting necessary traffic?",
        "options": [
            "Split-tunnel VPN",
            "Geofencing",
            "Client-to-site VPN",
            "Remote desktop gateway"
        ],
        "correct_answer": 1,
        "description": "The correct answer is 'Split-tunnel VPN.' Split-tunnel VPN allows remote users to access network resources while routing only specific traffic through the VPN tunnel, which can improve performance and avoid unnecessary load on the VPN. \n\n- Geofencing is used to restrict access based on geographic location, not routing traffic. \n- Client-to-site VPN refers to the method for remote access but does not specify traffic routing. \n- Remote desktop gateway is for remote desktop access, not traffic routing."
    },


    {
        "question": "A technician is troubleshooting servers with high CPU usage. While trying to connect, the technician needs to open a port for remote access. Which of the following ports should the technician open?",
        "options": [
            "443",
            "3321",
            "8080",
            "5900"
        ],
        "correct_answer": 4,
        "description": "The correct answer is 5900. Port 5900 is commonly used for VNC (Virtual Network Computing), a protocol that allows remote access to servers. \n\n- Port 443 is used for HTTPS, which is secure web traffic. \n- Port 3321 is used by some remote desktop solutions but is not the most commonly associated with remote access. \n- Port 8080 is typically used for HTTP alternate ports, not remote access protocols."
    },
    {
        "question": "A network security engineer is responding to a security incident. The engineer suspects that an attacker used an authorized administrator account to make configuration changes to the boundary firewall. Which of the following should the network security engineer review?",
        "options": [
            "Network traffic logs",
            "Audit logs",
            "Syslogs",
            "Event logs"
        ],
        "correct_answer": 2,
        "description": "The correct answer is audit logs. Audit logs provide detailed records of administrative actions, including changes made by authorized users, helping to track potential misuse. \n\n- Network traffic logs show traffic patterns but do not capture specific administrative actions. \n- Syslogs record various system events but are not as focused on security-related actions as audit logs. \n- Event logs primarily focus on system events rather than specific administrative actions."
    },
    {
        "question": "A systems administrator has two network switches that need to be cabled together via copper cabling. Neither of the switches support MDIX. Which of the following types of cables should the administrator use?",
        "options": [
            "Straight",
            "Crossover",
            "Patch cable",
            "Rollover"
        ],
        "correct_answer": 2,
        "description": "The correct answer is crossover. Since the switches do not support MDIX (Auto MDI-X), a crossover cable is required to connect them directly. \n\n- A straight-through cable is used for connecting devices with different roles, such as a switch to a router or a computer. \n- Patch cables are similar to straight-through cables and typically used for short-range connections. \n- A rollover cable is used for connecting to console ports on network devices, not for regular switch-to-switch connections."
    },
    {
        "question": "A network engineer wants to establish a site-to-site VPN tunnel using a protocol that allows for both data confidentiality and authentication. Which of the following is the best choice?",
        "options": [
            "IKE",
            "AH",
            "ESP",
            "IPSec"
        ],
        "correct_answer": 4,
        "description": "The correct answer is IPSec. IPSec is designed to provide both data confidentiality (encryption) and authentication, making it ideal for site-to-site VPN tunnels. \n\n- IKE (Internet Key Exchange) is part of the process used to establish secure connections but does not provide the full confidentiality and authentication. \n- AH (Authentication Header) only provides authentication but does not offer encryption. \n- ESP (Encapsulating Security Payload) provides encryption, but it does not focus on authentication as much as IPSec."
    },
    {
        "question": "Which of the following is the physical topology in which all devices are connected to each other?",
        "options": [
            "Bus",
            "Ring",
            "Mesh",
            "Star"
        ],
        "correct_answer": 3,
        "description": "The correct answer is Mesh. In a mesh topology, each device is directly connected to every other device, ensuring redundancy and reliability. \n\n- Bus topology has all devices connected to a single shared communication medium, which is not direct device-to-device. \n- Ring topology connects devices in a circular fashion, where each device is connected to two others, but not all devices are directly linked. \n- Star topology has a central device that all others connect to, not direct connections between devices."
    },
    {
        "question": "Which of the following most likely occurs when an attacker is between the target and a legitimate server?",
        "options": [
            "IP spoofing",
            "VLAN hopping",
            "Rogue DHCP",
            "On-path attack"
        ],
        "correct_answer": 4,
        "description": "The correct answer is On-path attack. An on-path attack occurs when an attacker positions themselves between a client and server, allowing them to intercept or alter communications. \n\n- IP spoofing involves falsifying the source IP address but does not necessarily require being between the target and server. \n- VLAN hopping allows attackers to send traffic to different VLANs, but it is not directly related to positioning between devices. \n- Rogue DHCP refers to unauthorized DHCP servers providing incorrect IP configurations, not an attack involving interception between a client and server."
    },
    {
        "question": "A technician is troubleshooting an incident regarding a fiber that is connecting two buildings. The technician suspects a break may have occurred midway along the route. Which of the following tools should the technician use to verify the point where the break might be located?",
        "options": [
            "Loopback adapter",
            "OTDR",
            "Cable tester",
            "New SFPs"
        ],
        "correct_answer": 2,
        "description": "The correct answer is OTDR (Optical Time Domain Reflectometer). An OTDR is used to detect breaks or faults in fiber-optic cables by sending light pulses down the fiber and analyzing the reflections. \n\n- A loopback adapter is used to test network ports, not for locating breaks in fiber. \n- A cable tester is used to test copper cables, not fiber-optic cables. \n- New SFPs (Small Form-factor Pluggable transceivers) would not help with locating fiber breaks."
    },
    {
        "question": "A company is moving into a new office, and the network technician is setting up a new wireless solution. Which of the following is the first step the technician should take?",
        "options": [
            "Perform a site survey.",
            "Order equipment.",
            "Create an SSID.",
            "Create network diagrams."
        ],
        "correct_answer": 1,
        "description": "The correct answer is to perform a site survey. A site survey is crucial for determining the best placement of wireless access points (APs) to ensure optimal coverage and performance. \n\n- Ordering equipment is important but should be done after determining the requirements based on the site survey. \n- Creating an SSID and network diagrams should follow after the survey, as these decisions depend on the layout and coverage areas."
    },
    {
        "question": "A technician is configuring a bandwidth-monitoring tool that supports payloads of 1,600 bytes. Which of the following should the technician configure for this tool?",
        "options": [
            "LACP",
            "Flow control",
            "Port mirroring",
            "Jumbo frames"
        ],
        "correct_answer": 4,
        "description": "The correct answer is Jumbo frames. Jumbo frames allow for larger Ethernet frame sizes (typically up to 9,000 bytes), which would support the 1,600-byte payload and improve the efficiency of the bandwidth monitoring tool. \n\n- LACP (Link Aggregation Control Protocol) is used for combining multiple network connections but does not affect frame size. \n- Flow control is used to manage traffic between devices to prevent congestion but does not relate to frame size. \n- Port mirroring is used to copy network traffic to another port for monitoring, not for adjusting payload size."
    },
    {
        "question": "Which of the following authentication methods requires a user to enter a password and scan a fingerprint?",
        "options": [
            "Single sign-on",
            "Kerberos",
            "Multifactor",
            "Network access control"
        ],
        "correct_answer": 3,
        "description": "The correct answer is Multifactor. Multifactor authentication requires multiple forms of verification, such as something the user knows (password) and something the user has (fingerprint). \n\n- Single sign-on (SSO) is a method of logging into multiple systems with one set of credentials but does not require multifactor authentication. \n- Kerberos is a network authentication protocol but does not involve fingerprint scanning. \n- Network access control refers to policies that govern access but does not specify authentication methods."
    },




  {
    "question": "Which of the following copper wire standards utilizes four pairs of wires to achieve Gigabit Ethernet speeds?",
    "options": [
      "1000BASE-FX",
      "1000BASE-T",
      "1000BASE-LR",
      "1000BASE-SX"
    ],
    "correct_answer": 2,
    "description": "The correct answer is 1000BASE-T. This standard uses four pairs of copper wires and supports Gigabit Ethernet speeds over twisted pair cabling (Cat5e or higher). \n\n- 1000BASE-FX uses fiber optic cables for Gigabit speeds. \n- 1000BASE.LR is designed for long-range fiber optic connections. \n- 1000BASE-SX is a short-range fiber optic standard."
  },
  {
    "question": "A technician is troubleshooting a SQL database connection. After remotely connecting to the end client, the technician tests basic connectivity. Which of the following ports is available to connect via command-line interface?",
    "options": [
      "143",
      "445",
      "993",
      "1521"
    ],
    "correct_answer": 4,
    "description": "The correct answer is 1521. Port 1521 is used for Oracle SQL database connections, allowing remote command-line access. \n\n- Port 143 is used for IMAP email protocol. \n- Port 445 is used for SMB file sharing. \n- Port 993 is used for secure IMAP."
  },
  {
    "question": "A company's management team wants to implement NAC on the wired and wireless networks. Which of the following is an authentication component that must be used in this solution?",
    "options": [
      "IPSec",
      "802.1X",
      "EAP",
      "TACACS+"
    ],
    "correct_answer": 2,
    "description": "The correct answer is 802.1X. This is a port-based network access control (NAC) standard that authenticates devices trying to connect to the network. \n\n- IPSec is a security protocol for encrypting IP traffic. \n- EAP is used in conjunction with 802.1X for authentication. \n- TACACS+ is used for remote access authentication but is not a core NAC standard."
  },
  {
    "question": "A network administrator is troubleshooting an issue on a newly configured college campus network. A Linux workstation can connect to the internet, but it fails to connect to the campus intranet, which is located on another campus. Which of the following commands should the administrator run next to troubleshoot the connection?",
    "options": [
      "ifconfig",
      "traceroute",
      "nmap",
      "dig"
    ],
    "correct_answer": 2,
    "description": "The correct answer is traceroute. This command helps trace the network path from the Linux workstation to the destination, showing where the connection fails. \n\n- ifconfig shows network interface information, not connectivity status. \n- nmap is a network scanning tool. \n- dig is a DNS lookup tool."
  },
  {
    "question": "Which of the following is the best way to remotely monitor who is accessing a secure data center?",
    "options": [
      "Access control vestibule",
      "Cameras",
      "Employee training",
      "Biometrics"
    ],
    "correct_answer": 4,
    "description": "The correct answer is biometrics. Biometric systems provide a secure and precise way to track and verify who is accessing a secure data center. \n\n- Access control vestibules control access but do not log detailed access information. \n- Cameras provide surveillance but cannot verify identity as accurately as biometrics. \n- Employee training is necessary but does not directly monitor physical access."
  },
  {
    "question": "A network consultant is installing a new wireless network with the following specifications: 5GHz, 1,300Mbps, 20/40/80MHz. Which of the following standards should the network consultant use?",
    "options": [
      "802.11a",
      "802.11ac",
      "802.11b",
      "802.11n"
    ],
    "correct_answer": 2,
    "description": "The correct answer is 802.11ac. This standard supports high speeds, such as 1,300Mbps, and operates on the 5GHz band with wider channel widths (20/40/80MHz). \n\n- 802.11a supports 54Mbps speeds and operates on the 5GHz band but with narrower channel widths. \n- 802.11b supports lower speeds (11Mbps) and operates on the 2.4GHz band. \n- 802.11n supports higher speeds but not as high as 802.11ac."
  },
  {
    "question": "In a data center, data traffic that moves east-west is flowing between:",
    "options": [
      "the top-of-rack and distribution switches.",
      "the server and the cloud.",
      "the top-of-rack and core switches.",
      "top-of-rack switches."
    ],
    "correct_answer": 4,
    "description": "The correct answer is top-of-rack switches. In a data center, east-west traffic refers to the communication between servers within the same data center, often routed through top-of-rack switches. \n\n- The other options represent different network traffic patterns, such as north-south (between data center and outside world)."
  },
  {
    "question": "Which of the following can IoT devices most likely be connected to?",
    "options": [
      "Router",
      "Firewall",
      "Proxy server",
      "Access point"
    ],
    "correct_answer": 4,
    "description": "The correct answer is access point. IoT devices typically connect to wireless networks via access points, allowing them to communicate with other devices on the network. \n\n- Routers provide network routing but are not specifically designed for IoT connections. \n- Firewalls and proxy servers are security devices, not primary connectivity points for IoT devices."
  },
  {
    "question": "A user reports that the internet seems slow on a workstation, but no other users have reported any issues. The server team confirms the servers are functioning normally. A technician suspects something specific to the user's computer is overutilizing bandwidth. Which of the following commands should the technician use to further investigate the issue?",
    "options": [
      "nmap",
      "tcpdump",
      "netstat",
      "nslookup"
    ],
    "correct_answer": 3,
    "description": "The correct answer is netstat. The netstat command can show active network connections and which processes may be using bandwidth on the workstation. \n\n- nmap is a network scanning tool, not designed for troubleshooting bandwidth usage. \n- tcpdump is used for packet capture, which may be overkill for this issue. \n- nslookup is used for DNS queries, not network usage."
  },
  {
    "question": "Which of the following routing protocols uses bandwidth and delay as the primary metrics to calculate the best path?",
    "options": [
      "EIGRIP",
      "RIP",
      "OSPF",
      "BGP"
    ],
    "correct_answer": 3,
    "description": "The correct answer is OSPF. OSPF uses a combination of bandwidth and delay to calculate the best path in a network. \n\n- EIGRP uses bandwidth, delay, load, and reliability but is often considered a hybrid routing protocol. \n- RIP uses hop count as the primary metric. \n- BGP uses AS path and other attributes, not bandwidth and delay."
  },


    {
        "question": "A new computer that was connected to the network reported an error of an Identical IP address with another computer. Both computers were configured for SLAAC. Which of the following is causing the error?",
        "options": [
            "Rogue DHCP server.",
            "Duplicate MAC addresses.",
            "Incorrect router advertisement.",
            "Wrong VLAN assignment."
        ],
        "correct_answer": 3,
        "description": "The correct answer is Incorrect router advertisement. In SLAAC (Stateless Address Autoconfiguration), routers send advertisements to inform devices on the network about how to configure their IP addresses. An incorrect router advertisement could cause duplicate IP addresses. \n\n- A rogue DHCP server could interfere with DHCP-based IP assignment, but SLAAC does not rely on DHCP for address assignment. \n- Duplicate MAC addresses are not a common cause of IP address conflicts. \n- A wrong VLAN assignment would affect connectivity but not lead to duplicate IP addresses."
    },
    {
        "question": "A user is having trouble uploading files to a server. However, other users in the department are not experiencing this issue. The network administrator checks the access switch and sees multiple CRC errors on that user's switchport. Which of the following should the network administrator do first?",
        "options": [
            "Replace the uplink cable for the access switch.",
            "Replace the user's network cable.",
            "Replace the NIC for the user's PC.",
            "Replace the access switch."
        ],
        "correct_answer": 2,
        "description": "The correct answer is to replace the user's network cable. CRC (Cyclic Redundancy Check) errors are typically caused by issues with physical connections, such as a faulty or damaged network cable. \n\n- Replacing the uplink cable may not address the issue since the problem is specific to the user's switchport. \n- Replacing the NIC might be considered, but network cable issues are more common and easier to check. \n- Replacing the access switch would be an extreme measure when the issue is likely local to the user."
    },
    {
        "question": "A network engineer has added a new route on a border router and is trying to determine if traffic is using the new route. Which of the following commands should the engineer use?",
        "options": [
            "ping",
            "arp",
            "trace",
            "route"
        ],
        "correct_answer": 4,
        "description": "The correct answer is 'route'. The 'route' command is used to view and manipulate the routing table, which will show whether traffic is using the new route. \n\n- 'ping' checks the connectivity to a destination but does not reveal the specific route taken. \n- 'arp' is used to view or modify the ARP table, which relates to resolving IP addresses to MAC addresses, not routing. \n- 'trace' (or traceroute) can show the path traffic takes, but it may not directly reflect routing table changes."
    },
    {
        "question": "A network technician is troubleshooting VoIP calls that have jumbled and distorted audio. The network technician analyzes the voice VLAN traffic and determines packets on the voice VLAN are being received out of order. Which of the following network metrics are causing the VoIP issues?",
        "options": [
            "Jitter",
            "Bandwidth",
            "Latency",
            "Delay"
        ],
        "correct_answer": 1,
        "description": "The correct answer is 'Jitter'. Jitter refers to the variation in the delay of packet delivery over the network, which can cause out-of-order packets and result in poor VoIP call quality. \n\n- 'Bandwidth' refers to the amount of data that can be transmitted but does not typically cause out-of-order packet delivery. \n- 'Latency' is the delay in packet transmission and can affect VoIP quality, but jitter specifically addresses out-of-order packets. \n- 'Delay' affects VoIP but does not directly cause jumbled or distorted audio."
    },
    {
        "question": "Which of the following should be used to associate an IPv6 address with a domain name?",
        "options": [
            "AAAA",
            "A",
            "SOA",
            "TXT"
        ],
        "correct_answer": 1,
        "description": "The correct answer is 'AAAA'. The AAAA record in DNS maps an IPv6 address to a domain name. \n\n- The 'A' record maps an IPv4 address to a domain name. \n- 'SOA' (Start of Authority) is a type of DNS record that provides information about the DNS zone, not for associating IP addresses. \n- 'TXT' records allow for arbitrary text to be stored in DNS and are not used for IP address mapping."
    },
    {
        "question": "Users report they cannot reach any websites on the internet. An on-site network engineer is able to duplicate the issue on a different PC. The network engineer then tries to ping a website and receives the following message: Ping request could not find host www.google.com. Please check the name and try again. Which of the following is the next step the engineer should take?",
        "options": [
            "Ping 127.0.0.1 to test local hardware.",
            "Test the website from outside the company.",
            "Ping internal name server functionality.",
            "Check internet firewall logs for blocked DNS traffic."
        ],
        "correct_answer": 3,
        "description": "The correct answer is 'Ping internal name server functionality.' The error indicates a DNS resolution issue, so the next step is to check if the internal DNS server is functioning correctly. \n\n- Pinging 127.0.0.1 tests the local machine's network stack but does not address DNS issues. \n- Testing the website from outside the company may help diagnose external connectivity issues but does not directly address DNS resolution. \n- Checking firewall logs is a good step if DNS issues are related to filtering, but verifying the DNS server's functionality is the more direct approach."
    },
    {
        "question": "Which of the following devices allows local, high-speed Ethernet traffic to be transmitted over twisted-pair telephone lines for WAN connectivity?",
        "options": [
            "Media converter",
            "WLAN controller",
            "Repeater",
            "DSL modem"
        ],
        "correct_answer": 4,
        "description": "The correct answer is 'DSL modem'. A DSL modem allows high-speed Ethernet traffic to be transmitted over standard telephone lines, enabling WAN connectivity. \n\n- A media converter is used to convert between different types of network media (e.g., fiber to copper). \n- A WLAN controller is responsible for managing wireless networks, not for WAN connectivity over telephone lines. \n- A repeater amplifies network signals but does not perform the function of connecting to WAN services."
    },
    {
        "question": "A network administrator is troubleshooting a network connectivity issue. The workstation can connect to the internet but not to internal network resources. Which of the following is most likely the cause of the issue?",
        "options": [
            "APIPA address",
            "Rogue DHCP server",
            "Unreachable DNS server",
            "Incorrect NAT settings"
        ],
        "correct_answer": 1,
        "description": "The correct answer is 'APIPA address'. An APIPA (Automatic Private IP Addressing) address is assigned when a device cannot reach a DHCP server and is unable to get a proper IP address. This often results in internet connectivity but prevents access to internal resources. \n\n- A rogue DHCP server could cause incorrect IP addressing, but an APIPA address is a more likely cause of the described issue. \n- An unreachable DNS server would prevent name resolution, but internet connectivity suggests the issue is with internal networking. \n- Incorrect NAT settings affect routing between internal and external networks but would not cause issues with internal resource access."
    },
    {
        "question": "Which of the following is associated with the session layer of the OSI model?",
        "options": [
            "Data representation",
            "Packets",
            "Sockets",
            "Frames"
        ],
        "correct_answer": 3,
        "description": "The correct answer is 'Sockets'. Sockets are an abstraction of the session layer in the OSI model, which establishes and manages communication sessions between devices. \n\n- 'Data representation' is part of the presentation layer, not the session layer. \n- 'Packets' are associated with the network layer. \n- 'Frames' are part of the data link layer, responsible for physical transmission and error detection."
    },
    {
        "question": "Clients have reported slowness between a branch and a hub location. The senior engineer suspects asymmetrical routing is causing the issue. Which of the following should the engineer run on both the source and the destination network devices to validate this theory?",
        "options": [
            "traceroute",
            "ping",
            "route",
            "nslookup"
        ],
        "correct_answer": 1,
        "description": "The correct answer is 'traceroute'. The 'traceroute' command helps identify the path that packets take between the source and destination, which can confirm if asymmetrical routing is occurring. \n\n- 'ping' checks connectivity but does not provide information about the route taken. \n- 'route' displays the local routing table but does not trace the actual packet path. \n- 'nslookup' is used for DNS queries and does not provide routing information."
    },


        {
            "question": "A company commissioned a site survey to check wireless network coverage. The technician noticed undesirable levels of RSSI in different areas of the office. Which of the following levels did the technician most likely notice?",
            "options": [
                "-82dBm",
                "-61dBm",
                "42dBm",
                "63dBm"
            ],
            "correct_answer": 1,
            "description": "The correct answer is -82dBm. A low RSSI (Received Signal Strength Indicator) value, such as -82dBm, indicates weak signal strength, which leads to poor wireless network coverage. \n\n- -61dBm is a better signal strength and is likely to provide stable connectivity. \n- 42dBm and 63dBm are not valid dBm measurements, as they are outside the expected range for signal strength."
        },
        {
            "question": "A network administrator will be running Ethernet cables through raised ceilings. Which of the following types of Ethernet cables is the safest solution?",
            "options": [
                "Shielded",
                "Plenum",
                "Unshielded",
                "Riser"
            ],
            "correct_answer": 2,
            "description": "The correct answer is Plenum. Plenum-rated cables are designed for use in air circulation spaces, such as raised ceilings, as they are fire-resistant and produce less toxic smoke. \n\n- Shielded cables provide protection against electromagnetic interference but are not fire-rated. \n- Unshielded cables do not have the necessary fire resistance for use in these spaces. \n- Riser cables are rated for vertical spaces and are not suitable for air circulation spaces."
        },
        {
            "question": "Outside traffic from local subnet is using an internal web server. A technician must apply best practices to ensure outside users can only access the web server and not any other internal resources. Which of the following should the technician do to best address the issue?",
            "options": [
                "Move the web server to a perimeter network.",
                "Connect the web server to the WAN.",
                "Connect the server directly to a second port on the cable modem.",
                "Block incoming port 80 and port 443 traffic to the server."
            ],
            "correct_answer": 1,
            "description": "The correct answer is to move the web server to a perimeter network. A perimeter network (also called a DMZ) is a network segment that is isolated from the internal network, allowing outside users to access only specific resources like the web server. \n\n- Connecting the web server directly to the WAN would expose it to unnecessary risks. \n- Blocking incoming traffic to the server would prevent users from accessing it entirely. \n- A second port on the cable modem does not provide the isolation needed for security."
        },
        {
            "question": "A technician is working on a solution to isolate traffic between specific types of devices, servers, and users on the internal firewall. Which of the following traffic flows should be isolated?",
            "options": [
                "East-west",
                "Access/edge",
                "Core/distribution",
                "North-south"
            ],
            "correct_answer": 1,
            "description": "The correct answer is East-west. East-west traffic refers to communication between devices within the same network or subnet. Isolating this traffic helps improve security by controlling which devices can communicate with each other. \n\n- Access/edge refers to traffic between the end-user devices and the network perimeter, which is less about isolating devices within the network. \n- Core/distribution refers to network infrastructure layers, which typically manage high-level traffic routing. \n- North-south refers to traffic between the internal network and external resources like the internet."
        },
        {
            "question": "A network engineer performed a detailed network analysis. The engineer has decided to update the STP port cost in order to optimize the network. Which of the following processes should the engineer use to gain approval for the network optimization?",
            "options": [
                "Business continuity",
                "Disaster recovery",
                "Incident response",
                "Change management"
            ],
            "correct_answer": 4,
            "description": "The correct answer is Change management. Change management ensures that network changes, like updating STP port costs, are approved and implemented systematically to minimize disruption. \n\n- Business continuity is about maintaining services during disruptions, not about making network changes. \n- Disaster recovery plans for recovering from events, not for routine changes. \n- Incident response focuses on responding to security or network issues, not on planned optimization."
        },
        {
            "question": "A network technician plugged a workstation into a network device. When the technician turned on the workstation, it was not connected at full duplex. Which of the following devices was the workstation connected to?",
            "options": [
                "Media converter",
                "Hub",
                "Bridge",
                "Layer 3 switch"
            ],
            "correct_answer": 2,
            "description": "The correct answer is Hub. A hub is an older network device that does not support full-duplex communication, often causing devices to operate at half-duplex. \n\n- A media converter, bridge, and Layer 3 switch typically support full-duplex communication."
        },
        {
            "question": "A user is trying to map a network fileshare to a local drive and needs to open a firewall port for this traffic. Which of the following ports needs to be opened to accomplish this task?",
            "options": [
                "389",
                "445",
                "514",
                "636"
            ],
            "correct_answer": 2,
            "description": "The correct answer is 445. Port 445 is used for SMB (Server Message Block), which is required for file sharing in Windows environments. \n\n- Port 389 is used for LDAP. \n- Port 514 is used for syslog. \n- Port 636 is used for secure LDAP (LDAPS)."
        },
        {
            "question": "Which of the following OSI layers is ICMP a part of?",
            "options": [
                "Application",
                "Session",
                "Network",
                "Transport"
            ],
            "correct_answer": 3,
            "description": "The correct answer is Network. ICMP (Internet Control Message Protocol) operates at the Network layer (Layer 3) of the OSI model, providing error messages and operational information. \n\n- Application layer (Layer 7) handles communication between applications. \n- Session layer (Layer 5) manages sessions between applications. \n- Transport layer (Layer 4) handles end-to-end communication and error recovery."
        },
        {
            "question": "A network administrator receives a call about a network printer that is not working for a workstation. The network administrator verifies the printer is turned on. Given the following information: \nRouter's gateway IP: 10.0.0.1/25 \nDevice: Printer - IP Address: 10.1.0.60 Subnet Mask: 255.255.255.128 \nDevice: Workstation - IP address 10.0.0.126 Subnet mask 255.255.255.192 \nWhich of the following should the administrator change to remediate this issue? (Choose two.)",
            "options": [
                "The subnet on the router",
                "The IP address on the printer",
                "The subnet on the printer",
                "The IP address on the router",
                "The subnet on the workstation",
                "The IP address on the workstation"
            ],
            "correct_answer": [3, 5],
            "description": "The correct answers are 'The subnet on the workstation' and 'The subnet on the printer.' The workstation and printer are currently in different subnets, which prevents communication. Here’s a detailed explanation: \n\n1. **Workstation Analysis:**\n   - The workstation IP is 10.0.0.126, and its subnet mask is 255.255.255.192 (/26).\n   - With this subnet mask, the workstation belongs to the network 10.0.0.64/26, which has a usable IP range of 10.0.0.65 to 10.0.0.126. The last usable IP is 10.0.0.126, where the workstation is currently assigned.\n   - This network does not include the router gateway IP (10.0.0.1), which belongs to the 10.0.0.0/25 network. The workstation’s subnet needs to be corrected to match the router’s subnet.\n\n2. **Printer Analysis:**\n   - The printer IP is 10.1.0.60, and its subnet mask is 255.255.255.128 (/25).\n   - This subnet places the printer in the 10.1.0.0/25 network, which has a usable range of 10.1.0.1 to 10.1.0.126.\n   - The printer's network does not match the router’s network (10.0.0.0/25), making it unreachable for the workstation. To resolve this, the printer's IP and subnet must be updated to match the router’s network.\n\n3. **Summary of Fixes:**\n   - The workstation's subnet mask must be updated to 255.255.255.128 (/25) so it aligns with the router’s network.\n   - The printer's IP address and/or subnet mask must also be updated to fall within the same 10.0.0.0/25 network.\n\n- **Router's Configuration:** The router’s IP and subnet are correct (10.0.0.1/25), so no changes are needed here.\n- **IP Address on the Workstation/Printer:** Changing the IP address alone without fixing the subnet mask would still result in communication failure. The subnet mask adjustment ensures they share the same network."
        },



    {
        "question": "An engineer recently installed a new distribution switch and connected two servers provisioned with the following IPs: 192.168.17.20 and 192.168.17.30. The servers cannot connect to the internet, but they can reach themselves. The engineer observes that the distribution switch has the following setup: interface VLAN 100 IP address 192.168.17.5 255.255.255.0. The engineer is able to reach the core router 192.168.17.1 from the distribution switch. Which of the following is the most likely cause of this issue?",
        "options": [
            "A routing loop has occurred.",
            "The subnet mask is incorrect.",
            "The servers are not configured with default gateway.",
            "There is an improper Layer 1 connection between the router and the ISP modem."
        ],
        "correct_answer": 3,
        "description": "The correct answer is 'The servers are not configured with default gateway.' The servers can communicate within the same subnet but cannot reach the internet, indicating a missing or incorrect gateway configuration. \n\n- A routing loop would prevent the network from reaching any destination, not just the internet. \n- The subnet mask is correct as it allows proper communication within the local network. \n- An improper Layer 1 connection would affect basic network connectivity, not just internet access."
    },
    {
        "question": "Which of the following is the best action to take before sending a network router to be recycled as electronic waste?",
        "options": [
            "Turn on port security.",
            "Shred the switch hard drive.",
            "Back up and erase the configuration.",
            "Remove the company asset ID tag."
        ],
        "correct_answer": 3,
        "description": "The correct answer is 'Back up and erase the configuration.' Before sending a router to be recycled, you should back up the configuration and securely erase any sensitive data to prevent unauthorized access. \n\n- Port security is a useful feature but does not address the need to secure configuration data. \n- Shredding the hard drive is unnecessary for routers without hard drives or storage. \n- Removing the company asset ID tag is not relevant to securing sensitive data."
    },
    {
        "question": "Which of the following best describes the purpose of an access control vestibule?",
        "options": [
            "To mitigate an on-path attack",
            "To mitigate tailgating",
            "To mitigate phishing",
            "To mitigate snooping"
        ],
        "correct_answer": 2,
        "description": "The correct answer is 'To mitigate tailgating.' An access control vestibule is designed to prevent unauthorized persons from following authorized individuals into secure areas. \n\n- On-path attacks involve network security, not physical security. \n- Phishing is an online social engineering attack, not related to physical access control. \n- Snooping refers to unauthorized access to information but is not the primary concern of a vestibule."
    },
    {
        "question": "A network administrator is switching to IPv6 and wants to be able to use packet-tracing software on the network to monitor traffic. The administrator wants to set up the IP addressing to include the MAC address of each machine that is connected. Which of the following should the administrator implement? (Choose two.)",
        "options": [
            "EUI-64",
            "RFC1819",
            "APIPA",
            "DHCPv6",
            "SLAAC",
            "CIDR"
        ],
        "correct_answer": [1, 5],
        "description": "The correct answers are 'EUI-64' and 'SLAAC.' EUI-64 (Extended Unique Identifier) allows IPv6 addresses to be automatically generated based on the MAC address. SLAAC (Stateless Address Autoconfiguration) is a method used to assign IPv6 addresses to devices. \n\n- RFC1819 is outdated and not relevant to modern IPv6 configurations. \n- APIPA is for automatic private IP addressing and is not used for IPv6 address configuration. \n- DHCPv6 is for IPv6 address assignment but does not specifically include MAC addresses in the addressing process."
    },
    {
        "question": "A network consultant is working with a software-defined network and is troubleshooting an issue with an application's instructions being properly translated for the network components. Which of the following is most likely at fault?",
        "options": [
            "Infrastructure layer",
            "Session layer",
            "Control layer",
            "Application layer"
        ],
        "correct_answer": 3,
        "description": "The correct answer is 'Control layer.' The control layer in a software-defined network is responsible for translating the application's instructions for network components. \n\n- The infrastructure layer is responsible for the physical network. \n- The session layer handles session management and communication, but not translation of instructions. \n- The application layer deals with user-facing services, but not the instructions for network management."
    },
    {
        "question": "A network administrator is creating a VLAN that will only allow executives to connect to a data source. Which of the following is this scenario an example of?",
        "options": [
            "Availability",
            "Confidentiality",
            "Internal threat",
            "External threat",
            "Integrity"
        ],
        "correct_answer": 2,
        "description": "The correct answer is 'Confidentiality.' Restricting access to sensitive data for executives is a measure to maintain confidentiality. \n\n- Availability ensures resources are accessible but is not the main concern in this scenario. \n- Internal threat refers to threats from within the organization, but this scenario is about securing data access. \n- External threat involves outside attackers, which is not the focus here. \n- Integrity ensures data accuracy and trustworthiness, but confidentiality is the primary concern in this case."
    },
    {
        "question": "Which of the following is a major difference between a router and a Layer 3 switch?",
        "options": [
            "A router can perform PAT, but a Layer 3 switch cannot.",
            "A Layer 3 switch is more efficient than a router.",
            "A router uses higher speed interfaces than a Layer 3 switch.",
            "A Layer 3 switch can run more routing protocols than a router."
        ],
        "correct_answer": 1,
        "description": "The correct answer is 'A router can perform PAT, but a Layer 3 switch cannot.' PAT (Port Address Translation) is a feature of routers, not Layer 3 switches. \n\n- Layer 3 switches are typically faster than routers for routing functions, but not always more efficient. \n- Routers and Layer 3 switches can use similar interfaces, but speed is not the primary distinction. \n- Routers generally support more routing protocols than Layer 3 switches."
    },
    {
        "question": "Which of the following common agreements would a company most likely have an employee sign as a condition of employment?",
        "options": [
            "NDA",
            "ISP",
            "SLA",
            "MOU"
        ],
        "correct_answer": 1,
        "description": "The correct answer is 'NDA' (Non-Disclosure Agreement). An NDA is commonly signed by employees to protect confidential company information. \n\n- ISP (Internet Service Provider) agreements are unrelated to employment. \n- SLA (Service Level Agreement) pertains to service delivery expectations, not employee conditions. \n- MOU (Memorandum of Understanding) is used for agreements between organizations, not typically for employment."
    },
    {
        "question": "A user is experiencing network connectivity issues. Upon investigation, the engineer learns that the user installed a personal router and switch to use for multiple computers in the department. Which of the following has the user most likely introduced into the network?",
        "options": [
            "Broadcast storms",
            "Collisions",
            "Rogue DHCP server",
            "DNS poisoning"
        ],
        "correct_answer": 3,
        "description": "The correct answer is 'Rogue DHCP server.' A personal router may introduce a rogue DHCP server, causing IP address conflicts and network issues. \n\n- Broadcast storms occur when too many broadcasts flood the network, typically due to misconfigurations. \n- Collisions happen in networks with older devices like hubs, but this is not typical in modern switched networks. \n- DNS poisoning involves corrupting DNS data, not an issue caused by installing a personal router."
    },
    {
        "question": "A branch office is experiencing frequent power-related issues that are taking the network down daily. Which of the following would best address this network uptime issue?",
        "options": [
            "MPLS",
            "IPS",
            "PDU",
            "UPS",
            "HA firewalls"
        ],
        "correct_answer": 4,
        "description": "The correct answer is 'UPS' (Uninterruptible Power Supply). A UPS will provide backup power during outages, ensuring the network stays operational. \n\n- MPLS is a method for routing data, not a solution for power issues. \n- IPS (Intrusion Prevention System) addresses security, not power problems. \n- PDU (Power Distribution Unit) helps manage power distribution but does not provide backup power. \n- HA (High Availability) firewalls ensure network redundancy, but they do not solve power-related issues."
    },






    {
        "question": "A network technician is working to deploy a new subnet to support 500 hosts. The technician needs to limit the number of unused IP addresses. Which of the following subnets should the technician choose?",
        "options": [
            "255.255.224.0",
            "255.255.248.0",
            "255.255.252.0",
            "255.255.254.0"
        ],
        "correct_answer": 4,
        "description": "The correct answer is 255.255.254.0. This subnet mask provides 510 usable IP addresses, which fits the requirement of supporting 500 hosts, while minimizing unused IP addresses. \n\n- 255.255.224.0 provides 2046 hosts, which results in more unused IPs. \n- 255.255.248.0 provides 2046 hosts, which is also more than needed. \n- 255.255.252.0 provides 1022 hosts, which is too large and not efficient for 500 hosts."
    },
   {
        "question": "Users are connected to a switch on an Ethernet interface of a campus router. The service provider is connected to the serial 1 interface on the router. The output of the interfaces is:\n\nE1/0: 192.168.8.1/24 -\n\nS1: 192.168.7.252/30 -\n\nAfter router and device configurations are applied, internet access is not possible. Which of the following is the most likely cause?",
        "options": [
            "The Ethernet interface was configured with an incorrect IP address.",
            "The router was configured with an incorrect loopback address.",
            "The router was configured with an incorrect default gateway.",
            "The serial interface was configured with the incorrect subnet mask."
        ],
        "correct_answer": 4,
        "description": "The correct answer is the serial interface was configured with the incorrect subnet mask. The serial interface uses the IP range 192.168.7.252/30, which provides only 2 usable addresses (192.168.7.253 for the service provider and 192.168.7.252 for the router). If the subnet mask is misconfigured, the router cannot communicate with the service provider, resulting in no internet access.\n\n- The Ethernet interface IP address (192.168.8.1/24) is correct and allows devices on the LAN to communicate.\n- The loopback address is irrelevant here, as it is typically used for testing or internal routing.\n- The default gateway is necessary for routing traffic, but the misconfigured subnet mask on the serial interface directly impacts connectivity to the upstream provider, which is critical for internet access."
    },
    {
        "question": "A network engineer is installing APs for a SOHO where every staff member uses a cordless phone. Which of the following standards would work best to reduce interference?",
        "options": [
            "802.11a",
            "802.11b",
            "802.11g",
            "802.1X"
        ],
        "correct_answer": 1,
        "description": "The correct answer is 802.11a. This standard operates on the 5 GHz band, which is less likely to interfere with cordless phones, which typically operate on the 2.4 GHz band. \n\n- 802.11b and 802.11g operate on the 2.4 GHz band and would be susceptible to interference from cordless phones. \n- 802.1X is a security protocol, not related to interference."
    },
    {
        "question": "A packet has a destination address that is located outside of the local network. Which of the following should be used to route this packet out of the local network?",
        "options": [
            "DNS server",
            "Load balancer",
            "DHCP server",
            "Default gateway"
        ],
        "correct_answer": 4,
        "description": "The correct answer is the default gateway. The default gateway is used to route packets destined for addresses outside of the local network. \n\n- DNS servers are responsible for resolving domain names to IP addresses but do not route packets. \n- Load balancers distribute network traffic but do not perform routing functions. \n- DHCP servers assign IP addresses to devices but do not route traffic."
    },
    {
        "question": "A network administrator wants all outgoing traffic to the internet to flow through a single device for web content inspection. Which of the following devices is the most appropriate?",
        "options": [
            "VPN headend",
            "Router",
            "Proxy server",
            "Load balancer"
        ],
        "correct_answer": 3,
        "description": "The correct answer is proxy server. A proxy server is used to filter and inspect web content by routing all traffic through it. \n\n- A VPN headend is used for secure remote access, not content inspection. \n- A router routes traffic but does not inspect content. \n- A load balancer distributes traffic but does not inspect web content."
    },
    {
        "question": "An attack is redirecting traffic from network hosts by changing their assigned DNS server. None of the hosts have static IP addresses, and the rogue DNS server was assigned automatically during the hosts' lease renewal for the network configuration. Which of the following should be implemented to prevent this type of attack from occurring again?",
        "options": [
            "DHCP snooping",
            "Port security",
            "802.1X authentication",
            "MAC filtering"
        ],
        "correct_answer": 1,
        "description": "The correct answer is DHCP snooping. DHCP snooping is a security feature that helps prevent rogue DHCP servers from assigning incorrect configuration to devices. \n\n- Port security limits access to a network port but does not address DNS redirection. \n- 802.1X authentication controls access to the network but does not specifically address DHCP attacks. \n- MAC filtering restricts access based on MAC addresses but does not protect against DNS server manipulation."
    },
    {
        "question": "The cybersecurity department needs to monitor historical IP network traffic on the WAN interface of the outside router without installing network sensors. Which of the following would be best to allow the department to complete this task?",
        "options": [
            "Enabling NetFlow on the interface",
            "Enabling SSH on the interface",
            "Enabling SNMP on the interface",
            "Enabling 802.1Q on the interface"
        ],
        "correct_answer": 1,
        "description": "The correct answer is enabling NetFlow on the interface. NetFlow allows the collection of network traffic data for analysis and monitoring without the need for physical sensors. \n\n- SSH is used for secure access to devices, not traffic monitoring. \n- SNMP is used for network management and monitoring but does not provide detailed flow-level data. \n- 802.1Q is used for VLAN tagging, not for monitoring traffic."
    }









    
]
