FROM minio/minio

MAINTAINER Alix de Langlais

#RUN \
#	docker run -p 9000:9000 \ 
#	-e "MINIO_ACCESS_KEY=AKIAIOSFODNN7EXAMPLE" \
#	-e "MINIO_SECRET_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY" \
#	minio/minio server /data


# Changement du répertoire courant
#WORKDIR /Documents/minio

COPY ./docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh


#ENTRYPOINT ["/docker-entrypoint.sh"]

EXPOSE 9000

CMD ["minio"]
