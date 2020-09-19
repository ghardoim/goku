#!/bin/bash

echo "Stage: Clean"
  if [[ -d dist/ ]]
  then
    rm -r dist/
  fi

echo "Stage: Build"
  source .venv/Scripts/activate
  cxfreeze goku.py
  deactivate

echo "Stage: Copy Utils"
  cp sorteio.json dist/
  cp -r img/ dist/

echo "Stage: Deploy"
  branch=$(git branch | grep \* | awk -F" " '{ print $2 }')
  git push && git switch master
  git merge $branch && git push
  git tag -a "$novaTag" -m "Com meu KI atual, eu consigo saber quem você segue para eu marcar"
  git push --tags

echo "Stage: Compile"
  tar -cf $novaTag.zip dist/