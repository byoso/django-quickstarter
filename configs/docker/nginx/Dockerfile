FROM nginxinc/nginx-unprivileged:1.23.2-alpine


RUN rm /etc/nginx/conf.d/default.conf

COPY configs/docker/nginx/* /etc/nginx/
# COPY configs/docker/nginx/default-ssl.conf.tpl /etc/nginx/conf.d/
COPY configs/docker/nginx/run.sh /run.sh

ENV APP_HOST=web
ENV APP_PORT=8000

USER root

RUN apk add --update --no-cache openssl bash
RUN chmod +x /run.sh

VOLUME /vol/staticfiles
VOLUME /vol/mediafiles
VOLUME /vol/www

# RUN mkdir -p /vol/staticfiles
# RUN mkdir -p /vol/mediafiles
# RUN chmod 755 /vol/staticfiles
# RUN chmod 755 /vol/mediafiles

# USER nginx

CMD ["sh","/run.sh"]
