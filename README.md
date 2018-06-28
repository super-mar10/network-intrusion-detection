# Network Intrusion Detection

### Task:

Develop a machine learning model to detect network intrusions. The predictive model will distinguish malicious and normal connections.


### Data:

NSL KDD is the dataset used for this project. It's an improved version from the famous KDD-99 dataset. This data originated from MIT's Lincoln Lab - which set up a simulated environment to study intrusion detection.


##### Data size:

* 41 features
* 125,973 connections in Train
* 22,543 connections in Test

##### Connection Types:

* 67,343 normal in Train
* 58,630 malicious in Train

##### The malicious attacks fall into 4 main categories and each category contains various attack types:

* DOS: Denial of service (ex. Smurf)
* R2L: Unauthorized access from a remote machine; hacker attemps to get local user privileges vulnerabilities in the system (ex. httptunnel)
* U2R: Unauthorized access to local superuser (root) privileges; hacker operates as root user and abuses vulnerabilities in the system (ex. buffer_overflow)
* Probing: Unauthorized scans on the victim's machine to determine vulnerabilities that may be exploited (ex. Nmap)


**Note**: The test data is not from the same probability distribution as the training data, and it includes specific attack types not in the training data.  This makes the task more realistic. 
