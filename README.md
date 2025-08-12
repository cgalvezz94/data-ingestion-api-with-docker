# Data-Ingestion-API-with-Docker

## 📌 Project Description
This project is the implementation of the **Globant Data Engineering Coding Challenge**, which aims to simulate a **database migration** scenario using three related tables:
- **departments**
- **jobs**
- **hired_employees**

The goal is to design and implement a **local REST API** that:
1. Stores historical data from CSV files.
2. Uploads these files into a new SQL database.
3. Supports **batch inserts** of up to 1000 rows in a single request.
4. Exposes SQL-based metrics through additional API endpoints.

**Assumptions**
1. The initial CSV upload endpoint loads and manages the full master data, including departments, jobs, and employees.
2. The batch insert endpoint only handles inserting new employees as transactions. 
3. It is assumed that the departments and jobs referenced by new employees already exist and are valid.
4. No batch update or batch insert is performed on departments or jobs in this version.


The solution also includes:
- Cloud hosting on **AWS**.
- Containerization with **Docker**.
- Automated testing.
- Documentation and code organization with best practices.

---

## 🚀 Features
- **Upload CSV files** for departments, jobs, and employees.
- **Batch insert** between 1 and 1000 records per request.
- **Explore and query** the uploaded data through dedicated endpoints.
- **SQL queries** to:
  - Count hires per quarter in 2021, grouped by department and job.
  - List departments with hires above the 2021 average.
- **Automated tests** for API functionality.
- **Dockerized application** for local and cloud deployments.
- **AWS-ready** architecture.

---

## 🛠 Tech Stack
**Programming Language**
- [Python 3.x](https://www.python.org/)

**Frameworks & Libraries**
- [FastAPI](https://fastapi.tiangolo.com/) – REST API framework with automatic Swagger docs.
- [SQLAlchemy](https://www.sqlalchemy.org/) – ORM for database modeling and queries.
- [Pandas](https://pandas.pydata.org/) – CSV parsing and data manipulation.
- [Pytest](https://docs.pytest.org/) – Testing framework.

**Database**  
- [SQLite](https://www.sqlite.org/index.html) – Lightweight, file-based SQL database used locally within the container for simplicity and cost-efficiency.

**Containerization**
- [Docker](https://www.docker.com/) – For packaging and running the application.

**Cloud Services**
- [Amazon ECR](https://aws.amazon.com/ecr/) – Fully managed container registry offering high-performance hosting.

---

## Deployment

- The Docker image is built and automatically pushed to a public Amazon ECR repository using GitHub Actions workflows.
- This automation ensures the latest image version is available publicly without manual intervention.


---

## Project Structure

my-project/
├──.github/ # Github Actions
├──docker/ # Dockerfile
├── src/ # Source code 
│ ├── api/ # API endpoint modules
│ │  ├── upload.py
│ │  ├── batch_insert.py
│ │  ├── requirement_1.py
│ │  ├── requirement_2.py
│ ├── data/ # Sample CSV files
│ │  ├── departments.csv
│ │  ├── hired_employees.csv
│ │  ├── jobs.csv
│ ├── sql/ # SQL scripts
│ │  ├── requirement_1.sql
│ │  ├── requirement_2.sql
│ ├── config.py 
│ └── main.py # API entry point
├── tests/ # Automated test files
│   ├── test_upload.py
│   ├── test_batch_insert.py
│   ├── test_requirement_1.py
│   ├── test_requirement_2.py
│   └── __init__.py  
├──README.md # This file 
└──requirements.txt # Python dependencies

---


## Design Decisions

- **High cohesion**: Each file in api/*.py has a clear and focused responsibility.

- **Modularity**: You can develop, test, and maintain each endpoint separately.

- **Low coupling**: main.py imports these modules but contains no business logic, it only registers them in the API.

- **Organized tests**: Each test targets its corresponding module, making it easy to scale and maintain.

- **Clear separation**: CSV and SQL files are kept outside of the code logic, which is ideal.


---


## 🏗 Architecture Overview

Due to the nature of this challenge, the monolithic architecture naturally suits better for this (single deploy
ment unit of all code). This style of architecture is the de facto standard for most applications, primarily because of its simplicity, familiarity, and low cost.

- **API Layer**  
  - Built with FastAPI  
  - Handles CSV ingestion, batch inserts, and query endpoints  
  - Runs inside a Docker container

- **Database Layer**  
  - SQLite database running inside the Docker container (non-persistent)  
  - Stores departments, jobs, and employees data temporarily during container runtime. 
  - Data is reset each time the container restarts

- **Storage Layer**  
  - Raw CSV files stored locally inside the container in the `/data/` folder  
  - API loads data from these local CSV files upon startup or request

- **Containerization**  
  - Docker is used to package the application into a container image.  
  - The Docker image is pushed to a public Amazon ECR repository for easy sharing and distribution.  
  - Deployment to ECS Fargate or other container orchestration services is not included in this version.


---

## 🔮 Possible Future Improvements

Although this project fulfills the requirements of the challenge, here are some ideas for potential enhancements in a production environment:

- Use a persistent database such as Amazon RDS (PostgreSQL) instead of SQLite to ensure data durability and scalability.

- Implement CSV file storage and retrieval from Amazon S3 to decouple data storage from the application container.

- Add more comprehensive error handling and input validation to improve robustness.

- Expand automated testing coverage to include integration and load tests.

- Secure API endpoints with authentication and authorization mechanisms.

- Implement logging and monitoring with AWS CloudWatch or other tools for better observability.

- Container orchestration with Kubernetes or ECS service autoscaling for higher availability and scalability.

These improvements would make the solution more production-ready and scalable beyond the scope of the current challenge.

---

## ✉️ Contact / Author

- **Name:** Camilo Gálvez Zúñiga  
- **Email:** cgalvezz@udd.cl  
- **LinkedIn:** (https://www.linkedin.com/in/camilogalvez12/)