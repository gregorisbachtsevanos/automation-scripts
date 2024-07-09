## How to Use:

###  install the speedtest-cli library
```
pip install speedtest-cli
```
### Explanation
Import speedtest: The script imports the speedtest module.\
Initialize Speedtest Object: Creates an instance of the Speedtest class.\
Find Best Server: The get_best_server method selects the best server based on ping.\
Perform Speed Tests:\
 -The download method performs the download speed test.\
 -The upload method performs the upload speed test.\
Convert Speeds: The script converts the speeds from bits per second to megabits p\er second by dividing by 1,000,000.\
Main Block: Calls the get_internet_speed function and prints the download and upload speeds.\
