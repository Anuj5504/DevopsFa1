pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Compiling C program...'
                sh 'gcc -o hello hello.c'
            }
        }
    }
}
