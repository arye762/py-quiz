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




]
