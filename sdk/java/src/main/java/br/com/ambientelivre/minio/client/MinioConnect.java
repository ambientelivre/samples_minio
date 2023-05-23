package br.com.ambientelivre.minio.client;

import io.minio.MinioClient;

public class MinioConnect {

	public static MinioClient ClientConnection() {

		MinioClient minioClient = MinioClient
				.builder()
				.endpoint("http://10.19.4.160:9000")
				.credentials("systemjava", "Vghm4JXpOBGZSUqHfyk57fwSdbU6qvnM").build();

		return minioClient;
	}
}
