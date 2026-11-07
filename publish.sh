#!/bin/bash
# copy public site files into ./public (served/deployed folder)
cd "$(dirname "$0")" && python3 src/build.py && rm -rf public && mkdir public && cp -r index.html faq.html privacy.html terms.html thank-you.html styles.css main.js favicon.png img public/ && rm -f public/img/logo-source.svg && echo published
