pipeline {
	agent any

	environment {
        IMAGE_NAME = "damducthoai/test-01"
		BUILD_TAG = "build-${BUILD_NUMBER}"
        REGISTRY = "docker.io"
		GIT_USER = "jenkins-bot"
        GIT_EMAIL = "nguyendamducthoai@gmail.com"
    }

	triggers {
		pollSCM 'H/10 * * * *'
	}

	options {
		disableConcurrentBuilds()
		buildDiscarder(logRotator(numToKeepStr: '14'))
	}

	stages {
		// stage("build container") {
		// 	options { timeout(time: 30, unit: 'MINUTES') }
		// 	steps {
        //         withCredentials([usernamePassword(credentialsId: 'dockerhub_id', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
        //                 sh '''
        //                     podman login -u ${DOCKER_USER} -p ${DOCKER_PASS} ${REGISTRY}
        //                     podman build -t ${IMAGE_NAME}:${BUILD_TAG} .
        //                     podman push ${IMAGE_NAME}:${BUILD_TAG}
        //                 '''
        //         }
				
		// 	}
		// }
		stage("update-manifests"){
			steps {
				withCredentials([usernamePassword(credentialsId: 'github-credentials', usernameVariable: 'GIT_USER', passwordVariable: 'GIT_PAT')]) {
					sh '''

						git config --global user.name "${GIT_USER}"
						git config --global user.email "${GIT_EMAIL}"

						git pull --rebase

						git remote set-url origin https://$GIT_USER:$GIT_PAT@github.com/nguyendamducthoai/nginx-demo.git

						cd kustomize/overlays/dev
						kustomize edit set image my-app=${IMAGE_NAME}:${BUILD_TAG}
						
						git add kustomization.yaml
						git commit -m "Automated commit from Jenkins"

						cd ../../../

						git status

						git push origin main
					'''
				}
				
			}
		}

	}
}