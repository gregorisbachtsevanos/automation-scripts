pip install scapy-python3 python-nmap

Explanation:
Get Default Gateway:

The function get_default_gateway_windows uses the ipconfig command to find the default gateway on a Windows system. It uses regular expressions to parse the command output for the gateway IP address.
Scan Network:

The scan_network function remains the same as the previous version, using nmap to scan the local network.
Main Function:

The main function orchestrates the process, printing out the default gateway, the number of devices found, and details about each device.
Notes:
This script is designed for Windows systems. It uses ipconfig to get the default gateway instead of ip route.
Ensure you run this script with administrative privileges because network scanning typically requires elevated permissions.
Network scanning should be done responsibly and with permission.
You may need to install nmap on your system separately. You can download it from the Nmap website. Make sure nmap is added to your system's PATH so that the nmap command can be used from the command line.
