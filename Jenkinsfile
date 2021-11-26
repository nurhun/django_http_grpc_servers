pipeline {

    agent any
    
    // Allow Github webhook integration.
    triggers {
        githubPush()
    }
    
    environment {
        IMAGE_NAME = "nurhun/django_crud"
        COMMIT_SHA = getCommitSHA()
        IMAGE_TAG = "v${BUILD_NUMBER}.${COMMIT_SHA}"
    }
    
    stages {
        stage('Build') {
            steps {
                container('jnlp'){
                    sh "docker build . -t ${IMAGE_NAME}:${IMAGE_TAG}"
                }
            }
        }

        stage('Push') {
            steps {
                script {                  
                    withDockerRegistry(credentialsId: 'DockerHub') {
                        sh "docker push ${IMAGE_NAME}:${IMAGE_TAG}"
                        sh "docker tag ${IMAGE_NAME}:${IMAGE_TAG} ${IMAGE_NAME}:latest"
                        sh "docker push ${IMAGE_NAME}"
                    }
                }
            }
        }
        
    }
}

// Get the commit SHA hash number to easily identify the exact commit where the image was build.
def getCommitSHA(){
    sh "git rev-parse --short HEAD > .git/current-commit"
    return readFile(".git/current-commit").trim()
}