package com.bigdata.controller.CollectBehavior;

import com.bigdata.model.UserBehavior.Behavior;
import com.bigdata.model.UserBehavior.BehaviorRepository;
import com.bigdata.model.UserBehavior.ReturnValue;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class CollectBehaviorController {

    @Autowired
    private BehaviorRepository behaviorRepository;

    @PostMapping("/collect")
    public @ResponseBody String addNewBehavior(@RequestBody ReturnValue returnValue){
        Behavior behavior = returnValue.getValue();
        behaviorRepository.save(behavior);
        return "Save";
    }

    @GetMapping(path="/collect/all")
    public @ResponseBody Iterable<Behavior> getAllUsers() {
        // This returns a JSON or XML with the users
        return behaviorRepository.findAll();
    }
}
