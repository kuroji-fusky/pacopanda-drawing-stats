#!/bin/bash

git clone --depth 1 https://github.com/supabase/supabase
cd supabase/docker

cp .env.example .env

docker compose up
