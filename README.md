**prerequisites: python2.7, phantomjs, BeautifulSoup, urllib2
*** tested ONLY on mac os x Sierra!

quick documentation:

1. links.txt - provide links plus 1 extra dummy link manually in txt file
2. savingUrlAsPdf.js - with phantomjs saves articles as pdf with random user agent
3. email-hackedcom.py  - sends pdfs from folder to hardcoded email address


- before running script edit some code:
      in runScript.sh -> “path_to_links.txt”
      in savingUrlsAsPdf -> “path_to_articles_folder"
      in email-hackedcom.py -> add friends emails, add your email addr. + password, subject to email, path
- second, go to hacked.com for some interesting article and copy the google ”cached URL"
 to the links.txt.
- run runScript.sh.

*optional: delete 2 rows if you dont want to send emails to friends.
