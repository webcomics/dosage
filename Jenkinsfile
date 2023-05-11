def pys = [
    [name: 'Python 3.10', docker: '3.10-bullseye', tox:'py310,flake8', main: true],
    [name: 'Python 3.9',  docker: '3.9-bullseye',  tox:'py39', main: false],
    [name: 'Python 3.8',  docker: '3.8-bullseye',  tox:'py38', main: false],
    [name: 'Python 3.7',  docker: '3.7-bullseye',  tox:'py37', main: false],
]

properties([
    durabilityHint('PERFORMANCE_OPTIMIZED'),
    buildDiscarder(logRotator(numToKeepStr: '100')),
])

Map tasks = [failFast: true]

pys.each { py ->
    tasks[py.name] = {
        node {
            stage("Checkout $py.name") {
                checkout scm
                sh '''
                    git clean -fdx
                    git fetch --tags
                '''
            }

            stage("Build $py.name") {
                def image = docker.image('docker.io/python:' + py.docker)
                image.pull()
                image.inside {
                    def tmpDir = pwd(tmp: true)
                    warnError('tox failed') {
                        sh """
                            HOME='$tmpDir'
                            pip install --no-warn-script-location tox
                            python -m tox -e $py.tox
                        """
                    }

                    if (py.main) {
                        sh """
                            HOME='$tmpDir'
                            pip install --no-warn-script-location build
                            python -m build
                        """
                    }
                }

                if (py.main) {
                    archiveArtifacts artifacts: 'dist/*', fingerprint: true
                    stash includes: 'dist/*.tar.gz', name: 'bin'
                    dir('.tox/reports') {
                        stash includes: '*/allure-data/**', name: 'allure-data'
                    }
                    def buildVer = findFiles(glob: 'dist/*.tar.gz')[0].name.replaceFirst(/\.tar\.gz$/, '')
                    currentBuild.description = buildVer

                    publishCoverage calculateDiffForChangeRequests: true,
                        sourceFileResolver: sourceFiles('STORE_LAST_BUILD'),
                        adapters: [
                            coberturaAdapter('.tox/reports/*/coverage.xml')
                        ]

                    recordIssues sourceCodeEncoding: 'UTF-8',
                        referenceJobName: 'dosage/master',
                        tool: flake8(pattern: '.tox/flake8.log', reportEncoding: 'UTF-8')
                }
                junit '.tox/reports/*/junit.xml'
            }
        }
    }
}

// MAIN //

parallel(tasks)
parallel modern: {
        stage('Modern Windows binary') {
            windowsBuild('3.10', 'dosage.exe')
        }
    },
    legacy: {
        stage('Legacy Windows binary') {
            // Still compatible with Windows 7
            windowsBuild('3.8', 'dosage-legacy.exe')
        }
    },
    report: {
        stage('Allure report') {
            processAllure()
        }
    }, failFast: true


def windowsBuild(pyver, exename) {
    warnError('windows build failed') {
        node {
            windowsBuildCommands(pyver, exename)
        }
    }
}

def windowsBuildCommands(pyver, exename) {
    deleteDir()
    unstash 'bin'

    def img = docker.image('docker.io/tobix/pywine:' + pyver)
    img.pull()
    img.inside {
        sh '''
            . /opt/mkuserwineprefix
            tar xvf dist/dosage-*.tar.gz
            cd dosage-*
            xvfb-run sh -c "
                wine py -m pip install -e .[css] &&
                cd scripts &&
                wine py -m PyInstaller -y dosage.spec;
                wineserver -w" 2>&1 | tee log.txt
        '''
        sh "mv */scripts/dist/*.exe $exename"
        archiveArtifacts '*.exe'
    }
}

def processAllure() {
    warnError('allure report failed') {
        node {
            deleteDir()
            unstash 'allure-data'
            sh 'mv */allure-data .'
            copyArtifacts filter: 'allure-history.zip', optional: true, projectName: JOB_NAME, selector: lastWithArtifacts()
            if (fileExists('allure-history.zip')) {
                unzip dir: 'allure-data', quiet: true, zipFile: 'allure-history.zip'
                sh 'rm -f allure-history.zip'
            }
            sh 'podman run --rm -v $PWD:/work --userns=keep-id docker.io/tobix/allure-cli generate allure-data'
            zip archive: true, dir: 'allure-report', glob: 'history/**', zipFile: 'allure-history.zip'
            publishHTML reportDir: 'allure-report', reportFiles: 'index.html', reportName: 'Allure Report'
        }
    }
}

// vim: set ft=groovy:
