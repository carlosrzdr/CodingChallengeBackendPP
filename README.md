# Coding Challenge Backend

_Simple instructions on how to set up the app_

### Prequisites 📋

_Docker must be installed to run the app_

### Clone GitHub repository 📦

_Clone the repository and move into the folder_

```
git clone https://github.com/carlosrzdr/CodingChallengeBackendPP
cd CodingChallengeBackendPP
```

### Build container image 🔧

_Execute the following command to build the image. The name given to the image is flask-app-container_

```
docker image build -t flask-app .
```


## Deployment 🚀

_To start the app start the docker container and bind the host's port to the port 5000 in flask-app_

_In this example, the port binded from the host is 5001_

```
docker run -p 5001:5000 -d flask-app --name flask-app-container
```

_Now travel to http://localhost:5001 to access the app_

### Execute tests ⚙️

_To execute the tests, move into the docker container_

```
docker exec -it flask-app-container bash
```

_And execute the tests with pytest_

```
python -m pytest tests
```