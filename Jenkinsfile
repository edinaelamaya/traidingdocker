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
                // Ejemplo de instalación de dependencias con pip en Windows
                bat \'python -m pip install -r requirements.txt\' // Reemplaza python con python3 si es necesario
            }
        }
        stage(\'Test\') {
            steps {
                // Ejemplo de ejecución de pruebas con pytest en Windows
                bat \'python -m pytest\' // Reemplaza python con python3 si es necesario
            }
        }
        // Puedes agregar más etapas según sea necesario
    }
}
'''
        }
      }

      stage('Test') {
        steps {
          sh '''pipeline {
    agent any

    stages {
        stage(\'Build\') {
            steps {
                // Ejemplo de instalación de dependencias con pip en Windows
                bat \'python -m pip install -r requirements.txt\' // Reemplaza python con python3 si es necesario
            }
        }
        stage(\'Test\') {
            steps {
                // Ejemplo de ejecución de pruebas con pytest en Windows
                bat \'python -m pytest\' // Reemplaza python con python3 si es necesario
            }
        }
        // Puedes agregar más etapas según sea necesario
    }
}
'''
          }
        }

      }
    }