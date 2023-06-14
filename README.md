# Ali Rafieefar's Graudit Dockerization and API Implementation Task

Hi, I am Ali Rafieefar, and this repository contains the implementation of a task for containerizing the Graudit tool and creating an API for scanning projects. You can find my GitHub profile [here](https://github.com/aliraf62) and my LinkedIn profile [here](https://www.linkedin.com/in/ali-rafieefar).

## Task Description

The objective of this repository is to create a Dockerized version of the Graudit tool, which scans source code for vulnerabilities in projects. The Graudit tool, available at https://github.com/wireghoul/graudit/, will be incorporated into a containerized environment that does not have internet access. Additionally, an API will be developed to serve as an interface for the Graudit tool. The API will receive a project's source code in the form of a .zip archive and provide the scan results in JSON format.


## Repository Structure

This repository contains two versions of the task implementation:

### Version 1

This version includes the basic implementation of the task. It contains the following files:

- **Dockerfile**: Docker configuration file.
- **graudit_api_test_Ali.py**: Python script that defines the API.
- **python_requirements.txt**: Python dependencies file.

To build and run the Docker container, use the following commands:

```bash
docker build -t ali_rafieefar_graudit_image .
docker run -p 5000:5000 ali_rafieefar_graudit_image
```

To use the API, use the following command:

```bash
curl admin:secret -X POST -F "file=@<path_to_your_code_zip_file>" http://localhost:5000/endpoint
```

### Version 2

This version includes additional security and error handling features. It contains the following files:

- **Dockerfile**: Docker configuration file.
- **app.py**: Python script that defines the API with enhanced error handling.
- **requirements.txt**: Python dependencies file.

To build and run the Docker container, use the following commands:

```bash
docker build -t graudit_version2_ali .
docker run -p 5000:5000 graudit_version2_ali
```

To use the API, use the following command:

```bash
curl -X POST -F "file=@<relative_or_absolute_path_to_your_project_zip_file>" http://localhost:5000/endpoint
```

## Final Notes

Please note that the code in this repository should be improved upon, especially the Version 2, which is currently untested. Feedback and contributions are welcome. 

In case of any questions or issues, please create an issue in this repository. I will do my best to respond as soon as possible. Thank you!
