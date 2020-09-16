#!/bin/bash

echo "Stage: Init"
  versao_PRD=$(git tag --sort=-creatordate | head -1 | sed -e 's/.*v\(.\)\..*/\1/')
  novaTag="sayajin-v$(expr $versao_PRD + 1).0.0"

source pipe/pipeline.sh