pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                // Construir la imagen Docker
                script {
                    docker.build('my-fastapi-app')
                }
            }
        }
        stage('Test') {
            steps {
                // Ejecutar pruebas si es necesario
                // Puedes agregar comandos para ejecutar tus pruebas aquí
            }
        }
        stage('Deploy') {
            steps {
                // Desplegar la aplicación con Docker Compose
                bat 'docker-compose up -d'
            }
        }
    }
}
