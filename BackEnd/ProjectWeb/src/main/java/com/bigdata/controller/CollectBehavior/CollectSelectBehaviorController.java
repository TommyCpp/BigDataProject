package com.bigdata.controller.CollectBehavior;

import com.bigdata.model.UserBehavior.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class CollectSelectBehaviorController {

    @Autowired
    private SelectBehaviorRepository selectBehaviorRepository;
    private Value value;


    @PostMapping("/select")
    public @ResponseBody String addNewSelectBehavior(@RequestBody Message message){
        value = message.getValue();
        SelectBehavior behavior = new SelectBehavior(value);
        selectBehaviorRepository.save(behavior);
        return "Save";
    }



    @GetMapping(path="/select/all")
    public @ResponseBody Iterable<SelectBehavior> getAllSelectBehavior() {
        // This returns a JSON or XML with the users
        return selectBehaviorRepository.findAll();
    }

}
