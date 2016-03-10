FROM python:2-onbuild
MAINTAINER quinn.thomson@robotsandpencils.com
WORKDIR /usr/src/app

# use this to test a SLACK_TOKEN environment variable
# ENV SLACK_TOKEN ###token###

CMD python run.py
