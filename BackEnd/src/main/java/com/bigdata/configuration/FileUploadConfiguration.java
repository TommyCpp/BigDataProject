package com.bigdata.configuration;

import org.springframework.boot.web.servlet.MultipartConfigFactory;
import org.springframework.context.annotation.Bean;

import javax.servlet.MultipartConfigElement;

public class FileUploadConfiguration {

    @Bean
    public MultipartConfigElement multipartConfigElement() {
        MultipartConfigFactory factory = new MultipartConfigFactory();
        //The Memory Size
        factory.setMaxFileSize("10000MB");
        factory.setMaxRequestSize("10000MB");
        //factory.setLocation("address")
        return factory.createMultipartConfig();
    }
}
