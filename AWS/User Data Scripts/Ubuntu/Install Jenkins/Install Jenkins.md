# Install Jenkins

## Procedure
1. Declare the shebang and include the directory where the bash file is located
```
#!/bin/bash
```

2. Update and upgrade the operating system
```
#!/bin/bash
apt-get update
apt-get upgrade -y
```

3. Write out the commands to download Jenkins
```
#!/bin/bash
apt-get update
apt-get upgrade -y
wget -O /usr/share/keyrings/jenkins-keyring.asc https://pkg.jenkins.io/debian/jenkins.io-2023.key
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null
apt-get update
apt-get install fontconfig -y
apt-get install openjdk-17-jre -y
apt-get install jenkins -y
```
4. Afterward, enable Jenkins and start the service two the systemctl commands shown down below

## Final Script
```
#!/bin/bash
apt-get update
apt-get upgrade -y
wget -O /usr/share/keyrings/jenkins-keyring.asc https://pkg.jenkins.io/debian/jenkins.io-2023.key
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null
apt-get update
apt-get install fontconfig -y
apt-get install openjdk-17-jre -y
apt-get install jenkins -y
systemctl enable jenkins
systemctl start jenkins
```
