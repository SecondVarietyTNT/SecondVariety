#!/bin/sh
docker logout
# я сначала собираю в свой тег , у меня docker.io такой, чтобы копия была
docker build -t gloks3/test:secvar .
sleep 2
#потом его дублирую в образ яндекса
docker tag gloks3/test:secvar cr.yandex/crpk0diklk28mrtmsjsk/secvar
sleep 2
# логинюсь в яндек репозаторий для образов
docker login -u oauth -p AQAAAABcdYjZAATuwd-JYYarG09ftmVQQGoG3G4 cr.yandex/crpk0diklk28mrtmsjsk
#sleep 2
# отправляю образ туда
docker push cr.yandex/crpk0diklk28mrtmsjsk/secvar

#yndex side
#docker stop `docker ps | awk   '/\d/ { print $1 ;}'`
#docker pull cr.yandex/crpb1lc8v34n47e82o1b/grpcserv1
#docker run -d -p 10.129.0.17:5000:5000 cr.yandex/crpb1lc8v34n47e82o1b/grpcserv1
#ssh -i ~/.ssh/yandex yc-user@51.250.109.24 ''
#ssh -i ~/.ssh/yandex yc-user@51.250.109.24 ''
#ssh -i ~/.ssh/yandex yc-user@51.250.109.24 'cd ~; ./dupd.sh'
#cr.yandex/crpb1lc8v34n47e82o1b/grpcserv1
#docker run -d -p 10.129.0.17:5000:5000 cr.yandex/crpb1lc8v34n47e82o1b/grpcserv1
