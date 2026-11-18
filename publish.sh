#!/bin/bash
# copy public site files into ./public (served/deployed folder)
cd "$(dirname "$0")" && python3 src/build.py && rm -rf public && mkdir public && cp -r index.html faq.html privacy.html terms.html thank-you.html styles.css main.js favicon.png img sitemap.xml robots.txt llms.txt 4a4908844786f95f96070f9223a3aced.txt public/ && for d in sell-my-house-fast-*; do [ -d "$d" ] && cp -r "$d" public/; done && rm -f public/img/logo-source.svg && echo published
