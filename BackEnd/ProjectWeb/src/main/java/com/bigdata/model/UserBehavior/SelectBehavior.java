package com.bigdata.model.UserBehavior;


import javax.persistence.*;
import java.util.Date;

@Entity
public class SelectBehavior extends Value{

    @Id
    @GeneratedValue(strategy=GenerationType.AUTO)
    private Integer id;
    private String username;
    private String type;
    private String text;
    private Date timestamp;


    public SelectBehavior() {
    }

    public SelectBehavior(Value value){
        this.username = value.getUsername();
        this.type = value.getType();
        this.text = value.getText();
        this.timestamp = value.getTimestamp();
    }

    public SelectBehavior(String username, String type, String text, Date timestamp) {
        this.username = username;
        this.type = type;
        this.text = text;
        this.timestamp = timestamp;
    }

}
