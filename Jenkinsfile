pipeline {
	agent any

	environment {
        IMAGE_NAME = "damducthoai/test-01"
		BUILD_TAG = "build-${BUILD_NUMBER}"
        REGISTRY = "docker.io"
    }

	triggers {
		pollSCM 'H/10 * * * *'
	}

	options {
		disableConcurrentBuilds()
		buildDiscarder(logRotator(numToKeepStr: '14'))
	}

	stages {
		stage("build container") {
			options { timeout(time: 30, unit: 'MINUTES') }
			steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub_id', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                        sh '''
                            podman login -u ${DOCKER_USER} -p ${DOCKER_PASS} ${REGISTRY}
                            podman build -t ${IMAGE_NAME}:${BUILD_TAG} .
                            podman push ${IMAGE_NAME}:${BUILD_TAG}
                        '''
                }
				
			}
		}

	}
}