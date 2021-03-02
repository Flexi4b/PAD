FROM centos:latest

RUN yum -y install httpd

COPY index.html /var/www/html/

COPY challenge_1.html /var/www/html/

COPY challenge_start.html /var/www/html/

COPY admin.html /var/www/html/

COPY login.html /var/www/html/

COPY admin_logo.png /var/www/html/

COPY sidebar.js /var/www/html/

COPY style.css /var/www/html/

COPY admin.css /var/www/html/

COPY Challenge_1.css /var/www/html/

COPY PAD_CSS.css /var/www/html/

CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]

EXPOSE 80