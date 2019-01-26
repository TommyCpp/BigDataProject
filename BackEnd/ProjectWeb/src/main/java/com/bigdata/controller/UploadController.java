package com.bigdata.controller;

import com.bigdata.model.MyData;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.atomic.AtomicLong;

@RestController
public class UploadController {
    private List<MyData> datas = new ArrayList<>();
    private AtomicLong nextId = new AtomicLong();

    @GetMapping("/hello")
    public String getHelloMessage(){
        return "hello";
    }

    @PostMapping("/data")
    public MyData createNewUpload(@RequestBody MyData mydata){
        mydata.setId(nextId.incrementAndGet());
        datas.add(mydata);
        return mydata;
    }
}
