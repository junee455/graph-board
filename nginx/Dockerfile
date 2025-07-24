FROM nginx:alpine

# Remove default config and copy ours
RUN rm /etc/nginx/conf.d/default.conf

COPY nginx-dev.conf /etc/nginx/nginx.conf
