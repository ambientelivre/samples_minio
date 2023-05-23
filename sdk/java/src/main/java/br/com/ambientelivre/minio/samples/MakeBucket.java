package br.com.ambientelivre.minio.samples;

import io.minio.BucketExistsArgs;
import io.minio.MakeBucketArgs;
import io.minio.errors.MinioException;
import java.io.IOException;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;

public class MakeBucket {
  public static void main(String[] args)
      throws IOException, NoSuchAlgorithmException, InvalidKeyException {
    try {


      if (!MinioConnect.ClientConnection().bucketExists(BucketExistsArgs.builder().bucket("myfirstbucket").build())) {
    	  MinioConnect.ClientConnection().makeBucket(MakeBucketArgs.builder().bucket("myfirstbucket").build());
        System.out.println("myfirstbucket criado com sucesso");
      }

    } catch (MinioException e) {
      System.out.println("Error occurred: " + e);
    }
  }
}
