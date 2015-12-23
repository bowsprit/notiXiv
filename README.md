# NotiXiv

This program is designed to produce targeted notifications of new additions to the article preprint
repository [www.arXiv.org](http://arxiv.org/).  Users will be able to subscribe to notifications
for articles released based on numerous articles attributes, including: author, institution, tags,
title-keywords, abstract-keywords, or citations to particular articles.

*Future: Additional data can also be gathered daily from the arXiv for any future analysis or data
products.*


## Structure
-   #### Frontend
    +   **API**: to manage user-subscription and notification information (i.e. to interact with
        backend).
    +   **Website**: interface to the API, for user-subscription management.
    +   **Notifications**: E-Mail, RSS, etc based daily notifications of subscription results.
-   #### Backend
    +   **Databases**: store user and subscription information.
    +   **Scraping**: gather and analyze daily arXiv publications.


## Databases
### Users  
Database for subscribed user information and their notification filters.

#### *Articles*
*If article data is collected daily, an additional database will be needed to store and access it.*
