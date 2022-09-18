#!/bin/sh



while read -r ln
do
git add $ln

done < <(find ./ -regex '^.*[cs|cshtml|js|razor|json|py|ipynb|csproj|css|html|htm]$'  -type f)
