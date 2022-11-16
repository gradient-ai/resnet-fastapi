# FastAPI-deployment

### ![FastAPI](images/FastAPI_logo.png)

### **About the Gradient Deployment**

This repository contains a project used to deploy a FastAPI application using a Gradient Deployment. 

Follow this [blog post](https://blog.paperspace.com/fast-track-to-deployments/) for a detailed description of how to setup and use this project.


### **Built With**

This project is designed to deploy on Gradient using FastAPI. As you notice in the Dockerfile, the Docker image is built using the Paperspace FastAPI deployment image ```paperspace/fastapi-deployment```. That base image is hosted on [Docker Hub](https://hub.docker.com/r/paperspace/fastapi-deployment).

### **Usage**

Use this repo as reference to the [blog post](https://blog.paperspace.com/fast-track-to-deployments/) describing how to serve your model on Gradient using FastAPI.

### **Limitations and Bias**

This project does not include a trained model but the model intended to be used in conjunction with this deployment outline is a ResNet model of various sizes.