# Building a Sustainable Package Index

"it is pronounced Pie-Pea-Eye"

## What is PyPI?

-   The canonical repository for software in python
-   Old - has been around for quite a while (2002)
    -   PyPI did not exist when Python was frist created

## What isnt PyPI?

-   A collectoin of audited software (the wild west)
    -   Anyone can publish anything
-   Github
-   A for profit organisation

## How to build a PyPI

1.  -   Define Some APIs
    -   Upload API
    -   JSON/XML-RPC Apis

2.  -   Implement in Python
3.  -   Put all in a CDN
    -   Very popular (6-7k requests received per second)
    -   Mirror size around 7TB
4.  Try to make all that sustainable
5.  Hope you break even

## About Sustainibility

-   Vital part of the python ecosystem
-   Needs:
    -   Longevity
    -   Mantainable
    -   Transparency
    -   Evolvability
    -   Scalability
-   Built with Python 3 (using latest and greatest technology)
    -   But not using anythign too weird
-   Everything is open source
-   Strong local development experience
    -   Can get a version running on Docker almost instantly on a local machine
-   Test!
    -   Prevent from breaking things moving forward
    -   100% test coverage
        -   Cannot get pull request without 100% test coverage
        -   While this slows down feature development, increases stabilty
-   Resiiliant to downtime
    -   99% of all requests hit the CDN - so can take down the backend without issue

## Organisational Sustainability

-   PyPI is a project of the Python Software Foundation, a non profit
-   PyPI iis run (almost entirely) by volunteers
    -   200 contributers working for free to improve the software

## Financial Sustainablity

-   Accepts donations (organisations + individuals, although individual contributions make up a negligible amount)
-   Grants & awards
    -   Was not doing this a year ago
    -   Mozilla has an open source award - which they won
    -   This allowed them to hire 4 employees and do a full rewrite of the backend code (with some frontend polish as well!)
-   OpenWebFoundation
    -   Allowed for security + accessibilty featuers

## Do you want a for profit PyPI?

-   Challenge - donated services
-   Current ecosystem
-   Volunteers
-   The transition

## Do you want more sustainability

-   Donate money
-   Donate time
    -   github.com/pypa/warehouse
