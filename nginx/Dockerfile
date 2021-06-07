FROM nginx:1.19.0


RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d

COPY proxy_params.conf /etc/nginx/conf.d/proxy_params.conf