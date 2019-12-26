#!/bin/sh
set -e

P="$(mktemp -d)"
mkdir "$P/git" "$P/out"

if [ "$encrypted_1671ba5f199a_key" ]
then
    eval "$(ssh-agent -s)"
    openssl aes-256-cbc -K "$encrypted_1671ba5f199a_key" \
        -iv "$encrypted_1671ba5f199a_iv" \
        -in .github/deploy_key.enc -out .github/deploy_key -d
    chmod 600 .github/deploy_key
    ssh-add .github/deploy_key

    pip install git+https://github.com/spanezz/staticsite.git@v1.2
fi

git clone --depth=10 --branch=gh-pages "git@github.com:${TRAVIS_REPO_SLUG}.git" "$P/git"

rm -Rfv dosage.egg-info
ssite build --output "$P/out"

rsync -r --del --verbose --exclude tests \
    --exclude dosagelib --exclude dist --exclude build --exclude scripts \
    "$P/out/"* "$P/git"

cd "$P/git"

git config user.email 'nobody@23.gs'
git config user.name 'Travis-CI Website Bot'
git config push.default simple

git add -A .
if [ "$TRAVIS_COMMIT" ]
then
	git commit -a -m "Update website from commit $TRAVIS_COMMIT" || true
	git push origin HEAD:gh-pages
fi

