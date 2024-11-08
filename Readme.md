# Django Translator App

This is a Django-based translation application that uses Docker to run and manage services. The app takes user input in a form and translates it into a specified language.

## Getting Started

### Prerequisites

- [Docker](https://www.docker.com/) installed on your system.

### Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ishijapriyansha/translate_app.git
   cd yourrepository

2. **Build the Docker images**:
    ```bash
    docker compose build

3. **Run the application in detached mode**
    ```bash
    docker compose up -d
This command starts the containers in the background.

### Usage

Access the application at http://localhost:8000
Follow the on-screen instructions to enter text and select a target language for translation.

### Stopping the application
    To stop the application, run:
    ```bash
    docker compose down
