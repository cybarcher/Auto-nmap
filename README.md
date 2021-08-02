# Auto-nmap

![Screenshot from 2021-08-02 05-55-49](https://user-images.githubusercontent.com/54572947/127843607-bfceeb77-52da-4d90-b686-a04d992be963.png)


# About
* Runs multithreaded nmap scans on the input file containg ip list
* creates a log file named scans.log to resume scanniing in case it got cancelled or interrupted
* Regularly checks Internet connection to avoid false positive scans
* Saves output file with ip name in XML and HTML format to view easily on the browser 

# Requirements

It requires python 2.X and works only on Linux
```
pip install multiprocessing.dummy
pip install netaddr
pip install nmap
sudo apt install xsltproc
```
# Usage

Save ip/subnets list in a single file and run the following command

```python auto-nmap.py iplist threads_count```

### Example
```python auto-nmap.py iplist 50```

# Output Result
### Created separate XML and HTML folders
![Screenshot from 2021-08-02 05-56-20](https://user-images.githubusercontent.com/54572947/127843838-74c30a39-a8e1-42a3-b383-51d47d3c8e92.png)


### File Names
![Screenshot from 2021-08-02 05-56-36](https://user-images.githubusercontent.com/54572947/127843915-18ab2a17-490d-4c84-8838-33deec7fd5f8.png)

### HTML result displayed in browser
![Screenshot from 2021-08-02 05-58-16](https://user-images.githubusercontent.com/54572947/127844029-13a8f430-4d81-43c9-a48f-40407284665e.png)

