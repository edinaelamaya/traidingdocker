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
                
                bat \'python3 -m pip install -r requirements.txt\'
            }
        }
        stage(\'Test\') {
            steps {
                
                bat \'python3 -m pytest\' 
            }
        }
        stage(\'Deploy\') {
            steps {
                sh \'docker-compose up -d\'
            }
        }
        
    }
}
'''
        }
      }

    }
  }