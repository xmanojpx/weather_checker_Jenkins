pipeline {
    agent any

    environment {
        PYTHON_PATH = '/usr/bin/python3'
        PIP_PATH = '/usr/bin/pip3'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                checkout scm
            }
        }
        
        stage('Setup Python Environment') {
            steps {
                echo 'Setting up Python environment...'
                sh '''
                    ${PIP_PATH} install virtualenv
                    virtualenv venv
                    . venv/bin/activate
                    ${PIP_PATH} install -r requirements.txt
                '''
            }
        }
        
        stage('Lint') {
            steps {
                echo 'Running linting...'
                sh '''
                    . venv/bin/activate
                    ${PIP_PATH} install flake8
                    flake8 weather.py test_weather.py
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                sh '''
                    . venv/bin/activate
                    pytest test_weather.py -v --junitxml=test-results/junit.xml
                '''
            }
        }
    }
    
    post {
        always {
            junit 'test-results/junit.xml'
            cleanWs()
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
} 