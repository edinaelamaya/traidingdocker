pipeline {
  agent any
  stages {
    stage('Build') {
      agent any
      steps {
        sh '''pipeline {
    agent any

    stages {
        stage(\'Build\') {
            steps {
                // Aqu� puedes agregar cualquier paso de construcci�n necesario para tu proyecto Python
                sh \'python3 -m pip install -r requirements.txt\' // Instala las dependencias si es necesario
            }
        }
        stage(\'Test\') {
            steps {
                // Ejecuta tus pruebas en Python
                sh \'python3 -m pytest\' // Ejecuta tus pruebas con pytest como ejemplo
            }
        }
        // Puedes agregar m�s etapas seg�n sea necesario, como etapas de despliegue, etc.
    }
}'''
        }
      }

    }
  }