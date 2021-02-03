pipeline {
    agent none
    stages {
        stage("Env set") {
            agent any
            steps {
                checkout scm
                script {
                    // Set app env
                    env.appName = sh (script:"basename `git rev-parse --show-toplevel`",returnStdout: true)
                    env.pwd = sh (script:"pwd",returnStdout: true)
                    // Git committer name
                    env.git_commit_name = sh (script: "git --no-pager show -s --format='%an' $GIT_COMMIT",returnStdout: true).trim()
                    echo "Git committer name: ${env.git_commit_name}"
                    // Git committer email
                    env.git_commit_email = sh (script: "git --no-pager show -s --format='%ae' $GIT_COMMIT",returnStdout: true).trim()
                    echo "Git committer email: ${env.git_commit_email}"
                }
            }
        }
        stage("Unit test") {
            agent {
                docker {
                    image "python:3.9.1-buster"
                }
            }
            steps {
                echo "make install"
                sh "make install"
                echo "make lint"
                sh "make lint"
                echo "make coverage"
                sh "make coverage"
            }
        }

        stage("Deploy to env") {
            when {
                anyOf {
                    branch 'develop';
                    branch 'master';
                }
            }
            agent any
            steps {
                sh "make deploy"
            }
        }
    }
    post {
        success {
            script {
                mail to: "${env.git_commit_email}",
                subject: "[Jenkins] SUCCESSFUL: ${env.appName} [${env.BUILD_NUMBER}]",
                body: """SUCCESSFUL: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'
分支: ${env.BRANCH_NAME}
JOB_NAME: ${env.JOB_NAME}
提交人: ${env.git_commit_name}
构建次数：${env.BUILD_NUMBER}
console output：${env.BUILD_URL}
                """
            }
        }
        failure {
             script {
                mail to: "${env.git_commit_email}",
                subject: "[Jenkins] FAILURE: ${env.appName} [${env.BUILD_NUMBER}]",
                body: """<p>SUCCESSFUL: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'
分支: ${env.BRANCH_NAME}
JOB_NAME: ${env.JOB_NAME}
提交人: ${env.git_commit_name}
构建次数：${env.BUILD_NUMBER}
console output：${env.BUILD_URL}
                """
             }
        }
    }
}