# Build and Run Docker

**Build Docker**
```
sudo docker build -t dockerpython .
```

**Run Docker**
```
sudo docker run -p 5000:5000 dockerpython
```

## If wanting to save token to environment variables. To get into a docker container shell (dockerpython is the name of the image and SOMENAME is the name of the container). 

**First run docker**
```
docker run -p 4000:80 --name SOMENAME dockerpython 
```

**Get into the shell**
```
sudo docker exec -it SOMENAME bash
```
**Save environment variable into root/.bashrc either through command line or install vim/nano**

**One liner to insert to first line**

```
sed -i '1 i\export COINBOT_TOKEN="<token>"' root/.bashrc
```
