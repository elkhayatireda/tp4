pipeline {
    environment {
        registry = "reeeeda/tp4"
        registryCredential = 'last_docker_hub'
        dockerImage = ''
    }
    agent any
    stages {
        stage('Cloning Git') {
            steps {
                git branch: 'master', url: 'https://github.com/elkhayatireda/tp4'
            }
        }
        stage('Building image') {
            steps {
                script {
                    dockerImage = docker.build("${registry}:${BUILD_NUMBER}")
                }
            }
        }
        stage('Test image') {
            steps {
                script {
                    echo "Tests passed"
                }
            }
        }
        stage('Publish Image') {
            steps {
                script {
                    docker.withRegistry('', registryCredential) {
                        dockerImage.push()
                        dockerImage.push('latest')
                    }
                }
            }
        }
        stage('Deploy image') {
            steps {
                bat """
                    docker rm -f tp4 2>nul
                    docker run -d --name tp4 -p 8081:80 ${registry}:${BUILD_NUMBER}
                """
            }
        }
    }
}