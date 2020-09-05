#!/bin/bash

echo "Stage: Clean"
  if [[ -d dist/ ]]
  then
    rm -r dist/
  fi

echo "Stage: Build"
  cxfreeze goku.py

echo "Stage: Clean Pós-Build"
  rm -r dist/lib/unittest
  rm -r dist/lib/tkinter
  rm -r dist/lib/xmlrpc
  rm -r dist/lib/email
  rm -r dist/lib/html
  rm -r dist/lib/http
  rm -r dist/lib/xml

echo "Stage: Copy Utils"
  cp sorteio.json dist/
  cp README.md dist/README.md

echo "Stage: Compile"
  tar -cf sayajin-v0.zip dist/