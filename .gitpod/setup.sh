commands=(
    # Adding Jenkins Key
    "wget -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -"

    # Adding Jenkins repo
    "echo deb https://pkg.jenkins.io/debian-stable binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list"

    # Syncing repos
    "sudo apt update"

    # Installing jenkins / jre
    "sudo apt install default-jre jenkins -y"

    # Disable Docker Permission Denied
    "sudo chmod 666 /var/run/docker.sock"

    # Running Sonarqube
    "docker run -d -p 9000:9000 -v sonarqube_conf:/opt/sonarqube/sconf -v sonarqube_extensions/opt/sonarqube/extensions -v sonarqube_logs:/opt/sonarqube/logs -v sonarqube_data:/opt/sonarqube/data sonarqube"

    # Starting jenkins 
    "sudo service jenkins start"
)
for command in "${commands[@]}"; do
    echo "RUNNING: ${command}" &&
    eval $command > /dev/null 2>&1 &&
    echo "DONE"
done
