import nmap
import subprocess
import re

def get_default_gateway_windows():
    """Retrieve the default gateway on a Windows system."""
    result = subprocess.run(['ipconfig'], capture_output=True, text=True)
    gateway = re.search(r'Default Gateway.*?: (\d+\.\d+\.\d+\.\d+)', result.stdout)
    if gateway:
        return gateway.group(1)
    else:
        raise Exception("Could not determine default gateway")

def scan_network(gateway_ip):
    """Scan the network for connected devices."""
    nm = nmap.PortScanner()
    nm.scan(hosts=f'{gateway_ip}/24', arguments='-sn')

    devices = []
    for host in nm.all_hosts():
        if 'mac' in nm[host]['addresses']:
            devices.append({
                'ip': nm[host]['addresses']['ipv4'],
                'mac': nm[host]['addresses']['mac'],
                'vendor': nm[host]['vendor'].get(nm[host]['addresses']['mac'], 'Unknown')
            })
    return devices

def main():
    try:
        gateway_ip = get_default_gateway_windows()
        print(f"Default Gateway: {gateway_ip}")
        devices = scan_network(gateway_ip)
        print(f"Devices connected to the network: {len(devices)}")
        for device in devices:
            print(f"IP: {device['ip']} MAC: {device['mac']} Vendor: {device['vendor']}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
