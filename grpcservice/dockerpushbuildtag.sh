#!/bin/sh
docker logout
docker build -t gloks3/test:grpcserv1 .
docker tag gloks3/test:grpcserv1 cr.yandex/crpb1lc8v34n47e82o1b/grpcserv1
docker login -u oauth -p AQAAAABcdYjZAATuwd-JYYarG09ftmVQQGoG3G4 cr.yandex/crpk0diklk28mrtmsjsk
docker push cr.yandex/crpb1lc8v34n47e82o1b/grpcserv1
#yndex side
#docker stop `docker ps | awk   '/\d/ { print $1 ;}'`
#docker pull cr.yandex/crpb1lc8v34n47e82o1b/grpcserv1
#docker run -d -p 10.129.0.17:5000:5000 cr.yandex/crpb1lc8v34n47e82o1b/grpcserv1
#ssh -i ~/.ssh/yandex yc-user@51.250.109.24 ''
#ssh -i ~/.ssh/yandex yc-user@51.250.109.24 ''
#ssh -i ~/.ssh/yandex yc-user@51.250.109.24 'cd ~; ./dupd.sh'
#cr.yandex/crpb1lc8v34n47e82o1b/grpcserv1
#docker run -d -p 10.129.0.17:5000:5000 cr.yandex/crpb1lc8v34n47e82o1b/grpcserv1