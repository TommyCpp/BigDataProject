# BigDataProject

# PLAN

# Server: http://52.87.181.158:8081/
  Server IP：52.87.181.158
  Public Port: 8081

  Ubuntu 18.04</br>
  System Id:root</br>
  System Password : 19950314</br>
  
  Public Key: BigDataProject\Server\Kevin\.ssh\MyKey.pem
  
  Connect Way:
  Download Git Bash
  Right Click -> Click "Git Bash Here" -> Type in following command:
  ```
   ssh -i 'C:\Studio\BigDataProject\Server\Kevin\.ssh\MyKey.pem' ubuntu@52.87.181.158
  ```
  "C:\Studio\BigDataProject\Server\Kevin\.ssh\MyKey.pem" is the place where the MyKey.pem stays in your computer
  

  <strong>#Config Server</strong></br>
  #Install Oracle Java8</br>
  sudo add-apt-repository ppa:webupd8team /java // we need to run this command for install java.</br>
  sudo apt-get update // using this command all dependency will be updated.</br>
  sudo apt-get install oracle-java8-installer // now using this command java will be installed.</br>
  sudo apt-get update // using this command all dependency will be updated.</br>

  <strong>#Intall Neo4j</strong></br>
  wget -O - https://debian.neo4j.org/neotechnology.gpg.key | sudo apt-key add -</br>
  echo 'deb http://debian.neo4j.org/repo stable/' >/tmp/neo4j.list</br>
  sudo mv /tmp/neo4j.list /etc/apt/sources.list.d</br>
  sudo apt-get update // using this command all dependency will be updated</br>

  <strong>#Use Neo4j</strong></br>
  Ctrl+Alt+t calls the Terminal</br>
  Enter "service neo4j start"</br>
  Enter “http://localhost:7474/browser/” in firefox browser for using the neo4j</br>
  "service neo4j status"//check status</br>
  "service neo4j restart"//restart</br>
  "sudo su"//run command as root</br>
