
# FROM nginx:1.23.2-alpine
FROM nginxinc/nginx-unprivileged:1.23.2-alpine


# RUN rm /etc/nginx/conf.d/default.conf

COPY configs/docker/nginx/nginx.conf /etc/nginx/conf.d/default.conf
COPY configs/docker/nginx/uwsgi_params /etc/nginx/uwsgi_params

USER root

RUN mkdir -p /staticfiles
RUN mkdir -p /mediafiles
RUN chmod 755 /staticfiles
RUN chmod 755 /mediafiles

USER nginx
