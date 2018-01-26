grep -rlis "gmail.com" --include="*.csv" --include="*.xls*" --include="*.sql" --include="*.db"  --include="*.txt" --include="*.xml" >> resultat_datafiles.txt
temp=$(date +%Y%m%d-%H%M)
mkdir -p /var/RGPD/quarantaine/$temp
while read line
do
   mv "$line" /var/RGPD/quarantaine/$temp
done < resultat_datafiles.txt
 
