#!/usr/bin/env python3

import subprocess

def runTasks(tasks):
    for task in tasks:
        print(task[0],end=" => ")
        output = subprocess.run(task[1],capture_output=True,shell=True,text=True)
        if output.returncode==0:
            print("Done")
        else:
            print("Error")
            print(output.stderr.strip())
            break
tasks = []
tasks.append([
        "Adding Jenkins Keys",
        """wget -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -"""
])

tasks.append(
    [
        "Adding Jenkins Repo",
        """echo deb https://pkg.jenkins.io/debian-stable binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list"""
    ]
)

tasks.append(
    [
        "Syncing System Repos",
        """sudo apt update"""
    ]
)
tasks.append(
    [
    "Installing jenkins / jre",
    """sudo apt install default-jre jenkins -y"""
    ]
)
tasks.append(
    [
    "Disable Docker Permission Denied",
    """sudo chmod 666 /var/run/docker.sock"""
    ]
)
tasks.append(
    [
        "Running Sonarqube",
        """docker run -d -p 9000:9000 -v sonarqube_conf:/opt/sonarqube/sconf -v sonarqube_extensions/opt/sonarqube/extensions -v sonarqube_logs:/opt/sonarqube/logs -v sonarqube_data:/opt/sonarqube/data sonarqube"""
    ]
)
tasks.append(
    [
        "Starting jenkins ",
        """sudo service jenkins start"""
    ]
)
runTasks(tasks)
