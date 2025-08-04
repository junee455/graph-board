FROM nginx:alpine

ARG CONF_TEMPLATE_FILE

# Remove default config and copy ours
RUN rm /etc/nginx/conf.d/default.conf

COPY ${CONF_TEMPLATE_FILE} /etc/nginx/nginx.conf.template
COPY entrypoint.sh /etc/entrypoint.sh

ENTRYPOINT /etc/entrypoint.sh