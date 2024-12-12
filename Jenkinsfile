pipeline {
    agent any  // Run on any available agent

    environment {
        PYTHON = 'python3'  // Specify python version if needed (adjust accordingly)
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the repository (if using version control like Git)
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install any required dependencies using pip (if there's a requirements.txt)
                sh '''
                    if [ -f requirements.txt ]; then
                        pip3 install -r requirements.txt
                    fi
                '''
            }
        }

        stage('Run Calculator') {
            steps {
                // Run the calc.py script
                sh 'python3 calc.py'
            }
        }
    }

    post {
        success {
            echo 'Calculator ran successfully!'
        }
        failure {
            echo 'There was an error running the calculator.'
        }
    }
}
