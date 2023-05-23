package br.com.ambientelivre.minio.samples;

import io.minio.BucketExistsArgs;
import io.minio.errors.MinioException;
import java.io.IOException;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;

public class BucketExists {

	public static void main(String[] args)
      throws IOException, NoSuchAlgorithmException, InvalidKeyException {
    try {
    	
      boolean found = 
    	MinioConnect.ClientConnection()
    			.bucketExists(
    					BucketExistsArgs
    					.builder()
    					.bucket("myfirstbucket")
    					.build()
    			);
      if (found) {
        System.out.println("myfirstbucket existe");
      } else {
        System.out.println("myfirstbucket não existe");
      }
    } catch (MinioException e) {
      System.out.println("Ocorreu um erro: " + e);
    }
  }
}