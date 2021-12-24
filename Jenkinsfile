pipeline {
    environment{
        PASS=credentials('dockerToken')
    }
    agent any
        stages {
        stage('Build') {
            steps {
                sh'''
                    docker build -t muhammad2000/fronttest ./Integration
                '''
            }
        }
        stage('Deploy') {
            steps {
                sh'''
                    docker login -u muhammad2000 -p $PASS
                    docker push muhammad2000/fronttest
                '''
            }
        }
    }
}
