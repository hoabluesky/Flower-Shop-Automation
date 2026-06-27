pipeline {
    agent any

    stages {

        stage('Create Virtual Environment') {
            steps {
                bat 'python -m venv venv'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'venv\\Scripts\\python.exe -m pip install -r requirements.txt'
            }
        }

        stage('Install Playwright') {
            steps {
                bat 'venv\\Scripts\\python.exe -m playwright install chromium'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'venv\\Scripts\\python.exe -m pytest --html=reports\\report.html --self-contained-html'
            }
        }
    }
}