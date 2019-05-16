FROM python:3.7-alpine

LABEL maintainer xiaohui.c.liu@accenture.com

WORKDIR /var/www


RUN apk --update add python3-dev build-base linux-headers pcre-dev uwsgi-python3
RUN pip install -U setuptools pip && pip install uwsgi pipenv 
RUN pip install nose
RUN pip install pytest-cov
# ENV USER=pythonuser
# RUN addgroup -g 1000 $USER && \ 
#     adduser -D -u 1000 -G $USER $USER
# USER $USER

COPY requirement.txt /var/www/requirement.txt
RUN pip install -r requirement.txt

COPY uwsgi.ini /var/www/uwsgi.ini
COPY src /var/www/src
COPY tests /var/www/tests

#unit test
RUN mkdir /var/www/coverage-reports
RUN mkdir /var/www/xunit-reports
# Here please be noticed that
# The source path in generated report must be same as where you are now:
# Example: 
# C:\Hunter\workspace-python\python-pipeline-2\src\main.py
# C:\Hunter\workspace-python\python-pipeline-2\tests\test.py
# The report you generated must be like this
#<sources>
#  <source>C:\Hunter\workspace-python\python-pipeline-2</source>
#</sources>
# but cannot like this:
#<sources>
#  <source>C:\Hunter\workspace-python\python-pipeline-2\src</source>
#</sources>
# it is decided by --cover-package=. or --cover-package=src
RUN nosetests --xunit-file=xunit-reports/xunit-result-nose.xml --with-xunit --with-coverage --cover-xml --cover-xml-file=coverage-reports/coverage-nose.xml --cover-package=.

EXPOSE 8080

CMD ["uwsgi", "--thunder-lock", "--ini", "/var/www/uwsgi.ini"]