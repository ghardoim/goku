#!/bin/bash

echo "Stage: Init"
  ultimaTag=$(git tag --sort=-creatordate | head -1)
  versao_PRD=$(echo $ultimaTag | sed -e 's/.*v\(.\)\..*/\1/')
  versao_RLS=$(echo $ultimaTag | sed -e 's/.*.\(.\)\../\1/')
  versao_SNP=$(echo $ultimaTag | sed -e 's/.*.\(.\)$/\1/')
  novaTag="sayajin-v$versao_PRD.$versao_RLS.$(expr $versao_SNP + 1)"

source pipe/pipeline.sh