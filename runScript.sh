#!/bin/sh
 #echo "first --> downloading URLs"

echo "Looping trough provided URLs begins!"

 i=1; #global variable used inside loop
 #looping trough provided links in links.txt
 # NOTICE - add an extra dummy link because last element in Txt is ignored and it doesnt save all the links as pdf!
while read p; do
         echo "Saving $i. HTML article to Pdf with phantomjs"
         phantomjs "PATH_TO_savingUrlAsPdf.js" $p "$i.pdf"
         ((i+=1));

        sleep .$[ ( $RANDOM % 25) ]s #sleeps random between 1-25 seconds
done <"PATH_TO_URLS.txt"


echo "Now sending PDFs to friends with python"
python "PATH_TO_email-hackedcom.py"




