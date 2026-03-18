# Decentralized Voting System on Web3 Auto

## Overview
The Decentralized Voting System on Web3 Auto is an innovative platform designed to facilitate secure and transparent voting processes using blockchain technology. This system addresses the need for a reliable and tamper-proof voting mechanism, ensuring that elections are conducted with integrity and transparency. The platform is accessible through a web-based interface, allowing users to register, view candidates, cast their votes, and access real-time results. It is particularly beneficial for organizations, communities, or any groups seeking to implement a trustworthy voting solution.

## Features
- **User Registration**: Secure registration process that assigns unique user IDs to voters, ensuring each participant can only vote once.
- **Candidate Listing**: Dynamic display of candidates along with their respective parties, providing voters with the necessary information to make informed decisions.
- **Voting Mechanism**: A straightforward and secure voting process that guarantees the integrity of each vote cast.
- **Real-time Results**: Immediate access to voting outcomes presented in a user-friendly format, ensuring transparency throughout the election.
- **Responsive Design**: A user interface designed to be accessible across various devices, enhancing user experience.
- **Data Security**: Utilizes SQLite for secure storage and management of user and vote data, ensuring data integrity.

## Tech Stack
| Technology   | Description                            |
|--------------|----------------------------------------|
| Python       | Programming language for backend logic |
| FastAPI      | Web framework for building APIs        |
| Uvicorn      | ASGI server for running FastAPI apps   |
| SQLAlchemy   | ORM for database interactions          |
| SQLite       | Database for storing user and vote data|
| HTML/CSS/JS  | Frontend technologies for UI           |
| Docker       | Containerization for deployment        |

## Architecture
The project architecture consists of a FastAPI backend that serves HTML templates for the frontend. The backend processes API requests related to user registration, voting, and results retrieval, while the SQLite database manages user, candidate, and vote information.

```plaintext
+------------------+      +------------------+
| Frontend (HTML)  | <--> | Backend (FastAPI)|
+------------------+      +------------------+
        |                         |
        v                         v
+------------------+      +------------------+
| Static Files     |      | SQLite Database  |
+------------------+      +------------------+
```

## Getting Started

### Prerequisites
- Python 3.11+
- pip (Python package manager)
- Docker (optional, for containerized deployment)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/decentralized-voting-system-on-web3-auto.git
   cd decentralized-voting-system-on-web3-auto
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application
To start the application, run the following command:
```bash
uvicorn app:app --reload
```
Visit `http://localhost:8000` in your web browser to access the application.

## API Endpoints
| Method | Path            | Description                                |
|--------|-----------------|--------------------------------------------|
| GET    | /               | Home page with welcome message             |
| GET    | /register       | Registration page                          |
| GET    | /candidates     | Page displaying list of candidates         |
| GET    | /vote           | Voting page                                |
| GET    | /results        | Results page displaying voting outcomes    |
| POST   | /api/register   | API endpoint for user registration         |
| GET    | /api/candidates | API endpoint to retrieve candidates list   |
| POST   | /api/vote       | API endpoint to submit a vote              |
| GET    | /api/results    | API endpoint to retrieve voting results    |

## Project Structure
```
.
├── app.py              # Main application file with FastAPI routes
├── Dockerfile          # Docker configuration file
├── requirements.txt    # Python dependencies
├── start.sh            # Shell script to start the application
├── static              # Static files (CSS, JS)
│   ├── css
│   │   └── style.css   # Stylesheet for the application
│   └── js
│       └── main.js     # JavaScript for client-side logic
├── templates           # HTML templates for frontend
│   ├── candidates.html # Candidates listing page
│   ├── index.html      # Home page
│   ├── register.html   # User registration page
│   ├── results.html    # Voting results page
│   └── vote.html       # Voting page
```

## Screenshots
*Screenshots of the application in action will be added here.*

## Docker Deployment
To deploy the application using Docker, follow these steps:
1. Build the Docker image:
   ```bash
   docker build -t decentralized-voting-system .
   ```
2. Run the Docker container:
   ```bash
   docker run -d -p 8000:8000 decentralized-voting-system
   ```
Access the application at `http://localhost:8000`.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes. Ensure your code adheres to the project's coding standards and includes appropriate tests.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---
Built with Python and FastAPI.
