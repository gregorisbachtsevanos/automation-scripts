import speedtest

def get_internet_speed():
    st = speedtest.Speedtest()
    
    # Get the best server based on ping
    st.get_best_server()
    
    # Perform download and upload speed tests
    download_speed = st.download()
    upload_speed = st.upload()
    
    # Convert speeds from bits per second to megabits per second
    download_speed_mbps = download_speed / 1_000_000
    upload_speed_mbps = upload_speed / 1_000_000
    
    return download_speed_mbps, upload_speed_mbps

if __name__ == "__main__":
    download, upload = get_internet_speed()
    print(f"Download speed: {download:.2f} Mbps")
    print(f"Upload speed: {upload:.2f} Mbps")
