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
                // Ejemplo de instalaci�n de dependencias con pip en Windows
                bat \'python -m pip install -r requirements.txt\' // Reemplaza python con python3 si es necesario
            }
        }
        stage(\'Test\') {
            steps {
                // Ejemplo de ejecuci�n de pruebas con pytest en Windows
                bat \'python -m pytest\' // Reemplaza python con python3 si es necesario
            }
        }
        // Puedes agregar m�s etapas seg�n sea necesario
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
                // Ejemplo de instalaci�n de dependencias con pip en Windows
                bat \'python -m pip install -r requirements.txt\' // Reemplaza python con python3 si es necesario
            }
        }
        stage(\'Test\') {
            steps {
                // Ejemplo de ejecuci�n de pruebas con pytest en Windows
                bat \'python -m pytest\' // Reemplaza python con python3 si es necesario
            }
        }
        // Puedes agregar m�s etapas seg�n sea necesario
    }
}
'''
          }
        }

      }
    }