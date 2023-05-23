package br.com.ambientelivre.minio.samples;

import io.minio.PutObjectArgs;
import io.minio.errors.MinioException;
import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;
import java.util.HashMap;
import java.util.Map;

public class PutObject {

	public static void main(String[] args)
      throws IOException, NoSuchAlgorithmException, InvalidKeyException {
    try {
    	

      StringBuilder builder = new StringBuilder();
      for (int i = 0; i < 1000; i++) {
        builder.append(
            "Sphinx of black quartz, judge my vow: Used by Adobe InDesign to display font samples. ");
        builder.append("(29 letters)\n");
        builder.append(
            "Jackdaws love my big sphinx of quartz: Similarly, used by Windows XP for some fonts. ");
        builder.append("(31 letters)\n");
        builder.append(
            "Pack my box with five dozen liquor jugs: According to Wikipedia, this one is used on ");
        builder.append("NASAs Space Shuttle. (32 letters)\n");
        builder.append(
            "The quick onyx goblin jumps over the lazy dwarf: Flavor text from an Unhinged Magic Card. ");
        builder.append("(39 letters)\n");
        builder.append(
            "How razorback-jumping frogs can level six piqued gymnasts!: Not going to win any brevity ");
        builder.append("awards at 49 letters long, but old-time Mac users may recognize it.\n");
        builder.append(
            "Cozy lummox gives smart squid who asks for job pen: A 41-letter tester sentence for Mac ");
        builder.append("computers after System 7.\n");
        builder.append(
            "A few others we like: Amazingly few discotheques provide jukeboxes; Now fax quiz Jack! my ");
        builder.append("brave ghost pled; Watch Jeopardy!, Alex Trebeks fun TV quiz game.\n");
        builder.append("---\n");
      }

      {

    	  ByteArrayInputStream bais = new ByteArrayInputStream(builder.toString().getBytes("UTF-8"));

    	  MinioConnect.ClientConnection().putObject(
            PutObjectArgs.builder().bucket("myfirstbucket").object("myfirstobject").stream(
                    bais, bais.available(), -1)
                .build());
        bais.close();
        System.out.println("myfirstobject foi carregado com sucesso");
      }


      {
        ByteArrayInputStream bais = new ByteArrayInputStream(builder.toString().getBytes("UTF-8"));

        Map<String, String> headers = new HashMap<>();
        headers.put("Content-Type", "application/octet-stream");
        headers.put("X-Amz-Storage-Class", "REDUCED_REDUNDANCY");

        Map<String, String> userMetadata = new HashMap<>();
        userMetadata.put("MyProject", "Project Minio");

        MinioConnect.ClientConnection().putObject(
            PutObjectArgs.builder().bucket("myfirstbucket").object("myfirstobject").stream(
                    bais, bais.available(), -1)
                .headers(headers)
                .userMetadata(userMetadata)
                .build());
        bais.close();
        System.out.println("myfirstobject foi carregado com sucesso");
      }

    } catch (MinioException e) {
      System.out.println("Error occurred: " + e);
    }
  }
}
