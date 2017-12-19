**prerequisites: python2.7, phantomjs, BeautifulSoup, urllib2
*** tested ONLY on mac os x Sierra! experimental code, for research purposes only. 
### Note: Google’s web crawler can bypass some paywalls.

<img src="https://cointelegraph.com/images/725_Ly9jb2ludGVsZWdyYXBoLmNvbS9zdG9yYWdlL3VwbG9hZHMvdmlldy9jYTU2MmQxZDQ4MmE0MmE1M2Q5MjgyNzM5Nzg1YTMyMS5qcGc=.jpg" alt="wolfiecindysmile" style="width:304px;height:228px;">


quick documentation:

1. links.txt - paste here the article URLs (the first URL is a dummy link(bug in the code) and wont be downloaded so paste a random URL)
2. savingUrlAsPdf.js - using phantomjs, we save the articles as pdf (be every call we use a random user agent for more anonymity)
3. email-article.py  - we send the articles(pdfs) to all the email addresses inside the email-article.py (note: add you own emails)
 

- before running script edit some code:
      in runScript.sh -> “path_to_URLs.txt”
      in savingUrlsAsPdf -> “path_to_articles_folder"
      in email-article.py -> add friends emails, add your email addr. + password, subject to email, path
- second, go to WEBSITE_OF_YOUR_CHOICE for some interesting article and copy the google ”cached URL"
  to the links.txt.
- run runScript.sh in terminal.

*optional: delete 2 rows in the runScript.sh if you dont want to send the files as a emails to "friends".
