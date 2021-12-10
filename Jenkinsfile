pipeline {
    agent any
        stages {
        stage('Build') {
            steps {
                sh'''
                    docker build -t muhammad2000/fronttest ./Integration
                '''
            }
        }
    }
}
