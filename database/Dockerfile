FROM postgres:latest
ENV POSTGRES_PASSWORD=secret
ENV POSTGRES_USER=username
ENV POSTGRES_DB=database
COPY init_script.sql /docker-entrypoint-initdb.d/init_script.sql