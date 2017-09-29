**prerequisites: python2.7, phantomjs, BeautifulSoup, urllib2
*** tested ONLY on mac os x Sierra! experimental code, just for research purposes. 
### Note: Google’s web crawler can bypass the paywall.

<img src="https://cointelegraph.com/images/725_Ly9jb2ludGVsZWdyYXBoLmNvbS9zdG9yYWdlL3VwbG9hZHMvdmlldy83MTNmNzk1YTEwZDJjZmM1MzExOTJlYmFlNjRjM2JjOS5qcGc=.jpg" alt="wolfiecindysmile" style="width:304px;height:228px;">


quick documentation:

1. links.txt - provide URLs to articles for download + first URL is a dummy link(bug in the code) and wont be downloaded
2. savingUrlAsPdf.js - with phantomjs saves articles as pdf with a random user agent
3. email-hackedcom.py  - sends pdfs from folder to hardcoded email address
4. 

- before running script edit some code:
      in runScript.sh -> “path_to_URLs.txt”
      in savingUrlsAsPdf -> “path_to_articles_folder"
      in email-hackedcom.py -> add friends emails, add your email addr. + password, subject to email, path
- second, go to WEBSITE_OF_YOUR_CHOICE for some interesting article and copy the google ”cached URL"
  to the links.txt.
- run runScript.sh in terminal.

*optional: delete 2 rows in the runScript.sh if you dont want to send the files as a emails to "friends".
