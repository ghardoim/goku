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

echo "Stage: Clean Pós-Build"
  removeLibs="dist/lib"
  rm -r $removeLibs/unittest
  rm -r $removeLibs/tkinter
  rm -r $removeLibs/xmlrpc
  rm -r $removeLibs/email
  rm -r $removeLibs/html
  rm -r $removeLibs/xml

echo "Stage: Copy Utils"
  cp sorteio.json dist/
  cp README.md dist/README.md

echo "Stage: push"
  git tag -a "$novaTag" -m "Com meu KI atual, eu consigo saber quem você segue para eu marcar"
  git merge $(git branch | grep \* | awk -F" " '{ print $2 }') master
  git switch master
  git push --tags

echo "Stage: Compile"
  tar -cf sayajin-v0.zip dist/