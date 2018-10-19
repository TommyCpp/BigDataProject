# BigDataProject

# PLAN

# Server
  <strong>#Connect Server</strong></br>
  Use TeamViewer to connect to server.</br>
  Server will be turn off after 11:00 pm.</br>
  Beacause my InternetyIP does not public IP, I need to use TeamViewer.</br>
  The TeamViewer ID and Password change each day.</br>
  Call me(Kaiwen Zhu) for the ID and Password to connect to the server, if you need to deploy your code and test it.</br>
  TeamViewer ServerID:</br>
  TeamViewer ServerPassWord:</br>

  Ubuntu 18.04</br>
  Operation System User: kevin</br>
  Operation System Password : 19950314</br>

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
