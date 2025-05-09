def pys = [
    [name: 'Python 3.13', docker: '3.13-bookworm', tox:'py313', main: true],
    [name: 'Python 3.12', docker: '3.12-bookworm', tox:'py312', main: false],
    [name: 'Python 3.11', docker: '3.11-bookworm', tox:'py311', main: false],
    [name: 'Python 3.10', docker: '3.10-bookworm', tox:'py310', main: false],
    [name: 'Python 3.9',  docker: '3.9-bookworm',  tox:'py39',  main: false],
    [name: 'Python 3.8',  docker: '3.8-bookworm',  tox:'py38',  main: false],
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
                            pip install --no-warn-script-location build pre-commit
                            python -m build
                            python -m pre_commit run --all-files || true
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

                    recordCoverage sourceCodeEncoding: 'UTF-8', tools: [
                        [parser: 'COBERTURA', pattern: '.tox/reports/*/coverage.xml']
                    ]

                    recordIssues sourceCodeEncoding: 'UTF-8',
                        referenceJobName: 'dosage/master',
                        tool: flake8(reportEncoding: 'UTF-8')
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
            windowsBuild('3.13', 'dosage.exe')
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
                wine python -m pip install .[css] &&
                cd scripts &&
                wine python -m PyInstaller -y dosage.spec;
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
