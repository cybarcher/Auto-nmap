# Auto-nmap



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
