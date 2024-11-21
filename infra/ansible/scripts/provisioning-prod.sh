#!/usr/bin/env bash

set -Eeuo pipefail

export ANSIBLE_HOST="tournesol-prod"
export DOMAIN_NAME="tournesol.app"

CURRENT_DIR="$(realpath -e "$(dirname "$0")")"

cd "$CURRENT_DIR/.."

./scripts/deploy-without-secrets.sh "${1:-"notapply"}" "${2:-"notfast"}"