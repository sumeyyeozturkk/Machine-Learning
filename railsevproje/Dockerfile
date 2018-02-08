FROM ruby:2.4.1
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev nodejs
RUN mkdir /railsfiyat
WORKDIR /railsfiyat
ADD Gemfile /railsfiyat/Gemfile
ADD Gemfile.lock /railsfiyat/Gemfile.lock
RUN bundle install
ADD . /railsfiyat