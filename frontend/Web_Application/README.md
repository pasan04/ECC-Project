This repository contains contents for launching a streamlit webapp via docker container.

To launch on your local machine:

Clone the GitHub repository to your local machine using the following command: 
git clone https://github.com/pasan04/ECC-Project.git


Change Directory to project directory: 
cd ECC-Project/frontend/Web_Application


Build the Docker container using the provided Dockerfile: docker build -t cloud_comp_project -f "path\to\your\project\directory\Dockerfile.txt" .

Run the Docker Container: docker run -p 8501:8501 cloud_comp_project

Access the Web App: http://localhost:8501
