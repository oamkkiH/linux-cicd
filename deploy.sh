#!/bin/bash
set -e

# Mene projektikansioon palvelimella
cd /var/www/cicd_app

# Hae uusin koodi
git pull

# Päivitä ja käynnistä kontit
docker compose down
docker compose up -d --build
