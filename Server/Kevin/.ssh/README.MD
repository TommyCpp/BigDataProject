- Download Git for Windows here. Run the downloaded installer accepting the default settings (this will install Git Bash as part of Git).
- Right click on your desktop (not on an icon or file) and select Git Bash Here to open a Git Bash command prompt.
- Use SSH to connect to your instance. In this case the user name is ec2-user, the SSH key is stored in the directory we saved it to in step 3 part d, and the IP address is from step 3 part f. The format is:
```
ssh -i 'C:\Studio\BigDataProject\Server\Kevin\.ssh\MyKey.pem' ubuntu@52.87.181.158
```
