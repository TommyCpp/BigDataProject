package com.bigdata.controller.CollectBehavior;


import com.bigdata.model.UserBehavior.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class CollectUrlBehaviorController {

    @Autowired
    private UrlBehaviorRepository urlBehaviorRepository;
    private Value value;

    @PostMapping("/url")
    public @ResponseBody
    String addNewUrlBehavior(@RequestBody Message message){
        value = message.getValue();
        UrlBehavior behavior = new UrlBehavior(value);
        urlBehaviorRepository.save(behavior);
        return "Save";
    }


    @GetMapping(path="/url/all")
    public @ResponseBody Iterable<UrlBehavior> getAllUrlBehavior() {
        // This returns a JSON or XML with the users
        return urlBehaviorRepository.findAll();
    }
}
