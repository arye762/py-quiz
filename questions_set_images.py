questions_set_images = [
{
    "question": "An organization experienced a security breach that allowed an attacker to send fraudulent wire transfers from a hardened PC exclusively to the attacker's bank through remote connections. A security analyst is creating a timeline of events and has found a different PC on the network containing malware. Upon reviewing the command history, the analyst finds the following:\n\n[Command history]\n\nWhich of the following best describes how the attacker gained access to the hardened PC?",
    "image": "images/question292.png",
    "options": [
        "The attacker created fileless malware that was hosted by the banking platform.",
        "The attacker performed a pass-the-hash attack using a shared support account.",
        "The attacker utilized living-off-the-land binaries to evade endpoint detection and response software.",
        "The attacker socially engineered the accountant into performing bad transfers."
    ],
    "correct_answer": 2,
    "description": "To determine how the attacker accessed the hardened PC:\n- Fileless malware exists only in memory and would not leave command history.\n\n- A pass-the-hash attack, which is the correct answer, reuses hashed credentials to gain access, fitting the scenario described.\n- Living-off-the-land binaries are legitimate tools used for malicious purposes but do not explain the access to the hardened PC.\n- Social engineering would involve tricking someone but is unrelated to the specific command history found.\n\n**Domain 4: Operations and Incident Response**"
	
},
{
    "question": "A security analyst received a tip that sensitive proprietary information was leaked to the public. The analyst is reviewing the PCAP and notices traffic between an internal server and an external host that includes the following: [PCAP data]. Which of the following was most likely used to exfiltrate the data?",
    "image": "images/question274.png",
    "options": [
        "Encapsulation",
        "MAC address spoofing",
        "Steganography",
        "Broken encryption",
        "Sniffing via on-path position"
    ],
    "correct_answer": 1,
    "description": "Encapsulation hides data within legitimate traffic, making it a likely method for exfiltration.\n\n- MAC address spoofing: Masks identity, not related to data exfiltration.\n- Steganography: Hides data in files, but not in network traffic.\n- Broken encryption: Indicates weak encryption, not directly exfiltration.\n- Sniffing: Used for interception, not exfiltration.\n\n**Domain 1: Attacks, Threats, and Vulnerabilities**"
}
 
]