find . -type f -name "*.zip" >> resultatzip
temp=$(date +%Y%m%d-%H%M)
mkdir -p /var/RGPD/quarantaine/containerfiles/$temp
while read line
do
   mv "$line" /var/RGPD/quarantaine/containerfiles/$temp
done < resultatzip
mv resultatzip /var/RGPD/quarantaine/containerfiles/$temp

