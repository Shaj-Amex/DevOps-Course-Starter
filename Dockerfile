# Create Python Image
FROM python:3.8.4-buster as Base

# Install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

ENV PATH="${PATH}:/root/.poetry/bin"

# Create Workdir & Copy the Code
WORKDIR /DevOps-Course-Starter
COPY . /DevOps-Course-Starter

# Expose the Port
EXPOSE 5000

FROM base as development


RUN poetry install
ENTRYPOINT [ "poetry", "run", "flask", "run", "--port", "5000" , "--host", "0.0.0.0"]

FROM base as production

ENV FLASK_ENV=production
RUN poetry install --no-dev
RUN poetry add gunicorn
ENTRYPOINT ["poetry", "run", "gunicorn", "--bind", "0.0.0.0:5000", "todo_app.app:app"]

FROM base as test 
ENV FLASK_ENV=development
RUN poetry install
# Install Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
  && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
  && apt-get update -qqy \
  && apt-get -qqy install \
    ${CHROME_VERSION:-google-chrome-stable} \
  && rm /etc/apt/sources.list.d/google-chrome.list \
  && rm -rf /var/lib/apt/lists/* /var/cache/apt/*


#RUN curl -sSL https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o chrome.deb &&\
#    apt-get install ./chrome.deb -y &&\
#    rm ./chrome.deb
# Install Chromium WebDriver
# Source https://github.com/SeleniumHQ/docker-selenium/blob/trunk/NodeChrome/Dockerfile

RUN CHROME_MAJOR_VERSION=$(google-chrome --version | sed -E "s/.* ([0-9]+)(\.[0-9]+){3}.*/\1/") \
  && CHROME_DRIVER_VERSION=$(wget --no-verbose -O - "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_${CHROME_MAJOR_VERSION}") \
  && echo "Using chromedriver version: "$CHROME_DRIVER_VERSION \
  && wget --no-verbose -O /tmp/chromedriver_linux64.zip https://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip \
  && rm -rf /opt/selenium/chromedriver \
  && unzip /tmp/chromedriver_linux64.zip -d /opt/selenium \
  && rm /tmp/chromedriver_linux64.zip \
  && mv /opt/selenium/chromedriver /opt/selenium/chromedriver-$CHROME_DRIVER_VERSION \
  && chmod 755 /opt/selenium/chromedriver-$CHROME_DRIVER_VERSION \
  && ln -fs /opt/selenium/chromedriver-$CHROME_DRIVER_VERSION /usr/bin/chromedriver

  #COPY /usr/bin/chromedriver


# Below Code Not Working
#RUN LATEST=`curl -sSL https://chromedriver.storage.googleapis.com/LATEST_RELEASE` &&\
#    echo "Installing chromium webdriver version ${LATEST}" &&\
#    curl -sSL https://chromedriver.storage.googleapis.com/${LATEST}/chromedriver_linux64.zip -o chromedriver_linux64.zip &&\
#   apt-get install unzip -y &&\
#    unzip ./chromedriver_linux64.zip
RUN export PATH=$PATH:/usr/bin/chromedriver

ENTRYPOINT ["poetry", "run", "pytest"]