FROM php:8.2-apache

RUN docker-php-ext-install pdo pdo_mysql mysqli

RUN a2enmod rewrite

COPY php.ini /usr/local/etc/php/php.ini

EXPOSE 80
