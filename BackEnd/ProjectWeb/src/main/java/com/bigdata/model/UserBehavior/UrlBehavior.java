package com.bigdata.model.UserBehavior;


import javax.persistence.*;
import java.util.Date;

@Entity
public class UrlBehavior extends Value{

    @Id
    @GeneratedValue(strategy=GenerationType.AUTO)
    private Integer id;
    private String username;
    private String type;
    private String url;
    private Date timestamp;


    public UrlBehavior() {

    }

    public UrlBehavior(Value value){
        this.username = value.getUsername();
        this.type = value.getType();
        this.url = value.getText();
        this.timestamp = value.getTimestamp();
    }

    public UrlBehavior(String username, String type, String text, Date timestamp) {
        this.username = username;
        this.type = type;
        this.text = text;
        this.timestamp = timestamp;
    }

}