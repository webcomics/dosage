def pys = [
    [name: 'Python 3.7', docker:'python:3.7-stretch', tox:'py37,flake8', main: true],
    [name: 'Python 3.6', docker:'python:3.6-stretch', tox:'py36', main: false],
    [name: 'Python 3.5', docker:'python:3.5-jessie', tox:'py35', main: false],
    [name: 'Python 2.7', docker:'python:2.7-stretch', tox:'py27', main: false]
]

properties([
    durabilityHint('PERFORMANCE_OPTIMIZED'),
    buildDiscarder(logRotator(numToKeepStr: '5')),
])

Map tasks = [failFast: true]

pys.each { py ->
    tasks[py.name] = {
        node {
            def image

            stage("Prepare docker $py.name") {
                dir('dockerbuild') {
                    deleteDir()
                    buildDockerfile(py.docker)
                    image = docker.build("dosage-$py.docker")
                }
            }

            stage("Build $py.name") {
                image.inside {
                    checkout scm
                    sh '''
                        git clean -fdx
                        git fetch --tags
                    '''

                    try {
                        sh "tox -e $py.tox"
                    } catch (err) {
                        echo "tox failed: ${err}"
                        currentBuild.result = 'UNSTABLE'
                    }

                    if (py.main) {
                        sh """
                            python setup.py sdist bdist_wheel
                        """
                    }
                }
            }

            stage ("Archive $py.name") {
                archiveArtifacts artifacts: '.tox/dist/*.zip', fingerprint: true
                if (py.main) {
                    archiveArtifacts artifacts: 'dist/*', fingerprint: true
                    stash includes: 'dist/*.tar.gz', name: 'bin'
                    def buildVer = findFiles(glob: 'dist/*.tar.gz')[0].name.replaceFirst(/\.tar\.gz$/, '')
                    currentBuild.description = buildVer

                    cobertura autoUpdateHealth: false,
                        autoUpdateStability: false,
                        coberturaReportFile: '.tox/cov-*.xml',
                        failUnhealthy: false,
                        failUnstable: false,
                        maxNumberOfBuilds: 0,
                        onlyStable: false,
                        zoomCoverageChart: false
                    warnings consoleParsers: [[parserName: 'flake8']]
                }
                junit '.tox/junit-*.xml'
            }
        }
    }
}

timestamps {
    ansiColor('xterm') {
        parallel(tasks)
        windowsBuild()
    }
}

def buildDockerfile(image) {
    def uid = sh(returnStdout: true, script: 'id -u').trim()
    def toxInst = 'apt-get update && apt-get -y install tox'
    if (image.contains('jessie')) {
        toxInst = 'pip install tox' // Dirty!
    }

    writeFile file: 'Dockerfile', text: """
    FROM $image
    RUN $toxInst
    RUN useradd -mu $uid dockerjenkins
    """
}

def windowsBuild() {
    node {
        deleteDir()
        unstash 'bin'
        docker.image('tobix/pywine').inside {
            sh '''
                . /opt/mkuserwineprefix
                tar xvf dist/dosage-*.tar.gz
                cd dosage-*
                xvfb-run sh -c "
                    wine py -m pip install -e .[css] &&
                    cd scripts &&
                    wine py -m PyInstaller -y dosage.spec;
                    wineserver -w" | tee log.txt
            '''
            archiveArtifacts '*/scripts/dist/*'
        }
    }
}

// vim: set ft=groovy:
