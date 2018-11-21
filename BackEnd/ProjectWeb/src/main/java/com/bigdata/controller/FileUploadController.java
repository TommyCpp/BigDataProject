package com.bigdata.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.servlet.ModelAndView;

import java.io.*;

@Controller
public class FileUploadController {

    //http://ip:port/upload
    @RequestMapping(value="/")
    public String upload(){
        return "uploadForm";
    }

    @RequestMapping(value="/uploadfile", method = RequestMethod.POST)
    public String upload(@RequestParam("file") MultipartFile file){
        if(!file.isEmpty()){
            try{
                BufferedOutputStream out = new BufferedOutputStream(
                        new FileOutputStream(new File(file.getOriginalFilename())));
                out.write(file.getBytes());
                out.flush();
                out.close();
            } catch (FileNotFoundException e){
                e.printStackTrace();
                return "Failure";
            } catch (IOException e){
                e.printStackTrace();
                return "Failure";
            }
            return "Success";
        } else {
            return "Failure";
        }
    }
}
